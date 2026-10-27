# Reference suite time budget

Scope: the two heavy tests in `tests/alternative-fulfillment/reference/alternative-fulfillment.test.ts`. This record exists because the shared validation gate turned red for every agent in this workspace on 27 October 2026, not because a behaviour changed. No assertion, expectation, row count, matrix coverage, fixture, reducer, schema or campaign source was modified.

## What failed, and where it was measured

`bun run validate` failed twice in the same window with the reference suite timing out:

| Test | Measured | Limit it hit | Limit before |
|---|---:|---:|---:|
| the 95 matrix portfolio rows execute selected work, optional tasks, exact outputs, and fresh victory | 39 030 ms | 30 000 ms (explicit) | 30 000 ms |
| load preserves valid lifecycle checkpoints and rejects altered escrow or recipe contracts | 5 400 ms | 5 000 ms (Bun implicit default) | 5 000 ms |

The second failure was Bun's implicit per-test default, because that test carried no explicit budget at all.

## The cause is contention, and the margin was already gone

The architect's own archived validation runs for the same suite record the 95-row test at **23 234 ms**, **25 516 ms** and **28 258 ms** while the machine was otherwise idle. The explicit 30 000 ms budget was therefore already **92 % consumed before any contention**: the test had a margin of roughly 6 % over its own worst recorded baseline, and 4 000 ms over the middle one.

The workspace then ran several workers concurrently. The failing runs happened at a load average of **19.03 on 10 cores**, with `bun install`, `biome`, `vitest` and other suites in flight. The same test then took 39 030 ms in isolation, and the lifecycle-checkpoint test took 5 400 ms against a 2 200–3 300 ms baseline — an inflation of roughly 1.5–1.6×, consistent with pure CPU contention and with no change in the code under test.

The reference test file has not changed since `cffa310` (`fix(fulfillment): validate cross-recipe zones and restored lifecycle`), which predates the failure, and the implementation it exercises is unchanged since then. The failure is therefore environmental, not a regression.

## The budgets now in force

| Test | Baseline (idle) | Budget before | Budget now | Margin over the worst idle baseline |
|---|---:|---:|---:|---:|
| 95 matrix portfolio rows | 23 234 / 25 516 / 28 258 ms | 30 000 ms | **60 000 ms** | 2.12× |
| load preserves valid lifecycle checkpoints | 2 200–3 301 ms | 5 000 ms (implicit) | **30 000 ms** | 9.1× |

The 60 000 ms budget keeps a **2.1× margin** over the worst recorded idle baseline, so a genuine 2× performance regression (≈ 51 s idle) still fails the test. The 30 000 ms budget matches the value the reference suite's sibling files already use (`tests/maps/geographic-raster.test.ts`, `tests/maps/large-map-diagnostic.test.ts`) and the DelendAI test-convention plugin's own `testTimeout: 30_000`; it is 9.1× the measured baseline and 5.5× the contended measurement.

## Measured headroom in the same file, left unchanged on purpose

The remaining tests of this file keep Bun's implicit default because their measured baseline leaves real margin against it. They are recorded here so a future change knows what was observed rather than assumed.

| Test | Measured (idle) | Share of the implicit 5 000 ms default |
|---|---:|---:|
| 27 difficulty and recipe-pair trials execute reserve, atomic rejection, cancel, and commit | 1 751 ms | 35 % |
| fresh output or recipient death in the victory batch wins both terminal races | 1 419 ms | 28 % |
| all 24 before-funding witnesses perform real optional actions before their reservation | 1 019 ms | 20 % |
| generated output or recipient loss defeats before either victory API, while optional-only loss gives no reward | 435 ms | 9 % |
| all seven optional objectives complete through their distinct arrival, visit, health, and payment inputs | 396 ms | 8 % |

The heaviest test outside this file, `tests/maps/geographic-raster.test.ts` (3 614 ms), already carries the same explicit 30 000 ms budget.

## What this does not establish

- It does not certify a performance improvement. No code was made faster; only the budget that measures it was made truthful.
- It does not make the workspace safe for unbounded parallel heavy gates. The architect's packets already require heavy gates to run in a serialized verification window, and that discipline still applies. This fix removes a coin flip, not a policy.
- It does not authorize skipping, relaxing or reinterpreting any check, and it changes no acceptance criterion of i00007/S2.
- It says nothing about engine, gameplay, balance, historical or localisation approval. The reference suite remains repository reference behaviour, not native execution.

Commands used to obtain the baselines: `bun test tests/alternative-fulfillment/reference/alternative-fulfillment.test.ts` and `bun run validate` in the shared checkout, with the idle figures read from the architect's archived logs in `.cache/delendai/.worktrees/gpt-6-d00002-S4-g2/.cache/yavneh-typed-design/validate*.log` and the contended figures from the failing runs of 27 October 2026.
