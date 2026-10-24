# Independent review: Hijaz DSM research references

Reviewer: gpt-6-luna  
Reviewed delivery: `f1ab2c82e92a192a164935b22e311a25aa54ef89`  
Base: `4c5ae8485577313ed3541de2e75136982f28eb12`  
Review date: 2026-10-24

This is a bounded review of the source contrast and four modern DSM extracts/previews in d00002/S7. It is not a whole-slice verdict, historical approval, native-map approval, or game verification.

## Findings

No blocking data-integrity defect was found in the reviewed extracts. The three retained source-tile downloads matched the recorded byte counts and SHA-256 hashes. The four TIFF crop hashes, byte counts, and dimensions match the processing record. I independently compared every crop sample with its declared source window using Pillow and libtiff readers; all four comparisons were exact. GeoTIFF tags agree with the declared EPSG:4326, Float32, 1/3600-degree spacing, and PixelIsPoint interpretation. Crop tiepoints match their source-window offsets, and each crop's outer-cell bounds enclose the declared padded map bounds. No crop was resampled or reprojected in the reviewed files.

The manifest has 47 assets on this delivery. All 39 entries from the base manifest remain unchanged and in order; the eight appended entries correspond to the four TIFF crops and four PNG previews. Each new entry records `productionApproved: false`. The canonical geography registry and `first-caliphs.json` are unchanged in the delivery. The four proposed frames remain identified as architect-selected exploratory bounds, not published historical bounds or promoted profiles; the stated count of 22 missing profiles is preserved.

The official Copernicus AWS readme describes GLO-30 as a DSM that includes buildings, infrastructure, and vegetation, and documents the COG edge-row/column trimming relevant to these tiles ([readme](https://copernicus-dem-30m.s3.amazonaws.com/readme.html)). The Copernicus product page identifies the DSM and its acquisition period (2011–2015), and lists EGM2008 vertical reference, metre units, and PixelIsPoint alignment for DGED ([product documentation](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM)). The linked GLO-30 licence permits reproduction, distribution, communication, and adaptation while requiring source, modified-data, liability, and non-endorsement notices ([licence, Articles 4 and 6](https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf)). The local notice contains those statements and the preview manifest entries point to it.

The four preview plots show height-only grayscale, WGS84 longitude/latitude axes, a north arrow, and a dashed candidate frame. They do not depict ancient paths, camps, water, or playable terrain. At original resolution, all four PNGs have identical header and footer pixel regions, including the warning that each is not an ancient battlefield or playable map and the modified-data attribution/liability text. The earlier apparent difference came from the viewer's cropped preview; it is withdrawn and is not a finding against the assets.

The consultation record carefully bounds the historical sources. Saudipedia's Badr page reports 623, which the collection flags as a source anomaly rather than using to overwrite the canonical date. TDV's Hudaybiyya entry supplies bounded geographic/date context, not a surveyed coordinate. The Nusuk location links expose modern visitor-marker coordinates in URL strings; the linked Google Maps views could not be opened in the browser session, so this review confirms the copied coordinate strings and lat/lon normalization only, not the mapped feature or imagery. The five markers remain explicitly modern administrative/visitor references. The source text's confessional claims and reported speech are not treated here as neutral narration.

## Validation scope

I checked file hashes, source byte counts, TIFF dimensions/tags, source-window pixel equality with two independent decoders, preview hashes/orientation and matching header/footer regions, padded-bound coverage, the manifest's unchanged 39-entry prefix, and the referenced official product/licence pages. `bun run validate` passed on this review worktree: TypeScript/Biome checks, 142 tests with 2,069 expectations, documentation and local-link checks, and validation of one campaign. Static inspection and these automated checks do not prove ancient geography, archaeological identification, terrain passability, native map correctness, or gameplay.

The formal DelendAI review queue was empty at the time this report was prepared; no formal S7 review or approval is claimed here.

## Correction to the visual check

On 2026-10-24, a follow-up full-resolution check compared the 0–89 and 1000–1183 row bands of all four PNGs with Pillow. Header and footer arrays are byte-for-byte identical across the four files. This supersedes the initial scaled-view observation above, which was caused by the viewer cropping the images.
