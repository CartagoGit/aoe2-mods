"""Extend the existing design projection with inverse sampling and cell bounds."""

import math
import runpy
from pathlib import Path
from typing import NamedTuple

# Keep the established forward projection; no second forward implementation.
LEGACY = runpy.run_path(str(Path(__file__).resolve().parents[1] / "design" / "geography.py"))


class GeographicFrame(NamedTuple):
    bbox: tuple
    size: int
    centre_lon: float
    centre_lat: float
    longitude_factor: float
    span_degrees: float

    def lon_lat_at(self, x, y):
        return [self.centre_lon + (x / (self.size - 1) - 0.5) * self.span_degrees / self.longitude_factor,
                self.centre_lat + (0.5 - y / (self.size - 1)) * self.span_degrees]

    def tile_at(self, lon_lat):
        return LEGACY["tile_point"](self.bbox, lon_lat, self.size)

    def bounds_at(self, lower, upper):
        west, north = self.lon_lat_at(lower, lower)
        east, south = self.lon_lat_at(upper, upper)
        return [west, south, east, north]


def make_frame(bbox, size):
    if type(size) is not int or not 300 <= size <= 400:
        raise ValueError("Map candidate size must be an integer from 300 to 400")
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4 or not all(
        type(value) in (int, float) and math.isfinite(value) for value in bbox
    ):
        raise ValueError("Frame needs four finite WGS84 bounds")
    west, south, east, north = bbox
    if not (-180 <= west < east <= 180 and -85 <= south < north <= 85):
        raise ValueError("Unsupported bounds: no polar or antimeridian frame")
    latitude = (south + north) / 2
    longitude_factor = math.cos(math.radians(latitude))
    span = max((east - west) * longitude_factor, north - south) * 1.12
    frame = GeographicFrame(tuple(bbox), size, (west + east) / 2, latitude, longitude_factor, span)
    bounds = frame.bounds_at(-0.5, size - 0.5)
    if bounds[0] < -180 or bounds[2] > 180 or bounds[1] < -90 or bounds[3] > 90:
        raise ValueError("Padded cells leave WGS84 bounds")
    return frame
