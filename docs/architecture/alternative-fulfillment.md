# Alternative fulfillment: architect decision

18 October 2026 · gpt-6 · i00007/S1 · architect-authored decision; official acceptance is tracked in DelendAI and the independent report. This document specifies a reusable capability. It does not implement a selector, payment reservation, actor generation, native UI or the Constantinople dossier. No current campaign, public schema, snapshot format, string reservation or progress key changes in S1.

## Decision and inspected implementation

Choose an explicit, opt-in successor of the composed capability profile for **joint selection of alternative service recipes**. Preserve the existing source envelope and all existing profile/snapshot-v2 behavior. A reservation is a resource transfer into an unavailable escrow, followed by either cancellation before work or one irreversible commitment. Selected work has recipe-qualified identities and receipts. Funding does not complete the work.

The source inspected at integrated base `216c033e` is listed with hashes in the [inspection record](../qa/alternative-fulfillment/decision/source-inspection.json). This is project-source inspection; no fresh claim about external engine/editor APIs follows.

| Existing facility | Reuse | What it cannot currently supply |
|---|---|---|
| [Resource helpers](../../packages/gameplay-state/resource-accounts.helper.ts) | Normalize, compare, debit and credit finite resource vectors | They do not own reservation identity, selection or escrow |
| [Fixed main payment](../../packages/gameplay-state/capability-state.reducer.ts) | Its phase, once-only and insufficient-stock discipline informs the new transaction | `pay-main` debits one fixed requirement irreversibly; its paid flag cannot mean a cancellable joint reservation |
| [Composed predicates](../../packages/schemas/scenario-capability.schema.ts) | Existing entity/receipt/presence/work predicates remain building blocks | The objective operator is `all`; supplying nine fixed payments does not create nine exclusive alternatives |
| Route choice | Keep accumulated campaign route behavior unchanged | The route predicate requires campaign progress keys, and cannot represent local funding or refundable selection |
| Derived identity and departure helpers | Reuse causal eligibility and unique output discipline where their actual contracts apply | An unselected recipe, refunded reservation or wrong attempt cannot authorize an output through a convenient old payment flag |
| Live presence / checkpoint | Reuse fresh monotonic observations and intermediate-only release semantics | An arrival history or checkpoint is not final living-recipient presence |
| [Native renderer](../../packages/aoe2-adapter/native-campaign.renderer.ts) / [Python exporter](../../tools/python/export_aoe2.py) | Preserve explicit unsupported-capability rejection | Composed export is currently rejected; no native selection/reservation operation was found |

Rejected approaches: reinterpret `choose-route`; replace alternatives with several fixed debits; set generic predicate facts to claim work; edit a v2 receipt after refund; or let a selected JSON label stand in for generated cargo, a building owner or a player's input. They would change existing semantics or hide unsupported operations.

The economic study is the concrete reproduction, not the only possible consumer. Finite supply packages, alternate work methods and mutually exclusive local service arrangements need the same general transaction. The new operation must not know campaign, religion, city, date or narrator.

## Compatibility boundary selected for S2

S2 is to define an explicit **profile v3 / snapshot v3 opt-in**, keeping the scenario source envelope at version 1. The existing `composed-world-ledger` v2 profile and snapshot stay literal, strict and byte-compatible for existing inputs. No existing campaign is migrated. The new profile composes shared primitive schemas, validators, resource helpers and causal/presence logic; it must not clone the reference engine or silently add optional fields to the approved v2 contract.

V3 is a versioned capability contract, not a repair to v2 content. S1 creates no schema literal, serializer, migration or action dispatcher. S2 must include the reviewed v3 design, a compatibility ADR implementation note, prior fixtures and before/after fingerprints. Unknown versions and unknown fields fail. V2 snapshots cannot acquire an empty escrow by inference, and v3 snapshots cannot be loaded under a v2 contract. Neither format is native game JSON.

New reference actions must be explicitly dispatched by the selected profile version. Their conceptual names below are specification terminology, not callable operations available today. Existing actions and snapshots retain their previous interpretation. Unimplemented profile/native support continues to fail; merely parsing v3 in S2 must never imply native support in S3.

## Immutable authoring inputs

The first successor profile supports exactly one joint plan per scenario; there are no parallel nested reservations or multiple-plan scheduling in this capability. A plan has a stable `planId`, activation phase, ordered service IDs, and finite alternative recipes per service. Each recipe declares its own ID, whole nonnegative cost vector, exact input/output identities, work prerequisites, receiving zones and completion requirements. Each service selects exactly one of its own recipes. Costs are computed from that immutable registry; the input command never supplies a trusted cost, credit, refund or paid flag.

A joint selection contains every required service exactly once. Reject omitted, duplicate, unknown or cross-service recipe IDs, unsupported account types, invalid/safe-integer-overflow amounts and cyclic work/derivation dependencies. Recipe work cannot depend on an output of an unselected alternative. Ordinary shared workers may be reused in sequential tasks only when the declared prerequisites and actual movement permit it; a single actor never occupies two separated zones in one observation.

Main costs draw only from spendable stock. Protected recovery and the finite optional reward reserve remain separate. A reservation creates no income; recipe costs cannot be negative and this first capability has no resale or refund-bonus feature. Optional tasks retain their own existing paid/reward receipts and funding source. Reserving, previewing or cancelling a plan is never a secondary reward trigger.

Structural enumeration limits in the current Python study are authoring-analysis limits, not a claim that the engine supports that many branches. S2 must bound supported structures; S3 additionally proves the actual target's integer resource representation, trigger/variable/UI budgets and performance. Fractional or otherwise unrepresentable native stock cannot be rounded, truncated or silently treated as an integer observer value. It remains unsupported until an explicit compatible representation is certified. No native gathering/economy support follows from the current fixed-integer study.

## Lifecycle and atomicity

A single plan permits at most one irreversible committed attempt. Before that point the player may edit a free draft and reserve/cancel different complete attempts. There is one active attempt at a time, one persistent monotonic attempt counter, and a revision for reservation lifecycle changes. Stale counters/revisions reject without mutation. A cancelled attempt cannot be revived; a fresh reservation uses the next counter. Safe-integer exhaustion rejects further reservations rather than wrapping. Retain bounded current-attempt state and the one eventual commitment, not an unbounded log of cancelled drafts.

| Operation | Preconditions | Entire atomic result |
|---|---|---|
| Preview/edit | Active nonterminal scenario; declared services/recipes | Show costs, actual available stock, remainder, work and recovery policy. No debit, escrow, output, receipt or completion fact |
| Reserve complete plan | Correct contract fingerprint, phase and next attempt; no active reservation/commit; exact complete selection; expected spendable balance equals current balance; full cost affordable | Debit the total once from spendable; credit the identical escrow; store selected IDs and current attempt/revision. No work or payment-completion receipt |
| Cancel | Exact current reserved attempt/revision; no commitment | Return that escrow once to spendable, clear escrow, close the attempt and advance revision. No output or work receipt; rewards earned independently meanwhile are preserved |
| Commit work | Exact current reserved attempt/revision; all selected input identities are eligible and living in a fresh observation; no main defeat/terminal condition | Consume the complete escrow once, create one immutable commitment with exact per-recipe shares and full total, advance revision and enable only selected work. No service is completed or output automatically created |
| Perform selected work | Correct committed attempt and recipe; actual declared prerequisite observations and causal receipts | Record only that recipe's qualified work/output facts, once. Physical movement, generation and reception remain distinct supported operations |
| Complete service | Its selected work, exact output reception and its required fresh living-recipient observations hold | Latch a service receipt qualified by contract, plan, attempt and recipe. It never authorizes another alternative |
| Cancel/change after commitment | Any committed or completed state | Reject unchanged. No refund, selection change or output replacement |
| Duplicate/stale operation | Repeated attempt, cancelled attempt, old revision, wrong recipe or duplicate receipt | Reject or return the identical state; never debit, credit, create output or latch again |

The reserve command includes an expected spendable vector from the displayed preview. If an optional debit/reward or another legitimate resource change occurs first, the controller refreshes the preview and asks for the player's explicit confirmation against the new balance. It must not auto-select a cheaper recipe, borrow escrow, substitute another currency or guess that a stale confirmation still reflects the player's intent. A plan lifecycle revision alone cannot detect changes to the spendable balance.

All selected services commit together. There is no partial reservation, per-service cancellation or post-work refund in this first operation. The compiler derives the per-recipe shares from the same total transfer: later service receipts do **not** debit those shares again. A zero-cost recipe still needs a valid selected attempt and explicit commitment; `enough(0)` is not permission to generate an output repeatedly.

The state keeps spendable, escrow and committed expenditure distinct. For each resource, the initial total of spendable + protected recovery + optional reserve equals their current balances + current escrow + committed main expenditure (both these selected commitments and any other declared fixed main payments) + paid optional expenditure, assuming no separately declared external transfer. Optional rewards transfer from their finite reserve into spendable. Cancellation transfers escrow back, not a newly computed price or the whole starting budget. This equation is an acceptance invariant, not a claim that the current reducer implements escrow.

## Terminal ordering, failures and recovery

An authoritative observation batch resolves known main defeat before accepting a reservation, commitment, service completion, reward or victory from that batch. Missing/unknown/stale living-input observations cannot be positive proof. Reference entry-to-terminal and tick-to-terminal paths must enforce the same rules.

Before commitment, a mistaken draft or unaffordable confirmation changes nothing; a funded mistaken plan can be cancelled. If a required original input is lost before commitment, the plan cannot commit. The author must state whether the scenario has another viable main path or is irrecoverably defeated. Do not convert a lost original into a new similarly named actor.

After commitment, material expenditure is irreversible. An incorrect position can be repaired by moving the same eligible living identity to the right destination. A missing observation can be recovered with a new actual batch. A destroyed unique required output or original recipient is a main failure in the minimal technical fixture. The generic capability does not resurrect it, refund spent work or switch recipes automatically. A campaign seeking finite physical recovery must author and separately certify its exact source, cost, identity and bounds before promotion; S1 grants none by prose.

Optional-only loss closes only that optional task. It cannot kill the main scenario, award its promised stock or satisfy a main recipe. All-skip must have at least one genuinely executable main plan at every difficulty.

At terminal the whole scenario becomes immutable, including its resource balances. A reservation that had not committed stays recorded as **unspent escrow**, frozen in the terminal snapshot; no output is authorized and no automatic refund/reward runs after defeat. A committed attempt stays spent. Victory requires commitment and all selected service/final-presence requirements, so a merely reserved plan cannot win. The final report distinguishes escrow from expenditure. Restarting the scenario creates a new complete initial world; loading a save restores the whole recorded world, not selected ledger fields.

## Concrete artificial identity fixture

These IDs are normative **technical fixture** identities under `fulfillment-fixture.*`. They are not new campaign IDs, string allocations, named historical people, geographic parcels or a completed Constantinople world. The fixture must be outside playable historical campaigns.

Common original inputs are `fulfillment-fixture.meal-worker`, `fulfillment-fixture.shelter-worker`, `fulfillment-fixture.meal-recipient`, `fulfillment-fixture.household-a` and `fulfillment-fixture.household-b`. Both households remain the same original identities across all shelter alternatives. Every common input is initially living; recipients cannot be substituted. Each main worker is distinct. Optional identities have their own namespace and cannot fill these roles.

| Service / selected recipe | Exactly one eligible output | Declared prerequisite work before output eligibility | Required physical reception |
|---|---|---|---|
| Meal / direct | `fulfillment-fixture.meal-direct-parcel` | Selected commitment, original meal worker at `meal-direct-source` | Output and original meal recipient at `meal-reception` |
| Meal / shared-hearth | `fulfillment-fixture.meal-hearth-parcel` | Selected commitment, original meal worker at `hearth-worksite`, then its qualified work receipt | Output and original meal recipient at `meal-reception` |
| Meal / purchased | `fulfillment-fixture.meal-purchased-parcel` | Selected commitment, original meal worker at `merchant-worksite`, then its qualified work receipt | Output and original meal recipient at `meal-reception` |
| Shelter / materials | `fulfillment-fixture.shelter-materials-parcel` | Selected commitment, original shelter worker at `materials-source` | Output and both original households at `materials-court` |
| Shelter / local-kit | `fulfillment-fixture.shelter-kit-parcel` | Selected commitment, original shelter worker at `kit-worksite`, then its qualified work receipt | Output and both original households at `kit-court` |
| Shelter / rented | `fulfillment-fixture.shelter-arrangement-parcel` | Selected commitment, original shelter worker at `host-worksite`, then its qualified work receipt | Output and both original households at `host-court` |

In this minimal technical fixture, work is a fresh post-commit arrival of the original assigned worker at its declared source/work zone, observed against the committed attempt after an authorized departure. That observation creates the qualified work receipt; it is not a freely writable fact or a receipt inferred from the payment. No processing duration, cooking simulation, repair effect or cargo inventory is implied. The corresponding selected output may become available only afterward. This deliberately small fixture tests causal identity; it does not specify the final historical episode's workload or establish its interest.

All short zone names above expand to `fulfillment-fixture.<name>`. Their geometry and native placement belong to the S2 artificial reference fixture and S3 engine fixture, not an ancient map. Every source/work zone must be separate from receiving zones; their full footprints and observation membership cannot make an initial placement count as work or delivery.

The six output IDs are declared once and unavailable until their own selected commitment and work prerequisites. A compliant generation backend makes each selected output available once; moving an arbitrary preplaced actor or setting a boolean is insufficient. No unselected output becomes eligible. Cancellation never makes output actors available, because no work/output begins before commitment. A parcel is an abstract identified gameplay consignment, not an implementation of an unmodeled carried-resource inventory. The arrangement parcel is a technical receipt object; it transfers neither ownership nor beliefs.

The completion predicate is **all services**, where each service requires **only its selected recipe**, qualified by the same committed attempt. Meal reception uses the exact chosen meal output and the meal recipient. Shelter reception uses the exact chosen shelter output and both original households at that recipe's court. Final victory requires a single fresh batch with all those selected outputs and original recipients alive at their respective required destinations. No historical arrival, alternative output, old batch, generic predicate or earlier intermediate latch can substitute. Outputs are not consumed in this minimal fixture. If a future design consumes goods, it needs explicit consumption semantics instead of impossible final presence.

## Save/load and input boundary

Persist contract fingerprint, version, difficulty, phase, spendable/escrow/other accounts, current attempt counter and lifecycle revision, exact selection, status, committed shares and qualifying work/output/service receipts with the complete world state. The v3 fingerprint must cover the complete immutable plan, recipe costs, input/output identities, work and reception prerequisites as well as the shared world/objective/state-machine semantics. The existing v2 fingerprint omits the new plan and cannot be reused unchanged for v3. Changing even one selected cost or destination must invalidate a saved v3 state. Keep the v2 fingerprint itself unchanged.

Validate identity membership, totals, uniqueness and lifecycle/account consistency on load; do not infer missing data or recompute a refund from current content. A mismatched contract or corrupt escrow rejects before mutation.

Persisted receipts are tied to their attempt; an old recipe's payment cannot unlock a different recipe after reload. Re-entry does not reserve or commit again. Saving immediately before and after reserve, cancel, commit, output creation, service completion and terminal is required. Loading an earlier legitimate save rolls back the entire timeline, including world outputs and resource sources; this design does not promise an external anti-rollback ledger.

Drop stale UI/native input queued across load and rebuild the preview from the restored snapshot. Historical observations may remain recorded, but only a new authoritative post-load observation of the restored world can satisfy new living-input, work or final-presence checks. Do not renumber a cached observation to make it fresh. The eventual native controller must prove that behavior; lifecycle counters do not by themselves identify an input from a discarded timeline. Save/load must preserve the actual engine world and the matching reference state, not merely a JSON field containing `selected=true`.

The player interaction protocol is preview → explicit reserve → visible cancellable reservation → explicit start-work. Every displayed step states the full two-service cost, stock, remaining work and cancellation boundary in EN/es-ES. This is a semantic UI requirement, not a claim that AoE2 has a custom modal/menu API. S3 must bind it to an actual supported input/template mechanism, disclose that concrete mechanism and certify it in the game. If that cannot be done faithfully, the capability stays rejected and the architect revises the design. Campaign progress variables cannot emulate this local protocol.

## Acceptance and implementation ownership

The [decision cases](../qa/alternative-fulfillment/decision/decision-cases.json) are hand-authored review examples with expected resource states, not an executable gameplay DSL, implementation or game evidence. The existing finite-allocation study remains a separate accounting oracle for 9/7/3 affordability and optional payment prefixes. It proves neither escrow nor the physical fixture above.

S2 implements the accepted reference contract/compiler and negative native gate using shared modules, with strict validation and adversarial tests. Required cases include complete/partial/mixed choices, stale previews, duplicate reserve/cancel/commit, zero cost, overflow, wrong attempt, generation causality, current final presence, protected-stock isolation, finite optional rewards, terminal priority and both terminal APIs. Existing v2 fixtures and fingerprints must remain unchanged. No unrestricted write-predicate or direct resource-credit escape hatch may satisfy the new capability.

S3 depends additionally on i00003 native composition, actual template/input support and s00001 engine evidence. It supplies native round-trip, xs-check where applicable, `bun run test:export`, and AoE2 runs with exact build/hash/profile/locale. Test reserve/cancel/start-work on the same game tick as optional payments, death and terminal events; pre-start commands, repeated clicks, every save boundary, queue restoration, native resource precision and output identity. Native limits must reject unsupported plans rather than approximate them.

The historical dossier remains d00002/S3 and f00003/S37, owned by the architect. Before MiniMax: complete actual geography, distinguish physical workloads, prove all-skip/all-complete/three combinable portfolios at each difficulty, write all original identities and EN/es screens, and obtain historical/technical/game reviews. The proposed capability cannot make a menu plus empty walking into a good RTS episode. None of the 215 selection-only episodes becomes a full dossier through this decision.
