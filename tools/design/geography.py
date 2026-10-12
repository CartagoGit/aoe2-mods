"""Geographic controls for design documents; never a native scenario generator."""
from math import cos, radians


def tile_point(bbox, lon_lat, size):
    west, south, east, north = bbox
    latitude = (south + north) / 2
    longitude_factor = cos(radians(latitude))
    span = max((east - west) * longitude_factor, north - south) * 1.12
    x = ((lon_lat[0] - (west + east) / 2) * longitude_factor / span + .5)
    y = (.5 - (lon_lat[1] - latitude) / span)
    return [round(x * (size - 1), 2), round(y * (size - 1), 2)]


def clip_segment(a, b, bbox):
    """Liang–Barsky clipping, keeping intersection points rather than dropping vertices."""
    xmin, ymin, xmax, ymax = bbox
    dx, dy = b[0] - a[0], b[1] - a[1]
    lower, upper = 0.0, 1.0
    for direction, distance in zip((-dx, dx, -dy, dy),
                                   (a[0] - xmin, xmax - a[0], a[1] - ymin, ymax - a[1])):
        if direction == 0:
            if distance < 0:
                return None
            continue
        ratio = distance / direction
        if direction < 0:
            lower = max(lower, ratio)
        else:
            upper = min(upper, ratio)
        if lower > upper:
            return None
    return [[round(a[0] + lower * dx, 6), round(a[1] + lower * dy, 6)],
            [round(a[0] + upper * dx, 6), round(a[1] + upper * dy, 6)]]


def geometry_lines(geometry):
    if geometry['type'] == 'LineString':
        return [geometry['coordinates']]
    if geometry['type'] == 'MultiLineString':
        return geometry['coordinates']
    return []
