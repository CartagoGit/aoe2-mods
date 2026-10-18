# Independent review: Imperial 34 finite allocation study

Reviewer: gpt-6-luna  
Candidate reviewed: `d3595e60ce2e9ce2a3d4e0bc2f158567d32cab0a` (base `1c0db6e2`; includes proposal `236bef2`, study candidate `cdc1ba8`, and narrator-scope correction `d3595e6`).  
Scope: accounting helper, report generator, tests, allocation plan/study, brief and handoff/proposal context. This is not a formal approval of `d00002/all`.

## Findings

I found no blocking arithmetic or implementation defect in the bounded accounting study. The helper applies each debit before its reserved reward, only follows affordable prefixes, and records each optional task at most once. It rejects boolean/non-integer/negative/unknown resource values and duplicate identities. For the supplied plan, the nine meal/shelter combinations produce 9/7/3 all-skip affordable combinations on easy/standard/hard. The hard all-skip plans and remainders agree with the plan. Rechecking every reported all-seven example order against each intermediate balance found 19 valid orders; none uses an optional reward to fund that same task. The hard shared-hearth/rented case correctly demonstrates that the 50-wood repair cannot be paid first, while a prior provisions reward can fund it. Optional reward stock remains explicitly separate from operating stock.

The four focused tests cover the key affordability, prefix, no-duplication, invalid-input and fingerprint cases. The audit labels its output `nativeImplemented=false` and `gameVerified=false`. The plan and study likewise state that this is candidate economic analysis, not a gameplay DSL, completed dossier, accepted architecture or proof of an interesting RTS episode. They leave actual routes, actors, work locations, UI, jointly atomic reservation, cancellation/recovery and engine behavior pending. The study correctly rejects promotion if the result is only a menu plus inevitable walking. The three-slice i00007 proposal remains pending; I did not implement it.

The current enumeration limits bound the supplied study (2 services, 3 alternatives each, 7 optionals) and reject excessive combinations/states. As a generalization limit, `MAX_COMBINATIONS` bounds the product of recipe counts but does not independently cap the number of services when each has one recipe. That is harmless for this fixed input, but a generalized authoring tool should also bound service/recipe row counts. The fingerprint includes the resolved plan and optional monetary inputs; it does not fingerprint the executable semantics of `secondary.py`. This does not invalidate the present report, whose source and shared-mechanics relationship are documented, but future reproducibility claims should retain a source/code revision fingerprint if those mechanics can change.

The final `d3595e6` change corrects only the narrator JSON scope label from 273 to 278 selected episode odysseys. The selection count was already 278; no narrator biography, knowledge, episode ID or episode content changed. JSON and project validation passed at the candidate tip.

## Verification

- `python3 tools/design/test_finite_allocation_audit.py`: 4 tests passed.
- `python3 tools/design/finite_allocation_audit.script.py`: 9 combinations; all-skip easy/standard/hard 9/7/3; `nativeImplemented=false`; `gameVerified=false`.
- `python3 tools/design/test_design.py`: 66 tests passed.
- `bun run validate`: passed; 108 tests / 426 expectations, documentation checks passed, and one campaign validated.

These checks assess the study and repository validation only. They do not establish historical accuracy, native capability, map feasibility, gameplay quality or engine behavior.
