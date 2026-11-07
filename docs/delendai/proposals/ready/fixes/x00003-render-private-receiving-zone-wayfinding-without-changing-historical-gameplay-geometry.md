---
id: x00003
title: "Render private receiving-zone wayfinding without changing historical gameplay geometry"
kind: fix
status: ready
type: proposal
track: general
date: 2026-11-07
---

# x00003 — Render private receiving-zone wayfinding without changing historical gameplay geometry

## goal

Give the private Jerusalem preview ten localized receiving-zone flags and revealers by extracting the already working Cesarea marker operation, then rebuild an honestly labelled private revision with actual native/container evidence.

## why

The accepted geographic build861e718 and review7cd39fb preserve the17originals but never call the marker loop in `build_delivery_episode.script.py::paint_world`. Their ten receiving zones exist as XS circles and source labels; they have no initial FLAG_A or MAP_REVEALER. FLAG_B appears only after an optional guide action. The guide's destination controls are therefore inadequately visible on a340map. The kit37f4db30 remains immutable evidence of native compilation and container integrity; it is not a verified playable delivery. Root and Terra confirmed this missing call by source inspection after the earlier technical acceptance.

The [closed correction packet](../../../../wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/27-private-receiving-wayfinding-fix.md) specifies the implementation boundary. Verify its relative path when moving this proposal between status folders; no operation is implemented by this document.

## non-goals

- No historical terrain, road or footprint reconstruction, source/ID/schema/string change, economic or objective modification, terrain painting/flattening, paid media, public export or distribution.
- No marker is a new source actor, payer, household or optional participant. No game observation or calibrated difficulty is claimed.

## slices

- global_gate: e2e

### S1 — Extract and reuse native receiving annotations
- **Status**: pending
- **Files**: `tools/python/private_wayfinding.renderer.py`, `tools/python/build_delivery_episode.script.py`, `tools/python/build_geographic_household_preview.script.py`, `tests/fixtures/native-history/test_private_wayfinding.py`, `tests/fixtures/native-history/test_private_geographic_preview.py`
- **Gate**: e2e
- acceptance:
  - "Extract only the existing FLAG_A + localized name trigger + MAP_REVEALER operation. Cesarea retains its own coast validation, terrain paint and easy-path assistance in their previous order/behaviour; preserve its native semantic signature/XS against a captured prechange baseline, with EN/es and difficulty cases. No pin change or source rebinding."
  - "Invoke the shared renderer in the geographic builder after household compilation and before native write/read/XS. Exactly ten labelled receivers add20auxiliary units and10label triggers;17source originals, original controller XS/variables/triggers, sources, geometry and every terrain cell/type/elevation remain intact. Both fixture and modern geographic variants record actual marker provenance, references, centres and labels in receipts. The old nongeographic64synthetic household wrapper is unchanged."
  - "Native positive EN/es cases and strict malformed/duplicate/nonfinite/unsupported-label failures verify actual serialized objects, labels, preserved originals and terrain; reject before partial mutation. Existing test:export discovery executes meaningful new cases, reports actual skips and passes. Official validate gate and independent different-model review are required before S2 rebuild."

### S2 — Rebuild the private Jerusalem revision and correct the handback
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/handoffs/PRIVATE-JERUSALEM-GEOGRAPHIC-PREVIEW.md`, `docs/qa/campaign-design/jerusalem-private-geographic-preview-build.json`
- **Gate**: e2e
- acceptance:
  - "After accepted S1, build actual six EN/es×difficulty variants with10localized FLAG_A/10MAP_REVEALER each, verify write/read/XS, sources, unchanged terrain and controller against prior outputs, then verify all12standalone/progressive containers by pinned listing/extraction and scenario hashes."
  - "Preserve both original Caesarea kit0d589ef2 and Jerusalem candidate37f4db30 unchanged. New r2 output has distinct filenames/hashes/revision; original chapter01bytes remain exact. Receipts distinguish17originals from20auxiliary annotations, and preserve per-chapter source provenance, rights notices and empty game observations."
  - "Guide explains flags and logical radius3receiving areas, without claiming painted modern-map road circles, measured collision, historical geography, a completed campaign or a game pass. Every release/engine/difficulty uncertainty remains explicit; actual gate and independent review precede this private handback."

## acceptance

- Make destinations inspectable through real reused native operations, preserving gameplay and georeferenced relief.
- Historical/engine/public-export approvals remain false. No earlier acceptance is misrepresented as a test of marker visibility in AoE2.
- Implementation is assigned only after root publishes this exact packet; MiniMax/Luna executes these named files and cases, and never redesigns the map or the mission to satisfy a test.
