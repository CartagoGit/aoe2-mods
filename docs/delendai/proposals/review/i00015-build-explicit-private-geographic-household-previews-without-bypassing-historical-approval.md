---
id: i00015
title: "Build explicit private geographic household previews without bypassing historical approval"
kind: infra
status: review
type: proposal
track: general
date: 2026-11-05
shipped-in:
  - "5020d0b6fe117f0c1e98a75bf06db70cacf83452"
  - "2c56e3eb9d162d72a5691c02a8423c01bdc532b1"
  - "d07fe11aae2f0142f540d1048931e14a0465d95f"
last-transition-id: f159b470-3453-426f-a894-0b6efc8e88e4
last-correlation-id: f159b470-3453-426f-a894-0b6efc8e88e4
last-transition-from: in-progress
last-transition-at: 2026-11-07T22:08:43.052Z
---

# i00015 — Build explicit private geographic household previews without bypassing historical approval

## goal

Add a bounded private household build path that reuses the supported native base/controller and verified geographic raster pipeline, records modern-reference uncertainty, preserves the synthetic fixture and public exporter refusal, and separates compilable development previews from historical approval and engine evidence.

## why

The synthetic household builder correctly refuses every historical build, so it cannot create the georeferenced development artifact needed for later engine inspection. Existing DSM extraction/quantisation and native base/controller are reusable. The first campaign can progress privately without falsely promoting modern relief, unknown collision or unplayed difficulty to historical approval.

## non-goals

- No public schema/export widening, campaign identity or string changes, historical approval, native navigation claim, artificial terrain flattening, full historical campaign, release or paid media.

## slices

- global_gate: type

### S1 — Architect private preview contract and geographic decisions
- **Status**: done
- **Files**: `docs/architecture/private-geographic-preview.md`, `docs/handoffs/PRIVATE-GEOGRAPHIC-PREVIEW-PACKET.md`, `docs/wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/25-private-geographic-preview-plan.json`, `docs/delendai/proposals/review/i00015-build-explicit-private-geographic-household-previews-without-bypassing-historical-approval.md`
- **Gate**: type
- acceptance:
  - "Define explicit development compilation separately from historical/native/engine approval; preserve synthetic and public-export refusals; no build-before-playtest cycle. Candidate authorization remains false until separately reviewed real S3 inputs."
  - "Pin actual sources,340frame,modern bands,17originals/10zones,continuous corridor envelope,half-cell convention and one explicitly bounded store override; retain source binding and unknown hydrology/collision. No source/ID/schema or dossier count change."
  - "Independent review of the reuse boundary, exact S2 ownership, failure modes and evidence; no unimplemented operation or prospective case is claimed executed."
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6.1-terra
- review-log: approved by gpt-6.1-terra — verified at 2c56e3eb9d16, validate exit 0 and tests 164/164 claimed, no recorded run cited; acceptance 3/3: (1) Architecture and plan false flags reviewed, existing historical refusal retained. (2) Input SHA256 verified, binding counts, geometry, raster and override independently checked. (3) Eleven S2 files and entry points reviewed, size-range P2 fixed, S2/S3 pending. — Independent source review 5020d0b, af91123, 1a4dac3 and 9a9c757 landed 2c56e3e. Earlier P2 size range fixed; helper boundaries 299/300/400/401 independently verified. Source hashes, 17 bodies/10 zones, frame, candidate raster, corridor and bounded override checked; actual implementation, historical and game approval remain pending. Official validate 164 tests/2159 assertions, journal archived.
- shipped-in: `2796a36557a3`

### S2 — Reusable private base, strict plan boundary and geographic preview compiler
- **Status**: done
- **DependsOn**: [S1]
- **Files**: `tools/python/private_household_base.factory.py`, `tools/python/private_native_artifact.service.py`, `tools/python/build_household_episode.script.py`, `tools/python/private_geographic_preview.validator.py`, `tools/python/build_geographic_household_preview.script.py`, `tools/map/geographic_corridor_audit.helper.py`, `tests/fixtures/native-history/test_private_geographic_preview.py`, `tests/maps/test_geographic_corridor_audit.py`, `tests/maps/geographic-corridor-audit.test.ts`, `tools/cli/native-fixtures.validator.ts`, `tools/cli/chronicles.script.ts`
- **Gate**: e2e
- acceptance:
  - "Implement only accepted S1; reuse actual geographic pipeline/native base/controller/signature, no copied world solver or public fallback. Preserve default synthetic semantic signature/XS and all65dossier outputs; keep real plan unauthorized in this implementation slice."
  - "Meaningful accepted artificial fixtures and strict negatives for authorization,unknown keys,bool/nonfinite/out-of-range dimensions/bands,source/hash/CRS/half-cell/grid drift,corridor endcaps/even widths/known water,nodata,unlisted identity/zone/position change,stored evidence flags and input mutation. Derived binding evidence is recomputed; no terrain flattening or source hiding."
  - "Register corridor tests in the Bun gate and native fixture discovery in the existing test:export path, failing empty discovery and reporting actual skips. Real native write/reopen/terrain+controller signature and XS pass; bun run validate and test:export plus official gate and different-model review. Never mark a compilation case engine/historical approval."
- review-state: done
- review-implementer: gpt-6-luna
- review-reviewer: gpt-6.1-terra
- review-log: approved by gpt-6.1-terra — verified at d07fe11aae2f, validate exit 0 and tests 122/122 claimed, no recorded run cited; acceptance 3/3: (1) Reviewed landed source, original plan false, six legacy semantic and XS comparisons identical, public refusal unchanged. (2) Reviewed fixture and validation implementation, fixed prior independent findings and verified changed same-path TIFF probe; implementer focused 52 tests passed. (3) Official gate passed validate on d07fe11; implementer test:export exit 0, native 122 passed and zero skipped, corridor Python 15 and wrapper 1 passed; this rev… — Independent review of S2 landing d07fe11; official publish gate bun install and bun run validate passed; test:export 122 native tests, zero skipped; focused fixture 52, corridor 15 and Bun wrapper 1 passed in implementer logs. Original real plan remains unauthorized. No historical, engine, or gameplay approval.
- shipped-in: `f77346ff086e`

### S3 — Architect-authorized Jerusalem development build and progressive private handback
- **Status**: review
- **DependsOn**: [S2]
- **Files**: `docs/wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/25-private-geographic-preview-plan.json`, `docs/handoffs/PRIVATE-JERUSALEM-GEOGRAPHIC-PREVIEW.md`, `docs/qa/campaign-design/jerusalem-private-geographic-preview-build.json`
- **Gate**: e2e
- acceptance:
  - "Independently verify real source/grid/corridor/body evidence and authorize only this development plan through architect-owned changes; do not set historical binding approval true. Build six private EN/es-ES/difficulty variants with actual hashes,write/read/XS and scope limits."
  - "Preserve original Caesarea kit/hash. If packaging progressive chapters use the pinned campaign utility and exact existing episode01/02 ordering; no final campaign progress flag, public distribution or production-ready claim. Actual episode03continuation remains."
  - "Guide records controls and real Windows/Steam/es-ES test cases: geometry/pathfinding/collision/save-load/terminal/optional utility/difficulty with build/hash; pending observations stay pending and do not block producing the artifact that enables them."
- review-state: in_review
- review-implementer: gpt-6
- shipped-in: `5cd14b3bc848`

## acceptance

- Reuse verified operations and explicitly implement the missing private path; no fictional support, historical approval or game evidence.
- Source campaign/identity/screens and the old synthetic/default outputs remain intact.
- Independent reviews and real gates separate authored decisions, native compilation and actual gameplay.
