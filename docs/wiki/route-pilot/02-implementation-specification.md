# Route laboratory: bounded implementation specification

Architect: gpt-6, 2026-10-24. f00001/S1 specification, awaiting independent review. This document and the [closed text inventory](15-text-inventory.json) complete the [brief](00-brief.md). Neither is a game test. Fictional technical fixture; no historical source, ancient geography or authentic testimony is claimed.

## Assignment boundary and files

S1 owns this wiki directory only. After independent review, official integration and formal S1 acceptance, MiniMax's next mechanical assignment is f00001/S2: `staging/campaigns/route-pilot` and `staging/campaigns/route-successor`. S2 must produce both complete source bundles, all seventeen draft catalogues and honest media provenance, then pass both staging checks without `--partial`. No `campaigns/`, lock, glossary, adapter, schema or historical dossier edits in S2. S3 alone owns joint promotion and ID allocation. S4 records real evidence. The live server decides readiness; this document cannot clear a dependency.

Preserve schemaVersion1. Reuse `campaign.schema.ts`, the existing scenario compiler and the native exporter rather than creating a pilot framework. No composed v2/v3 capabilityProfile is required. Follow `docs/guides/staging.md`. Keep descriptive filenames; no index.ts or barrel modules. Required bundle structure is `campaign.json`, the declared `scenarios/<scenario-id>/scenario.json`, plus actual licensed media if any. Do not invent extra source JSON fields to represent this specification's tables.

| Fixed property | T01 | T02 |
|---|---|---|
| Campaign id | route-pilot | route-successor |
| Public/internal identity | CDF-T01 / CDF_RoutePilot | CDF-T02 / CDF_RouteSuccessor |
| Source locale / campaign status | en / fixture | en / fixture |
| Scenario id | 01-route-choice | 01-recap |
| Scenario title namespace | scenario.route-pilot-choice | scenario.route-successor-recap |
| Campaign narrator | route-observer | route-archivist |
| Source recommendedPrevious | [] | []; optional predecessor is a static introduction line; adaptive layout pending |
| enforceRequirement | false | false |
| Date/location | Fictional technical laboratory / Artificial plain | Same |

Both use the collection-narrator for factual framing, then explicitly hand over to their separate fictional campaign narrator. The observer is curious, practical and concise; the archivist is patient, careful about uncertainty and speaks about records rather than offering the observer's invitation to choose a path. Neither is a historical witness or cloned voice. No extra named character is permitted. The on-map guard is an unnamed technical unit, not a third speaking character. Factions/buildings/ram labels in the inventory are UI labels, not persons.

## Exact candidate maps

Both maps are32×32, start(6,16), grass-1, elevation0, no blocked cells, water, resources, walls, gates, decorations, reinforcements or production. This deliberate laboratory exception does not change the large historical-map policy. All positions are candidate placement until native footprint and path checks pass.

T01: human faction `player`, player1, byzantines; enemy faction `targets`, player2, byzantines. This civilization is a technical representation without ethnic/religious inference. Unit `guard` uses catalog type `militia` at(6,16), essential=true. The word guard is its permanent scenario ID and displayed role, not an invented engine unit type or historical hero. Rams `ram-north` and `ram-south`, type `battering-ram`, at(8,14)/(8,18), essential=false. Enemy buildings `target-a`/`target-b`, catalog building type `castle`, at(24,8)/(24,24), essential=false. No garrison, rebuild, extra unit, starting technology upgrade or content-authored attack-order trigger. The legacy exporter nevertheless generates cdf-react-<difficulty>-targets for enemy factions without aiScript and includes task_object effects for both castles toward map.start. Do not claim this trigger is absent. Its building behavior is unverified; ENG25 explicitly tests it and reports an infrastructure mismatch if necessary. Keep the guard in the western start area; the player chooses which castle the rams approach. The castles' normal defensive fire remains engine behavior, not a scripted wave or measured balance result.

T02: the same artificial frame; one nonessential `observer-marker`, type `militia`, human player1 byzantines at(6,16), no opponent, buildings or movement objective. The marker is not a speaking character. Test that this empty opposition setup does not produce an unintended auto-victory; an engine refusal is an infrastructure finding, never an excuse to add an invented adversary silently.

All factions have finite-reserve economy, all four initial resources0, no production, no reinforcements and reserve equal to their actual finite initial unit count. All three difficulty profiles use zero resource vectors, enemyReactionSeconds1 and hints=true. No difficulty changes the route/progress oracle. This is an interface experiment with intentionally identical profiles, not an odyssey balance example. Native default AI/economy must be inspected: zero resources and no workers prohibit authored production but do not by themselves certify AI inactivity.

## Objectives, terminal and persistence

T01 ordered objective definitions: `prepare`, timer1second, requires[]; `destroy-a`, destroy target-a, requires[prepare]; `destroy-b`, destroy target-b, requires[prepare]. All are kind=main. `victory.objectives=[prepare]`. Ordered `victory.routes` is exactly:

```json
[
  {"id":"route-a","objectives":["destroy-a"],"progressKey":"progress.route-pilot.route-a"},
  {"id":"route-b","objectives":["destroy-b"],"progressKey":"progress.route-pilot.route-b"}
]
```

Do not also require both destroy objectives globally. No scenario-wide `victory.progressKey`; each selected route writes its own permanent key. Defeat: essentialUnits[guard], timeoutSeconds900, arbitration=defeat-first. No other loss defeats. A lost ram can make this tiny test unwinnable; reload/restart is explicit, with no free respawn or claimed recovery economy. This is acceptable for the disposable laboratory and not a historical mission design pattern.

Logical oracle: while terminal=open, check required loss/timeout first. If defeated, commit terminal=defeat and write neither route. Otherwise complete eligible objectives and choose the first satisfied route in the fixed A,B order. Commit one victory and only that route's progress=1. Never write0 to either key. If both targets fall in the same evaluation before terminal, A wins; B remains available by replay. If A has already won, later destruction cannot write B in that run. A prior B flag is retained when A wins, and conversely. Exported trigger order expresses this policy; only the linked engine matrix can certify its actual same-tick/persistence behavior. Do not claim a new reference reducer implements these legacy route rules.

The1second prepare is a technical dependency test. Destroyed-before-prepare must still count after prepare; no timer may stand in for destruction. Timeout is a test window, never a historical event. Saving/restoring before and after each terminal must neither erase accumulated profile progress nor invent a second completion. Progress keys are locale-independent and are not string IDs or local objective variables. The local cdf-terminal guard is not a cross-campaign save database.

T02 has one main objective `finish-recap`, timer10seconds, requires[]. `victory.objectives=[finish-recap]`, routes[], no progressKey, essentialUnits[], arbitration=defeat-first and no timeout. It never writes, clears or repairs predecessor keys. Its10seconds refer to active scenario time from load, not an invented post-caption relative clock. The full campaign recap belongs before scenario start in the native presentation. Scenario intro is one short factual reminder only; do not try to fit every recap branch into ten seconds of gameplay or pause the timer with an unsupported operation.

## Recap truth table and screens

Read both predecessor keys independently. Use exactly one branch; missing is different from a read failure. Only known successful reads permit the first four rows.

| Read result | A | B | One branch |
|---|---:|---:|---|
| success | absent/0 | absent/0 | recap-missing |
| success | 1 | absent/0 | recap-a |
| success | absent/0 | 1 | recap-b |
| success | 1 | 1 | recap-both |
| unavailable/error | any | any | recap-unknown |

Common factual introduction → explicit handover → campaign persona → predecessor recommendation (T02) → one sufficient recap → scenario briefing. Every branch explains the previous two routes well enough to start here. No forced launch, hidden prerequisite, disabled button or mandatory prequel. Read failure supplies the neutral summary; it does not overwrite profile data. At T01 completion recommend T02 by title and public ID; replay remains optional. At T02 completion return to the menu, without advertising a nonexistent third lab.

The [text inventory](15-text-inventory.json) is the closed EN/es-ES source for S2. The earlier [screen contract](14-screen-contract.md) describes the intended surfaces; the inventory supplies missing schema labels and precise wording. Each scenario title, objective, unit/faction name, required message and line uses one listed semantic key. Titles are not voiced. Do not create duplicate text keys for repeated factual copy. Exactly36 keys are materialisable in S2;7 native-conditional intentions remain documentary only, excluded from all runtime catalogues until a real capability exists. The inventory marks the split per key. Supply all17 configured locales for the36 representable keys with draft review state; EN/es-ES entries must exactly match their inventory values. Other translations must be actual text, not English copied under a translated locale. No locale or voice is approved by a validator.

Static source narrative/outro must remain valid independently of native conditional presentation: T01's source outro uses the generic `campaign.route-pilot.victory`; T02's source outro uses its generic victory. Do not place both route-specific victory strings in an unconditional outro. Route-specific victory screens and the mutually exclusive recap require a real, accredited native conditional layout. Keep their7 intended strings in this documentary inventory, outside the S2 bundle/catalogues. Unreferenced catalogue entries fail validation; unbound narrative.events fail game.event-unbound. Do not evade either check by playing all branches unconditionally or inventing inert event lines, a source condition union or a template operator. The source fixture has a static sufficient predecessor summary in its introduction and no adaptive recap. Its complete source bundle does not certify the intended adaptive UI.

The required T01 scenario `narrative.intro` reuses `campaign.route-pilot.fact`, with `collection-narrator` as speaker. Keep that factual line in `campaign.introduction` too; the two line records have distinct IDs and the same textKey. This deliberately repeats the existing short fictional-laboratory notice at scenario entry, without adding a string or copying the full campaign introduction. T02 keeps its separately inventoried `scenario.route-successor-recap.intro`. See the [binding amendment](17-briefing-binding-amendment.md).

## Native capabilities and media boundaries

The current legacy exporter creates guarded ordered victory triggers and store-key-value effects (`tools/python/export_aoe2.py`). The current native campaign renderer binds real templates; it does not synthesize a conditional SequenceItems layout or supply a progress-read UI operator. recommendedPrevious can describe only one endingKey per record; it cannot encode the two-key missing/error truth table here. Therefore both source fixtures explicitly use recommendedPrevious=[]; T02 retains its optional predecessor recommendation in ordinary introduction text. Do not turn a single-key metadata warning into an alleged two-route check. Template identity, branch expressions, read-error handling, presentation timing and engine behavior remain dependencies of i00003/S4 narrative/progress and s00001 compatibility/template work. S1 closes the design decision, not those capabilities. A source bundle may be reviewed with that dependency explicit; native candidate/production remains blocked until real template evidence exists. Reuse an existing infrastructure proposal if it owns the missing operation; do not emulate it in campaign content.

No generated audio or downloaded art is required to close the S1 specification. In S2 prefer no optional assets over invented paths/hashes. If a required schema/media surface needs bytes, use a small original deterministic map diagram or local licensed recording with exact hash, author, license and restrictions; no mass paid generation. Missing native slides/audio remain explicit production limits. No synthetic voice means no claim of a dubbed campaign. Never reuse unlicensed game screenshots or package historical images for this fictional map.

## Delivery sequence and feedback loop

First MiniMax delivery is one closed ready slice, reviewed before the next starts. Its packet must cite the exact integrated S1 commit, live slice, allowed paths, inventory, acceptance commands and known native dependencies. MiniMax reports actual model/provider, own DelendAI unit/session/claim, commit, checks and failures. The architect reviews source conformity, naming/reuse, localisation, map/oracle fidelity and real limitations. Defects return to the same slice with concrete reproduction; record a reusable instruction only when evidence shows the need. Passing validation does not automatically approve content or grant broader scope.

Architect work continues in parallel on history, geography, narrators, alternative objectives, economics and independent review. Each historical episode can enter the mechanical queue after its own design/source/map/capability prerequisites are approved and the official proposal permits it; completion of all nine odysseys is not a blanket prerequisite. A dossier count is not such approval. Global locks (string IDs/glossary) remain serialised at materialisation, even with parallel authors.

On2026-10-24 the attempted MiniMax-M3.1-Flash OpenCode launch was rejected before any tool work with HTTP429/2056, Token Plan usage limit. The separate mmx OAuth quota query reported0% weekly general quota. This is a provider blocker, not a DelendAI rejection or a completed MiniMax delivery. The architect owns this S1 specification; do not attribute it to MiniMax. Retry the bounded assignment after the provider permits it, without changing provider/model, buying credits or increasing task scope automatically.
