"""Focused source validation and parser checks for native XS transactions."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

from AoE2ScenarioParser.datasets.trigger_lists import Attribute


ROOT = Path(__file__).resolve().parents[3]
HELPER_PATH = ROOT / "tools/python/native_transactions.helper.py"
SPEC = importlib.util.spec_from_file_location("native_transactions_helper", HELPER_PATH)
HELPER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HELPER)


class NativeResourceTransactionTests(unittest.TestCase):
    def test_payment_checks_every_resource_before_any_debit_and_sets_receipt_last(self):
        source = HELPER.render_payment_function(
            "cdf_pay_court", 1, {"wood": 7, "food": 25, "gold": 2}, 8, {9: 1})
        food_check = source.index("if (cdf_stock_food < 25)")
        wood_check = source.index("if (cdf_stock_wood < 7)")
        gold_check = source.index("if (cdf_stock_gold < 2)")
        first_write = source.index("xsSetPlayerAttribute")
        self.assertLess(food_check, first_write)
        self.assertLess(wood_check, first_write)
        self.assertLess(gold_check, first_write)
        self.assertLess(source.index("xsTriggerVariable(9) != 1"), first_write)
        self.assertLess(source.index("xsTriggerVariable(8) != 0"), first_write)
        self.assertLess(first_write, source.index("xsSetTriggerVariable(8, 1)"))
        self.assertIn(f"xsPlayerAttribute(1, {Attribute.FOOD_STORAGE.value})", source)
        self.assertIn(f"xsPlayerAttribute(1, {Attribute.WOOD_STORAGE.value})", source)
        self.assertIn(f"xsPlayerAttribute(1, {Attribute.GOLD_STORAGE.value})", source)
        self.assertNotIn("yield", source.lower())

    def test_reward_checks_all_reserves_then_debits_then_credits_then_completes(self):
        source = HELPER.render_reward_function(
            "cdf_grant_shelter", 2, {"stone": 13, "food": 6},
            {"food": 3, "stone": 4}, 5, {6: 1})
        food_check = source.index("if (cdf_reserve_food < 6)")
        stone_check = source.index("if (cdf_reserve_stone < 13)")
        first_write = source.index("xsSetTriggerVariable")
        self.assertLess(source.index("xsTriggerVariable(6) != 1"), first_write)
        self.assertLess(source.index("xsTriggerVariable(5) != 0"), first_write)
        self.assertLess(food_check, first_write)
        self.assertLess(stone_check, first_write)
        first_credit = source.index("xsSetPlayerAttribute")
        self.assertLess(first_write, first_credit)
        self.assertLess(source.rindex("xsSetTriggerVariable(5, 1)"), source.index("return (true)"))
        self.assertLess(source.index("xsSetTriggerVariable(3,"), first_credit)
        self.assertLess(source.index("xsSetTriggerVariable(4,"), first_credit)
        self.assertIn(f"xsPlayerAttribute(2, {Attribute.FOOD_STORAGE.value})", source)
        self.assertIn(f"xsPlayerAttribute(2, {Attribute.STONE_STORAGE.value})", source)
        self.assertNotIn("yield", source.lower())

    def test_zero_amounts_are_valid_but_do_not_write_native_resource_attributes(self):
        payment = HELPER.render_payment_function("cdf_free", 1, {"food": 0, "stone": 0}, 10)
        reward = HELPER.render_reward_function(
            "cdf_free_reward", 1, {"food": 0}, {"food": 11}, 12)
        self.assertNotIn("xsPlayerAttribute", payment)
        self.assertNotIn("xsSetPlayerAttribute", payment)
        self.assertIn("xsSetTriggerVariable(10, 1)", payment)
        self.assertNotIn("xsTriggerVariable(11)", reward)
        self.assertNotIn("xsPlayerAttribute", reward)
        self.assertNotIn("xsSetPlayerAttribute", reward)
        self.assertNotIn("xsSetTriggerVariable(11,", reward)
        self.assertIn("xsSetTriggerVariable(12, 1)", reward)

    def test_repeated_receipt_or_completion_returns_before_resource_writes(self):
        payment = HELPER.render_payment_function("cdf_repeat_payment", 1, {"wood": 1}, 7)
        reward = HELPER.render_reward_function(
            "cdf_repeat_reward", 1, {"wood": 1}, {"wood": 8}, 9)
        self.assertLess(payment.index("xsTriggerVariable(7) != 0"), payment.index("xsSetPlayerAttribute"))
        self.assertLess(reward.index("xsTriggerVariable(9) != 0"), reward.index("xsSetTriggerVariable(8,"))

    def test_rejects_bad_names_players_resources_amounts_flags_and_variable_ids(self):
        for name in ("pay", "cdf_bad-name", "cdf_bad;return true", "cdf_ñ", "cdf space", 5):
            with self.subTest(name=name), self.assertRaises(ValueError):
                HELPER.render_payment_function(name, 1, {}, 0)
        for player in (True, False, 0, 9, 1.0, "1"):
            with self.subTest(player=player), self.assertRaises((TypeError, ValueError)):
                HELPER.render_payment_function("cdf_pay", player, {}, 0)
        for variable in (True, False, 1.0, "1", -1, 65_536):
            with self.subTest(receipt=variable), self.assertRaises((TypeError, ValueError)):
                HELPER.render_payment_function("cdf_pay", 1, {}, variable)
            with self.subTest(completion=variable), self.assertRaises((TypeError, ValueError)):
                HELPER.render_reward_function("cdf_reward", 1, {}, {}, variable)
            with self.subTest(reserve=variable), self.assertRaises((TypeError, ValueError)):
                HELPER.render_reward_function("cdf_reward", 1, {"food": 1}, {"food": variable}, 7)
        for amount in (True, False, 1.0, "1", -1, 1_000_000_001):
            with self.subTest(amount=amount), self.assertRaises((TypeError, ValueError)):
                HELPER.render_payment_function("cdf_pay", 1, {"food": amount}, 0)
        for flags in ({True: 1}, {1.0: 1}, {1: True}, {1: 1.0}, {65_536: 1}):
            with self.subTest(flags=flags), self.assertRaises((TypeError, ValueError)):
                HELPER.render_payment_function("cdf_pay", 1, {}, 0, flags)
        with self.assertRaises(ValueError):
            HELPER.render_payment_function("cdf_pay", 1, {"woodland": 2}, 0)

    def test_rejects_aliases_between_state_variables_and_flags(self):
        invalid_calls = [
            lambda: HELPER.render_payment_function("cdf_pay", 1, {}, 3, {3: 0}),
            lambda: HELPER.render_reward_function("cdf_reward", 1, {"food": 1}, {"food": 4}, 4),
            lambda: HELPER.render_reward_function("cdf_reward", 1, {"food": 1}, {"food": 4}, 5, {4: 0}),
            lambda: HELPER.render_reward_function("cdf_reward", 1, {"food": 1}, {"food": 4}, 5, {5: 0}),
            lambda: HELPER.render_reward_function("cdf_reward", 1, {"food": 1, "wood": 1}, {"food": 4, "wood": 4}, 5),
        ]
        for call in invalid_calls:
            with self.subTest(call=call), self.assertRaises(ValueError):
                call()

    def test_reward_requires_exact_resource_to_reserve_binding(self):
        with self.assertRaises(ValueError):
            HELPER.render_reward_function("cdf_reward", 1, {"food": 1}, {}, 8)
        with self.assertRaises(ValueError):
            HELPER.render_reward_function("cdf_reward", 1, {"food": 1}, {"wood": 9}, 8)

    def test_real_parser_embeds_reopens_and_xs_checks_both_functions(self):
        from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

        scenario = AoE2DEScenario.from_default("1.59")
        scenario.map_manager.map_size = 32
        manager = scenario.trigger_manager
        payment_receipt = manager.add_variable("cdf-payment-receipt").variable_id
        completion = manager.add_variable("cdf-reward-completion").variable_id
        reserve_food = manager.add_variable("cdf-reserve-food").variable_id
        reserve_gold = manager.add_variable("cdf-reserve-gold").variable_id
        required_flag = manager.add_variable("cdf-required-flag").variable_id
        source = "\n\n".join([
            HELPER.render_payment_function(
                "cdf_fixture_payment", 1, {"food": 40, "gold": 15}, payment_receipt,
                {required_flag: 1}),
            HELPER.render_reward_function(
                "cdf_fixture_reward", 1, {"food": 7, "wood": 3},
                {"food": reserve_food, "wood": reserve_gold}, completion,
                {required_flag: 1}),
        ])
        scenario.xs_manager.xs_check.raise_on_error = True
        scenario.xs_manager.add_script(xs_string=source)
        scenario.xs_manager.validate(xs=source)

        with tempfile.TemporaryDirectory(prefix="native-resource-xs-") as temporary:
            path = Path(temporary) / "native-resource-transactions.aoe2scenario"
            scenario.write_to_file(str(path))
            reopened = AoE2DEScenario.from_file(str(path), game_version="DE")
            embedded = reopened.xs_manager._get_scenario_xs()
            self.assertIn("bool cdf_fixture_payment()", embedded)
            self.assertIn("bool cdf_fixture_reward()", embedded)
            self.assertIn(f"xsPlayerAttribute(1, {Attribute.FOOD_STORAGE.value})", embedded)
            self.assertIn(f"xsPlayerAttribute(1, {Attribute.GOLD_STORAGE.value})", embedded)
            self.assertIn(f"xsSetPlayerAttribute(1, {Attribute.WOOD_STORAGE.value}", embedded)
            self.assertIn(f"xsTriggerVariable({reserve_food})", embedded)
            self.assertIn(f"xsSetTriggerVariable({completion}, 1)", embedded)
            reopened.xs_manager.xs_check.raise_on_error = True
            reopened.xs_manager.validate(xs=embedded)


if __name__ == "__main__":
    unittest.main()
