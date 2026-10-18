---
id: i00007
title: "Alternative fulfillment plans with atomic reservation and persistent recipe identity"
kind: infra
status: ready
type: proposal
track: campaign-design
date: 2026-10-18
---

# i00007 — Alternative fulfillment plans with atomic reservation and persistent recipe identity

## goal

Record and resolve the missing reusable alternative-fulfillment operation exposed by the design-only Constantinople380 allocation study. Current contracts and native exporter do not implement recipe choice, joint reservation or branch-qualified outputs. Preserve all existing schemas, IDs and historical campaign identities until a separately reviewed architecture decision explicitly authorizes a compatible capability design. No historical authoring is unlocked.

## why

Reproduction: docs/research/odyssey-research/imperial34-care-allocation-plan.json and its checked report enumerate nine two-service combinations with all-skip affordability9/7/3. This internal accounting is not gameplay DSL. Existing objective predicates are composed with all and fixed payment receipts; prose, multiple simultaneous fixed debits, route-progress keys and a derived token cannot safely stand in for an exclusive recipe. The final dossier is still pending; reject this approach if real world geometry and native pilots reveal only a menu and idle walking.

## non-goals

- No changed public campaign contracts, existing string/progress ranges or campaign identity as a content workaround.
- No completed Constantinople dossier, authenticated historical care service, 380church parcel, played balance or native support claimed from the accounting study.
- No new global timer, creed test, ownership-transfer proxy, auto choice, unlimited exchange or MiniMax architecture assignment.

## slices

- global_gate: e2e

### S1 — Architect decision and explicit choice/reservation semantics
- **Status**: review
- **Files**: `docs/architecture/alternative-fulfillment.md`, `docs/qa/alternative-fulfillment/decision`
- **Gate**: type
- acceptance:
  - "Inspect installed contracts/reference/native operations and issue a bounded ADR choosing a proven reuse path or an explicit compatible capability design; do not alter existing contracts merely to make this episode pass."
  - "Specify unique service/recipe identity, preview without debit, exactly one choice per service, joint affordability and atomic reservation, once-only debits, pre-work cancellation versus post-work commitment, explicit refund/recovery/lost-output behavior and defeat-first terminal handling."
  - "State exact output identities, prerequisites, physical reception and survivor rules; payment is neither delivered cargo nor ownership/belief. Define save/load and all-skip/all-complete/three-portfolio acceptance. Independent review required before implementation."
- review-state: in_review
- review-implementer: gpt-6

### S2 — Only after ADR: compatible reference implementation and compiler rejection
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `packages/schemas`, `packages/gameplay-state`, `packages/gameplay-validation`, `packages/scenario-compiler`, `tests/alternative-fulfillment/reference`
- **Gate**: type
- acceptance:
  - "Proceed only under the accepted S1 design; retain preexisting profile/source compatibility, IDs and fixtures. Reuse actual resource transactions and immutable reducer; do not copy the reference engine or simulate an unimplemented native operation as available."
  - "Adversarial tests: all nine candidate combinations per difficulty; unaffordable joint transaction no partial debit; repeated/reentered/loaded selection no second charge/output; mixed recipe receipts, cancellation after commitment, wrong/duplicate output, optional reward before payment, lost recipient and terminal races."
  - "Keep unsupported native export rejected explicitly. A resource-state enumeration and reference tests are not native or game evidence."

### S3 — Native composition, bilingual choice UI and bounded engine evidence
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `packages/aoe2-adapter`, `tools/python`, `tests/fixtures/native-alternative-fulfillment`, `templates/native/alternative-fulfillment`
- **Gate**: e2e
- acceptance:
  - "External prerequisites: existing i00003 native composition, template/input support and s00001 engine verification are required; pending external gates remain pending. Never mark this implementable from local slice dependency alone."
  - "Native UI shows both services, complete costs, remainder and work before explicit confirmation; no fabricated menu in campaign progress variables. Actual reservations, cancellation, recipe-qualified outputs and actor receptions must agree with reference across save/load and all difficulties."
  - "Run bun run validate and bun run test:export, real round-trip and xs-check where applicable, then actual AoE2 evidence with build/hash/locale/profile for duplicate clicks, insufficient stock, optional order, wrong output, loss and terminal. Mechanical content authoring remains blocked until architect and independent review accept the resulting gameplay."

## acceptance

- Inspect installed contracts/reference/native operations and issue a bounded ADR choosing a proven reuse path or an explicit compatible capability design; do not alter existing contracts merely to make this episode pass.
- Specify unique service/recipe identity, preview without debit, exactly one choice per service, joint affordability and atomic reservation, once-only debits, pre-work cancellation versus post-work commitment, explicit refund/recovery/lost-output behavior and defeat-first terminal handling.
- State exact output identities, prerequisites, physical reception and survivor rules; payment is neither delivered cargo nor ownership/belief. Define save/load and all-skip/all-complete/three-portfolio acceptance. Independent review required before implementation.
- Proceed only under the accepted S1 design; retain preexisting profile/source compatibility, IDs and fixtures. Reuse actual resource transactions and immutable reducer; do not copy the reference engine or simulate an unimplemented native operation as available.
- Adversarial tests: all nine candidate combinations per difficulty; unaffordable joint transaction no partial debit; repeated/reentered/loaded selection no second charge/output; mixed recipe receipts, cancellation after commitment, wrong/duplicate output, optional reward before payment, lost recipient and terminal races.
- Keep unsupported native export rejected explicitly. A resource-state enumeration and reference tests are not native or game evidence.
- External prerequisites: existing i00003 native composition, template/input support and s00001 engine verification are required; pending external gates remain pending. Never mark this implementable from local slice dependency alone.
- Native UI shows both services, complete costs, remainder and work before explicit confirmation; no fabricated menu in campaign progress variables. Actual reservations, cancellation, recipe-qualified outputs and actor receptions must agree with reference across save/load and all difficulties.
- Run bun run validate and bun run test:export, real round-trip and xs-check where applicable, then actual AoE2 evidence with build/hash/locale/profile for duplicate clicks, insufficient stock, optional order, wrong output, loss and terminal. Mechanical content authoring remains blocked until architect and independent review accept the resulting gameplay.
