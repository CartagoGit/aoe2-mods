"""Build an explicitly bounded private episode preview, never promote a campaign.

This input is an authored dossier plus a reviewed physical binding. It is not
public scenario IR and cannot enable or silently lower composed v2/v3 exports.
"""

import argparse
import contextlib
import hashlib
import io
import json
import math
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
native_signature = runpy.run_path(str(HERE / "native_signature.helper.py"))[
    "native_signature"
]
RECEIVING_WAYFINDING = runpy.run_path(
    str(HERE / "private_wayfinding.renderer.py")
)["render_receiving_wayfinding"]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _root_path(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("input path must stay in the source workspace")
    return path


def load_delivery_source(root, binding_path):
    binding = json.loads(binding_path.read_text(encoding="utf8"))
    source = _root_path(root, binding["sourcePath"])
    if sha256(source) != binding["sourceSha256"]:
        raise ValueError("delivery source hash mismatch; re-review the changed source")
    campaign = json.loads(source.read_text(encoding="utf8"))
    dossier = campaign["episodes"][binding["sourceDossierIndex"]]
    if (
        campaign["campaignId"] != binding["campaignId"]
        or dossier["id"] != binding["episodeId"]
    ):
        raise ValueError("delivery source identity mismatch")
    for level, profile in binding["difficulty"].items():
        if (
            dossier["difficulty"][level]["startingResources"]
            != profile["startingResources"]
        ):
            raise ValueError(
                "native starting resources must match the authored profile"
            )
    adapter = runpy.run_path(str(HERE / "native_delivery.adapter.py"))
    adapter["validate_delivery_contract"](dossier, binding)
    return campaign, dossier, binding


def coast_intersections(root, binding):
    """Use every clipped source vertex; no fabricated Roman harbor or DEM."""
    geo = runpy.run_path(str(root / "tools/design/geography.py"))
    frame_module = runpy.run_path(str(root / "tools/map/geographic_frame.helper.py"))
    frame = frame_module["make_frame"](binding["map"]["bbox"], binding["map"]["size"])
    source = _root_path(root, binding["map"]["coastlineSource"])
    if sha256(source) != binding["map"]["coastlineSourceSha256"]:
        raise ValueError("shoreline source hash mismatch")
    bounds = frame.bounds_at(-0.5, binding["map"]["size"] - 0.5)
    segments = []
    for feature in json.loads(source.read_text())["features"]:
        for line in geo["geometry_lines"](feature["geometry"]):
            for a, b in zip(line, line[1:]):
                clipped = geo["clip_segment"](a, b, bounds, precision=None)
                if clipped:
                    segments.append([frame.tile_at(p) for p in clipped])
    result = []
    for y in range(binding["map"]["size"]):
        xs = []
        for a, b in segments:
            if min(a[1], b[1]) <= y <= max(a[1], b[1]) and a[1] != b[1]:
                xs.append(a[0] + (y - a[1]) * (b[0] - a[0]) / (b[1] - a[1]))
        if len(xs) != 1:
            raise ValueError(
                "bounded west-sea preview needs one unambiguous shoreline intersection per row"
            )
        result.append(xs[0])
    return result


def _segment_distance(point, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    denominator = dx * dx + dy * dy
    t = (
        max(0, min(1, ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / denominator))
        if denominator
        else 0
    )
    return math.dist(point, [a[0] + t * dx, a[1] + t * dy])


def physical_base(binding, dossier, level):
    """Construct a NEW explicit physical v1 base; do not strip a capability IR."""
    size = binding["map"]["size"]
    stocks = dossier["difficulty"][level]["startingResources"]
    factions = [
        {
            "id": name,
            "player": player,
            "civilization": "byzantines",
            "role": role,
            "economy": {
                "model": "finite-reserve",
                "initial": stocks if player == 1 else dict.fromkeys(stocks, 0),
            },
        }
        for name, player, role in [("player", 1, "human"), ("local", 2, "ally")]
    ]
    native_units = []
    name_mapping = {}
    for i, entity in enumerate(binding["entities"]):
        key = f"original-{i}"
        name_mapping[entity["id"]] = key
        x, y = map(math.floor, entity["position"])
        native_units.append(
            {
                "id": key,
                "faction": "player" if entity["player"] == 1 else "local",
                "type": entity["unitType"],
                "position": {"x": x, "y": y},
                "essential": False,
            }
        )
    start = binding["collection"]["entities"][0]
    view = next(u["position"] for u in native_units if u["id"] == name_mapping[start])
    return {
        "schemaVersion": 1,
        "scenario": {
            "id": binding["episodeId"],
            "map": {
                "width": size,
                "height": size,
                "baseTerrain": "grass-1",
                "tiles": [],
                "blocked": [],
                "start": view,
            },
            "factions": factions,
            "units": native_units,
            "technologies": [],
        },
    }, name_mapping


def paint_world(scenario, binding, coast, level, locale):
    from AoE2ScenarioParser.datasets.other import OtherInfo
    from AoE2ScenarioParser.datasets.terrains import TerrainId

    size = binding["map"]["size"]
    corridors = binding["map"]["corridors"]
    for y in range(size):
        for x in range(size):
            tile = scenario.map_manager.get_tile(x, y)
            terrain = (
                TerrainId.WATER_DEEP
                if x < coast[y] - 1
                else TerrainId.BEACH
                if x < coast[y] + 1
                else TerrainId.GRASS_1
            )
            if x > coast[y] + 2:
                for corridor in corridors:
                    if any(
                        _segment_distance((x, y), a, b) <= corridor["widthTiles"] / 2
                        for a, b in zip(corridor["points"], corridor["points"][1:])
                    ):
                        terrain = TerrainId.DIRT_1
                for z in binding["zones"]:
                    distance = math.dist((x, y), z["centre"])
                    if z["radius"] - 0.5 <= distance <= z["radius"] + 0.5:
                        terrain = TerrainId.ROAD
            tile.terrain_id, tile.elevation = int(terrain), 0
    for zone in binding["zones"]:
        x, y = zone["centre"]
        if x <= coast[min(size - 1, max(0, round(y)))] + 2:
            raise ValueError("receiving court would be in coastal water")
    provenance = RECEIVING_WAYFINDING(scenario, binding["zones"], locale)
    # Difficulty changes disclosed assistance, not movement, damage or deadlines.
    if level == "easy":
        for corridor in corridors:
            for a, b in zip(corridor["points"], corridor["points"][1:]):
                steps = max(1, math.ceil(math.dist(a, b) / 8))
                for i in range(steps + 1):
                    t = i / steps
                    scenario.unit_manager.add_unit(
                        player=1,
                        unit_const=OtherInfo.MAP_REVEALER.ID,
                        x=a[0] + t * (b[0] - a[0]),
                        y=a[1] + t * (b[1] - a[1]),
                    )
    for corridor in corridors:
        for point in corridor["points"]:
            if (
                point[0]
                <= coast[min(size - 1, max(0, round(point[1])))]
                + 2
                + corridor["widthTiles"] / 2
            ):
                raise ValueError("corridor footprint approaches coastal water")
    return provenance


def build_variant(root, dossier, binding, coast, output, locale, level, version):
    from AoE2ScenarioParser.datasets.buildings import BuildingInfo
    from AoE2ScenarioParser.datasets.techs import TechInfo
    from AoE2ScenarioParser.datasets.units import UnitInfo
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

    factory = runpy.run_path(str(HERE / "native_scenario.factory.py"))
    controller = runpy.run_path(str(HERE / "native_delivery.adapter.py"))
    base, mapping = physical_base(binding, dossier, level)
    scenario, native_ids, _ = factory["create_native_scenario_base"](base, version)
    originals = {key: native_ids[native_name] for key, native_name in mapping.items()}
    for player in (1, 2):
        p = scenario.player_manager.players[player]
        p.disabled_buildings = sorted({u.ID for u in BuildingInfo if u.ID >= 0})
        p.disabled_units = sorted({u.ID for u in UnitInfo if u.ID >= 0})
        p.disabled_techs = sorted({u.ID for u in TechInfo if u.ID >= 0})
    receiving_wayfinding = paint_world(scenario, binding, coast, level, locale)
    result = controller["compile_delivery_controller"](
        scenario, originals, dossier, binding, locale
    )
    goals = [
        o["text"][locale]
        for o in dossier["objectivePlan"] + dossier["secondaryObjectives"]
    ]
    scenario.message_manager.instructions = (
        dossier["title"][locale] + "\n\n" + "\n\n".join(goals)
    )
    scenario.message_manager.hints = "\n\n".join(
        s["text"][locale]
        for s in dossier["screens"]
        if s["id"] in ("route-help", "economy-help", "recovery-help")
    )
    scenario.message_manager.history = (
        dossier["historicalBrief"][locale]
        + "\n\n"
        + dossier["dramatizationNotice"][locale]
    )
    scenario.message_manager.victory = "\n\n".join(
        s["text"][locale]
        for s in dossier["screens"]
        if s["id"] in ("fact-outro", "persona-outro", "next-episode")
    )
    scenario.message_manager.loss = next(
        s["text"][locale] for s in dossier["screens"] if s["id"] == "defeat"
    )
    output.mkdir(parents=True, exist_ok=True)
    path = output / (binding["episodeId"] + ".aoe2scenario")
    scenario.write_to_file(str(path))
    reopened = AoE2DEScenario.from_file(str(path))
    before, after = native_signature(scenario), native_signature(reopened)
    if before != after:
        differences = [key for key in before if before[key] != after[key]]
        raise RuntimeError(
            "native delivery round-trip changed fields: " + ", ".join(differences)
        )
    reopened.xs_manager.xs_check.raise_on_error = True
    reopened.xs_manager.validate_scenario_xs()
    (output / "native-controller.xs").write_text(
        result.pop("xsSource"), encoding="utf8"
    )
    (output / "source-captions.json").write_text(
        json.dumps(dossier["screens"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf8",
    )
    result.update(
        {
            "scenario": path.name,
            "scenarioSha256": sha256(path),
            "locale": locale,
            "difficulty": level,
            "scenarioVersion": version,
            "triggers": len(scenario.trigger_manager.triggers),
            "initialUnitCountIncludingMarkers": len(
                scenario.unit_manager.get_all_units()
            ),
            "receivingWayfindingProvenance": receiving_wayfinding,
            "status": "private native delivery prototype; not campaign release",
            "historicalApproval": False,
            "generalComposedExportEnabled": False,
        }
    )
    (output / "native-receipt.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return path, result


def _build_preview(root, binding_path, output, locales, levels):
    campaign, dossier, binding = load_delivery_source(root, binding_path)
    if any(locale not in binding["locales"] for locale in locales) or any(
        level not in binding["difficulty"] for level in levels
    ):
        raise ValueError("unsupported preview locale or difficulty")
    coast = coast_intersections(root, binding)
    version = json.loads((root / "config/engine.json").read_text())["scenarioVersion"]
    exporter = runpy.run_path(str(HERE / "export_aoe2.py"))
    reports = []
    private_name = campaign["editorialContract"]["internalName"] + "_PrivateOpening"
    for locale in locales:
        for level in levels:
            folder = output / locale / level
            captured = io.StringIO()
            try:
                with contextlib.redirect_stdout(captured):
                    path, receipt = build_variant(
                        root, dossier, binding, coast, folder, locale, level, version
                    )
            except Exception:
                print(captured.getvalue(), file=sys.stderr)
                raise
            # Reuse the pinned container tool; this is a private single-episode
            # container, never a promoted 30-episode catalogue or global ID change.
            container = folder / (private_name + ".aoe2campaign")
            binary = str(exporter["rge_binary"]())
            subprocess.run(
                [
                    binary,
                    "c",
                    str(container),
                    campaign["editorialContract"]["campaignTitle"][locale],
                    str(path),
                ],
                check=True,
                capture_output=True,
            )
            with tempfile.TemporaryDirectory() as tmp:
                extracted = Path(tmp) / "extracted"
                subprocess.run(
                    [binary, "x", str(container), str(extracted)],
                    check=True,
                    capture_output=True,
                )
                recovered = list(extracted.rglob("*.aoe2scenario"))
                if len(recovered) != 1 or sha256(recovered[0]) != sha256(path):
                    raise RuntimeError(
                        "private episode container did not preserve native scenario"
                    )
            receipt["campaignSha256"] = sha256(container)
            (folder / "native-receipt.json").write_text(
                json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                encoding="utf8",
            )
            reports.append(receipt)
    report = {
        "campaignId": campaign["campaignId"],
        "episodeId": dossier["id"],
        "sourceSha256": binding["sourceSha256"],
        "bindingSha256": sha256(binding_path),
        "variants": reports,
        "gameVerified": False,
        "pending": [
            "actual-engine objectives and optional effects",
            "native save/load and terminal arbitration",
            "map navigation and Roman geographic refinement",
            "difficulty and reward utility calibration",
            "certified campaign UI/SequenceItems and release localization IDs",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "preview-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return report


def build_preview(
    root,
    binding_path,
    output,
    locales=("en", "es-ES"),
    levels=("easy", "standard", "hard"),
):
    if output.exists():
        raise ValueError(
            "use a new preview output directory; existing artifacts are immutable"
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix="private-delivery-", dir=output.parent
    ) as temporary:
        candidate = Path(temporary) / "candidate"
        report = _build_preview(root, binding_path, candidate, locales, levels)
        candidate.rename(output)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("binding", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--locale", choices=["en", "es-ES"], action="append")
    parser.add_argument(
        "--difficulty", choices=["easy", "standard", "hard"], action="append"
    )
    args = parser.parse_args()
    print(
        json.dumps(
            build_preview(
                args.root.resolve(),
                args.binding.resolve(),
                args.output.resolve(),
                args.locale or ("en", "es-ES"),
                args.difficulty or ("easy", "standard", "hard"),
            )
        )
    )


if __name__ == "__main__":
    main()
