---
id: i00010
title: "Project pooled original survivor sets without changing reference contracts"
kind: infra
status: in-progress
type: proposal
track: campaign-factory
date: 2026-10-25
shipped-in:
  - "6e3bbf51e05337dc054750bffed00f456805bc68"
  - "d86c561303916d658394b560030875fa045991b6"
last-transition-id: 082c6ac1-d366-414d-8240-38812e493540
last-correlation-id: 082c6ac1-d366-414d-8240-38812e493540
last-transition-from: ready
last-transition-at: 2026-10-26T02:23:23.654Z
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
- **Status**: done
- **Files**: `docs/architecture/pooled-survivor-projection.md`, `docs/handoffs/POOLED-SURVIVOR-PROJECTION-PACKET.md`
- **Gate**: type
- acceptance:
  - "Specify a strict internal choice of one existing group or a nonempty unique groups array, stable flattening of already generated main IDs, valid positive minimum no greater than unique pool size, and explicit diagnostics for malformed/unknown/duplicate inputs, with real artificial reproduction."
  - "Keep unchanged public reference loss/current-presence contracts, actor origins and identity, legacy output, external i00009/S2 serialization requirement, no historical authorization and independent verification boundaries."
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6-luna
- review-log: approved by gpt-6-luna — verified at 6e3bbf51e053, validate exit 0 and tests 157/157 claimed, no recorded run cited; acceptance 2/2: (1) The decision and packet define mutually exclusive group/groups selectors; reject missing, wrong-type, empty, duplicate, unknown and overlapping identities; pre… (2) The documents retain the two-field dossier projection and public schema/reducer, preserve all actor IDs/origins, require i00009/S2 before shared-factory implem… — Independent S1 review. Reproduced the documented current factory failure (`KeyError: 'group'`); the accepted design closes the mapping contract while preserving the public survivor semantics, identity, ordering, legacy output and all historical/native/game boundaries. `bun run validate` exit 0: 157/157 tests, 2,136 expect() calls, docs and campaign checks passed.

### S2 — Implement strict survivor projection and verify the existing loss reference
- **Status**: done
- **DependsOn**: [S1]
- **Files**: `tools/design/episode_dossier.factory.py`, `tools/design/test_pooled_survivor_projection.py`, `tools/design/test_design.py`, `tests/unit/pooled-survivor-projection.fixture.ts`, `docs/qa/pooled-survivor-projection/acceptance.md`
- **Gate**: type
- acceptance:
  - "After i00009/S2 is independently accepted and integrated, reuse existing group-ID generation and strict numeric primitives to project exactly one survivor row for any declared group union. Do not create or relocate an actor, invent a group alias in public output, or modify any runtime/public schema."
  - "Use real artificial factory output plus existing strict dossier/reference validation to test four groups of2 pooled at minimum6, unchanged single-group output, malformed/unknown/duplicate groups and minimum types/bounds; verify existing death logic tolerates2original losses and defeats on3 regardless of the origin court, with required defeat before possible victory."
  - "Preserve all64 current dossiers,2645screens,398secondaries,49reference records, existing generated artifacts/native rejection and IDs; run targeted/design/bun validation, record independent review and native/game/history limitations without authoring a historical campaign."
- review-state: done
- review-implementer: minimax-m3.1-flash-preview
- review-reviewer: gpt-6-luna
- review-log: approved by gpt-6-luna — verified at d86c56130391, validate exit 0 and tests 157/157 claimed, no recorded run cited; acceptance 3/3: (1) Verified factory resolves mutually exclusive group/groups selectors in authored order, applies the existing is_positive_integer primitive and emits only entiti… (2) 14 focused Python tests passed. The test-only TS bridge takes real factory output, validates the artificial public v2 profile and semantic references, then inv… (3) Focused tests and bun run validate passed (157/157, 2,136 expectations; docs check and 3 campaigns passed). Factory source checks preserve 64 dossiers and lega… — Independent S2 review only; focused and validation logs are saved under /tmp/i00010-s2-independent-review/. The test-only TS bridge exercises the public reference validator and reducer; no native/game/history approval is claimed.

## acceptance

- Specify a strict internal choice of one existing group or a nonempty unique groups array, stable flattening of already generated main IDs, valid positive minimum no greater than unique pool size, and explicit diagnostics for malformed/unknown/duplicate inputs, with real artificial reproduction.
- Keep unchanged public reference loss/current-presence contracts, actor origins and identity, legacy output, external i00009/S2 serialization requirement, no historical authorization and independent verification boundaries.
- After i00009/S2 is independently accepted and integrated, reuse existing group-ID generation and strict numeric primitives to project exactly one survivor row for any declared group union. Do not create or relocate an actor, invent a group alias in public output, or modify any runtime/public schema.
- Use real artificial factory output plus existing strict dossier/reference validation to test four groups of2 pooled at minimum6, unchanged single-group output, malformed/unknown/duplicate groups and minimum types/bounds; verify existing death logic tolerates2original losses and defeats on3 regardless of the origin court, with required defeat before possible victory.
- Preserve all64 current dossiers,2645screens,398secondaries,49reference records, existing generated artifacts/native rejection and IDs; run targeted/design/bun validation, record independent review and native/game/history limitations without authoring a historical campaign.
