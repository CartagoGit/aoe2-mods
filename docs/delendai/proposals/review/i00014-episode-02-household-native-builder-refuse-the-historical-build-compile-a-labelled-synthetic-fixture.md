---
id: i00014
title: "Episode-02 household native builder: refuse the historical build, compile a labelled synthetic fixture"
kind: infra
status: review
type: proposal
track: campaign-design
date: 2026-10-27
last-transition-id: c2a881b5-b934-47ba-9cac-2d85809f83cb
last-correlation-id: c2a881b5-b934-47ba-9cac-2d85809f83cb
last-transition-from: in-progress
last-transition-at: 2026-10-27T19:46:22.321Z
---

# i00014 — Episode-02 household native builder: refuse the historical build, compile a labelled synthetic fixture

## goal

Give episode 02 the missing build entry point: a builder that verifies the real authored source, refuses a historical Jerusalem build with the exact named blockers, and compiles the household ledger controller on a separately labelled synthetic physical fixture, with receipts that state the historical and game gates are still open.

## why

The architect's episode-02 decision and layout review name a missing capability precisely: "a builder must reject it as a historical build until those gates close. Controller compilation can advance on a separately labelled synthetic fixture", and "Builder acceptance must require an explicit approved topographic/route decision and real native footprint inspection. In particular, the empty map.corridors and nativeElevation: null in this draft are blockers, not instructions to create a flat open map or silently reuse the coastal painter." Today no such builder exists: tools/python/build_delivery_episode.script.py is hard-wired to the episode-01 Caesarea binding, so the episode-02 household controller that is already implemented and reviewed (product 111d4967, integrated 5bdd1fa3) has no build entry point at all. The private binding draft is not merely unapproved but uncompilable: its empty corridors leave the guide circuit's mark-alternative-route effect without its authored relief corridor, so the adapter correctly refuses it. Without a builder the second private episode cannot be produced at all, and the risk is that someone fills the gap by painting a flat open map or reusing the coastal painter, which is exactly what the architect forbids. This slice adds the missing entry point and keeps the historical gates visible.

## non-goals

- No historical Jerusalem build, campaign container, mod or release; the builder has no code path that can emit one.
- No new native capability, composed v2/v3 export, schema, public contract, string identity, ID range or campaign source change.
- No duplication of the payment, spatial, repair-HP, caption, reserved-payout or terminal-closure logic: the builder reuses the household adapter, the shared base factory and the optional-circuit adapter.
- No geography, route, terrain, elevation or footprint decision: the unresolved route and native elevation stay visible as blockers instead of being invented.
- No engine, gameplay, balance, localisation or historical approval; gameVerified stays false.
- No second controller module: the existing household adapter remains the only household-ledger controller.

## slices

- global_gate: e2e

### S1 — Episode-02 household builder with historical-build refusal and a labelled synthetic compile
- **Status**: review
- **Files**: `tools/python/build_household_episode.script.py`, `tests/fixtures/native-history/test_native_household_controller.py`, `docs/qa/campaign-design/household-ledger-builder.md`
- **Gate**: e2e
- acceptance:
  - "Verify the authored source through the binding's own sourceSha256, campaignId, episodeId and per-difficulty starting-resource vectors, and fail closed on any mismatch instead of continuing with a changed source."
  - "Refuse a historical build by reporting the binding's own named blockers (no approved route, no native elevation, no footprint inspection, binding not approved for a historical build) and leave the builder with no code path that can emit a historical Jerusalem campaign, container or mod."
  - "Compile the household controller on a separately labelled synthetic physical fixture derived from the binding's semantics, reusing the existing household adapter, shared base factory and optional-circuit adapter; keep the nonhistorical label in the scenario identity, the messages and the receipt, and record the real blockers, the synthetic label and the open game and historical gates."
- review-state: in_review
- review-implementer: minimax-m3.1-flash-preview
- shipped-in: `e63985d11326`

## acceptance

- Verify the authored source through the binding's own sourceSha256, campaignId, episodeId and per-difficulty starting-resource vectors, and fail closed on any mismatch instead of continuing with a changed source.
- Refuse a historical build by reporting the binding's own named blockers (no approved route, no native elevation, no footprint inspection, binding not approved for a historical build) and leave the builder with no code path that can emit a historical Jerusalem campaign, container or mod.
- Compile the household controller on a separately labelled synthetic physical fixture derived from the binding's semantics, reusing the existing household adapter, shared base factory and optional-circuit adapter; keep the nonhistorical label in the scenario identity, the messages and the receipt, and record the real blockers, the synthetic label and the open game and historical gates.
