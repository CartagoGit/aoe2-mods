"""Resample explicitly georeferenced metre samples; never infer game terrain."""

import hashlib
import json
import math
import runpy
from pathlib import Path

FRAME = runpy.run_path(str(Path(__file__).with_name("geographic_frame.helper.py")))


def finite_number(value):
    return type(value) in (int, float) and math.isfinite(value)


def validate_source(source):
    if type(source.get("schemaVersion")) is not int or source["schemaVersion"] != 1 or source.get("horizontalCrs") != "EPSG:4326":
        raise ValueError("Only internal version-1 EPSG:4326 sample grids are supported")
    if source.get("sourceClassification") not in ("modern-dem", "modern-dsm", "synthetic-test"):
        raise ValueError("Explicit modern/synthetic source classification is required")
    if source.get("heightUnit") != "metre":
        raise ValueError("Source heights must explicitly declare metre units; no implicit conversion")
    if not isinstance(source.get("verticalDatum"), str) or not source["verticalDatum"].strip():
        raise ValueError("Metre heights require an explicit vertical datum")
    origin, step = source.get("sampleOriginLonLat"), source.get("stepDegrees")
    if not isinstance(origin, list) or len(origin) != 2 or not all(map(finite_number, origin)):
        raise ValueError("A sample-center origin is required")
    if not isinstance(step, list) or len(step) != 2 or not all(map(finite_number, step)) or not step[0] > 0 > step[1]:
        raise ValueError("Only regular north-up grids with positive longitude and negative latitude steps are supported")
    rows = source.get("rows")
    if not isinstance(rows, list) or len(rows) < 2 or not isinstance(rows[0], list) or len(rows[0]) < 2:
        raise ValueError("At least two rows and columns of samples are required")
    width = len(rows[0])
    if any(not isinstance(row, list) or len(row) != width or any(
        value is not None and not finite_number(value) for value in row
    ) for row in rows):
        raise ValueError("Rectangular rows must contain finite metre values or explicit null nodata")
    east = origin[0] + (width - 1) * step[0]
    south = origin[1] + (len(rows) - 1) * step[1]
    if not (-180 <= origin[0] < east <= 180 and -90 <= south < origin[1] <= 90):
        raise ValueError("Source sample centers leave WGS84 bounds")


def sample_bilinear(source, lon_lat):
    x = (lon_lat[0] - source["sampleOriginLonLat"][0]) / source["stepDegrees"][0]
    y = (lon_lat[1] - source["sampleOriginLonLat"][1]) / source["stepDegrees"][1]
    height, width = len(source["rows"]), len(source["rows"][0])
    # Only absorb floating-point noise, not missing geographic coverage.
    tolerance = 1e-7
    if x < -tolerance or y < -tolerance or x > width - 1 + tolerance or y > height - 1 + tolerance:
        return None, "outside-source-sample-centers"
    x, y = min(max(x, 0), width - 1), min(max(y, 0), height - 1)
    left, top = math.floor(x), math.floor(y)
    right, bottom = min(left + 1, width - 1), min(top + 1, height - 1)
    fx, fy = x - left, y - top
    value = 0.0
    for column, row, weight in ((left, top, (1 - fx) * (1 - fy)),
                                (right, top, fx * (1 - fy)),
                                (left, bottom, (1 - fx) * fy), (right, bottom, fx * fy)):
        if weight == 0:
            continue
        sample = source["rows"][row][column]
        if sample is None:
            return None, "source-nodata"
        value += sample * weight
    return round(value, 6), None


def compile_height_candidate(source, bbox, size, allow_incomplete=False):
    validate_source(source)
    frame = FRAME["make_frame"](bbox, size)
    rows, missing = [], {}
    for y in range(size):
        row = []
        for x in range(size):
            value, reason = sample_bilinear(source, frame.lon_lat_at(x, y))
            row.append(value)
            if reason:
                missing[reason] = missing.get(reason, 0) + 1
        rows.append(row)
    if missing and not allow_incomplete:
        raise ValueError(f"Incomplete sample coverage; no fill/extrapolation allowed: {missing}")
    values = [value for row in rows for value in row if value is not None]
    return {"schemaVersion": 1, "kind": "geographic-height-raster-candidate",
            "status": "research candidate; no historical, native terrain, navigation or game approval",
            "sourceClassification": source["sourceClassification"], "horizontalCrs": "EPSG:4326",
            "verticalDatum": source["verticalDatum"], "heightUnit": "metre", "mapSize": size,
            "requestedBBox": list(bbox), "paddedSampleCenterBounds": frame.bounds_at(0, size - 1),
            "outerCellBounds": frame.bounds_at(-0.5, size - 0.5),
            "orientation": "north-up, x eastward, y southward; native AoE2 camera/orientation calibration pending",
            "projection": "existing cosine-corrected design projection, 1.12 square padding, integer 0..size-1 sample centers",
            "resampling": "bilinear on source sample centers, rounded to 6 decimals; no nodata fill or geographic extrapolation",
            "completeSampleCoverage": not bool(missing), "missingSamples": missing,
            "rangeMetres": [min(values), max(values)] if values else None,
            "sourceGridSemanticSha256": hashlib.sha256(json.dumps(source, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest(),
            "reportedSourceProvenance": source.get("provenance", {}),
            "localSourceHashVerified": False, "sourceSampleExtractionVerified": False, "nativeTerrainWritten": False, "gameVerified": False,
            "passabilityStatus": "unassessed; heights are not a water, building, cliff or navigation mask",
            "historicalStatus": "unassessed; modern DSM may contain buildings and vegetation; no ancient surface inferred",
            "elevationRowsMetres": rows}
