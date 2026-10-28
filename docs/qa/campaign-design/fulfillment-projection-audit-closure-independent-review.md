# Independent review — fulfillment projection audit closure

Reviewer: `gpt-6-luna` · 2026-10-25 · d00002/S11, scoped to the added “Review closure: retained bindings and independent audit” section and the updated playstyles rule in the S2 packet, plus the new Git-authorship instruction in the MiniMax handoff.

Reviewed root commit `176b40d` against the accepted i00008/S1 decision, the ten-field `ProjectionRequest`, current v3 schema/validator and the existing reducer suite. This is a document-level review only. It does not approve S2/S11 implementation, any historical profile, or native behavior.

## Result

No inconsistency found in the requested scope.

- **One strict profile with reproducible derived views.** The handoff keeps the profile once and the five named dossier views (`worldContract`, `objectivePlan`, `stateMachine`, `secondaryObjectives`, `secondaryBudget`) as exact copies, as the ADR requires. It retains authoring presentation bindings separately from the strict profile and distinguishes those inputs from the derived projection fields. The standalone audit can reconstruct the ten request fields from episode identity, the single profile, accounts, size, screens, those retained bindings and raw map-binding fields; derived annotations such as `absoluteTile` and `radius` are expressly excluded as request inputs.
- **Flat retention avoids a second profile copy.** Follow-up `2e6e76e` makes every projection field a top-level episode field, requires field-by-field comparison against the revalidated projection, and explicitly forbids a nested `bridgeDossierProjection` or duplicate profile. This resolves the open question about how the projection is retained without weakening the one-profile rule.
- **Audit checks derived service data, not just matching IDs.** The closure requires reprojecting through the same typed bridge and optional helper, then comparing service recipe costs, workers, outputs, recipients, zones, map bindings, selection rows/remainders and optional prefix analysis. The already verified batch result is passed into the audit during generation, avoiding a second bridge process per episode; a standalone audit makes one reconstructed projection. Missing source authority or a failed projection diagnoses the dossier instead of skipping checks.
- **Reducer evidence and mapper coverage stay separate.** The unchanged reference suite still contains the 95-path selected-output/terminal matrix (`tests/alternative-fulfillment/reference/alternative-fulfillment.test.ts`). The packet reuses that evidence instead of copying those paths into each mapper test. Its new end-to-end composer test uses a complete valid artificial request through the real bridge and checks that edits to derived service output and financial rows are caught. The 34-case design specification remains unchanged, and actual executed coverage is to be reported separately; none of this text claims those new tests have already passed.
- **Playstyles have meaningful distinct portfolios.** Every optional-objective list is nonempty, contains unique IDs from the actual secondary contracts, and the three unordered ID sets differ regardless of cost wording. This matches the existing dossier audit's nonempty/known-ID/unique-set checks and prevents empty or prose-only portfolio variants.
- **Git author and agent attribution remain separate.** The handoff directs future commits to retain the configured Git author `Cartago`, forbids model-name Git overrides and history rewrites, and keeps `DELENDAI_AGENT_ID`, the DelendAI unit/session and its audit as the model attribution path. The checked worktree's configured Git identity is `Cartago <cartago.relaxingcup@gmail.com>`, consistent with the instruction.

## Limits

Read-only inspection; no tests or heavy validation run. No S11 or S2 verdict was recorded.
