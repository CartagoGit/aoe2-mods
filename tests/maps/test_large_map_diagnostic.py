"""Fast artificial tests for the isolated large-map diagnostic clone."""

import copy
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DIAGNOSTIC = runpy.run_path(str(ROOT / "tools/map/large-map-diagnostic.script.py"))
BUILD = DIAGNOSTIC["build_diagnostic_ir"]
MARKERS = DIAGNOSTIC["_marker_cells"]


def fixture():
    return {
        "schemaVersion": 1,
        "id": "technical-pilot",
        "mode": "aoe2-de",
        "internalName": "CDF_TechnicalPilot",
        "messages": {"intro": "keep this text"},
        "scenarios": [{
            "schemaVersion": 1,
            "scenario": {
                "schemaVersion": 1,
                "id": "01-technical-battle",
                "mechanic": "battle",
                "titleKey": "scenario.technical-battle.title",
                "narrative": {"intro": [{"position": {"x": 7, "y": 8}, "textKey": "unchanged"}]},
                "map": {
                    "width": 32, "height": 32, "baseTerrain": "grass-1",
                    "tiles": [], "blocked": [], "start": {"x": 4, "y": 4},
                },
                "units": [
                    {"id": "guard", "type": "militia", "position": {"x": 4, "y": 4}},
                    {"id": "enemy-guard", "type": "militia", "position": {"x": 24, "y": 24}},
                ],
                "objectives": [
                    {"id": "prepare", "textKey": "prepare", "location": {"x": 4, "y": 4}},
                    {"id": "defeat-guard", "textKey": "defeat", "location": {"x": 24, "y": 24}},
                ],
                "victory": {"progressKey": "progress.technical-pilot.route-a", "routes": []},
                "triggers": [],
            },
        }],
    }


def changed_paths(before, after, path=""):
    if isinstance(before, dict) and isinstance(after, dict):
        result = []
        for key in sorted(set(before) | set(after)):
            child = f"{path}.{key}" if path else key
            if key not in before or key not in after:
                result.append(child)
            else:
                result.extend(changed_paths(before[key], after[key], child))
        return result
    if isinstance(before, list) and isinstance(after, list):
        if len(before) != len(after):
            return [path]
        return [child for index, (left, right) in enumerate(zip(before, after))
                for child in changed_paths(left, right, f"{path}[{index}]")]
    return [] if before == after else [path]


class LargeMapDiagnosticTests(unittest.TestCase):
    def test_fixed_transform_markers_and_clone_only_progress_removal(self):
        source = fixture()
        original = copy.deepcopy(source)
        transformed, details = BUILD(source, 400)
        scenario = transformed["scenarios"][0]["scenario"]
        self.assertEqual(source, original)
        self.assertEqual(scenario["map"]["start"], {"x": 50, "y": 50})
        self.assertEqual({row["id"]: row["position"] for row in scenario["units"]}, {
            "guard": {"x": 50, "y": 50}, "enemy-guard": {"x": 300, "y": 300},
        })
        self.assertEqual({row["id"]: row["location"] for row in scenario["objectives"]}, {
            "prepare": {"x": 50, "y": 50}, "defeat-guard": {"x": 300, "y": 300},
        })
        self.assertEqual((scenario["map"]["width"], scenario["map"]["height"]), (400, 400))
        self.assertNotIn("progressKey", scenario["victory"])
        self.assertIn("progressKey", source["scenarios"][0]["scenario"]["victory"])
        self.assertEqual(details["markerCellCount"], 36)
        self.assertEqual(len({(row["position"]["x"], row["position"]["y"])
                              for row in scenario["map"]["tiles"]}), 36)
        terrain_counts = {}
        for row in scenario["map"]["tiles"]:
            terrain_counts[row["terrain"]] = terrain_counts.get(row["terrain"], 0) + 1
            self.assertEqual(row["elevation"], 0)
            self.assertTrue(0 <= row["position"]["x"] < 400)
            self.assertTrue(0 <= row["position"]["y"] < 400)
        self.assertEqual(terrain_counts, {"road": 9, "dirt-1": 9, "snow": 9, "water-deep": 9})
        water_cells = [row["position"] for row in scenario["map"]["tiles"]
                       if row["terrain"] == "water-deep"]
        self.assertTrue(all(cell["x"] != cell["y"] for cell in water_cells))
        allowed = {
            "scenarios[0].scenario.map.width", "scenarios[0].scenario.map.height",
            "scenarios[0].scenario.map.start.x", "scenarios[0].scenario.map.start.y",
            "scenarios[0].scenario.map.tiles", "scenarios[0].scenario.victory.progressKey",
        }
        allowed.update(f"scenarios[0].scenario.units[{index}].position.{axis}"
                       for index in range(2) for axis in ("x", "y"))
        allowed.update(f"scenarios[0].scenario.objectives[{index}].location.{axis}"
                       for index in range(2) for axis in ("x", "y"))
        self.assertEqual(set(changed_paths(original, transformed)), allowed)
        self.assertEqual(scenario["narrative"]["intro"][0]["position"], {"x": 7, "y": 8})
        self.assertEqual(scenario["titleKey"], "scenario.technical-battle.title")

    def test_300_rounding_and_marker_positions_are_fixed(self):
        transformed, details = BUILD(fixture(), 300)
        scenario = transformed["scenarios"][0]["scenario"]
        self.assertEqual(scenario["map"]["start"], {"x": 38, "y": 38})
        self.assertEqual(scenario["units"][1]["position"], {"x": 225, "y": 225})
        self.assertEqual([row["centre"] for row in details["markers"]],
                         [[150, 15], [285, 150], [150, 285], [15, 150]])
        self.assertEqual(len({tuple(cell) for row in details["markers"] for cell in row["cells"]}), 36)

    def test_rejects_bad_sizes_before_transform(self):
        for size in (True, False, 300.0, "400", 299, 401, None):
            with self.subTest(size=size), self.assertRaisesRegex(ValueError, "size"):
                BUILD(fixture(), size)

    def test_rejects_unknown_or_unsupported_ir_shapes(self):
        cases = []
        bad = fixture(); bad["id"] = "another-campaign"; cases.append((bad, "only the aoe2-de technical-pilot"))
        bad = fixture(); bad["scenarios"].append(copy.deepcopy(bad["scenarios"][0])); cases.append((bad, "exactly one"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["map"]["width"] = 31; cases.append((bad, "square 32"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["map"]["width"] = 32.0; cases.append((bad, "square 32"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["map"]["tiles"] = [{"position": {"x": 1, "y": 1}}]; cases.append((bad, "tiles and blocked"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["triggers"] = [{"id": "authored"}]; cases.append((bad, "authored triggers"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["victory"]["routes"] = [{"id": "route"}]; cases.append((bad, "alternative routes"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["capabilityProfile"] = {}; cases.append((bad, "capability profiles"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["map"]["capabilityProfile"] = {}; cases.append((bad, "tiles and blocked"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["units"][0]["position"]["x"] = True; cases.append((bad, "integer 0..31"))
        bad = fixture(); bad["schemaVersion"] = True; cases.append((bad, "schemaVersion 1"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["units"][0] = None; cases.append((bad, "guard and enemy-guard"))
        bad = fixture(); bad["scenarios"][0]["scenario"]["objectives"][0] = None; cases.append((bad, "prepare and defeat-guard"))
        for source, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                BUILD(source, 400)


if __name__ == "__main__":
    unittest.main()
