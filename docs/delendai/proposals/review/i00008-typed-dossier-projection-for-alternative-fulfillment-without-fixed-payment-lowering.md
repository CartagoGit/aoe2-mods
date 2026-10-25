---
id: i00008
title: "Typed dossier projection for alternative fulfillment without fixed-payment lowering"
kind: infra
status: review
type: proposal
track: campaign-factory
date: 2026-10-25
last-transition-id: 5f7f5a37-b8d1-4cb3-90cc-efcdcfef8a55
last-correlation-id: 5f7f5a37-b8d1-4cb3-90cc-efcdcfef8a55
last-transition-from: in-progress
last-transition-at: 2026-10-25T13:24:20.246Z
shipped-in:
  - "11fcf956f31981af2d04f0d6aebf327b96d14e20"
  - "6f06737db6dfd3ccc2251e375398c5c2201eb4cb"
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
- **Status**: review
- **DependsOn**: [S2]
- **Files**: `docs/architecture/overview.md`, `docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md`, `docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md`, `docs/qa/fulfillment-dossier-projection/independent-review.md`
- **Gate**: e2e
- acceptance:
  - "Document concrete commands, source authority, version dispatch and failure behavior without historical dossier-count changes."
  - "Keep full historical dossier in d00002/S3 and native/UI/engine evidence in i00007/S3, i00003 and s00001; no historical authoring unlocked by infrastructure alone."
- review-state: in_review
- review-implementer: gpt-6-luna

## acceptance

- Define a single authoritative v3 profile with derived dossier views, exact source-to-zone mapping, shared objective versus fulfillment completion, financial proofs and immutable legacy boundary.
- Close responsibilities, rejection cases and mechanical implementation instructions; independent review before S2.
- Reuse capabilityProfileV3Schema and validateScenarioCapability. Keep exact authored recipes, identities, costs and lifecycle; reject unknown mappings/versions, drift between views, unsupported semantics or simultaneous fixed-payment lowering.
- Use artificial fixtures and adversarial tests for affordability, cost/reserve isolation, zones, outputs, terminal gates and truthful evidence. Verify all legacy dossier/wiki/map outputs unchanged.
- Run focused tests and bun run validate, then independent review and official publication. No native adapter, shared schema, historical content, ID or string-lock changes.
- Document concrete commands, source authority, version dispatch and failure behavior without historical dossier-count changes.
- Keep full historical dossier in d00002/S3 and native/UI/engine evidence in i00007/S3, i00003 and s00001; no historical authoring unlocked by infrastructure alone.
