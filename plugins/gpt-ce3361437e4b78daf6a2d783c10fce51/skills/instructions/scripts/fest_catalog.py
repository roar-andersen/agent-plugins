#!/usr/bin/env python3
"""Local FEST 2.5.1 download, import and search. Python 3.10+, standard library."""
import argparse
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import tempfile
import unicodedata
import urllib.request
import urllib.error
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import zipfile

NS = "http://www.kith.no/xmlstds/eresept/m30/2014-12-01"
SOURCE_PAGE = "https://www.dmp.no/om-oss/distribusjon-av-legemiddeldata/fest/nedlasting-av-fest-og-safest"
BASE = "https://www.dmp.no/globalassets/documents/om-oss/distribusjon-av-legemiddeldata/fest/festfiler/"
URLS = {"rekvirent": BASE + "fest251.zip", "institusjon": BASE + "fest251_inst.zip", "veterinaer": BASE + "fest251_vet.zip"}
DATASETS = tuple(URLS) + ("bandasjist", "nav", "farmalogg")
MAX_BYTES = 2 * 1024**3
INDEX_VERSION = 1


def local(tag):
    return tag.rsplit("}", 1)[-1]


def normalize(value):
    value = unicodedata.normalize("NFKD", value.casefold())
    return "".join(c for c in value if not unicodedata.combining(c))


def config_path():
    base = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / ".config")))
    return base / "Fest251Expert" / "settings.json"


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".fest-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def read_config(path):
    if not path.exists():
        return {"version": 1, "datasets": {}}
    result = json.loads(path.read_text(encoding="utf-8"))
    if result.get("version") != 1:
        raise ValueError("Ukjent oppsettsversjon.")
    return result


class SafeXML:
    """Reject declarations, including UTF-16 encodings, before parsing each chunk."""
    def __init__(self, stream):
        self.stream = stream
        self.tail = b""

    def read(self, size=-1):
        chunk = self.stream.read(size)
        scan = (self.tail + chunk).replace(b"\x00", b"").upper()
        if b"<!DOCTYPE" in scan or b"<!ENTITY" in scan:
            raise ValueError("DTD og entity-deklarasjoner er ikke tillatt i FEST-filer.")
        self.tail = (self.tail + chunk)[-64:]
        return chunk


def copy_bounded(source, destination):
    digest = hashlib.sha256()
    total = 0
    with open(destination, "wb") as output:
        while True:
            chunk = source.read(1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if total > MAX_BYTES:
                raise ValueError("Filen overskrider grensen på 2 GiB.")
            digest.update(chunk)
            output.write(chunk)
    return digest.hexdigest(), total


def download(url, destination):
    # Only the verified, public production URLs; no local-file or arbitrary URL fetches.
    if url not in URLS.values():
        raise ValueError("Ukjent nedlastingsadresse.")
    request = urllib.request.Request(url, headers={"User-Agent": "FEST-251-Expert/0.2.0"})
    with urllib.request.urlopen(request, timeout=90) as response:
        final = urlparse(response.url)
        if final.scheme != "https" or final.hostname not in {"www.dmp.no", "dmp.no"}:
            raise ValueError("DMP videresendte til en ukjent vert. Kontroller kilden før oppdatering.")
        return copy_bounded(response, destination)


def unpack_xml(archive, destination):
    with zipfile.ZipFile(archive) as zipped:
        members = [m for m in zipped.infolist() if not m.is_dir() and m.filename.lower().endswith(".xml")]
        if len(members) != 1:
            raise ValueError("ZIP-filen må inneholde nøyaktig én XML-fil.")
        member = members[0]
        # Extract to our own fixed name, never to a filename supplied by the archive.
        if member.file_size > MAX_BYTES or member.file_size / max(member.compress_size, 1) > 2000:
            raise ValueError("ZIP-filen overskrider tillatt størrelse eller komprimeringsforhold.")
        with zipped.open(member) as stream:
            return copy_bounded(stream, destination)


def index_xml(xml_path, db_path, extract="full"):
    counts = {}
    status_counts = {}
    hentet = None
    depth = -1
    catalog = None
    root = None
    catalog_node = None
    with closing(sqlite3.connect(db_path)) as db:
        db.executescript("""
            CREATE TABLE entries(rowid INTEGER PRIMARY KEY, catalog TEXT, entry_id TEXT UNIQUE,
                object_id TEXT, status TEXT, title TEXT, xml TEXT, search TEXT);
            CREATE INDEX object_ids ON entries(object_id);
            CREATE TABLE refs(entry_rowid INTEGER, target_id TEXT, element TEXT);
            CREATE INDEX ref_target ON refs(target_id);
            CREATE VIRTUAL TABLE search_index USING fts5(search, content='entries', content_rowid='rowid');
            CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT);
        """)
        with open(xml_path, "rb") as stream:
            for event, node in ET.iterparse(SafeXML(stream), events=("start", "end")):
                if event == "start":
                    depth += 1
                    if depth == 0:
                        root = node
                        if node.tag != "{" + NS + "}FEST":
                            raise ValueError("Filen er ikke FEST 2.5.1 med forventet M30-namespace.")
                    elif depth == 1:
                        catalog = local(node.tag) if local(node.tag).startswith("Kat") else None
                        catalog_node = node
                        if catalog:
                            counts[catalog] = 0
                    continue
                if depth == 1 and local(node.tag) == "HentetDato":
                    hentet = (node.text or "").strip()
                if depth == 2 and catalog:
                    if not local(node.tag).startswith("Oppf"):
                        raise ValueError("Uventet katalogstruktur.")
                    entry_id = None
                    status = None
                    payload = None
                    for child in node:
                        name = local(child.tag)
                        if name == "Id":
                            entry_id = child.text
                        elif name == "Status":
                            status = child.attrib.get("V")
                        elif name != "Tidspunkt":
                            payload = child
                    if not entry_id or status not in {"A", "U"}:
                        raise ValueError("Oppføring mangler Id eller har ukjent status.")
                    if extract == "full" and status == "U":
                        raise ValueError("Filen inneholder utgåtte oppføringer; registrer den som inkrement.")
                    object_id = next(((c.text or "").strip() for c in (payload if payload is not None else []) if local(c.tag) == "Id"), None)
                    parts = []
                    title = None
                    for child in node.iter():
                        if child.text and child.text.strip():
                            parts.append(child.text.strip())
                            if title is None and local(child.tag) in {"NavnFormStyrke", "Varenavn", "Navn", "Varenr", "Varenummer"}:
                                title = child.text.strip()
                        parts.extend(child.attrib.values())
                    text = normalize(" ".join(parts))
                    cursor = db.execute("INSERT INTO entries(catalog,entry_id,object_id,status,title,xml,search) VALUES(?,?,?,?,?,?,?)",
                        (catalog, entry_id.strip(), object_id, status, title or object_id or entry_id,
                         ET.tostring(node, encoding="unicode"), text))
                    for child in node.iter():
                        if local(child.tag).startswith("Ref") and child.text:
                            for target in child.text.split():
                                db.execute("INSERT INTO refs VALUES(?,?,?)", (cursor.lastrowid, target, local(child.tag)))
                    counts[catalog] += 1
                    status_counts[status] = status_counts.get(status, 0) + 1
                    node.clear()
                    catalog_node.remove(node)
                if depth == 1:
                    node.clear()
                    root.remove(node)
                    catalog = None
                depth -= 1
        if not hentet or not counts or not sum(counts.values()):
            raise ValueError("Filen mangler HentetDato eller inneholder ingen oppføringer.")
        from datetime import datetime
        datetime.fromisoformat(hentet.replace("Z", "+00:00"))
        metadata = {"hentet_dato": hentet, "namespace": NS, "catalog_counts": counts,
            "status_counts": status_counts, "extract": extract, "index_version": INDEX_VERSION,
            "validation": "XML lest; ikke XSD-validert"}
        db.execute("INSERT INTO search_index(search_index) VALUES('rebuild')")
        db.executemany("INSERT INTO metadata VALUES(?,?)", ((k, json.dumps(v, ensure_ascii=False)) for k, v in metadata.items()))
        db.commit()
    return metadata


def import_file(config, config_file, directory, dataset, file, extract, environment, source_url=None):
    directory = Path(directory).expanduser().resolve()
    directory.mkdir(parents=True, exist_ok=True)
    file = Path(file).resolve()
    if not file.is_file():
        raise ValueError("Kildefilen finnes ikke.")
    if file.stat().st_size > MAX_BYTES:
        raise ValueError("Kildefilen overskrider grensen på 2 GiB.")
    dataset_dir = directory / dataset
    dataset_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".fest-import-", dir=dataset_dir) as staging:
        staging = Path(staging)
        xml_path = staging / "catalog.xml"
        if file.suffix.lower() == ".zip":
            digest, size = unpack_xml(file, xml_path)
            shutil.copyfile(file, staging / "download.zip")
        elif file.suffix.lower() == ".xml":
            with open(file, "rb") as source:
                digest, size = copy_bounded(source, xml_path)
        else:
            raise ValueError("Velg en XML- eller ZIP-fil.")
        previous = config["datasets"].get(dataset)
        if previous and previous.get("sha256") == digest and previous.get("environment") == environment and previous.get("extract") == extract and previous.get("index_version") == INDEX_VERSION and Path(previous["index_path"]).exists() and Path(previous["xml_path"]).exists():
            return {"dataset": dataset, "unchanged": True, **previous}
        metadata = index_xml(xml_path, staging / "index.sqlite", extract)
        # Increment files may be inspected, never replace a complete active dataset.
        if extract != "full":
            raise ValueError("Inkrementer kan ikke registreres som komplett katalog. Bruk fullt uttrekk.")
        if previous and source_url and metadata["hentet_dato"] < previous["hentet_dato"]:
            raise ValueError("Nedlastingen er eldre enn aktiv fil; beholdt eksisterende datagrunnlag.")
        snapshot = dataset_dir / (digest + "-v" + str(INDEX_VERSION))
        # Snapshot names are immutable; context metadata is stored outside the index.
        if not snapshot.exists():
            staging.rename(snapshot)
            staging.mkdir()  # TemporaryDirectory can clean up its original path safely.
        metadata.update({"dataset": dataset, "environment": environment, "sha256": digest,
            "xml_bytes": size, "index_bytes": (snapshot / "index.sqlite").stat().st_size,
            "source_url": source_url, "source_file": str(file) if not source_url else None,
            "xml_path": str(snapshot / "catalog.xml"), "index_path": str(snapshot / "index.sqlite")})
        from datetime import datetime, timezone
        metadata["imported_at"] = datetime.now(timezone.utc).isoformat()
        config["datasets"][dataset] = metadata
        config["directory"] = str(directory)
        atomic_json(config_file, config)
        return metadata


def selected(config, dataset):
    values = list(config.get("datasets", {}).values())
    values = values if dataset == "all" else [v for v in values if v["dataset"] == dataset]
    if not values:
        raise ValueError("Ingen registrert fil for valgt uttrekk. Kjør oppsett eller registrer fil.")
    for value in values:
        if not Path(value["index_path"]).is_file() or not Path(value["xml_path"]).is_file():
            raise ValueError("En registrert fil eller indeks er flyttet eller slettet. Registrer filen på nytt.")
    return values


def connect_readonly(meta):
    return sqlite3.connect(Path(meta["index_path"]).as_uri() + "?mode=ro", uri=True)


def record(meta, row, xml=False):
    result = dict(zip(("rowid", "catalog", "entry_id", "object_id", "status", "title", "xml", "search"), row))
    result.pop("search")
    result.pop("rowid")
    if not xml:
        result.pop("xml")
    result["source"] = {k: meta[k] for k in ("dataset", "environment", "hentet_dato", "xml_path", "sha256", "validation")}
    return result


def search(config, dataset, query, limit, catalog=None):
    tokens = re.findall(r"\w+", normalize(query))
    if not tokens:
        raise ValueError("Oppgi et navn, varenummer, ATC-kode eller en identifikator.")
    # Literal token prefixes only; never accept FTS operators from user text.
    match = " AND ".join('"' + t + '"*' for t in tokens)
    results = []
    total = 0
    sources = selected(config, dataset)
    for meta in sources:
        with closing(connect_readonly(meta)) as db:
            where = "search_index MATCH ? AND e.status='A'"
            args = [match]
            if catalog:
                where += " AND e.catalog=?"
                args.append(catalog)
            total += db.execute("SELECT count(*) FROM search_index JOIN entries e ON e.rowid=search_index.rowid WHERE " + where, args).fetchone()[0]
            rows = db.execute("SELECT e.* FROM search_index JOIN entries e ON e.rowid=search_index.rowid WHERE " + where + " ORDER BY rank LIMIT ?", args + [limit]).fetchall()
            results.extend(record(meta, r) for r in rows)
    return {"query": query, "total": total, "results": results[:limit], "truncated": total > limit,
        "searched_sources": [{k: m[k] for k in ("dataset", "environment", "hentet_dato", "xml_path")} for m in sources],
        "note": "Søker i de valgte lokale uttrekkene. Ingen treff betyr ikke at varen mangler i FEST."}


def get_entry(config, dataset, identifier):
    results = []
    for meta in selected(config, dataset):
        with closing(connect_readonly(meta)) as db:
            rows = db.execute("SELECT * FROM entries WHERE entry_id=? OR object_id=? LIMIT 20", (identifier, identifier)).fetchall()
            results.extend(record(meta, r, True) for r in rows)
    return {"id": identifier, "results": results}


def related(config, dataset, identifier, limit):
    results = []
    for meta in selected(config, dataset):
        with closing(connect_readonly(meta)) as db:
            outgoing = db.execute("SELECT DISTINCT r.target_id,r.element FROM refs r JOIN entries e ON e.rowid=r.entry_rowid WHERE e.entry_id=? OR e.object_id=? LIMIT ?", (identifier, identifier, limit + 1)).fetchall()
            incoming = db.execute("SELECT DISTINCT e.* FROM refs r JOIN entries e ON e.rowid=r.entry_rowid WHERE r.target_id=? LIMIT ?", (identifier, limit + 1)).fetchall()
            resolved = []
            for target, element in outgoing[:limit]:
                rows = db.execute("SELECT * FROM entries WHERE object_id=? OR entry_id=? LIMIT 20", (target, target)).fetchall()
                resolved.append({"element": element, "target_id": target, "entries": [record(meta, r) for r in rows], "resolved": bool(rows)})
            results.append({"dataset": meta["dataset"], "outgoing": resolved, "incoming": [record(meta, r) for r in incoming[:limit]], "truncated": len(outgoing) > limit or len(incoming) > limit})
    return {"id": identifier, "relations": results}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=config_path())
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("status")
    setup = commands.add_parser("setup")
    setup.add_argument("--directory", required=True)
    setup.add_argument("--datasets", nargs="+", choices=URLS, default=list(URLS))
    refresh = commands.add_parser("refresh")
    refresh.add_argument("--datasets", nargs="+", choices=URLS)
    register = commands.add_parser("register")
    register.add_argument("--directory")
    register.add_argument("--file", required=True)
    register.add_argument("--dataset", choices=DATASETS, required=True)
    register.add_argument("--environment", choices=("production", "staging", "test", "unknown"), default="unknown")
    for action in ("search", "get", "related"):
        p = commands.add_parser(action)
        p.add_argument("--dataset", choices=DATASETS + ("all",), required=True)
        if action == "search":
            p.add_argument("--query", required=True)
            p.add_argument("--catalog")
        else:
            p.add_argument("--id", required=True)
        if action != "get":
            p.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)
    config = read_config(args.config)
    if args.command == "status":
        return {"setup_required": not bool(config["datasets"]), "config_path": str(args.config), **config}
    if args.command in {"setup", "refresh"}:
        directory = args.directory if args.command == "setup" else config.get("directory")
        if not directory:
            raise ValueError("Kjør oppsett og velg mappe først.")
        datasets = args.datasets or [d for d in config["datasets"] if d in URLS]
        if not datasets:
            raise ValueError("Ingen uttrekk er valgt for oppdatering.")
        Path(directory).mkdir(parents=True, exist_ok=True)
        results = []
        errors = []
        for dataset in dict.fromkeys(datasets):
            print("Henter og indekserer " + dataset + " ...", file=sys.stderr, flush=True)
            try:
                with tempfile.TemporaryDirectory(prefix=".fest-download-", dir=directory) as temp:
                    archive = Path(temp) / "download.zip"
                    download(URLS[dataset], archive)
                    results.append(import_file(config, args.config, directory, dataset, archive, "full", "production", URLS[dataset]))
            except (OSError, ValueError, ET.ParseError, sqlite3.Error, zipfile.BadZipFile) as error:
                errors.append({"dataset": dataset, "error": str(error), "previous_preserved": dataset in config["datasets"]})
        return {"results": results, "errors": errors, "complete": not errors, "source_page": SOURCE_PAGE}
    if args.command == "register":
        directory = args.directory or config.get("directory")
        if not directory:
            raise ValueError("Oppgi --directory ved første registrering.")
        return import_file(config, args.config, directory, args.dataset, args.file, "full", args.environment)
    if args.command != "get" and not 1 <= args.limit <= 50:
        raise ValueError("Antall treff må være mellom 1 og 50.")
    if args.command == "search":
        return search(config, args.dataset, args.query, args.limit, args.catalog)
    if args.command == "get":
        return get_entry(config, args.dataset, args.id)
    return related(config, args.dataset, args.id, args.limit)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        output = main()
        print(json.dumps(output, ensure_ascii=False, indent=2))
        if isinstance(output, dict) and output.get("complete") is False:
            sys.exit(1)
    except (OSError, ValueError, ET.ParseError, sqlite3.Error, zipfile.BadZipFile) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        sys.exit(1)
