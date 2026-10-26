# i00009/S2 — implementation and acceptance evidence

**Status:** S2 integrated and independently approved. This record documents the implemented projection and its static evidence; it is not a historical dossier review or an AoE2 playtest report.

The [authoring guide](../../guides/authored-secondary-rewards.md) explains the source field and its output. Relevant source and tests are [`secondary.py`](../../../tools/design/secondary.py), [`episode_dossier.factory.py`](../../../tools/design/episode_dossier.factory.py), [`test_authored_secondary_rewards.py`](../../../tools/design/test_authored_secondary_rewards.py), and [`test_design.py`](../../../tools/design/test_design.py).

## Accepted scope

The source-only input is `optionalTasks[].resourceReward` in the expanded legacy dossier builder. It applies only to `aid`, `extract`, `repair`, and `trade`. Omission preserves the previous kind defaults and output. An explicit object replaces the bonus; `{}` and all-zero vectors emit no resource bonus and use the specified bilingual zero captions. Resource keys are the existing four-resource set and values pass the strict `resource_amounts` helper. Unsupported informational kinds reject the field, including an empty object.

Repair still requires its existing 50-wood payment and full-health restoration. Trade still requires arrival followed by its existing 50-gold payment. The factory derives the reserved reward sum from the generated effects and optional costs from generated `atomic-payment` requirements, then passes those actual totals through existing difficulty accounting and validation. No global reward total, public schema, v3 mapper, generated dossier, or native adapter was changed by S2.

## Executed checks

The implementationer's full checks ran in the isolated S2 unit at candidate `5481b316857d308f69d486107c3a9c3421970725`, before that unit merged the subsequent documentation-only `origin/develop` changes. The original outputs are retained locally under `/tmp/i00009-S2-validation-5481b31/`; the independent root records are `/tmp/i00009-root-focused.log`, `/tmp/i00009-root-dossiers-check.log`, `/tmp/i00009-root-verify.log`, and `/tmp/i00009-root-validate.log`.

| Command | Recorded result |
|---|---|
| `python3 tools/design/test_authored_secondary_rewards.py` | 3 tests passed |
| `PYTHONPATH=tools/design python3 -m unittest test_design.AuthoredSecondaryRewardTests` | 3 tests passed; same focused cases are registered in the existing runner |
| `python3 tools/design/test_design.py` | 112 tests passed in 47.69 seconds |
| `python3 tools/design/episode_dossiers.script.py --check` | 64 expanded dossiers checked; no historical or native approval asserted; generated artifacts were not rewritten |
| `python3 tools/design/verify.py` | Passed; 64 draft dossiers, 2,645 draft screens, 398 optional drafts, 49 additional registered references, 0 expanded approved dossiers |
| `bun run validate` | Passed: check/type and lint, 157 Bun tests, 2,136 expectations, documentation links, and 3 campaign validations |

DelendAI then integrated candidate `0cf4d064beddbd736de942c0510de0ffabeb753b` against `9047d9954e005e091b257901c0dce16f52fc67b7`. Its official prospective-merge certification passed `bun install --frozen-lockfile` and `bun run validate`. Root's independent review recorded verdict `9f4be255` and approved S2's 3/3 acceptance criteria. The full Python suite and dossier checks above were run before the integration merge; the official Bun gate is the verification run against the integrated prospective product.

## Independent lifecycle reference and limits

Existing reference code/tests cover behaviors that this projection does not implement: `packages/gameplay-state/capability-state.reducer.ts` gates an optional award on satisfied requirements, nonterminal state, available optional reserve, and an unused reward flag; it debits reserve, credits spendable stock, and latches completion once. It marks a lost optional entity `failed-optional` and prevents an award after terminal closure. Relevant examples include `tests/unit/phase-ledgers.test.ts` (optional completion/idempotence and terminal closure) and `tests/alternative-fulfillment/reference/alternative-fulfillment.test.ts` (optional-only loss cannot reward). These are repository reference tests; they do not demonstrate native execution of the legacy dossier contract.

The catalog counts stayed at 64 draft dossiers, 2,645 draft screens, 398 optional objectives, and 49 registered reference records. The 64 dossiers remain drafts; the verify report records zero expanded approved dossiers. Jerusalem70 remains partial in its assigned work. No historical reward decision was made, no map or scenario was played, no game balance was verified, and no native support was added. S2 approval is limited to the implementation packet and static acceptance criteria above.
