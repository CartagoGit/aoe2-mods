"""Build a private, sparse technical-pilot scenario at 300 or 400 tiles.

The clone keeps the existing technical-pilot identities and game data. It adds
only four artificial terrain markers and deliberately does not model geography.
"""

import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SIZE = 400
BASE_SIZE = 32
SOURCE_CAMPAIGN = "technical-pilot"
SOURCE_SCENARIO = "01-technical-battle"
MARKERS_400 = (
    ("data-north", 200, 20, "road"),
    ("data-east", 380, 200, "dirt-1"),
    ("data-south", 200, 380, "snow"),
    ("data-west", 20, 200, "water-deep"),
)
TRANSPORT_RECTANGLE_400 = (180, 80, 220, 320)  # half-open x0,y0,x1,y1
TRANSPORT_UNITS_400 = (
    {"id": "diagnostic-transport", "type": "transport-ship", "faction": "player", "x": 187, "y": 200},
    {"id": "diagnostic-passenger", "type": "villager-male", "faction": "player", "x": 176, "y": 200},
)


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _coordinate(value, label):
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < BASE_SIZE:
        raise ValueError(f"unsupported technical-pilot coordinate at {label}: expected integer 0..31")
    return value


def _schema_v1(value):
    return type(value) is int and value == 1


def _scale(value, size):
    return math.floor(value * size / BASE_SIZE + 0.5)


def _scale_marker(value_400, size):
    return math.floor(value_400 * size / 400 + 0.5)


def _scale_pair(point, label, size):
    if not isinstance(point, dict) or set(point) != {"x", "y"}:
        raise ValueError(f"unsupported technical-pilot coordinate shape at {label}")
    return {"x": _scale(_coordinate(point["x"], f"{label}.x"), size),
            "y": _scale(_coordinate(point["y"], f"{label}.y"), size)}


def validate_diagnostic_source(source):
    """Accept only the known, single-scenario technical fixture shape."""
    if not isinstance(source, dict) or not _schema_v1(source.get("schemaVersion")):
        raise ValueError("unsupported source: expected schemaVersion 1 campaign IR")
    if source.get("id") != SOURCE_CAMPAIGN or source.get("mode") != "aoe2-de":
        raise ValueError("unsupported source: only the aoe2-de technical-pilot campaign is accepted")
    if "capabilityProfile" in source or source.get("capability"):
        raise ValueError("unsupported source: capability profiles are not accepted by the diagnostic")
    scenarios = source.get("scenarios")
    if not isinstance(scenarios, list) or len(scenarios) != 1:
        raise ValueError("unsupported source: expected exactly one technical-pilot scenario")
    entry = scenarios[0]
    if not isinstance(entry, dict) or not _schema_v1(entry.get("schemaVersion")):
        raise ValueError("unsupported source: scenario wrapper must use schemaVersion 1")
    if "capabilityProfile" in entry or entry.get("capability"):
        raise ValueError("unsupported source: scenario wrapper capability profiles are not accepted")
    scenario = entry.get("scenario")
    if (not isinstance(scenario, dict) or not _schema_v1(scenario.get("schemaVersion"))
            or scenario.get("id") != SOURCE_SCENARIO):
        raise ValueError("unsupported source: expected 01-technical-battle")
    if "capabilityProfile" in scenario or scenario.get("capability"):
        raise ValueError("unsupported source: scenario capability profiles are not accepted")

    map_spec = scenario.get("map")
    if (not isinstance(map_spec, dict) or type(map_spec.get("width")) is not int
            or type(map_spec.get("height")) is not int
            or map_spec.get("width") != BASE_SIZE or map_spec.get("height") != BASE_SIZE
            or map_spec.get("baseTerrain") != "grass-1"):
        raise ValueError("unsupported source: expected the current square 32 grass-1 map")
    if (map_spec.get("tiles") != [] or map_spec.get("blocked") != []
            or "capabilityProfile" in map_spec or map_spec.get("capability")):
        raise ValueError("unsupported source: source map tiles and blocked cells must be empty")
    if scenario.get("triggers") != []:
        raise ValueError("unsupported source: authored triggers must be empty")
    if scenario.get("authoredTriggers", []) != [] or scenario.get("alternativeRoutes", []) != []:
        raise ValueError("unsupported source: authored triggers and alternative routes must be empty")
    victory = scenario.get("victory")
    if not isinstance(victory, dict) or victory.get("routes") != []:
        raise ValueError("unsupported source: alternative routes must be empty")
    if not isinstance(victory.get("progressKey"), str) or not victory["progressKey"]:
        raise ValueError("unsupported source: expected the disposable fixture progress key")

    units = scenario.get("units")
    if (not isinstance(units, list) or any(not isinstance(unit, dict) for unit in units)
            or {unit.get("id") for unit in units} != {"guard", "enemy-guard"}
            or len(units) != 2):
        raise ValueError("unsupported source: expected exactly the guard and enemy-guard units")
    if any(unit.get("type") != "militia" for unit in units):
        raise ValueError("unsupported source: technical diagnostic unit types changed")
    objectives = scenario.get("objectives")
    if (not isinstance(objectives, list) or any(not isinstance(row, dict) for row in objectives)
            or [row.get("id") for row in objectives] != ["prepare", "defeat-guard"]
            or len(objectives) != 2):
        raise ValueError("unsupported source: expected prepare and defeat-guard objectives")

    _scale_pair(map_spec.get("start"), "map.start", 400)
    for unit in units:
        _scale_pair(unit.get("position"), f"unit.{unit['id']}.position", 400)
    for objective in objectives:
        _scale_pair(objective.get("location"), f"objective.{objective['id']}.location", 400)
    return scenario


def _marker_cells(size):
    markers = []
    all_cells = set()
    for marker_id, x400, y400, terrain in MARKERS_400:
        centre = (_scale_marker(x400, size), _scale_marker(y400, size))
        cells = [(x, y) for y in range(centre[1] - 1, centre[1] + 2)
                 for x in range(centre[0] - 1, centre[0] + 2)]
        if any(x < 0 or y < 0 or x >= size or y >= size for x, y in cells):
            raise ValueError(f"marker {marker_id} exceeds the diagnostic map bounds")
        if all_cells.intersection(cells):
            raise ValueError(f"diagnostic marker patches overlap at {marker_id}")
        all_cells.update(cells)
        markers.append({"id": marker_id, "centre": list(centre), "terrain": terrain,
                        "cells": [list(cell) for cell in cells]})
    if len(all_cells) != 36:
        raise ValueError("diagnostic must contain exactly 36 unique marker cells")
    return markers


def _transport_rectangle(size):
    x0, y0, x1, y1 = TRANSPORT_RECTANGLE_400
    left, top, right, bottom = (_scale_marker(value, size) for value in (x0, y0, x1, y1))
    width = right - left
    if width <= 7 or bottom <= top:
        raise ValueError("transport-observation rectangle collapsed after scaling")
    beach = [left, right - 1]
    shallow = list(range(left + 1, left + 4)) + list(range(right - 4, right - 1))
    deep = list(range(left + 4, right - 4))
    return {"xStart": left, "xEndExclusive": right, "yStart": top, "yEndExclusive": bottom,
            "beachColumns": beach, "shallowColumns": shallow, "deepColumns": deep,
            "cellCount": width * (bottom - top)}


def _overlay_transport_rectangle(map_spec, rectangle):
    for y in range(rectangle["yStart"], rectangle["yEndExclusive"]):
        for x in range(rectangle["xStart"], rectangle["xEndExclusive"]):
            edge_distance = min(x - rectangle["xStart"], rectangle["xEndExclusive"] - 1 - x)
            terrain = "beach" if edge_distance == 0 else (
                "water-shallow" if edge_distance <= 3 else "water-deep")
            map_spec["tiles"].append({"position": {"x": x, "y": y},
                                      "terrain": terrain, "elevation": 0})


def _transport_expected_counts(size, rectangle):
    area = rectangle["cellCount"]
    rows = rectangle["yEndExclusive"] - rectangle["yStart"]
    beach = len(rectangle["beachColumns"]) * rows
    shallow = len(rectangle["shallowColumns"]) * rows
    deep = len(rectangle["deepColumns"]) * rows + 9  # existing west marker
    return {"grass-1": size * size - area - 36, "water-deep": deep,
            "water-shallow": shallow, "beach": beach, "road": 9,
            "dirt-1": 9, "snow": 9}


def build_diagnostic_ir(source, size=DEFAULT_SIZE, variant="scale"):
    """Deep-clone and transform the fixed 32-tile fixture without mutating input."""
    if isinstance(size, bool) or not isinstance(size, int) or size not in (300, 400):
        raise ValueError("diagnostic size must be the integer 300 or 400")
    if variant not in ("scale", "transport-observation"):
        raise ValueError("diagnostic variant must be scale or transport-observation")
    validate_diagnostic_source(source)
    clone = copy.deepcopy(source)
    scenario = clone["scenarios"][0]["scenario"]
    map_spec = scenario["map"]
    original = {
        "mapStart": copy.deepcopy(map_spec["start"]),
        "units": {unit["id"]: copy.deepcopy(unit["position"]) for unit in scenario["units"]},
        "objectives": {objective["id"]: copy.deepcopy(objective["location"])
                       for objective in scenario["objectives"]},
    }
    map_spec["start"] = _scale_pair(map_spec["start"], "map.start", size)
    for unit in scenario["units"]:
        unit["position"] = _scale_pair(unit["position"], f"unit.{unit['id']}.position", size)
    for objective in scenario["objectives"]:
        objective["location"] = _scale_pair(objective["location"],
                                             f"objective.{objective['id']}.location", size)
    map_spec["width"] = size
    map_spec["height"] = size

    markers = _marker_cells(size)
    map_spec["tiles"] = [
        {"position": {"x": x, "y": y}, "terrain": marker["terrain"], "elevation": 0}
        for marker in markers for x, y in marker["cells"]
    ]
    details = {"size": size, "originalCoordinates": original,
               "transformedCoordinates": {
                   "mapStart": copy.deepcopy(map_spec["start"]),
                   "units": {unit["id"]: copy.deepcopy(unit["position"]) for unit in scenario["units"]},
                   "objectives": {objective["id"]: copy.deepcopy(objective["location"])
                                  for objective in scenario["objectives"]}},
               "markers": markers, "progressKeyRemovedFromClone": True,
               "markerCellCount": 36}
    if variant == "transport-observation":
        factions = scenario.get("factions")
        if (not isinstance(factions, list) or {row.get("id") for row in factions if isinstance(row, dict)}
                != {"player", "enemy"} or len(factions) != 2):
            raise ValueError("transport-observation source drift: expected player and enemy factions")
        faction_by_id = {row["id"]: row for row in factions}
        if (faction_by_id["player"].get("player") != 1 or faction_by_id["player"].get("role") != "human"
                or faction_by_id["enemy"].get("player") != 2 or faction_by_id["enemy"].get("role") != "enemy"):
            raise ValueError("transport-observation source drift: expected human player 1 and enemy player 2")
        original_units = {row["id"]: row for row in scenario["units"]}
        if (original_units["guard"].get("faction") != "player" or original_units["guard"].get("essential") is not True
                or original_units["enemy-guard"].get("faction") != "enemy"
                or original_units["enemy-guard"].get("essential") is not False):
            raise ValueError("transport-observation source drift: expected only the player guard to be essential")
        for faction in factions:
            strategy = faction.get("strategy")
            if (not isinstance(strategy, dict)
                    or strategy.get("limits") != "Dos unidades como máximo"):
                raise ValueError("transport-observation source drift: expected the two-unit faction limits")
        faction_by_id["player"]["strategy"]["limits"] = (
            "Tres unidades del jugador, incluidas dos unidades de observación no esenciales.")
        defeat = scenario.get("defeat")
        if (not isinstance(defeat, dict) or defeat.get("timeoutSeconds") != 600
                or defeat.get("essentialUnits") != ["guard"]
                or defeat.get("arbitration") != "defeat-first"):
            raise ValueError("transport-observation source drift: expected defeat-first, guard-only, 600-second timeout")
        rectangle = _transport_rectangle(size)
        for unit in TRANSPORT_UNITS_400:
            position = {"x": _scale_marker(unit["x"], size), "y": _scale_marker(unit["y"], size)}
            scenario["units"].append({"id": unit["id"], "faction": unit["faction"],
                                      "type": unit["type"], "position": position, "essential": False})
        details["transformedCoordinates"]["units"].update(
            {unit["id"]: copy.deepcopy(scenario["units"][-2 + index]["position"])
             for index, unit in enumerate(TRANSPORT_UNITS_400)})
        # Bind new unit positions and expected ownership/type to exact IDs.
        player_by_faction = {row["id"]: row.get("player") for row in factions}
        details["nativeUnits"] = [
            {"id": unit["id"], "type": unit["type"], "faction": unit["faction"],
             "player": player_by_faction[unit["faction"]],
             "position": copy.deepcopy(unit["position"]), "essential": unit.get("essential", False)}
            for unit in scenario["units"]]
        details["originalEssentialUnits"] = [row for row in details["nativeUnits"] if row["essential"]]
        scenario["defeat"]["timeoutSeconds"] = 1800
        _overlay_transport_rectangle(map_spec, rectangle)
        details.update({"variant": variant, "transportRectangle": rectangle,
                        "expectedTerrainCounts": _transport_expected_counts(size, rectangle),
                        "timeoutSeconds": 1800, "sourceTimeoutSeconds": 600})
    # This clone is deliberately disposable and must not write the fixture route.
    del scenario["victory"]["progressKey"]
    if variant == "scale":
        details["transformedCoordinates"] = {
            "mapStart": copy.deepcopy(map_spec["start"]),
            "units": {unit["id"]: copy.deepcopy(unit["position"]) for unit in scenario["units"]},
            "objectives": {objective["id"]: copy.deepcopy(objective["location"])
                           for objective in scenario["objectives"]},
        }
    return clone, details


def _run(argv, cwd=ROOT):
    proc = subprocess.run(argv, cwd=cwd, env=os.environ.copy(), capture_output=True,
                          text=True, check=False)
    record = {"argv": [str(arg) for arg in argv], "cwd": str(cwd),
              "exitCode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    if proc.returncode:
        diagnostics = []
        if proc.stdout.strip():
            diagnostics.append(f"stdout:\n{proc.stdout.rstrip()}")
        if proc.stderr.strip():
            diagnostics.append(f"stderr:\n{proc.stderr.rstrip()}")
        detail = "\n".join(diagnostics) or "no diagnostic output"
        raise RuntimeError(f"command failed ({proc.returncode}): {argv!r}\n{detail}")
    return record


def _verify_native_defeat_binding(triggers, guard_reference_id, destroy_object_condition_id,
                                  timer_condition_id, timeout):
    guard_triggers = [trigger for trigger in triggers if trigger.name == "cdf-defeat-guard"]
    timeout_triggers = [trigger for trigger in triggers if trigger.name == f"cdf-defeat-{timeout}"]
    if len(guard_triggers) != 1 or len(timeout_triggers) != 1:
        raise RuntimeError("decoded native defeat triggers do not match the guard and variant timeout")
    guard_destroy_conditions = [condition for condition in guard_triggers[0].conditions
                                if condition.condition_type == destroy_object_condition_id]
    other_defeat_destroy_conditions = [
        condition
        for trigger in triggers
        if trigger.name.startswith("cdf-defeat-") and trigger.name != guard_triggers[0].name
        for condition in trigger.conditions
        if condition.condition_type == destroy_object_condition_id
    ]
    if (len(guard_destroy_conditions) != 1 or other_defeat_destroy_conditions
            or guard_destroy_conditions[0].unit_object != guard_reference_id):
        raise RuntimeError("decoded native destroy-defeat condition is not bound to the original guard")
    if not any(condition.condition_type == timer_condition_id and condition.timer == timeout
               for condition in timeout_triggers[0].conditions):
        raise RuntimeError("decoded native timeout defeat condition differs from the transport variant")
    return {"trigger": guard_triggers[0].name, "conditionType": int(destroy_object_condition_id),
            "unitReferenceId": int(guard_destroy_conditions[0].unit_object),
            "guardReferenceId": int(guard_reference_id), "linkedToOriginalGuard": True,
            "timeoutTrigger": timeout_triggers[0].name, "timeoutSeconds": timeout}


def _read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"cannot read required JSON {path}: {error}") from error


def inspect_native_diagnostic(path, transform):
    """Decode the native bytes and record the artificial controls, not game QA."""
    import contextlib
    import io
    from collections import Counter
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
    from AoE2ScenarioParser.datasets.conditions import ConditionId
    from AoE2ScenarioParser.datasets.units import UnitInfo
    from AoE2ScenarioParser.datasets.terrains import TerrainId

    terrain_ids = {"grass-1": int(TerrainId.GRASS_1), "road": int(TerrainId.ROAD),
                   "dirt-1": int(TerrainId.DIRT_1), "snow": int(TerrainId.SNOW),
                   "water-deep": int(TerrainId.WATER_DEEP),
                   "water-shallow": int(TerrainId.WATER_SHALLOW),
                   "beach": int(TerrainId.BEACH)}
    with contextlib.redirect_stdout(io.StringIO()):
        scenario = AoE2DEScenario.from_file(str(path))
    size = transform["size"]
    tiles = scenario.map_manager.terrain
    counts = Counter(tile.terrain_id for tile in tiles)
    if transform.get("variant") == "transport-observation":
        expected = {terrain_ids[name]: count for name, count in transform["expectedTerrainCounts"].items()}
    else:
        expected = {terrain_ids["grass-1"]: size * size - 36}
        expected.update({terrain_ids[marker["terrain"]]: 9 for marker in transform["markers"]})
    if scenario.map_manager.map_size != size or len(tiles) != size * size or dict(counts) != expected:
        raise RuntimeError("decoded native map dimensions/terrain counts differ from the diagnostic")
    if any(tile.elevation != 0 for tile in tiles):
        raise RuntimeError("decoded native diagnostic has unexpected nonzero elevation")
    cells = []
    for marker in transform["markers"]:
        terrain_id = terrain_ids[marker["terrain"]]
        for x, y in marker["cells"]:
            if scenario.map_manager.get_tile(x, y).terrain_id != terrain_id:
                raise RuntimeError(f"decoded native marker differs at {x},{y}")
            cells.append({"x": x, "y": y, "terrain": marker["terrain"], "terrainId": terrain_id})
    rectangle_cells_checked = 0
    rectangle = transform.get("transportRectangle")
    if rectangle:
        for y in range(rectangle["yStart"], rectangle["yEndExclusive"]):
            for x in range(rectangle["xStart"], rectangle["xEndExclusive"]):
                edge_distance = min(x - rectangle["xStart"], rectangle["xEndExclusive"] - 1 - x)
                terrain = "beach" if edge_distance == 0 else (
                    "water-shallow" if edge_distance <= 3 else "water-deep")
                if scenario.map_manager.get_tile(x, y).terrain_id != terrain_ids[terrain]:
                    raise RuntimeError(f"decoded transport rectangle differs at {x},{y}: expected {terrain}")
                rectangle_cells_checked += 1
    unit_observations = []
    for player_index, player_units in enumerate(scenario.unit_manager.units):
        for unit in player_units:
            unit_type = getattr(unit, "unit_const", None)
            unit_type_id = getattr(unit_type, "ID", unit_type)
            owner = getattr(unit, "player_number", None)
            if owner is None:
                owner = player_index
            unit_observations.append({"typeId": int(unit_type_id), "player": int(owner),
                                      "x": unit.x, "y": unit.y,
                                      "referenceId": getattr(unit, "reference_id", None)})
    if transform.get("nativeUnits"):
        expected_units = []
        for expected_unit in transform["nativeUnits"]:
            unit_enum = getattr(UnitInfo, expected_unit["type"].upper().replace("-", "_"), None)
            if unit_enum is None:
                raise RuntimeError(f"pinned parser lacks expected unit enum {expected_unit['type']}")
            expected_native_row = {"typeId": int(unit_enum.ID), "player": expected_unit["player"],
                                   "x": expected_unit["position"]["x"] + 0.5,
                                   "y": expected_unit["position"]["y"] + 0.5}
            matches = [row for row in unit_observations
                       if all(row[field] == expected_native_row[field]
                              for field in ("typeId", "player", "x", "y"))]
            if len(matches) != 1 or matches[0]["referenceId"] is None:
                raise RuntimeError(f"decoded native unit does not uniquely match {expected_unit['id']}")
            expected_units.append({"id": expected_unit["id"], "type": expected_unit["type"],
                                   "typeId": int(unit_enum.ID), "player": expected_unit["player"],
                                   "x": expected_unit["position"]["x"] + 0.5,
                                   "y": expected_unit["position"]["y"] + 0.5,
                                   "essential": expected_unit["essential"],
                                   "referenceId": matches[0]["referenceId"]})
        observed_multiset = sorted((row["typeId"], row["player"], row["x"], row["y"])
                                   for row in unit_observations)
        expected_multiset = sorted((row["typeId"], row["player"], row["x"], row["y"])
                                   for row in expected_units)
        if observed_multiset != expected_multiset:
            raise RuntimeError("decoded native unit types/owners/positions differ from the diagnostic")
        if len(transform["originalEssentialUnits"]) != 1 or transform["originalEssentialUnits"][0]["id"] != "guard":
            raise RuntimeError("transport diagnostic lost the original guard essential-unit binding")
        guard_reference_id = next(row["referenceId"] for row in expected_units if row["id"] == "guard")
        defeat_binding = _verify_native_defeat_binding(
            scenario.trigger_manager.triggers, guard_reference_id, ConditionId.DESTROY_OBJECT,
            ConditionId.TIMER,
            transform["timeoutSeconds"])
        essential_binding = {"id": "guard", "player": next(row["player"] for row in expected_units
                                                                if row["id"] == "guard"),
                             "typeId": next(row["typeId"] for row in expected_units if row["id"] == "guard"),
                             "position": next({"x": row["x"], "y": row["y"]} for row in expected_units
                                              if row["id"] == "guard"),
                             "referenceId": guard_reference_id}
    else:
        positions = sorted((row["x"], row["y"]) for row in unit_observations)
        expected_positions = sorted((point["x"] + 0.5, point["y"] + 0.5)
                                    for point in transform["transformedCoordinates"]["units"].values())
        if positions != expected_positions:
            raise RuntimeError("decoded native unit positions differ from the diagnostic")
        expected_units = []
        essential_binding = None
        defeat_binding = None
    positions = sorted((row["x"], row["y"]) for row in unit_observations)
    reproduction = [sys.executable, "tools/map/large-map-diagnostic.script.py", "--size", str(size)]
    if transform.get("variant") == "transport-observation":
        reproduction.extend(["--variant", "transport-observation"])
    return {"scenarioSha256": _sha256(path.read_bytes()), "mapSize": size,
            "tileCount": len(tiles), "terrainIdByName": terrain_ids,
            "terrainCountsByName": {name: counts[value] for name, value in terrain_ids.items()},
            "allElevationsZero": True, "markerCellsChecked": len(cells), "markerCells": cells,
            "transportRectangleCellsChecked": rectangle_cells_checked,
            "unitObservations": unit_observations, "expectedUnits": expected_units,
            "originalEssentialUnitBinding": essential_binding,
            "nativeDefeatBinding": defeat_binding, "unitPositions": positions,
            "producerFunction": "tools/map/large-map-diagnostic.script.py::inspect_native_diagnostic",
            "producerFileSha256": _sha256(Path(__file__).read_bytes()),
            "reproductionCommand": reproduction,
            "scope": "native binary decode only; no game, camera, passability, history or performance verification"}


def run_diagnostic(size=DEFAULT_SIZE, variant="scale"):
    if isinstance(size, bool) or not isinstance(size, int) or size not in (300, 400):
        raise ValueError("diagnostic size must be the integer 300 or 400")
    if variant not in ("scale", "transport-observation"):
        raise ValueError("diagnostic variant must be scale or transport-observation")
    commands = []
    commands.append(_run(["bun", "run", "campaign:build", SOURCE_CAMPAIGN]))
    source_ir_path = ROOT / "build" / SOURCE_CAMPAIGN / "campaign-ir.json"
    source_report_path = ROOT / "build" / SOURCE_CAMPAIGN / "build-report.json"
    source_ir_bytes = source_ir_path.read_bytes()
    source = _read_json(source_ir_path)
    campaign_report = _read_json(source_report_path)
    if not isinstance(campaign_report.get("sourceSha256"), str) or not campaign_report["sourceSha256"]:
        raise RuntimeError("technical-pilot build report is missing its source hash")
    clone, transform = build_diagnostic_ir(source, size, variant)
    engine_catalog = _read_json(ROOT / "config" / "engine-catalog.json")
    available_terrains = set(engine_catalog.get("terrains", []))
    required_terrains = {row["terrain"] for row in transform["markers"]}
    if transform.get("variant") == "transport-observation":
        required_terrains.update(("beach", "water-shallow", "water-deep"))
    missing_terrains = sorted(required_terrains - available_terrains)
    if missing_terrains:
        raise RuntimeError(f"diagnostic terrain names absent from pinned engine catalogue: {missing_terrains}")
    available_units = set(engine_catalog.get("units", []))
    missing_units = sorted({row["type"] for row in transform.get("nativeUnits", [])} - available_units)
    if missing_units:
        raise RuntimeError(f"diagnostic unit names absent from pinned engine catalogue: {missing_units}")

    product_slug = "transport-map-diagnostic" if variant == "transport-observation" else "large-map-diagnostic"
    archive_stem = f"transport-map-diagnostic-{size}" if variant == "transport-observation" else f"large-map-diagnostic-{size}"
    scenario_stem = f"CDF_Transport{size}_Diagnostic" if variant == "transport-observation" else f"CDF_LargeMap{size}_Diagnostic"
    build_root = ROOT / "build" / product_slug / str(size)
    export_root = build_root / "export"
    kit_root = build_root / "kit"
    dist_root = ROOT / "dist"
    archive = dist_root / f"{archive_stem}.zip"
    zip_temp = dist_root / f".{archive_stem}.zip.tmp"
    receipt_path = build_root / "zip-receipt.json"
    receipt_temp = build_root / ".zip-receipt.json.tmp"
    build_root.mkdir(parents=True, exist_ok=True)
    # Invalidate the previous publication before replacing the kit/report it names.
    for stale in (receipt_path, receipt_temp, zip_temp, archive, build_root / "native-inspection.json"):
        stale.unlink(missing_ok=True)
    for generated_dir in (export_root, kit_root):
        if generated_dir.is_symlink():
            raise RuntimeError(f"refusing to replace generated output symlink: {generated_dir}")
        if generated_dir.exists():
            shutil.rmtree(generated_dir)
    export_root.mkdir(parents=True, exist_ok=True)
    kit_root.mkdir(parents=True, exist_ok=True)
    dist_root.mkdir(parents=True, exist_ok=True)
    diagnostic_ir_path = build_root / "campaign-ir.json"
    diagnostic_ir_bytes = (json.dumps(clone, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    diagnostic_ir_path.write_bytes(diagnostic_ir_bytes)

    export_command = [sys.executable, "tools/python/export_aoe2.py", "build",
                      str(diagnostic_ir_path), str(export_root)]
    commands.append(_run(export_command))
    adapter_report = _read_json(export_root / "export-report.json")
    if adapter_report.get("gameVerified") is not False:
        raise RuntimeError("native exporter report unexpectedly claims game verification")
    scenario_source = export_root / f"{SOURCE_SCENARIO}.aoe2scenario"
    if not scenario_source.is_file():
        raise RuntimeError(f"native exporter did not produce {scenario_source.name}")

    scenario_archive_path = Path("scenario") / f"{scenario_stem}.aoe2scenario"
    scenario_target = kit_root / scenario_archive_path
    scenario_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(scenario_source, scenario_target)
    scenario_sha = _sha256(scenario_target.read_bytes())
    matching_reports = [row for row in adapter_report.get("scenarioReports", [])
                        if row.get("id") == SOURCE_SCENARIO]
    if len(matching_reports) != 1 or matching_reports[0].get("sha256") != scenario_sha:
        raise RuntimeError("copied scenario bytes differ from the adapter's round-trip report")
    files = [{"archivePath": scenario_archive_path.as_posix(),
              "sourcePath": str(scenario_source.relative_to(ROOT)),
              "sha256": scenario_sha}]
    inspection = inspect_native_diagnostic(scenario_target, transform)
    (build_root / "native-inspection.json").write_text(json.dumps(inspection, indent=2) + "\n", encoding="utf-8")

    locales = []
    locale_sources = {
        "en": ROOT / "build" / SOURCE_CAMPAIGN / "mod/resources/en/strings/key-value/key-value-modded-strings-utf8.txt",
        "es": ROOT / "build" / SOURCE_CAMPAIGN / "mod/resources/es/strings/key-value/key-value-modded-strings-utf8.txt",
    }
    for locale, source_path in locale_sources.items():
        if not source_path.is_file():
            raise RuntimeError(f"compiled draft locale catalogue missing: {source_path}")
        relative = Path("locale-mod") / "resources" / locale / "strings" / "key-value" / source_path.name
        target = kit_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        source_bytes = source_path.read_bytes()
        target.write_bytes(source_bytes)
        copied_bytes = target.read_bytes()
        if copied_bytes != source_bytes:
            raise RuntimeError(f"draft locale catalogue was not copied byte-for-byte: {locale}")
        locales.append({"locale": locale, "archivePath": relative.as_posix(),
                        "sourcePath": str(source_path.relative_to(ROOT)),
                        "sha256": _sha256(source_bytes), "byteIdentical": True})

    readme = _kit_readme(size, transform)
    (kit_root / "README.txt").write_text(readme, encoding="utf-8")
    report = {
        "artifact": "private-artificial-transport-map-editor-diagnostic" if variant == "transport-observation"
                    else "private-artificial-large-map-editor-diagnostic",
        "sourceCampaign": SOURCE_CAMPAIGN,
        "sourceSha256": campaign_report.get("sourceSha256"),
        "sourceIrPath": str(source_ir_path.relative_to(ROOT)),
        "sourceIrSha256": _sha256(source_ir_bytes),
        "diagnosticIrSha256": _sha256(diagnostic_ir_bytes),
        "size": size,
        "variant": variant,
        "transformedCoordinates": transform,
        "markerLegend": ([
            "Grid data-north is a calibration label, not camera-orientation evidence.",
            "North marker is road; east is dirt-1; south is snow; west is water-deep.",
            "The water marker is an artificial terrain patch; it proves no crossing or transport behavior.",
            "All cells use elevation 0 over grass-1, with no walls or historical layer.",
        ] if variant == "scale" else [
            "Grid labels identify test coordinates only; camera orientation and passability remain pending game observations.",
            "The four 3x3 markers remain separate from the bounded artificial beach/shallow/deep rectangle.",
            "Terrain names and a native binary decode alone do not establish boarding, unloading, route access or gameplay.",
            "All terrain is flat at elevation 0; no bridge, cliff, current or historical coastline is asserted.",
        ]),
        "transportObservation": ({
            "rectangle": transform["transportRectangle"],
            "addedUnits": transform["nativeUnits"][2:],
            "timeoutSeconds": 1800,
            "inheritedObjectiveLimitations": [
                "The existing objectives remain prepare then defeat enemy-guard.",
                "They do not check boarding, unloading, land detours or boat loss.",
                "Avoid losing the essential guard or defeating the enemy before observations finish.",
            ],
            "terrainCountsByName": transform["expectedTerrainCounts"],
            "gameObservations": "all pending; no native export establishes gameplay support",
        } if variant == "transport-observation" else None),
        "localeCatalogues": locales,
        "scenario": files[0],
        "commands": list(commands),
        "diagnosticCommand": [sys.executable, "tools/map/large-map-diagnostic.script.py",
                              "--size", str(size), "--variant", variant],
        "exportCommand": commands[1],
        "externalZipReceipt": str((build_root / "zip-receipt.json").relative_to(ROOT)),
        "adapterReport": adapter_report,
        "nativeInspection": inspection,
        "archiveReceiptPolicy": "Packaging is complete only when the external receipt exists and its report SHA-256 matches this report. A missing receipt means packaging is incomplete.",
        "gameVerified": False,
        "historicalMap": False,
        "nativeTerrainFromDsm": False,
        "cameraCalibration": "pending",
        "pending": (["manual boarding and passenger-in-boat observation", "unloading at opposite shore",
                     "north and south land-detour walkability", "boat deletion with passenger aboard",
                     "save/load before boarding, aboard and after unloading", "editor loading and terrain rendering",
                     "gameVerified remains false; no victory/route/performance claim"]
                    if variant == "transport-observation" else
                    ["editor loading and orientation observation", "ordinary movement and save/load",
                     "campaign launch and native campaign UI are excluded", "not a performance proof at campaign caps"]),
        "timeoutSeconds": transform.get("timeoutSeconds", 600),
        "inheritedCombatUnitCount": 2,
    }
    report_path = kit_root / "diagnostic-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    try:
        commands.append(_run([sys.executable, "tools/python/export_aoe2.py", "zip", str(kit_root), str(zip_temp)]))
    except Exception:
        zip_temp.unlink(missing_ok=True)
        raise
    zip_temp.replace(archive)
    archive_sha = _sha256(archive.read_bytes())
    receipt = {"archive": str(archive.relative_to(ROOT)), "sha256": archive_sha,
               "reportPath": str(report_path.relative_to(ROOT)),
               "reportSha256": _sha256(report_path.read_bytes()),
               "scenarioSha256": scenario_sha,
               "campaignBuildCommand": commands[0], "exportCommand": commands[1],
               "zipCommand": commands[-1]}
    receipt_temp.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    receipt_temp.replace(receipt_path)
    return {"report": report, "receipt": receipt}


def _kit_readme(size, transform):
    markers = "\n".join(
        f"- {m['id']}: {m['terrain']} at grid centre {m['centre'][0]},{m['centre'][1]}"
        for m in transform["markers"]
    )
    transport_text = ""
    terrain_context = (
        "They use grid labels for coordinate orientation only; they do not calibrate the isometric camera. "
        "The west water-deep marker is an artificial 3x3 patch, not a river or crossing. The rest of the map is grass-1 "
        "at elevation 0; there are no walls, bridges, cliffs or historical layers.\n\n"
        if transform.get("variant") != "transport-observation" else
        "They use grid labels for coordinate orientation only; they do not calibrate the isometric camera. "
        "The separate artificial beach/shallow/deep rectangle is specified below; it is not a dated coastline or certified route. "
        "All terrain is elevation 0, with no walls, bridges, cliffs or historical layers.\n\n"
    )
    fixture_limits = (
        "The inherited fixture has two combat units and a 600-second timeout; victory and performance are not guaranteed. "
        if transform.get("variant") != "transport-observation" else
        "The inherited fixture has two combat units and the variant has a 1800-second timeout; victory and performance are not guaranteed. "
    )
    movement_instruction = (
        "move the existing guard along the ordinary diagonal toward the enemy"
        if transform.get("variant") != "transport-observation" else
        "avoid combat and observe the north/south land detours plus the transport states listed below"
    )
    screenshot_instruction = (
        "take a screenshot showing the four terrain controls"
        if transform.get("variant") != "transport-observation" else
        "take screenshots showing the four terrain controls and the complete transport rectangle"
    )
    if transform.get("variant") == "transport-observation":
        rectangle = transform["transportRectangle"]
        transport_text = (
            f"\n\nTransport observation variant: a flat artificial rectangle x=[{rectangle['xStart']},"
            f"{rectangle['xEndExclusive']}) y=[{rectangle['yStart']},{rectangle['yEndExclusive']}) with one beach edge, "
            "three shallow-water columns on each side, and deep water inside. The player has three units (the original guard, "
            "a nonessential transport ship and a nonessential villager passenger); the enemy has one original militia. "
            "Timeout is 1800 seconds. The inherited objectives still only prepare and defeat the enemy guard: they do not "
            "confirm boarding, unloading, detours or passenger outcome. Do not defeat the enemy or lose the essential guard "
            "before observations are complete. This is an artificial terrain fixture, not a coast or a route claim.\n\n"
            "Record the exact game build, Steam/store, operating system and UI language. Observe editor load; ordinary boarding; "
            "passenger actually inside the boat; unloading on the opposite side; north and south land detours; deletion of the "
            "boat with the passenger aboard; and save/load before boarding, aboard, and after unloading. Record what happens "
            "when the boat is deleted without assuming passenger death or survival. Leave every outcome pending if the editor "
            "cannot expose it. Use a separate named copy for edits and saves; record its path and hash and confirm the included "
            "original remains unchanged.\n"
        )
    return (
        "Private AoE2:DE editor diagnostic — not a campaign release\n\n"
        f"Map: {size} x {size}. The only terrain markers are four disjoint 3x3 patches:\n{markers}\n\n"
        f"{terrain_context}"
        "Editor test: treat the included scenario as a read-only original. Open it to inspect, then immediately use Save As "
        "to create a separate copy with a different filename before any edit or save. Record the original SHA-256 from "
        "diagnostic-report.json and the copy's SHA-256; use a different filename. Identical bytes may have an identical hash. Never overwrite the "
        "included artifact. Enable the included locale-mod folder only if checking existing draft labels. Observe load success, "
        f"{screenshot_instruction}, "
        f"{movement_instruction}, "
        "then save and reopen the named copy. Confirm the included original still matches its recorded hash. Record editor mode "
        f"separately from launching any campaign. {fixture_limits}It does not provide a performance benchmark. "
        "This kit contains no campaign container and does not claim "
        "game verification, balance, historical geography, transport, camera calibration or production readiness."
        f"{transport_text}\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, choices=(300, 400), default=DEFAULT_SIZE)
    parser.add_argument("--variant", choices=("scale", "transport-observation"), default="scale")
    args = parser.parse_args()
    result = run_diagnostic(args.size, args.variant)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
