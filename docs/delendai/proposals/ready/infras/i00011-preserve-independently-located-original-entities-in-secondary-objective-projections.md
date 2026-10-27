---
id: i00011
title: "Preserve independently located original entities in secondary objective projections"
kind: infra
status: ready
type: proposal
track: general
date: 2026-10-27
---

# i00011 — Preserve independently located original entities in secondary objective projections

## goal

Resolve the reusable gap between per-original physical origins and single-origin secondary projection, through an explicit independently reviewed architecture decision. Preserve all existing campaign identities, string/progress ranges and public v2/v3 contracts until that decision authorizes a compatible opt-in operation. A dossier must not move original actors or invent large local offsets to conceal a missing capability.

## why

The reviewed Yavneh world candidate has two distinct working-record carriers at record-west and record-north. `tools/design/secondary.py` projects one placement.originHub into every original and then requires every initialHub to equal reachability.originHub. The typed `packages/gameplay-validation/scenario-capability.validator.ts` enforces that same invariant. The strict secondary schema permits one reachability.originHub and no invented per-origin metadata. Patching Python alone, silently changing the meaning of originHub, or flattening one pickup into another would hide the problem.

This also concerns future distributed archives, dispersed aid pickup and independently consenting civilian originals. This proposal records a genuine missing reusable operation; it does not declare a historical scenario implemented. The world candidate and financial witness remain useful while composition is blocked.

## non-goals

- No silent relaxation of the existing single-origin contract, new fields in an unchanged strict schema, content ID/string renumbering, fabricated roads or actor substitution.
- No implementation before S1 independently resolves the explicit opt-in/versioning and compatibility boundary.
- No replacement reducer, DelendAI clone, historical campaign generation, terrain approval or game evidence from a connectivity graph.
- No public distribution, mass paid media or automatic content-authoring unlock.

## slices

- global_gate: type

### S1 — Architect decision, inspected invariant and compatibility cases
- **Status**: pending
- **Files**: `docs/architecture/secondary-origin-identity.md`, `docs/qa/secondary-origins/decision`
- **Gate**: type
- acceptance:
  - "Inspect both typed and Python schemas/validators, actual authoring forwarding, state/save/load and map bindings. Select a proven existing representation or define a separately explicit compatible capability; do not reinterpret originHub as fallback silently."
  - "Specify authority for each immutable original's initialHub, exact cardinality/identity assignment, assigned receiving zone, deterministic summary origin if retained, and a declared-corridor path for each origin. Distinguish graph connectivity from full-width land, offsets, bridges, transport and historical geography."
  - "Choose and justify opt-in/version/migration handling before code: old valid and invalid contract cases retain their documented interpretation; scope broader semantics only through an approved capability boundary. Independent model review required."

### S2 — Approved reference contract and coordinated validation only
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `packages/schemas`, `packages/gameplay-validation/scenario-capability.validator.ts`, `packages/gameplay-state`, `tests/secondary-origins/reference`
- **Gate**: type
- acceptance:
  - "Implement only the exact accepted S1 branch. Preserve all prior fixtures/IDs and source input immutability; reuse current entity identity, arrival receipts, current-life predicates and resource accounts without a second reducer."
  - "Reject missing/duplicate/unknown origins, per-original cardinality mismatch, unreachable assigned destinations, unknown corridor IDs, crossed destination assignments and initial delivery. Do not accept a total at one post as another original's arrival."
  - "Save/load retains the same original identities and authoritative origins; stale observations, duplicates and loss cannot create or substitute a receipt. Keep unsupported native/export modes rejected."

### S3 — Authoring projection, map/source trace and closed handoff
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `tools/design/secondary.py`, `tools/design/episode_dossier.factory.py`, `tools/design/fulfillment-dossier.mapper.ts`, `tools/design`, `tests/unit/fulfillment-dossier.test.ts`, `docs/guides`
- **Gate**: type
- acceptance:
  - "Forward only the approved explicit source operation through the real factory and typed projector, preserving per-original hub and local offset without aliases. Default legacy generation remains byte-identical."
  - "Check Python and TypeScript agreement through the actual complete pipeline: two geographically separate original pickups, distinct assigned destinations, declared corridor coverage from each original and source-to-map trace. Include negative disconnected and missing-hub cases."
  - "Run focused and full validate gates, preserve exact product/review hashes and provide a bounded MiniMax packet. No full historical dossier or authoring proposal is unlocked merely because this reference slice passes."

### S4 — Bounded native adapter and actual engine evidence
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `packages/aoe2-adapter`, `tools/python`, `tests/fixtures/native-secondary-origins`, `docs/qa/secondary-origins/native`
- **Gate**: e2e
- acceptance:
  - "External prerequisites i00003 native composition/input/map support and s00001 engine evidence remain explicit. For alternative-service scenarios also require i00007/S3; source/reference success never substitutes for these operations."
  - "Native originals begin at their own physical sites with exact handles, path/transport and destinations, not giant offsets from a false hub. Verify initial placement, independent arrivals, death, duplicate input, reward-once and save/load."
  - "Run validate/test:export, pinned native round-trips/XS checks and AoE2 tests with build/hash/locale/difficulty. Keep untested or unsupported branches rejected and retain independent review before any historical authoring recommendation."

## acceptance

- S1 architecture decision and independent verdict precede any contract or validator change.
- Per-original origins, destinations and immutable identity survive the real source/reference/native chain without geographic aliasing.
- Existing single-origin content and unsupported-mode rejection remain preserved at their approved compatibility boundary.
- Graph, native serialization and engine-play evidence are reported separately; incomplete stages remain pending.
