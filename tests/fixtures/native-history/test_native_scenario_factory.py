"""Pruebas directas de la base nativa compartida con el analizador fijado real.

Solo accredited native serialization: build a base envelope, reopen it and check
the real manager state. No gameplay, balance, difficulty or engine evidence.
"""
import contextlib
import copy
import io
from pathlib import Path
import runpy
import tempfile
import unittest

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState, VictoryCondition
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

ROOT = Path(__file__).resolve().parents[3]
FACTORY = runpy.run_path(str(ROOT / "tools/python/native_scenario.factory.py"))
EXPORTER = runpy.run_path(str(ROOT / "tools/python/export_aoe2.py"))
create_native_scenario_base = FACTORY["create_native_scenario_base"]
enum_name = FACTORY["enum_name"]
unit_id = FACTORY["unit_id"]
export_scenario = EXPORTER["export_scenario"]

VERSION = "1.59"
WIDTH = 16
OVERRIDE = {"x": 2, "y": 3}
BLOCKED = {"x": 5, "y": 6}
MESSAGE_IDS = {"victory": 1900000120, "hints": 1900000121}
OBJECTIVE_IDS = {"prepare": 1900000101, "defeat-raid": 1900000102}
LINE_IDS = {"intro-line": 1900000110}


def base_ir():
    """A small known v1 base: two factions, two typed units, one terrain override."""
    return {
        "schemaVersion": 1,
        "messageIds": dict(MESSAGE_IDS),
        "objectiveIds": dict(OBJECTIVE_IDS),
        "lineIds": dict(LINE_IDS),
        "unitNameIds": {},
        "factionNameIds": {},
        "scenario": {
            "id": "native-base-fixture",
            "map": {
                "width": WIDTH,
                "height": WIDTH,
                "baseTerrain": "grass-1",
                "tiles": [{"position": dict(OVERRIDE), "terrain": "dirt-1", "elevation": 2}],
                "blocked": [dict(BLOCKED)],
                "start": {"x": 1, "y": 1},
            },
            "units": [
                {"id": "scout", "faction": "player", "type": "militia",
                 "position": {"x": 1, "y": 1}, "essential": True},
                {"id": "raider", "faction": "enemy", "type": "militia",
                 "position": {"x": 12, "y": 12}, "essential": False},
            ],
            "factions": [
                {"id": "player", "player": 1, "civilization": "byzantines", "role": "human",
                 "economy": {"model": "finite-reserve",
                             "initial": {"food": 200, "wood": 150, "gold": 100, "stone": 50}}},
                {"id": "enemy", "player": 2, "civilization": "byzantines", "role": "enemy",
                 "economy": {"model": "finite-reserve",
                             "initial": {"food": 120, "wood": 90, "gold": 60, "stone": 30}}},
            ],
            "technologies": [],
            "objectives": [
                {"id": "prepare", "requires": [], "completion": {"type": "timer", "seconds": 5}},
                {"id": "defeat-raid", "requires": ["prepare"],
                 "completion": {"type": "destroy", "unit": "raider"}},
            ],
            "variables": [{"id": "choice", "initial": 0}],
            "defeat": {"essentialUnits": ["scout"], "timeoutSeconds": 600},
            "victory": {"objectives": ["prepare", "defeat-raid"],
                        "progressKey": "progress.native-base-fixture"},
            "balance": {
                profile: {"resources": {"food": 200, "wood": 200, "gold": 100, "stone": 100},
                          "enemyReactionSeconds": 30, "hints": profile == "easy"}
                for profile in ("easy", "standard", "hard")
            },
            "narrative": {"intro": [{"id": "intro-line", "durationSeconds": 3}],
                          "events": [], "outro": []},
            "triggers": [],
        },
    }


def quiet(action, *args, **kwargs):
    with contextlib.redirect_stdout(io.StringIO()):
        return action(*args, **kwargs)


def units_by_reference(scenario):
    return {unit.reference_id: unit for unit in scenario.unit_manager.get_all_units()}


class NativeScenarioFactoryTests(unittest.TestCase):
    def test_base_manager_state_matches_the_declared_envelope(self):
        ir = base_ir()
        scenario, units, factions = quiet(create_native_scenario_base, ir, VERSION)
        self.assertEqual(scenario.map_manager.map_size, WIDTH)
        self.assertEqual(len(scenario.map_manager.terrain), WIDTH * WIDTH)
        self.assertEqual(int(TerrainId.GRASS_1),
                         scenario.map_manager.get_tile(0, 0).terrain_id)
        self.assertEqual(int(TerrainId.GRASS_1),
                         scenario.map_manager.get_tile(WIDTH - 1, WIDTH - 1).terrain_id)
        self.assertEqual(int(TerrainId.DIRT_1),
                         scenario.map_manager.get_tile(OVERRIDE["x"], OVERRIDE["y"]).terrain_id)
        self.assertEqual(2, scenario.map_manager.get_tile(OVERRIDE["x"], OVERRIDE["y"]).elevation)
        self.assertEqual(0, scenario.map_manager.get_tile(0, 0).elevation)
        self.assertEqual(scenario.option_manager.victory_condition, VictoryCondition.CUSTOM)
        self.assertTrue(scenario.option_manager.victory_custom_conditions_required)
        self.assertTrue(scenario.option_manager.lock_teams)
        self.assertFalse(scenario.option_manager.allow_players_choose_teams)
        self.assertEqual(MESSAGE_IDS["victory"], scenario.message_manager.victory_string_table_id)
        self.assertEqual(MESSAGE_IDS["hints"], scenario.message_manager.hints_string_table_id)
        self.assertEqual(2, scenario.player_manager.active_players)
        human = scenario.player_manager.players[1]
        rival = scenario.player_manager.players[2]
        self.assertTrue(human.human)
        self.assertFalse(rival.human)
        self.assertEqual(Civilization.BYZANTINES, human.civilization)
        self.assertTrue(human.lock_civ)
        self.assertTrue(human.lock_personality)
        self.assertEqual(200, human.population_cap)
        self.assertEqual(200, rival.population_cap)
        self.assertEqual((200, 150, 100, 50),
                         (human.food, human.wood, human.gold, human.stone))
        self.assertEqual((120, 90, 60, 30),
                         (rival.food, rival.wood, rival.gold, rival.stone))
        self.assertEqual((1, 1), (human.initial_player_view_x, human.initial_player_view_y))
        self.assertEqual(int(DiplomacyState.ENEMY), human.diplomacy[2])
        self.assertEqual(int(DiplomacyState.ENEMY), rival.diplomacy[1])
        self.assertEqual({"player", "enemy"}, set(factions))
        self.assertEqual(2, factions["enemy"]["player"])
        self.assertEqual({"scout", "raider"}, set(units))
        placed = units_by_reference(scenario)
        scout = placed[units["scout"]]
        raider = placed[units["raider"]]
        self.assertEqual(UnitInfo.MILITIA.ID, scout.unit_const)
        self.assertEqual(UnitInfo.MILITIA.ID, raider.unit_const)
        self.assertEqual(1, scout.player)
        self.assertEqual(2, raider.player)
        self.assertEqual((1.5, 1.5), (scout.x, scout.y))
        self.assertEqual((12.5, 12.5), (raider.x, raider.y))
        wall = [unit for unit in placed.values() if unit.unit_const == BuildingInfo.STONE_WALL.ID]
        self.assertEqual(1, len(wall))
        self.assertEqual(0, wall[0].player)
        self.assertEqual((BLOCKED["x"] + 0.5, BLOCKED["y"] + 0.5), (wall[0].x, wall[0].y))
        self.assertLess(units["scout"], units["raider"])
        self.assertLess(units["raider"], wall[0].reference_id)

    def test_base_creates_no_gameplay_objective_or_progress_triggers(self):
        scenario, _, _ = quiet(create_native_scenario_base, base_ir(), VERSION)
        self.assertEqual([], list(scenario.trigger_manager.triggers))
        self.assertEqual([], list(scenario.trigger_manager.variables))

    def test_reopened_file_preserves_the_base(self):
        ir = base_ir()
        scenario, units, _ = quiet(create_native_scenario_base, ir, VERSION)
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / "base.aoe2scenario"
            quiet(scenario.write_to_file, str(out))
            self.assertTrue(out.is_file())
            reopened = quiet(AoE2DEScenario.from_file, str(out))
            self.assertEqual(WIDTH, reopened.map_manager.map_size)
            self.assertEqual(int(TerrainId.GRASS_1), reopened.map_manager.get_tile(0, 0).terrain_id)
            self.assertEqual(int(TerrainId.DIRT_1),
                             reopened.map_manager.get_tile(OVERRIDE["x"], OVERRIDE["y"]).terrain_id)
            self.assertEqual(2,
                             reopened.map_manager.get_tile(OVERRIDE["x"], OVERRIDE["y"]).elevation)
            self.assertEqual(VictoryCondition.CUSTOM, reopened.option_manager.victory_condition)
            self.assertTrue(reopened.option_manager.lock_teams)
            self.assertFalse(reopened.option_manager.allow_players_choose_teams)
            self.assertEqual(MESSAGE_IDS["victory"],
                             reopened.message_manager.victory_string_table_id)
            human = reopened.player_manager.players[1]
            rival = reopened.player_manager.players[2]
            self.assertEqual((200, 150, 100, 50),
                             (human.food, human.wood, human.gold, human.stone))
            self.assertEqual((120, 90, 60, 30),
                             (rival.food, rival.wood, rival.gold, rival.stone))
            self.assertEqual(int(DiplomacyState.ENEMY), human.diplomacy[2])
            self.assertEqual(int(DiplomacyState.ENEMY), rival.diplomacy[1])
            placed = units_by_reference(reopened)
            wall_ids = {unit.reference_id for unit in placed.values()
                        if unit.unit_const == BuildingInfo.STONE_WALL.ID}
            self.assertEqual({*units.values(), *wall_ids}, set(placed))
            scout = placed[units["scout"]]
            raider = placed[units["raider"]]
            self.assertEqual(UnitInfo.MILITIA.ID, scout.unit_const)
            self.assertEqual(1, scout.player)
            self.assertEqual((1.5, 1.5), (scout.x, scout.y))
            self.assertEqual(2, raider.player)
            self.assertEqual((12.5, 12.5), (raider.x, raider.y))
            self.assertEqual([], list(reopened.trigger_manager.triggers))

    def test_building_leaves_the_source_ir_unchanged(self):
        ir = base_ir()
        original = copy.deepcopy(ir)
        quiet(create_native_scenario_base, ir, VERSION)
        self.assertEqual(original, ir)

    def test_unsupported_inputs_are_rejected_before_any_written_artifact(self):
        nonsquare = base_ir()
        nonsquare["scenario"]["map"]["height"] = WIDTH + 1
        composed_version = base_ir()
        composed_version["schemaVersion"] = 2
        composed_capability = base_ir()
        composed_capability["capability"] = {"schemaVersion": 3}
        composed_profile = base_ir()
        composed_profile["scenario"]["capabilityProfile"] = {"schemaVersion": 3}
        unknown_version = base_ir()
        unknown_version["schemaVersion"] = 3
        economic_ai = base_ir()
        economic_ai["scenario"]["factions"][1]["economy"]["model"] = "scripted"
        for ir, message in (
            (nonsquare, "mapa cuadrado"),
            (composed_version, "schemaVersion 1"),
            (composed_capability, "perfiles de capacidad"),
            (composed_profile, "perfiles de capacidad"),
            (unknown_version, "schemaVersion 1"),
            (economic_ai, "aiScript PER explícito"),
        ):
            with self.subTest(message=message):
                with self.assertRaisesRegex(ValueError, message):
                    quiet(create_native_scenario_base, ir, VERSION)
                with tempfile.TemporaryDirectory() as temporary:
                    out = Path(temporary) / "rejected.aoe2scenario"
                    with self.assertRaises(ValueError):
                        quiet(export_scenario, ir, out, VERSION)
                    self.assertFalse(out.exists())

    def test_legacy_exporter_keeps_its_unsupported_profile_diagnostic(self):
        composed = base_ir()
        composed["schemaVersion"] = 2
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / "composed.aoe2scenario"
            with self.assertRaisesRegex(ValueError, "capability-not-implemented"):
                quiet(export_scenario, composed, out, VERSION)
            self.assertFalse(out.exists())
        profile = base_ir()
        profile["scenario"]["capabilityProfile"] = {"schemaVersion": 3}
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / "profile.aoe2scenario"
            with self.assertRaisesRegex(ValueError, "capability-not-implemented"):
                quiet(export_scenario, profile, out, VERSION)
            self.assertFalse(out.exists())

    def test_legacy_exporter_still_exports_the_same_base(self):
        ir = base_ir()
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / "legacy.aoe2scenario"
            report = quiet(export_scenario, ir, out, VERSION)
            self.assertEqual("native-base-fixture", report["id"])
            self.assertEqual(2, report["units"])
            self.assertGreater(report["triggers"], 0)
            reopened = quiet(AoE2DEScenario.from_file, str(out))
            self.assertEqual(WIDTH, reopened.map_manager.map_size)
            self.assertEqual(int(TerrainId.DIRT_1),
                             reopened.map_manager.get_tile(OVERRIDE["x"], OVERRIDE["y"]).terrain_id)
            self.assertEqual(2,
                             reopened.map_manager.get_tile(OVERRIDE["x"], OVERRIDE["y"]).elevation)
            self.assertEqual((200, 150, 100, 50),
                             (reopened.player_manager.players[1].food,
                              reopened.player_manager.players[1].wood,
                              reopened.player_manager.players[1].gold,
                              reopened.player_manager.players[1].stone))
            wall = [unit for unit in reopened.unit_manager.get_all_units()
                    if unit.unit_const == BuildingInfo.STONE_WALL.ID]
            self.assertEqual(1, len(wall))
            self.assertEqual((BLOCKED["x"] + 0.5, BLOCKED["y"] + 0.5), (wall[0].x, wall[0].y))
            names = [trigger.name for trigger in reopened.trigger_manager.triggers]
            self.assertIn("cdf-initialize", names)
            self.assertIn("cdf-objective-prepare", names)

    def test_enum_resolution_stays_shared_by_the_exporter(self):
        self.assertEqual("STONE_WALL", enum_name("stone-wall"))
        self.assertEqual(BuildingInfo.STONE_WALL.ID, unit_id("stone-wall"))
        self.assertEqual(UnitInfo.MILITIA.ID, unit_id("militia"))
        self.assertEqual(BuildingInfo.STONE_WALL.ID, EXPORTER["unit_id"]("stone-wall"))
        self.assertEqual("STONE_WALL", EXPORTER["enum_name"]("stone-wall"))
        with self.assertRaisesRegex(ValueError, "Unidad no soportada"):
            unit_id("not-a-unit")


if __name__ == "__main__":
    unittest.main()
