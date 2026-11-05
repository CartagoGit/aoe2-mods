# Transport map diagnostic: bounded mechanical packet

Architect: gpt-6, 26 October 2026. Partial milestone inside the existing i00003/S2, after its original large-map diagnostic. This packet authorizes an assigned worker to implement a private artificial observation fixture. It does not authorize closing S2, historical production, a new transport contract or game-verification claims. Consult the connected DelendAI proposal and own claims before work.

## Purpose, ownership and reuse

Add one explicit `transport-observation` variant to [large-map-diagnostic.script.py](../../tools/map/large-map-diagnostic.script.py), reusing its source validation, coordinate scaling, real exporter, catalogue checks, packaging, native inspection and failure-safe receipts. Keep the existing default as `scale` and preserve its transformations, output paths and two-unit fixture. Do not duplicate the adapter or create a parallel scenario writer.

Owned implementation files, all already inside S2: `tools/map/large-map-diagnostic.script.py`, `tests/maps/test_large_map_diagnostic.py`, `tests/maps/large-map-diagnostic.test.ts` and `docs/architecture/geographic-maps.md`. Do not alter schemas, public campaign/progress IDs, engine catalogue, campaign sources, string registry, global CLI or geographic profiles. Use a small variant-specific builder/helper and common orchestration; no plugin framework is required for two fixtures. Descriptive role filenames remain mandatory.

The source remains the compiled 32-square `technical-pilot` / `01-technical-battle` IR with exactly its original two militia. Validate it with the existing strict checks before cloning. Accept only integer sizes 300/400, reject booleans and unsupported variants before exporting or invalidating a previous completed artifact. The original input must remain byte-equivalent after either build. Remove only the disposable clone's progressKey as already specified in the [scale packet](LARGE-MAP-DIAGNOSTIC-PACKET.md).

## Fixed artificial geometry

Use the existing 32-to-size rounding for the original start, two militia and objective positions. Keep four existing 3×3 orientation patches (36 cells). All four patches lie outside the new rectangle below. All map elevations remain zero; no bridge, cliff, current or historical coastline is asserted.

Define rectangle endpoints in the 400 grid, half-open: x `[180,220)`, y `[80,320)`. For the selected size, scale each endpoint independently with `floor(value * size / 400 + 0.5)`. Overlay each rectangle cell exactly once. The first and last x columns are `beach`; each next inner column whose distance from its nearer outer edge is 1, 2 or 3 is `water-shallow`; all remaining columns are `water-deep`. The outer edge distance is `min(x-left, right-1-x)`. This geometric rule, including the three shallow columns at size 300, is authoritative; do not scale a 400 raster cell-by-cell or introduce duplicate positions.

| Size | Rectangle | Beach columns | Shallow columns | Deep columns |
|---|---|---|---|---|
| 400 | x180..219, y80..319 | 180,219 | 181..183,216..218 | 184..215 |
| 300 | x135..164, y60..239 | 135,164 | 136..138,161..163 | 139..160 |

At 400 there are 9,600 rectangle cells: 480 beach, 1,440 shallow and 7,680 deep. At 300 there are 5,400: 360 beach, 1,080 shallow and 3,960 deep. With the original markers retained, expected whole-map counts are:

| Size | grass-1 | water-deep | water-shallow | beach | road | dirt-1 | snow |
|---|---:|---:|---:|---:|---:|---:|---:|
| 400 | 150364 | 7689 | 1440 | 480 | 9 | 9 | 9 |
| 300 | 84564 | 3969 | 1080 | 360 | 9 | 9 | 9 |

The west marker adds the extra nine deep-water cells. All marker and rectangle positions are unique and within bounds. North and south land detours are candidate manual routes via y60/y340 at 400, scaled to y45/y255 at 300, outside the rectangle ends. They are not authored bridges or certified paths. Test the actual native shoreline; terrain names alone do not prove embarkation or unload access.

## Units, timing and objective limits

Preserve both existing militia IDs, factions, positions and normal native statistics. Add exactly two nonessential player units: `diagnostic-transport` of type `transport-ship` at base-400 point (187,200), and `diagnostic-passenger` of type `villager-male` at (176,200). Scale these new coordinates with size/400 rounding. At 300 the ship is (140,150), passenger (132,150). Both unit types and all seven terrain names exist in the pinned catalogue; check them before invoking the adapter. The boat starts in deep water at both sizes, and the passenger on ordinary grass outside the shoreline. IDs are private IR-clone entity IDs, not new registered campaign identities. No new military/religious representation, training queue, production or statistic override is added.

The existing player is now three units and enemy one. Correct only the variant clone's descriptive faction strategy `limits` text so it does not still describe the whole fixture as two units. Do not infer an engine population cap from that prose. Keep economy, objectives, prepare timer and defeat-first policy unchanged. Set only this variant clone's `defeat.timeoutSeconds` from the known source 600 to 1800, to leave a finite manual observation window. Reject source drift of that expected field rather than replacing arbitrary timers. Preserve the default variant's 600 seconds. Record this difference in report and instructions. The guard remains the only essential unit; boat/passenger deletion is an observation action, not a newly authored defeat condition.

The two existing objectives remain prepare then destroy enemy-guard. They do not verify boarding, unloading, detours or boat loss. The player must avoid defeating the enemy or losing the essential guard before completing observations. No automatic transport predicate, carrier ledger, replacement passenger, disembark receipt or loss detector is introduced. Existing localization remains copied draft text for the original combat fixture, with this mismatch explained in the kit instructions rather than altered string IDs.

## Export and receipts

Expose `--variant scale|transport-observation`; default scale. The pure builder and runner accept the explicit variant too, preserving existing call signatures through a default. New variant outputs belong to `build/transport-map-diagnostic/<size>/` and `dist/transport-map-diagnostic-<size>.zip`; scenario archive name `scenario/CDF_Transport<size>_Diagnostic.aoe2scenario`. Keep scale outputs separate. Reuse the same failure-safe artifact lifecycle: remove matching stale receipt/archive/temp/native-inspection before replacing outputs, no ZIP after failed export, receipt only after successful ZIP, bind report/scenario/archive hashes. Invalid input leaves prior completed outputs untouched.

Extend the current native inspector to reuse expected terrain data and transformed-unit coordinates for both variants. A helper can derive expected cell overrides/counts from the known transform or clone; it must not create a second exporter. Verify map size, all elevations, every authored marker/rectangle cell, whole-map terrain counts, all four actual native unit positions, unit types/owners and original essential-unit binding. Avoid an inspector that merely compares aggregate totals while accepting misplaced shorelines. Keep producer file hash and reproduction command, including the explicit variant, in its result. Reuse actual pinned parser unit/terrain enums instead of hardcoding guessed engine numbers.

Reports retain gameVerified=false, historicalMap=false, nativeTerrainFromDsm=false and cameraCalibration=pending. Record variant, rectangle rules/coordinates, added units, inherited objective limitations, timeout, terrain counts and all commands. This is a private editor kit, not a campaign container, mod publication or Steam-specific installer. Follow [the store-independent private-test instructions](PRIVATE-PILOTS-WINDOWS-STEAM-ES.md); use relative archive paths and never touch the user's game installation.

## Required verification and delivery

Fast tests must cover both sizes and variants, exact coordinates and terrain counts above, nonoverlapping cells, ship in deep water/passenger on grass, all unmodified fields, default preservation, timeout-only variant change and source immutability. Reject unsupported source/size/variant before exporter execution. Extend meaningful export/ZIP failure regressions so variant path selection cannot leave a stale successful receipt. Keep the Bun wrapper registering the Python suite. No native export inside each unit test.

Run validate and test:export in the assigned serialized verification window. Perform one real transport-observation 400 export, decode the scenario using the committed inspector and preserve complete logs, artifact hashes, byte-identical draft locales and the external receipt outside any unit later retired. Record 300 as pure-tested only unless actually exported. Git author and committer remain Cartago; actual model identity/session must be its own. Publish through DelendAI's gate. Independent review is required for the bounded product; never self-approve or submit the entire S2 as complete.

The manual observation sheet must leave all outcomes pending. Ask the tester to record exact game build/store/OS/language and artifact hash, editor load, ordinary boarding, actual passenger in boat, unload at the opposite shore, north and south land detours, boat deletion with a passenger aboard, and save/load before boarding, aboard and after unloading. Record what the game does on boat deletion without assuming passenger death or survival. If the editor cannot expose a required state, record that limit. Preserve original scenario; save experiments as a separate file/path with its own hash.

Remaining full-S2 gates include calibrated camera/geography, relief/footprints/real bridges, certified cliff impassability, route feasibility and campaign-specific performance caps. This flat water fixture alone cannot satisfy them, and a native binary decode cannot provide GAME VERIFIED. Missing operations become infrastructure requirements, never wall-as-cliff or timer-as-boarding substitutions.

## Bounded packet review

gpt-6-luna independently read the packet, source fixture and pinned catalogue on 26 October 2026. It confirmed both terrain-count tables, endpoints, ship/passenger placement, source timeout and economy-review arithmetic. This is packet review, not implementation acceptance or a formal verdict on i00003/S2. Actual rectangular-cell/type/owner inspection remains part of the assigned implementation.
