"""Focused native evidence for the private geographic household preview.

Every positive case here is an explicitly labelled synthetic fixture that
travels the real pipeline: the pinned TIFF is read by the existing extractor,
the frame helper and the bilinear compiler build the grid, the absolute band
table quantises it, the shared base factory and the household controller
compile the scenario, and the shared artifact service writes it, reopens it,
compares the complete semantic signature and runs the pinned XS check.

The architect's real plan stays untouched, including its independently owned
authorization decision. The historical build refusal stays, and no engine
executes. The fixture is a development
instrument, not a historical build and not a game observation.
"""

import copy
import json
import math
import runpy
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = runpy.run_path(str(ROOT / "tools/python/private_geographic_preview.validator.py"))
BUILDER = runpy.run_path(
    str(ROOT / "tools/python/build_geographic_household_preview.script.py")
)
HOUSEHOLD_BUILDER = runpy.run_path(
    str(ROOT / "tools/python/build_household_episode.script.py")
)
FRAME = runpy.run_path(str(ROOT / "tools/map/geographic_frame.helper.py"))
CORRIDOR_AUDIT = runpy.run_path(str(ROOT / "tools/map/geographic_corridor_audit.helper.py"))
SIGNATURE = runpy.run_path(str(ROOT / "tools/python/native_signature.helper.py"))

WIKI = ROOT / "docs/wiki/faith-origins/episodes/02-civilian-refuge-jerusalem"
REAL_PLAN = WIKI / "25-private-geographic-preview-plan.json"
REAL_BINDING = WIKI / "19-native-binding-draft.json"
REAL_RASTER = WIKI / "24-modern-surface-frame-crop.tif"
CAMPAIGN = ROOT / "docs/design/odysseys/faith-origins.json"

FIXTURE_SIZE = 300
FIXTURE_BBOX = [35.12, 31.7, 35.3, 31.86]
FIXTURE_ARTIFACT_ID = "synthetic-geographic-household-preview-fixture"
FIXTURE_COLUMNS = 48
FIXTURE_ROWS = 48
FIXTURE_TILE = 16
FIXTURE_LON_MIN = 35.1040
FIXTURE_LON_MAX = 35.3160
FIXTURE_LAT_MAX = 31.8701
FIXTURE_LAT_MIN = 31.6895
# A stepped column gradient: every native level appears, the steps cross one
# band each and the moved body's conservative envelope stays uniform.
FIXTURE_PLATEAU_HEIGHT = 100.0
FIXTURE_PLATEAU_BASE = 250.0
FIXTURE_PLATEAU_COLUMNS = 6
FIXTURE_BANDS = ((300, 1), (400, 2), (500, 3), (600, 4), (700, 5), (800, 6), (900, 7))
FIXTURE_STORE = "02-civilian-refuge-jerusalem.side-3.entity-1"
FIXTURE_CORRIDORS = (
    ("main", 10, [(40, 90), (90, 110), (140, 140), (190, 170), (240, 200)]),
    ("relief", 6, [(40, 90), (70, 140), (120, 180), (190, 170), (240, 200)]),
)
NATIVE_LEVEL_MIN = 0
NATIVE_LEVEL_MAX = 7


def sha256(path):
    return BUILDER["sha256"](path)


def write_synthetic_tiff(
    path,
    columns,
    rows,
    scale,
    tiepoint,
    values,
    *,
    model_type=2,
    raster_type=2,
    geographic_type=4326,
    nodata=None,
):
    """Write a minimal little-endian float32 GeoTIFF with the georeference tags.

    The file is a real tiled TIFF with a model pixel scale, a model tiepoint
    and the geographic GeoKeys, so the existing extractor reads it through the
    same path it reads a real modern crop.
    """
    tiles = []
    for tile_y in range(0, rows, FIXTURE_TILE):
        for tile_x in range(0, columns, FIXTURE_TILE):
            raw = bytearray()
            for j in range(tile_y, min(tile_y + FIXTURE_TILE, rows)):
                for i in range(tile_x, min(tile_x + FIXTURE_TILE, columns)):
                    raw += struct.pack("<f", values[j][i])
            tiles.append(zlib.compress(bytes(raw), 9))
    geo_keys = []
    if model_type is not None:
        geo_keys.extend((1024, 0, 1, model_type))
    if raster_type is not None:
        geo_keys.extend((1025, 0, 1, raster_type))
    if geographic_type is not None:
        geo_keys.extend((2048, 0, 1, geographic_type))
    directory = [1, 1, 0, len(geo_keys) // 4] + geo_keys
    entries = [
        (256, 3, 1, columns),
        (257, 3, 1, rows),
        (258, 3, 1, 32),
        (259, 3, 1, 8),
        (262, 3, 1, 1),
        (277, 3, 1, 1),
        (284, 3, 1, 1),
        (317, 3, 1, 1),
        (322, 3, 1, FIXTURE_TILE),
        (323, 3, 1, FIXTURE_TILE),
        (339, 3, 1, 3),
    ]
    extra = [
        (33550, 12, 3, struct.pack("<3d", *scale)),
        (33922, 12, len(tiepoint), struct.pack("<%dd" % len(tiepoint), *tiepoint)),
        (
            34735,
            3,
            len(directory),
            struct.pack("<%dH" % len(directory), *directory),
        ),
        (
            324,
            4,
            len(tiles),
            b"".join(struct.pack("<I", 0) for _ in tiles),
        ),
        (
            325,
            4,
            len(tiles),
            b"".join(struct.pack("<I", len(tile)) for tile in tiles),
        ),
    ]
    if nodata is not None:
        nodata_bytes = str(nodata).encode("ascii") + b"\x00"
        extra.append((42113, 2, len(nodata_bytes), nodata_bytes))
    count = len(entries) + len(extra)
    extra_offset = 8 + (2 + count * 12 + 4)
    payload = bytearray()
    offsets = {}
    for tag, field_type, number, data in extra:
        offsets[tag] = extra_offset + len(payload)
        payload += data
    tile_offsets = []
    for tile in tiles:
        tile_offsets.append(extra_offset + len(payload))
        payload += tile
    struct.pack_into(
        "<%dI" % len(tile_offsets),
        payload,
        offsets[324] - extra_offset,
        *tile_offsets,
    )
    directory_bytes = bytearray()
    directory_bytes += struct.pack("<H", count)
    for tag, field_type, number, value in sorted(
        entries + [(tag, field_type, number, "offset") for tag, field_type, number, _ in extra]
    ):
        directory_bytes += struct.pack("<HHI", tag, field_type, number)
        if value == "offset":
            directory_bytes += struct.pack("<I", offsets[tag])
        elif field_type == 3:
            directory_bytes += struct.pack("<HH", value, 0)
        else:
            directory_bytes += struct.pack("<I", value)
    directory_bytes += struct.pack("<I", 0)
    Path(path).write_bytes(
        bytes(b"II" + struct.pack("<HI", 42, 8) + directory_bytes + payload)
    )
    return Path(path)


def fixture_surface(columns, rows):
    """The synthetic sample surface: a stepped column gradient."""
    return [
        [
            FIXTURE_PLATEAU_BASE
            + FIXTURE_PLATEAU_HEIGHT * math.floor(column / FIXTURE_PLATEAU_COLUMNS)
            for column in range(columns)
        ]
        for _ in range(rows)
    ]


def fixture_binding(path, dossier, source_binding):
    """The labelled synthetic binding of the fixture, on the fixture frame.

    The established synthetic physical-binding helper supplies the labelled
    identities, the notice and the authored semantics. The fixture then places
    that labelled layout on its own 300 tile frame and pins the result, so the
    source binding and the architect's frame stay untouched.
    """
    synthetic = HOUSEHOLD_BUILDER["synthetic_physical_binding"](
        source_binding, dossier
    )
    factor = FIXTURE_SIZE / 64.0
    for entity in synthetic["entities"]:
        entity["position"] = [
            round(entity["position"][0] * factor, 6),
            round(entity["position"][1] * factor, 6),
        ]
    for zone in synthetic["zones"]:
        zone["centre"] = [
            round(zone["centre"][0] * factor, 6),
            round(zone["centre"][1] * factor, 6),
        ]
    for hub in synthetic["map"].get("hubs") or []:
        hub["centre"] = [
            round(hub["centre"][0] * factor, 6),
            round(hub["centre"][1] * factor, 6),
        ]
    synthetic["map"]["size"] = FIXTURE_SIZE
    synthetic["map"]["bbox"] = list(FIXTURE_BBOX)
    Path(path).write_text(
        json.dumps(synthetic, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return synthetic


def fixture_corridors():
    """The authored fixture corridors, in projected and geographic points."""
    frame = FRAME["make_frame"](FIXTURE_BBOX, FIXTURE_SIZE)
    corridors = []
    for identifier, width, tile_points in FIXTURE_CORRIDORS:
        lon_lat = []
        for x, y in tile_points:
            point = frame.lon_lat_at(x, y)
            lon_lat.append([point[0], point[1]])
        corridors.append(
            {
                "id": identifier,
                "sourceComparisonId": f"synthetic-{identifier}-candidate",
                "mode": "land",
                "widthTiles": width,
                "lonLatPoints": lon_lat,
                "tilePoints": [list(point) for point in tile_points],
                "hubOrder": ["hub-1", "hub-2", "hub-3"],
                "status": (
                    "synthetic development fixture geometry; no route is approved "
                    "and no surveyed ancient route is claimed"
                ),
            }
        )
    return corridors


def fixture_override(binding, levels=None):
    """The one bounded move of the fixture plan."""
    store = next(
        entity for entity in binding["entities"] if entity["id"] == FIXTURE_STORE
    )
    to_position = [
        round(store["position"][0] + 3, 6),
        round(store["position"][1] - 3, 6),
    ]
    return {
        "id": FIXTURE_STORE,
        "fromPosition": list(store["position"]),
        "toPosition": to_position,
        "fromNativeCentre": [
            math.floor(store["position"][0]) + 0.5,
            math.floor(store["position"][1]) + 0.5,
        ],
        "toNativeCentre": [
            math.floor(to_position[0]) + 0.5,
            math.floor(to_position[1]) + 0.5,
        ],
        "deltaTiles": [
            math.floor(to_position[0]) - math.floor(store["position"][0]),
            math.floor(to_position[1]) - math.floor(store["position"][1]),
        ],
        "retainSourcePositionAndOffset": True,
        "authority": (
            "synthetic fixture move inside the same labelled frame; no historic "
            "or archaeological claim"
        ),
        "reason": "synthetic fixture clearance check for the bounded override",
        "conservativeExtentTiles": 3,
        "envelopeExtraTiles": "sqrt(0.5), for a conservative cell-footprint envelope",
        "uniformEnvelopeCellCount": 45,
        "uniformEnvelopeLevel": 3,
        "hubCentreDistanceTiles": 11.389,
        "minimumExtraReceiverClearanceTiles": 3.389,
        "minimumExtraOtherBodyClearanceTiles": 26.463,
        "footprintClaim": (
            "conservative geometric exclusion, not measured engine collision; "
            "engine inspection pending"
        ),
    }


def build_fixture(directory):
    """Write the labelled fixture files and return their paths."""
    campaign = json.loads(CAMPAIGN.read_text(encoding="utf8"))
    dossier = campaign["episodes"][1]
    source_binding = json.loads(REAL_BINDING.read_text(encoding="utf8"))
    binding_path = directory / "synthetic-binding.json"
    binding = fixture_binding(binding_path, dossier, source_binding)
    raster_path = directory / "synthetic-surface.tif"
    step_lon = (FIXTURE_LON_MAX - FIXTURE_LON_MIN) / (FIXTURE_COLUMNS - 1)
    step_lat = (FIXTURE_LAT_MAX - FIXTURE_LAT_MIN) / (FIXTURE_ROWS - 1)
    write_synthetic_tiff(
        raster_path,
        FIXTURE_COLUMNS,
        FIXTURE_ROWS,
        (step_lon, step_lat, 0.0),
        (0.0, 0.0, 0.0, FIXTURE_LON_MIN, FIXTURE_LAT_MAX, 0.0),
        fixture_surface(FIXTURE_COLUMNS, FIXTURE_ROWS),
    )
    notice_path = directory / "synthetic-surface-notice.md"
    notice_path.write_text(
        "# Synthetic geographic test fixture surface\n\n"
        "Synthetic sample grid authored for the i00015/S2 implementation. It is "
        "not a survey, not a modern DSM and not a historic surface.\n",
        encoding="utf8",
    )
    plan = {
        "schemaVersion": 1,
        "kind": "private-geographic-household-preview-plan",
        "date": "2026-11-05",
        "architect": "synthetic fixture authored by the i00015/S2 implementation",
        "status": (
            "synthetic test fixture plan; no historical approval, no engine "
            "evidence and no distribution"
        ),
        "privateBuildAuthorized": True,
        "historicalApproval": False,
        "gameVerified": False,
        "generalComposedExportEnabled": False,
        "campaignId": "faith-origins",
        "episodeId": "02-civilian-refuge-jerusalem",
        "artifactScenarioId": FIXTURE_ARTIFACT_ID,
        "sourceBinding": {
            "path": str(binding_path.relative_to(ROOT)),
            "sha256": sha256(binding_path),
        },
        "sourceCampaign": {
            "path": str(CAMPAIGN.relative_to(ROOT)),
            "sha256": sha256(CAMPAIGN),
            "dossierIndex": 1,
        },
        "raster": {
            "path": str(raster_path.relative_to(ROOT)),
            "sha256": sha256(raster_path),
            "sourceClassification": "synthetic-test",
            "horizontalCrs": "EPSG:4326",
            "sampleAnchor": "centre",
            "heightUnit": "metre",
            "verticalDatum": (
                "synthetic fixture surface; not a surveyed vertical datum"
            ),
            "licenseNoticePath": str(notice_path.relative_to(ROOT)),
            "width": FIXTURE_COLUMNS,
            "height": FIXTURE_ROWS,
        },
        "frame": {
            "mapSize": FIXTURE_SIZE,
            "bbox": list(FIXTURE_BBOX),
            "sampleConvention": (
                "existing frame integer sample index[i,j] maps native tile[i,j]; "
                "body centres snap floor(design)+0.5; report half-cell "
                "displacement, never claim an exact ancient address"
            ),
        },
        "bands": [
            {"fromMetres": metres, "nativeLevel": level}
            for metres, level in FIXTURE_BANDS
        ],
        "terrain": {
            "baseTerrain": "grass-1",
            "purpose": (
                "synthetic test ground with a derived surface; no reconstructed "
                "ancient land and no vegetation mask"
            ),
            "knownWaterCells": [],
            "hydrologyCoverage": (
                "unresolved; empty known-water list is not proof of dry ground"
            ),
            "knownWaterPolicy": (
                "reject any supplied known-water cells in this bounded builder; "
                "never paint known water as land, infer water from level0, "
                "invent a ford/bridge or bypass this refusal"
            ),
            "flatteningAllowed": False,
            "heightInterpolationChangesAllowed": False,
        },
        "corridors": fixture_corridors(),
        "bodyOverrides": [fixture_override(binding)],
        "layoutPolicy": {
            "originalBodies": 17,
            "zones": 10,
            "mainOriginals": 8,
            "optionalOriginals": 9,
            "otherBodyChangesAllowed": False,
            "zoneChangesAllowed": False,
            "minimumBodyCentreDistanceTiles": 4,
            "receiverApproachTiles": 2,
            "storeActualFootprintVerified": False,
            "recomputeDerivedLayoutEvidence": True,
            "priorLayoutFigure": (
                "21-physical-layout.png records the architect's source position "
                "and must not be relabelled as this fixture"
            ),
        },
        "presentation": {
            "en": (
                "Synthetic geographic test fixture. The relief is a generated "
                "sample surface; no historical terrain, route, collision or "
                "balance claim."
            ),
            "es-ES": (
                "Fixture geografico sintetico. El relieve es una superficie de "
                "muestras generada; sin afirmaciones de terreno, ruta, colision "
                "ni equilibrio historicos."
            ),
            "preserveSourceScreens": 39,
            "preserveNarratorOrder": ["fact-intro", "handover", "persona-intro"],
            "continuationEpisodeId": "03-shared-provision-jerusalem",
            "campaignComplete": False,
        },
        "buildPolicy": {
            "locales": ["en", "es-ES"],
            "difficulties": ["easy", "standard", "hard"],
            "nativeBase": "tools/python/native_scenario.factory.py",
            "controller": "tools/python/native_household.adapter.py",
            "signature": "tools/python/native_signature.helper.py",
            "syntheticBuilderMustRemainUnchangedByDefault": True,
            "historicalBuilderRefusalMustRemain": True,
            "engineEvidenceRequiredBeforeCompilation": False,
            "engineEvidenceRequiredBeforeGameVerified": True,
            "publicDistributionAuthorized": False,
        },
        "evidence": {
            "sourceSamplesVerified": FIXTURE_COLUMNS * FIXTURE_ROWS,
            "nativeHeightCells": FIXTURE_SIZE * FIXTURE_SIZE,
            "modernHeightRangeMetres": [0.0, 0.0],
            "levelHistogram": [0] * 8,
            "adjacentLevelJumpAtLeast2Count": 0,
            "independentPixelDecoder": (
                "the existing extractor re-read every sample from the source "
                "bytes of the pinned synthetic TIFF"
            ),
            "priorCorridorAuditLimitation": (
                "the older square fixture helper with even widths covers nine "
                "and five tiles; this preview uses the continuous capsule "
                "envelope"
            ),
            "dataArtifactStatus": (
                "synthetic test fixture; adds no dossier, registered media or "
                "approved historic geometry"
            ),
        },
    }
    plan_path = directory / "synthetic-preview-plan.json"
    plan_path.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    derived = BUILDER["derive_geographic_grid"](ROOT, plan, raster_path=raster_path)
    plan["evidence"]["modernHeightRangeMetres"] = list(derived["rangeMetres"])
    plan["evidence"]["levelHistogram"] = derived["levelHistogram"]
    plan["evidence"]["adjacentLevelJumpAtLeast2Count"] = derived["cliffEdgeCount"]
    override = plan["bodyOverrides"][0]
    centre = VALIDATOR["native_centre"](override["toPosition"])
    cells = BUILDER["_conservative_envelope"](
        derived["levels"], centre, override["conservativeExtentTiles"]
    )
    override["uniformEnvelopeCellCount"] = len(cells)
    override["uniformEnvelopeLevel"] = int(
        derived["levels"][cells[0][1]][cells[0][0]]
    )
    plan_path.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return {
        "directory": directory,
        "plan": plan,
        "planPath": plan_path,
        "bindingPath": binding_path,
        "rasterPath": raster_path,
        "derived": derived,
    }


_FIXTURE = None
_NATIVE_BUILDS = {}


def shared_fixture():
    """The labelled fixture files, written once per process."""
    global _FIXTURE
    if _FIXTURE is None:
        scratch = ROOT / ".cache" / "scratch"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(
            prefix="private-geographic-preview-", dir=scratch
        )
        fixture = build_fixture(Path(temporary.name))
        fixture["temporary"] = temporary
        _FIXTURE = fixture
    return _FIXTURE


def shared_native_build(locales=("en",), levels=("standard",)):
    """The compiled fixture, built once per locale and difficulty."""
    key = (tuple(locales), tuple(levels))
    if key not in _NATIVE_BUILDS:
        fixture = shared_fixture()
        _NATIVE_BUILDS[key] = BUILDER["build_geographic_preview"](
            ROOT,
            fixture["planPath"],
            fixture["directory"] / "build",
            locales=locales,
            levels=levels,
        )
    return _NATIVE_BUILDS[key]


class PrivateGeographicPreviewFixture(unittest.TestCase):
    """The shared fixture of the private geographic preview tests.

    The fixture files and every compiled artifact are built once per process
    and reused by the read-only assertions: a native compilation is an
    expensive operation and it must not run once per assertion. The mutation
    tests write their own inputs and never reuse a compiled artifact.
    """

    def fixture(self):
        return shared_fixture()

    def native_build(self, locales=("en",), levels=("standard",)):
        """The compiled fixture, built once per locale and difficulty."""
        return shared_native_build(locales, levels)

    def variant(self, locales=("en",), levels=("standard",)):
        """The compiled variant receipt."""
        return self.native_build(locales, levels)["variants"][0]

    def plan_copy(self):
        return copy.deepcopy(self.fixture()["plan"])

    def write_plan(self, name, plan):
        path = self.fixture()["directory"] / name
        path.write_text(
            json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
        )
        return path

    def refuse(self, plan, name="mutated-plan.json"):
        path = self.write_plan(name, plan)
        with self.assertRaises(ValueError) as error:
            VALIDATOR["validate_private_geographic_plan"](ROOT, path)
        return str(error.exception)



class PrivateGeographicBoundaryTests(PrivateGeographicPreviewFixture):
    def write_isolated_modern_plan(self, root, authorized):
        """Keep the canonical path and raster without touching the real plan."""
        plan = json.loads(REAL_PLAN.read_text(encoding="utf8"))
        plan["privateBuildAuthorized"] = authorized
        for relative in (plan["raster"]["path"], plan["raster"]["licenseNoticePath"]):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())
        path = root / REAL_PLAN.relative_to(ROOT)
        path.write_text(json.dumps(plan), encoding="utf8")
        return path

    def test_the_fixture_plan_is_accepted_and_is_a_fixture(self):
        validated = VALIDATOR["validate_private_geographic_plan"](
            ROOT, self.fixture()["planPath"]
        )
        self.assertEqual("fixture", validated["mode"])
        self.assertEqual(FIXTURE_SIZE, validated["frameSize"])
        self.assertEqual(17, len(validated["binding"]["entities"]))
        self.assertEqual(10, len(validated["binding"]["zones"]))

    def test_a_synthetic_fixture_cannot_reuse_the_canonical_modern_plan_path(self):
        with self.assertRaises(ValueError) as error:
            VALIDATOR["_validate_fixture_plan_origin"](ROOT, REAL_PLAN.resolve())
        self.assertIn("separately pinned plan file", str(error.exception))

    def test_an_unauthorized_canonical_plan_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = self.write_isolated_modern_plan(root, False)
            with self.assertRaises(ValueError) as error:
                VALIDATOR["validate_private_geographic_plan"](root, path)
        self.assertIn("not authorized", str(error.exception))

    def test_authorized_canonical_plan_still_requires_pinned_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = self.write_isolated_modern_plan(root, True)
            with self.assertRaises(ValueError) as error:
                VALIDATOR["validate_private_geographic_plan"](root, path)
        self.assertIn("sourceBinding.path does not exist", str(error.exception))

    def test_a_copied_true_authorization_cannot_enable_the_modern_plan(self):
        plan = json.loads(REAL_PLAN.read_text(encoding="utf8"))
        plan["privateBuildAuthorized"] = True
        path = self.write_plan("copied-modern-plan.json", plan)
        with self.assertRaises(ValueError) as error:
            VALIDATOR["validate_private_geographic_plan"](ROOT, path)
        self.assertIn("canonical geographic plan", str(error.exception))

    def test_a_repinned_binding_clone_is_not_the_original_binding_19(self):
        plan = json.loads(REAL_PLAN.read_text(encoding="utf8"))
        clone = self.fixture()["directory"] / "repinned-real-binding.json"
        clone.write_bytes(REAL_BINDING.read_bytes())
        plan["sourceBinding"] = {
            "path": str(clone.relative_to(ROOT)),
            "sha256": sha256(clone),
        }
        with self.assertRaises(ValueError) as error:
            VALIDATOR["_validate_source_binding"](plan, ROOT, "modern")
        self.assertIn("original source binding 19", str(error.exception))

    def test_the_real_modern_override_is_exactly_one_bounded_store_move(self):
        plan = json.loads(REAL_PLAN.read_text(encoding="utf8"))
        binding = json.loads(REAL_BINDING.read_text(encoding="utf8"))
        validate = VALIDATOR["_validate_modern_source_boundary"]
        validate(ROOT, REAL_PLAN.resolve(), binding, plan["layoutPolicy"], plan["bodyOverrides"])

        for overrides in ([], plan["bodyOverrides"] + plan["bodyOverrides"]):
            with self.assertRaises(ValueError) as error:
                validate(ROOT, REAL_PLAN.resolve(), binding, plan["layoutPolicy"], overrides)
            self.assertIn("exactly one", str(error.exception))

        other = copy.deepcopy(plan["bodyOverrides"])
        other[0]["id"] = binding["entities"][0]["id"]
        with self.assertRaises(ValueError) as error:
            validate(ROOT, REAL_PLAN.resolve(), binding, plan["layoutPolicy"], other)
        self.assertIn("player-2 store in hub-2", str(error.exception))

        too_far = copy.deepcopy(plan["bodyOverrides"])
        too_far[0]["deltaTiles"] = [0, -5]
        with self.assertRaises(ValueError) as error:
            validate(ROOT, REAL_PLAN.resolve(), binding, plan["layoutPolicy"], too_far)
        self.assertIn("four snapped tiles", str(error.exception))

        too_wide = copy.deepcopy(plan["bodyOverrides"])
        too_wide[0]["conservativeExtentTiles"] = 4
        with self.assertRaises(ValueError) as error:
            validate(ROOT, REAL_PLAN.resolve(), binding, plan["layoutPolicy"], too_wide)
        self.assertIn("exactly three", str(error.exception))

        wrong_approach = copy.deepcopy(plan["layoutPolicy"])
        wrong_approach["receiverApproachTiles"] = 1
        with self.assertRaises(ValueError) as error:
            validate(ROOT, REAL_PLAN.resolve(), binding, wrong_approach, plan["bodyOverrides"])
        self.assertIn("two tiles", str(error.exception))

        outside_hub = copy.deepcopy(plan["bodyOverrides"])
        outside_hub[0]["toPosition"] = [200.05, 185.88]
        outside_hub[0]["toNativeCentre"] = [200.5, 185.5]
        outside_hub[0]["deltaTiles"] = [0, -4]
        outside_hub[0]["hubCentreDistanceTiles"] = round(
            math.dist(outside_hub[0]["toNativeCentre"], [200.05, 197.88]), 3
        )
        with self.assertRaises(ValueError) as error:
            validate(ROOT, REAL_PLAN.resolve(), binding, plan["layoutPolicy"], outside_hub)
        self.assertIn("twelve-tile hub-2 radius", str(error.exception))

    def test_real_modern_tiff_geo_keys_and_anchor_are_checked_from_bytes(self):
        modern_raster = json.loads(REAL_PLAN.read_text(encoding="utf8"))["raster"]
        BUILDER["validate_geotiff_boundary"]({"raster": modern_raster}, REAL_RASTER)

        directory = self.fixture()["directory"]
        values = fixture_surface(FIXTURE_COLUMNS, FIXTURE_ROWS)
        scale = ((FIXTURE_LON_MAX - FIXTURE_LON_MIN) / (FIXTURE_COLUMNS - 1),
                 (FIXTURE_LAT_MAX - FIXTURE_LAT_MIN) / (FIXTURE_ROWS - 1), 0.0)
        tiepoint = (0.0, 0.0, 0.0, FIXTURE_LON_MIN, FIXTURE_LAT_MAX, 0.0)
        bad_sources = (
            ("missing-model.tif", {"model_type": None}, "model type 2"),
            ("wrong-model.tif", {"model_type": 1}, "model type 2"),
            ("wrong-geographic-crs.tif", {"geographic_type": 3857}, "CRS 4326"),
            ("wrong-raster-anchor.tif", {"raster_type": 1}, "sample anchor"),
            ("multiple-tiepoints.tif", {"tiepoint": tiepoint + tiepoint}, "six-value tiepoint"),
            ("nodata-tag.tif", {"nodata": -9999}, "GDAL_NODATA"),
        )
        plan = {
            "raster": {
                "sampleAnchor": "centre",
                "width": FIXTURE_COLUMNS,
                "height": FIXTURE_ROWS,
            }
        }
        for filename, options, message in bad_sources:
            path = directory / filename
            write_synthetic_tiff(
                path,
                FIXTURE_COLUMNS,
                FIXTURE_ROWS,
                scale,
                options.pop("tiepoint", tiepoint),
                values,
                **options,
            )
            with self.assertRaises(ValueError) as error:
                BUILDER["validate_geotiff_boundary"](plan, path)
            self.assertIn(message, str(error.exception), filename)

    def test_bad_pixel_scale_and_raster_origin_are_rejected(self):
        directory = self.fixture()["directory"]
        values = fixture_surface(FIXTURE_COLUMNS, FIXTURE_ROWS)
        tiepoint = (0.0, 0.0, 0.0, FIXTURE_LON_MIN, FIXTURE_LAT_MAX, 0.0)
        plan = {"raster": {"sampleAnchor": "centre", "width": FIXTURE_COLUMNS, "height": FIXTURE_ROWS}}
        for filename, scale, raster_origin, message in (
            ("zero-scale.tif", (0.0, 0.004, 0.0), (0.0, 0.0, 0.0), "positive X and Y"),
            ("nonzero-origin.tif", (0.004, 0.004, 0.0), (1.0, 0.0, 0.0), "raster origin"),
        ):
            path = directory / filename
            point = (*raster_origin, *tiepoint[3:])
            write_synthetic_tiff(
                path, FIXTURE_COLUMNS, FIXTURE_ROWS, scale, point, values
            )
            with self.assertRaises(ValueError) as error:
                BUILDER["validate_geotiff_boundary"](plan, path)
            self.assertIn(message, str(error.exception))

    def test_same_path_cached_geo_keys_are_cleared_before_revalidation(self):
        directory = self.fixture()["directory"]
        path = directory / "same-path-geo-key.tif"
        values = fixture_surface(FIXTURE_COLUMNS, FIXTURE_ROWS)
        scale = ((FIXTURE_LON_MAX - FIXTURE_LON_MIN) / (FIXTURE_COLUMNS - 1),
                 (FIXTURE_LAT_MAX - FIXTURE_LAT_MIN) / (FIXTURE_ROWS - 1), 0.0)
        tiepoint = (0.0, 0.0, 0.0, FIXTURE_LON_MIN, FIXTURE_LAT_MAX, 0.0)
        write_synthetic_tiff(
            path, FIXTURE_COLUMNS, FIXTURE_ROWS, scale, tiepoint, values
        )
        BUILDER["_clear_extractor_caches"]()
        BUILDER["EXTRACTOR"]["georeference"](str(path))
        write_synthetic_tiff(
            path, FIXTURE_COLUMNS, FIXTURE_ROWS, scale, tiepoint, values,
            model_type=1,
        )
        raster = {
            "path": str(path),
            "sha256": sha256(path),
            "sourceClassification": "modern-dsm",
            "sampleAnchor": "centre",
            "verticalDatum": "test datum reported only",
            "licenseNoticePath": "synthetic notice",
            "width": FIXTURE_COLUMNS,
            "height": FIXTURE_ROWS,
        }
        with self.assertRaises(ValueError) as error:
            BUILDER["derive_geographic_grid"](ROOT, {"raster": raster}, raster_path=path)
        self.assertIn("model type 2", str(error.exception))

    def test_fixture_tiff_nodata_sentinel_is_rejected_before_extraction(self):
        directory = self.fixture()["directory"]
        path = directory / "fixture-with-nodata.tif"
        write_synthetic_tiff(
            path,
            FIXTURE_COLUMNS,
            FIXTURE_ROWS,
            ((FIXTURE_LON_MAX - FIXTURE_LON_MIN) / (FIXTURE_COLUMNS - 1),
             (FIXTURE_LAT_MAX - FIXTURE_LAT_MIN) / (FIXTURE_ROWS - 1), 0.0),
            (0.0, 0.0, 0.0, FIXTURE_LON_MIN, FIXTURE_LAT_MAX, 0.0),
            fixture_surface(FIXTURE_COLUMNS, FIXTURE_ROWS),
            nodata=-9999,
        )
        raster = {
            "path": str(path),
            "sha256": sha256(path),
            "sourceClassification": "synthetic-test",
            "sampleAnchor": "centre",
            "verticalDatum": "synthetic test datum",
            "licenseNoticePath": "synthetic notice",
            "width": FIXTURE_COLUMNS,
            "height": FIXTURE_ROWS,
        }
        with self.assertRaises(ValueError) as error:
            BUILDER["derive_geographic_grid"](ROOT, {"raster": raster}, raster_path=path)
        self.assertIn("GDAL_NODATA", str(error.exception))

    def test_an_unknown_key_is_refused(self):
        plan = self.plan_copy()
        plan["unexpectedKey"] = True
        self.assertIn("unknown keys", self.refuse(plan))

    def test_a_missing_key_is_refused(self):
        plan = self.plan_copy()
        del plan["layoutPolicy"]
        self.assertIn("missing keys", self.refuse(plan))

    def test_a_boolean_used_as_an_integer_is_refused(self):
        plan = self.plan_copy()
        plan["frame"]["mapSize"] = True
        self.assertIn("must be an integer", self.refuse(plan))

    def test_a_nonfinite_number_is_refused(self):
        plan = self.plan_copy()
        plan["frame"]["bbox"] = [35.12, 31.7, 35.3, float("nan")]
        self.assertIn("finite", self.refuse(plan))

    def test_a_nonincreasing_band_table_is_refused(self):
        plan = self.plan_copy()
        plan["bands"][2]["fromMetres"] = plan["bands"][1]["fromMetres"]
        self.assertIn("must increase", self.refuse(plan))

    def test_a_band_level_outside_the_native_range_is_refused(self):
        plan = self.plan_copy()
        plan["bands"][3]["nativeLevel"] = 8
        self.assertIn("at most 7", self.refuse(plan))

    def test_a_map_size_outside_the_frame_range_is_refused(self):
        for size in (299, 401):
            plan = self.plan_copy()
            plan["frame"]["mapSize"] = size
            self.assertIn("from 300 to 400", self.refuse(plan))

    def test_a_size_that_does_not_match_the_source_binding_is_refused(self):
        fixture = self.fixture()
        binding_path = fixture["directory"] / "resized-binding.json"
        binding = json.loads(fixture["bindingPath"].read_text(encoding="utf8"))
        binding["map"]["size"] = 320
        binding_path.write_text(
            json.dumps(binding, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
        )
        plan = self.plan_copy()
        plan["sourceBinding"]["path"] = str(binding_path.relative_to(ROOT))
        plan["sourceBinding"]["sha256"] = sha256(binding_path)
        self.assertIn("must match the size", self.refuse(plan))

    def test_a_bounding_box_that_does_not_match_the_source_binding_is_refused(self):
        plan = self.plan_copy()
        plan["frame"]["bbox"] = [35.1, 31.7, 35.3, 31.86]
        self.assertIn("bounding box", self.refuse(plan))

    def test_a_crs_that_is_not_wgs84_is_refused(self):
        plan = self.plan_copy()
        plan["raster"]["horizontalCrs"] = "EPSG:3857"
        self.assertIn("EPSG:4326", self.refuse(plan))

    def test_a_corridor_projection_that_does_not_match_is_refused(self):
        plan = self.plan_copy()
        plan["corridors"][0]["tilePoints"][1] = [
            plan["corridors"][0]["tilePoints"][1][0] + 3.0,
            plan["corridors"][0]["tilePoints"][1][1],
        ]
        self.assertIn("projected", self.refuse(plan))

    def test_a_changed_source_binding_is_refused(self):
        plan = self.plan_copy()
        plan["sourceBinding"]["sha256"] = "0" * 64
        self.assertIn("hash", self.refuse(plan))

    def test_a_changed_raster_is_refused(self):
        plan = self.plan_copy()
        plan["raster"]["sha256"] = "1" * 64
        self.assertIn("hash", self.refuse(plan))

    def test_a_path_outside_the_project_is_refused(self):
        plan = self.plan_copy()
        plan["raster"]["path"] = "../outside.tif"
        self.assertIn("inside the project", self.refuse(plan))

    def test_wrong_original_or_zone_counts_are_refused(self):
        plan = self.plan_copy()
        plan["layoutPolicy"]["originalBodies"] = 16
        self.assertIn("originalBodies", self.refuse(plan))
        plan = self.plan_copy()
        plan["layoutPolicy"]["zones"] = 9
        self.assertIn("zones", self.refuse(plan))

    def test_wrong_stock_vectors_are_refused(self):
        plan = self.plan_copy()
        binding_path = self.fixture()["directory"] / "mutated-binding.json"
        binding = json.loads(self.fixture()["bindingPath"].read_text(encoding="utf8"))
        binding["difficulty"]["standard"]["startingResources"]["food"] = 999
        binding_path.write_text(
            json.dumps(binding, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
        )
        plan = self.plan_copy()
        plan["sourceBinding"]["path"] = str(binding_path.relative_to(ROOT))
        plan["sourceBinding"]["sha256"] = sha256(binding_path)
        self.assertIn("stocks", self.refuse(plan))

    def test_known_water_is_refused(self):
        plan = self.plan_copy()
        plan["terrain"]["knownWaterCells"] = [[10, 10]]
        self.assertIn("known water", self.refuse(plan))

    def test_flattening_is_refused(self):
        plan = self.plan_copy()
        plan["terrain"]["flatteningAllowed"] = True
        self.assertIn("flattening", self.refuse(plan))

    def test_an_unknown_source_classification_is_refused(self):
        plan = self.plan_copy()
        plan["raster"]["sourceClassification"] = "ancient-bare-earth"
        self.assertIn("classification", self.refuse(plan))

    def test_the_dem_classification_is_not_a_supported_discriminator(self):
        plan = self.plan_copy()
        plan["raster"]["sourceClassification"] = "modern-dem"
        self.assertIn("classification", self.refuse(plan))

    def test_a_delta_that_is_not_an_exact_integer_pair_is_refused(self):
        for delta in ([True, False], ["0", "-3"], [0.0, -3.0], [0, -3.4]):
            plan = self.plan_copy()
            plan["bodyOverrides"][0]["deltaTiles"] = delta
            self.assertIn("deltaTiles", self.refuse(plan))

    def test_an_unsafe_artifact_identifier_is_refused(self):
        for identifier in (
            "synthetic-geographic-../../escape",
            "synthetic-geographic-a/b",
            "synthetic-geographic-a\\b",
            "..",
            "/absolute/synthetic-geographic-a",
        ):
            plan = self.plan_copy()
            plan["artifactScenarioId"] = identifier
            self.assertIn("artifactScenarioId", self.refuse(plan))

    def test_the_output_directory_may_not_hold_a_pinned_input(self):
        fixture = self.fixture()
        with self.assertRaises(ValueError) as error:
            BUILDER["build_geographic_preview"](
                ROOT,
                fixture["planPath"],
                fixture["directory"],
                locales=("en",),
                levels=("standard",),
            )
        self.assertIn("pinned source input", str(error.exception))

    def test_a_fixture_identifier_must_carry_the_synthetic_prefix(self):
        plan = self.plan_copy()
        plan["artifactScenarioId"] = "faith-origins-02-private-geographic-preview"
        self.assertIn("synthetic-geographic-", self.refuse(plan))

    def test_the_approval_flags_must_stay_false(self):
        for key in ("historicalApproval", "gameVerified", "generalComposedExportEnabled"):
            plan = self.plan_copy()
            plan[key] = True
            self.assertIn("never", self.refuse(plan))

    def test_a_public_distribution_must_stay_unauthorized(self):
        plan = self.plan_copy()
        plan["buildPolicy"]["publicDistributionAuthorized"] = True
        self.assertIn("public distribution", self.refuse(plan))

    def test_the_reuse_boundary_is_pinned(self):
        plan = self.plan_copy()
        plan["buildPolicy"]["nativeBase"] = "tools/python/other.factory.py"
        self.assertIn("nativeBase", self.refuse(plan))

    def test_a_stored_evidence_flag_does_not_replace_the_derived_grid(self):
        plan = self.plan_copy()
        histogram = [1] * 8
        histogram[0] = FIXTURE_SIZE * FIXTURE_SIZE - 7
        plan["evidence"]["levelHistogram"] = histogram
        path = self.write_plan("drifted-plan.json", plan)
        with self.assertRaises(ValueError) as error:
            BUILDER["build_geographic_preview"](
                ROOT, path, self.fixture()["directory"] / "drifted-build"
            )
        self.assertIn("drifted", str(error.exception))

    def test_a_mutated_source_is_refused_at_build_time(self):
        plan = self.plan_copy()
        raster_path = self.fixture()["directory"] / "mutated-surface.tif"
        raster_path.write_bytes(self.fixture()["rasterPath"].read_bytes())
        plan["raster"]["path"] = str(raster_path.relative_to(ROOT))
        plan["raster"]["sha256"] = sha256(raster_path)
        path = self.write_plan("mutated-raster-plan.json", plan)
        raster_path.write_bytes(raster_path.read_bytes() + b"\x00")
        with self.assertRaises(ValueError) as error:
            BUILDER["build_geographic_preview"](
                ROOT, path, self.fixture()["directory"] / "mutated-build"
            )
        self.assertIn("hash", str(error.exception))

    def test_a_pinned_input_mutation_after_validation_is_refused(self):
        validated = VALIDATOR["validate_private_geographic_plan"](
            ROOT, self.fixture()["planPath"]
        )
        raster_copy = self.fixture()["directory"] / "post-validation-raster.tif"
        raster_copy.write_bytes(validated["rasterPath"].read_bytes())
        validated["rasterPath"] = raster_copy
        raster_copy.write_bytes(raster_copy.read_bytes() + b"\x00")
        with self.assertRaises(ValueError) as error:
            VALIDATOR["verify_source_hashes"](validated)
        self.assertIn("pinned raster changed while building", str(error.exception))

    def test_an_unlisted_move_is_refused(self):
        validated = VALIDATOR["validate_private_geographic_plan"](
            ROOT, self.fixture()["planPath"]
        )
        derived = BUILDER["derive_preview_binding"](validated, self.fixture()["derived"])
        derived["entities"][0]["position"] = [
            derived["entities"][0]["position"][0] + 1.0,
            derived["entities"][0]["position"][1],
        ]
        with self.assertRaises(ValueError) as error:
            VALIDATOR["verify_derived_binding"](
                validated["binding"], derived, validated["overrides"]
            )
        self.assertIn("without a listed override", str(error.exception))

    def test_a_changed_zone_is_refused(self):
        validated = VALIDATOR["validate_private_geographic_plan"](
            ROOT, self.fixture()["planPath"]
        )
        derived = BUILDER["derive_preview_binding"](validated, self.fixture()["derived"])
        derived["zones"][0]["centre"] = [1.0, 1.0]
        with self.assertRaises(ValueError) as error:
            VALIDATOR["verify_derived_binding"](
                validated["binding"], derived, validated["overrides"]
            )
        self.assertIn("zone", str(error.exception))


class PrivateGeographicNativeTests(PrivateGeographicPreviewFixture):
    def test_the_grid_is_derived_through_the_real_pipeline(self):
        derived = self.fixture()["derived"]
        self.assertEqual(FIXTURE_COLUMNS * FIXTURE_ROWS, derived["verification"]["sampleCount"])
        self.assertTrue(derived["verification"]["verified"])
        self.assertEqual(FIXTURE_SIZE * FIXTURE_SIZE, sum(derived["levelHistogram"]))
        self.assertTrue(
            all(count > 0 for count in derived["levelHistogram"]),
            derived["levelHistogram"],
        )
        self.assertEqual(0, derived["cliffEdgeCount"])
        self.assertEqual(
            [FIXTURE_PLATEAU_BASE, FIXTURE_PLATEAU_BASE + 700.0],
            [round(value, 6) for value in derived["rangeMetres"]],
        )

    def test_the_fixture_compiles_a_native_artifact(self):
        receipt = self.variant()
        scenario_path = (
            self.fixture()["directory"]
            / "build"
            / "en"
            / "standard"
            / (FIXTURE_ARTIFACT_ID + ".aoe2scenario")
        )
        self.assertTrue(scenario_path.is_file())
        self.assertTrue(
            (self.fixture()["directory"] / "build" / "en" / "standard" / "native-controller.xs").is_file()
        )
        self.assertTrue(receipt["nativeRoundTripVerified"])
        self.assertTrue(receipt["xsChecked"])
        self.assertTrue(receipt["nativeTerrainWritten"])
        reopened = AoE2DEScenario.from_file(str(scenario_path))
        self.assertEqual(FIXTURE_ARTIFACT_ID, reopened.name)
        signature = SIGNATURE["native_signature"](reopened)
        self.assertEqual(FIXTURE_SIZE * FIXTURE_SIZE, len(signature["terrain"]))
        elevations = {elevation for _, elevation in signature["terrain"]}
        self.assertTrue(elevations)
        self.assertTrue(all(0 <= elevation <= 7 for elevation in elevations))
        self.assertGreater(len(elevations), 1)
        self.assertIn("xsTriggerVariable", signature["xs"])

    def test_the_artifact_carries_the_notice_and_no_approval(self):
        receipt = self.variant()
        self.assertTrue(receipt["syntheticFixture"])
        self.assertIn("nonhistorical", receipt["syntheticNotice"])
        self.assertFalse(receipt["historicalApproval"])
        self.assertFalse(receipt["gameVerified"])
        self.assertFalse(receipt["generalComposedExportEnabled"])
        self.assertFalse(receipt["publicDistributionAuthorized"])
        self.assertIn("Synthetic geographic test fixture", receipt["developmentNotice"])
        scenario_path = (
            self.fixture()["directory"]
            / "build"
            / "en"
            / "standard"
            / (FIXTURE_ARTIFACT_ID + ".aoe2scenario")
        )
        reopened = AoE2DEScenario.from_file(str(scenario_path))
        self.assertIn("Synthetic geographic test fixture", reopened.message_manager.instructions)

    def test_a_short_presentation_cannot_erase_the_native_synthetic_notice(self):
        plan = self.plan_copy()
        plan["presentation"]["en"] = "preview"
        path = self.write_plan("short-presentation-plan.json", plan)
        output = self.fixture()["directory"] / "short-presentation-build"
        BUILDER["build_geographic_preview"](
            ROOT, path, output, locales=("en",), levels=("standard",)
        )
        scenario_path = (
            output / "en" / "standard" / (FIXTURE_ARTIFACT_ID + ".aoe2scenario")
        )
        reopened = AoE2DEScenario.from_file(str(scenario_path))
        self.assertIn("explicitly nonhistorical synthetic geographic test fixture", reopened.message_manager.instructions)
        self.assertIn("\n\npreview\n\n", reopened.message_manager.instructions)

    def test_the_receipt_carries_the_source_and_terrain_evidence(self):
        receipt = self.variant()
        self.assertEqual(sha256(self.fixture()["rasterPath"]), receipt["rasterSha256"])
        self.assertEqual(
            sha256(self.fixture()["bindingPath"]), receipt["sourceBindingSha256"]
        )
        self.assertEqual(sha256(CAMPAIGN), receipt["sourceCampaignSha256"])
        self.assertEqual(
            sha256(self.fixture()["planPath"]), self.native_build()["planSha256"]
        )
        self.assertEqual(len(receipt["terrainSha256"]), 64)
        self.assertEqual(
            receipt["coverage"]["nativeHeightCells"], FIXTURE_SIZE * FIXTURE_SIZE
        )
        self.assertEqual(
            receipt["coverage"]["sourceSamplesVerified"],
            FIXTURE_COLUMNS * FIXTURE_ROWS,
        )
        self.assertEqual(1, len(receipt["overrideProvenance"]))
        self.assertTrue(receipt["overrideProvenance"][0]["applied"])
        self.assertEqual(
            17, receipt["layoutEvidence"]["originalActorCount"]
        )
        self.assertEqual(10, receipt["layoutEvidence"]["zoneCount"])

    def test_the_layout_evidence_is_recomputed_and_the_move_is_bounded(self):
        receipt = self.variant()
        evidence = receipt["layoutEvidence"]
        self.assertGreaterEqual(
            evidence["minimumBodyCentreDistanceTiles"],
            self.fixture()["plan"]["layoutPolicy"]["minimumBodyCentreDistanceTiles"],
        )
        self.assertEqual(
            8, evidence["mainOriginalCount"]
        )
        self.assertEqual(
            9, evidence["optionalOriginalCount"]
        )
        snapped = evidence["nativeSnappedEntities"][FIXTURE_STORE]
        self.assertEqual(
            [
                math.floor(self.fixture()["plan"]["bodyOverrides"][0]["toPosition"][0]) + 0.5,
                math.floor(self.fixture()["plan"]["bodyOverrides"][0]["toPosition"][1]) + 0.5,
            ],
            snapped,
        )

    def test_the_corridor_audit_uses_the_continuous_capsule(self):
        report = self.native_build()["corridorAudit"]
        self.assertTrue(report["accepted"])
        for corridor, (identifier, width, points) in zip(
            report["corridors"], FIXTURE_CORRIDORS
        ):
            self.assertEqual(identifier, corridor["corridorId"])
            self.assertAlmostEqual(
                width / 2.0 + math.sqrt(0.5), corridor["inclusionRadiusTiles"]
            )
            included = {tuple(cell) for cell in corridor["includedCells"]}
            self.assertEqual(corridor["includedCellCount"], len(included))
            # The exact capsule interior is worked out here, independently of
            # the auditor, and the conservative envelope must contain it.
            interior = set()
            xs = [point[0] for point in points]
            ys = [point[1] for point in points]
            for y in range(
                int(min(ys) - width) - 1, int(max(ys) + width) + 2
            ):
                for x in range(
                    int(min(xs) - width) - 1, int(max(xs) + width) + 2
                ):
                    if not (0 <= x < FIXTURE_SIZE and 0 <= y < FIXTURE_SIZE):
                        continue
                    if (
                        CORRIDOR_AUDIT["polyline_distance"](
                            (x + 0.5, y + 0.5), [tuple(point) for point in points]
                        )
                        <= width / 2.0
                    ):
                        interior.add((x, y))
            self.assertTrue(interior)
            self.assertTrue(interior.issubset(included), identifier)
            self.assertGreater(len(included), len(interior), identifier)
            self.assertEqual(0, corridor["nodataCellCount"])
            self.assertEqual(0, corridor["knownWaterCellCount"])
            self.assertFalse(corridor["envelopeLeavesFrame"])
            self.assertEqual(0, corridor["outsideCellCount"])

    def test_the_architect_plan_and_its_sources_are_untouched(self):
        authorization_before = json.loads(REAL_PLAN.read_text(encoding="utf8"))[
            "privateBuildAuthorized"
        ]
        before = {
            "plan": sha256(REAL_PLAN),
            "binding": sha256(REAL_BINDING),
            "campaign": sha256(CAMPAIGN),
            "raster": sha256(REAL_RASTER),
        }
        self.native_build()
        self.assertEqual(before["plan"], sha256(REAL_PLAN))
        self.assertEqual(before["binding"], sha256(REAL_BINDING))
        self.assertEqual(before["campaign"], sha256(CAMPAIGN))
        self.assertEqual(before["raster"], sha256(REAL_RASTER))
        plan = json.loads(REAL_PLAN.read_text(encoding="utf8"))
        self.assertEqual(authorization_before, plan["privateBuildAuthorized"])
        self.assertFalse(plan["historicalApproval"])
        self.assertFalse(plan["gameVerified"])

    def test_the_labeled_synthetic_builder_still_refuses_the_historical_build(self):
        campaign, dossier, binding = HOUSEHOLD_BUILDER["load_household_source"](
            ROOT, REAL_BINDING
        )
        with self.assertRaises(ValueError) as error:
            HOUSEHOLD_BUILDER["refuse_historical_build"](binding)
        self.assertIn("historical Jerusalem build refused", str(error.exception))
        blockers = HOUSEHOLD_BUILDER["historical_build_blockers"](binding)
        self.assertIn("no approved topographic/route decision", blockers)

    def test_a_second_locale_and_difficulty_compiles_its_own_artifact(self):
        receipt = self.variant(locales=("es-ES",), levels=("hard",))
        self.assertEqual("es-ES", receipt["locale"])
        self.assertEqual("hard", receipt["difficulty"])
        self.assertTrue(receipt["nativeRoundTripVerified"])
        self.assertTrue(receipt["xsChecked"])
        scenario_path = (
            self.fixture()["directory"]
            / "build"
            / "es-ES"
            / "hard"
            / (FIXTURE_ARTIFACT_ID + ".aoe2scenario")
        )
        self.assertTrue(scenario_path.is_file())
        reopened = AoE2DEScenario.from_file(str(scenario_path))
        self.assertIn(
            "Fixture geografico sintetico", reopened.message_manager.instructions
        )
        self.assertEqual(FIXTURE_SIZE * FIXTURE_SIZE, len(
            SIGNATURE["native_signature"](reopened)["terrain"]
        ))
        self.assertFalse(receipt["historicalApproval"])
        self.assertFalse(receipt["gameVerified"])


if __name__ == "__main__":
    unittest.main()
