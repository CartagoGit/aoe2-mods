# i00009 — closed mechanical implementation packet

Architect: gpt-6 · 25 October 2026. Read the live DelendAI proposal and [architect decision](../architecture/authored-secondary-rewards.md). S2 starts only after S1's independent approval on the integrated product; it is assigned to Luna or MiniMax by the architect. No author chooses new reward values for a historical episode under this packet.

## Ownership and fixed result

Work in your own official i00009/S2 unit from current develop, with your actual model identity and session. Git author/committer stays Cartago. Claim exactly the live S2 Files: `tools/design/secondary.py`, `tools/design/episode_dossier.factory.py`, `tools/design/test_authored_secondary_rewards.py`, `tools/design/test_design.py`. The last file only registers the meaningful Python cases in the existing design test runner. Do not change `packages/`, public schemas, campaign/odyssey JSON, existing generated wiki/SVG, native templates, string registries, research records or game statistics.

Implement one internal optional source key, `resourceReward`, for `aid`, `extract`, `repair`, `trade`. Omission preserves exact old results. An explicit vector is validated by the existing strict `resource_amounts` helper and converted to stable resource order with zeros omitted. `{}` is an intentional zero. No mutating caller data/default dictionaries, fallback after invalid input, special historical ID, extra payment option or new general DSL is allowed. Unsupported kinds reject the field even when empty.

Reuse `build_optional_objectives`, its existing predicates/effects/IDs and `objective_text`. For positive effective rewards, existing caption machinery names only the effective resources. For a zero override on the allowed kinds, use the exact EN/es-ES lines in the decision. Keep information-kind captions byte-identical. Existing 50-wood repair and 50-gold trade costs, genuine arrival/restoration requirements, funding flags and optional failure isolation do not change.

Forward the key through `build_dossier` only when present. Compute the reward and cost totals from the resulting actual effect/payment contracts, then pass those totals to the existing accounting construction. Do not retain a contradictory second sum of global defaults or weaken surplus/cache/recovery checks. The already implemented v3 path remains untouched.

## Required meaningful evidence

| Case | What must be established |
|---|---|
| Omitted field | Same existing objective/caption/budget output; exact current generated dossier/wiki/SVG bytes preserved. |
| Positive override | Effective resource effect, goal EN/es-ES and reserved stock agree; an omitted resource does not inherit its old default. |
| Explicit zero | `{}` and an all-zero vector produce no resource bonus; both exact zero captions appear; no information-kind lookup error. |
| Four eligible kinds | Actual arrival, restore and existing payment requirements remain intact. A zero reward does not zero a 50-resource cost. |
| Invalid vectors | Reject negative, Boolean, integral and fractional floats, strings, null, arrays and unknown resource keys; no coercion/default. |
| Misplaced field | Reject override on copy/guide/watch/scout, including `{}`; do not attach inert money to an information effect. |
| Mutation | Input dictionaries and global defaults unchanged after success and rejection; repeated calls deterministic. |
| Mixed factory fixture | Use the real legacy dossier factory and validator with at least six artificial optional tasks/four kinds/three playstyles and distinct original placements. Effective totals come from generated effects/payment requirements, not a hand-made aggregate assertion. Keep preplaced identities out of their receiving zones. |
| Funding and limits | Main all-skip remains solvent; reserved rewards and recovery remain isolated. Over-budget/cache-exceeding overrides stay invalid. A repair cannot spend its own unearned reward. |
| Existing lifecycle | Cite the existing immutable optional-state implementation/tests for once-only completion, failed optional and terminal closure. Do not create a second reducer or invent new save/load/game evidence. |

Avoid a test that merely repeats the implementation. Verify real output contracts, a complete valid factory fixture, the independent validator and stable legacy artifacts. Use the existing default/fixture helpers where possible; create no historical dossier or copied narrative for testing. Keep tests under the existing Python/Bun runners without adding a dependency.

Run the focused command for the new Python test module and `python3 tools/design/test_design.py` using the existing runner. Check `python3 tools/design/episode_dossiers.script.py --check`, `python3 tools/design/verify.py` and `bun run validate`. No regeneration is needed to land a feature whose current sources omit the field; a failing check returns to the implementation instead of rewriting the 64 dossiers. The official publication independently validates the prospective merge. Adapter/export behavior has not changed; do not manufacture a native export fixture.

## Delivery and escalation

Provide your exact ref/checkout, real identity, commit, diff, executed commands/results, unchanged-artifact evidence and limitations. Submit only S2, publish through DelendAI and receive independent review; never approve your own slice or transition the entire proposal to review. A corrected round follows the installed different-reviewer rule. Return any ambiguity with field/operation, minimal reproduction and expected/actual result. Do not choose a historical benefit, change a contract, weaken a gate or silently pick another task.

S3 is a separate documentation/acceptance slice after accepted S2. It records implemented commands and actual evidence; it cannot approve Jerusalem70, complete d00002/S4, remove the 54 civic flags or turn source vectors into native gameplay. All 214 missing dossiers, historical editorial review, geographic design and game calibration stay with their assigned owners.
