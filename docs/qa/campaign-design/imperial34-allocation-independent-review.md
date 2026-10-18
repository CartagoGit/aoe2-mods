# Independent review: Imperial 34 finite allocation study

Reviewer: gpt-6-luna  
Candidate reviewed: `d3595e60ce2e9ce2a3d4e0bc2f158567d32cab0a` (base `1c0db6e2`; includes proposal `236bef2`, study candidate `cdc1ba8`, and narrator-scope correction `d3595e6`).  
Scope: accounting helper, report generator, tests, allocation plan/study, brief and handoff/proposal context. This is not a formal approval of `d00002/all`.

## Findings

I found no blocking arithmetic or implementation defect in the bounded accounting study. The helper applies each debit before its reserved reward, only follows affordable prefixes, and records each optional task at most once. It rejects boolean/non-integer/negative/unknown resource values and duplicate identities. For the supplied plan, the nine meal/shelter combinations produce 9/7/3 all-skip affordable combinations on easy/standard/hard. The hard all-skip plans and remainders agree with the plan. Rechecking every reported all-seven example order against each intermediate balance found 19 valid orders; none uses an optional reward to fund that same task. The hard shared-hearth/rented case correctly demonstrates that the 50-wood repair cannot be paid first, while a prior provisions reward can fund it. Optional reward stock remains explicitly separate from operating stock.

The four focused tests cover the key affordability, prefix, no-duplication, invalid-input and fingerprint cases. The audit labels its output `nativeImplemented=false` and `gameVerified=false`. The plan and study likewise state that this is candidate economic analysis, not a gameplay DSL, completed dossier, accepted architecture or proof of an interesting RTS episode. They leave actual routes, actors, work locations, UI, jointly atomic reservation, cancellation/recovery and engine behavior pending. The study correctly rejects promotion if the result is only a menu plus inevitable walking. The three-slice i00007 proposal remains pending; I did not implement it.

The current enumeration limits bound the supplied study (2 services, 3 alternatives each, 7 optionals) and reject excessive combinations/states. As a generalization limit, `MAX_COMBINATIONS` bounds the product of recipe counts but does not independently cap the number of services when each has one recipe. That is harmless for this fixed input, but a generalized authoring tool should also bound service/recipe row counts. The fingerprint includes the resolved plan and optional monetary inputs; it does not fingerprint the executable semantics of `secondary.py`. This does not invalidate the present report, whose source and shared-mechanics relationship are documented, but future reproducibility claims should retain a source/code revision fingerprint if those mechanics can change.

The final `d3595e6` change corrects only the narrator JSON scope label from 273 to 278 selected episode odysseys. The selection count was already 278; no narrator biography, knowledge, episode ID or episode content changed. JSON and project validation passed at the candidate tip.

## Verification

- `python3 tools/design/test_finite_allocation_audit.py`: 4 tests passed.
- `python3 tools/design/finite_allocation_audit.script.py`: 9 combinations; all-skip easy/standard/hard 9/7/3; `nativeImplemented=false`; `gameVerified=false`.
- `python3 tools/design/test_design.py`: 66 tests passed.
- `bun run validate`: passed; 108 tests / 426 expectations, documentation checks passed, and one campaign validated.

These checks assess the study and repository validation only. They do not establish historical accuracy, native capability, map feasibility, gameplay quality or engine behavior.

## Incremental review: `891be5e52d7e04c68bbf082a12f460e2e8c82773`

The added `MAX_SERVICES = 8` closes the previously noted unbounded service-count case. Its regression supplies nine one-recipe services and expects rejection; the combined allocation/optional-state bound also has a direct rejection case. The existing four focused tests pass. This remains a cap for this pure analysis helper, not a runtime contract.

I independently decoded the committed DSM crop with Pillow and compared every value against the original file available at `/tmp/Copernicus_DSM_COG_10_N41_00_E028_00_DEM.tif`, using the recorded integer source window (column 3312, row 3384, 286 × 210). The source SHA-256 is `d33df50121e0bb20e4801d8901832e368f756d740a71343c6070313ed6246377`; the crop SHA-256 is `25b1a91f7bee6511fe80732f8d3179f994d2976cbc9811de72f92b67846ab228` and 167,144 bytes. All 60,060 float samples are exactly equal and finite. TIFF scale is 1/3600 degree; the PixelIsPoint tiepoint gives crop sample (0,0) center (28.92, 41.06), consistent with the source window and recorded affine. The requested bbox [28.92, 41.002, 28.999, 41.06] is covered by sample centers: eastmost crop center is 28.9991666667 and southernmost is 41.0019444444. Outer cell bounds are wider; they are not substituted for sample-center coverage. Both TIFFs decode to EPSG:4326/WGS84 GeoKeys, PixelIsPoint, float32 and no nodata tag. Raw GeoKey arrays differ because offsets into GeoDoubleParams were relocated during lossless re-encoding; the decoded key values, scale and tiepoint agree. The vertical datum is documented from the product, not tagged in the TIFF. This is a modern DSM reference only; the file does not verify 380 terrain, coastline, ancient sites, traversability or production-map approval. The notice and manifest entry identify the licence, attribution and non-production status.

The narrator label correction remains limited to the scope text. The refreshed handoff now says nine odysseys/278 selections and lists i00007 as pending; its Constantinople section preserves the all-skip arithmetic while explicitly saying choice/reservation, terrain and gameplay are not implemented. The study and README distinguish the 63 dossiers from the 215 selection-only episodes (278 total), and the manifest contains 37 assets including the new DSM crop. JSON parsing and `bun run validate` pass.

I inspected the received Jewish opening collection's metadata, scope, structure and recorded access-gap section, but did not independently reopen its cited primary or secondary sources. Its own metadata limits it to four existing episodes, attributes it to gpt-6-luna, identifies consulted project material separately from source work, and states that it is not independent historical review or approval. It includes partial-access/edition caveats and does not claim a building, route, date or coordinate established by that file. This is a review of attribution and scope controls only, not a review of its historical conclusions.

Incremental verification at this tip: `python3 tools/design/test_finite_allocation_audit.py` (4 passed), `python3 tools/design/finite_allocation_audit.script.py` (9 combinations; 9/7/3; native/game verification false), `python3 tools/design/test_design.py` (66 passed), and `bun run validate` (108 tests / 426 expectations; docs and campaign checks passed). I found no new blocker within this bounded scope. The allocation prototype still has no runtime implementation, game proof or historical approval.
