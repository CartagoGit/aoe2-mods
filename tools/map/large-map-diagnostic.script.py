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


def build_diagnostic_ir(source, size=DEFAULT_SIZE):
    """Deep-clone and transform the fixed 32-tile fixture without mutating input."""
    if isinstance(size, bool) or not isinstance(size, int) or size not in (300, 400):
        raise ValueError("diagnostic size must be the integer 300 or 400")
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
    # This clone is deliberately disposable and must not write the fixture route.
    del scenario["victory"]["progressKey"]
    transformed = {
        "mapStart": copy.deepcopy(map_spec["start"]),
        "units": {unit["id"]: copy.deepcopy(unit["position"]) for unit in scenario["units"]},
        "objectives": {objective["id"]: copy.deepcopy(objective["location"])
                       for objective in scenario["objectives"]},
    }
    return clone, {"size": size, "originalCoordinates": original,
                   "transformedCoordinates": transformed, "markers": markers,
                   "progressKeyRemovedFromClone": True, "markerCellCount": 36}


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


def _read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"cannot read required JSON {path}: {error}") from error


def run_diagnostic(size=DEFAULT_SIZE):
    if isinstance(size, bool) or not isinstance(size, int) or size not in (300, 400):
        raise ValueError("diagnostic size must be the integer 300 or 400")
    commands = []
    commands.append(_run(["bun", "run", "campaign:build", SOURCE_CAMPAIGN]))
    source_ir_path = ROOT / "build" / SOURCE_CAMPAIGN / "campaign-ir.json"
    source_report_path = ROOT / "build" / SOURCE_CAMPAIGN / "build-report.json"
    source_ir_bytes = source_ir_path.read_bytes()
    source = _read_json(source_ir_path)
    campaign_report = _read_json(source_report_path)
    if not isinstance(campaign_report.get("sourceSha256"), str) or not campaign_report["sourceSha256"]:
        raise RuntimeError("technical-pilot build report is missing its source hash")
    clone, transform = build_diagnostic_ir(source, size)
    engine_catalog = _read_json(ROOT / "config" / "engine-catalog.json")
    available_terrains = set(engine_catalog.get("terrains", []))
    missing_terrains = sorted({row["terrain"] for row in transform["markers"]} - available_terrains)
    if missing_terrains:
        raise RuntimeError(f"diagnostic terrain names absent from pinned engine catalogue: {missing_terrains}")

    build_root = ROOT / "build" / "large-map-diagnostic" / str(size)
    export_root = build_root / "export"
    kit_root = build_root / "kit"
    dist_root = ROOT / "dist"
    build_root.mkdir(parents=True, exist_ok=True)
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

    scenario_archive_path = Path("scenario") / f"CDF_LargeMap{size}_Diagnostic.aoe2scenario"
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
        "artifact": "private-artificial-large-map-editor-diagnostic",
        "sourceCampaign": SOURCE_CAMPAIGN,
        "sourceSha256": campaign_report.get("sourceSha256"),
        "sourceIrPath": str(source_ir_path.relative_to(ROOT)),
        "sourceIrSha256": _sha256(source_ir_bytes),
        "diagnosticIrSha256": _sha256(diagnostic_ir_bytes),
        "size": size,
        "transformedCoordinates": transform,
        "markerLegend": [
            "Grid data-north is a calibration label, not camera-orientation evidence.",
            "North marker is road; east is dirt-1; south is snow; west is water-deep.",
            "The water marker is artificial and away from the diagonal start-to-target corridor; it proves no crossing or transport.",
            "All cells use elevation 0 over grass-1, with no walls or historical layer.",
        ],
        "localeCatalogues": locales,
        "scenario": files[0],
        "commands": commands,
        "exportCommand": commands[1],
        "externalZipReceipt": str((build_root / "zip-receipt.json").relative_to(ROOT)),
        "adapterReport": adapter_report,
        "gameVerified": False,
        "historicalMap": False,
        "nativeTerrainFromDsm": False,
        "cameraCalibration": "pending",
        "pending": ["editor loading and orientation observation", "ordinary movement and save/load", "campaign launch and native campaign UI are excluded", "not a performance proof at campaign caps"],
    }
    (kit_root / "diagnostic-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    archive = dist_root / f"large-map-diagnostic-{size}.zip"
    zip_temp = dist_root / f".large-map-diagnostic-{size}.zip.tmp"
    try:
        commands.append(_run([sys.executable, "tools/python/export_aoe2.py", "zip", str(kit_root), str(zip_temp)]))
    except Exception:
        zip_temp.unlink(missing_ok=True)
        raise
    zip_temp.replace(archive)
    archive_sha = _sha256(archive.read_bytes())
    receipt = {"archive": str(archive.relative_to(ROOT)), "sha256": archive_sha,
               "reportPath": str((kit_root / "diagnostic-report.json").relative_to(ROOT)),
               "campaignBuildCommand": commands[0], "exportCommand": commands[1],
               "zipCommand": commands[-1]}
    (build_root / "zip-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return {"report": report, "receipt": receipt}


def _kit_readme(size, transform):
    markers = "\n".join(
        f"- {m['id']}: {m['terrain']} at grid centre {m['centre'][0]},{m['centre'][1]}"
        for m in transform["markers"]
    )
    return (
        "Private AoE2:DE editor diagnostic — not a campaign release\n\n"
        f"Map: {size} x {size}. The only terrain markers are four disjoint 3x3 patches:\n{markers}\n\n"
        "They use grid labels for coordinate orientation only; they do not calibrate the isometric camera. "
        "The west water-deep marker is a modern artificial test patch, not a river, crossing or proof of boat support. "
        "The rest of the map is grass-1 at elevation 0; there are no walls, bridges, cliffs or historical layers.\n\n"
        "Editor test: treat the included scenario as a read-only original. Open it to inspect, then immediately use Save As "
        "to create a separate copy with a different filename before any edit or save. Record the original SHA-256 from "
        "diagnostic-report.json and the copy's SHA-256; use a different filename. Identical bytes may have an identical hash. Never overwrite the "
        "included artifact. Enable the included locale-mod folder only if checking existing draft labels. Observe load success, "
        "take a screenshot showing the four terrain controls, move the existing guard along the ordinary diagonal toward the enemy, "
        "then save and reopen the named copy. Confirm the included original still matches its recorded hash. Record editor mode "
        "separately from launching any campaign. The inherited fixture has only two combat units and a 600-second timeout; it "
        "does not guarantee victory or provide a performance benchmark. This kit contains no campaign container and does not claim "
        "game verification, balance, historical geography, transport, camera calibration or production readiness.\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, choices=(300, 400), default=DEFAULT_SIZE)
    args = parser.parse_args()
    result = run_diagnostic(args.size)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
