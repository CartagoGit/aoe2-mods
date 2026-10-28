# Yavneh modern surface reference

This is a modern Copernicus GLO-30 digital surface model (DSM) crop around the candidate 400 × 400 frame in the pinned Yavneh world plan. It is a geographic visualization aid only. The DSM records the modern reflective surface, including roofs, infrastructure and vegetation; it is not bare-earth terrain, a reconstruction of Yavneh in 70–80 CE, an archaeological parcel plan, evidence for ancient roads, or approval of a game map. The 22 plotted locations remain fictional activity-site candidates.

The source object is the public one-degree N31/E034 COG tile: [download GeoTIFF](https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N31_00_E034_00_DEM/Copernicus_DSM_COG_10_N31_00_E034_00_DEM.tif). Its downloaded bytes are 28,960,707 and SHA-256 is `d157903d3c8adb88598def6c1e40f938ecf7a366a598aa000fe45de250ea756a`. The object reports last modified 9 May 2022 and ETag `0283b64c92086b1f44dee16f03f0b5a8`; the ETag is recorded as object metadata, not used as a cryptographic checksum.

Copernicus describes GLO-30 as a DSM that includes buildings and vegetation and documents GLO-30 DGED as geographic EPSG:4326, float32, RasterPixelIsPoint with elevations referenced to EGM2008. The source TIFF itself exposes EPSG:4326 and `AREA_OR_POINT=Point`, but no vertical datum tag. Copernicus documents TanDEM-X collection during 2011–2015 and notes that older elevation models may fill local data gaps; this is modern surface data, not a historical model. The public AWS mirror describes COG tiles on a one-degree grid and links the product licence. Sources: [Copernicus DEM product and technical specifications](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM), [AWS Open Data Registry entry](https://registry.opendata.aws/copernicus-dem/), [AWS mirror readme](https://copernicus-dem-30m.s3.amazonaws.com/readme.html), and [Copernicus WorldDEM-30 licence (PDF)](https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf). The local [licence notice](../../../research/odyssey-research/geography/jerusalem-modern-dsm-license.md) records the source, modification, liability, no-endorsement and downstream obligations that apply here.

## Frame and extraction

The source-control plan is [02-yavneh-world-plan.json](../../../design/episode-plans/jewish-tradition/02-yavneh-world-plan.json), SHA-256 `388e2d27b707b35d73a07423c415653e02482a2620ea208ce4ee05cc03942046`. Its authored bbox is `[34.714, 31.846, 34.755, 31.884]` in west, south, east, north order. Using the existing `tools/map/geographic_frame.helper.py::make_frame` at size 400 gives sample-centre extent `[34.70944390442437, 31.84372, 34.759556095575626, 31.886280000000003]`; the full padded sample-cell bounds are `[34.70938110719235, 31.843666666666667, 34.759618892807644, 31.886333333333337]`. The N31/E034 source tile fully encloses that padded extent.

The TIFF is a pixel-aligned integer-window crop at source columns 2554–2735 and rows 409–563 (182 × 155 samples; 28,210 values). It preserves float32 values, EPSG:4326, `AREA_OR_POINT=Point`, no-data value, and affine transform. Reopening the crop reproduced every value in the source window exactly. All 160,000 geographic sample locations of the 400 × 400 design frame were also checked against the source and reopened crop; all fell inside the crop and matched the same source pixel values. Processing consisted only of the integer window crop and lossless DEFLATE re-encoding: no reprojection, resampling, smoothing, filling, interpolation or terrain derivation.

The crop outer-cell bounds are `[34.70930555555555, 31.843472222222225, 34.75986111111111, 31.88652777777778]`, enclosing all padded frame cells. Crop size is 91,728 bytes; SHA-256 `de5b1ce5fb99e23a5f5b843bdd3cadea6303f208cc623e3089a60c005f588d3f`. The preview uses a YlOrBr palette, north-up orientation, cosine-corrected geographic aspect and P2–P98 display stretch; those display choices do not alter raster values. It shows the authored bbox, padded-cell outline and 22 fictional candidate markers. Preview size is 251,246 bytes; SHA-256 `f498aa50b3308c8c5c665852f31281618cb07cb74608097906b78ccd2b6e9010`.

## Required notices

Source notice:

> © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved.

Modified-data notice:

> produced using Copernicus WorldDEM-30 © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved.

Liability notice:

> The organisations in charge of the Copernicus programme by law or by delegation do not incur any liability for any use of the Copernicus WorldDEM-30.

No official endorsement by the provider, licensor or Copernicus programme is implied. Any later distribution or communication must preserve applicable licence obligations and notices. No route, native-terrain, historical, production or game approval is made here; no new research-manifest resource is registered.
