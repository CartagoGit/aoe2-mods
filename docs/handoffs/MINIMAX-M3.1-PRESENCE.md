# MiniMax packet — presence promotion and deposit QA

Architect: gpt-6 · 26 October 2026. Future bounded assignment for i00005/S3, **not assigned or executable yet**. Its native prerequisite i00005/S2 and the additional i00003/S3 foundation remain pending. Read the live proposal and [ADR 0005](../decisions/0005-live-entity-presence.md); do not infer native support from this packet or an artificial export. The source scenario envelope and public profiles retain their accepted versions.

## Entry gate and exact scope

Before asking for a unit, recover DelendAI overview/capabilities and i00005/S1–S3 plus i00003/S3. Only start S3 after its S2 and all external native prerequisites are integrated and independently accepted for the operations below. A missing source file was an avoidable handoff gap; creating this packet removes that gap but cannot satisfy a native gate. Root will explicitly assign the worker and the scope when dependencies hold.

The existing S3 Files are `tools/design/episode_dossier.validator.py`, `docs/design/odysseys/imperial-church.json`, `docs/qa/entity-presence` and this handoff. Do not edit public schemas, reducers, native adapters, IDs, campaign identity or string ranges under S3. No broad migration of all dossiers, new gameplay, or general support-status rewrite is authorized. If native capability lacks a real observable, report the reproduction against i00005/S2/i00003/S3 and keep content blocked; do not add a timer, boolean, frozen actor or paid receipt as position.

## Exact source binding — Milan350

The target is `imperial-church/22-civilian-record-preservation-milan`, not the separate 313 Milan agreement episode. Read the full current dossier and preserve its source/history/economy/terrain gates. Its ID prefix below is `imperial-church.22-civilian-record-preservation-milan.`; concatenate that exact prefix with each suffix. Do not generate replacement identities or collapse stores. If the current source bindings differ from this table at assignment time, stop and return the discrepancy to root; do not select new identities or silently migrate the contract.

| Original identity suffix | Assigned destination suffix | Final presence binding |
| --- | --- | --- |
| `western-civilian-bundle-1` | `destination-2` | o3/req-3, requiredCount 1 |
| `northeastern-civilian-bundle-1` | `destination-3` | o3/req-4, requiredCount 1 |
| `southeastern-civilian-bundle-1` | `destination-4` | o3/req-5, requiredCount 1 |
| `original-store-custodians-1` | `destination-2` | o3/req-6, pooled requiredCount 3 across the three assigned custodians |
| `original-store-custodians-2` | `destination-3` | same req-6, own destination only |
| `original-store-custodians-3` | `destination-4` | same req-6, own destination only |

Those six originals must be alive/currently inside their own assigned stores at the successful return closure. Previously recorded delivery remains true after movement; it is not residence. Count each original once even if zones overlap. Wrong originals, optional participants, extra copies and another store do not substitute. A later departure makes the final attempt incomplete until a valid original returns; it does not erase historical receipt or impose immobility. Required irreversible loss still has defeat priority.

The same three `original-reporting-clerks-1/2/3` must first obtain their own o2/req-5 store receipts, then satisfy o3/req-1 ordered departure and o3/req-2 arrival after that departure at `destination-5`. This remains the accepted receipt/ordered-return contract. Do not silently add current-residence requirements to reporting clerks, reinterpret their old visits as the final six-object presence, or replace them with a new worker. Preserve any separately authored survival rule. Exact current presence applies to the four explicit o3 bindings, not every historical arrival in the mission.

## Reuse and state rules

Reuse `packages/schemas/live-spatial-batch.schema.ts`, `packages/gameplay-state/live-entity-presence.helper.ts`, the existing capability reducer/snapshot and `tests/unit/entity-presence.test.ts` as the reference. Native S2 must supply actual current life/zone observations in the closure evaluation; fabricated test input remains test input. A saved positive observation is insufficient after load: obtain fresh input in the current host context, preserve monotonic sequencing/fingerprint rules and never reuse old positive memberships. Omitted actors are unknown, not assumed present.

Preserve ADR 0005: whole-batch rejection for invalid/duplicate/stale evidence cannot certify completion, but it cannot suppress independent clock/deadline/defeat processing. A generated actor needs its actual producer fact before counting; a declared identity alone is insufficient. Checkpoint presence under [ADR 0006](../decisions/0006-checkpoint-entity-presence.md) is separate: its intermediate latch may persist after departure, while current presence dependencies are rechecked before victory. Do not weaken either rule to make this dossier pass.

## Required QA observations

Use the integrated native S2 fixture and actual artifact hashes. Record reference tests, binary round-trips/xs-check and game observations as separate evidence:

1. All six original bindings are alive at their assigned stores; the three clerk receipt/departure/return chains are valid. The intended terminal attempt can succeed.
2. After the old delivery receipt, move each bundle or custodian out in turn. History persists, but final presence fails; return the same original and test recovery.
3. Put a bundle in another store, swap two custodians, add an optional substitute, or overlap zones. Wrong assignment/identity and duplicate counting cannot satisfy the minimum.
4. Apply an original death in the same closure evaluation that would otherwise win. Required defeat wins once. Previously latched history cannot revive it.
5. Save with positive old presence, load and attempt completion without fresh input; then refresh actual positions both inside and outside. Test the native host's restore semantics rather than a serialized true flag.
6. Invalid/stale/duplicate batches cannot force victory or suppress an independently due defeat/deadline. A generated identity without its producer cannot count.
7. Show the separate receipt-only and intermediate-checkpoint cases do not acquire permanent final residence as a side effect. Preserve the existing reporting-clerk contract above.

For game cases record Windows/Steam first, exact AoE2:DE build, mode, locale, selected difficulty, original/copy hashes, steps, actual result and evidence files. Other installations require observations of their own; no Steam API/path belongs in the native artifact. An original preserved for comparison and an editor copy have different names/paths; hashes may coincide when their bytes do.

## Delivery and promotion boundary

Keep `presencePlan.implementationStatus` and per-requirement/native flags truthful. Do not set one global “implemented” value merely because the reference model exists. Before any support-state change, root must identify the exact native capability evidence and the validator's current recognized values; if no value represents the true partial state, return that architecture question rather than invent a status or public schema field. Each applicable requirement, presencePlan and requiredCapabilities view must agree. No historical dossier becomes approved-complete as an incidental result.

Run the focused applicable checks, `python3 tools/design/episode_dossiers.script.py --check`, `python3 tools/design/verify.py` and `bun run validate`. Run `bun run test:export` when an assigned native path/fixture is affected. Canonical/generated source updates must remain coordinated under their actual file ownership; if regenerated wiki/map outputs fall outside this slice, root must assign their ownership before mutation. Never write current historical outputs while claiming a read/check command.

Preserve full logs/receipts outside disposable worktrees before publication. Use your own model identity/session/unit; Git author and committer remain configured human Cartago. Never publish, retire, claim or commit inside another model's unit or pass its identity to a CLI to recover “orphan” work. Integration is the official gate; an independent model reviews the exact integrated product. S3 does not close all odysseys, release a mod, prove gameplay calibration or authorize historical production. Return remaining source, terrain, balance, localization and native/game gates explicitly.
