# Alternative fulfillment in design dossiers

Architect: gpt-6 · 2026-10-25 · i00008/S1. Proposed decision, pending independent acceptance. This specifies a design projection; it implements neither a dossier generator nor native gameplay. The [acceptance matrix](../qa/fulfillment-dossier-projection/acceptance-matrix.json) is normative for the mechanical implementation.

## Source authority and compatibility

Use an explicit `designProfile: alternative-fulfillment-v3` branch in an authored episode blueprint. Its `referenceCapabilityProfile` is one complete, explicitly authored `CapabilityProfileV3`, validated through the existing [schema](../../packages/schemas/alternative-fulfillment.schema.ts) and [semantic validator](../../packages/gameplay-validation/scenario-capability.validator.ts). This is an internal design input, not a new campaign field or an extension of a public v2 contract. An absent discriminator follows the existing dossier path unchanged. An unknown discriminator or version fails. Never infer v3 from prose, a recipe-shaped object or a pending capability label.

The author supplies the complete shared world, objectives, states, recipe plan and secondary contracts. The projector does not invent a shared objective or import the artificial fixture's identities, coordinates or placeholder prose. Runtime fields remain exactly those accepted by the existing schema. Historical-material notes, geographic qualifications, source citations, labels, routes and screen text stay in presentation metadata outside that strict profile.

Keep the validated profile once in the generated dossier. Existing top-level views needed by the wiki and audits (`worldContract`, `objectivePlan`, `stateMachine`, `secondaryObjectives`, `secondaryBudget`) are exact derived copies of the corresponding profile fields. An audit compares them with their authority; conflicting copies fail. Fulfillment services are a separate derived view of `fulfillmentPlan`; they never become simultaneous `resource-transaction` predicates. No fixed cost is charged for an unselected recipe. No profile or blueprint is silently mutated during generation.

The current 63 legacy dossiers and their wiki/map outputs must remain content-identical. Their identity, strings, fixed-payment budgets and validation path do not acquire empty fulfillment fields. Unknown or malformed opt-in inputs cannot fall back to that legacy path. No campaign is moved to staging, no source schema is widened, and no string IDs are allocated by i00008.

## Responsibilities and data flow

1. The architect authors the profile, geography, accounts, historical/narrative material and screen bindings. The existing geographic frame helper computes hub coordinates. All IDs are supplied rather than derived from translated labels.
2. `tools/design/fulfillment-dossier.mapper.ts` parses the input with the existing v3 schema, calls `validateScenarioCapability`, and creates only deterministic design views and account analyses. Reuse core resource helpers and the existing plan-selection cost helpers; do not reproduce the reducer's reservation, observation or terminal engine.
3. `tools/design/fulfillment-dossier.script.ts` is a thin JSON stdin/stdout bridge to that mapper. One request contains the opt-in episodes for one generation pass. Successful stdout is one JSON result; failures have a nonzero exit and actionable diagnostics naming the episode and offending binding. No network, campaign mutation, ID allocation or native export occurs.
4. `tools/design/fulfillment-dossier.helper.py` invokes that bridge with an argument list and JSON stdin, without a shell. Missing Bun, invalid output or a failed schema/semantic check stops generation. It must never skip validation. The bridge result is reused by generation and verification instead of spawning a process for every recipe.
5. The existing factory/script dispatches only explicit opt-in blueprints to the new projection. Shared identity, captions, continuity, references and optional mechanics continue through existing helpers. Split common checks only where needed; do not weaken the legacy validator to make a v3 episode pass.
6. Rendering distinguishes shared preconditions, selected-service work/reception and terminal requirements. It displays finite operating stock, separate optional reserve, each recipe cost and affordable combinations. It does not use the legacy fixed-payment/gatherable-bank table for these plans.

The [world plan](../design/episode-plans/imperial-church/34-constantinople-world-plan.md) describes the present consumer. It is not a generic mapper input specification: its `workPointId` and `receptionPointId` need explicit zone bindings authored by the architect. Mapper code must not contain that campaign ID, date, religion, narrator or recipe names.

The bridge request is a strict object `{ requests: ProjectionRequest[] }`; its successful response is `{ projections: DossierProjection[] }` in the same episode order. A request has exactly these fields:

| Field | Authoritative value |
|---|---|
| `episodeId` | Existing stable selection ID; unique within the batch. |
| `referenceCapabilityProfile` | Complete existing strict `CapabilityProfileV3`. |
| `accountsByDifficulty` | Exactly easy/standard/hard, each with exactly spendable/protectedRecovery/optionalReserve and four safe integer resource amounts. |
| `mapSize` | Integer 300–400. |
| `hubs` | Unique `{id, centre:[x,y]}` records, one per profile district; finite coordinates in the existing projected frame. |
| `pointZoneBindings` | `{pointId, zoneId, hubId, offsetTiles:[x,y]}` records resolving every main-world zone exactly once. Both pointId and zoneId are individually unique. pointId names a presentation point, independently of district/hub identity. hubId must equal the bound zone's hub and offsetTiles must equal its offset exactly. Several points/zones may share one hub. Optional zones retain their own declared hub/offset. |
| `recipeBindings` | One `{serviceId, recipeId, workPointId, receptionPointId, title, goalScreenId}` per actual recipe; title has exactly nonempty EN/es-ES, point bindings must resolve the recipe's exact zones. |
| `serviceBindings` | One `{serviceId, goalScreenId, completeScreenId}` per service. These are presentation bindings, never freely writable completion facts. |
| `planScreenIds` | Exactly preview/reserved/cancelled/started/complete, each naming a supplied authored screen. |
| `screens` | The existing factory's complete screen records, with unique IDs/keys, exact EN/es-ES text, authored conditions/narrators and lossless caption segments. No caption or narrative is invented by the mapper. |

`DossierProjection` returns the episode ID, validated reference profile, its exact derived shared views, service/recipe/screen bindings and a `selectionAnalysisByDifficulty` table containing explicit recipe selections, totals, affordability and remainders. It retains all declared selection rows, including unaffordable ones, and separately lists affordable selections. The Python wrapper attaches these fields to existing historical, continuity and map metadata; it does not treat this bridge response as a whole dossier. Runtime identifiers pass through the existing ID schemas. Presentation identifiers must resolve exactly and cannot use JavaScript prototype keys. Reject unknown request fields rather than dropping them.

## Geography and identity bindings

Each referenced district has exactly one declared map hub with its existing tile centre. Each work/reception point binding resolves to one declared profile zone, with the authored hub, offset and radius. Its absolute point is that hub's centre plus the zone's offset; the radius comes from the same zone. Recipe point IDs resolve through the unique point-to-zone table, never directly through a hub name. Thus two zones in one hub remain distinct work/reception points. Reject a duplicate pointId even if it names different zoneIds, a zone bound twice, or a binding with a different hub/offset. No additional free coordinate can override the zone. A point does not become a historical parcel through that binding. Each original actor and recipe output resolves to exactly one main-world identity; all recipe cost components are preserved and expanded to the existing four-resource representation without rounding.

Presentation labels and route workloads bind by stable IDs. Reject unknown, duplicate, missing or cross-service recipe/output/recipient/zone references. Check complete work and reception circle bounds in the candidate map, including offsets, and work-versus-reception overlap in absolute tile coordinates even across different hubs. The shared v3 validator's same-hub checks are still run; the map audit adds spatial evidence rather than changing that validator. Existing corridor/shore checks remain necessary and do not become pathfinding certificates.

Use the actual seven secondary contracts from the authored profile. Do not regenerate them from their kind or substitute the artificial reference fixture. Their own identities, receiving zones, source/context bindings, costs, effects and finite funding remain intact. Profile outputs cannot be reused as optional actors or arbitrary shared predicate facts, as the existing v3 validator requires. Historical-person controls remain documentary and gameplay gates in their established layers.

## Objectives and terminal meaning

The profile's shared `objectivePlan` retains its exact predicates, dependency order and state-machine transitions. It is not a label for the complete fulfillment plan. The dossier separately binds each displayed service goal to its exact service ID, describes reserve/commit/work/generation/reception, and identifies the final fresh-presence requirement. A paid flag or a shared objective receipt cannot be displayed as service completion.

The existing reducer owns the conjunction: shared victory eligibility plus an irreversible selected commitment, all selected service receipts and a fresh living batch at the selected receiving zones; known main defeat wins. The projector neither inserts `fulfillment-complete` as a new predicate nor sets a generic victory fact. It may not move a shared objective outside the plan activation phase to manufacture an executable order. Every phase and transition is explicitly authored and checked by the existing reference behavior.

For Constantinople, the architect still must author that exact shared precondition/profile and its interaction with the service goals. The artificial fixture's meal-recipient precondition is an inspected example, not a decision automatically inherited by the historical episode. This remaining content decision blocks its full dossier, but does not block implementing a generic mapper against already explicit artificial inputs.

The presentation binds each plan, recipe, service and terminal message to authored EN/es-ES screens. Free preview, unaffordable confirmation, cancellable reservation, cancellation and irreversible start-work must remain distinguishable. Unknown screen targets or a message claiming completion at reservation fail. Caption splitting reuses the existing factory. Surface, audio, input/template and real-engine status stay pending; a storyboard does not implement a selector.

## Finite accounts and difficulty

Require explicit accounts for easy, standard and hard: `spendable`, `protectedRecovery` and `optionalReserve`, with safe nonnegative integers for all four resources. For this first design projection, no passive income, gatherable bank, replacement purchase or external resource transfer is inferred. A design needing one returns to the architect to specify supported semantics; it cannot place an unmodeled bank in presentation notes.

This first projection also rejects shared main `resource-transaction` requirements and nonzero shared `predicate.resourceAmounts`: its main cost authority is the selected fulfillment plan alone. This is an explicit mapper limitation, not a restriction added to v3. Shared nonpayment preconditions remain available. `optionalReserve` must equal `secondaryBudget.reservedRewards` component by component; `reallocatedCacheAllowance` is a descriptive allowance, never another credit. Protected recovery is reported separately and is unavailable to plan or optional payments. Cost aggregation must reject safe-integer overflow before comparing affordability.

Enumerate complete service selections under the existing v3 bounds of 8 services, 8 recipes per service and 4096 combinations. A row records exact recipe IDs, total debit, affordability and spendable remainder for each difficulty. Require at least one affordable all-skip choice in every profile. Do not sum all alternatives into `mandatoryDeliveries`, reduce protected stock to pay a choice, or include optional reward stock in the operating balance.

Use the existing finite-allocation helper for reachable optional-payment prefixes and the existing secondary budgets for costs/rewards. Adapt explicit IDs and vectors only; do not implement a second economy oracle. Check reserve conservation, reward isolation and aid-before-repair boundaries using the genuine v3 reducer in focused tests. A financial witness is not an executed route or a completed secondary. All-complete and three combinable portfolio expectations remain attached to their exact authored tasks, orders and selected choices.

The Constantinople candidate's 9/7/3 all-skip counts are regression data, not a constant of the generic mapper. The generic artificial test must also use different service/recipe counts and costs. The [allocation study](../design/episode-plans/imperial-church/34-care-allocation.study.md) remains a dated accounting source; it is not native calibration or a source of invented timings.

## Delivery boundary

i00008/S2 owns the reusable code and artificial compatibility evidence. S3 documents the resulting commands and handoff. S1 implementation instructions remain proposed until independently accepted. The full historical profile, complete dossier, historical/geographic interpretation, remaining screens and editorial pacing belong to d00002/S3. Native/UI/engine work remains i00007/S3, i00003 and s00001. No completion count or historical authoring gate changes through this infrastructure alone.

Run meaningful focused adversarial checks, compare all legacy artifacts, then `bun run validate`. `bun run test:export` is required if an eventual change affects the adapter; this proposal does not own adapter edits. Integrate via the official DelendAI gate and obtain a model-independent review. Never mark a gameplay/native/historical check passed because JSON/schema/reference tests passed.

Operational provenance: the official `create_proposal` call allocated i00008 in automatic snapshot `077a5b7`. That snapshot inherited the checkout's human Git author configuration; the call and the proposal design were made by gpt-6, not a verified human contribution. This receipt preserves the snapshot without rewriting history. Ordinary architect commits use explicit gpt-6 author identity.
