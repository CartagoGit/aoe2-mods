"""Focused artificial tests for authored secondary reward projection."""

import copy
import json
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESOURCES = ("food", "wood", "gold", "stone")


class AuthoredSecondaryRewardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.secondary = runpy.run_path(str(ROOT / "tools/design/secondary.py"))
        cls.pipeline = runpy.run_path(str(ROOT / "tools/design/episode_dossiers.script.py"))
        cls.factory = cls.pipeline["factory"]
        cls.validator = cls.pipeline["validator"]

    def scenario(self):
        return {"id": "artificial-reward-projection", "mapPlan": {
            "hubs": [{"id": f"hub-{n}"} for n in range(1, 5)]}}

    def task(self, kind, **extra):
        task = {
            "kind": kind,
            "title": {"en": f"Artificial {kind}", "es-ES": f"{kind} artificial"},
            "subject": {"en": "the artificial district", "es-ES": "el distrito artificial"},
            "rationale": {"en": "Artificial test only", "es-ES": "Solo prueba artificial"},
        }
        task.update(extra)
        return task

    def test_omission_preserves_builder_contract_and_explicit_rewards_are_exact(self):
        builder = self.secondary["build_optional_objectives"]
        baseline_task = self.task("aid")
        legacy = builder(self.scenario(), [baseline_task])[0]
        repeated = builder(self.scenario(), [copy.deepcopy(baseline_task)])[0]
        self.assertEqual(legacy, repeated)
        self.assertEqual(legacy["effects"][0]["resources"], {"food": 100, "wood": 50})

        positive = builder(self.scenario(), [self.task("aid", resourceReward={"wood": 7, "gold": 0})])[0]
        self.assertEqual(positive["effects"][0]["resources"], {"wood": 7})
        self.assertTrue(positive["text"]["en"].endswith("Benefit: 7 wood, once."))
        self.assertTrue(positive["text"]["es-ES"].endswith("Ventaja: 7 de madera, una vez."))

        for reward in ({}, {key: 0 for key in RESOURCES}):
            with self.subTest(reward=reward):
                zero = builder(self.scenario(), [self.task("extract", resourceReward=reward)])[0]
                self.assertEqual(zero["effects"][0]["resources"], {})
                self.assertIn("No resource bonus. Completing this task achieves the optional local outcome described above.", zero["text"]["en"])
                self.assertIn("Sin bonificación de recursos. Al completar esta tarea se consigue el resultado local opcional indicado arriba.", zero["text"]["es-ES"])
                self.assertEqual(zero["predicate"]["requirements"][0]["kind"], "entity-arrival")

    def test_rejects_invalid_or_misplaced_resource_reward_without_mutation(self):
        builder = self.secondary["build_optional_objectives"]
        defaults = copy.deepcopy(self.secondary["REWARDS"])
        invalid_vectors = (-1, True, 1.0, 0.5, "2", None, [], {"ore": 2}, {"wood": -1})
        for value in invalid_vectors:
            task = self.task("aid", resourceReward=value)
            before = copy.deepcopy(task)
            with self.subTest(value=value), self.assertRaises(ValueError):
                builder(self.scenario(), [task])
            self.assertEqual(task, before)

        for kind in ("copy", "guide", "watch", "scout"):
            task = self.task(kind, resourceReward={})
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "only supported"):
                builder(self.scenario(), [task])
            self.assertEqual(task["resourceReward"], {})
        self.assertEqual(self.secondary["REWARDS"], defaults)

    def test_factory_accounts_from_generated_effects_and_payments_in_mixed_fixture(self):
        campaign = json.loads((ROOT / "docs/design/odysseys/imperial-church.json").read_text())
        selection_by_id = {row["id"]: row for row in campaign["episodeSelection"]}
        authored = copy.deepcopy(next(row for row in campaign["episodeBlueprints"] if row.get("order") == 1))
        selection = selection_by_id[authored["episodeId"]]
        by_order = {row["order"]: row for row in campaign["episodeSelection"]}
        next_selection = by_order.get(selection["order"] + 1)
        for task in authored["optionalTasks"]:
            if task["kind"] == "aid":
                task["resourceReward"] = {"wood": 9}
            elif task["kind"] == "repair":
                task["resourceReward"] = {}
            elif task["kind"] == "trade":
                task["resourceReward"] = {"gold": 0}
            elif task["kind"] == "extract":
                task["resourceReward"] = {"gold": 11}
        geography = json.loads((ROOT / "docs/design/geography.json").read_text())
        profile = next(row for row in geography["profiles"] if row["id"] == selection["geographyId"])
        baseline = json.loads((ROOT / "docs/design/catalog.json").read_text())["campaigns"]
        draft = self.factory.build_dossier(
            campaign, selection, authored, profile, next_selection, baseline
        )
        self.assertEqual(len(draft["secondaryObjectives"]), 6)
        self.assertGreaterEqual(len({row["kind"] for row in draft["secondaryObjectives"]}), 4)
        self.assertGreaterEqual(len(draft["playstyles"]), 3)
        actual_rewards = {key: 0 for key in RESOURCES}
        actual_costs = {key: 0 for key in RESOURCES}
        for objective in draft["secondaryObjectives"]:
            for effect in objective["effects"]:
                for key, amount in effect["resources"].items():
                    actual_rewards[key] += amount
            for requirement in objective["predicate"]["requirements"]:
                if requirement["kind"] == "atomic-payment":
                    for key, amount in requirement["resources"].items():
                        actual_costs[key] += amount
        self.assertEqual(draft["secondaryBudget"]["reservedRewards"], actual_rewards)
        self.assertEqual(draft["secondaryBudget"]["maxOptionalCosts"], actual_costs)
        for level in ("easy", "standard", "hard"):
            self.assertTrue(draft["difficulty"][level]["mainFeasibleSkippingAllOptionals"])
        repair = next(row for row in draft["secondaryObjectives"] if row["kind"] == "repair")
        trade = next(row for row in draft["secondaryObjectives"] if row["kind"] == "trade")
        self.assertEqual(repair["effects"][0]["resources"], {})
        self.assertTrue(any(req["kind"] == "atomic-payment" and req["resources"] == {"wood": 50}
                            for req in repair["predicate"]["requirements"]))
        self.assertEqual(trade["effects"][0]["resources"], {})
        self.assertTrue(any(req["kind"] == "atomic-payment" and req["resources"] == {"gold": 50}
                            for req in trade["predicate"]["requirements"]))
        self.assertEqual(self.validator.audit_dossier(draft, campaign, baseline), [])

        oversized = copy.deepcopy(authored)
        next(task for task in oversized["optionalTasks"] if task["kind"] == "aid")[
            "resourceReward"
        ] = {"food": 10000}
        invalid = self.factory.build_dossier(
            campaign, selection, oversized, profile, next_selection, baseline
        )
        errors = self.validator.audit_dossier(invalid, campaign, baseline)
        self.assertTrue(any("rewards created beyond old cache allowance" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
