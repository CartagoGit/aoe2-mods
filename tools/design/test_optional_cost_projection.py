"""Focused tests for opt-in authored secondary payment costs."""

import copy
import json
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESOURCES = ("food", "wood", "gold", "stone")


class OptionalCostProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.secondary = runpy.run_path(str(ROOT / "tools/design/secondary.py"))
        cls.pipeline = runpy.run_path(str(ROOT / "tools/design/episode_dossiers.script.py"))
        cls.factory = cls.pipeline["factory"]
        cls.validator = cls.pipeline["validator"]

    def scenario(self):
        return {
            "id": "artificial-secondary-cost",
            "mapPlan": {"hubs": [{"id": f"hub-{number}"} for number in range(1, 5)]},
            "sourceIds": ["artificial-source"],
            "historicalBrief": {"en": "Artificial note", "es-ES": "Nota artificial"},
            "goals": [{"en": "Artificial goal", "es-ES": "Objetivo artificial"}],
        }

    def task(self, kind, **extra):
        task = {
            "kind": kind,
            "title": {"en": f"Artificial {kind}", "es-ES": f"{kind} artificial"},
            "subject": {"en": "the artificial district", "es-ES": "el distrito artificial"},
            "rationale": {"en": "Artificial test only", "es-ES": "Solo prueba artificial"},
        }
        task.update(extra)
        return task

    def authored_instruction(self):
        return {
            "en": "Pay the stated cost once for this local task.",
            "es-ES": "Paga una vez el coste indicado para esta tarea local.",
        }

    def test_cost_overrides_preserve_requirements_rewards_and_arrival_order(self):
        builder = self.secondary["build_optional_objectives"]
        cases = (
            ("repair", {"wood": 30}, False),
            ("trade", {"gold": 20}, True),
            ("extract", {"food": 20}, True),
        )
        for kind, cost, after_arrival in cases:
            with self.subTest(kind=kind):
                source = self.task(kind, resourceCost=cost, instruction=self.authored_instruction())
                before = copy.deepcopy(source)
                side = builder(self.scenario(), [source])[0]
                self.assertEqual(source, before)
                self.assertEqual(len(side["world"]["entities"]), 2 if kind == "extract" else 1)
                payment = next(
                    requirement for requirement in side["predicate"]["requirements"]
                    if requirement["kind"] == "atomic-payment"
                )
                self.assertEqual(payment["resources"], cost)
                self.assertEqual(payment["receipt"], f"artificial-secondary-cost.{side['id']}.payment")
                self.assertTrue(payment["once"])
                self.assertTrue(payment["protectedRecoveryCannotBeSpent"])
                self.assertIs(payment["afterArrival"], after_arrival)
                self.assertEqual(side["effects"][0]["resources"], self.secondary["REWARDS"][kind])
                self.assertEqual(side["effects"][0]["funding"], "reserved-optional-stock")
                if kind == "repair":
                    requirements = side["predicate"]["requirements"]
                    self.assertEqual([row["kind"] for row in requirements], ["entity-health", "atomic-payment"])
                    health = requirements[0]
                    self.assertEqual(health["health"], "full")
                    self.assertEqual(health["paymentReceipt"], payment["receipt"])
                    self.assertEqual(
                        health["restoration"],
                        "atomic authored-cost repair transaction restores full health; no additional engine repair charge",
                    )
                else:
                    arrival = side["predicate"]["requirements"][0]
                    self.assertEqual(arrival["kind"], "entity-arrival")
                    self.assertEqual(len(arrival["entities"]), 2 if kind == "extract" else 1)
                    self.assertEqual(arrival["requiredCount"], len(arrival["entities"]))
                    self.assertTrue(arrival["aliveAtDelivery"])
                    self.assertTrue(arrival["oncePerEntity"])
                    self.assertTrue(arrival["noSubstitutes"])
                    self.assertTrue(arrival["initialPlacementDoesNotCount"])

    def test_real_factory_and_validator_sum_each_authored_cost_once(self):
        campaign = json.loads((ROOT / "docs/design/odysseys/imperial-church.json").read_text())
        authored = copy.deepcopy(next(row for row in campaign["episodeBlueprints"] if row.get("order") == 1))
        for task in authored["optionalTasks"]:
            if task["kind"] in ("repair", "trade", "extract"):
                task["resourceCost"] = {"repair": {"wood": 30}, "trade": {"gold": 20}, "extract": {"food": 20}}[task["kind"]]
                task["instruction"] = self.authored_instruction()
        before = copy.deepcopy(authored)
        selection_by_id = {row["id"]: row for row in campaign["episodeSelection"]}
        selection = selection_by_id[authored["episodeId"]]
        by_order = {row["order"]: row for row in campaign["episodeSelection"]}
        next_selection = by_order[selection["order"] + 1]
        geography = json.loads((ROOT / "docs/design/geography.json").read_text())
        profile = next(row for row in geography["profiles"] if row["id"] == selection["geographyId"])
        baseline = json.loads((ROOT / "docs/design/catalog.json").read_text())["campaigns"]
        draft = self.factory.build_dossier(campaign, selection, authored, profile, next_selection, baseline)
        self.assertEqual(authored, before)
        self.assertEqual(
            draft["secondaryBudget"]["maxOptionalCosts"],
            {"food": 20, "wood": 30, "gold": 20, "stone": 0},
        )
        self.assertEqual(self.validator.audit_dossier(draft, campaign, baseline), [])

    def test_absent_cost_preserves_existing_full_fixture_projection(self):
        campaign = json.loads((ROOT / "docs/design/odysseys/imperial-church.json").read_text())
        authored = copy.deepcopy(next(row for row in campaign["episodeBlueprints"] if row.get("order") == 1))
        selection_by_id = {row["id"]: row for row in campaign["episodeSelection"]}
        selection = selection_by_id[authored["episodeId"]]
        by_order = {row["order"]: row for row in campaign["episodeSelection"]}
        geography = json.loads((ROOT / "docs/design/geography.json").read_text())
        profile = next(row for row in geography["profiles"] if row["id"] == selection["geographyId"])
        baseline = json.loads((ROOT / "docs/design/catalog.json").read_text())["campaigns"]
        draft = self.factory.build_dossier(
            campaign, selection, authored, profile, by_order[selection["order"] + 1], baseline
        )
        expected = next(row for row in campaign["episodes"] if row["id"] == selection["id"])
        self.assertEqual(draft["secondaryObjectives"], expected["secondaryObjectives"])
        self.assertEqual(
            json.dumps(draft["secondaryObjectives"], ensure_ascii=False, separators=(",", ":")),
            json.dumps(expected["secondaryObjectives"], ensure_ascii=False, separators=(",", ":")),
        )

    def test_invalid_cost_kinds_vectors_and_missing_bilingual_instruction_fail(self):
        builder = self.secondary["build_optional_objectives"]
        for kind in ("scout", "aid", "copy", "guide", "watch"):
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "only supported"):
                builder(self.scenario(), [self.task(kind, resourceCost={"food": 1})])

        invalid_costs = (
            {}, {key: 0 for key in RESOURCES}, None, [], "2", True, 1.0,
            {"ore": 1}, {"wood": -1}, {"wood": True}, {"wood": 1.0},
            {"wood": 0.5}, {"wood": "2"}, {"wood": None},
        )
        for value in invalid_costs:
            task = self.task("repair", resourceCost=value, instruction=self.authored_instruction())
            before = copy.deepcopy(task)
            with self.subTest(cost=value), self.assertRaises(ValueError):
                builder(self.scenario(), [task])
            self.assertEqual(task, before)

        bad_instructions = (
            None, {"en": "English only"}, {"en": "", "es-ES": "Texto"},
            {"en": "Pay once", "es-ES": " "}, {"en": 7, "es-ES": "Texto"},
        )
        for instruction in bad_instructions:
            task = self.task("extract", resourceCost={"food": 20}, instruction=instruction)
            with self.subTest(instruction=instruction), self.assertRaisesRegex(ValueError, "instruction"):
                builder(self.scenario(), [task])


if __name__ == "__main__":
    unittest.main()
