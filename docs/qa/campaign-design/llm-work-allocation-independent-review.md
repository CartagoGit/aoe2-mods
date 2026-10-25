# Independent review — LLM work allocation and S2 packet

Reviewer: gpt-6-luna  
Reviewed root-authored scope at candidate `a6419e6` (integrated into this review unit at `b24a4d7`):

- `docs/handoffs/LLM-WORK-ALLOCATION.md`
- `docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md`
- `docs/handoffs/FULFILLMENT-DOSSIER-S2-PACKET.md`
- The i00008/S2 `Files` addition to its proposal, naming `tsconfig.json`.

This is a scoped document review. It does not approve S11 as a whole or the six Luna-authored onboarding/handoff documents present in the same candidate.

## Findings

The initial candidate had one non-blocking wording gap: it attributed empty optional dependencies only to the accounting helper, although the existing `validateSharedScenarioCapability` already rejects every side objective with nonempty `dependencies` (`capability.secondary-optional`). Architect commit `83560f4f0a378deceb648cf2ee8130d192bb63e5` corrected the packet to require preserving that existing validator rejection and separately state that the helper has no dependency scheduler. I confirm the finding is closed; it needs no schema or validator change.

I found no remaining discrepancy within the requested scope. The implementation limitations describe a design projection and do not imply that code, native behavior, a historical dossier or game verification already exists.

## Cross-check evidence

- The nine `docs/design/odysseys/*.json` selections sum to 278. Their authored episode arrays contain 63 complete design drafts; those arrays contain 2,594 screens and 391 secondary objectives. The 215 remaining selections are not full dossiers. This matches the stated 30/34/30/32/32/30/28/32/30 selection distribution. The auxiliary Constantinople plan is separately identified and excluded from these totals.
- `civic-difficulty-mechanical-audit.json` records 54 `staticRiskCandidates` across the 63 drafts. Its label and risk rule are mechanical candidates, not engine or balance failures; the handoff preserves that distinction.
- `docs/design/geography.json` has 26 profiles; the research `reference-manifest.json` contains 47 local resources. The repository's geography coverage notes record 22 distinct missing geographic IDs affecting 25 selections (`docs/research/odyssey-research/README.md`, `docs/production/plan.md`). The four Hijaz DSM crops are modern terrain evidence and the four named profiles remain absent from the canonical registry; the text does not call them historic terrain or playable maps.
- The staging campaign files each declare 17 locales with `draft` status. The route-pilot text inventory has 43 entries: 36 `s2-materialize` and seven `native-pending-documentary-only`. The work-allocation/queue docs attribute implementation to gpt-6-luna, distinguish the seven documentary intents, and state that MiniMax's earlier HTTP 429 produced no work. I found no claim that MiniMax implemented or reviewed this S2.
- Live DelendAI status confirmed f00001/S2 `done`, implementer `gpt-6-luna`, reviewer `gpt-6`, acceptance 3/3; it confirmed i00008/S1 `done`, reviewer `gpt-6-luna`, acceptance 2/2. The checked-in handoff distinguishes these formal statuses from the pending i00008/S2 mapper and the unintegrated Constantinople candidate; it does not call either a dossier 64 or native support.
- The i00008 proposal change only adds `tsconfig.json` to S2 `Files`. `tsconfig.json` currently includes packages, CLI and tests, but not `tools/design/**/*.ts`; the S2 packet confines the intended change to adding that tree while preserving existing includes/options. No schema, state-machine, S1 acceptance, package, adapter or campaign contract is changed by this planning edit.
- In the S2 packet, `optional_states(stock, optionals)` accepts explicit costs/rewards and does not validate or constrain IDs. The older `resolved_inputs`/`build_report` path imposes ASCII hyphen IDs and preset `COSTS`/`REWARDS`, so the instruction not to route arbitrary v3 IDs or authored vectors through those presets is accurate. The proposed bounds match the helper constants and guard: 12 optionals, 65,536 combined analysis states, in addition to the existing v3 8-service/8-recipes/4,096-selection limits. Extracting at most one atomic-payment cost and one finite-supply-withdrawal reward per side, and rejecting resource-bearing effects outside that supported financial shape, avoids silently dropping authored economics. These are projection constraints; the v3 schema is not changed.

The three retained root documents were reviewed for consistency only. The six Luna-authored documents in the candidate are outside this report's approval scope. No test suite was run; root owns the combined validation gate. This report makes no S11-wide approval claim.
