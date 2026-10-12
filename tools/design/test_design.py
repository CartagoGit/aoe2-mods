"""Adversarial tests for the high-impact geographic and design acceptance checks."""
import copy
import json
import unittest
from geography import clip_segment, tile_point
from verify import ROOT, verify


class DesignAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((ROOT / 'docs/design/catalog.json').read_text())

    def test_crossing_segment_keeps_intersections_even_with_no_inner_vertices(self):
        self.assertEqual(clip_segment([-2, .5], [2, .5], [0, 0, 1, 1]), [[0, .5], [1, .5]])
        self.assertIsNone(clip_segment([-2, 2], [2, 2], [0, 0, 1, 1]))

    def test_north_and_east_preserved_at_high_latitude(self):
        centre = tile_point([8, 44, 10, 46], [9, 45], 320)
        self.assertGreater(tile_point([8, 44, 10, 46], [9.5, 45], 320)[0], centre[0])
        self.assertLess(tile_point([8, 44, 10, 46], [9, 45.5], 320)[1], centre[1])

    def test_missing_spanish_and_witness_voice_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        screen = invalid['campaigns'][0]['scenarios'][0]['screens'][1]
        del screen['text']['es-ES']
        screen['narrator'] = 'partisan-voice'
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('bilingual' in e for e in errors))
        self.assertTrue(any('voice order' in e for e in errors))

    def test_overspent_finite_reserve_and_continuity_cycle_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        invalid['campaigns'][0]['scenarios'][0]['difficulty']['hard']['waves'][0]['count'] += 1
        invalid['campaigns'][1]['routes'][0]['next'] = invalid['campaigns'][0]['id']
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('reserve' in e for e in errors))
        self.assertTrue(any('cycle' in e for e in errors))

    def test_insolvent_recovery_budget_is_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        profile = invalid['campaigns'][0]['scenarios'][0]['difficulty']['hard']
        profile['gatherableBank']['food'] = 0
        profile['startingResources']['food'] = 0
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('insolvent food' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
