---
id: d00003
title: "Synchronize the fulfillment reference handoff after independent approval"
kind: docs
status: ready
type: proposal
track: campaign-design
date: 2026-10-23
---

# d00003 — Synchronize the fulfillment reference handoff after independent approval

## goal

Keep architecture and MiniMax instructions aligned with the integrated i00007 reference delivery, distinguishing decision approval, reference approval and unsupported native/game capabilities. Recover live DelendAI states before editing; record pending external gates and preserve campaign identities and counts.

## why

Existing handoffs still describe every i00007 slice as pending. A bounded documentation unit avoids mixing handoff files outside the implementation scope or claiming completion of d00002.

## non-goals

- No native implementation or engine certification.
- No historical campaign generation, new dossier or campaign/source/string identity change.
- No closing d00002 or unblocking historical content authoring.

## slices

- global_gate: none

### S1 — Align architecture and MiniMax workflow with the verified reference state
- **Status**: pending
- **Files**: `docs/architecture/overview.md`, `docs/handoffs/MINIMAX-M3.1-START.md`, `docs/handoffs/MINIMAX-M3.1-WORKFLOW.md`, `docs/handoffs/MINIMAX-M3.1-NEXT-PROPOSALS.md`, `docs/handoffs/MINIMAX-M3.1-QUALITY-GATES.md`, `docs/qa/campaign-design/fulfillment-handoff-independent-review.md`
- **Gate**: none
- acceptance:
  - "After i00007/S2 formal approval is visible in the official server, document exact integrated provenance and the opt-in v3 boundary with unchanged v2 source/IDs and explicit native rejection."
  - "Remove stale all-slices-pending instructions; keep i00007/S3 external i00003 and s00001 gates, 63 design drafts / 215 selections without dossiers, and f00001/S1 as the only designated starting task for MiniMax."
  - "Run bun run validate and obtain independent review by a different model; publish through DelendAI without manual integration-branch changes."

## acceptance

- After i00007/S2 formal approval is visible in the official server, document exact integrated provenance and the opt-in v3 boundary with unchanged v2 source/IDs and explicit native rejection.
- Remove stale all-slices-pending instructions; keep i00007/S3 external i00003 and s00001 gates, 63 design drafts / 215 selections without dossiers, and f00001/S1 as the only designated starting task for MiniMax.
- Run bun run validate and obtain independent review by a different model; publish through DelendAI without manual integration-branch changes.
