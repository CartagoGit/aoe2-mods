"""Adversarial accounting tests, not native or scenario playtests."""

import copy
import json
from pathlib import Path
import runpy
import unittest

helpers = runpy.run_path(str(Path(__file__).with_name("finite_allocation.helper.py")))
amounts = helpers["amounts"]
balance = helpers["balance"]
optional_states = helpers["optional_states"]
build_report = helpers["build_report"]
ROOT = Path(__file__).resolve().parents[2]


class FiniteAllocationTests(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((ROOT / "docs/research/odyssey-research/imperial34-care-allocation-plan.json").read_text())

    def test_actual_candidate_has_three_distinct_hard_choices_and_no_optional_dependency(self):
        report = build_report(self.plan)
        self.assertEqual([report["profiles"][level]["allSkipAffordableCount"]
                          for level in ("easy", "standard", "hard")], [9, 7, 3])
        hard = report["profiles"]["hard"]["combinations"]
        self.assertEqual([row["recipes"] for row in hard if row["allSkipAffordable"]], [
            ["meal-direct", "shelter-rented"],
            ["meal-shared-hearth", "shelter-rented"],
            ["meal-purchased", "shelter-local-kit"],
        ])
        self.assertTrue(all(row["allOptionalsAfterFundingAffordable"] for row in hard if row["allSkipAffordable"]))
        self.assertEqual(report["reservedOptionalRewards"], amounts({"food": 400, "wood": 150, "gold": 25}))
        self.assertFalse(report["nativeImplemented"])
        self.assertFalse(report["gameVerified"])

    def test_payment_before_reward_and_affordable_prefix_not_final_net_sum(self):
        optionals = [
            {"id": "repair", "cost": amounts({"wood": 50}), "reward": amounts({"wood": 100})},
            {"id": "aid", "cost": amounts({}), "reward": amounts({"wood": 50})},
        ]
        states = optional_states(amounts({"wood": 20}), optionals)
        self.assertNotIn(1, states)  # Repair alone cannot borrow its own reward.
        self.assertEqual(states[3], (amounts({"wood": 120}), ["aid", "repair"]))
        self.assertEqual(len(states), 3)  # No repeated repair to manufacture wood.
        self.assertIsNone(balance(amounts({}), amounts({"gold": 1}), amounts({"gold": 10})))

    def test_invalid_inputs_fail_without_inventing_stock_or_dropping_profiles(self):
        mutations = [
            lambda p: p.update(schemaVersion=True),
            lambda p: p.update(classification="native gameplay"),
            lambda p: p["operatingStockByDifficulty"].pop("hard"),
            lambda p: p["operatingStockByDifficulty"]["hard"].update(food=True),
            lambda p: p["operatingStockByDifficulty"]["hard"].update(wood=-1),
            lambda p: p["operatingStockByDifficulty"]["hard"].update(labor=100),
            lambda p: p["services"].append(copy.deepcopy(p["services"][0])),
            lambda p: p["services"][1]["recipes"][0].update(id="meal-direct"),
            lambda p: p["optionalTasks"].append(copy.deepcopy(p["optionalTasks"][0])),
            lambda p: p["optionalTasks"][0].update(kind="automatic-wealth"),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                plan = copy.deepcopy(self.plan)
                mutate(plan)
                with self.assertRaises(ValueError):
                    build_report(plan)
        many = copy.deepcopy(self.plan)
        many["services"] = [{"id": f"service-{i}", "recipes": [
            {"id": f"recipe-{i}", "cost": {}}]} for i in range(9)]
        with self.assertRaisesRegex(ValueError, "one to eight"):
            build_report(many)
        many = copy.deepcopy(self.plan)
        many["optionalTasks"] = [{"id": f"side-{i}", "kind": "copy"} for i in range(12)]
        with self.assertRaisesRegex(ValueError, "Combined"):
            build_report(many)
        plan = copy.deepcopy(self.plan)
        plan["operatingStockByDifficulty"]["hard"] = {}
        with self.assertRaisesRegex(ValueError, "depends on optional"):
            build_report(plan)  # Possible aid rewards do not replace all-skip acceptance.

    def test_actual_report_fingerprint_catches_candidate_and_shared_mechanics_changes(self):
        report = build_report(self.plan)
        saved = json.loads((ROOT / "docs/research/odyssey-research/imperial34-care-allocation-audit.json").read_text())
        self.assertEqual(report, saved)
        changed = copy.deepcopy(self.plan)
        changed["services"][0]["recipes"][0]["cost"]["food"] += 1
        self.assertNotEqual(build_report(changed)["resolvedInputsSha256"], report["resolvedInputsSha256"])
        shared = build_report.__globals__["REWARDS"]
        old = shared["aid"]
        try:
            shared["aid"] = {**old, "food": old["food"] + 1}
            self.assertNotEqual(build_report(self.plan)["resolvedInputsSha256"], report["resolvedInputsSha256"])
        finally:
            shared["aid"] = old


if __name__ == "__main__":
    unittest.main()
