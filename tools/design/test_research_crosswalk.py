"""Adversarial source-identity, access-scope and byte-provenance checks."""

import copy
import hashlib
import json
import runpy
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
API = runpy.run_path(str(Path(__file__).with_name('research_crosswalk.validator.py')))
RENDERER = runpy.run_path(str(Path(__file__).with_name('research_crosswalk.script.py')))


class ResearchCrosswalkTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / API['RESEARCH_DIR'] / 'source-audit.json'
        self.path.parent.mkdir(parents=True)
        self.episode = {'id': '01-records', 'order': 1, 'date': 'c.100', 'geographyId': 'city',
                        'historicalSelection': {'sourceUrl': 'https://example.org/text', 'passage': 'book1'}}
        second = {**copy.deepcopy(self.episode), 'id': '02-records', 'order': 2}
        self.campaigns = [{'campaignId': 'test-campaign', 'episodeSelection': [self.episode, second]},
                          {'campaignId': 'unlinked-campaign', 'episodeSelection': [copy.deepcopy(self.episode)]}]
        record = {'id': self.episode['id'], 'sourceUrl': 'https://example.org/text', 'locator': 'book1',
                  'consultationStatus': 'full_article_consulted', 'readScope': 'Archived declaration only',
                  'classification': 'retrospective', 'cautions': 'Not contemporary testimony',
                  'dateInDesign': 'c.100', 'placeInDesign': 'city'}
        self.source = {'sourceFile': '/obsolete/path/never-read.json',
                       'events': [record, {**record, 'id': '02-records'}]}
        self.path.write_text(json.dumps(self.source))
        self.data = {'schemaVersion': 1,
                     'sources': [{'id': 'archive', 'path': self.path.relative_to(self.root).as_posix(),
                                  'campaignIds': ['test-campaign'],
                                  'sha256': hashlib.sha256(self.path.read_bytes()).hexdigest()}],
                     'consultations': [],
                     'bindings': [{'campaignId': 'test-campaign', 'scenarioId': self.episode['id'],
                                   'selectionSha256': API['selection_fingerprint']('test-campaign', self.episode),
                                   'sourceId': 'archive', 'recordPointer': '/events/0', 'architectCheck': None}]}

    def audit(self, data=None, campaigns=None):
        return API['audit_crosswalk'](self.root, self.campaigns if campaigns is None else campaigns,
                                     self.data if data is None else data)

    def add_consultation(self, access='excerpt'):
        self.data['consultations'] = [{'id': 'fresh-read', 'realIdentity': 'test-reader', 'date': '2026-10-23',
                                      'url': 'https://example.org/new-text', 'title': 'A bounded source',
                                      'locator': 'page2', 'access': access, 'readScope': 'Only page2 read',
                                      'finding': 'A narrow context' if access in API['READABLE_ACCESS'] else None,
                                      'limits': 'No historical approval'}]
        self.data['bindings'][0]['architectCheck'] = {
            'consultationIds': ['fresh-read'], 'scopeNote': 'Different source explicitly attributed', 'corrections': []}

    def test_archived_full_read_cannot_become_a_new_architect_read(self):
        errors, report = self.audit()
        self.assertEqual(errors, [])
        first, second = report['campaigns']
        self.assertEqual((first['linked'], first['architectChecks'], first['withPassageRead']), (1, 0, 0))
        self.assertEqual((second['selected'], second['linked'], second['unlinked']), (1, 0, 1))
        self.add_consultation('unavailable')
        errors, report = self.audit()
        self.assertEqual(errors, [])
        self.assertEqual(report['campaigns'][0]['withPassageRead'], 0)
        self.assertEqual(report['campaigns'][0]['onlyUnavailableOrMetadata'], 1)
        self.assertIn('No passage finding', RENDERER['render_report'](report))

    def test_source_pointer_and_campaign_cannot_substitute_another_identity(self):
        for field, value in [('recordPointer', '/events/1'), ('recordPointer', '/events/9'),
                             ('scenarioId', 'absent'), ('campaignId', 'absent')]:
            with self.subTest(field=field, value=value):
                invalid = copy.deepcopy(self.data)
                invalid['bindings'][0][field] = value
                self.assertTrue(self.audit(invalid)[0])

    def test_source_campaign_scope_rejects_rehashed_same_id_from_another_campaign(self):
        invalid = copy.deepcopy(self.data)
        binding = invalid['bindings'][0]
        binding['campaignId'] = 'unlinked-campaign'
        binding['selectionSha256'] = API['selection_fingerprint']('unlinked-campaign', self.episode)
        self.assertTrue(any('outside the archived source scope' in error for error in self.audit(invalid)[0]))
        for scope in [[], 'test-campaign', ['absent'], ['test-campaign', 'test-campaign'], [[]]]:
            with self.subTest(scope=scope):
                invalid = copy.deepcopy(self.data)
                invalid['sources'][0]['campaignIds'] = scope
                self.assertTrue(self.audit(invalid)[0])

    def test_stale_selection_and_archived_bytes_fail_without_editing_canonical_data(self):
        for field in ['date', 'geographyId', 'historicalSelection']:
            invalid = copy.deepcopy(self.campaigns)
            invalid[0]['episodeSelection'][0][field] = 'changed'
            self.assertTrue(self.audit(campaigns=invalid)[0])
        self.path.write_text(self.path.read_text() + '\n')
        self.assertTrue(any('Stale archived' in error for error in self.audit()[0]))

    def test_duplicate_and_unresolved_bindings_or_consultations_fail(self):
        duplicated = copy.deepcopy(self.data)
        duplicated['bindings'] *= 2
        self.assertTrue(self.audit(duplicated)[0])
        duplicated = copy.deepcopy(self.data)
        duplicated['sources'] *= 2
        self.assertTrue(self.audit(duplicated)[0])
        missing = copy.deepcopy(self.data)
        missing['bindings'][0]['sourceId'] = 'absent'
        self.assertTrue(self.audit(missing)[0])
        self.add_consultation()
        self.data['bindings'][0]['architectCheck']['consultationIds'] = ['absent']
        self.assertTrue(self.audit()[0])
        self.data['bindings'][0]['architectCheck'] = None
        self.assertTrue(any('Unused' in error for error in self.audit()[0]))

    def test_unknown_approval_fields_and_inflated_access_are_rejected(self):
        for access in ['unavailable', 'metadata-only']:
            self.add_consultation(access)
            self.data['consultations'][0]['finding'] = 'Claimed full chapter reading'
            self.assertTrue(self.audit()[0])
        self.add_consultation()
        for invalid_access in ['full-book', True, ['excerpt']]:
            self.data['consultations'][0]['access'] = invalid_access
            self.assertTrue(self.audit()[0])
        self.add_consultation()
        self.data['historicalApproval'] = True
        self.assertTrue(self.audit()[0])
        del self.data['historicalApproval']
        self.data['bindings'][0]['architectCheck']['approved'] = True
        self.assertTrue(self.audit()[0])

    def test_local_sources_reject_escape_and_symlinks_outside_project(self):
        for path in ['/tmp/audit.json', '../audit.json', 'docs/design/catalog.json', r'..\audit.json']:
            invalid = copy.deepcopy(self.data)
            invalid['sources'][0]['path'] = path
            self.assertTrue(self.audit(invalid)[0])
        with tempfile.TemporaryDirectory() as external:
            outside = Path(external) / 'outside.json'
            outside.write_bytes(self.path.read_bytes())
            self.path.unlink()
            self.path.symlink_to(outside)
            self.assertTrue(self.audit()[0])
            self.path.unlink()
            source_dir = self.path.parent
            source_dir.rename(self.root / 'old-source-dir')
            source_dir.symlink_to(Path(external), target_is_directory=True)
            self.assertTrue(self.audit()[0])

    def test_json_pointer_escapes_are_exact_and_array_indices_unambiguous(self):
        self.assertEqual(API['record_at']({'a/b': {'~x': [7]}}, '/a~1b/~0x/0'), 7)
        for pointer in ['events/0', '/events/-1', '/events/00', '/events/0~2', '/events/-']:
            with self.subTest(pointer=pointer):
                with self.assertRaises((ValueError, KeyError, IndexError)):
                    API['record_at'](self.source, pointer)

    def test_summary_scope_stays_distinct_and_report_is_deterministic(self):
        self.add_consultation('summary')
        errors, report = self.audit()
        self.assertEqual(errors, [])
        self.assertEqual(report['records'][0]['consultations'][0]['access'], 'summary')
        rendered = RENDERER['render_report'](report)
        self.assertEqual(rendered, RENDERER['render_report'](copy.deepcopy(report)))
        self.assertIn('No historical authoring or native gate is unlocked', rendered)
        self.assertEqual(self.campaigns[0]['episodeSelection'][0], self.episode)

    def test_actual_first_caliphs_archive_preserves_gaps_and_bibliographic_correction(self):
        catalog = runpy.run_path(str(ROOT / 'tools/design/odyssey_catalog.helper.py'))
        _, campaigns = catalog['odyssey_catalog']()
        data = json.loads((ROOT / API['CROSSWALK_PATH']).read_text())
        errors, report = API['audit_crosswalk'](ROOT, campaigns, data)
        self.assertEqual(errors, [])
        self.assertEqual(sum(row['selected'] for row in report['campaigns']), 278)
        row = next(row for row in report['campaigns'] if row['campaignId'] == 'first-caliphs')
        self.assertEqual((row['linked'], row['architectChecks'], row['withPassageRead'],
                          row['onlyUnavailableOrMetadata'], row['linkedWithoutArchitectCheck']), (30, 9, 7, 2, 21))
        yamama = next(row for row in report['records'] if row['scenarioId'] == '02-the-roads-of-yamama')
        self.assertIn('date', yamama['differences'])
        mismatch = next(row for row in report['records'] if row['scenarioId'] == '10-finite-defence-and-trench-supply-medina')
        self.assertIn('scope warning', mismatch['architectCheck']['scopeNote'])
        self.assertEqual(mismatch['architectCheck']['consultationIds'],
                         ['khandaq-retrieved-scope-warning', 'morony-medina-paragraph'])
        self.assertIn('not a support or acceptance score', RENDERER['render_report'](report))
        self.assertIn('Jonathan P. Berkey', RENDERER['render_report'](report))
        self.assertEqual((ROOT / API['REPORT_PATH']).read_text(), RENDERER['render_report'](report))


if __name__ == '__main__':
    unittest.main()
