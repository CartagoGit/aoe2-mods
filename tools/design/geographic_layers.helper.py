"""Clip real vector controls without interpreting them as ancient terrain."""

from geography import clip_segment, geometry_lines, tile_point


def index_layer(layer):
    lines = []
    for feature in layer["features"]:
        for coordinates in geometry_lines(feature["geometry"]):
            if len(coordinates) < 2:
                continue
            longitudes, latitudes = zip(*coordinates)
            lines.append(
                (
                    (min(longitudes), min(latitudes), max(longitudes), max(latitudes)),
                    coordinates,
                )
            )
    return lines


def clipped_tile_segments(indexed_lines, bbox, size, *, clip_bbox=None):
    """Clip to an explicit viewport while retaining the original projection.

    Existing callers keep their original rectangle/rounding. A wider clipping
    envelope must not also become a wider projection and move existing points.
    """
    result = []
    viewport = bbox if clip_bbox is None else clip_bbox
    west, south, east, north = viewport
    for bounds, coordinates in indexed_lines:
        if (
            bounds[2] < west
            or bounds[0] > east
            or bounds[3] < south
            or bounds[1] > north
        ):
            continue
        for a, b in zip(coordinates, coordinates[1:]):
            clipped = clip_segment(a, b, viewport, precision=6 if clip_bbox is None else None)
            if clipped:
                result.append([tile_point(bbox, point, size) for point in clipped])
    return result
