---
id: i00012
title: "Reuse one strict shared profile projection within each fulfillment validation call"
kind: infra
status: ready
type: proposal
track: general
date: 2026-10-27
---

# i00012 — Reuse one strict shared profile projection within each fulfillment validation call

## goal

Remove repeated strict v3-to-v2 projection within one synchronous validation/presence call, preserving public APIs, every rejection and all 95 portfolio checks; recover reliable official gate without changing timeouts or cross-call caching.

## why

The architect's isolated Yavneh docs validate locally (158 tests/2,138 expectations; the95portfolio test23.23s and25.52s), but three official candidate gates rejected on preexisting30s/5s timeouts. Attempts02 and03 completed all2,138 expectations while the95portfolio test took31.08s and35.62s. Preserve these failures; do not change tests/timeouts or claim a landed candidate.

Source inspection finds `validateFulfillmentSnapshot` parses the identical shared v2 projection twice per synchronous call; `fulfillmentPresent` parses it once for each selected result/recipient. A bounded local reuse eliminates those duplicate parses without reusing trust across calls. A same-process60-iteration microbenchmark observed113ms for shared projection,197ms for full fingerprint,404ms for snapshot validation. These are diagnostic observations, not a performance SLA. Reusing an Intl.Collator offered no material improvement and is not part of this proposal.

## non-goals

- No global/WeakMap/profile-identity cache, caller-supplied trusted context, frozen-profile requirement, skipped schema/fingerprint/snapshot validation, or new public contract.
- No reduced95matrix coverage, timeout/test runner/config changes, canonical serialization changes, native support, campaign changes or historical content approval.

## slices

- global_gate: type

### S1 — Local projection reuse and regression evidence
- **Status**: pending
- **Files**: `packages/gameplay-state/fulfillment-snapshot.factory.ts`, `tests/alternative-fulfillment/reference/fulfillment-projection-reuse.test.ts`
- **Gate**: type
- acceptance:
  - "In validateFulfillmentSnapshot compute sharedCapabilityProfile(profile) once locally; pass that same strictly parsed value to validateFulfillmentCore and capabilityFingerprint. In fulfillmentPresent compute it once before the selected-result/recipient predicate loop. Preserve short-circuit and malformed-profile behavior, public signatures, schema/fingerprint algorithms, every state/receipt/account/presence check, and source immutability. If eager projection changes inactive-plan behavior, retain the existing early return before computing."
  - "Retain all existing95portfolio/adversarial cases unchanged. Add meaningful regression that mutating the same profile object between distinct validation calls still rejects contract mismatch; changed result/recipient presence still fails; no cache or source mutation. Compare exact baseline fingerprints and replay outcomes on the existing fixture, and capture bounded before/after timings without flaky timing assertions."
  - "Root and independent model review exact diff; bun run validate and official frozen-install/validate gate pass without timeout adjustment. No native adapter change; export only if a new concern warrants it. Product integration does not close any historical content slice."

## acceptance

- Strict validation and results remain equivalent; reuse is local to one invocation.
- Gate evidence preserves previous rejected attempts and reports measured improvement with its environmental limits.
- Independent approval required; implementer never approves itself.
