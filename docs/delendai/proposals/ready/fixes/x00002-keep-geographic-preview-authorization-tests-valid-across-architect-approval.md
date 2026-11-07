---
id: x00002
title: "Keep geographic preview authorization tests valid across architect approval"
kind: fix
status: ready
type: proposal
track: general
date: 2026-11-07
---

# x00002 — Keep geographic preview authorization tests valid across architect approval

## goal

Allow the architect to authorize i00015/S3 after accepted S2 without making the native regression suite require a permanently unauthorized canonical plan.

## why

S2 was accepted at d07fe11a/e72c4a. Two tests still hard-code the real plan's authorization as false. A legitimate S3 authorization would therefore fail test:export. The correction source is 228ee9e, preserved in the official i00015/S2 generation4 unit when the post-acceptance defect was discovered. DelendAI refuses reopening an accepted slice, so this separate fix owns its independent review. S3 must wait for this fix's acceptance; no actual plan authorization is part of this delivery.

## non-goals

- No production-code, historical-plan, binding, source, campaign, string, geographic or public-export change. No native/game approval or mass authoring.

## slices

- global_gate: e2e

### S1 — Exercise authorization independently and preserve source decisions
- **Status**: pending
- **Files**: `tests/fixtures/native-history/test_private_geographic_preview.py`
- **Gate**: e2e
- acceptance:
  - "An isolated canonical-path plan explicitly set false rejects as unauthorized, without modifying the real plan."
  - "An isolated true plan still rejects missing pinned binding inputs. Authorization is never a bypass of input validation."
  - "The synthetic native fixture preserves the exact real source bytes and whichever authorization value the architect set; historical/game flags remain false. Focused boundary and actual native preservation cases pass, followed by the official validate gate and different-model review."

## acceptance

- Keep the existing S2 approval intact and record the correction separately. Never require the architect's development authorization to stay false forever, never promote that authorization to historical or engine approval, and keep i00015/S3 waiting for independent acceptance of this fix.
