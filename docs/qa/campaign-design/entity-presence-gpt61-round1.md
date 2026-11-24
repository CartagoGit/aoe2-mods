# i00005/S1 — independent reference review

Reviewer: gpt-6.1-sol. Implementer confirmed by runtime: gpt-6-sol. Own official review unit g6, session19150587. Reviewed integrated source58e376deb9e1c69f9ef35bbfef36015a69647890; incorporated integrated submit8c55de534460c859c5f187bc6ccd4274d92075fb (proposal metadata only). Runtime S1=in_review, S2/S3 pending. No implementer files edited.

## P1 — unproduced identity satisfies presence

`packages/gameplay-state/live-entity-presence.helper.ts:107` counts observed identities without `generationReady`. Profile declares custodian-1 as an output of derived-token producer.derive. The profile validates with zero diagnostics. Without any derive-token action or producer fact, a fresh complete batch including custodian-1 lets return latch. requirementFacts contains only return.first-receipt. Existing record-arrival and other entity observers explicitly require generationReady, so the new predicate bypasses the existing causal contract. This admits an uncreated receipt/token placeholder as a present original.

Reproduce: `bun /tmp/gpt61-i00005-generated-repro.ts`. Expected: unproduced identity cannot count (or incompatible source rejected). Actual: diagnostics[]; objectiveLatches[return]; no producer.derive fact. Add mixed-profile regression and preserve normal originals/quorum, produced-token and generated receipt behavior.

## P1 — invalid batch suppresses deadline defeat

`packages/gameplay-state/capability-state.reducer.ts:74` returns immediately on an invalid/stale batch unless defeatConditions explicitly nonempty. Automatic phase-deadline expiry is evaluated only later in tick. Valid profile adds deadline10s (warning2) to phase-1. At now11, plain tick defeats. Same tick with a duplicate-identity spatial batch returns the nonterminal pre-tick state. Deadline defeat therefore loses priority solely because optional new observation is malformed.

Reproduce: `bun /tmp/gpt61-i00005-invalid-deadline-repro.ts`. Actual: diagnostics[]; deadline plain=defeat; invalidbatch=null. Reject the batch atomically while retaining independent clock/defeat processing; do not turn invalid membership into fresh positive evidence. Test duplicate and stale inputs at the deadline, including a previously positive observation and latched objective.

## Checks and limits

Own frozen install and bun run validate exit0:99/99 tests,357 expectations; docs and campaign validation pass. Log /tmp/gpt61-i00005-validate.log. Existing tests do not cover either cross-contract reproduction above. Inspected strict schema/structural validator/compiler integration, observer replacement semantics, irreversible destruction, fresh latch/tick/enter-phase guards, snapshot shape/fingerprint and ADR0005. Invalid batch cannot directly reuse saved positive positions for latch/victory because the attempted action returns; a later latch/victory also needs fresh input. Partial accepted batches replace membership and omit unknowns; six-of-eight quorum is supported.

Native composed v2 remains unsupported; no historical, geographic, native, game or balance approval. Acceptance1 causal presence and acceptance2 defeat priority are not met for the cases above; changes requested.

## Formal result and export limitation

Official proposal_review request_changes succeeded: S1=changes_requested, reviewer=gpt-6.1-sol, implementer=gpt-6-sol; verdict commit252f2dc313aae775be2fbb58b88f6eecea02b1a9. Restored only automatic unrelated f00003 R100 rename, same body, commit612451a. Net review diff changes only i00005 proposal metadata.

Own `bun run test:export` exit1: Python environment lacks AoE2ScenarioParser (ModuleNotFoundError), before any export work. No previous author toolchain/venv exists here. Log /tmp/gpt61-i00005-export.log. Thus3variants/2roundtrips remains implementer-reported evidence, not my execution. Read TypeScript native-campaign.renderer and Python export_aoe2 guards: composed profile2 explicitly rejects capability-not-implemented. This environmental export failure is not itself a candidate code finding.


Archived reproductions: [unproduced identity](entity-presence-generated-reproduction.md), [deadline rejection](entity-presence-invalid-deadline-reproduction.md). Original temporary paths in the report describe the review session; the linked Markdown preserves that evidence after temporary files expire. Formal changes request integrated in62ec0d4.
