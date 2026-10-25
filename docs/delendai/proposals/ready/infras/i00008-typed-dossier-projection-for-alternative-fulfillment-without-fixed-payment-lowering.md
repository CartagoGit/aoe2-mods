---
id: i00008
title: "Typed dossier projection for alternative fulfillment without fixed-payment lowering"
kind: infra
status: ready
type: proposal
track: campaign-factory
date: 2026-10-25
---

# i00008 — Typed dossier projection for alternative fulfillment without fixed-payment lowering

## goal

Project an explicitly authored and validated composed-world-ledger v3 reference profile into design-only dossiers. Preserve exclusive recipe choice, atomic reservation, selected fresh reception, all 63 legacy dossiers, public schemas and string identities. Native support and the historical dossier remain separate gates.

## why

TODO: why this work matters now.

## non-goals

- TODO: what this proposal deliberately skips.

## slices

- global_gate: none

### S1 — Architect decision and projection acceptance contract
- **Status**: pending
- **Files**: `docs/architecture/fulfillment-dossier-projection.md`, `docs/qa/fulfillment-dossier-projection/acceptance-matrix.json`
- **Gate**: e2e
- acceptance:
  - "Define a single authoritative v3 profile with derived dossier views, exact source-to-zone mapping, shared objective versus fulfillment completion, financial proofs and immutable legacy boundary."
  - "Close responsibilities, rejection cases and mechanical implementation instructions; independent review before S2."

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
