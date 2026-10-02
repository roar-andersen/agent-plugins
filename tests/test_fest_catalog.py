import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / 'plugins/fest-251-ekspert/skills/instructions/scripts/fest_catalog.py'
spec = importlib.util.spec_from_file_location('fest_catalog', SCRIPT)
fest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fest)
NS = fest.NS
XML = f'''<FEST xmlns="{NS}"><HentetDato>2026-09-29T08:00:00</HentetDato>
<KatLegemiddelMerkevare><OppfLegemiddelMerkevare><Id>ID_ENTRY1</Id><Tidspunkt>2026-09-01T00:00:00</Tidspunkt><Status V="A"/>
<LegemiddelMerkevare xmlns="http://www.kith.no/xmlstds/eresept/forskrivning/2014-12-01"><Id>ID_OBJECT1</Id><NavnFormStyrke>Prøve tablett 500 mg</NavnFormStyrke><RefVirkestoff>ID_SUBSTANCE</RefVirkestoff></LegemiddelMerkevare></OppfLegemiddelMerkevare></KatLegemiddelMerkevare>
<KatVirkestoff><OppfVirkestoff><Id>ID_ENTRY2</Id><Status V="A"/><Virkestoff><Id>ID_SUBSTANCE</Id><Navn>Prøvestoff</Navn></Virkestoff></OppfVirkestoff></KatVirkestoff></FEST>'''

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name)
        self.config_file = self.path / 'settings.json'
        self.config = {'version': 1, 'datasets': {}}
        self.xml = self.path / 'sample.xml'
        self.xml.write_text(XML, encoding='utf-8')

    def tearDown(self):
        self.temp.cleanup()

    def install(self, file=None, dataset='institusjon'):
        return fest.import_file(self.config, self.config_file, self.path / 'data', dataset, file or self.xml, 'full', 'production')

    def test_search_and_reference_resolution(self):
        self.install()
        hits = fest.search(self.config, 'institusjon', 'prøve 500', 10)
        self.assertEqual(hits['total'], 1)
        self.assertEqual(hits['results'][0]['object_id'], 'ID_OBJECT1')
        self.assertEqual(fest.search(self.config, 'institusjon', 'notfound', 10)['total'], 0)
        item = fest.get_entry(self.config, 'institusjon', 'ID_OBJECT1')['results'][0]
        self.assertIn('forskrivning/2014-12-01', item['xml'])
        relation = fest.related(self.config, 'institusjon', 'ID_OBJECT1', 10)['relations'][0]
        self.assertTrue(relation['outgoing'][0]['resolved'])
        self.assertEqual(relation['outgoing'][0]['entries'][0]['object_id'], 'ID_SUBSTANCE')
        incoming = fest.related(self.config, 'institusjon', 'ID_SUBSTANCE', 10)['relations'][0]['incoming']
        self.assertEqual(incoming[0]['object_id'], 'ID_OBJECT1')

    def test_failed_import_preserves_active_dataset(self):
        self.install()
        before = self.config_file.read_bytes()
        self.xml.write_text(XML.replace(NS, 'wrong-namespace'), encoding='utf-8')
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual(self.config_file.read_bytes(), before)
        self.assertEqual(fest.search(self.config, 'institusjon', '500', 10)['total'], 1)

    def test_idempotent_and_changed_file(self):
        self.install()
        self.assertTrue(self.install()['unchanged'])
        self.xml.write_text(XML.replace('500', '250'), encoding='utf-8')
        self.install()
        self.assertEqual(fest.search(self.config, 'institusjon', '500', 10)['total'], 0)
        self.assertEqual(fest.search(self.config, 'institusjon', '250', 10)['total'], 1)

    def test_zip_never_extracts_supplied_paths(self):
        archive = self.path / 'sample.zip'
        with zipfile.ZipFile(archive, 'w') as zipped:
            zipped.writestr('../../escaped.xml', XML)
        self.install(archive)
        self.assertFalse((self.path.parent / 'escaped.xml').exists())
        self.assertEqual(fest.search(self.config, 'institusjon', '500', 10)['total'], 1)

    def test_dtd_and_increments_are_rejected(self):
        self.xml.write_text('<!DOCTYPE FEST [<!ENTITY x "attack">]>' + XML, encoding='utf-8')
        with self.assertRaises(ValueError):
            self.install()
        self.xml.write_text(XML.replace('V="A"', 'V="U"'), encoding='utf-8')
        with self.assertRaises(ValueError):
            self.install()

    def test_datasets_are_not_merged(self):
        self.install(dataset='institusjon')
        self.xml.write_text(XML.replace('500', '750'), encoding='utf-8')
        self.install(dataset='veterinaer')
        self.assertEqual(fest.search(self.config, 'institusjon', '750', 10)['total'], 0)
        self.assertEqual(fest.search(self.config, 'veterinaer', '750', 10)['total'], 1)

    def test_older_download_does_not_replace_active_dataset(self):
        self.install()
        self.xml.write_text(XML.replace('2026-09-29', '2026-03-09'), encoding='utf-8')
        with self.assertRaises(ValueError):
            fest.import_file(self.config, self.config_file, self.path / 'data', 'institusjon', self.xml, 'full', 'production', fest.URLS['institusjon'])
        self.assertEqual(self.config['datasets']['institusjon']['hentet_dato'], '2026-09-29T08:00:00')

if __name__ == '__main__':
    unittest.main()
