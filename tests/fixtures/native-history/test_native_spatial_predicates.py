"""Focused validation and real-parser checks for generated native XS predicates."""

import importlib.util
import math
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER_PATH = ROOT / "tools/python/native_spatial.helper.py"
SPEC = importlib.util.spec_from_file_location("native_spatial_helper", HELPER_PATH)
HELPER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HELPER)


class NativeSpatialPredicateTests(unittest.TestCase):
    def test_alive_predicate_accepts_uid_zero_and_checks_real_existence_health_and_owner(self):
        source = HELPER.render_unit_alive_predicate("cdf_guard_alive", 0, 2)
        self.assertIn("xsTriggerVariable(0)", source)
        self.assertIn("if (cdf_unit_id < 0)", source)
        self.assertNotIn("cdf_unit_id <= 0", source)
        self.assertIn("xsDoesUnitExist(cdf_unit_id)", source)
        self.assertIn("xsGetUnitHitpoints(cdf_unit_id) <= 0.0", source)
        self.assertIn("xsGetWorldPlayerId(2)", source)
        self.assertIn("xsGetUnitOwner(cdf_unit_id) != cdf_expected_owner", source)
        self.assertNotIn("xsSet", source)

    def test_gaia_owner_uses_zero_without_world_player_remapping(self):
        source = HELPER.render_unit_alive_predicate("cdf_gaia_alive", 4, 0)
        self.assertIn("xsGetUnitOwner(cdf_unit_id) != 0", source)
        self.assertNotIn("xsGetWorldPlayerId", source)

    def test_circle_predicate_uses_real_position_squared_distance_and_garrison_state(self):
        x = 10.1234567890123
        y = 20.9876543210987
        radius = 3.14159265358979
        source = HELPER.render_unit_circle_predicate("cdf_near_site", 0, 1, x, y, radius, 64)
        self.assertIn("xsGetGarrisonedInUnitId(cdf_unit_id) >= 0", source)
        self.assertIn("xsGetUnitPosition(cdf_unit_id)", source)
        self.assertIn("xsVectorGetX(cdf_unit_position)", source)
        self.assertIn("xsVectorGetY(cdf_unit_position)", source)
        self.assertIn(f"{x:.17g}", source)
        self.assertIn(f"{y:.17g}", source)
        self.assertIn(f"{radius * radius:.17g}", source)
        self.assertIn("(cdf_dx * cdf_dx + cdf_dy * cdf_dy) <=", source)
        self.assertNotIn("xsSet", source)

    def test_circle_boundary_is_inclusive_and_radius_is_not_a_square(self):
        source = HELPER.render_unit_circle_predicate("cdf_circle_edge", 3, 1, 5, 5, 2, 16)
        self.assertIn("<= 4.0", source)
        self.assertNotIn("abs(", source)
        self.assertNotIn("cdf_dx <=", source)

    def test_rejects_malformed_function_names_and_integer_fields(self):
        for name in ("alive", "cdf_bad-name", "cdf_bad;return true", "cdf_ñ", "cdf space", 7):
            with self.subTest(name=name), self.assertRaises(ValueError):
                HELPER.render_unit_alive_predicate(name, 0, 1)
        for value in (True, False, 1.0, "1", None):
            with self.subTest(handle_variable=value), self.assertRaises(TypeError):
                HELPER.render_unit_alive_predicate("cdf_alive", value, 1)
            with self.subTest(player=value), self.assertRaises(TypeError):
                HELPER.render_unit_alive_predicate("cdf_alive", 1, value)

    def test_rejects_integer_ranges_and_exact_map_size(self):
        for handle_variable in (-1, 2_147_483_648):
            with self.subTest(handle_variable=handle_variable), self.assertRaises(ValueError):
                HELPER.render_unit_alive_predicate("cdf_alive", handle_variable, 1)
        for player in (-1, 9):
            with self.subTest(player=player), self.assertRaises(ValueError):
                HELPER.render_unit_alive_predicate("cdf_alive", 1, player)
        for map_size in (True, False, 32.0, "32", 0, 481):
            with self.subTest(map_size=map_size), self.assertRaises((TypeError, ValueError)):
                HELPER.render_unit_circle_predicate("cdf_circle", 1, 1, 5, 5, 2, map_size)

    def test_rejects_nonfinite_and_nonnumber_circle_inputs(self):
        for value in (True, False, "2", None, math.nan, math.inf, -math.inf, 10**400):
            for field in ("x", "y", "radius"):
                args = {"x": 5, "y": 5, "radius": 2}
                args[field] = value
                with self.subTest(field=field, value=value), self.assertRaises((TypeError, ValueError)):
                    HELPER.render_unit_circle_predicate("cdf_circle", 1, 1,
                                                        args["x"], args["y"], args["radius"], 32)

    def test_rejects_zero_radius_outside_center_and_circle_past_map_edges(self):
        invalid = [
            (5, 5, 0, 32),
            (5, 5, -1, 32),
            (5, 5, 33, 32),
            (-0.1, 5, 1, 32),
            (32, 5, 1, 32),
            (2, 5, 3, 32),
            (5, 29.1, 3, 32),
        ]
        for x, y, radius, size in invalid:
            with self.subTest(x=x, y=y, radius=radius, size=size), self.assertRaises(ValueError):
                HELPER.render_unit_circle_predicate("cdf_circle", 1, 1, x, y, radius, size)

    def test_real_parser_scenario_embeds_and_checks_uid_zero_and_negative_fixtures(self):
        from AoE2ScenarioParser.datasets.trigger_lists import Operation
        from AoE2ScenarioParser.datasets.units import UnitInfo
        from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

        scenario = AoE2DEScenario.from_default("1.59")
        scenario.map_manager.map_size = 32
        unit = scenario.unit_manager.add_unit(
            player=1, unit_const=UnitInfo.MILITIA.ID, x=10.5, y=10.5)
        self.assertEqual(unit.reference_id, 0, "the real parser fixture must exercise valid UID zero")
        manager = scenario.trigger_manager
        zero_handle = manager.add_variable("cdf-fixture-uid-zero").variable_id
        negative_handle = manager.add_variable("cdf-fixture-uid-negative").variable_id
        initialise = manager.add_trigger("cdf-fixture-native-handles", enabled=True, looping=False)
        initialise.new_effect.change_variable(variable=zero_handle, quantity=unit.reference_id,
                                              operation=Operation.SET)
        initialise.new_effect.change_variable(variable=negative_handle, quantity=-1,
                                              operation=Operation.SET)
        source = "\n\n".join([
            HELPER.render_unit_alive_predicate("cdf_fixture_zero_alive", zero_handle, 1),
            HELPER.render_unit_alive_predicate("cdf_fixture_negative_alive", negative_handle, 1),
            HELPER.render_unit_circle_predicate("cdf_fixture_in_circle", zero_handle, 1,
                                                10.5, 10.5, 2.0, 32),
            HELPER.render_unit_circle_predicate("cdf_fixture_small_radius", zero_handle, 1,
                                                0.00000001, 0.5, 0.00000001, 32),
        ])
        scenario.xs_manager.xs_check.raise_on_error = True
        scenario.xs_manager.add_script(xs_string=source)
        scenario.xs_manager.validate(xs=source)

        with tempfile.TemporaryDirectory(prefix="native-spatial-xs-") as temporary:
            path = Path(temporary) / "native-spatial-predicates.aoe2scenario"
            scenario.write_to_file(str(path))
            reopened = AoE2DEScenario.from_file(str(path), game_version="DE")
            embedded = reopened.xs_manager._get_scenario_xs()
            self.assertIn("bool cdf_fixture_zero_alive()", embedded)
            self.assertIn("bool cdf_fixture_negative_alive()", embedded)
            self.assertIn("bool cdf_fixture_small_radius()", embedded)
            self.assertIn("xsTriggerVariable(0)", embedded)
            self.assertIn("xsTriggerVariable(1)", embedded)
            self.assertIn("xsGetGarrisonedInUnitId(cdf_unit_id) >= 0", embedded)
            self.assertIn("0.00000001", embedded)
            self.assertIn("0.0000000000000001", embedded)
            self.assertNotIn("e-", embedded)
            self.assertEqual(reopened.map_manager.map_size, 32)
            self.assertEqual(reopened.unit_manager.units[1][0].reference_id, 0)
            self.assertEqual((reopened.unit_manager.units[1][0].x,
                              reopened.unit_manager.units[1][0].y), (10.5, 10.5))
            loaded_initialise = next(trigger for trigger in reopened.trigger_manager.triggers
                                     if trigger.name == "cdf-fixture-native-handles")
            self.assertEqual([effect.quantity for effect in loaded_initialise.effects], [0, -1])
            reopened.xs_manager.xs_check.raise_on_error = True
            reopened.xs_manager.validate(xs=embedded)


if __name__ == "__main__":
    unittest.main()
