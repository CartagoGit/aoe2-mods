"""Fast artificial tests for the isolated large-map diagnostic clone."""

import copy
import hashlib
import json
import runpy
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch
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
                    {"id": "guard", "faction": "player", "type": "militia",
                     "position": {"x": 4, "y": 4}, "essential": True},
                    {"id": "enemy-guard", "faction": "enemy", "type": "militia",
                     "position": {"x": 24, "y": 24}, "essential": False},
                ],
                "factions": [
                    {"id": "player", "player": 1, "role": "human",
                     "strategy": {"limits": "Dos unidades como máximo"}},
                    {"id": "enemy", "player": 2, "role": "enemy",
                     "strategy": {"limits": "Dos unidades como máximo"}},
                ],
                "objectives": [
                    {"id": "prepare", "textKey": "prepare", "location": {"x": 4, "y": 4}},
                    {"id": "defeat-guard", "textKey": "defeat", "location": {"x": 24, "y": 24}},
                ],
                "victory": {"progressKey": "progress.technical-pilot.route-a", "routes": []},
                "defeat": {"essentialUnits": ["guard"], "timeoutSeconds": 600,
                           "arbitration": "defeat-first"},
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
    def test_run_failure_keeps_stdout_and_stderr(self):
        command = [
            sys.executable,
            "-c",
            "import sys; print('stdout sentinel'); print('stderr sentinel', file=sys.stderr); sys.exit(7)",
        ]
        with self.assertRaisesRegex(RuntimeError, r"command failed \(7\)") as caught:
            DIAGNOSTIC["_run"](command)
        self.assertIn("stdout:\nstdout sentinel", str(caught.exception))
        self.assertIn("stderr:\nstderr sentinel", str(caught.exception))

    def test_failed_rerun_invalidates_old_archive_and_receipt(self):
        run = DIAGNOSTIC["run_diagnostic"]
        for variant in ("scale", "transport-observation"):
            for failure in ("export", "zip"):
                with self.subTest(variant=variant, stage=failure), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    source = root / "build/technical-pilot"
                    source.mkdir(parents=True)
                    (source / "campaign-ir.json").write_text(json.dumps(fixture()))
                    (source / "build-report.json").write_text(json.dumps({"sourceSha256": "artificial-source"}))
                    (root / "config").mkdir()
                    (root / "config/engine-catalog.json").write_text(json.dumps({
                        "terrains": ["grass-1", "road", "dirt-1", "snow", "water-deep", "water-shallow", "beach"],
                        "units": ["militia", "transport-ship", "villager-male"]}))
                    for locale in ("en", "es"):
                        path = source / f"mod/resources/{locale}/strings/key-value/key-value-modded-strings-utf8.txt"
                        path.parent.mkdir(parents=True)
                        path.write_text("artificial catalogue")
                    slug = "transport-map-diagnostic" if variant == "transport-observation" else "large-map-diagnostic"
                    archive_stem = f"transport-map-diagnostic-400" if variant == "transport-observation" else "large-map-diagnostic-400"
                    build = root / "build" / slug / "400"
                    build.mkdir(parents=True)
                    receipt = build / "zip-receipt.json"
                    receipt.write_text("stale receipt")
                    archive = root / f"dist/{archive_stem}.zip"
                    archive.parent.mkdir()
                    archive.write_bytes(b"stale archive")
                    calls = []

                    def fake_run(argv):
                        calls.append(argv)
                        if argv[0] == "bun":
                            return {"argv": argv, "exitCode": 0}
                        action = argv[2]
                        if action == "build":
                            if failure == "export":
                                raise RuntimeError("export failure sentinel")
                            export = Path(argv[-1])
                            content = b"artificial bytes for orchestration test only"
                            (export / "01-technical-battle.aoe2scenario").write_bytes(content)
                            (export / "export-report.json").write_text(json.dumps({
                                "gameVerified": False, "scenarioReports": [{"id": "01-technical-battle",
                                "sha256": hashlib.sha256(content).hexdigest()}]}))
                            return {"argv": argv, "exitCode": 0}
                        Path(argv[-1]).write_bytes(b"incomplete zip")
                        raise RuntimeError("zip failure sentinel")

                    with patch.dict(run.__globals__, {"ROOT": root, "_run": fake_run,
                            "inspect_native_diagnostic": lambda *args: {"scope": "orchestration test stub only"}}):
                        with self.assertRaisesRegex(RuntimeError, f"{failure} failure sentinel"):
                            run(400, variant)
                    self.assertFalse(receipt.exists())
                    self.assertFalse(archive.exists())
                    self.assertFalse((root / f"dist/.{archive_stem}.zip.tmp").exists())
                    if failure == "export":
                        self.assertEqual(len(calls), 2)
                        self.assertFalse((build / "kit/diagnostic-report.json").exists())
                    else:
                        self.assertEqual(len(calls), 3)
                        report = json.loads((build / "kit/diagnostic-report.json").read_text())
                        self.assertIn("missing receipt", report["archiveReceiptPolicy"])

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

    def test_transport_observation_geometry_units_and_timeout(self):
        expectations = {
            300: {
                "rectangle": (135, 60, 165, 240),
                "counts": {"grass-1": 84564, "water-deep": 3969, "water-shallow": 1080,
                           "beach": 360, "road": 9, "dirt-1": 9, "snow": 9},
                "ship": {"x": 140, "y": 150}, "passenger": {"x": 132, "y": 150},
                "columns": (2, 22, 6),
            },
            400: {
                "rectangle": (180, 80, 220, 320),
                "counts": {"grass-1": 150364, "water-deep": 7689, "water-shallow": 1440,
                           "beach": 480, "road": 9, "dirt-1": 9, "snow": 9},
                "ship": {"x": 187, "y": 200}, "passenger": {"x": 176, "y": 200},
                "columns": (2, 32, 6),
            },
        }
        for size, expected in expectations.items():
            source = fixture()
            original = copy.deepcopy(source)
            cloned, details = BUILD(source, size, "transport-observation")
            scenario = cloned["scenarios"][0]["scenario"]
            rect = details["transportRectangle"]
            self.assertEqual((rect["xStart"], rect["yStart"], rect["xEndExclusive"],
                              rect["yEndExclusive"]), expected["rectangle"])
            self.assertEqual(details["expectedTerrainCounts"], expected["counts"])
            self.assertEqual(scenario["map"]["width"], size)
            self.assertEqual(scenario["map"]["height"], size)
            cells = [(row["position"]["x"], row["position"]["y"]) for row in scenario["map"]["tiles"]]
            self.assertEqual(len(cells), len(set(cells)))
            self.assertEqual(len(cells), 36 + rect["cellCount"])
            counts = {}
            for row in scenario["map"]["tiles"]:
                counts[row["terrain"]] = counts.get(row["terrain"], 0) + 1
                self.assertEqual(row["elevation"], 0)
                self.assertTrue(0 <= row["position"]["x"] < size)
                self.assertTrue(0 <= row["position"]["y"] < size)
            self.assertEqual(counts, {name: count for name, count in expected["counts"].items()
                                      if name != "grass-1"})
            self.assertEqual((len(rect["beachColumns"]), len(rect["deepColumns"]),
                              len(rect["shallowColumns"])), expected["columns"])
            positions = {unit["id"]: unit["position"] for unit in scenario["units"]}
            self.assertEqual(positions["diagnostic-transport"], expected["ship"])
            self.assertEqual(positions["diagnostic-passenger"], expected["passenger"])
            self.assertEqual(scenario["units"][-2]["type"], "transport-ship")
            self.assertEqual(scenario["units"][-1]["type"], "villager-male")
            self.assertFalse(scenario["units"][-2]["essential"])
            self.assertFalse(scenario["units"][-1]["essential"])
            self.assertEqual(scenario["defeat"]["timeoutSeconds"], 1800)
            self.assertEqual(scenario["defeat"]["essentialUnits"], ["guard"])
            self.assertEqual(scenario["defeat"]["arbitration"], "defeat-first")
            source_scenario = source["scenarios"][0]["scenario"]
            expected_objectives = copy.deepcopy(source_scenario["objectives"])
            for objective in expected_objectives:
                objective["location"] = {
                    axis: (int((objective["location"][axis] * size / 32) + 0.5))
                    for axis in ("x", "y")}
            self.assertEqual(scenario["objectives"], expected_objectives)
            expected_factions = copy.deepcopy(source_scenario["factions"])
            expected_factions[0]["strategy"]["limits"] = (
                "Tres unidades del jugador, incluidas dos unidades de observación no esenciales.")
            self.assertEqual(scenario["factions"], expected_factions)
            tile_map = {(row["position"]["x"], row["position"]["y"]): row["terrain"]
                        for row in scenario["map"]["tiles"]}
            self.assertEqual(tile_map.get((expected["ship"]["x"], expected["ship"]["y"])), "water-deep")
            self.assertEqual(tile_map.get((expected["passenger"]["x"], expected["passenger"]["y"]), "grass-1"),
                             "grass-1")
            for y400 in (60, 340):
                y = int((y400 * size / 400) + 0.5)
                x = (rect["xStart"] + rect["xEndExclusive"] - 1) // 2
                self.assertNotIn((x, y), tile_map)
                self.assertNotIn(y, range(rect["yStart"], rect["yEndExclusive"]))
            self.assertEqual(source, original)
            self.assertEqual(scenario["victory"]["routes"], [])
            self.assertNotIn("progressKey", scenario["victory"])

    def test_transport_variant_rejects_source_drift_and_unknown_variant(self):
        source = fixture()
        source["scenarios"][0]["scenario"]["defeat"]["timeoutSeconds"] = 900
        with self.assertRaisesRegex(ValueError, "source drift.*timeout"):
            BUILD(source, 400, "transport-observation")
        with self.assertRaisesRegex(ValueError, "variant"):
            BUILD(fixture(), 400, "some-other-mode")

    def test_transport_readme_keeps_manual_observations_pending(self):
        _, details = BUILD(fixture(), 400, "transport-observation")
        readme = DIAGNOSTIC["_kit_readme"](400, details)
        for required in ("1800-second timeout", "ordinary boarding", "passenger actually inside the boat",
                         "unloading on the opposite side", "north and south land detours",
                         "deletion of the boat", "before boarding, aboard, and after unloading",
                         "without assuming passenger death or survival", "different filename",
                         "Identical bytes may have an identical hash", "the included original still matches"):
            self.assertIn(required, readme)
        self.assertNotIn("diagonal toward the enemy", readme)

    def test_native_defeat_trigger_must_target_original_guard_reference(self):
        verify = DIAGNOSTIC["_verify_native_defeat_binding"]
        destroy_condition = SimpleNamespace(condition_type=6, unit_object=41, timer=None)
        timeout_condition = SimpleNamespace(condition_type=10, unit_object=None, timer=1800)
        triggers = [
            SimpleNamespace(name="cdf-defeat-guard", conditions=[destroy_condition]),
            SimpleNamespace(name="cdf-defeat-1800", conditions=[timeout_condition]),
        ]
        binding = verify(triggers, 41, 6, 10, 1800)
        self.assertTrue(binding["linkedToOriginalGuard"])
        self.assertEqual(binding["unitReferenceId"], 41)
        destroy_condition.unit_object = 42
        with self.assertRaisesRegex(RuntimeError, "not bound to the original guard"):
            verify(triggers, 41, 6, 10, 1800)

        bad_timer_type = SimpleNamespace(condition_type=0, unit_object=None, timer=1800)
        with self.assertRaisesRegex(RuntimeError, "timeout defeat condition"):
            verify([SimpleNamespace(name="cdf-defeat-guard", conditions=[destroy_condition]),
                    SimpleNamespace(name="cdf-defeat-1800", conditions=[bad_timer_type])],
                   42, 6, 10, 1800)

        moved_destroy = SimpleNamespace(condition_type=6, unit_object=42, timer=None)
        triggers = [
            SimpleNamespace(name="cdf-defeat-guard", conditions=[]),
            SimpleNamespace(name="cdf-defeat-1800", conditions=[timeout_condition, moved_destroy]),
        ]
        with self.assertRaisesRegex(RuntimeError, "not bound to the original guard"):
            verify(triggers, 41, 6, 10, 1800)

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
