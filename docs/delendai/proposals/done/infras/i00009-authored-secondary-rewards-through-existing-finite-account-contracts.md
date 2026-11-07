---
id: i00009
title: "Authored secondary rewards through existing finite-account contracts"
kind: infra
status: done
type: proposal
track: campaign-factory
date: 2026-10-25
shipped-in:
  - "2bd271486fba1b19376ff942a529fd6bb752db56"
  - "0cf4d064beddbd736de942c0510de0ffabeb753b"
  - "34f87ceca32d34afa20dd79483cda033cfa3d0b9"
last-transition-id: 43e18a82-91b1-423a-9f03-aadb6b6dd0be
last-correlation-id: 43e18a82-91b1-423a-9f03-aadb6b6dd0be
last-transition-from: review
last-transition-at: 2026-10-26T03:20:19.633Z
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
- shipped-in: `2bd271486fba`

### S2 — Reusable optional reward projection and budget derivation
- **Status**: done
- **DependsOn**: [S1]
- **Files**: `tools/design/secondary.py`, `tools/design/episode_dossier.factory.py`, `tools/design/test_authored_secondary_rewards.py`, `tools/design/test_design.py`
- **Gate**: type
- acceptance:
  - "Implement only the accepted internal authoring projection, reuse shared numeric primitives and existing objective builder, reject malformed and unsupported overrides, and preserve existing optional costs, identities, once-only effects and main independence."
  - "Derive all secondary accounting from the generated existing contracts rather than duplicated global reward assumptions; exercise zero and positive overrides, pre-reward affordability, isolated finite reserve, reload/repeated-completion protection already supplied by the existing reference, and invalid type/resource inputs."
  - "Prove all64 current dossiers,2645screens,398secondaries,49reference records, public schemas, previous outputs and native failure behavior remain unchanged; run focused Python/design checks and bun run validate with an artificial fixture, no historical modification."
- review-state: done
- review-implementer: gpt-6-luna
- review-reviewer: gpt-6
- review-log: approved by gpt-6 — verified at 0cf4d064bedd, validate exit 0 and tests 157/157 claimed, no recorded run cited; acceptance 3/3: (1) Reviewed four-file implementation and follow-up5481: resource_amounts strict validation, override eligible kinds only, omission legacy and explicit zero captio… (2) Independent focused3tests pass; full factory fixture and independent audit, generated effects/payments sums, fixed50wood/50gold costs, cache-overflow rejection… (3) Independent dossier--check64 and verify64/2645/398/49 zeroerrors; validate157/157 with2136assertions and3campaigns, includes registered112Python design tests. … — Independent review of gpt-6-luna implementation including hardened vector/mutation tests. Actual root commands/logs /tmp/i00009-root-{focused,dossiers-check,verify,validate}.log pass. Three criteria conform; unchanged64/2645/398/49, strict validation and derived finite budgets. No native/historical/game approval. Prior close_slice validate-required attempt did not close the slice; official product gate and this peer verdict are distinct.
- shipped-in: `0cf4d064bedd`

### S3 — Document supported commands and independent acceptance boundaries
- **Status**: done
- **DependsOn**: [S2]
- **Files**: `docs/guides/authored-secondary-rewards.md`, `docs/qa/authored-secondary-rewards/acceptance.md`
- **Gate**: type
- acceptance:
  - "Document the exact implemented input/output, supported reward kinds, rejection and legacy behavior, real commands/results and independent review status, with public contracts/native/game/historical gates explicitly unchanged."
  - "Keep Jerusalem70 and all other historical design choices in d00002; do not mark a useful reward, full dossier or historical mechanical packet approved merely because infrastructure tests pass."
- review-state: done
- review-implementer: gpt-6-luna
- review-reviewer: minimax-m3.1-flash-preview
- review-log: approved by minimax-m3.1-flash-preview — verified at 34f87ceca32d, validate exit 0 and tests 158/158 claimed, no recorded run cited; acceptance 2/2: (1) Verified line by line against the implementation. Input/output: optionalTasks[].resourceReward only, forwarded by build_dossier solely when present (tools/desi… (2) Both documents keep the historical boundary explicit. The guide states the feature does not write current historical blueprints, choose a reward for Jerusalem7… — Independent review of i00009/S3 (documentation slice) delivered by gpt-6-luna and submitted at 0a960cf; product integrated on develop at 34f87ce. Reviewer minimax-m3.1-flash-preview is distinct from the implementer gpt-6-luna and did not author the delivered files. The review round had been claimed by gpt-6 (chore(review): claim i00009) but that unit recorded no verdict, so the runtime removed it as unpublishable and the claim was released; I then claimed the review in my own review unit and verified everything below myself. Acceptance 2/2. Scope check: the delivery adds only docs/guides/authored-secondary-rewards.md (60 lines), docs/qa/authored-secondary-rewards/acceptance.md (32 lines) and 4 lines of proposal metadata; no code, schema, ID, string lock or native adapter change, and no out-of-scope file. Claim 1 verified against the code, not only the prose: the supported-kind set, the default bonus table, the fixed repair/trade costs, the rejection of the field for copy/guide/watch/scout including {}, the strict resource_amounts validation, the verbatim bilingual zero-reward captions, the 'Benefit/Ventaja ... once.' goal suffix and the reservedRewards/maxOptionalCosts derivation all match the source. Claim 2 verified: both documents keep the 64 dossiers as drafts with zero expanded approved dossiers, leave Jerusalem70 partial and disclaim history, geography, native and game evidence; verify.py reports expandedApprovedDossiers 0. Evidence run by this reviewer in the review unit: bun run validate exit 0, 158/158 tests across 14 files, 2138 expectations, docs:check valid, 3 campaigns validated; plus the focused python3 tools/design/test_authored_secondary_rewards.py 3/3, episode_dossiers.script.py --check 64 dossiers and verify.py 0 errors. ChangedSince note: the acceptance record quotes 157 Bun tests / 2136 expectations from the S2 unit run; the integrated tree now reports 158/2138 because the later i00003/S2 delivery (a7f8dcd, adding tests/maps/large-map-diagnostic.test.ts) landed after S2. That later commit is not a defect of this slice and was not judged here. Approval covers S3's documentation only. It does not approve any historical dossier, the Jerusalem70 design, native support, game verification or the blocked historical authoring proposals.
- shipped-in: `34f87ceca32d`

## acceptance

- Specify one optional internal authoring field resourceReward for existing finite-supply-withdrawal kinds only, using shared strict resource validation; omission preserves byte-identical legacy output and costs remain unchanged.
- Specify truthful zero-reward presentation, actual-contract-derived reward/cost budgets, finite reserved funding, failure cases and explicit no native/historical approval. Include a bounded real reproduction of the current missing projection and a closed artificial mechanical task.
- Implement only the accepted internal authoring projection, reuse shared numeric primitives and existing objective builder, reject malformed and unsupported overrides, and preserve existing optional costs, identities, once-only effects and main independence.
- Derive all secondary accounting from the generated existing contracts rather than duplicated global reward assumptions; exercise zero and positive overrides, pre-reward affordability, isolated finite reserve, reload/repeated-completion protection already supplied by the existing reference, and invalid type/resource inputs.
- Prove all64 current dossiers,2645screens,398secondaries,49reference records, public schemas, previous outputs and native failure behavior remain unchanged; run focused Python/design checks and bun run validate with an artificial fixture, no historical modification.
- Document the exact implemented input/output, supported reward kinds, rejection and legacy behavior, real commands/results and independent review status, with public contracts/native/game/historical gates explicitly unchanged.
- Keep Jerusalem70 and all other historical design choices in d00002; do not mark a useful reward, full dossier or historical mechanical packet approved merely because infrastructure tests pass.
