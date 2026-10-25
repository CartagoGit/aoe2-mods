---
id: i00009
title: "Authored secondary rewards through existing finite-account contracts"
kind: infra
status: ready
type: proposal
track: campaign-factory
date: 2026-10-25
shipped-in:
  - "2bd271486fba1b19376ff942a529fd6bb752db56"
---

# i00009 — Authored secondary rewards through existing finite-account contracts

## goal

Project explicitly authored finite optional resource rewards through the existing design factory and budget analysis, preserving every current dossier and public gameplay/native contract. Deliver an architect-reviewed narrow packet before assigning mechanical implementation.

## why

The Jerusalem70 root design exposed an authoring-projection limitation: tools/design/secondary.py always uses REWARDS[kind], while episode_dossier.factory.py independently sums the same global defaults. Existing secondary effect schemas already carry resource vectors and the reference supports finite reserved-account transfers, but the authoring path cannot express a deliberately different or zero resource reward. Do not add an otherwise unwanted main payment, healing, recruitment, enemy wave or fictional historical outcome merely to make a default reward useful. Register this limitation instead of advertising an unavailable authoring operation. The optional task's intrinsic outcome and its explicit instructions remain separate from a monetary bonus.

## non-goals

- No public schema, profile version, selected ID, campaign identity, chronology, string range or native adapter change.
- No configurable optional payment costs: repair/trade keep their existing actual operations and default fixed costs.
- No historical dossier insertion, authoring unlock, measured balance, localization approval or game/native support.
- No unrestricted secondary DSL, inferred benefits, new healing/spawn/speed operation, automatic content rewrite or reward funding from recovery.

## slices

- global_gate: type

### S1 — Architect decision, real reproduction and closed implementation packet
- **Status**: done
- **Files**: `docs/architecture/authored-secondary-rewards.md`, `docs/handoffs/AUTHORED-SECONDARY-REWARDS-PACKET.md`
- **Gate**: type
- acceptance:
  - "Specify one optional internal authoring field resourceReward for existing finite-supply-withdrawal kinds only, using shared strict resource validation; omission preserves byte-identical legacy output and costs remain unchanged."
  - "Specify truthful zero-reward presentation, actual-contract-derived reward/cost budgets, finite reserved funding, failure cases and explicit no native/historical approval. Include a bounded real reproduction of the current missing projection and a closed artificial mechanical task."
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6-luna
- review-log: approved by gpt-6-luna — verified at 2bd271486fba, validate exit 0 and tests 157/157 claimed, no recorded run cited; acceptance 2/2: (1) The decision and packet limit the field to aid/extract/repair/trade, reuse design_numbers.helper.py resource_amounts, preserve omitted defaults and fixed repai… (2) Decision gives exact EN/es-ES zero captions and invalid/misplaced cases, derives totals from actual effects and atomic-payment contracts, keeps finite reserved… — Independent review of i00009/S1 decision only at integrated product 2bd271486fba1b19376ff942a529fd6bb752db56. S2 implementation, native behavior, historical authoring, and S3 remain pending.

### S2 — Reusable optional reward projection and budget derivation
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `tools/design/secondary.py`, `tools/design/episode_dossier.factory.py`, `tools/design/test_authored_secondary_rewards.py`, `tools/design/test_design.py`
- **Gate**: type
- acceptance:
  - "Implement only the accepted internal authoring projection, reuse shared numeric primitives and existing objective builder, reject malformed and unsupported overrides, and preserve existing optional costs, identities, once-only effects and main independence."
  - "Derive all secondary accounting from the generated existing contracts rather than duplicated global reward assumptions; exercise zero and positive overrides, pre-reward affordability, isolated finite reserve, reload/repeated-completion protection already supplied by the existing reference, and invalid type/resource inputs."
  - "Prove all64 current dossiers,2645screens,398secondaries,49reference records, public schemas, previous outputs and native failure behavior remain unchanged; run focused Python/design checks and bun run validate with an artificial fixture, no historical modification."

### S3 — Document supported commands and independent acceptance boundaries
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `docs/guides/authored-secondary-rewards.md`, `docs/qa/authored-secondary-rewards/acceptance.md`
- **Gate**: type
- acceptance:
  - "Document the exact implemented input/output, supported reward kinds, rejection and legacy behavior, real commands/results and independent review status, with public contracts/native/game/historical gates explicitly unchanged."
  - "Keep Jerusalem70 and all other historical design choices in d00002; do not mark a useful reward, full dossier or historical mechanical packet approved merely because infrastructure tests pass."

## acceptance

- Specify one optional internal authoring field resourceReward for existing finite-supply-withdrawal kinds only, using shared strict resource validation; omission preserves byte-identical legacy output and costs remain unchanged.
- Specify truthful zero-reward presentation, actual-contract-derived reward/cost budgets, finite reserved funding, failure cases and explicit no native/historical approval. Include a bounded real reproduction of the current missing projection and a closed artificial mechanical task.
- Implement only the accepted internal authoring projection, reuse shared numeric primitives and existing objective builder, reject malformed and unsupported overrides, and preserve existing optional costs, identities, once-only effects and main independence.
- Derive all secondary accounting from the generated existing contracts rather than duplicated global reward assumptions; exercise zero and positive overrides, pre-reward affordability, isolated finite reserve, reload/repeated-completion protection already supplied by the existing reference, and invalid type/resource inputs.
- Prove all64 current dossiers,2645screens,398secondaries,49reference records, public schemas, previous outputs and native failure behavior remain unchanged; run focused Python/design checks and bun run validate with an artificial fixture, no historical modification.
- Document the exact implemented input/output, supported reward kinds, rejection and legacy behavior, real commands/results and independent review status, with public contracts/native/game/historical gates explicitly unchanged.
- Keep Jerusalem70 and all other historical design choices in d00002; do not mark a useful reward, full dossier or historical mechanical packet approved merely because infrastructure tests pass.
