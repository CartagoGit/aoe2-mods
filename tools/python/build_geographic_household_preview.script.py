"""Compile a private geographic household preview from an authored plan.

This is the bounded private build path the architect's accepted architecture
describes. It reuses the existing, verified operations instead of copying
them: the DSM extractor, the frame helper, the bilinear raster compiler, the
absolute band quantiser, the shared native base factory, the household
controller adapter, the shared semantic signature and the shared native
artifact service. It owns no world solver, no payment circuit, no TIFF
decoder, no projection, no quantiser and no exporter.

What it does own is the boundary between a development preview and an
approval. The plan is validated with exact keys before any scenario is
modified; the raster is derived from the pinned source through the real
pipeline; the grid and the binding evidence are recomputed and compared with
the plan, so a stored evidence flag is never trusted. The output carries the
development notice, the source and terrain hashes, the band table, the
coverage and the override provenance. `nativeTerrainWritten` becomes true
only after the terrain was written, and historical approval, game verification
and the public composed export stay false in every mode.

It is not a historical build, not an engine test and not a distribution.
"""

import argparse
import contextlib
import copy
import hashlib
import io
import json
import math
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MAP = HERE.parent / "map"

VALIDATOR = runpy.run_path(str(HERE / "private_geographic_preview.validator.py"))
EXTRACTOR = runpy.run_path(str(MAP / "geographic_dsm_extractor.py"))
COMPILER = runpy.run_path(str(MAP / "geographic_raster.compiler.py"))
QUANTISER = runpy.run_path(str(MAP / "terrain_quantiser.py"))
CORRIDOR_AUDIT = runpy.run_path(str(MAP / "geographic_corridor_audit.helper.py"))
BASE_FACTORY = runpy.run_path(str(HERE / "private_household_base.factory.py"))
ARTIFACT_SERVICE = runpy.run_path(str(HERE / "private_native_artifact.service.py"))
FACTORY = runpy.run_path(str(HERE / "native_scenario.factory.py"))
ADAPTER = runpy.run_path(str(HERE / "native_household.adapter.py"))
RECEIVING_WAYFINDING = runpy.run_path(
    str(HERE / "private_wayfinding.renderer.py")
)["render_receiving_wayfinding"]

SYNTHETIC_NOTICE = (
    "explicitly nonhistorical synthetic geographic test fixture compiled "
    "through the real raster, frame and quantisation pipeline; not the "
    "Jerusalem map, not an approved route, not a historical build and not a "
    "game-played mission"
)
DEVELOPMENT_STATUS = (
    "private development preview; modern relief is a reference, not a survey, "
    "and no historical approval, engine evidence or public distribution is "
    "claimed"
)
TERRAIN_CLASSIFICATION = (
    "derived modern reference relief from the pinned raster through the "
    "absolute band table; not an ancient bare-earth elevation and not "
    "approved terrain"
)


def sha256(path):
    """The SHA-256 of a file's bytes."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _clear_extractor_caches():
    """Drop the extractor's file caches.

    The extractor caches the raster by path. A same-path changed source must
    not survive the fresh hash and verification boundary, so the cache is
    dropped before the extraction and before the re-read.
    """
    for name in ("_read_tiff", "_tile_rows"):
        cached = getattr(EXTRACTOR.get(name), "cache_clear", None)
        if cached is not None:
            cached()


def validate_geotiff_boundary(plan, path):
    """Check TIFF tags the legacy extractor cannot enforce in either mode."""
    raster = plan["raster"]
    reference = EXTRACTOR["georeference"](str(path))
    if reference["modelTypeGeoKey"] != 2:
        raise ValueError("a pinned TIFF must declare geographic model type 2")
    if reference["geographicTypeGeoKey"] != 4326:
        raise ValueError("a pinned TIFF must declare geographic CRS 4326")
    expected_raster_type = 2 if raster["sampleAnchor"] == "centre" else 1
    if reference["rasterTypeGeoKey"] != expected_raster_type:
        raise ValueError("the TIFF raster type does not match the declared sample anchor")
    if (reference["imageWidth"], reference["imageLength"]) != (
        raster["width"],
        raster["height"],
    ):
        raise ValueError("the TIFF dimensions do not match the pinned raster dimensions")

    scale = reference["modelPixelScaleTag"]
    if len(scale) != 3 or any(not math.isfinite(float(value)) for value in scale):
        raise ValueError("a pinned TIFF needs three finite model pixel scale values")
    if float(scale[0]) <= 0 or float(scale[1]) <= 0:
        raise ValueError("a pinned TIFF needs positive X and Y pixel scales")
    tiepoint = reference["modelTiepointTag"]
    if len(tiepoint) != 6 or any(
        not math.isfinite(float(value)) for value in tiepoint
    ):
        raise ValueError("a pinned TIFF needs exactly one finite six-value tiepoint")
    if [float(value) for value in tiepoint[:3]] != [0.0, 0.0, 0.0]:
        raise ValueError("a pinned TIFF tiepoint must start at raster origin [0,0,0]")
    if reference["gdalNoData"] is not None:
        raise ValueError("a pinned TIFF with GDAL_NODATA needs explicit nodata support")


def _bands(plan):
    """The explicit band table of the plan, checked to increase."""
    bands = tuple(
        (float(band["fromMetres"]), int(band["nativeLevel"]))
        for band in plan["bands"]
    )
    if not bands:
        raise ValueError("the plan needs an explicit band table")
    previous = None
    for metres, level in bands:
        if previous is not None and (metres <= previous[0] or level <= previous[1]):
            raise ValueError("the band thresholds and levels must increase")
        previous = (metres, level)
    return bands


def derive_geographic_grid(root, plan, *, raster_path=None):
    """Derive the native grid of one plan from its pinned raster.

    The extraction, the projection, the resampling and the quantisation are
    the existing ones. The frame size and the bands come from the plan, so
    the Edirne defaults never collapse a district into its top band.
    """
    raster = plan["raster"]
    path = Path(raster_path) if raster_path else Path(root) / raster["path"]
    width = int(raster["width"])
    height = int(raster["height"])
    pinned = raster["sha256"]
    if sha256(path) != pinned:
        raise ValueError("the pinned raster changed before the extraction")
    _clear_extractor_caches()
    validate_geotiff_boundary(plan, path)
    grid = EXTRACTOR["extract_window"](
        str(path),
        column_start=0,
        column_end=width - 1,
        row_start=0,
        row_end=height - 1,
        sample_anchor=raster["sampleAnchor"],
        vertical_datum=raster["verticalDatum"],
        source_classification=raster["sourceClassification"],
        licence_notice_path=raster["licenseNoticePath"],
    )
    _clear_extractor_caches()
    verification = EXTRACTOR["verify_extraction"](
        grid, str(path), column_start=0, row_start=0
    )
    if not verification["verified"]:
        raise ValueError("the extracted samples did not match the source raster")
    if verification["sampleCount"] != width * height:
        raise ValueError("the extraction did not read every pinned sample")
    if sha256(path) != pinned:
        raise ValueError("the source raster changed during the extraction")
    candidate = COMPILER["compile_height_candidate"](
        grid, plan["frame"]["bbox"], int(plan["frame"]["mapSize"])
    )
    if not candidate["completeSampleCoverage"]:
        raise ValueError("the derived grid has an incomplete sample coverage")
    quantised = QUANTISER["quantise_height_candidate"](candidate, _bands(plan))
    levels = quantised["levelRows"]
    for row in levels:
        for level in row:
            if level is None:
                raise ValueError("the derived grid kept a cell without data")
            if not 0 <= int(level) <= 7:
                raise ValueError("a derived native level is outside 0..7")
    if quantised["nodataCells"]:
        raise ValueError("the derived grid kept cells without data")
    terrain_sha = hashlib.sha256(
        json.dumps(levels, sort_keys=True, separators=(",", ":")).encode("utf8")
    ).hexdigest()
    return {
        "grid": grid,
        "verification": verification,
        "candidate": candidate,
        "quantised": quantised,
        "levels": levels,
        "terrainSha256": terrain_sha,
        "levelHistogram": [
            int(quantised["levelHistogram"][str(level)]) for level in range(8)
        ],
        "rangeMetres": quantised["rangeMetres"],
        "cliffEdgeCount": int(quantised["cliffEdgeCount"]),
    }


def _check_evidence_drift(plan, derived):
    """Reject a grid that no longer matches the plan's declared evidence."""
    declared = plan["evidence"]
    if derived["levelHistogram"] != list(declared["levelHistogram"]):
        raise ValueError(
            "the derived level histogram does not match the plan's evidence; "
            "the grid drifted"
        )
    declared_range = [float(value) for value in declared["modernHeightRangeMetres"]]
    derived_range = [float(value) for value in derived["rangeMetres"]]
    if any(abs(a - b) > 1e-6 for a, b in zip(declared_range, derived_range)):
        raise ValueError(
            "the derived height range does not match the plan's evidence; the "
            "grid drifted"
        )
    if derived["cliffEdgeCount"] != int(declared["adjacentLevelJumpAtLeast2Count"]):
        raise ValueError(
            "the derived adjacent level jumps do not match the plan's evidence; "
            "the grid drifted"
        )


def derive_preview_binding(validated, derived):
    """Derive the preview binding from the pinned source and the plan.

    Every original identity, the household ledger, the payment rules, the
    survival rules, the narration, the stock vectors and the source position
    and offset of each body survive. Only the moves the plan lists are
    applied, and the source binding itself is never modified.
    """
    plan = validated["plan"]
    binding = copy.deepcopy(validated["binding"])
    overrides = {override["id"]: override for override in validated["overrides"]}
    for entity in binding["entities"]:
        override = overrides.get(entity["id"])
        if override is not None:
            entity["position"] = [float(value) for value in override["toPosition"]]
    corridors = []
    for corridor in validated["corridors"]:
        corridors.append(
            {
                "id": corridor["id"],
                "widthTiles": corridor["widthTiles"],
                "points": [
                    [float(point[0]), float(point[1])]
                    for point in corridor["tilePoints"]
                ],
                "sourceComparisonId": corridor["sourceComparisonId"],
                "hubOrder": list(corridor["hubOrder"]),
                "status": corridor["status"],
            }
        )
    binding["map"] = dict(binding["map"])
    binding["map"]["size"] = validated["frameSize"]
    binding["map"]["bbox"] = [float(value) for value in validated["bbox"]]
    binding["map"]["corridors"] = corridors
    binding["map"]["routeApproved"] = False
    binding["map"]["nativeElevation"] = {
        "assignment": "absolute band table over the pinned modern raster",
        "bands": [
            {"fromMetres": metres, "nativeLevel": level}
            for metres, level in validated["bands"]
        ],
        "levelHistogram": {
            str(index): count for index, count in enumerate(derived["levelHistogram"])
        },
        "historicalApproval": False,
        "gameVerified": False,
    }
    binding["map"]["nativeElevationClassification"] = TERRAIN_CLASSIFICATION
    binding["privatePreviewOverrides"] = [
        dict(override, applied=True) for override in validated["overrides"]
    ]
    if validated["mode"] == "fixture":
        binding["synthetic"] = True
        binding["syntheticNotice"] = SYNTHETIC_NOTICE
        binding["map"]["synthetic"] = True
        binding["map"]["syntheticNotice"] = SYNTHETIC_NOTICE
    binding["developmentNotice"] = DEVELOPMENT_STATUS
    binding["historicalApproval"] = False
    binding["gameVerified"] = False
    return binding


def _audit_corridors(validated, derived):
    """Audit every authored corridor against the derived grid."""
    corridors = [
        {
            "id": corridor["id"],
            "widthTiles": corridor["widthTiles"],
            "points": [tuple(point) for point in corridor["tilePoints"]],
        }
        for corridor in validated["corridors"]
    ]
    report = CORRIDOR_AUDIT["audit_corridors"](
        corridors,
        validated["frameSize"],
        levels=derived["levels"],
        known_water_cells=validated["plan"]["terrain"]["knownWaterCells"],
    )
    if not report["accepted"]:
        reasons = "; ".join(
            violation["reason"]
            for corridor in report["corridors"]
            for violation in corridor["violations"]
        )
        raise ValueError("the corridor audit refused the plan: " + reasons)
    return report


def _check_layout_policy(validated, source_evidence, derived_evidence):
    """The derived layout must respect the plan's declared policy."""
    policy = validated["policy"]
    if derived_evidence["minimumBodyCentreDistanceTiles"] < policy[
        "minimumBodyCentreDistanceTiles"
    ] - 1e-9:
        raise ValueError(
            "the derived bodies are closer than the plan's minimum body centre "
            "distance"
        )
    for field, expected in (
        ("originalActorCount", policy["originalBodies"]),
        ("zoneCount", policy["zones"]),
        ("mainOriginalCount", policy["mainOriginals"]),
        ("optionalOriginalCount", policy["optionalOriginals"]),
    ):
        if derived_evidence[field] != expected:
            raise ValueError(f"the derived {field} does not match the plan")
    if source_evidence["minimumStoreClearanceBeyondCirclePlus2ApproachPlus3ConservativeExtentTiles"] is not None:
        if (
            derived_evidence[
                "minimumStoreClearanceBeyondCirclePlus2ApproachPlus3ConservativeExtentTiles"
            ]
            < source_evidence[
                "minimumStoreClearanceBeyondCirclePlus2ApproachPlus3ConservativeExtentTiles"
            ] - 1e-9
        ):
            raise ValueError(
                "the listed move reduces the store clearance; the bounded "
                "override may not do that"
            )


def _conservative_envelope(levels, centre, extent):
    """The conservative cell-footprint envelope of one body.

    The envelope is the disc of radius extent + sqrt(0.5) around the native
    centre: sqrt(0.5) is the largest distance from the centre of a unit tile
    to any point of its own footprint.
    """
    radius = extent + math.sqrt(0.5)
    centre_x, centre_y = centre
    cells = []
    first_x = int(math.floor(centre_x - radius)) - 1
    last_x = int(math.ceil(centre_x + radius)) + 1
    first_y = int(math.floor(centre_y - radius)) - 1
    last_y = int(math.ceil(centre_y + radius)) + 1
    for j in range(first_y, last_y + 1):
        for i in range(first_x, last_x + 1):
            if (i + 0.5 - centre_x) ** 2 + (j + 0.5 - centre_y) ** 2 > radius * radius:
                continue
            if 0 <= j < len(levels) and 0 <= i < len(levels[j]):
                cells.append((i, j))
    return cells


def _check_override_envelopes(validated, derived):
    """The declared conservative envelope of every listed move is recomputed."""
    for override in validated["overrides"]:
        centre = VALIDATOR["native_centre"](override["toPosition"])
        cells = _conservative_envelope(
            derived["levels"], centre, override["conservativeExtentTiles"]
        )
        if len(cells) != override["uniformEnvelopeCellCount"]:
            raise ValueError(
                "the conservative envelope of the listed move holds "
                f"{len(cells)} cells, not the declared "
                f"{override['uniformEnvelopeCellCount']}"
            )
        levels = {int(derived["levels"][j][i]) for i, j in cells}
        if levels != {int(override["uniformEnvelopeLevel"])}:
            raise ValueError(
                "the conservative envelope of the listed move is not uniform at "
                f"the declared level {override['uniformEnvelopeLevel']}"
            )


def _audit_summary(report):
    """The corridor audit without the full cell list."""
    return [
        {
            key: value
            for key, value in corridor.items()
            if key not in ("includedCells", "authoredPoints")
        }
        for corridor in report["corridors"]
    ]


def label_preview_scenario(scenario, dossier, locale, notice):
    """Carry the development notice inside the artifact, not only in a receipt."""
    screens = {screen["id"]: screen for screen in dossier["screens"]}
    goals = [
        objective["text"][locale]
        for objective in dossier["objectivePlan"] + dossier["secondaryObjectives"]
    ]
    scenario.message_manager.instructions = (
        notice + "\n\n" + dossier["title"][locale] + "\n\n" + "\n\n".join(goals)
    )
    scenario.message_manager.hints = "\n\n".join(
        screens[key]["text"][locale]
        for key in ("route-help", "economy-help", "recovery-help")
    )
    scenario.message_manager.history = (
        dossier["historicalBrief"][locale]
        + "\n\n"
        + dossier["dramatizationNotice"][locale]
    )
    scenario.message_manager.victory = "\n\n".join(
        screens[key]["text"][locale] for key in ("fact-outro", "persona-outro")
    )
    scenario.message_manager.loss = screens["defeat"]["text"][locale]


def _native_tiles(derived, base_terrain):
    """The native tiles of the derived grid."""
    tiles = []
    for y, row in enumerate(derived["levels"]):
        for x, level in enumerate(row):
            tiles.append(
                {
                    "position": {"x": x, "y": y},
                    "terrain": base_terrain,
                    "elevation": int(level),
                }
            )
    return tiles


def build_variant(
    validated,
    derived,
    output,
    locale,
    level,
    version,
):
    """Compile one private variant and prove it."""
    dossier = validated["dossier"]
    binding = derived["binding"]
    authored_presentation = validated["presentation"][locale]
    notice = (
        SYNTHETIC_NOTICE + "\n\n" + authored_presentation
        if validated["mode"] == "fixture"
        else DEVELOPMENT_STATUS + "\n\n" + authored_presentation
    )
    base, mapping = BASE_FACTORY["build_private_household_base"](
        binding,
        dossier,
        level,
        scenario_id=validated["artifactScenarioId"],
        size=validated["frameSize"],
        base_terrain=validated["plan"]["terrain"]["baseTerrain"],
        tiles=derived["tiles"],
    )
    scenario, native_ids, _ = FACTORY["create_native_scenario_base"](base, version)
    units = {
        entity_id: native_ids[native_name] for entity_id, native_name in mapping.items()
    }
    result = ADAPTER["compile_household_controller"](
        scenario, units, dossier, binding, locale
    )
    wayfinding_provenance = RECEIVING_WAYFINDING(
        scenario, binding["zones"], locale
    )
    label_preview_scenario(scenario, dossier, locale, notice)
    xs_source = result.pop("xsSource")
    artifact = ARTIFACT_SERVICE["write_and_verify_artifact"](
        scenario,
        output,
        validated["artifactScenarioId"],
        xs_source=xs_source,
    )
    VALIDATOR["verify_source_hashes"](validated)
    receipt = {
        "scenario": artifact["scenario"],
        "scenarioSha256": artifact["scenarioSha256"],
        "xsFile": artifact["xsFile"],
        "xsSha256": artifact["xsSha256"],
        "locale": locale,
        "difficulty": level,
        "scenarioVersion": version,
        "developmentNotice": notice,
        "status": DEVELOPMENT_STATUS,
        "syntheticFixture": validated["mode"] == "fixture",
        "syntheticNotice": SYNTHETIC_NOTICE if validated["mode"] == "fixture" else None,
        "artifactScenarioId": validated["artifactScenarioId"],
        "sourceBindingSha256": validated["sourceHashes"]["binding"],
        "sourceBindingPath": str(validated["bindingPath"].relative_to(validated["root"])),
        "sourceCampaignSha256": validated["sourceHashes"]["campaign"],
        "rasterSha256": validated["sourceHashes"]["raster"],
        "terrainSha256": derived["terrainSha256"],
        "bands": [
            {"fromMetres": metres, "nativeLevel": level}
            for metres, level in validated["bands"]
        ],
        "levelHistogram": {
            str(index): count for index, count in enumerate(derived["levelHistogram"])
        },
        "coverage": {
            "completeSampleCoverage": True,
            "missingSamples": {},
            "nodataCells": 0,
            "sourceSamplesVerified": derived["verification"]["sampleCount"],
            "nativeHeightCells": validated["frameSize"] ** 2,
        },
        "overrideProvenance": derived["binding"]["privatePreviewOverrides"],
        "receivingWayfindingProvenance": wayfinding_provenance,
        "layoutEvidence": derived["layoutEvidence"],
        "corridorAudit": _audit_summary(derived["corridorAudit"]),
        "nativeTerrainWritten": True,
        "nativeRoundTripVerified": artifact["nativeRoundTripVerified"],
        "xsChecked": artifact["xsChecked"],
        "triggers": len(scenario.trigger_manager.triggers),
        "initialUnitCountIncludingMarkers": len(
            scenario.unit_manager.get_all_units()
        ),
        "historicalApproval": False,
        "gameVerified": False,
        "generalComposedExportEnabled": False,
        "publicDistributionAuthorized": False,
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "native-receipt.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return receipt


def build_geographic_preview(
    root,
    plan_path,
    output,
    locales=("en", "es-ES"),
    levels=("easy", "standard", "hard"),
):
    """Compile the private preview of one authorized plan."""
    root = Path(root).resolve()
    validated = VALIDATOR["validate_private_geographic_plan"](root, plan_path)
    plan = validated["plan"]
    output = VALIDATOR["require_output_outside_inputs"](
        output,
        [
            Path(plan_path),
            validated["bindingPath"],
            validated["campaignPath"],
            validated["rasterPath"],
            root / plan["raster"]["licenseNoticePath"],
        ],
    )
    if any(locale not in validated["presentation"] for locale in locales):
        raise ValueError("unsupported preview locale")
    if any(level not in validated["buildPolicy"]["difficulties"] for level in levels):
        raise ValueError("unsupported preview difficulty")
    derived = derive_geographic_grid(
        root, plan, raster_path=validated["rasterPath"]
    )
    _check_evidence_drift(plan, derived)
    binding = derive_preview_binding(validated, derived)
    VALIDATOR["verify_derived_binding"](
        validated["binding"], binding, validated["overrides"]
    )
    source_evidence = VALIDATOR["derive_layout_evidence"](
        validated["binding"], validated["policy"]
    )
    layout_evidence = VALIDATOR["derive_layout_evidence"](
        binding, validated["policy"]
    )
    _check_layout_policy(validated, source_evidence, layout_evidence)
    _check_override_envelopes(validated, derived)
    corridor_audit = _audit_corridors(validated, derived)
    tiles = _native_tiles(derived, plan["terrain"]["baseTerrain"])
    version = json.loads((root / "config/engine.json").read_text())["scenarioVersion"]
    derived = dict(
        derived,
        binding=binding,
        tiles=tiles,
        layoutEvidence=layout_evidence,
        corridorAudit=corridor_audit,
    )
    output = Path(output)
    VALIDATOR["verify_source_hashes"](validated)
    reports = []
    for locale in locales:
        for level in levels:
            folder = output / locale / level
            captured = io.StringIO()
            try:
                with contextlib.redirect_stdout(captured):
                    receipt = build_variant(
                        validated, derived, folder, locale, level, version
                    )
            except Exception:
                print(captured.getvalue(), file=sys.stderr)
                raise
            reports.append(receipt)
    VALIDATOR["verify_source_hashes"](validated)
    report = {
        "kind": "private-geographic-household-preview-report",
        "campaignId": plan["campaignId"],
        "episodeId": plan["episodeId"],
        "mode": validated["mode"],
        "artifactScenarioId": validated["artifactScenarioId"],
        "planPath": str(Path(plan_path).resolve().relative_to(root)),
        "planSha256": validated["sourceHashes"]["plan"],
        "sourceBindingSha256": validated["sourceHashes"]["binding"],
        "sourceBindingPath": str(
            validated["bindingPath"].relative_to(root)
        ),
        "sourceCampaignPath": str(validated["campaignPath"].relative_to(root)),
        "rasterPath": str(validated["rasterPath"].relative_to(root)),
        "rasterSha256": validated["sourceHashes"]["raster"],
        "terrainSha256": derived["terrainSha256"],
        "bands": [
            {"fromMetres": metres, "nativeLevel": level}
            for metres, level in validated["bands"]
        ],
        "levelHistogram": {
            str(index): count for index, count in enumerate(derived["levelHistogram"])
        },
        "coverage": {
            "completeSampleCoverage": True,
            "missingSamples": {},
            "nodataCells": 0,
            "sourceSamplesVerified": derived["verification"]["sampleCount"],
            "nativeHeightCells": validated["frameSize"] ** 2,
        },
        "overrideProvenance": derived["binding"]["privatePreviewOverrides"],
        "layoutEvidence": layout_evidence,
        "corridorAudit": corridor_audit,
        "syntheticFixture": validated["mode"] == "fixture",
        "syntheticNotice": SYNTHETIC_NOTICE if validated["mode"] == "fixture" else None,
        "developmentNotice": DEVELOPMENT_STATUS,
        "historicalApproval": False,
        "gameVerified": False,
        "generalComposedExportEnabled": False,
        "publicDistributionAuthorized": False,
        "variants": reports,
        "pending": [
            "an independent review of the actual source, geometry and override",
            "engine pathfinding, house and marker collision, save/load and terminal evidence",
            "difficulty and reward utility calibration",
            "certified campaign UI/SequenceItems and release localization IDs",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    VALIDATOR["verify_source_hashes"](validated)
    (output / "preview-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--locale", choices=["en", "es-ES"], action="append")
    parser.add_argument(
        "--difficulty", choices=["easy", "standard", "hard"], action="append"
    )
    args = parser.parse_args()
    print(
        json.dumps(
            build_geographic_preview(
                args.root.resolve(),
                args.plan.resolve(),
                args.output.resolve(),
                args.locale or ("en", "es-ES"),
                args.difficulty or ("easy", "standard", "hard"),
            )
        )
    )


if __name__ == "__main__":
    main()
