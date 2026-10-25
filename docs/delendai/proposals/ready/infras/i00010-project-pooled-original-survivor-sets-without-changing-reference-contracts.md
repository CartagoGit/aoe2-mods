---
id: i00010
title: "Project pooled original survivor sets without changing reference contracts"
kind: infra
status: ready
type: proposal
track: campaign-factory
date: 2026-10-25
---

# i00010 — Project pooled original survivor sets without changing reference contracts

## goal

Let the existing design factory express one survivor pool across multiple authored original object groups, preserving public v2 survivor semantics and all current outputs. Close architect decisions before delegating the mechanical mapping.

## why

Jerusalem70 deliberately has eight original household identities in four two-person origin courts, with any six surviving required. The existing public v2 survivorGroupSchema and reference loss evaluator already accept an arbitrary explicit entity set, but world_and_objectives currently projects every authored survivor row through exactly one group key. A real artificial four-group source with groups:[west,east,south,central], minimum6 raises KeyError('group'). Four per-court minima, moving everyone to one origin or omitting impossible-threshold defeat would change the intended design and are unauthorized. This is a source projection requirement, not a new native capability. S2 must follow accepted i00009/S2 because both touch the same factory/runner; never claim those files concurrently.

## non-goals

- No public scenario/capability schema, profile version, campaign/episode identity, actor identity or string-range change.
- No duplicate/generated/replacement original actors, party aliases in the engine, per-court minima, or weaker final presence/loss rule.
- No historical dossier insertion, native export/observation, game evidence or broad generic grouping DSL.

## slices

- global_gate: type

### S1 — Architect pooled-original mapping decision and closed packet
- **Status**: review
- **Files**: `docs/architecture/pooled-survivor-projection.md`, `docs/handoffs/POOLED-SURVIVOR-PROJECTION-PACKET.md`
- **Gate**: type
- acceptance:
  - "Specify a strict internal choice of one existing group or a nonempty unique groups array, stable flattening of already generated main IDs, valid positive minimum no greater than unique pool size, and explicit diagnostics for malformed/unknown/duplicate inputs, with real artificial reproduction."
  - "Keep unchanged public reference loss/current-presence contracts, actor origins and identity, legacy output, external i00009/S2 serialization requirement, no historical authorization and independent verification boundaries."
- review-state: in_review
- review-implementer: gpt-6

### S2 — Implement strict survivor projection and verify the existing loss reference
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `tools/design/episode_dossier.factory.py`, `tools/design/test_pooled_survivor_projection.py`, `tools/design/test_design.py`, `docs/qa/pooled-survivor-projection/acceptance.md`
- **Gate**: type
- acceptance:
  - "After i00009/S2 is independently accepted and integrated, reuse existing group-ID generation and strict numeric primitives to project exactly one survivor row for any declared group union. Do not create or relocate an actor, invent a group alias in public output, or modify any runtime/public schema."
  - "Use real artificial factory output plus existing strict dossier/reference validation to test four groups of2 pooled at minimum6, unchanged single-group output, malformed/unknown/duplicate groups and minimum types/bounds; verify existing death logic tolerates2original losses and defeats on3 regardless of the origin court, with required defeat before possible victory."
  - "Preserve all64 current dossiers,2645screens,398secondaries,49reference records, existing generated artifacts/native rejection and IDs; run targeted/design/bun validation, record independent review and native/game/history limitations without authoring a historical campaign."

## acceptance

- Specify a strict internal choice of one existing group or a nonempty unique groups array, stable flattening of already generated main IDs, valid positive minimum no greater than unique pool size, and explicit diagnostics for malformed/unknown/duplicate inputs, with real artificial reproduction.
- Keep unchanged public reference loss/current-presence contracts, actor origins and identity, legacy output, external i00009/S2 serialization requirement, no historical authorization and independent verification boundaries.
- After i00009/S2 is independently accepted and integrated, reuse existing group-ID generation and strict numeric primitives to project exactly one survivor row for any declared group union. Do not create or relocate an actor, invent a group alias in public output, or modify any runtime/public schema.
- Use real artificial factory output plus existing strict dossier/reference validation to test four groups of2 pooled at minimum6, unchanged single-group output, malformed/unknown/duplicate groups and minimum types/bounds; verify existing death logic tolerates2original losses and defeats on3 regardless of the origin court, with required defeat before possible victory.
- Preserve all64 current dossiers,2645screens,398secondaries,49reference records, existing generated artifacts/native rejection and IDs; run targeted/design/bun validation, record independent review and native/game/history limitations without authoring a historical campaign.
