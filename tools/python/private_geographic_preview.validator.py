"""Exact-key validator for a private geographic household preview plan.

A private geographic preview is compiled from an authored plan plus the
existing source. This validator decides whether that plan may be compiled at
all, and it fails closed: an unknown key, a missing key, a boolean used as an
integer, a non-finite number, a band table that does not increase, a size or
bounding box that does not match the pinned source, a path that leaves the
project, a changed source hash, a duplicate or changed original, a wrong
zone count, a wrong stock vector or an override the plan does not list all
stop the build before any scenario is modified.

The plan is the author's decision, so the validator never relaxes a rule to
make a plan compile. It also never trusts a stored evidence flag: the
compiled grid and the derived binding evidence are recomputed by the builder
and compared with the plan, and a mismatch is a grid drift rejection.

Two modes exist and only one discriminator separates them:
`raster.sourceClassification`. The `modern-dsm` mode is the architect's
development input and stays unauthorized until the architect authorizes it.
The `synthetic-test` mode is the labelled artificial fixture used to exercise
this implementation before any real plan is authorized; it needs its own
separately pinned synthetic binding and TIFF grid, a
`synthetic-geographic-` artifact identifier and a map size from 300 to 400.
Every other classification is refused. An authorized fixture plan never
authorizes the architect's plan.
"""

import hashlib
import json
import math
import re
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAME = runpy.run_path(str(HERE.parent / "map" / "geographic_frame.helper.py"))

PLAN_KIND = "private-geographic-household-preview-plan"
PLAN_SCHEMA_VERSION = 1
# The architecture names exactly two source discriminators: the modern DSM of
# the architect's own development plan and the labelled synthetic fixture.
# Every other classification is refused, even when the underlying extractor
# could decode it.
MODERN_CLASSIFICATIONS = ("modern-dsm",)
FIXTURE_CLASSIFICATION = "synthetic-test"
SYNTHETIC_ARTIFACT_PREFIX = "synthetic-geographic-"
MINIMUM_MAP_SIZE = 300
MAXIMUM_MAP_SIZE = 400
NATIVE_LEVEL_MIN = 0
NATIVE_LEVEL_MAX = 7
SOURCE_BINDING_KIND = "private-historical-household-native-binding"
STORE_CONSERVATIVE_EXTENT = 3
HALF_CELL_CONVENTION = "floor(design)+0.5"
TILE_POINT_TOLERANCE = 0.01

TOP_LEVEL_KEYS = frozenset(
    {
        "schemaVersion",
        "kind",
        "date",
        "architect",
        "status",
        "privateBuildAuthorized",
        "historicalApproval",
        "gameVerified",
        "generalComposedExportEnabled",
        "campaignId",
        "episodeId",
        "artifactScenarioId",
        "sourceBinding",
        "sourceCampaign",
        "raster",
        "frame",
        "bands",
        "terrain",
        "corridors",
        "bodyOverrides",
        "layoutPolicy",
        "presentation",
        "buildPolicy",
        "evidence",
    }
)
SOURCE_BINDING_KEYS = frozenset({"path", "sha256"})
SOURCE_CAMPAIGN_KEYS = frozenset({"path", "sha256", "dossierIndex"})
RASTER_KEYS = frozenset(
    {
        "path",
        "sha256",
        "sourceClassification",
        "horizontalCrs",
        "sampleAnchor",
        "heightUnit",
        "verticalDatum",
        "licenseNoticePath",
        "width",
        "height",
    }
)
FRAME_KEYS = frozenset({"mapSize", "bbox", "sampleConvention"})
BAND_KEYS = frozenset({"fromMetres", "nativeLevel"})
TERRAIN_KEYS = frozenset(
    {
        "baseTerrain",
        "purpose",
        "knownWaterCells",
        "hydrologyCoverage",
        "knownWaterPolicy",
        "flatteningAllowed",
        "heightInterpolationChangesAllowed",
    }
)
CORRIDOR_KEYS = frozenset(
    {
        "id",
        "sourceComparisonId",
        "mode",
        "widthTiles",
        "lonLatPoints",
        "tilePoints",
        "hubOrder",
        "status",
    }
)
OVERRIDE_KEYS = frozenset(
    {
        "id",
        "fromPosition",
        "toPosition",
        "fromNativeCentre",
        "toNativeCentre",
        "deltaTiles",
        "retainSourcePositionAndOffset",
        "authority",
        "reason",
        "conservativeExtentTiles",
        "envelopeExtraTiles",
        "uniformEnvelopeCellCount",
        "uniformEnvelopeLevel",
        "hubCentreDistanceTiles",
        "minimumExtraReceiverClearanceTiles",
        "minimumExtraOtherBodyClearanceTiles",
        "footprintClaim",
    }
)
LAYOUT_POLICY_KEYS = frozenset(
    {
        "originalBodies",
        "zones",
        "mainOriginals",
        "optionalOriginals",
        "otherBodyChangesAllowed",
        "zoneChangesAllowed",
        "minimumBodyCentreDistanceTiles",
        "receiverApproachTiles",
        "storeActualFootprintVerified",
        "recomputeDerivedLayoutEvidence",
        "priorLayoutFigure",
    }
)
PRESENTATION_KEYS = frozenset(
    {
        "en",
        "es-ES",
        "preserveSourceScreens",
        "preserveNarratorOrder",
        "continuationEpisodeId",
        "campaignComplete",
    }
)
BUILD_POLICY_KEYS = frozenset(
    {
        "locales",
        "difficulties",
        "nativeBase",
        "controller",
        "signature",
        "syntheticBuilderMustRemainUnchangedByDefault",
        "historicalBuilderRefusalMustRemain",
        "engineEvidenceRequiredBeforeCompilation",
        "engineEvidenceRequiredBeforeGameVerified",
        "publicDistributionAuthorized",
    }
)
EVIDENCE_KEYS = frozenset(
    {
        "sourceSamplesVerified",
        "nativeHeightCells",
        "modernHeightRangeMetres",
        "levelHistogram",
        "adjacentLevelJumpAtLeast2Count",
        "independentPixelDecoder",
        "priorCorridorAuditLimitation",
        "dataArtifactStatus",
    }
)
REUSE_BOUNDARY = {
    "nativeBase": "tools/python/native_scenario.factory.py",
    "controller": "tools/python/native_household.adapter.py",
    "signature": "tools/python/native_signature.helper.py",
}


class PrivatePreviewRejection(ValueError):
    """A private preview plan that may not be compiled."""


def _reject(message):
    raise PrivatePreviewRejection(message)


def _require_exact_keys(owner, expected, label):
    if not isinstance(owner, dict):
        _reject(f"{label} must be an object")
    unknown = sorted(set(owner) - set(expected))
    if unknown:
        _reject(f"{label} has unknown keys: {', '.join(unknown)}")
    missing = sorted(set(expected) - set(owner))
    if missing:
        _reject(f"{label} is missing keys: {', '.join(missing)}")


def _require_bool(owner, key, label):
    value = owner.get(key)
    if type(value) is not bool:
        _reject(f"{label}.{key} must be a boolean")
    return value


def _require_int(owner, key, label, *, minimum=None, maximum=None):
    value = owner.get(key)
    if type(value) is not int:
        _reject(f"{label}.{key} must be an integer, not {type(value).__name__}")
    if minimum is not None and value < minimum:
        _reject(f"{label}.{key} must be at least {minimum}")
    if maximum is not None and value > maximum:
        _reject(f"{label}.{key} must be at most {maximum}")
    return value


def _require_number(owner, key, label):
    value = owner.get(key)
    if type(value) not in (int, float) or not math.isfinite(value):
        _reject(f"{label}.{key} must be a finite number")
    return float(value)


def _require_text(owner, key, label, *, nonempty=True):
    value = owner.get(key)
    if not isinstance(value, str):
        _reject(f"{label}.{key} must be a string")
    if nonempty and not value.strip():
        _reject(f"{label}.{key} must not be empty")
    return value


def _require_safe_identifier(value, label):
    """An artifact identifier is a file name, never a path.

    The identifier becomes a file name inside the artifact directory, so a
    separator, a traversal or an absolute path is refused instead of being
    sanitised.
    """
    if not isinstance(value, str) or not value.strip():
        _reject(f"{label} must be a nonempty identifier")
    if value in (".", ".."):
        _reject(f"{label} must not be a relative path element")
    if "/" in value or "\\" in value:
        _reject(f"{label} must be a plain file name without a path separator")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value):
        _reject(f"{label} must use plain file name characters")
    return value


def _require_pair(value, label):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        _reject(f"{label} must be a pair of numbers")
    if any(type(item) not in (int, float) or not math.isfinite(item) for item in value):
        _reject(f"{label} must be a pair of finite numbers")
    return (float(value[0]), float(value[1]))


def _require_hex_digest(owner, key, label):
    value = owner.get(key)
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        _reject(f"{label}.{key} must be a lowercase SHA-256 digest")
    return value


def sha256(path):
    """The SHA-256 of a file's bytes."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _inside_root(root, relative, label):
    if not isinstance(relative, str) or not relative.strip():
        _reject(f"{label} must be a path inside the project")
    candidate = Path(relative)
    if candidate.is_absolute():
        _reject(f"{label} must be a relative path inside the project")
    resolved = (root / candidate).resolve()
    if not resolved.is_relative_to(root):
        _reject(f"{label} must stay inside the project")
    if not resolved.is_file():
        _reject(f"{label} does not exist: {relative}")
    return resolved


def native_centre(position):
    """The native centre of a design position: floor(design)+0.5."""
    return (math.floor(position[0]) + 0.5, math.floor(position[1]) + 0.5)


def _validate_bands(plan):
    bands = plan.get("bands")
    if not isinstance(bands, list) or not bands:
        _reject("the plan needs an explicit band table")
    previous_metres = None
    previous_level = None
    pairs = []
    for index, band in enumerate(bands):
        label = f"bands[{index}]"
        _require_exact_keys(band, BAND_KEYS, label)
        metres = _require_number(band, "fromMetres", label)
        level = _require_int(
            band, "nativeLevel", label, minimum=1, maximum=NATIVE_LEVEL_MAX
        )
        if metres <= 0:
            _reject(f"{label}.fromMetres must be above zero")
        if previous_metres is not None and metres <= previous_metres:
            _reject("the band thresholds must increase")
        if previous_level is not None and level <= previous_level:
            _reject("the band levels must increase")
        previous_metres, previous_level = metres, level
        pairs.append((metres, level))
    return tuple(pairs)


def _validate_terrain(plan):
    terrain = plan.get("terrain")
    _require_exact_keys(terrain, TERRAIN_KEYS, "terrain")
    _require_text(terrain, "baseTerrain", "terrain")
    _require_text(terrain, "purpose", "terrain")
    _require_text(terrain, "hydrologyCoverage", "terrain")
    _require_text(terrain, "knownWaterPolicy", "terrain")
    known_water = terrain.get("knownWaterCells")
    if not isinstance(known_water, list):
        _reject("terrain.knownWaterCells must be a list")
    if known_water:
        _reject(
            "this bounded builder rejects supplied known water; water and bridge "
            "support needs its own accepted input and operation"
        )
    if _require_bool(terrain, "flatteningAllowed", "terrain"):
        _reject("terrain flattening is not allowed in this builder")
    if _require_bool(terrain, "heightInterpolationChangesAllowed", "terrain"):
        _reject("terrain interpolation changes are not allowed in this builder")
    return terrain


def _validate_frame(plan):
    frame = plan.get("frame")
    _require_exact_keys(frame, FRAME_KEYS, "frame")
    size = _require_int(frame, "mapSize", "frame")
    if not MINIMUM_MAP_SIZE <= size <= MAXIMUM_MAP_SIZE:
        _reject(
            f"frame.mapSize must be from {MINIMUM_MAP_SIZE} to {MAXIMUM_MAP_SIZE}"
        )
    bbox = frame.get("bbox")
    if not isinstance(bbox, list) or len(bbox) != 4:
        _reject("frame.bbox must be four WGS84 bounds")
    if any(type(value) not in (int, float) or not math.isfinite(value) for value in bbox):
        _reject("frame.bbox must be four finite numbers")
    west, south, east, north = (float(value) for value in bbox)
    if not (-180 <= west < east <= 180 and -85 <= south < north <= 85):
        _reject("frame.bbox must be an ordered WGS84 rectangle")
    convention = _require_text(frame, "sampleConvention", "frame")
    if HALF_CELL_CONVENTION not in convention:
        _reject(
            "frame.sampleConvention must declare the half-cell convention "
            f"{HALF_CELL_CONVENTION}"
        )
    return size, (west, south, east, north)


def _validate_corridors(plan, size, bbox):
    corridors = plan.get("corridors")
    if not isinstance(corridors, list) or not corridors:
        _reject("the plan needs at least one authored corridor")
    seen = set()
    for index, corridor in enumerate(corridors):
        label = f"corridors[{index}]"
        _require_exact_keys(corridor, CORRIDOR_KEYS, label)
        identifier = _require_text(corridor, "id", label)
        if identifier in seen:
            _reject(f"corridor identifiers must be unique: {identifier}")
        seen.add(identifier)
        _require_text(corridor, "sourceComparisonId", label)
        _require_text(corridor, "status", label)
        if _require_text(corridor, "mode", label) != "land":
            _reject(f"{label}.mode must be land in this bounded builder")
        width = _require_number(corridor, "widthTiles", label)
        if width <= 0:
            _reject(f"{label}.widthTiles must be positive")
        hub_order = corridor.get("hubOrder")
        if not isinstance(hub_order, list) or not hub_order:
            _reject(f"{label}.hubOrder must be a nonempty list")
        if any(not isinstance(hub, str) or not hub for hub in hub_order):
            _reject(f"{label}.hubOrder must list hub identifiers")
        lon_lat = corridor.get("lonLatPoints")
        tile_points = corridor.get("tilePoints")
        if not isinstance(lon_lat, list) or len(lon_lat) < 2:
            _reject(f"{label}.lonLatPoints needs at least two points")
        if not isinstance(tile_points, list) or len(tile_points) != len(lon_lat):
            _reject(f"{label}.tilePoints must match the authored longitude points")
        for point in lon_lat:
            _require_pair(point, f"{label}.lonLatPoints")
        for point in tile_points:
            _require_pair(point, f"{label}.tilePoints")
    return corridors


def _check_corridor_projection(corridors, size, bbox):
    """The authored tile points must be the projection of the longitude points."""
    frame = FRAME["make_frame"](list(bbox), size)
    for index, corridor in enumerate(corridors):
        label = f"corridors[{index}]"
        for position, (point, tile_point) in enumerate(
            zip(corridor["lonLatPoints"], corridor["tilePoints"])
        ):
            projected = frame.tile_at([float(point[0]), float(point[1])])
            drift = max(
                abs(projected[0] - float(tile_point[0])),
                abs(projected[1] - float(tile_point[1])),
            )
            if drift > TILE_POINT_TOLERANCE:
                _reject(
                    f"{label}.tilePoints[{position}] does not match the projected "
                    f"longitude point of the frame"
                )
            if not (0 <= tile_point[0] < size and 0 <= tile_point[1] < size):
                _reject(f"{label}.tilePoints[{position}] leaves the frame")


def _validate_layout_policy(plan):
    policy = plan.get("layoutPolicy")
    _require_exact_keys(policy, LAYOUT_POLICY_KEYS, "layoutPolicy")
    _require_int(policy, "originalBodies", "layoutPolicy", minimum=1)
    _require_int(policy, "zones", "layoutPolicy", minimum=1)
    _require_int(policy, "mainOriginals", "layoutPolicy", minimum=1)
    _require_int(policy, "optionalOriginals", "layoutPolicy", minimum=1)
    if _require_bool(policy, "otherBodyChangesAllowed", "layoutPolicy"):
        _reject("layoutPolicy does not allow other body changes")
    if _require_bool(policy, "zoneChangesAllowed", "layoutPolicy"):
        _reject("layoutPolicy does not allow zone changes")
    minimum_distance = _require_number(policy, "minimumBodyCentreDistanceTiles", "layoutPolicy")
    if minimum_distance <= 0:
        _reject("layoutPolicy.minimumBodyCentreDistanceTiles must be positive")
    approach = _require_number(policy, "receiverApproachTiles", "layoutPolicy")
    if approach < 0:
        _reject("layoutPolicy.receiverApproachTiles must not be negative")
    if _require_bool(policy, "storeActualFootprintVerified", "layoutPolicy"):
        _reject("the store footprint is not verified by the engine")
    if not _require_bool(policy, "recomputeDerivedLayoutEvidence", "layoutPolicy"):
        _reject("the derived layout evidence must be recomputed")
    _require_text(policy, "priorLayoutFigure", "layoutPolicy")
    return policy


def _validate_presentation(plan):
    presentation = plan.get("presentation")
    _require_exact_keys(presentation, PRESENTATION_KEYS, "presentation")
    _require_text(presentation, "en", "presentation")
    _require_text(presentation, "es-ES", "presentation")
    _require_int(presentation, "preserveSourceScreens", "presentation", minimum=1)
    order = presentation.get("preserveNarratorOrder")
    if not isinstance(order, list) or not order:
        _reject("presentation.preserveNarratorOrder must be a nonempty list")
    if any(not isinstance(item, str) or not item for item in order):
        _reject("presentation.preserveNarratorOrder must list screen identifiers")
    _require_text(presentation, "continuationEpisodeId", "presentation")
    if _require_bool(presentation, "campaignComplete", "presentation"):
        _reject("a private preview is not a complete campaign")
    return presentation


def _validate_build_policy(plan):
    policy = plan.get("buildPolicy")
    _require_exact_keys(policy, BUILD_POLICY_KEYS, "buildPolicy")
    locales = policy.get("locales")
    if not isinstance(locales, list) or not locales:
        _reject("buildPolicy.locales must be a nonempty list")
    if any(locale not in ("en", "es-ES") for locale in locales):
        _reject("buildPolicy.locales must stay inside the supported locales")
    difficulties = policy.get("difficulties")
    if not isinstance(difficulties, list) or not difficulties:
        _reject("buildPolicy.difficulties must be a nonempty list")
    if any(level not in ("easy", "standard", "hard") for level in difficulties):
        _reject("buildPolicy.difficulties must stay inside the supported levels")
    for key, expected in REUSE_BOUNDARY.items():
        if _require_text(policy, key, "buildPolicy") != expected:
            _reject(f"buildPolicy.{key} must stay {expected}")
    if not _require_bool(policy, "syntheticBuilderMustRemainUnchangedByDefault", "buildPolicy"):
        _reject("the labelled synthetic fixture must remain the default builder")
    if not _require_bool(policy, "historicalBuilderRefusalMustRemain", "buildPolicy"):
        _reject("the historical build refusal must remain")
    if _require_bool(policy, "engineEvidenceRequiredBeforeCompilation", "buildPolicy"):
        _reject("compilation does not wait for engine evidence")
    if not _require_bool(policy, "engineEvidenceRequiredBeforeGameVerified", "buildPolicy"):
        _reject("game verification still requires engine evidence")
    if _require_bool(policy, "publicDistributionAuthorized", "buildPolicy"):
        _reject("public distribution is not authorized")
    return policy


def _validate_evidence(plan, size):
    evidence = plan.get("evidence")
    _require_exact_keys(evidence, EVIDENCE_KEYS, "evidence")
    samples = _require_int(evidence, "sourceSamplesVerified", "evidence", minimum=1)
    cells = _require_int(evidence, "nativeHeightCells", "evidence", minimum=1)
    if cells != size * size:
        _reject("evidence.nativeHeightCells must be the map size squared")
    expected_samples = plan["raster"]["width"] * plan["raster"]["height"]
    if samples != expected_samples:
        _reject(
            "evidence.sourceSamplesVerified must be the pinned raster sample count"
        )
    height_range = evidence.get("modernHeightRangeMetres")
    if not isinstance(height_range, list) or len(height_range) != 2:
        _reject("evidence.modernHeightRangeMetres must be a pair")
    if any(type(value) not in (int, float) or not math.isfinite(value) for value in height_range):
        _reject("evidence.modernHeightRangeMetres must be finite")
    if float(height_range[0]) > float(height_range[1]):
        _reject("evidence.modernHeightRangeMetres must be ordered")
    histogram = evidence.get("levelHistogram")
    if not isinstance(histogram, list) or len(histogram) != NATIVE_LEVEL_MAX + 1:
        _reject("evidence.levelHistogram must hold one count per native level")
    for count in histogram:
        if type(count) is not int or count < 0:
            _reject("evidence.levelHistogram must hold nonnegative integers")
    if sum(histogram) != cells:
        _reject("evidence.levelHistogram must add up to the native height cells")
    _require_int(evidence, "adjacentLevelJumpAtLeast2Count", "evidence", minimum=0)
    _require_text(evidence, "independentPixelDecoder", "evidence")
    _require_text(evidence, "priorCorridorAuditLimitation", "evidence")
    _require_text(evidence, "dataArtifactStatus", "evidence")
    return evidence


def _validate_overrides(plan, source_binding):
    overrides = plan.get("bodyOverrides")
    if not isinstance(overrides, list):
        _reject("bodyOverrides must be a list")
    entities = {entity["id"]: entity for entity in source_binding["entities"]}
    seen = set()
    for index, override in enumerate(overrides):
        label = f"bodyOverrides[{index}]"
        _require_exact_keys(override, OVERRIDE_KEYS, label)
        identifier = _require_text(override, "id", label)
        if identifier in seen:
            _reject(f"an override may not be declared twice: {identifier}")
        seen.add(identifier)
        if identifier not in entities:
            _reject(f"{label}.id is not an original of the source binding")
        from_position = _require_pair(override.get("fromPosition"), f"{label}.fromPosition")
        to_position = _require_pair(override.get("toPosition"), f"{label}.toPosition")
        source_position = _require_pair(
            entities[identifier]["position"], "the source binding position"
        )
        if from_position != source_position:
            _reject(f"{label}.fromPosition must be the position of the source binding")
        if to_position == from_position:
            _reject(f"{label}.toPosition must move the body")
        if _require_pair(override.get("fromNativeCentre"), f"{label}.fromNativeCentre") != native_centre(from_position):
            _reject(f"{label}.fromNativeCentre must be floor(design)+0.5")
        if _require_pair(override.get("toNativeCentre"), f"{label}.toNativeCentre") != native_centre(to_position):
            _reject(f"{label}.toNativeCentre must be floor(design)+0.5")
        delta = override.get("deltaTiles")
        if not isinstance(delta, list) or len(delta) != 2:
            _reject(f"{label}.deltaTiles must be a pair of integers")
        if any(type(value) is not int for value in delta):
            _reject(f"{label}.deltaTiles must hold exact integers")
        expected = [
            math.floor(to_position[0]) - math.floor(from_position[0]),
            math.floor(to_position[1]) - math.floor(from_position[1]),
        ]
        if [delta[0], delta[1]] != expected:
            _reject(f"{label}.deltaTiles must be the snapped tile move")
        if not _require_bool(override, "retainSourcePositionAndOffset", label):
            _reject(f"{label} must retain the source position and offset")
        _require_text(override, "authority", label)
        _require_text(override, "reason", label)
        _require_text(override, "envelopeExtraTiles", label)
        _require_text(override, "footprintClaim", label)
        extent = _require_number(override, "conservativeExtentTiles", label)
        if extent <= 0:
            _reject(f"{label}.conservativeExtentTiles must be positive")
        _require_int(override, "uniformEnvelopeCellCount", label, minimum=1)
        _require_int(
            override, "uniformEnvelopeLevel", label, minimum=NATIVE_LEVEL_MIN, maximum=NATIVE_LEVEL_MAX
        )
        _require_number(override, "hubCentreDistanceTiles", label)
        _require_number(override, "minimumExtraReceiverClearanceTiles", label)
        _require_number(override, "minimumExtraOtherBodyClearanceTiles", label)
    return overrides


def _validate_source_binding(plan, root, mode):
    declared = plan.get("sourceBinding")
    _require_exact_keys(declared, SOURCE_BINDING_KEYS, "sourceBinding")
    digest = _require_hex_digest(declared, "sha256", "sourceBinding")
    path = _inside_root(root, declared.get("path"), "sourceBinding.path")
    if sha256(path) != digest:
        _reject("the source binding hash does not match the pinned source")
    binding = json.loads(path.read_text(encoding="utf8"))
    if binding.get("kind") != SOURCE_BINDING_KIND:
        _reject("the pinned source binding is not a private household binding")
    if type(binding.get("schemaVersion")) is not int or binding["schemaVersion"] != 1:
        _reject("the pinned source binding has an unsupported schema version")
    if binding.get("campaignId") != plan.get("campaignId"):
        _reject("the source binding belongs to another campaign")
    if binding.get("episodeId") != plan.get("episodeId"):
        _reject("the source binding belongs to another episode")
    if mode == "fixture":
        if binding.get("synthetic") is not True:
            _reject("a synthetic-test plan needs a labelled synthetic binding")
        if not isinstance(binding.get("syntheticNotice"), str) or not binding[
            "syntheticNotice"
        ].strip():
            _reject("the synthetic binding must carry its synthetic notice")
    else:
        if binding.get("synthetic") is True:
            _reject("a modern plan may not use a synthetic binding")
    return path, binding


def _validate_source_campaign(plan, root):
    declared = plan.get("sourceCampaign")
    _require_exact_keys(declared, SOURCE_CAMPAIGN_KEYS, "sourceCampaign")
    digest = _require_hex_digest(declared, "sha256", "sourceCampaign")
    path = _inside_root(root, declared.get("path"), "sourceCampaign.path")
    if sha256(path) != digest:
        _reject("the source campaign hash does not match the pinned source")
    index = _require_int(declared, "dossierIndex", "sourceCampaign", minimum=0)
    campaign = json.loads(path.read_text(encoding="utf8"))
    if campaign.get("campaignId") != plan.get("campaignId"):
        _reject("the source campaign belongs to another campaign")
    episodes = campaign.get("episodes")
    if not isinstance(episodes, list) or index >= len(episodes):
        _reject("the source campaign has no dossier at the pinned index")
    dossier = episodes[index]
    if dossier.get("id") != plan.get("episodeId"):
        _reject("the pinned dossier is another episode")
    return path, campaign, dossier


def _validate_raster(plan, root):
    raster = plan.get("raster")
    _require_exact_keys(raster, RASTER_KEYS, "raster")
    digest = _require_hex_digest(raster, "sha256", "raster")
    path = _inside_root(root, raster.get("path"), "raster.path")
    _inside_root(root, raster.get("licenseNoticePath"), "raster.licenseNoticePath")
    classification = _require_text(raster, "sourceClassification", "raster")
    if classification not in MODERN_CLASSIFICATIONS + (FIXTURE_CLASSIFICATION,):
        _reject(f"unknown raster source classification: {classification}")
    if _require_text(raster, "horizontalCrs", "raster") != "EPSG:4326":
        _reject("the raster must declare EPSG:4326")
    if _require_text(raster, "sampleAnchor", "raster") not in ("centre", "corner"):
        _reject("the raster sample anchor must be centre or corner")
    if _require_text(raster, "heightUnit", "raster") != "metre":
        _reject("the raster must declare metre heights")
    _require_text(raster, "verticalDatum", "raster")
    width = _require_int(raster, "width", "raster", minimum=1)
    height = _require_int(raster, "height", "raster", minimum=1)
    if sha256(path) != digest:
        _reject("the raster hash does not match the pinned source")
    return path, raster


def validate_private_geographic_plan(root, plan_path):
    """Validate one private geographic preview plan and fail closed."""
    root = Path(root).resolve()
    plan_path = Path(plan_path).resolve()
    if not plan_path.is_relative_to(root):
        _reject("the private preview plan must stay inside the project")
    if not plan_path.is_file():
        _reject("the private preview plan does not exist")
    plan = json.loads(plan_path.read_text(encoding="utf8"))
    _require_exact_keys(plan, TOP_LEVEL_KEYS, "the private preview plan")
    if type(plan.get("schemaVersion")) is not int or plan["schemaVersion"] != PLAN_SCHEMA_VERSION:
        _reject("the private preview plan has an unsupported schema version")
    if plan.get("kind") != PLAN_KIND:
        _reject("the private preview plan has an unsupported kind")
    _require_text(plan, "date", "the private preview plan")
    _require_text(plan, "architect", "the private preview plan")
    _require_text(plan, "status", "the private preview plan")
    _require_text(plan, "campaignId", "the private preview plan")
    _require_text(plan, "episodeId", "the private preview plan")
    artifact_scenario_id = _require_safe_identifier(
        plan.get("artifactScenarioId"),
        "the private preview plan's artifactScenarioId",
    )

    raster_path, raster = _validate_raster(plan, root)
    classification = raster["sourceClassification"]
    mode = "fixture" if classification == FIXTURE_CLASSIFICATION else "modern"
    if mode == "fixture":
        if not artifact_scenario_id.startswith(SYNTHETIC_ARTIFACT_PREFIX):
            _reject(
                "a synthetic-test plan needs a "
                f"{SYNTHETIC_ARTIFACT_PREFIX} artifact identifier"
            )
        if not _require_bool(plan, "privateBuildAuthorized", "the private preview plan"):
            _reject("a synthetic-test plan must carry its own fixture authorization")
    else:
        if not _require_bool(plan, "privateBuildAuthorized", "the private preview plan"):
            _reject(
                "this private plan is not authorized for a development build; "
                "the architect owns that decision"
            )
    if _require_bool(plan, "historicalApproval", "the private preview plan"):
        _reject("a private preview never carries historical approval")
    if _require_bool(plan, "gameVerified", "the private preview plan"):
        _reject("a private preview never carries game verification")
    if _require_bool(plan, "generalComposedExportEnabled", "the private preview plan"):
        _reject("a private preview never enables the public composed export")

    size, bbox = _validate_frame(plan)
    bands = _validate_bands(plan)
    _validate_terrain(plan)
    corridors = _validate_corridors(plan, size, bbox)
    policy = _validate_layout_policy(plan)
    presentation = _validate_presentation(plan)
    build_policy = _validate_build_policy(plan)
    evidence = _validate_evidence(plan, size)

    binding_path, binding = _validate_source_binding(plan, root, mode)
    campaign_path, campaign, dossier = _validate_source_campaign(plan, root)
    overrides = _validate_overrides(plan, binding)

    if binding["map"]["size"] != size:
        _reject("frame.mapSize must match the size of the source binding")
    if [float(value) for value in binding["map"]["bbox"]] != list(bbox):
        _reject("frame.bbox must match the bounding box of the source binding")
    _check_corridor_projection(corridors, size, bbox)
    if policy["originalBodies"] != len(binding["entities"]):
        _reject("layoutPolicy.originalBodies must match the source binding")
    if policy["zones"] != len(binding["zones"]):
        _reject("layoutPolicy.zones must match the source binding")
    main_originals = len(binding["households"]["entities"])
    if policy["mainOriginals"] != main_originals:
        _reject("layoutPolicy.mainOriginals must match the source binding")
    if policy["optionalOriginals"] != len(binding["entities"]) - main_originals:
        _reject("layoutPolicy.optionalOriginals must match the source binding")
    if presentation["preserveSourceScreens"] != len(dossier["screens"]):
        _reject("presentation.preserveSourceScreens must match the authored dossier")
    narrator_order = list((binding.get("narration") or {}).get("introOrder") or [])
    preserved = presentation["preserveNarratorOrder"]
    cursor = 0
    for screen in preserved:
        while cursor < len(narrator_order) and narrator_order[cursor] != screen:
            cursor += 1
        if cursor >= len(narrator_order):
            _reject(
                "presentation.preserveNarratorOrder must keep the authored "
                "narrator order"
            )
        cursor += 1
    for level in build_policy["difficulties"]:
        if level not in binding["difficulty"]:
            _reject(f"the source binding does not declare the {level} difficulty")
        if (
            binding["difficulty"][level]["startingResources"]
            != dossier["difficulty"][level]["startingResources"]
        ):
            _reject("the source binding stocks must match the authored profile")
    return {
        "plan": plan,
        "planPath": plan_path,
        "root": root,
        "mode": mode,
        "artifactScenarioId": artifact_scenario_id,
        "rasterPath": raster_path,
        "raster": raster,
        "bindingPath": binding_path,
        "binding": binding,
        "campaignPath": campaign_path,
        "campaign": campaign,
        "dossier": dossier,
        "frameSize": size,
        "bbox": bbox,
        "bands": bands,
        "corridors": corridors,
        "policy": policy,
        "presentation": presentation,
        "buildPolicy": build_policy,
        "evidence": evidence,
        "overrides": overrides,
    }


def require_output_outside_inputs(output, inputs):
    """Refuse an output directory that would hold a pinned source input.

    The build writes receipts, a report, a scenario and an XS file. It never
    writes into a directory that holds the pinned plan, binding, campaign or
    raster, so a build can never overwrite the source it was derived from.
    """
    resolved = Path(output).resolve()
    for path in inputs:
        target = Path(path).resolve()
        if target == resolved or target.is_relative_to(resolved):
            raise PrivatePreviewRejection(
                "the output directory must not hold a pinned source input: "
                + str(target)
            )
    return resolved


def derive_layout_evidence(binding, policy, *, conservative_extent=STORE_CONSERVATIVE_EXTENT):
    """Recompute the layout minima from the actual snapped positions.

    Nothing here is copied from the source binding's own evidence: the
    minima come from the derived positions, the native centres and the
    declared receiving approach.
    """
    centres = {
        entity["id"]: native_centre(entity["position"])
        for entity in binding["entities"]
    }
    zones = [
        (zone["id"], (float(zone["centre"][0]), float(zone["centre"][1])), float(zone["radius"]))
        for zone in binding["zones"]
    ]
    identifiers = [entity["id"] for entity in binding["entities"]]
    minimum_body = None
    for index, first in enumerate(identifiers):
        for second in identifiers[index + 1 :]:
            distance = math.dist(centres[first], centres[second])
            minimum_body = distance if minimum_body is None else min(minimum_body, distance)
    minimum_edge = None
    minimum_gap = None
    store_clearance = None
    store_id = None
    for entity in binding["entities"]:
        centre = centres[entity["id"]]
        for zone_id, zone_centre, radius in zones:
            clearance = math.dist(centre, zone_centre) - radius
            minimum_edge = clearance if minimum_edge is None else min(minimum_edge, clearance)
            if entity["player"] == 2 and entity["unitType"] == "house":
                beyond = clearance - policy["receiverApproachTiles"] - conservative_extent
                if store_clearance is None or beyond < store_clearance:
                    store_clearance = beyond
                    store_id = entity["id"]
    for index, (first_id, first_centre, first_radius) in enumerate(zones):
        for second_id, second_centre, second_radius in zones[index + 1 :]:
            gap = math.dist(first_centre, second_centre) - first_radius - second_radius
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
    main_originals = len(binding["households"]["entities"])
    return {
        "scope": (
            "recomputed geometric checks of the derived positions and their "
            "floor+0.5 native centres; not native pathfinding and not measured "
            "engine footprint data"
        ),
        "nativeSnappedEntities": {
            identifier: [centre[0], centre[1]] for identifier, centre in centres.items()
        },
        "minimumBodyCentreDistanceTiles": minimum_body,
        "minimumInitialCircleEdgeDistanceTiles": minimum_edge,
        "minimumReceivingCircleGapTiles": minimum_gap,
        "minimumStoreClearanceBeyondCirclePlus2ApproachPlus3ConservativeExtentTiles": store_clearance,
        "storeEntityId": store_id,
        "storeExtentClassification": (
            "deliberately conservative design exclusion radius, not measured "
            "engine footprint"
        ),
        "originalActorCount": len(binding["entities"]),
        "mainOriginalCount": main_originals,
        "optionalOriginalCount": len(binding["entities"]) - main_originals,
        "zoneCount": len(binding["zones"]),
        "sourceActorsAndZonesUnchanged": True,
    }


def verify_derived_binding(source_binding, derived, overrides):
    """Reject any change of the source binding the plan did not list."""
    if derived.get("kind") != SOURCE_BINDING_KIND:
        _reject("the derived binding is not a private household binding")
    if type(derived.get("schemaVersion")) is not int or derived["schemaVersion"] != 1:
        _reject("the derived binding has an unsupported schema version")
    moved = {override["id"]: override for override in overrides}
    source_entities = {entity["id"]: entity for entity in source_binding["entities"]}
    derived_entities = {entity["id"]: entity for entity in derived["entities"]}
    if set(source_entities) != set(derived_entities):
        _reject("the derived binding changed the original identities")
    if [entity["id"] for entity in source_binding["entities"]] != [
        entity["id"] for entity in derived["entities"]
    ]:
        _reject("the derived binding changed the original order")
    for identifier, source_entity in source_entities.items():
        derived_entity = derived_entities[identifier]
        for field in ("unitType", "player", "label", "representation", "initialHub"):
            if derived_entity.get(field) != source_entity.get(field):
                _reject(f"the derived binding changed {identifier}.{field}")
        if identifier in moved:
            override = moved[identifier]
            if tuple(derived_entity["position"]) != tuple(override["toPosition"]):
                _reject(f"the derived binding did not apply the listed move of {identifier}")
            for field in ("sourcePosition", "sourceOffsetTiles"):
                if field in source_entity and derived_entity.get(field) != source_entity.get(field):
                    _reject(f"the derived binding did not retain {identifier}.{field}")
        elif derived_entity["position"] != source_entity["position"]:
            _reject(f"the derived binding moved {identifier} without a listed override")
    source_zones = {zone["id"]: zone for zone in source_binding["zones"]}
    derived_zones = {zone["id"]: zone for zone in derived["zones"]}
    if set(source_zones) != set(derived_zones):
        _reject("the derived binding changed the zone identities")
    for identifier, source_zone in source_zones.items():
        derived_zone = derived_zones[identifier]
        if derived_zone.get("centre") != source_zone.get("centre"):
            _reject(f"the derived binding moved the zone {identifier}")
        if derived_zone.get("radius") != source_zone.get("radius"):
            _reject(f"the derived binding changed the radius of {identifier}")
        if derived_zone.get("label") != source_zone.get("label"):
            _reject(f"the derived binding changed the label of {identifier}")
    for field in ("households", "optionalPayments", "narration", "difficulty", "accountPolicy"):
        if derived.get(field) != source_binding.get(field):
            _reject(f"the derived binding changed {field}")
    return True
