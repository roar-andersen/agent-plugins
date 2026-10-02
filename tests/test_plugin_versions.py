import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/plugin_versions.py'
spec = importlib.util.spec_from_file_location('versions', SCRIPT)
versions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(versions)


class VersionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.old_root = versions.ROOT
        versions.ROOT = self.root
        self.directory = self.root / 'plugins/example'
        for rel in versions.MANIFESTS:
            path = self.directory / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            versions.write(path, {'name': 'example', 'version': '1.2.3'})
        skill = self.directory / 'skills/example/SKILL.md'
        skill.parent.mkdir(parents=True)
        skill.write_text('Original skill', encoding='utf-8')
        for rel in versions.MARKETS:
            path = self.root / rel
            path.parent.mkdir(parents=True)
            source = {'source': 'local', 'path': './plugins/example'} if rel.startswith('.agents') else './plugins/example'
            versions.write(path, {'name': 'test-market', 'plugins': [{'name': 'example', 'version': '1.2.3', 'source': source}]})
        versions.git('init')
        versions.git('config', 'user.name', 'Test')
        versions.git('config', 'user.email', 'test@example.invalid')
        versions.git('add', '.')
        versions.git('commit', '-m', 'Baseline')
        self.base = versions.git('rev-parse', 'HEAD').stdout.strip()

    def tearDown(self):
        versions.ROOT = self.old_root
        self.temp.cleanup()

    def change(self):
        (self.directory / 'skills/example/SKILL.md').write_text('Changed skill', encoding='utf-8')

    def test_automatic_patch_syncs_all_manifests_and_marketplaces(self):
        self.change()
        plugins, markets = versions.catalog()
        self.assertEqual(versions.prepare(self.base, plugins, markets, True), ['example'])
        plugins, markets = versions.catalog()
        versions.validate(plugins, markets)
        self.assertEqual(plugins['example'][1]['version'], '1.2.4')

    def test_explicit_minor_is_preserved(self):
        self.change()
        plugins, markets = versions.catalog()
        versions.synchronize('example', '1.3.0', plugins, markets)
        versions.prepare(self.base, plugins, markets, True)
        self.assertEqual(versions.catalog()[0]['example'][1]['version'], '1.3.0')

    def test_unchanged_plugin_does_not_bump(self):
        plugins, markets = versions.catalog()
        self.assertEqual(versions.prepare(self.base, plugins, markets, True), [])
        self.assertEqual(plugins['example'][1]['version'], '1.2.3')

    def test_regression_and_mismatched_manifests_are_rejected(self):
        plugins, markets = versions.catalog()
        versions.synchronize('example', '1.2.2', plugins, markets)
        with self.assertRaises(ValueError):
            versions.prepare(self.base, plugins, markets, True)
        versions.write(self.directory / '.claude-plugin/plugin.json', {'name': 'example', 'version': '1.2.1'})
        with self.assertRaises(ValueError):
            versions.validate(plugins, markets)

    def test_semantic_bumps(self):
        self.assertEqual(versions.bump('1.2.3', 'major'), '2.0.0')
        self.assertEqual(versions.bump('1.2.3', 'minor'), '1.3.0')
        with self.assertRaises(ValueError):
            versions.version('1.2.3+build')


if __name__ == '__main__':
    unittest.main()
