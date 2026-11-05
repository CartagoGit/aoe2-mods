# Authored optional resource rewards

This guide describes one internal field accepted by the expanded legacy dossier factory: `optionalTasks[].resourceReward` in an episode blueprint passed through `tools/design/episode_dossier.factory.py::build_dossier`. It is source-authoring input for the design dossier. It is not a public scenario field, JSON Schema change, runtime command, engine capability, or permission to change a historical episode.

The [architect decision](../architecture/authored-secondary-rewards.md) and [closed implementation packet](../handoffs/AUTHORED-SECONDARY-REWARDS-PACKET.md) define the rationale and boundaries. The implementation lives in [`secondary.py`](../../tools/design/secondary.py) and [`episode_dossier.factory.py`](../../tools/design/episode_dossier.factory.py).

## Supported tasks and behavior

Only `aid`, `extract`, `repair`, and `trade` accept `resourceReward`. The existing default bonuses and fixed payments are:

| Kind | Default bonus when the field is omitted | Fixed payment/requirement |
|---|---|---|
| `aid` | 100 food, 50 wood | None |
| `extract` | 100 food, 25 gold | None |
| `repair` | 200 food, 100 wood | Pay 50 wood and restore the damaged store to full health |
| `trade` | 150 food, 50 wood | Escort the trader to the receiving post, then pay 50 gold once |

Omission keeps the legacy defaults, goal text, and resulting dossier behavior. Supplying an object replaces that bonus completely: omitted resources become zero rather than inheriting their former defaults. `{}` and an all-zero vector are intentional zero bonuses. For zero overrides the generated goal says so explicitly; it still describes the task's local outcome.

```json
{
  "kind": "aid",
  "resourceReward": { "wood": 7 }
}
```

For this artificial fixture, the resulting effect has `resources: {"wood": 7}`. The goal suffix is `Benefit: 7 wood, once.` in English and `Ventaja: 7 de madera, una vez.` in Spanish. No default food bonus is added.

```json
{
  "kind": "extract",
  "resourceReward": {}
}
```

For an artificial subject named “the artificial district”, the effect has `resources: {}` and the generated captions end with:

- EN: `No resource bonus. Completing this task achieves the optional local outcome described above.`
- es-ES: `Sin bonificación de recursos. Al completar esta tarea se consigue el resultado local opcional indicado arriba.`

An omitted field behaves differently. For example, an `aid` task with no `resourceReward` keeps `{"food": 100, "wood": 50}`. An explicit `{"wood": 7}` keeps only wood. Repair and trade retain their stated costs even with `{}` or all-zero rewards.

## Validation and accounting

The builder validates an explicit object with the existing `tools/design/design_numbers.helper.py::resource_amounts` helper. Keys may only be `food`, `wood`, `gold`, and `stone`; each value must be a nonnegative Python integer. Boolean values, floats (including `1.0`), strings, negative values, nulls, arrays, and unknown keys are rejected. Explicit vectors are emitted in the established resource order with zero entries omitted. Invalid input fails closed; it does not fall back to a default. `copy`, `guide`, `watch`, and `scout` reject `resourceReward`, including `{}`, because their existing effects are informational rather than resource transfers.

`build_dossier` forwards the field only when it is present. After `build_optional_objectives` creates the actual contracts, the factory derives:

- `secondaryBudget.reservedRewards` by summing `effects[].resources`;
- `secondaryBudget.maxOptionalCosts` by summing the `resources` on `atomic-payment` requirements.

Those vectors feed the existing difficulty accounting and validator. The validator still checks budget agreement, reward-cache allowance, available surplus, protected recovery, and that the main route remains solvent when every optional task is skipped. A reward cannot fund its own prerequisite payment. There is no payment override, extra cache, automatic income, or weakened limit.

For reference, `tools/design/secondary.py::build_optional_objectives` remains responsible for the existing IDs, predicates, payment requirements, effects, and captions. The separate `packages/gameplay-state/capability-state.reducer.ts` reference model accepts a reward only after its optional requirements and reserve checks; it latches once-only flags and closes side tasks at terminal state. Its examples are static reference behavior, not proof that the legacy dossier source is executed by AoE2. Related tests include the optional idempotence case in `tests/unit/phase-ledgers.test.ts` and the optional-only loss case in `tests/alternative-fulfillment/reference/alternative-fulfillment.test.ts`.

## Verification boundaries

S2 was implemented with artificial fixtures and independently approved. The accepted product is `0cf4d064` with independent verdict `9f4be255` (3/3 acceptance criteria). The pre-merge candidate checks and integrated gate are recorded in [the S2 acceptance record](../qa/authored-secondary-rewards/acceptance.md).

This feature leaves the public schemas and the v3 projection path unchanged. It does not write current historical blueprints, choose a reward for Jerusalem70, establish historical truth, certify map geometry, or implement a native trigger. The current catalog remains 64 draft dossiers, 2,645 draft screens, 398 optional objectives, and 49 registered reference records. Jerusalem70 remains partial in its assigned design work. No map was played and no AoE2 game verification is claimed.
