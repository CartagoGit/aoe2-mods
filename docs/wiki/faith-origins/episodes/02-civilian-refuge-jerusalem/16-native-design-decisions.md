# When the City Held Its Breath: native design decisions

Architect: gpt-6, 27 October 2026. Campaign identity remains `faith-origins`, **Embers of the Covenant**. This is the existing second selected episode, **When the City Held Its Breath / Cuando la ciudad contuvo el aliento**, c. 30–33 CE. These are concrete decisions for a future source amendment and bounded native packet; no second scenario is implemented by this document. The first Caesarea prototype can be played independently while this work continues.

## Historical event, fiction and narrator

The common narrator attributes a retrospective report to Tacitus. [Annals 15.44](https://dcc.dickinson.edu/tacitus-annals/15-44), paragraph 3, places Christus's execution under Tiberius and Pilate. It does not date the year or describe these families, a refuge journey, a safe road or a specific relief organization. The chosen date is an approximate editorial reconstruction. Tacitus's hostile religious language is the source author's perspective, not the voice or conclusion of the common narrator.

The neutral opening distinguishes that report from fictional household logistics, then hands over to the same campaign narrator, **Miriam of Caesarea / Miriam de Cesarea**. She speaks retrospectively from inherited accounts. Her personal focus here is the gap between an archival number and the same living people needing food at another destination. She cannot remember a first-century event or authenticate the fictional household names. Keep her existing biography and life dates; do not introduce another persona or make her the playable relief organizer.

All 39 paired EN/es-ES screens remain the source inventory. Preserve the order fact-intro → handover → persona-intro and the historical-license notice. Main reactions refer to those households and the one receipt; the factual outro keeps the attested execution separate from local success. The ending recommends the actual next selected episode 03. This is not a campaign ending, a new campaign intro or a progress permission gate. Do not place later canonical books as first-century cargo.

## Identity semantics closed by the architect

Use eight original household representatives, alternating the existing male/female civilian proxy types. One proxy represents one fictional household for gameplay; it does not claim to count every historical family member. Keep all eight stable original IDs and the source's six-of-eight survival margin. Nine optional bodies are separate from those eight: two aid, two copy, one repair store, one trader, one guide and two visiting households. Neither an optional body nor a new unit of the same type can replace a main original.

The **court ledger is dynamic and cumulative**, not frozen when the first six qualify. Any original household that reaches the court later can become eligible for the final delivery. This is the actual existing reference behavior, not a newly invented native rule. All eight may qualify; the player chooses which six or more survive and complete both receipts.

The selected arrival semantics record a visit while the original is alive, not simultaneous presence or mandatory continued residence. Earlier visits remain facts across phases. A prior final-refuge visit may later count once that same identity is in the court ledger and the main payment is complete. Do not invent an unexpressed after-payment departure, force the first six as a permanent cohort or silently require all six to stand together. If a later design wants those rules, author them explicitly with supported departure/presence operations first.

There is a real liveness gap in the current dossier: six historical refuge arrivals can include two subsequently destroyed people while two other originals keep the global survivor count at six. Root's chosen correction uses an **existing** requirement, without modifying schemas or global reducer semantics:

- Preserve `o3/req-1`, its destinations and its reference to the `o1/received-households` ledger.
- Append `o3/req-2`: `entity-state`, state `alive-and-held`, the same eight originals and final destinations, `requiredCount=6`, `oncePerEntity=true`, and the same eligible ledger.
- The host records the held fact for an original observed alive on a final arrival. At evaluation, eligibility, that identity's recorded arrival, held fact and non-destroyed state must intersect. Two unrelated living originals cannot repair this count.
- This does not promise current presence or physical detention. A living original may leave the circle after delivery. A destroyed original cannot count as alive, even though its historical receipt remains.

Luna checked the pattern on an artificial valid v2 profile: after six deliveries, destroying two leaves the historical-arrived predicate true and the proposed alive-and-held predicate false. That is reference evidence for an existing primitive, not a compiled historical episode or a native test. The exact proposed requirement and twenty-one prospective cases are in [the matrix](17-native-acceptance-matrix.json). **The requirement is not yet inserted in the source.** Source materialization must preserve previous IDs, regenerate the affected dossier, and receive independent review before the new compiler accepts this episode.

The additional requirement is checked **when its objective is evaluated**. It is not an automatic fresh terminal guard in the global reference reducer: a host can latch o3, process two deaths, then tick with the surviving global group still at six. The objective latch alone can remain sufficient for reference victory. Do not claim req-2 fixes that API gap globally.

The bounded native host must therefore use **one guarded XS invocation** for the final commit. It checks ready/phase/payment, original ownership and living counts, and each qualifying original's court-arrival/refuge-arrival/held facts using fresh native state. If irrecoverable loss is true it commits defeat first; otherwise it needs six currently living qualifying originals before writing both the final objective latch and terminal success in that same invocation. There is no intermediate action, timer or caption phase between the fresh test and the terminal write. Captions run after the terminal. Save/load cannot restore an exposed “o3 latched but terminal undecided” native state. A future generic host wishing to allow that gap needs its own explicit terminal freshness design; this document does not silently patch the reducer or make that promise.

Three original household losses before the terminal latch defeat the mission; two may be tolerated if the remaining six qualify. Evaluate that loss before final success. Arrivals do not immunize a body against subsequent destruction. Close all available secondary transactions when the main terminal commits.

## Payment, actions and resources

The mandatory payment remains one atomic **240 food** receipt after the court goal. Reuse the actual native payment helper; never debit a partial amount or borrow protected recovery. For the later physical binding, select the named court payment flag to authorize it. That marker is a UI surface, not a ninth main household, a source witness or an extra survivor requirement. A missing native selection/control operation must be reported, not emulated by an automatic timer or unstated payment trigger.

Easy/standard/hard starting food is 402/350/297. Subtracting 240 leaves 162/110/57 without optional income. The optional payments total 50 wood and 50 gold; starting wood 172/150/127 and gold 86/75/63 cover both. Reserved optional payouts remain 550 food, 200 wood and 25 gold; recovery and replacements stay separate and unimplemented until actual capability exists.

Preserve six optional circuits and their assigned identities:

| Circuit | Player decision and effect | Closure needed before native work |
|---|---|---|
| Unlisted neighbors | Deliver each of two original aid bearers to its own court; one 100 food/50 wood reward. | Separate physical approaches from the main court. |
| Names on two scraps | Bring both original records to the western copyist; historical context and a hint. | Name the fictional labels plainly, not as surviving ancient documents. |
| Refuge store roof | Authorize 50 wood on the original store; full repair and one 200 food/100 wood payout. | Store placement must not obstruct a receiving circle. Reuse full-HP capture, not a guessed HP constant. |
| Olive road trader | Arrive with the original trader, then authorize 50 gold; one 150 food/50 wood payout. | Replace the generated repeated “trader of ... trader” label with a task-specific EN/es name in the binding. |
| Ridge road guide | Escort the original guide; reveal an already authored alternate route. | The source's “surveyed” wording overstates present geometry. Neither candidate below is certified. |
| Two visiting households | Deliver both optional households to their separate western reception point; one 100 food/25 gold payout. | The destination is hub-1, not the southern main refuge. Rename its player instructions “western guest reception / recepción occidental de visitantes”; do not silently relocate IDs or count these as main families. |

All losses are local to the corresponding optional circuit. Keep consent to repair/trade, failed-payment retry and persistent once flags. None requires a hidden optional reward to fund the main goal.

This second quiet civilian episode teaches original-group intersection and loss margins after the first episode's unique-copy provenance. It has no authored hostile roster or secret deadline. Existing worker caps 12/9/6 and duration estimates are not placed workers or measurements. Retain honest prototype difficulty labels; food/vision differences alone are not proof of a satisfying hard mode. The next gameplay calibration must establish whether split groups, detours, route information and aid rewards have strategic value before the opening act is accepted as balanced.

## Geographic decision and measured comparison

The current 340 × 340 frame is regional: bbox [35.12,31.70,35.30,31.86], with all three existing fictional hubs retained for inspection. Hub-1 at [35.218,31.791] is an exterior northwestern gathering point in this plan; it is **not an excavated western-city neighborhood**. Amend its description to “Northwestern household gathering / Reunión de hogares del noroeste” before physical delegation. Do not paint a complete first-century residential quarter there. Hubs 2 and 3 are fictional receiving/refuge points in the southern hinterland, not excavated safe houses.

The archived modern DSM was checked by SHA-256 and sampled at all hubs: approximately 803.09 / 763.51 / 688.52 metres of **modern surface**. Buildings and vegetation are included. These are not first-century ground levels or AoE2 elevation assignments.

The [new comparison](18-modern-surface-route-comparison.json) records exact candidate points, tile projection, distances and all modern samples; the [figure](18-modern-surface-route-comparison.png) is a standalone scientific plot. The existing straight chain is about 5.42 km / 92.03 tiles. Hypothetical western main and relief alternatives measure about 5.76 km / 97.81 tiles and 7.95 km / 135.10 tiles. They preserve geography instead of moving hubs to conceal a crossing. These are **comparison candidates only**: many adjacent modern samples have steep differences, which may include buildings or terrain. No route is approved from this calculation.

Archaeological controls read for the decision:

- [IAA Stepped Street, 2023](https://hadashot.iaa.org.il/report_detail_eng.aspx?id=26274&mag_id=135), opening and stratigraphy: first-century street segments connect the Siloam area southward/northward toward the Temple Mount; destruction in 70 and later phases are distinct. This is not evidence for the fictional western corridor.
- [IAA Mount Zion, 2026](https://publications.iaa.org.il/ha-esi/vol138/iss1/58/), conclusions and cited staircase research: a local first-century stepped connection from Hinnom is discussed with qualifications. It does not certify an end-to-end refuge route or identify the present medieval building as a first-century shelter.
- [IAA Wilson's Arch/Great Causeway, 2011](https://hadashot.iaa.org.il/report_detail_eng.aspx?id=1738), W5006 and phase table: an earlier retaining/road structure and probable bridge are distinguished from later second/third-century rows of arches. Do not copy the complete later causeway or treat the presumed 33 CE damage as a certain scenario event.

No IAA figure/photo is copied. The existing Wilson 1865 map is dated comparison only. Keep the western ridge, Hinnom, the City of David ridge and Kidron distinct. Do not create a navigable Kidron, fill a ravine to force connectivity, invent a bridge, or import later walls, sanctuaries and streets.

**Map gate still open:** compare steep intervals with dated topography and ground evidence, choose actual on-map footprints/approaches and inspect native pathfinding. The two source corridors currently share a hub chain; claiming that the guide reveals a surveyed alternate route is premature. No worker is authorized to infer the missing ancient streets or turn either comparison candidate into approved terrain.

## Next bounded deliveries

1. Materialize only the source amendments above using existing factories: append o3/req-2, clarify cumulative arrivals/held semantics, change the exterior gathering label and optional guest-reception wording, and qualify the “surveyed” route text. Preserve campaign, episode, object, zone, existing requirement and receipt IDs.
2. Source hash changes affect the first episode binding because it pins the full campaign source file. Revalidate that episode 01 is byte-equivalent as an object; update its binding source hash explicitly without modifying the immutable private artifacts or attributing their old hashes to a new build. Regenerate the affected source audit through its owning unit; never weaken hash validation.
3. Close the native geographic binding with actual footprint and route evidence. Keep unresolved geometry visible rather than assigning it to MiniMax as a guess.
4. Extend the native implementation in a bounded new task: reuse original-handle spatial predicates, payment/optional reserve helpers, shared base, caption queue and optional circuits. Separate household ledger orchestration from the Cesarea copy-provenance controller; do not copy the full exporter or claim the public composed profile is implemented.
5. Independently review, build six variants and add the new mission to a private progressive container only after source/native checks pass. Preserve the independently playable first episode and exact artifact identities. Actual engine and difficulty observations remain their own evidence.

Catalogue totals remain 64 drafts / 214 missing / 2,645 paired screens / 398 secondary contracts / 50 reference records. These decisions, prospective cases and the figure are not a new dossier, registered reference, native mission or historical approval.
