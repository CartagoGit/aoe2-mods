---
id: i00013
title: "Author explicit finite difficulty accounts without compensating legacy resource banks"
kind: infra
status: ready
type: proposal
track: general
date: 2026-10-27
---

# i00013 — Author explicit finite difficulty accounts without compensating legacy resource banks

## goal

Add an explicit opt-in authoring path for independently specified difficulty accounts in the existing legacy dossier factory; preserve default output and all public gameplay contracts, distinguish spendable/finite bank/protected recovery/once-only reward reserve, and prove actual all-skip/all-complete feasibility without automatic budget compensation.

## why

The current legacy factory computes `bank = main + protected + replacement + rewardReserve + margin - start` and `accessible = start + bank - rewardReserve`. Start changes are compensated by the bank: the accessible total becomes main + protected + replacement + margin at every difficulty. The current audit has63identical accessible budgets; this alone does not prove identical gameplay because authored opposition and phase deadlines can vary. No existing proposal found in the read-only inventory enables explicit legacy accounts; i00008 is the separate supported v3 opt-in. Do not force a distributed-note mission into an exclusive recipe plan to obtain per-difficulty accounting.

This is a missing authoring-factory capability, not a public gameplay-contract defect. Keep all current64dossiers/source IDs and default output intact. An explicit new path must disclose its own accounts and refuse an inconsistent or infeasible source instead of silently creating a compensating bank.

## non-goals

- No mass rewrite or historical approval of64dossiers, no numeric/string/progress identity changes, no v3 recipe coercion, native bank/spawn implementation or played balance claim.
- No automatic compensation, negative bank, optional reward borrowing, double-counted allowance, protected recovery spending, renewable resource or timeout chosen merely to make difficulty labels different.

## slices

- global_gate: type

### S1 — Architect account boundaries and compatibility decision
- **Status**: pending
- **Files**: `docs/architecture/authored-difficulty-accounts.md`, `docs/qa/campaign-design/authored-difficulty-accounts-cases.json`
- **Gate**: type
- acceptance:
  - "Define a source-only opt-in authoredDifficultyAccounts with exactly easy/standard/hard and each record exactly spendable, gatherableBank, protectedRecovery, optionalReserve; each requires exact four-resource keys, reuses existing numeric resource normalization and adds a safe-integer bound including intermediate sums at the new source boundary. The existing Python normalizer alone does not enforce that ceiling. No field means complete old behavior and byte-identical default outputs. No gameplay schema widening is authorized."
  - "Emit existing difficulty fields from those explicit values: startingResources=spendable S, gatherableBank=B, protectedRecoveryStock=P, accessibleWithoutOptionalRewards=S+B (P/R excluded); replacementBudget Z is the existing common planning reserve within spendable, not another credited account. Main feasibility requires S+B >= mandatory M + Z. R equals the exact authored once-only positive side reward sum, never spendable before award; no reward reserve is added to B. If protectedRecoveryStock is also authored outside the opt-in it must agree with P rather than silently conflict. Under the opt-in omit obsolete startingResources/discretionaryMargin inputs or reject conflicting duplicate inputs by a documented rule."
  - "Decide all-optional affordability through the actual shared finite_allocation.optional_states/balance on authored side costs/rewards after M and Z are excluded, with no preset substitution. Preserve payment-before-reward, seven/eight once-flags and exact R exhaustion. A financial witness assumes spatial predicates and finite bank collection; bank0 must be used until actual gathering placement is separately approved. Native/end-to-end difficulty stays pending. Independent review precedes implementation."

### S2 — Reuse the existing factory and finite analyzer
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `tools/design/episode_dossier.factory.py`, `tools/design/authored_difficulty_accounts.helper.py`, `tools/design/test_authored_difficulty_accounts.py`
- **Gate**: type
- acceptance:
  - "Implement only the independently accepted source-only branch, reusing current strict resource validators and actual optional-state analyzer; no second economy/solver or preset assumptions. Keep the legacy three-argument helper call compatible if adding optional objective inputs internally. Refuse missing task inputs for the opt-in; no fake success."
  - "Under the opt-in set reallocatedCacheAllowance to the same R account, not a second legacy600F300W150G promise. Keep secondaryBudget reservedRewards/maxOptionalCosts consistent with actual source predicates/effects and preserve default outputs when absent. No native capability is claimed."
  - "Exercise the real factory on bounded artificial source: independently different easy/standard/hard spendable and B0, nonzero protected recovery, exact reward reserve, all-skip and all-complete witnesses, zero and positive authored costs, unaffordable payment-before-reward, duplicate/unknown/missing keys, booleans/fractions/overflow, conflicting aliases, infeasible and negative vectors. Compare all64current legacy/v3 dossiers for no source/output drift when the field is absent."

### S3 — Independent acceptance and bounded content use
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `docs/qa/campaign-design/authored-difficulty-accounts-review.md`, `docs/handoffs/LLM-WORK-ALLOCATION.md`
- **Gate**: type
- acceptance:
  - "Different actual model reviews the exact implementation and complete default compatibility evidence; bun run validate and official gate pass. Do not self-approve."
  - "A separately designed jewish-tradition03 candidate may use B0 and explicit accounts only after acceptance; every route, objective, screen, timing and historical/source decision remains its own architect packet. No canonical dossier count or historical-authoring unlock is implied by this infrastructure."

## acceptance

- Missing factory operation is explicit; no executable source is advertised before implementation and independent acceptance.
- Both accounts and actual difficulty levers have traceable intended effects, while static feasibility remains distinct from AoE2 playtesting.
