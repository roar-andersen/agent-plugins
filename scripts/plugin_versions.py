"""Validate plugin versions and synchronize both marketplaces. Standard library only."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MARKETS = ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json')
MANIFESTS = ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json')
SEMVER = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z')


def version(value):
    match = SEMVER.fullmatch(value or '')
    if not match:
        raise ValueError(f'Versjonen må være MAJOR.MINOR.PATCH uten suffiks: {value!r}')
    return tuple(map(int, match.groups()))


def bump(value, part):
    major, minor, patch = version(value)
    return '.'.join(map(str, {'major': (major + 1, 0, 0), 'minor': (major, minor + 1, 0),
        'patch': (major, minor, patch + 1)}[part]))


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def git(*args, check=True):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=check)


def catalog():
    markets = {rel: read(ROOT / rel) for rel in MARKETS}
    names = [[e['name'] for e in m['plugins']] for m in markets.values()]
    if any(len(n) != len(set(n)) for n in names) or set(names[0]) != set(names[1]):
        raise ValueError('Marketplace-katalogene må inneholde de samme unike pluginnavnene.')
    result = {}
    for entry in markets[MARKETS[0]]['plugins']:
        source = entry['source']
        if not isinstance(source, dict) or source.get('source') != 'local':
            raise ValueError('Denne versjonskontrollen støtter lokale repo-pluginer.')
        relative = source['path']
        directory = (ROOT / relative).resolve()
        if not relative.startswith('./plugins/') or not directory.is_relative_to(ROOT / 'plugins'):
            raise ValueError('Pluginstien må ligge under ./plugins/.')
        root = read(directory / 'plugin.json')
        if root['name'] != entry['name']:
            raise ValueError('Pluginnavn og marketplace-oppføring er ulike.')
        version(root['version'])
        result[root['name']] = (directory, root)
        other = next(e for e in markets[MARKETS[1]]['plugins'] if e['name'] == root['name'])
        if other['source'] != relative:
            raise ValueError('Marketplace-katalogene må peke på samme pluginmappe.')
    return result, markets


def synchronize(name, value, plugins, markets):
    directory, root = plugins[name]
    for rel in MANIFESTS:
        path = directory / rel
        if path.exists():
            data = read(path)
            if data['name'] != name:
                raise ValueError('Manifestene har ulike navn.')
            data['version'] = value
            write(path, data)
    for rel, market in markets.items():
        for entry in market['plugins']:
            if entry['name'] == name:
                entry['version'] = value
        write(ROOT / rel, market)
    root['version'] = value


def validate(plugins, markets):
    for name, (directory, root) in plugins.items():
        value = root['version']
        for rel in MANIFESTS:
            path = directory / rel
            if path.exists():
                overlay = read(path)
                if overlay['name'] != name or overlay['version'] != value:
                    raise ValueError(f'{name}: manifestene har ulike navn/versjoner.')
        for market in markets.values():
            entry = next(e for e in market['plugins'] if e['name'] == name)
            if entry.get('version') != value:
                raise ValueError(f'{name}: marketplace-versjon avviker fra manifest.')
        if not list((directory / 'skills').glob('*/SKILL.md')):
            raise ValueError(f'{name}: ingen skills funnet.')
        forbidden = [p for p in directory.rglob('*') if p.is_file() and
            (p.suffix.lower() in {'.xml', '.sqlite', '.zip'} or p.name == 'settings.json')]
        if forbidden:
            raise ValueError(f'{name}: lokale kataloger/innstillinger skal ikke publiseres.')


def prepare(base, plugins, markets, auto_patch=False):
    if not base or set(base) == {'0'}:
        return list(plugins)
    git('rev-parse', '--verify', base + '^{commit}')
    released = []
    # Working tree may contain pending changes; comparison includes those, not just HEAD.
    for name, (directory, root) in plugins.items():
        rel = directory.relative_to(ROOT).as_posix()
        old_result = git('show', base + ':' + rel + '/plugin.json', check=False)
        if old_result.returncode:
            released.append(name)
            continue
        old = json.loads(old_result.stdout)
        previous = version(old['version'])
        current = version(root['version'])
        changed = bool(git('diff', '--name-only', base, '--', rel).stdout.strip())
        if current < previous:
            raise ValueError(f'{name}: versjonen kan ikke reduseres.')
        if changed:
            if current == previous:
                if not auto_patch:
                    raise ValueError(f'{name}: innhold endret uten versjonsøkning.')
                synchronize(name, bump(old['version'], 'patch'), plugins, markets)
            released.append(name)
    return released


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Git commit to compare with')
    parser.add_argument('--auto-patch', action='store_true')
    parser.add_argument('--plugin')
    parser.add_argument('--bump', choices=('major', 'minor', 'patch'))
    parser.add_argument('--release-list', type=Path)
    args = parser.parse_args()
    plugins, markets = catalog()
    if bool(args.bump) != bool(args.plugin):
        raise ValueError('Bruk --plugin og --bump sammen.')
    if args.bump:
        if args.plugin not in plugins:
            raise ValueError('Ukjent plugin.')
        synchronize(args.plugin, bump(plugins[args.plugin][1]['version'], args.bump), plugins, markets)
    released = prepare(args.base, plugins, markets, args.auto_patch)
    validate(plugins, markets)
    if args.release_list:
        args.release_list.write_text(''.join(f'{name}-v{plugins[name][1]["version"]}\n' for name in released), encoding='utf-8')
    print(json.dumps({name: data['version'] for name, (_, data) in plugins.items()}, indent=2))


if __name__ == '__main__':
    main()
