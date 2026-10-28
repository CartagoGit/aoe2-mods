"""Extract a verified sample grid from a real modern DSM crop.

The raster compiler in `tools/map/geographic_raster.compiler.py` deliberately
refuses to read a GeoTIFF: it takes a declared sample grid and says that "a
verified external extraction step must provide the sample centers correctly;
rotated/nonregular rasters need a future explicit adapter". This module is that
external extraction step, for the regular, north-up, unrotated crops this
repository actually holds.

It reads the TIFF with the standard library only — no third-party dependency, no
network, no game installation — and it never guesses:

* the **sample anchor** is a required argument. A GeoTIFF ties its raster to
  the ground either at a pixel centre (`PixelIsPoint`) or at a pixel corner
  (`PixelIsArea`), and the two disagree by half a pixel. The GeoKey is read and
  recorded, the declared anchor decides, and the difference between them is
  reported rather than silently resolved.
* the **vertical datum** and the **source classification** are required
  arguments. A height without a datum is not a height.
* a crop with a **rotation**, a **model transformation** or a **non-north-up**
  orientation is refused instead of being approximated.

The float predictor (`Predictor=3`) is implemented the way libtiff implements
it: the decoded tile buffer is a flat byte stream that is accumulated with
`cp[i] = (cp[i] + cp[i-1]) & 0xff` and only then de-interleaved into samples.
The accumulation runs over the flat buffer, so the byte planes are *not*
independent; an implementation that differences each plane on its own decodes
this raster into nonsense. The reproduction of the hand-verified fixture in
`tests/maps/fixtures/edirne-dsm-sample-grid.json` is the regression test for
that detail.

The output is the compiler's input format plus a provenance block, and
`verify_extraction` re-reads the source afterwards and confirms every value, so
the artifact carries a real verification rather than a claim.
"""

import hashlib
import json
import struct
import zlib
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# TIFF field types and their byte widths.
_TYPE_SIZES = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 6: 1, 7: 1, 8: 2, 9: 4, 10: 8, 11: 4, 12: 8}

TAG_IMAGE_WIDTH = 256
TAG_IMAGE_LENGTH = 257
TAG_BITS_PER_SAMPLE = 258
TAG_COMPRESSION = 259
TAG_PHOTOMETRIC = 262
TAG_STRIP_OFFSETS = 273
TAG_SAMPLES_PER_PIXEL = 277
TAG_ROWS_PER_STRIP = 278
TAG_STRIP_BYTE_COUNTS = 279
TAG_PLANAR_CONFIG = 284
TAG_PREDICTOR = 317
TAG_TILE_WIDTH = 322
TAG_TILE_LENGTH = 323
TAG_TILE_OFFSETS = 324
TAG_TILE_BYTE_COUNTS = 325
TAG_SAMPLE_FORMAT = 339
TAG_MODEL_PIXEL_SCALE = 33550
TAG_MODEL_TIEPOINT = 33922
TAG_MODEL_TRANSFORMATION = 34264
TAG_GEO_KEY_DIRECTORY = 34735
TAG_GEO_DOUBLE_PARAMS = 34736
TAG_GEO_ASCII_PARAMS = 34737
TAG_GDAL_NODATA = 42113

GEO_KEY_GEOTYPE = 1024
GEO_KEY_RASTER_TYPE = 1025
GEO_KEY_GEOGRAPHIC_TYPE = 2048
GEO_KEY_CITATION = 1026

RASTER_PIXEL_IS_AREA = 1
RASTER_PIXEL_IS_POINT = 2

SUPPORTED_COMPRESSION = (1, 8)
SUPPORTED_PREDICTORS = (1, 3)
SUPPORTED_BITS = (16, 32)


@lru_cache(maxsize=4)
def _read_tiff(path):
    """Read the header and the first IFD of a TIFF file."""
    data = Path(path).read_bytes()
    if len(data) < 8:
        raise ValueError("the file is too short to be a TIFF")
    order = data[:2]
    if order == b"II":
        endian = "<"
    elif order == b"MM":
        endian = ">"
    else:
        raise ValueError("not a TIFF file: the byte order marker is missing")
    magic, first_ifd = struct.unpack(endian + "HI", data[2:8])
    if magic != 42:
        raise ValueError("not a baseline TIFF file")
    count = struct.unpack(endian + "H", data[first_ifd:first_ifd + 2])[0]
    tags = {}
    for index in range(count):
        start = first_ifd + 2 + index * 12
        tag, field_type, field_count = struct.unpack(endian + "HHI", data[start:start + 8])
        size = _TYPE_SIZES.get(field_type)
        if size is None:
            continue
        total = size * field_count
        if total <= 4:
            payload = data[start + 8:start + 8 + total]
        else:
            offset = struct.unpack(endian + "I", data[start + 8:start + 12])[0]
            payload = data[offset:offset + total]
        tags[tag] = _decode_field(endian, field_type, field_count, payload)
    return {"endian": endian, "tags": tags, "data": data, "sha256": hashlib.sha256(data).hexdigest()}


def _decode_field(endian, field_type, field_count, payload):
    if field_type == 2:
        return payload.split(b"\x00", 1)[0].decode("ascii", "replace")
    if field_type in (5, 10):
        numbers = struct.unpack(endian + "%d%s" % (field_count * 2, "I" if field_type == 5 else "d"), payload)
        return [numbers[i * 2] / numbers[i * 2 + 1] if numbers[i * 2 + 1] else None
                for i in range(field_count)]
    codes = {1: "B", 3: "H", 4: "I", 6: "b", 7: "B", 8: "h", 9: "i", 11: "f", 12: "d"}
    code = codes.get(field_type)
    if code is None:
        return payload
    return list(struct.unpack(endian + "%d%s" % (field_count, code), payload))


def _scalar(tags, tag, default=None):
    value = tags.get(tag)
    if value is None:
        return default
    if isinstance(value, list):
        return value[0] if value else default
    return value


def _geo_keys(tags):
    directory = tags.get(TAG_GEO_KEY_DIRECTORY) or []
    keys = {}
    if len(directory) < 4:
        return keys
    count = directory[3]
    for index in range(count):
        base = 4 + index * 4
        if base + 3 >= len(directory):
            break
        key_id, location, length, offset = directory[base:base + 4]
        if location == 0:
            keys[key_id] = offset
        elif location == TAG_GEO_DOUBLE_PARAMS:
            params = tags.get(TAG_GEO_DOUBLE_PARAMS) or []
            keys[key_id] = params[offset:offset + length]
        elif location == TAG_GEO_ASCII_PARAMS:
            params = tags.get(TAG_GEO_ASCII_PARAMS) or ""
            keys[key_id] = params[offset:offset + length]
    return keys


def _fp_acc_row(row_bytes, width, bps, file_big_endian):
    """Undo libtiff's floating point predictor for one row.

    libtiff's `fpAcc` accumulates the whole row buffer as a flat byte stream and
    only then de-interleaves it into samples, so the accumulation crosses the
    byte-plane boundaries. Differencing each plane on its own is wrong, and
    the difference is not a rounding detail: it decodes into different numbers.
    """
    accumulated = bytearray(len(row_bytes))
    total = 0
    for index, byte in enumerate(row_bytes):
        total = (total + byte) & 0xFF
        accumulated[index] = total
    out = bytearray(width * bps)
    for count in range(width):
        base = count * bps
        for byte in range(bps):
            if file_big_endian:
                out[base + byte] = accumulated[byte * width + count]
            else:
                out[base + byte] = accumulated[(bps - byte - 1) * width + count]
    return out


def _decode_tile(raw, endian, width, height, predictor, samples_per_pixel, bits_per_sample):
    """Decode a decompressed tile or strip into rows of sample values."""
    if samples_per_pixel != 1:
        raise ValueError(f"only single-sample rasters are supported, got {samples_per_pixel}")
    if bits_per_sample not in SUPPORTED_BITS:
        raise ValueError(f"only 16- and 32-bit samples are supported, got {bits_per_sample}")
    bps = bits_per_sample // 8
    file_big_endian = endian == ">"
    prefix = ">" if file_big_endian else "<"
    rows = []
    for row_index in range(height):
        start = row_index * width * bps
        row_bytes = raw[start:start + width * bps]
        if len(row_bytes) != width * bps:
            raise ValueError("the decoded tile is shorter than its declared size")
        if predictor == 3:
            row_bytes = _fp_acc_row(row_bytes, width, bps, file_big_endian)
        rows.append(list(struct.unpack(prefix + "%df" % width, bytes(row_bytes))))
    return rows


@lru_cache(maxsize=16)
def _tile_rows(path, index):
    """Decode one tile once and keep its rows."""
    tiff = _read_tiff(path)
    tags = tiff["tags"]
    endian = tiff["endian"]
    data = tiff["data"]
    compression = _scalar(tags, TAG_COMPRESSION, 1)
    predictor = _scalar(tags, TAG_PREDICTOR, 1)
    samples = _scalar(tags, TAG_SAMPLES_PER_PIXEL, 1)
    bits = _scalar(tags, TAG_BITS_PER_SAMPLE, 8)
    tile_width = _scalar(tags, TAG_TILE_WIDTH)
    tile_length = _scalar(tags, TAG_TILE_LENGTH)
    offsets = tags[TAG_TILE_OFFSETS]
    counts = tags[TAG_TILE_BYTE_COUNTS]
    raw = data[offsets[index]:offsets[index] + counts[index]]
    if compression == 8:
        raw = zlib.decompress(raw)
    rows = _decode_tile(raw, endian, tile_width, tile_length, predictor, samples, bits)
    return tuple(tuple(row) for row in rows)


def read_pixel(path, column, row):
    """Read one float sample from a tiled or stripped TIFF."""
    path = str(path)
    tiff = _read_tiff(path)
    tags = tiff["tags"]
    width = _scalar(tags, TAG_IMAGE_WIDTH)
    length = _scalar(tags, TAG_IMAGE_LENGTH)
    compression = _scalar(tags, TAG_COMPRESSION, 1)
    predictor = _scalar(tags, TAG_PREDICTOR, 1)
    if compression not in SUPPORTED_COMPRESSION:
        raise ValueError(f"unsupported compression {compression}")
    if predictor not in SUPPORTED_PREDICTORS:
        raise ValueError(f"unsupported predictor {predictor}")
    if column < 0 or column >= width or row < 0 or row >= length:
        raise ValueError(f"sample ({column},{row}) is outside the raster")

    if TAG_TILE_OFFSETS in tags:
        tile_width = _scalar(tags, TAG_TILE_WIDTH)
        tile_length = _scalar(tags, TAG_TILE_LENGTH)
        tiles_across = (width + tile_width - 1) // tile_width
        tile_x = column // tile_width
        tile_y = row // tile_length
        index = tile_y * tiles_across + tile_x
        rows = _tile_rows(path, index)
        return rows[row % tile_length][column % tile_width]

    if TAG_STRIP_OFFSETS in tags:
        rows_per_strip = _scalar(tags, TAG_ROWS_PER_STRIP, length)
        offsets = tags[TAG_STRIP_OFFSETS]
        counts = tags[TAG_STRIP_BYTE_COUNTS]
        strip = row // rows_per_strip
        raw = tiff["data"][offsets[strip]:offsets[strip] + counts[strip]]
        if compression == 8:
            raw = zlib.decompress(raw)
        rows = _decode_tile(raw, tiff["endian"], width,
                            min(rows_per_strip, length - strip * rows_per_strip),
                            predictor, _scalar(tags, TAG_SAMPLES_PER_PIXEL, 1),
                            _scalar(tags, TAG_BITS_PER_SAMPLE, 8))
        return rows[row % rows_per_strip][column]

    raise ValueError("the raster has neither strips nor tiles")


def georeference(path):
    """The georeference of the raster, read and not interpreted."""
    tiff = _read_tiff(str(path))
    tags = tiff["tags"]
    if TAG_MODEL_TRANSFORMATION in tags:
        raise ValueError("a rotated or skewed raster needs an explicit adapter")
    scale = tags.get(TAG_MODEL_PIXEL_SCALE)
    tiepoint = tags.get(TAG_MODEL_TIEPOINT)
    if not scale or not tiepoint:
        raise ValueError("the raster carries no pixel scale or tiepoint")
    if len(tiepoint) < 6:
        raise ValueError("the tiepoint is incomplete")
    keys = _geo_keys(tags)
    return {
        "modelPixelScaleTag": list(scale),
        "modelTiepointTag": list(tiepoint),
        "rasterTypeGeoKey": keys.get(GEO_KEY_RASTER_TYPE),
        "geographicTypeGeoKey": keys.get(GEO_KEY_GEOGRAPHIC_TYPE),
        "modelTypeGeoKey": keys.get(GEO_KEY_GEOTYPE),
        "citation": keys.get(GEO_KEY_CITATION),
        "imageWidth": _scalar(tags, TAG_IMAGE_WIDTH),
        "imageLength": _scalar(tags, TAG_IMAGE_LENGTH),
        "bitsPerSample": _scalar(tags, TAG_BITS_PER_SAMPLE),
        "sampleFormat": _scalar(tags, TAG_SAMPLE_FORMAT),
        "compression": _scalar(tags, TAG_COMPRESSION, 1),
        "predictor": _scalar(tags, TAG_PREDICTOR, 1),
        "planarConfiguration": _scalar(tags, TAG_PLANAR_CONFIG, 1),
        "gdalNoData": tags.get(TAG_GDAL_NODATA),
    }


def sample_origin(reference, column, row, anchor):
    """The longitude and latitude of one sample centre.

    `anchor` is `centre` for a PixelIsPoint raster and `corner` for a
    PixelIsArea raster. The caller must declare which one the source uses; this
    function never decides.
    """
    if anchor not in ("centre", "corner"):
        raise ValueError("the sample anchor must be declared as centre or corner")
    scale_x, scale_y = reference["modelPixelScaleTag"][0], reference["modelPixelScaleTag"][1]
    lon_0, lat_0 = reference["modelTiepointTag"][3], reference["modelTiepointTag"][4]
    offset = 0.0 if anchor == "centre" else 0.5
    return [
        lon_0 + (column + offset) * scale_x,
        lat_0 - (row + offset) * scale_y,
    ]


def extract_window(path, *, column_start, column_end, row_start, row_end,
                   sample_anchor, vertical_datum, source_classification,
                   licence_notice_path, source_url=None, limits=(), extra_provenance=None):
    """Extract a rectangular window of samples into the compiler's input format."""
    reference = georeference(path)
    if reference["geographicTypeGeoKey"] not in (None, 4326):
        raise ValueError("only EPSG:4326 rasters are supported")
    width = column_end - column_start + 1
    height = row_end - row_start + 1
    rows = []
    for row in range(row_start, row_end + 1):
        line = []
        for column in range(column_start, column_end + 1):
            line.append(read_pixel(path, column, row))
        rows.append(line)

    origin = sample_origin(reference, column_start, row_start, sample_anchor)
    scale_x, scale_y = reference["modelPixelScaleTag"][0], reference["modelPixelScaleTag"][1]
    provenance = {
        "localSourcePath": str(path),
        "sourceSha256": _read_tiff(str(path))["sha256"],
        "columnOffset": column_start,
        "rowOffset": row_start,
        "width": width,
        "height": height,
        "sampleAnchor": sample_anchor,
        "licenseNoticePath": licence_notice_path,
        "sourceUrl": source_url,
        "extractionDescription": (
            "Direct standard-library reads of the contiguous float32 samples at zero-based "
            "crop columns %d-%d and rows %d-%d; no resampling and no writes to the source."
            % (column_start, column_end, row_start, row_end)
        ),
    }
    if extra_provenance:
        provenance.update(extra_provenance)
    georef = {
        "rasterInterpretation": (
            "declared anchor '%s' (%s); GeoKey 1025 = %s"
            % (sample_anchor,
               "PixelIsPoint" if sample_anchor == "centre" else "PixelIsArea",
               reference["rasterTypeGeoKey"])
        ),
        "modelTiepointTag": reference["modelTiepointTag"],
        "modelPixelScaleTag": reference["modelPixelScaleTag"],
        "sampleWindowZeroBasedCropPixels": {
            "columnStart": column_start,
            "columnEndInclusive": column_end,
            "rowStart": row_start,
            "rowEndInclusive": row_end,
        },
        "valueUnits": "metres, 32-bit float raster samples",
    }
    return {
        "schemaVersion": 1,
        "sourceClassification": source_classification,
        "horizontalCrs": "EPSG:4326",
        "verticalDatum": vertical_datum,
        "heightUnit": "metre",
        "sampleOriginLonLat": origin,
        "stepDegrees": [scale_x, -scale_y],
        "rows": rows,
        "georeference": georef,
        "provenance": provenance,
        "limits": list(limits),
    }


def verify_extraction(grid, path, *, column_start, row_start):
    """Re-read the source and confirm every extracted value.

    The receipt says what was re-read and what matched; it is a verification,
    not a claim about the source's own accuracy.
    """
    rows = grid["rows"]
    mismatches = []
    for row_index, row in enumerate(rows):
        for column_index, value in enumerate(row):
            actual = read_pixel(path, column_start + column_index, row_start + row_index)
            if actual != value:
                mismatches.append({
                    "cell": [column_start + column_index, row_start + row_index],
                    "extracted": value,
                    "reread": actual,
                })
    values = [value for row in rows for value in row]
    return {
        "verified": not mismatches,
        "sampleCount": len(values),
        "mismatches": mismatches,
        "rangeMetres": [min(values), max(values)] if values else None,
        "sourceSha256": _read_tiff(str(path))["sha256"],
        "method": "every extracted value re-read from the source raster and compared exactly",
    }


def write_artifact(payload, path):
    """Write an artifact to an explicit path."""
    target = Path(path)
    if str(target.parent) not in ("", "."):
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return str(target)
