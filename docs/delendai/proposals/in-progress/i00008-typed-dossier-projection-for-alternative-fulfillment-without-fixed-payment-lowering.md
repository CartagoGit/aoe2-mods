---
id: i00008
title: "Typed dossier projection for alternative fulfillment without fixed-payment lowering"
kind: infra
status: in-progress
type: proposal
track: campaign-factory
date: 2026-10-25
last-transition-id: 230e7a4c-2ea0-4980-af53-65eefdf955fc
last-correlation-id: 230e7a4c-2ea0-4980-af53-65eefdf955fc
last-transition-from: ready
last-transition-at: 2026-10-25T01:26:46.091Z
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
- **Status**: review
- **Files**: `docs/architecture/fulfillment-dossier-projection.md`, `docs/qa/fulfillment-dossier-projection/acceptance-matrix.json`
- **Gate**: e2e
- acceptance:
  - "Define a single authoritative v3 profile with derived dossier views, exact source-to-zone mapping, shared objective versus fulfillment completion, financial proofs and immutable legacy boundary."
  - "Close responsibilities, rejection cases and mechanical implementation instructions; independent review before S2."
- review-state: in_review
- review-implementer: gpt-6

### S2 — Reusable opt-in projection, validation and rendering
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `tools/design/fulfillment-dossier.mapper.ts`, `tools/design/fulfillment-dossier.script.ts`, `tools/design/fulfillment-dossier.helper.py`, `tools/design/episode_dossier.factory.py`, `tools/design/episode_dossier.validator.py`, `tools/design/episode_dossiers.script.py`, `tools/design/render.py`, `tools/design/test_design.py`, `tests/unit/fulfillment-dossier.test.ts`
- **Gate**: e2e
- acceptance:
  - "Reuse capabilityProfileV3Schema and validateScenarioCapability. Keep exact authored recipes, identities, costs and lifecycle; reject unknown mappings/versions, drift between views, unsupported semantics or simultaneous fixed-payment lowering."
  - "Use artificial fixtures and adversarial tests for affordability, cost/reserve isolation, zones, outputs, terminal gates and truthful evidence. Verify all legacy dossier/wiki/map outputs unchanged."
  - "Run focused tests and bun run validate, then independent review and official publication. No native adapter, shared schema, historical content, ID or string-lock changes."

### S3 — Design pipeline integration and handoff
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `docs/architecture/overview.md`, `docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md`, `docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md`, `docs/qa/fulfillment-dossier-projection/independent-review.md`
- **Gate**: e2e
- acceptance:
  - "Document concrete commands, source authority, version dispatch and failure behavior without historical dossier-count changes."
  - "Keep full historical dossier in d00002/S3 and native/UI/engine evidence in i00007/S3, i00003 and s00001; no historical authoring unlocked by infrastructure alone."

## acceptance

- Define a single authoritative v3 profile with derived dossier views, exact source-to-zone mapping, shared objective versus fulfillment completion, financial proofs and immutable legacy boundary.
- Close responsibilities, rejection cases and mechanical implementation instructions; independent review before S2.
- Reuse capabilityProfileV3Schema and validateScenarioCapability. Keep exact authored recipes, identities, costs and lifecycle; reject unknown mappings/versions, drift between views, unsupported semantics or simultaneous fixed-payment lowering.
- Use artificial fixtures and adversarial tests for affordability, cost/reserve isolation, zones, outputs, terminal gates and truthful evidence. Verify all legacy dossier/wiki/map outputs unchanged.
- Run focused tests and bun run validate, then independent review and official publication. No native adapter, shared schema, historical content, ID or string-lock changes.
- Document concrete commands, source authority, version dispatch and failure behavior without historical dossier-count changes.
- Keep full historical dossier in d00002/S3 and native/UI/engine evidence in i00007/S3, i00003 and s00001; no historical authoring unlocked by infrastructure alone.
