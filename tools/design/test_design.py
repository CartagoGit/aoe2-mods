"""Adversarial tests for the high-impact geographic and design acceptance checks."""

import copy
import json
import runpy
import unittest
import tempfile
import hashlib
from pathlib import Path
from geography import clip_segment, tile_point
from verify import ROOT, verify


class DesignAcceptanceTests(unittest.TestCase):
    def test_odyssey_assignments_reject_shared_slice_and_early_promotion(self):
        assignments = json.loads((ROOT / "docs/design/assignments.json").read_text())
        invalid = copy.deepcopy(assignments)
        row = invalid["assignments"][0]
        row["episodeSlices"][1]["sliceId"] = row["episodeSlices"][0]["sliceId"]
        row["promotionSlice"] = row["episodeSlices"][0]["sliceId"]
        audit = runpy.run_path(
            str(ROOT / "tools/design/odyssey_assignments.validator.py")
        )["audit_assignments"]
        errors = audit(ROOT, self.odysseys, invalid)
        self.assertTrue(any("share one authoring slice" in error for error in errors))
        self.assertTrue(any("promotion precedes" in error for error in errors))

    def test_clipped_geographic_layer_keeps_crossing_without_interior_vertices(self):
        helper = runpy.run_path(str(ROOT / "tools/design/geographic_layers.helper.py"))
        layer = {
            "features": [
                {
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[-2, 0.5], [2, 0.5]],
                    }
                },
                {"geometry": {"type": "LineString", "coordinates": [[-2, 2], [2, 2]]}},
            ]
        }
        segments = helper["clipped_tile_segments"](
            helper["index_layer"](layer), [0, 0, 1, 1], 320
        )
        self.assertEqual(
            segments,
            [
                [
                    tile_point([0, 0, 1, 1], [0, 0.5], 320),
                    tile_point([0, 0, 1, 1], [1, 0.5], 320),
                ]
            ],
        )

    def test_expanded_captions_cannot_drop_historical_qualification(self):
        draft = self.draft()
        draft["screens"][1]["captionSegments"]["en"] = ["An invented certainty"]
        self.assertTrue(
            any(
                "caption content lost" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_research_reference_rejects_hash_drift_and_external_path_without_reading_it(
        self,
    ):
        audit = runpy.run_path(
            str(ROOT / "tools/design/research_references.validator.py")
        )["audit_references"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data.json").write_text("{}")
            asset = {
                "id": "fixture",
                "path": "data.json",
                "bytes": 2,
                "sha256": hashlib.sha256(b"{}").hexdigest(),
                "license": "Public domain",
                "author": "Fixture",
                "sourcePage": "https://example.org/fixture",
                "productionApproved": False,
            }
            self.assertEqual(audit(root, {"assets": [asset]}), [])
            (root / "data.json").write_text("[]")
            self.assertTrue(
                any("hash drift" in error for error in audit(root, {"assets": [asset]}))
            )
            asset["path"] = "../outside.json"
            self.assertEqual(
                audit(root, {"assets": [asset]}), ["Unsafe reference path: fixture"]
            )

    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((ROOT / "docs/design/catalog.json").read_text())
        cls.odyssey_helper = runpy.run_path(
            str(ROOT / "tools/design/odyssey_catalog.helper.py")
        )
        cls.odyssey_policy, cls.odysseys = cls.odyssey_helper["odyssey_catalog"]()
        cls.dossier_validator = staticmethod(
            runpy.run_path(str(ROOT / "tools/design/episode_dossier.validator.py"))[
                "audit_dossier"
            ]
        )

    def draft(self, order=1):
        return copy.deepcopy(
            next(e for e in self.odysseys[0]["episodes"] if e["order"] == order)
        )

    def test_playstyles_cannot_reference_missing_or_duplicate_optional_tasks(self):
        draft = self.draft()
        draft["playstyles"][0]["optionalObjectives"] = ["side-missing"]
        draft["playstyles"][2]["optionalObjectives"] = copy.deepcopy(
            draft["playstyles"][1]["optionalObjectives"]
        )
        errors = self.dossier_validator(draft)
        self.assertTrue(any("invalid playstyle portfolio" in error for error in errors))
        self.assertTrue(
            any("repeated playstyle portfolio" in error for error in errors)
        )

    def test_expanded_dossiers_reject_wrong_narrator_and_incomplete_translation(self):
        draft = self.draft()
        draft["screens"][1]["narrator"] = "miriam-archive"
        del draft["screens"][3]["text"]["es-ES"]
        errors = self.dossier_validator(draft)
        self.assertTrue(any("narrator voice" in error for error in errors))
        self.assertTrue(any("incomplete localization" in error for error in errors))

    def test_expanded_dossiers_reject_impossible_arrival_and_duplicate_survivors(self):
        draft = self.draft(2)
        draft["objectivePlan"][0]["predicate"]["requirements"][0]["requiredCount"] = 9
        draft["worldContract"]["survivorGroups"][0]["entities"].append(
            draft["worldContract"]["survivorGroups"][0]["entities"][0]
        )
        errors = self.dossier_validator(draft)
        self.assertTrue(any("impossible counter" in error for error in errors))
        self.assertTrue(any("duplicate survivor" in error for error in errors))

    def test_expanded_withdrawal_cannot_use_unsupplied_recipient_ledger(self):
        draft = self.draft(2)
        draft["objectivePlan"][2]["predicate"]["requirements"][0][
            "eligibleEntitiesFromLedger"
        ]["ledger"] = "missing"
        self.assertTrue(
            any(
                "prior recipient ledger" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_expanded_dossiers_reject_funding_booleans_that_hide_overdraw(self):
        draft = self.draft()
        draft["difficulty"]["hard"]["gatherableBank"]["wood"] = 0
        draft["difficulty"]["hard"]["mainFeasibleSkippingAllOptionals"] = True
        self.assertTrue(
            any(
                "nonoptional stock drift" in error
                or "main goal needs optional" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_expanded_dossiers_reject_early_campaign_finale_and_initial_arrival(self):
        draft = self.draft(2)
        draft["stateMachine"]["campaignProgressWrite"] = True
        req = draft["objectivePlan"][0]["predicate"]["requirements"][0]
        eid = req["entities"][0]
        zone = next(
            z
            for z in draft["worldContract"]["zones"]
            if z["id"] == req["destinations"][eid]
        )
        entity = next(e for e in draft["worldContract"]["entities"] if e["id"] == eid)
        entity["initialHub"] = zone["hub"]
        entity["offsetTiles"] = zone["offsetTiles"][:]
        errors = self.dossier_validator(draft)
        self.assertTrue(
            any("intermediate episode can end campaign" in error for error in errors)
        )
        self.assertTrue(
            any("initial arrival incorrectly counts" in error for error in errors)
        )

    def test_odyssey_expansion_cannot_discard_baseline_semantic_identity(self):
        invalid = copy.deepcopy(self.odysseys)
        episode = next(
            e for e in invalid[0]["episodeSelection"] if e["existingContract"]
        )
        episode["id"] = "replacement-id-that-loses-progress"
        errors = self.odyssey_helper["audit_selections"](self.odyssey_policy, invalid)
        self.assertTrue(any("semantic identity was lost" in e for e in errors))

    def test_odyssey_selection_cannot_claim_three_repeated_cores_as_variety(self):
        invalid = copy.deepcopy(self.odysseys)
        for episode in invalid[0]["episodeSelection"][:3]:
            episode["coreMechanic"] = "identical-escort"
        errors = self.odyssey_helper["audit_selections"](self.odyssey_policy, invalid)
        self.assertTrue(any("three consecutive identical cores" in e for e in errors))

    def test_odyssey_predecessor_notice_must_remain_nonblocking(self):
        invalid = copy.deepcopy(self.odysseys)
        invalid[1]["continuityContract"]["proceedWithoutPredecessor"] = False
        errors = self.odyssey_helper["audit_selections"](self.odyssey_policy, invalid)
        self.assertTrue(
            any("predecessor progress would gate play" in e for e in errors)
        )

    def test_crossing_segment_keeps_intersections_even_with_no_inner_vertices(self):
        self.assertEqual(
            clip_segment([-2, 0.5], [2, 0.5], [0, 0, 1, 1]), [[0, 0.5], [1, 0.5]]
        )
        self.assertIsNone(clip_segment([-2, 2], [2, 2], [0, 0, 1, 1]))

    def test_north_and_east_preserved_at_high_latitude(self):
        centre = tile_point([8, 44, 10, 46], [9, 45], 320)
        self.assertGreater(tile_point([8, 44, 10, 46], [9.5, 45], 320)[0], centre[0])
        self.assertLess(tile_point([8, 44, 10, 46], [9, 45.5], 320)[1], centre[1])

    def test_missing_spanish_and_witness_voice_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        screen = invalid["campaigns"][0]["scenarios"][0]["screens"][1]
        del screen["text"]["es-ES"]
        screen["narrator"] = "partisan-voice"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("bilingual" in e for e in errors))
        self.assertTrue(any("voice order" in e for e in errors))

    def test_overspent_finite_reserve_and_continuity_cycle_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        invalid["campaigns"][0]["scenarios"][0]["difficulty"]["hard"]["waves"][0][
            "count"
        ] += 1
        invalid["campaigns"][1]["routes"][0]["next"] = invalid["campaigns"][0]["id"]
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("reserve" in e for e in errors))
        self.assertTrue(any("cycle" in e for e in errors))

    def test_insolvent_recovery_budget_is_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        profile = invalid["campaigns"][0]["scenarios"][0]["difficulty"]["hard"]
        profile["gatherableBank"]["food"] = 0
        profile["startingResources"]["food"] = 0
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("insolvent food" in e for e in errors))

    def test_missing_workshop_ledger_is_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "new-rome")[
            "scenarios"
        ][1]
        pred = mission["objectivePlan"][1]["predicate"]
        pred["requirements"] = [
            r for r in pred["requirements"] if r["id"] != "workshop-ledger"
        ]
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("missing required ledger" in e for e in errors))

    def test_karbala_supplies_must_follow_same_families(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "house-of-ali")[
            "scenarios"
        ][3]
        water = next(
            r
            for r in mission["objectivePlan"][1]["predicate"]["requirements"]
            if r["id"] == "water-to-six-families"
        )
        water["pairs"][0]["receiver"] = "another-family"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("same surviving families" in e for e in errors))

    def test_payment_allocation_and_double_receipt_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "church-of-rome")[
            "scenarios"
        ][1]
        payment = mission["objectivePlan"][1]["predicate"]["requirements"][0]
        payment["allocations"][payment["receivingZones"][0]]["gold"] = 0
        mission["objectivePlan"][2]["predicate"]["requirements"][0]["paidFlag"] = (
            payment["paidFlag"]
        )
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("unbalanced delivery" in e for e in errors))
        self.assertTrue(any("duplicated receipt" in e for e in errors))

    def test_local_supply_gap_must_preserve_feasibility_and_difficulty(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = invalid["campaigns"][0]["scenarios"][0]
        for balance in mission["difficulty"].values():
            for index, wave in enumerate(balance["waves"]):
                wave["offsetSeconds"] = 150 * (index + 1)
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("two local supply trips" in e for e in errors))
        self.assertTrue(any("identical wave pressure" in e for e in errors))

    def test_northern_access_cannot_alias_southern_rally(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "imperial-church")[
            "scenarios"
        ][0]
        north = mission["objectivePlan"][0]["predicate"]["requirements"][0]["zones"][0]
        next(z for z in mission["worldContract"]["zones"] if z["id"] == north)[
            "hub"
        ] = "hub-3"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("wrong geographic district" in e for e in errors))

    def test_truce_deliveries_require_two_separate_receivers(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "house-of-ali")[
            "scenarios"
        ][1]
        delivery = mission["objectivePlan"][1]["predicate"]["requirements"][0]
        same_zone = next(iter(delivery["destinations"].values()))
        delivery["destinations"] = {e: same_zone for e in delivery["entities"]}
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("distinct destination distribution" in e for e in errors))
        self.assertTrue(any("actual delivery receipt" in e for e in errors))

    def test_withdrawal_cannot_substitute_unsupplied_families(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "house-of-ali")[
            "scenarios"
        ][3]
        withdrawal = next(
            r
            for r in mission["objectivePlan"][2]["predicate"]["requirements"]
            if r["id"] == "withdraw-same-families"
        )
        withdrawal["eligibleEntitiesFromLedger"]["ledger"] = "all-families"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("supplied survivor intersection" in e for e in errors))

    def test_side_reward_cannot_spend_main_recovery_or_create_resources(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = invalid["campaigns"][0]["scenarios"][0]
        reward = next(o for o in mission["secondaryObjectives"] if o["kind"] == "aid")[
            "effects"
        ][0]
        reward["resources"]["food"] = 10000
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("optional reward budget drift" in e for e in errors))

    def test_two_optional_receivers_or_lookouts_cannot_share_one_footprint(self):
        invalid = copy.deepcopy(self.catalogue)
        objective = next(
            o
            for o in invalid["campaigns"][0]["scenarios"][0]["secondaryObjectives"]
            if o["kind"] == "aid"
        )
        objective["world"]["zones"][1]["offsetTiles"] = objective["world"]["zones"][0][
            "offsetTiles"
        ]
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(
            any("secondary receiving/observation zones overlap" in e for e in errors)
        )

    def test_loading_a_save_cannot_reopen_an_optional_reward(self):
        invalid = copy.deepcopy(self.catalogue)
        objective = invalid["campaigns"][0]["scenarios"][0]["secondaryObjectives"][0]
        objective["stateContract"]["persistentAcrossSave"] = False
        objective["stateContract"]["rewardTransaction"].remove("debit reserved stock")
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(
            any("incomplete optional state/persistence guard" in e for e in errors)
        )
        self.assertTrue(
            any("undefined atomic optional funding transaction" in e for e in errors)
        )


if __name__ == "__main__":
    unittest.main()
