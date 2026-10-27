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

The25negative/source-gate cases are prospective acceptance requirements. They have **not** been run against an implemented opt-in factory, because that operation does not yet exist. The cases distinguish malformed source, protected/reward borrowing, contradictory aliases, missing actual task inputs and an unapproved nonzero bank. A path may study a bank financially while remaining blocked for content/native approval; do not conflate the two gates.

## Closed implementation assignment after independent S1 acceptance

S2 owns only `tools/design/episode_dossier.factory.py`, `tools/design/authored_difficulty_accounts.helper.py` and `tools/design/test_authored_difficulty_accounts.py`. The helper validates/derives the new source envelope; the existing factory still composes the dossier. Reuse current resource normalization and optional-state functions. Do not duplicate the solver, optional mechanics, renderer, source schema or native exporter.

If the existing three-argument `difficulty_profiles` needs actual side rows, add a compatible optional internal argument. Absence of those rows under the opt-in is an error; it cannot fall back to guessed preset costs. Calls without the opt-in keep their previous behavior. Extract side costs/rewards from actual built predicates/effects, with duplicate side IDs and unsafe sums rejected before analysis.

Verify the real factory with all three positive cases and meaningful negative cases; compare every one of the64current legacy/v3 dossier outputs against its baseline when the field is absent, without changing their source files or catalogue counts. Preserve fingerprint/source/ID/state semantics and all unchanged default results. Complete `bun run validate` and official certification; a different model reviews the exact implementation. This packet does not grant self-approval, broad historical authoring or a native exporter bypass.

A later jewish-tradition03 packet may use the accepted operation. Its screen inventory, fiction/source distinction, real frame, actor routes, optional benefits, deadlines and continuation require their own closed decisions. Different budgets alone do not prove a satisfying challenge.
