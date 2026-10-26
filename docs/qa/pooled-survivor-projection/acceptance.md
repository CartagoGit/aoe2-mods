# i00010/S2 — pooled original survivor projection: acceptance evidence

Slice: i00010/S2 (implementer `minimax-m3.1-flash-preview`, session `8c9fc1ac`).
Decision: [pooled original survivors](../../architecture/pooled-survivor-projection.md).
Packet: [POOLED-SURVIVOR-PROJECTION-PACKET](../../handoffs/POOLED-SURVIVOR-PROJECTION-PACKET.md).
Base: `develop` at `188c2f9e`. Prerequisites verified on the live DelendAI server before
claiming files: i00009/S2 `done` (product `0cf4d064`, independent verdict `9f4be25`) and
i00010/S1 `done` (independent approval merged at `f4a2599`).

This document records executed evidence only. It does not approve the Jerusalem map, its
secondary rewards, the complete episode, any historical authoring proposal, native
implementation or game behaviour.

## What changed

`tools/design/episode_dossier.factory.py` projects one survivor row per authored selector.
A row now selects exactly one of:

- `group`: one existing nonempty group name (unchanged legacy selector), or
- `groups`: a nonempty list of distinct nonempty group names.

The factory resolves those names against the object-group dictionary it already generates,
flattens the selected groups in authored order, preserves each group's generated order and
rejects ambiguous, missing, wrong-typed, empty, duplicate, unknown or membership-repeating
input, plus any minimum that is not a positive integer or exceeds the pooled identity count.
The minimum is checked with the existing shared primitive
`tools/design/design_numbers.helper.py::is_positive_integer`; no second numeric policy, no
coercion, no clamping, no alias, no deduplication.

The emitted row keeps exactly the previous two fields, `entities` and
`minimumAliveOrAlreadySafe`. No public schema, reducer, native adapter, string registry,
actor, origin, offset, historical source or generated artifact changed.

`tests/unit/pooled-survivor-projection.fixture.ts` is a test-only bridge. The design row has
two fields and the public v2 row additionally declares `loss`; the bridge adapts one
artificial profile, validates it with the public schema and validator and then executes the
existing reducer. It is not a production mapper or an export path.

## Commands and results

Executed in the isolated unit
`.cache/delendai/.worktrees/minimax-m3.1-flash-preview-i00010-S2`; logs under the ignored
`build/pooled-survivor-projection/logs/`.

| Command | Exit | Result |
| --- | --- | --- |
| `python3 tools/design/test_pooled_survivor_projection.py` | 0 | 14 tests, OK |
| `python3 tools/design/test_design.py` | 0 | 126 tests, OK (112 previous + 14 registered) |
| `python3 tools/design/episode_dossiers.script.py --check` | 0 | `64 explicit expanded dossiers checked`; no stale dossier, wiki or SVG byte |
| `python3 tools/design/verify.py` | 0 | `status: passed`, `errors: []` |
| `bun run validate` | 0 | tsc + biome clean, `157 pass / 0 fail`, 2136 expect() calls, docs:check valid, 3 campaigns validated |
| `bun run test:export` | 0 | `variants: 3`, `roundTrips: 2`, `unsupportedModeRejected: true`, `gameVerified: false` |

`bun run test:export` only runs inside this unit with the shared pinned artefacts:
`COF_PYTHON=/home/cartago/_projects/games/aoe2-mods/.venv/bin/python` and
`RGE_CAMPAIGN_BIN=/home/cartago/_projects/games/aoe2-mods/.cache/toolchain/3c40203b650de9888ca82fae1276ea67bf3d3d93/rge_campaign`.
Without them the isolated unit has no Python virtualenv and no pinned parser build and the
adapter aborts before any export; that is an environment fact of the worktree, not a
behaviour change. No adapter, scenario, schema or export file was modified by this slice.

## Evidence

### 1. The real artificial reproduction, before and after

Before this slice the documented reproduction raised `KeyError('group')` at
`tools/design/episode_dossier.factory.py` `world_and_objectives`, because the projection
indexed `groups[row["group"]]` only. After the slice the same input produces one survivor
row:

- entities: `artificial.pooled-originals.west-1`, `west-2`, `east-1`, `east-2`, `south-1`,
  `south-2`, `central-1`, `central-2` (authored court order, each court's generated order);
- `minimumAliveOrAlreadySafe`: 6;
- row fields: exactly `entities` and `minimumAliveOrAlreadySafe`.

The eight entity objects are byte-identical to the projection of the same authored object
groups without any survivor row: the same ids, the same `initialHub` (`hub-1` … `hub-4`) and
the same `offsetTiles`. The main identity set stays eight distinct identities; no actor is
created, moved or duplicated.

### 2. Legacy output is unchanged

- The single-`group` selector still projects the previous row exactly: `entities` equals the
  generated group ids and `minimumAliveOrAlreadySafe` is copied unchanged.
- Every one of the 49 current blueprints that carry survivor rows (138 authored rows) was
  re-projected through the factory and compared with the committed generated dossier:
  `survivorGroups` and `entities` match for all 49, and all 138 authored rows still declare
  only `group` and `minimumAliveOrAlreadySafe`. No source was migrated.
- `python3 tools/design/episode_dossiers.script.py --check` compares the generated dossier,
  wiki and SVG bytes of all existing sources and reported no stale artifact.
- `verify.py` counts are unchanged: 64 expanded dossiers, 2645 draft screens, 398 optional
  drafts, 49 additional downloaded references, 0 errors. The existing dossier numeric audit
  `audit_count_thresholds` returns no error for all 64 dossiers.

### 3. Rejections happen in the real factory

`tools/design/test_pooled_survivor_projection.py` drives the actual factory (not a copied
helper) for: both selectors at once, no selector, `group: null`, empty and blank group
name, scalar `groups`, empty `groups`, duplicate group names, blank name in `groups`,
unknown pooled name, unknown group, a group that resolves to no original, missing minimum,
zero, negative, boolean, float and string minima, and an oversized minimum (9 over a pool of
8). Each case raises `ValueError`.

A pool that repeats an entity identity is rejected as well. That case is exercised as a
narrow defensive input to the factory helper with a forged group mapping; no invalid
historical world was created to reach it.

### 4. The existing loss evaluator, executed

`tests/unit/pooled-survivor-projection.fixture.ts` builds the public artificial profile from
the factory output (the eight real factory originals with their real ids, origin hubs and
offsets, their real origin districts declared, and the factory's two-field row adapted with
`loss = "defeat"`), validates it with `capabilityProfileV2Schema` and
`validateScenarioCapability` (no issue), and then executes the existing reducer
(`reduceCapabilityState`, `destroy-entity`, `record-arrival`, `latch-objective`, `tick`).
Observed results:

| Observation | Result |
| --- | --- |
| Cross-court losses (one from `west`, one from `east`) | terminal `null`, 6 pooled alive |
| Third loss (`south`) | terminal `defeat`, 5 pooled alive |
| Same-court losses (both `west`) | terminal `null`, 6 pooled alive |
| Third loss (`east`) | terminal `defeat`, 5 pooled alive |
| Receipt only (`record-arrival` of `bundle-1` at `store-1`, no fresh observation) | objective not satisfied, live presence not satisfied, no latch |
| Latch of `return` with a fresh valid batch placing the six helper actors in their stores | `objectiveLatches: ["return"]`, terminal `null` |
| Control: fresh sequence-2 tick from that same prior state, six remaining pooled originals alive | terminal `victory`, phase `victory` |
| Same prior state, fresh sequence-2 tick also reporting the third pooled original dead with no zones | terminal `defeat`, phase `defeat` |

The defeat is produced by the reducer's own loss evaluation
(`capability-predicates.validator.ts::hasIrrecoverableLoss`), which counts distinct
surviving originals across the pool; the control proves that the same prior state would
otherwise win, so the required defeat-before-victory ordering is executed, not assumed. No
hand-counted array is offered as proof and no latch or terminal flag is set by hand.

### 5. Presence, receipts and optional identity

Fresh presence stays separate from arrival receipts: after the arrival receipt the current
presence requirement is still unsatisfied and the objective does not latch until a fresh
live batch arrives. No optional identity can enter the pool: the public validator rejects
pool members that are not declared main-world entities, which is confirmed by the reused
negative cases (`capability.survivor-entity`), including an optional identity that exists
only in a secondary world. The existing validator cases are reused unchanged: duplicate pool
identity → `capability.survivor-identity`, unknown identity → `capability.survivor-entity`,
oversized minimum → `capability.survivor-threshold`.

## Remaining limitations and gates

- Native implementation, native observers, terminal batching, pathfinding and game QA stay
  pending under their own proposals; the composed profile remains reference-only and the
  native renderer and Python adapter still reject it as `capability-not-implemented`.
- No game was run. No map, route, balance, difficulty or playability claim is made.
- No historical dossier was created, regenerated or migrated; Jerusalem70, its map frame and
  its secondary rewards remain inside d00002 and are not approved here.
- The pooled selector is internal to the design source. No new public schema, profile
  version, string registry entry or campaign/episode identity was introduced.
- The artificial bridge and its artificial profile are test-only; the optional identity it
  adds to one secondary exists only inside that test profile.
- i00010/S2 requires an independent review on the integrated product; the implementer does
  not approve this slice.
