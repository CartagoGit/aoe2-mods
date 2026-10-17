# Adrianople 378: relief and withdrawal design

17 October 2026. Architect gpt-6, d00002/S3 with S1 research and S11 handoff. ID `32-defeat-and-withdrawal-adrianople`, display 30, future f00003/S35. Design only: no exact battle location, historical terrain, native navigation or game balance approved. The modern raster is already integrated; this decision adds no new downloaded binary or licence assumption.

The [source audit](imperial32-source-audit.json) records selected primary reading. Roman defeat and Valens’ death are fixed. Different accounts of his death remain alternatives. The Latin temporal eighth hour cannot supply an eight-mile radius; an earlier fifteen-mile position is not the battlefield. Ammianus 31.15.4 also prevents an automatic equation of survival with admission to Hadrianopolis. The playable groups, route sector and opposing patrols are disclosed local fiction. No emperor rescue, corpse search, wagon-circle assault, theological punishment or replay of the later siege.

## Geographic frame and evidence

Use WGS 84 bbox `[26.60,41.70,26.76,41.87]`, north up. Approximate span at the middle latitude:13.3 km east-west and 18.8 km north-south. This is a regional design frame northeast of modern Edirne, not a proposed battlefield identification. Modern city orientation `[26.5556,41.6769]` is off map southwest; it is not a certified gate or objective. Keep profile `adrianople378` separate from the 324 lower-Hebrus ferry environment.

The [sampling dataset](adrianople378-relief-sampling.json) records the existing [source crop and transformation](edirne-modern-dsm-processing.json), SHA 256 `7495100ff4e45717006daaaae3996dc0f91d06df524a656405703ff51457546e`, EPSG 4326 and PixelIsPoint. The local center-mask snapshot has 351900 valid cells within a 612×576 read window;612 boundary cells are excluded by its rasterizer convention. Those are distinct quantities. Local DSM minimum 47.845 m, median 144.469 m, p 95 212.000 m, maximum 268.356 m. They are surface samples; vegetation, buildings and modern infrastructure can contribute. Vertical EGM 2008/metres come from product documentation, not a vertical CRS embedded in this TIFF.

Luna gpt-6-luna collected points and 101 samples per straight segment supplied by architect gpt-6. Root independently checked all 1414 coordinate/value/pixel-index samples, eight 5×5 windows, ranges, sums, source hash/CRS/Point and approximate distances:4335 assertions passed. This is data verification, not a game test. The dataset records the preliminary collector’s wrong identity and “user-supplied” labels as a provenance correction. Modern low colors in the [regional preview](images/edirne-modern-dsm-regional-preview.png) mean height, not water. Neither the figure nor missing coarse river lines certifies ancient dry ground.

| Hub | Architect point lon,lat | Modern DSM containing-cell m | Design role; not an ancient site |
|---|---|---:|---|
| 1 NE | 26.729,41.837|142.862|Six original foot stragglers; four required |
| 2 N |26.681,41.836|178.662|Four original mounted scouts; two required |
| 3 C |26.687,41.793|113.242|Mounted checkpoint, potentially contested |
| 4 W |26.636,41.791|112.809|Foot checkpoint, outside hostile envelope |
| 5 SW |26.628,41.730|78.512|Shared off-city receiver; dry footprint unverified |
| 6 S |26.686,41.742|152.392|Optional supply shoulder |
| 7 E |26.729,41.785|197.357|Initial finite opposing force |
| 8 NW |26.635,41.837|159.010|Northern relief and independent travelers |

Do not interpret a lower containing cell as a wetland or a higher cell as a fort. In particular the southwest receiver needs a dated local water/ground check before approval; the point itself does not prove a dry camp. Low central/western points are separated by local rises: the route cannot be a flat trench connecting equal endpoint heights.

## Route comparisons and useful decisions

Lengths in tiles are the factory’s cosine-corrected, square-padded schematic centerlines; kilometre values are approximate straight regional polylines, not measured roads. DSM min/max include 101 containing-cell samples per segment, with repeated endpoints. Native corridor polygons, ramps, unit packing and actual travel times are not certified. Do not turn accumulated unsmoothed DSM deltas into road grade, travel cost or evidence of difficulty.

| Proposed route | Schematic tiles | Approximate km | Sampled DSM range m | Intended decision |
|---|---:|---:|---|---|
| NE→N→NW→W |243.36|12.886|112.50–195.52|Longer northern foot relief; can concentrate support near mounted rally |
| NE→C→W |192.98|10.223|108.80–178.20|Shorter central foot passage through bounded local pressure |
| N→C |90.61|4.780|113.24–178.88|Mounted scouts descend toward their own checkpoint |
| C→W→SW |208.24|11.016|78.51–172.16|Western final mounted withdrawal; useful reunion with foot column |
| C→S→SW |200.94|10.637|70.24–154.70|Southern alternative, with separate finite supply opportunities |
| W→SW |128.44|6.777|78.51–144.79|Main foot exit; preserve actual intervening rise |
| E→C |67.74|3.597|103.86–197.36|Invented pressure direction; not an authenticated Gothic advance |
| NE→E→S |221.37|11.696|136.04–201.06|Exposed eastern connection; no main goal requires it |

Northern foot relief is about 50.38 schematic tiles /2.66 approximate km longer than central passage. This cost is a hypothesis to measure, not a blanket statement that northern travel is interesting. Southern final travel is slightly shorter in the schematic than western travel; its “detour” means a diversion to optional supplies, not a proven longer route. Keep this distinction in captions and review. The 384 secondary tasks across the project do not prove 384 good decisions.

The local design’s main problem is preserving two types of originals through a staggered withdrawal. o 2 checks four foot originals currently west while two mounted originals are currently central; then o 3 checks both groups southwest. The riders are usable tactical participants and must also escape. They are not disposable flags. No ongoing hold begins at o 2 and no old arrival substitutes for current presence. Fourteen supporting troops can concentrate or split; they do not replace a foot or mounted original. The player may avoid compulsory kills, but the central mounted muster must still require a fair tactical decision in the real map.

Compare northern foot relief with central support, central force concentration followed by separation for the checkpoint, and southern supply investment during final mounted withdrawal. All can combine. Seven tasks cover northern/central observation, guidance, two distinct aid deliveries, a 50 Wrepair, a 50 Gtrade and two independent travelers. Rewards are finite and idempotent. Mandatory 180 F 80 Wand both survivor thresholds remain viable with every secondary skipped; accessible all-skip stock 1070 F 640 W 210 G 120 S is a static envelope, not calibrated pacing. Never add a late artificial reinforcement, hidden deadline or forced loss to make this design feel harder.

## Terrain candidate to be resolved by the architect

Proposed compression of verified modern relative relief into the existing native 0–7 height range:

| Modern source height band m | Candidate native height |
|---|---:|
| below 70 |0|
|70 to below 100 |1|
|100 to below 130 |2|
|130 to below 160 |3|
|160 to below 190 |4|
|190 to below 220 |5|
|220 to below 250 |6|
|250 and above |7|

These cutoffs are an explicit architect candidate, not implemented terrain or a historic reconstruction. They retain broad sampled differences, but must be checked against the whole padded square, present-day surface filtering, dated hydrography, slope continuity and native ramps. Native height 0 does not mean water. Do not quantile-remap each district separately, mirror terrain, or apply cliff barriers wherever a threshold is crossed. A ridge may need connected graded transitions without changing its regional orientation. Exact flattening for actor footprints and any relocation requires architect review with evidence; MiniMax cannot decide those corrections independently.

## Infrastructure and acceptance before handoff

Existing owner i00003/S2 covers regional terrain/footprints; i00003/S3 covers finite military native adaptation; i00005/S2 covers live observations; s00001 covers real motor evidence. The bounded-pursuit requirement remains unimplemented: the author’s proposed lon 26.676–26.750 /lat 41.772–41.814 encounter sector is not an existing IR/adapter AI polygon. It may contest central C; origins N/NE, western muster, southwest reception, southern supplies and northern relief must stay outside the complete acquisition/attack/projectile/turnaround envelope. The existing i00003/S3 acceptance now records this reproducible requirement, with out-of-sector targets, kiting, maximum range and save/load retaining targets. Implement it there and reject unsupported bounds; never ignore them or silently replace them with a timer. No claim that a patrol order or max unit count guarantees a leash.

At all three difficulties instantiate only 8/14/22 selected opposing identities and the same four mounted plus fourteen supporting friendlies. Unused maximum roster members are absent, not invisible reserves. No production, paid military replacement, initial simulated wound or automatic health bonus. Select dated native military proxies separately; generic design role labels are not certified engine unit IDs.

Acceptance requires traversing the full widths 10/12/8 tiles with actual formation/receiving radii, testing alternate routes with all secondaries skipped and completed, and testing 90 joint original subsets. Move actors out between observations, substitute eligible originals, remove unknown/dead actors, save/load at both checkpoints and during payment. Third loss in either original group defeats; optional loss alone does not. Test central pressure without impossible focus fire or unbounded pursuit, and show how easy/standard/hard changes a decision. Measure active/idle time and unavoidable travel using [playability acceptance](../../design/civic-playability-acceptance.md); generic 40–75 minute fields are placeholders, not a session result.

All source and derived raster data remain governed by the [Copernicus licence notice](geography/edirne-modern-dsm-license.md). This text and numerical sampling do not grant production artwork approval, identify an ancient location or close a historical/native/game gate.
