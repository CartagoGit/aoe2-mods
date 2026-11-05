# Jerusalem: physical actor layout review

Architect: gpt-6, 27 October 2026. Scope: the [private draft binding](19-native-binding-draft.json), not an approved historical terrain, native mission, engine test or additional dossier. Source SHA-256 is recorded in the binding. The 30-episode source file is unchanged by this delivery.

## Placement and player meaning

The binding retains eight main household originals and nine optional originals. Source offsets and physical binding offsets are separate, explicit fields. All movement stays in the same fictional hub district. Numbered main labels are deliberately fictional and bilingual; they are not names recovered from a historical register. Aid and copy proxies are named **bearers**, so a selectable civilian can carry a fictional crate or working copy without depicting a crate as a person or a later canonical book. The store is a fixed damaged building; the trader and guide have distinct task names. Optional visiting households remain separate from the main eight.

The source draft has five coincident actor pairs in three positions. The revised offsets remove these coincidences. It also separates the copy and visiting-household reception points at hub-1 and the overlapping aid, repair-approach and trade points at hub-2. `destination-1` remains an activity circle with no invented main objective. The repair-zone point is a district approach marker only: the actual repair authorization is selection of the original store, wherever its fixed body is placed. It is not an unstated delivery condition or the building's address.

The shared native base snaps each body to `floor(coordinate)+0.5`. Rechecking those actual proposed positions gives:

| Geometric property | Result |
|---|---:|
| Distinct original bodies | 17 of 17 |
| Minimum distance between body centres | 4 tiles |
| Minimum initial body-centre clearance outside any receiving circle | 3.100467 tiles |
| Minimum gap between receiving-circle edges | 2 tiles |
| Minimum store clearance beyond circle radius + 2-tile approach + conservative 3-tile extent | 0.392074 tiles |

The [placement figure](21-physical-layout.png) shows the three district layouts with native-snapped body centres and receiving circles. It is a geometric diagram, not a reconstruction of the landscape.

The 3-tile extent is a deliberately conservative design exclusion radius, not an extracted engine footprint. It does not certify decorative markers, later terrain obstructions or engine pathfinding. Do not promote these arithmetic checks to native footprint evidence. Preserve the original handles after native creation and inspect the actual fixed building/approach before approval. All 17 starting centres remain outside all ten receiving circles, including circles not used by the main objective.

## Input, economy and sequencing

The payment action is now explicit in EN/es-ES: after the court goal, select any living original main household currently inside that court to pay 240 food once. Every selection opportunity shares the one authored receipt. An optional civilian, another unit of the same type, a corpse, garrisoned unit or wrong-owner original cannot authorize payment. Lack of funds must remain retryable. This is a native implementation requirement, not an engine-tested interaction. It replaces the unsupported assumption that an internal payment flag provides a selectable UI object.

Stocks are copied only from the authored starting-resource vectors. Optional reserve and protected recovery stay separate. No workers, gathering, hostility or deadline are invented. The private assistance profiles therefore remain uncalibrated; splitting deliveries and pursuing optionals may provide choices, but no measured challenge or duration is asserted. The recommendation after this episode is the existing `03-shared-provision-jerusalem`; no campaign completion or progress gate is fabricated.

The same main original must belong to the dynamic court ledger and the refuge/held intersection. Final success and fresh living-original census belong in one guarded native action. The reference latch/death counterexample remains explicitly documented; this layout does not patch the global reducer.

## Historical terrain still requires a separate decision

The 340 × 340 frame and the three existing hub coordinates are preserved. The northwestern gathering and southern court/refuge are fictional activity areas in real regional geography. They are not archaeological house addresses. The existing modern DSM comparison remains a dated observation with its own earlier source pin; this binding does not relabel it as regenerated historical ground. No native elevation or approved route is assigned here.

The [IAA Stepped Street report](https://hadashot.iaa.org.il/report_detail_eng.aspx?id=26274&mag_id=135), opening and stratigraphy, records first-century segments between Siloam and the Temple Mount and separates later layers. It does not establish these western fictional paths. The [IAA Mount Zion report](https://publications.iaa.org.il/ha-esi/vol138/iss1/58/), opening and stratigraphy, distinguishes later modifications and uncertain early identifications. Neither source permits inserting the medieval upper room, modern roads or a certified end-to-end refuge route into c.30–33 CE.

Builder acceptance must require an explicit approved topographic/route decision and real native footprint inspection. In particular, the empty `map.corridors` and `nativeElevation: null` in this draft are blockers, not instructions to create a flat open map or silently reuse the coastal painter. Synthetic controller fixtures can be built independently and must retain their nonhistorical label. Game build/version, pathfinding, save/load and balance still need actual AoE2 evidence.
