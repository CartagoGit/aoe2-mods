"""Adversarial checks for the conditional model; no game timing assertions."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "readiness_timing_audit", Path(__file__).with_name("readiness_timing_audit.script.py")
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class ReadinessTimingTests(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((AUDIT.ROOT / AUDIT.DEFAULT_PLAN).read_text())
        campaign = json.loads((AUDIT.ROOT / self.plan["campaignSource"]).read_text())
        self.episode = next(row for row in campaign["episodes"] if row["id"] == self.plan["episodeId"])

    def test_graph_uses_authored_detour_and_rejects_disconnection(self):
        graph = {"a": {"b": 5}, "b": {"a": 5, "c": 7}, "c": {"b": 7}, "d": {}}
        self.assertEqual(AUDIT.shortest_distance(graph, "a", "c"), 12)
        with self.assertRaisesRegex(ValueError, "No authored land route"):
            AUDIT.shortest_distance(graph, "a", "d")

    def test_integer_worker_split_and_actual_staging_debit(self):
        self.assertEqual(AUDIT.worker_split({"food": 80, "wood": 20}, 5, 1),
                         {"workers": {"food": 4, "wood": 1}, "harvestSeconds": 20})
        result = AUDIT.build_report(self.plan, self.episode)
        hard = result["profiles"]["hard"]
        self.assertEqual(hard["stagingDebit"], {"food": 240, "wood": 180, "gold": 0, "stone": 0})
        self.assertEqual(hard["initialShortfall"], {"food": 189, "wood": 146, "gold": 0, "stone": 0})
        self.assertEqual(len(result["movements"]), 9)
        self.assertEqual(len(hard["samples"]), 18)
        # Increasing travel cost with other assumptions held cannot improve readiness.
        samples = {(r["movementTilesPerGameSecond"], r["netResourcePerWorkerGameSecond"], r["pathLengthFactor"]): r
                   for r in hard["samples"]}
        self.assertGreaterEqual(samples[(0.6, 0.2, 1.2)]["estimatedReadinessSeconds"],
                                samples[(0.6, 0.2, 1.0)]["estimatedReadinessSeconds"])
        self.assertTrue(any(r["strictlyInsideAssumedWindow"] for r in hard["samples"]))
        self.assertTrue(any(not r["strictlyInsideAssumedWindow"] for r in hard["samples"]))

    def test_incomplete_or_duplicate_assignment_cannot_look_fast(self):
        for mutation in ("missing", "duplicate", "wrong-zone", "disconnected", "unavailable"):
            with self.subTest(mutation=mutation):
                plan, episode = copy.deepcopy(self.plan), copy.deepcopy(self.episode)
                if mutation == "missing":
                    plan["stagingAssignments"].pop()
                elif mutation == "duplicate":
                    plan["stagingAssignments"].append(plan["stagingAssignments"][0])
                elif mutation == "wrong-zone":
                    plan["stagingAssignments"][-1]["zoneId"] = plan["stagingAssignments"][-2]["zoneId"]
                elif mutation == "disconnected":
                    episode["mapPlan"]["corridors"] = []
                else:
                    episode["worldContract"]["entities"][0]["generationPolicy"] = "after future payment"
                with self.assertRaises(ValueError):
                    AUDIT.build_report(plan, episode)

    def test_invalid_hypotheses_and_stale_source_are_detectable(self):
        for field, bad in (("movementTilesPerGameSecond", [0]),
                           ("netResourcePerWorkerGameSecond", [True]),
                           ("pathLengthFactors", [0.8]), ("collectionSeconds", -1)):
            with self.subTest(field=field):
                plan = copy.deepcopy(self.plan)
                plan["assumptions"][field] = bad
                with self.assertRaises(ValueError):
                    AUDIT.build_report(plan, self.episode)
        baseline = AUDIT.build_report(self.plan, self.episode)
        changed = copy.deepcopy(self.episode)
        changed["difficulty"]["hard"]["startingResources"]["food"] -= 1
        result = AUDIT.build_report(self.plan, changed)
        self.assertNotEqual(result["episodeSha256"], baseline["episodeSha256"])
        self.assertEqual(result["profiles"]["hard"]["initialShortfall"]["food"], 190)


if __name__ == "__main__":
    unittest.main()
