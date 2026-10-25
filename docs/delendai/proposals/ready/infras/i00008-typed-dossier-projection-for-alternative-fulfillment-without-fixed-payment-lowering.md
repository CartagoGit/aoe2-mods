---
id: i00008
title: "Typed dossier projection for alternative fulfillment without fixed-payment lowering"
kind: infra
status: ready
type: proposal
track: campaign-factory
date: 2026-10-25
last-transition-id: cec1b74b-0cb3-486d-9063-abcc51d6e1d9
last-correlation-id: cec1b74b-0cb3-486d-9063-abcc51d6e1d9
last-transition-from: review
last-transition-at: 2026-10-25T13:31:10.522Z
shipped-in:
  - "11fcf956f31981af2d04f0d6aebf327b96d14e20"
  - "6f06737db6dfd3ccc2251e375398c5c2201eb4cb"
  - "c5533f777dfb7e0f9c9c76157109725aa5288ed8"
---

# i00008 — Typed dossier projection for alternative fulfillment without fixed-payment lowering

## goal

Project an explicitly authored and validated composed-world-ledger v3 reference profile into design-only dossiers. Preserve exclusive recipe choice, atomic reservation, selected fresh reception, all 63 legacy dossiers, public schemas and string identities. Native support and the historical dossier remain separate gates.

## why

The existing dossier factory derives budgets from fixed resource-transaction requirements. The independently reviewed v3 reference retains exclusive recipes and atomic joint reservation, while the Constantinople world plan remains outside the complete-dossier pipeline. A reusable typed projection is needed before a mechanical implementer can materialize that design without replacing its choices with simultaneous fixed debits. This infrastructure can proceed against artificial inputs while the architect completes the historical profile.

## non-goals

- No change to public campaign/profile/snapshot schemas, existing v2 behavior, campaign identity, string locks or progress keys.
- No native renderer, selection UI, cargo, terrain/pathfinding, audio or engine implementation; those remain separately gated.
- No automatic authoring or approval of a historical dossier, no campaign generation/distribution, no translation approval and no game-balance claim.
- No second reference reducer, accounting engine or DelendAI queue. Reuse existing validators, helpers, state transitions and the connected work runtime.

## slices

- global_gate: none

### S1 — Architect decision and projection acceptance contract
- **Status**: done
- **Files**: `docs/architecture/fulfillment-dossier-projection.md`, `docs/qa/fulfillment-dossier-projection/acceptance-matrix.json`
- **Gate**: e2e
- acceptance:
  - "Define a single authoritative v3 profile with derived dossier views, exact source-to-zone mapping, shared objective versus fulfillment completion, financial proofs and immutable legacy boundary."
  - "Close responsibilities, rejection cases and mechanical implementation instructions; independent review before S2."
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6-luna
- review-log: approved by gpt-6-luna — verified at 11fcf956f319, validate exit 0 and tests 142/142 claimed, no recorded run cited; acceptance 2/2: (1) Reviewed architecture and acceptance matrix; they define one strict v3 source, derived views, exact zone/point bindings, separate shared and fulfillment termin… (2) Responsibilities, bridge shape, failure handling, unsupported semantics and S2 gate are explicit; confirmed S1 only and implementation remains pending. — Independent design review on integrated 11fcf956. bun run validate exited 0: 142/142 tests, 2069 expectations. The 34 S2 matrix cases remain specified-not-executed; this approves S1 design only, not mapper implementation, S2, native, or gameplay.
- shipped-in: `11fcf956f319`

### S2 — Reusable opt-in projection, validation and rendering
- **Status**: done
- **DependsOn**: [S1]
- **Files**: `tools/design/fulfillment-dossier.mapper.ts`, `tools/design/fulfillment-dossier.script.ts`, `tools/design/fulfillment-dossier.helper.py`, `tools/design/episode_dossier.factory.py`, `tools/design/episode_dossier.validator.py`, `tools/design/episode_dossiers.script.py`, `tools/design/render.py`, `tools/design/test_design.py`, `tests/unit/fulfillment-dossier.test.ts`, `tsconfig.json`
- **Gate**: e2e
- acceptance:
  - "Reuse capabilityProfileV3Schema and validateScenarioCapability. Keep exact authored recipes, identities, costs and lifecycle; reject unknown mappings/versions, drift between views, unsupported semantics or simultaneous fixed-payment lowering."
  - "Use artificial fixtures and adversarial tests for affordability, cost/reserve isolation, zones, outputs, terminal gates and truthful evidence. Verify all legacy dossier/wiki/map outputs unchanged."
  - "Run focused tests and bun run validate, then independent review and official publication. No native adapter, shared schema, historical content, ID or string-lock changes."
- shipped-in: `6f06737db6df`
- review-state: done
- review-implementer: gpt-6-luna
- review-reviewer: gpt-6
- review-log: approved by gpt-6 — verified at 6f06737db6df, validate exit 0 and tests 157/157 claimed, no recorded run cited; acceptance 3/3: (1) Independent source review of 9c20f205 integrated at6f06737; strict schema/semantic reuse, exact selected service views, retained binding re-projection, drift/u… (2) 15 mapper tests and Python bridge cases plus independent valid-boundary and after-funding probes; existing general reducer tests retained. Direct comparison ag… (3) Reviewer independent bun run validate exit0:157tests/13files,2134expectations; source report a311e43 integrated. Official product6f06737 passed installation/va… — Independent reviewer gpt-6 approves only integrated S2 infrastructure6f06737; implementer gpt-6-luna. Report docs/qa/fulfillment-dossier-projection/independent-review.md. 157tests passed independently; no native/historical/game approval.

### S3 — Design pipeline integration and handoff
- **Status**: done
- **DependsOn**: [S2]
- **Files**: `docs/architecture/overview.md`, `docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md`, `docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md`, `docs/qa/fulfillment-dossier-projection/independent-review.md`, `tools/design/civic_difficulty_audit.script.py`, `tools/design/test_civic_difficulty_audit.py`, `tests/unit/fulfillment-dossier.test.ts`, `docs/design/civic-playability-acceptance.md`, `docs/handoffs/LLM-WORK-ALLOCATION.md`, `docs/production/plan.md`, `README.md`
- **Gate**: e2e
- acceptance:
  - "Document concrete commands, source authority, version dispatch and failure behavior without historical dossier-count changes."
  - "Keep full historical dossier in d00002/S3 and native/UI/engine evidence in i00007/S3, i00003 and s00001; no historical authoring unlocked by infrastructure alone."
  - "Dispatch the global civic audit on the explicit v3 designProfile using authored accounts, selection views and enemyRoster; reject malformed or unknown data, preserve exact legacy report data and all historical source/artifact counts, and prove compatibility through the genuine artificial composed fixture."
- review-state: done
- review-implementer: gpt-6-luna
- review-reviewer: gpt-6
- review-log: requested_changes by gpt-6 — S3 has no delivered implementation: the proposal-level transition for S2 also marked pending S3 review. Request S3 changes before integration: concrete accepted S2 handoff commands/status and compatible global civic audit. Reproduced using an uninserted composed51-screen/seven-secondary temporary preview: civic_difficulty_audit.script.py::episode_audit raises KeyError('accessibleWithoutOptionalRewards'). Preserve current63/215 counts and all public/native contracts. Architect closed packet will govern a Files-scoped amendment; no legacy field emulation, no historical insertion.
- review-log: resubmitted by gpt-6-luna — resubmitted; answers the request above: Implemented the opt-in civic audit dispatch and S3 handoff. Strict composed-world-ledger schema/profile and resource-vector checks; fixed legacy episode baseline; actual composed artificial fixture; focused and full validation pass. Independent review report a6d3e81 merged. Legacy 63-row report bytes preserved; no historical/native/game approval.
- review-log: requested_changes by gpt-6.1-sol — Fresh independent review: P2 exact difficulty/selection view guard at civic auditor line206 accepts difficulty-only True or 1.0 where authored account and selection analysis contain integer1 because Python equality aliases bool/float/int. Independently reproduced both using existing v3_episode fixture. Validate duplicate difficulty with type-sensitive equality or equivalent strict checks; add both regression cases. Other scoped implementation and handoff coherent. Independent 14 Python and full bun run validate exit0:157tests/13files/2136assertions,3campaigns. Report docs/qa/fulfillment-dossier-projection/fresh-global-audit-review.md. No historical/native/game approval.
- review-log: approved by gpt-6 — verified at c5533f777dfb, validate exit 0 and tests 157/157 claimed, no recorded run cited; acceptance 3/3: (1) Integrated S3 handoff documents explicit opt-in, bridge/composer/audit commands and fail-closed behavior; source remained 63 legacy episodes in this infrastruc… (2) Handoff and code preserve native rejection and content gates; no historical insertion, public schema, campaign identity or native adapter changes. (3) 15 independently passing Python tests cover actual composed artificial fixture, unknown/malformed cases, selection and duplicate-view bool/float/NaN drift, and… — Independent correction review of integrated c5533f777dfb7e0f9c9c76157109725aa5288ed8. GPT-6.1 finding answered by c8bd0a9: type-sensitive complete-view canonical JSON comparison rejects bool/int/float drift and NaN, accepts key reorder. Independently executed 15 Python tests and full validate (157 tests, 2136 assertions, 3 campaigns) on exact source; publication gate passed. Reports global-audit-independent-review.md and fresh-global-audit-review.md retained. No historical/native/game approval.

## acceptance

- Define a single authoritative v3 profile with derived dossier views, exact source-to-zone mapping, shared objective versus fulfillment completion, financial proofs and immutable legacy boundary.
- Close responsibilities, rejection cases and mechanical implementation instructions; independent review before S2.
- Reuse capabilityProfileV3Schema and validateScenarioCapability. Keep exact authored recipes, identities, costs and lifecycle; reject unknown mappings/versions, drift between views, unsupported semantics or simultaneous fixed-payment lowering.
- Use artificial fixtures and adversarial tests for affordability, cost/reserve isolation, zones, outputs, terminal gates and truthful evidence. Verify all legacy dossier/wiki/map outputs unchanged.
- Run focused tests and bun run validate, then independent review and official publication. No native adapter, shared schema, historical content, ID or string-lock changes.
- Document concrete commands, source authority, version dispatch and failure behavior without historical dossier-count changes.
- Keep full historical dossier in d00002/S3 and native/UI/engine evidence in i00007/S3, i00003 and s00001; no historical authoring unlocked by infrastructure alone.

## S3 bounded integration amendment — 25 October 2026

Root reproduced the remaining global civic-audit failure after successful temporary v3 composition: KeyError(accessibleWithoutOptionalRewards). The [closed packet](../../../../handoffs/FULFILLMENT-DOSSIER-S3-PACKET.md) defines the explicit reporting branch, legacy invariance and exact handoff work. Files add only that internal auditor, its existing regressions and status documentation. No public/runtime contract, selected episode, ID range or historical content changes. The global transition accidentally queued S3 for review alongside S2; the independent request-changes action records its undelivered state. This amendment does not alter the accepted S1/S2 verdicts.
