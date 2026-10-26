# Geographic map preparation

`i00003/S2` is in progress, not complete. This first implementation produces an internal grid of metre heights from explicitly georeferenced samples. It implements no AoE2 terrain, water, walls, bridges, footprints, native transport, navigation or gameplay verification. The public campaign schema and composed capability profile retain their existing versions and native rejection gates.

## Data flow and ownership

`tools/map/geographic_frame.helper.py` reuses the established forward projection from `tools/design/geography.py`. It adds inverse sampling and separate sample-center/outer-cell bounds. This read-only dependency keeps the existing designs byte-compatible; a future shared geometry extraction must preserve their output. North-up WGS84 coordinates use cosine-corrected longitude and 1.12 square padding. An integer control coordinate 0..size−1 locates a tile sample center. The outer cell envelope extends half a sample interval beyond those extrema; it must not be confused with the requested bbox or the padded control-point bounds. Native camera/orientation calibration remains pending.

`tools/map/geographic_raster.compiler.py` is a pure compiler for a small internal sample-grid format. A source explicitly supplies EPSG:4326, metre units, a vertical datum, a modern DEM/DSM or synthetic classification, the first sample's center, positive longitude/negative latitude steps and rectangular finite values or null nodata. It rejects other coordinate systems, polar/antimeridian frames, implicit units and map sizes outside 300–400. There is no GeoTIFF reader or guessed affine/PixelIsPoint conversion in this compiler. A verified external extraction step must provide the sample centers correctly; rotated/nonregular rasters need a future explicit adapter.

The compiler resamples at the existing design projection's integer tile centers with bilinear interpolation, rounded to six decimals. It never fills nodata, extrapolates beyond sample-center coverage or derives water from low elevation. A source may cover the requested rectangle while missing the larger padded square. Default compilation rejects incomplete coverage. `--allow-incomplete` preserves null values and explicit missing counts in a research candidate; it cannot promote the result or create land. Zero-weight nodata neighbors do not poison an otherwise exact valid sample. Pixel indices within 1e-7 of an integer are snapped only to absorb floating-point coordinate noise; this is not geographic gap filling or a claim of positional accuracy.

`tools/map/geographic_raster.script.py` reads input bytes, verifies modern inputs' reported original-file hash and local source notice, records the sample-grid byte hash, then writes the candidate to an explicit output path. It refuses to overwrite the sample grid or the original source artifact. Synthetic fixtures are explicitly labeled and never receive a verified modern-source flag. A matching file hash identifies the referenced file; it does not prove extraction, units, geographic interpretation, copyright clearance or ancient terrain. `sourceSampleExtractionVerified` therefore remains false. Modern output carries the source notice text and the resampling description. No network, game installation, native exporter or new third-party dependency is used.

## Private large-map editor diagnostic

`tools/map/large-map-diagnostic.script.py` accepts only the compiled, single-scenario `technical-pilot` fixture and builds a deep clone at 300 or 400 tiles. It changes only map dimensions, the map start, the two initial unit positions, the two objective locations, and the disposable clone's empty-route progress key; it then adds four disjoint 3×3 artificial terrain controls. The pure transform and its bounds/rejection cases are registered by `tests/maps/large-map-diagnostic.test.ts` and `tests/maps/test_large_map_diagnostic.py`. They do not run the exporter.

When the reserved export window is available, run `tools/map/large-map-diagnostic.script.py --size 400` (or `--size 300`) with the selected/pinned Python interpreter, for example `python3 tools/map/large-map-diagnostic.script.py --size 400` when `python3` is that interpreter. The command first runs the existing `bun run campaign:build technical-pilot`, then invokes `tools/python/export_aoe2.py` with `sys.executable`, copies the generated scenario and the two draft locale catalogues byte-for-byte into a private editor kit, and uses the existing adapter ZIP command. Build files stay under `build/large-map-diagnostic/<size>/`; the private ZIP and its non-self-referential hash receipt go under `dist/` and the build directory. It does not include the generated campaign container in that ZIP.

The 400-tile artificial marker centres are data-north road `(200,20)`, data-east dirt-1 `(380,200)`, data-south snow `(200,380)`, and data-west water-deep `(20,200)`; 300-tile centres use the same rounded scale. North is a grid label, not camera calibration. The water patch is away from the diagonal movement corridor and establishes no crossing or transport capability. The report keeps `gameVerified`, `historicalMap` and `nativeTerrainFromDsm` false and `cameraCalibration` pending. A screenshot, editor load, movement, save/load and actual orientation remain human game observations; no campaign launch, performance-at-cap testing, historical interpretation or public distribution is claimed.

## Reproduction

Run the adversarial suite directly, or through the normal Bun test gate:

```sh
python3 tests/maps/test_geographic_raster.py
bun test tests/maps/geographic-raster.test.ts
```

The [small real DSM fixture](../../tests/maps/fixtures/edirne-dsm-sample-grid.json) preserves 25 contiguous source samples. Luna collected them; the architect independently re-read the same TIFF pixels, source hash and PixelIsPoint tiepoint, then added explicit metre-unit metadata for this internal format. Its [licence notice](../../tests/maps/fixtures/edirne-dsm-sample-grid.license.md) carries the source, modified-data and liability notices. The frame below is deliberately a tiny technical sample area; interpolating it onto 300 or 400 samples does not make it a historically coherent giant game map or increase source resolution.

```sh
python3 tools/map/geographic_raster.script.py \
  --source-grid tests/maps/fixtures/edirne-dsm-sample-grid.json \
  --bbox 26.5603 41.66975 26.5608 41.67025 \
  --size 300 --output /tmp/edirne-height-candidate.json
```

The output is `geographic-height-raster-candidate`, an internal research artifact. It stores raw metre heights, not native elevation levels or a format AoE2 recognizes. The source grid and actual source file have distinct hashes. Its completeness flag means only that every requested sample had interpolation support. It is not a certificate of accuracy, terrain, passability or chronology.

## Remaining S2 acceptance

- Add verified extraction for real regional elevation rasters, with CRS/vertical datum, sample interpretation, coverage, licence and field-specific uncertainty. A modern DSM includes buildings and vegetation; it is not a bare-earth DTM or an ancient terrain reconstruction. Preserve unknown areas instead of flattening them.
- Define dated land/water/building/fortification layers independently of height. Validate complete unit/building footprints, receiver packing and full corridor widths against those layers and the half-cell frame envelope. A centerline missing a river is insufficient. Bridge and ferry claims require dated controls and actual supported operations; no painted land across water.
- Choose explicit height-to-native-level quantization, slopes, cliffs and performance budgets without losing meaningful terrain. Do not infer an accessible path from a smooth raster or a large map size. The existing authored map dimensions are candidates, not engine acceptance evidence.
- Implement and review actual map/transport operations with the relevant native adapter slice. Supply the real loading, disembarkation, lost-boat, alternative-route and impassable-cliff fixtures demanded by S2; the present raster tests do not substitute for them. Native composed-profile export stays rejected until its own implementation exists.
- Calibrate real orientation, footprint collisions, routes, resource sites and timing in AoE2 with build, artifact hash and difficulty. Apply the existing per-episode all-skip/all-complete/three-portfolio playability matrix. No historical or production authoring slice unlocks from these numerical tests.

The Bun wrapper reuses the existing Python-command selector and runs the standard-library Python suite, making this partial raster component part of `bun run validate`. This does not change the proposal's pending status, satisfy all of S2, or approve any historical dossier. Independent technical review and the official merge gate must be recorded for the delivered component separately.

## Component checkpoint — 18 October 2026

Architect gpt-6 implemented the files above in the official `i00003/S2` unit based on integrated develop 2164c2d0. `bun run validate` passes 108 tests/426 expectations and includes six internal Python cases through the new map test. The cases cover inverse/orientation, a synthetic plane, nodata and square-padding gaps, invalid units/frames/grids, actual DSM sample input on 300 and 400 grids, original-file and sample-grid provenance, and rejection of bad hashes/source-grid overwrite. A separate actual 400-grid CLI run completed with finite height range 34.881202–38.48747 metres, complete sample coverage and `nativeTerrainWritten=false`, `gameVerified=false`. Root manually rechecked the 25 fixture pixels against the actual TIFF before normalization. No native map, transport/export or AoE2 run is claimed. Independent technical review and official publication remain pending at this checkpoint; the full S2 acceptance above remains incomplete.

Independent technical review on final candidate `6d8bca8` is conforming within the component's scope: see [Luna's report](../../tests/maps/geographic-raster-review.md), commit `c0370826`. The reviewer ran six tests under Python 3.10, the Bun wrapper and the full 108-test/426-expectation gate, plus a 400-square CLI run and independent comparison of 25 fixture values and georeference against the actual TIFF. The review does not approve historical interpretation, source licensing, native terrain or the whole S2 slice. The architect's own earlier gate passed, and its final targeted wrapper rerun passed after the snapping fix. Official publication and merge certification remain separate; S2 continues pending because the acceptance above is incomplete.

## Regional reference extent audit

`tools/map/geographic_extent_audit.script.py` reuses the existing nine-odyssey catalogue loader and selection validator, then compares every authored episode's requested rectangle, padded sample-center square and full outer-cell envelope against its regional reference rectangle. It reports each campaign, including those with zero dossiers, and fingerprints the semantic input snapshots. Missing profiles, missing dossier lists or invalid frames fail; they cannot look like covered maps. Containment is an arithmetic question, never historical approval or a DEM/terrain certificate.

```sh
python3 tools/map/geographic_extent_audit.script.py \
  --output build/reports/geographic-extent-audit.json
```

Without `--output`, JSON goes to stdout. Repository output belongs under generated `build/`; an explicit external temporary destination is also allowed. No campaign, bbox, actor, source profile or approved contract is rewritten.

The first actual run on 18 October 2026 covered all 63 dossiers and all 278 selections in nine campaigns. It found 26 outer-envelope coverage questions: 17 faith-origins and 9 imperial-church. None arose only from the half-cell extension; the padded sample centers already exceeded the reference in all 26 cases. Those are review questions, not 26 historically false maps. A regional rectangle is a source-control frame, not a political boundary, ancient land mask or complete source-coverage certificate. An inside result also proves none of those things.

The per-record coordinates and input hashes in the generated artifact identify the actual required extent. The relevant architect slices, d00002/S2 for faith-origins and d00002/S3 for imperial-church, must determine whether additional dated geographic controls/elevation coverage or a consciously redesigned frame is appropriate. Do not globally shrink maps or enlarge reference profiles just to remove findings. Source coverage, local actor/corridor placement and real historical terrain must be reviewed together before MiniMax materializes a map. The Sirmium final frame is inside its reference even with outer cells; that does not grant its ancient-terrain or packing approval. The current larger Adrianople 378 frame extends beyond its smaller regional reference and needs the same explicit source-coverage treatment, not a hidden terrain fill.

Three additional Python regressions cover requested-vs-padded mismatch, a pure half-cell edge case, retention of a zero-dossier campaign, missing-source rejection and the actual complete-catalogue CLI. The normal Bun map test runs these with the original six raster tests. This audit does not complete S2's footprint/bridge/transport/navigation acceptance, change dossier counts or close any historical-authoring gate.

The [independent extent review](../../tests/maps/geographic-extent-review.md), commit `1c6acfd7`, is conforming on candidate `c8fbc3f`. The reviewer reproduced 63/278/26/0, retained all seven zero-dossier campaigns, ran nine Python 3.10 cases and the full 108-test/426-expectation gate, and checked forbidden output destinations. These are component checks, not approval of 26 historical maps or the whole S2 slice. Official integration remains governed by the merge gate.

The [design SVG renderer](../../tools/design/episode_dossiers.script.py) now separates the padded sample-center clipping envelope from the unchanged requested projection bbox, reusing the frame helper above. Modern geographic and explicitly schematic controls can reach the full drawn square. Existing callers retain their old clipping/rounding default; the explicit viewport option retains unrounded intersection coordinates until the existing tile projection. No hub, corridor, campaign or geographic source profile is rescaled. This corrects a drawing omission, not the 26 regional-coverage questions, a historical shoreline or native terrain. Native source-layer coverage and actual terrain remain separate gates.


## Actual 400-square binary diagnostic — 26 October 2026

The bounded diagnostic implementation by gpt-6-luna is integrated at `a7f8dcd5fd3091868eeab73b0aad2206d419a85d`; it does not close all i00003/S2. Root gpt-6 subsequently ran the real 400 export with the pinned parser 0.9.6 / scenario 1.59 and existing rge_campaign. Compiler, adapter build/round-trip/xs-check and ZIP commands exited 0. The editor-kit ZIP has SHA-256 `eab9d88e5af8e0bc77b4f1827167c5db17560e1a8fa3548014ab0320cb112c0b` (6309 bytes); its original scenario is `c5a9290b437bb40f8dad01edb4a7e54d5fc0e1d9d17bb65d6d3a68cda142770c` (3461 bytes). These are hashes of this execution, not a promise of stable native binary metadata.

Root independently decoded the copied native scenario: 400-square, 160000 tiles, 159964 grass cells and exactly 9 each of road/dirt-1/snow/water-deep at all 36 specified marker cells; every elevation is 0. The two native unit centres are (50.5,50.5) and (300.5,300.5), consistent with the adapter’s half-tile placement. Both archived draft locale catalogues match compiler bytes; the five-entry kit contains no campaign container. The receipt and decoded inspection are preserved outside the disposable unit, under the private `large-map-diagnostic-400-20261026` artifact directory.

The README now requires a separate named editor copy and verification of the untouched original. A copy can have the same hash when its bytes are identical; there is no requirement to edit it to force another hash. Actual game load, isometric-camera orientation, movement, save/load, transport, history and performance remain unverified. No 300 native export is inferred from the 300 pure transform tests.
