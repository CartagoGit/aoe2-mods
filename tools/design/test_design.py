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

    def test_missing_workshop_ledger_is_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid['campaigns'] if c['id'] == 'new-rome')['scenarios'][1]
        pred = mission['objectivePlan'][1]['predicate']
        pred['requirements'] = [r for r in pred['requirements'] if r['id'] != 'workshop-ledger']
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('missing required ledger' in e for e in errors))

    def test_karbala_supplies_must_follow_same_families(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid['campaigns'] if c['id'] == 'house-of-ali')['scenarios'][3]
        water = next(r for r in mission['objectivePlan'][1]['predicate']['requirements'] if r['id'] == 'water-to-six-families')
        water['pairs'][0]['receiver'] = 'another-family'
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('same surviving families' in e for e in errors))

    def test_payment_allocation_and_double_receipt_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid['campaigns'] if c['id'] == 'church-of-rome')['scenarios'][1]
        payment = mission['objectivePlan'][1]['predicate']['requirements'][0]
        payment['allocations'][payment['receivingZones'][0]]['gold'] = 0
        mission['objectivePlan'][2]['predicate']['requirements'][0]['paidFlag'] = payment['paidFlag']
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('unbalanced delivery' in e for e in errors))
        self.assertTrue(any('duplicated receipt' in e for e in errors))

    def test_local_supply_gap_must_preserve_feasibility_and_difficulty(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = invalid['campaigns'][0]['scenarios'][0]
        for balance in mission['difficulty'].values():
            for index, wave in enumerate(balance['waves']):
                wave['offsetSeconds'] = 150 * (index+1)
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('two local supply trips' in e for e in errors))
        self.assertTrue(any('identical wave pressure' in e for e in errors))


    def test_northern_access_cannot_alias_southern_rally(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid['campaigns'] if c['id'] == 'imperial-church')['scenarios'][0]
        north = mission['objectivePlan'][0]['predicate']['requirements'][0]['zones'][0]
        next(z for z in mission['worldContract']['zones'] if z['id'] == north)['hub'] = 'hub-3'
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('wrong geographic district' in e for e in errors))

    def test_truce_deliveries_require_two_separate_receivers(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid['campaigns'] if c['id'] == 'house-of-ali')['scenarios'][1]
        delivery = mission['objectivePlan'][1]['predicate']['requirements'][0]
        same_zone = next(iter(delivery['destinations'].values()))
        delivery['destinations'] = {e: same_zone for e in delivery['entities']}
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('distinct destination distribution' in e for e in errors))
        self.assertTrue(any('actual delivery receipt' in e for e in errors))

    def test_withdrawal_cannot_substitute_unsupplied_families(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid['campaigns'] if c['id'] == 'house-of-ali')['scenarios'][3]
        withdrawal = next(r for r in mission['objectivePlan'][2]['predicate']['requirements'] if r['id'] == 'withdraw-same-families')
        withdrawal['eligibleEntitiesFromLedger']['ledger'] = 'all-families'
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('supplied survivor intersection' in e for e in errors))


    def test_side_reward_cannot_spend_main_recovery_or_create_resources(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = invalid['campaigns'][0]['scenarios'][0]
        reward = next(o for o in mission['secondaryObjectives'] if o['kind'] == 'aid')['effects'][0]
        reward['resources']['food'] = 10000
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('optional reward budget drift' in e for e in errors))

    def test_two_optional_receivers_or_lookouts_cannot_share_one_footprint(self):
        invalid = copy.deepcopy(self.catalogue)
        objective = next(o for o in invalid['campaigns'][0]['scenarios'][0]['secondaryObjectives'] if o['kind'] == 'aid')
        objective['world']['zones'][1]['offsetTiles'] = objective['world']['zones'][0]['offsetTiles']
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('secondary receiving/observation zones overlap' in e for e in errors))

    def test_loading_a_save_cannot_reopen_an_optional_reward(self):
        invalid = copy.deepcopy(self.catalogue)
        objective = invalid['campaigns'][0]['scenarios'][0]['secondaryObjectives'][0]
        objective['stateContract']['persistentAcrossSave'] = False
        objective['stateContract']['rewardTransaction'].remove('debit reserved stock')
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any('incomplete optional state/persistence guard' in e for e in errors))
        self.assertTrue(any('undefined atomic optional funding transaction' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
