# Explicit finite accounts for authored difficulty

Architect gpt-6 · 27 October2026 · i00013/S1 · decision candidate. This specifies a missing **authoring factory** operation. It does not implement that operation, widen a gameplay schema, approve historical content or establish difficulty in AoE2. Independent acceptance remains required before S2 implementation.

## Problem and reuse boundary

The legacy factory's current bank is `M + P + Z + R + Q − start`. Its reported accessible budget is `start + bank − R`, so changing the starting multiplier changes the bank by the opposite amount and leaves that reported total equal to `M + P + Z + Q`. Here M is mandatory payment, P recovery, Z replacement planning reserve, R optional reward reserve and Q discretionary margin. This explains a static observation, not a verdict that all existing difficulties play alike: opposition, timing and the available workers can differ. Do not silently repair or rewrite64dossiers from this observation.

The accepted v3 authoring path already takes explicit accounts; keep it unchanged. A non-recipe v2 scenario must not be recast as a fictitious exclusive recipe merely to gain resource controls. Extend only the existing legacy factory through one explicit opt-in and reuse its common dossier composition, resource validation and the real finite allocation analyzer.

## Exact source input and precedence

`authoredDifficultyAccounts` is a source-only object with exactly `easy`, `standard`, `hard`. Each record contains exactly four accounts, and each account contains exactly `food`, `wood`, `gold`, `stone`:

| Account | Meaning |
|---|---|
| `spendable` S | Actual operating stock available initially. |
| `gatherableBank` B | Explicit finite recoverable supply; zero until its placement/collection is separately supported and approved. |
| `protectedRecovery` P | Segregated recovery stock; unavailable for main or optional payments in these feasibility witnesses. |
| `optionalReserve` R | Segregated once-only rewards, unavailable before an earned award. |

Reuse `design_numbers.helper.py::resource_amounts` for canonical normalization, adding exact-key and `0..Number.MAX_SAFE_INTEGER` checks at this new boundary. The existing Python numeric helper itself does not impose the JavaScript safe-integer ceiling; do not claim it does or change every legacy caller. Reject bools, fractions, negatives, unknown/missing keys and nonfinite/unsafe values. Check intermediate additions as well as individual inputs; separate safe integers can overflow when summed.

With the opt-in, reject legacy `startingResources` and `discretionaryMargin` aliases as ambiguous. If the optional common `protectedRecoveryStock` alias is present, every authored P must agree; it may instead be omitted when P is declared here. The existing common `replacementBudget` Z remains a planning floor **within** spendable resources, not another credited bank or a fourth runtime reserve. No opt-in means the complete old path and output remain unchanged. The strict v3 blueprint does not accept this new legacy field.

## Derived fields and conservation

For each difficulty emit existing `startingResources=S`, `gatherableBank=B`, `protectedRecoveryStock=P` and `accessibleWithoutOptionalRewards=S+B`. In this explicit mode P and R are excluded from that accessible figure. The output `basis` must state that distinction so reports never compare this figure to the old compensated metric as if their bookkeeping definitions were identical. Do not derive B from any shortfall.

Mandatory all-skip feasibility requires `S+B >= M+Z` resource by resource. A negative/free-resource shortfall is a rejected content source, never an invitation to draw from P, R or a future optional task. Feasibility with nonzero B assumes all its approved finite nodes can actually be collected; it says nothing about deadlines, protection or reachability. New design candidates use B0.

R equals the exact sum of all actual once-only side effect rewards. The generated `secondaryBudget.reservedRewards` and `reallocatedCacheAllowance` describe that **same** R. They are not separate credits. Preserve `maxOptionalCosts` from actual payment predicates. Do not retain the unrelated legacy600F300W150G allowance in this opt-in branch.

After reserving M and the unspent planning floor Z in the analysis, run existing `finite_allocation.helper.py::optional_states` with the actual authored side cost/reward vectors. Its `balance` pays before crediting a reward. Do not substitute the convenience preset or an aggregate-cost guess. For7tasks the all-complete mask is127; for8 it is255. Each side ID/once flag is distinct. Enforce the existing dossier6–8 task bound before subset enumeration, and reject unsafe aggregate and resulting balances; raw optional_states is reused behind this bounded, validated input, not exposed to unbounded task counts. A reachable full mask establishes `allOptionalCostsAffordable` under the stated actor/spatial assumptions; a false result rejects a content source that promises an all-complete route. No resource reward may fund its own preceding debit.

The analyzer's temporary subtraction of Z protects a planning floor; it is not a native debit or new account. Its free remainder plus the unchanged floor is the final spendable balance. With B0, checked conservation is `initial S + P + R = final spendable + P + remaining R + M + paid optional costs`. Never add an allowance or Z a second time.

## Boundary cases and evidence

The [bounded cases](../qa/campaign-design/authored-difficulty-accounts-cases.json) use artificial identities and seven task vectors. The actual shared analyzer was executed for three authored difficulty accounts, each with B0 and nonzero P. All128optional subsets are reachable after main payment while preserving Z, and the all-seven witnesses exhaust R exactly. Their different final spendable vectors are arithmetic evidence, not calibrated gameplay.

The31negative/source-gate cases are prospective acceptance requirements. They have **not** been run against an implemented opt-in factory, because that operation does not yet exist. The cases distinguish malformed source, protected/reward borrowing, contradictory aliases, missing actual task inputs and an unapproved nonzero bank. A path may study a bank financially while remaining blocked for content/native approval; do not conflate the two gates.

## Closed implementation assignment after independent S1 acceptance

S2 owns the eight exact factory/helper/validator/report/test Files listed in the coordinated validation decision below and in the proposal; the original three-File implementation scope was insufficient and is superseded. The helper validates/derives the new source envelope; the existing factory still composes the dossier. Reuse current resource normalization and optional-state functions. Do not duplicate the solver, optional mechanics, renderer, source schema or native exporter.

If the existing three-argument `difficulty_profiles` needs actual side rows, add a compatible optional internal argument. Absence of those rows under the opt-in is an error; it cannot fall back to guessed preset costs. Calls without the opt-in keep their previous behavior. Extract side costs/rewards from actual built predicates/effects, with duplicate side IDs and unsafe sums rejected before analysis.

Verify the real factory with all three positive cases and meaningful negative cases; compare every one of the64current legacy/v3 dossier outputs against its baseline when the field is absent, without changing their source files or catalogue counts. Preserve fingerprint/source/ID/state semantics and all unchanged default results. Complete `bun run validate` and official certification; a different model reviews the exact implementation. This packet does not grant self-approval, broad historical authoring or a native exporter bypass.

A later jewish-tradition03 packet may use the accepted operation. Its screen inventory, fiction/source distinction, real frame, actor routes, optional benefits, deadlines and continuation require their own closed decisions. Different budgets alone do not prove a satisfying challenge.

## Coordinated validation decision — 28 October2026; closes architecture P2

The independent reviewer reproduced a real compatibility error in the initial decision: `secondary.py` recomputes legacy available stock as `start+B−R` and need as `M+Z+P`. Merely emitting S+B would produce nonoptional-stock drift, and the legacy margin check would apply the wrong definition. That initial design is not accepted as an implementation packet. The following explicit opt-in dispatch replaces that incomplete part; no check is disabled or selected by parsing the prose `basis`.

The **derived episode dossier**, outside all public gameplay/profile schemas, gets `economyProfile: "authored-finite-accounts-v1"` only when this source-only opt-in is present. The author may not directly provide that output marker to bypass input validation. Marker absent retains the complete legacy path. Unknown marker rejects. The v3 dossier path rejects the presence of any economyProfile marker, including the known legacy opt-in: its existing typed accounts remain the sole v3 contract. Place this guard in the common episode validator before its existing v3 early dispatch; a secondary-only guard is insufficient.

For the new mode define `supplyMargins = S+B−M−Z`, the free operating surplus excluding the unspent replacement floor. It must be nonnegative and reproduced exactly. P and R remain separate and never enter that margin. `secondaryBudget` and actual effects supply R; do not duplicate an independently spendable reward account. The new numeric branch reconstructs S/B/P/R/Z from actual dossier fields/predicates/effects, validates exact keys and safe intermediate totals, recomputes main all-skip feasibility, and independently verifies the actual all-complete optional-state witness. It may reuse the shared arithmetic and finite analyzer, but must not trust a stored true affordability flag or stored witness. It keeps every existing predicate, identity, health, arrival, payment, once-flag, effect and playstyle check outside the accounting branch.

In `secondary.py::check_optional_objectives`, use explicit known-marker dispatch only for its current numeric financing section. The marker-absent formula and checks stay byte-semantically unchanged. Under the known new mode compare `accessible=S+B`, main need M+Z, exact surplus above, exact R, and the recomputed BFS. A malformed or unknown mode fails closed; it cannot fall through. The shared numeric primitive currently normalizes sparse resources, so exact four-key and safe-sum requirements remain this new branch's responsibility.

The civic difficulty report must expose this explicit model and its assumptions beside the existing budget fields, without implying that the old compensated metric and the new segregated metric count the same accounts. Keep its original output unchanged for marker-absent episodes and its v3 branch unchanged; reject unknown markers and v3+marker. The expanded wiki renderer displays the explicit model for new episodes, retaining default output exactly when absent.

`readiness_timing_audit.script.py` is deliberately **unsupported** for this new economy profile in this slice. Reject the known new marker and unknown markers explicitly before calculating or emitting any timing result. Do not silently run the old authored timing assumptions against the new model or present budget arithmetic as travel-time evidence. Enabling that operation needs a separately reviewed timing decision. This rejection is testable and does not remove the existing legacy timing path. The old39-contract `verify.py`, `render.py`, `objectives.py` and optional-design entry point receive no opt-in support or changes here.

Exact S2 ownership is:

- `tools/design/episode_dossier.factory.py`
- `tools/design/authored_difficulty_accounts.helper.py`
- `tools/design/secondary.py`
- `tools/design/episode_dossier.validator.py`
- `tools/design/civic_difficulty_audit.script.py`
- `tools/design/readiness_timing_audit.script.py`
- `tools/design/episode_dossiers.script.py`
- `tools/design/test_authored_difficulty_accounts.py`

Avoid a circular eager load `secondary → new helper → finite_allocation → secondary`. Load the new numeric audit helper lazily inside the opt-in branch after secondary's common constants/functions are initialized, using the established explicit helper loader. Exercise the real factory followed by audit_dossier/check_optional_objectives and civic dispatch, not just a private numeric helper. If this ownership still cannot support a real operation, stop with its actual diagnostic; no emulation or validator bypass is authorized.

Add source/derived-mode tests for unknown markers, v3+marker, wrong supply margin, forbidden direct input marker, unchanged default numeric checks and explicit timing rejection. Compare all64default legacy/v3 dossiers, their generated wiki/SVG and civic report before/after, preserving hashes when the opt-in is absent. These are implementation acceptance requirements; no such implementation or comparison is claimed by this ADR.

## Required test registration — 5 November2026

S2 ownership adds `tools/design/test_design.py` as a ninth file solely to import `AuthoredDifficultyAccountsTests` from the new module, following the existing explicit unittest registration. The global documentation gate runs this file and would otherwise omit the new finance regressions. This is a required integration correction; it changes none of the accepted account/validation semantics. The earlier eight-file list records the original assignment and is superseded for this one registration. The derived overflow regression and the other implemented prospective cases must execute through this mandatory entry as well as the focused command.
