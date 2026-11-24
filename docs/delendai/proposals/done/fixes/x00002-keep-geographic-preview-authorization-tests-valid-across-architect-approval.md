---
id: x00002
title: "Keep geographic preview authorization tests valid across architect approval"
kind: fix
status: done
type: proposal
track: general
date: 2026-11-07
shipped-in:
  - "f77346ff086eba263b1fb9aa6382f6cac16737cf"
last-transition-id: 61a1b22e-2fbe-4661-b0d3-9d28ceef76cf
last-correlation-id: 61a1b22e-2fbe-4661-b0d3-9d28ceef76cf
last-transition-from: ready
last-transition-at: 2026-11-07T22:26:31.482Z
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
- **Status**: done
- **Files**: `tests/fixtures/native-history/test_private_geographic_preview.py`
- **Gate**: e2e
- acceptance:
  - "An isolated canonical-path plan explicitly set false rejects as unauthorized, without modifying the real plan."
  - "An isolated true plan still rejects missing pinned binding inputs. Authorization is never a bypass of input validation."
  - "The synthetic native fixture preserves the exact real source bytes and whichever authorization value the architect set; historical/game flags remain false. Focused boundary and actual native preservation cases pass, followed by the official validate gate and different-model review."
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6.1-terra
- review-log: approved by gpt-6.1-terra — verified at f77346ff086e, validate exit 0 and tests 3/3 claimed, no recorded run cited; acceptance 3/3: (1) Temporary root recreates canonical relative path and verifies refusal; implementation log records passing test. (2) Separate temporary true plan reaches and rejects missing pinned source binding; implementation log records passing test. (3) Source hashes and authorization before/after compared; historical and game flags false; implementer native roundtrip preservation passed and official validate … — Independent review of delivery 228ee9e on landing f77346ff. Implementer gpt-6 focused boundary two tests and native preservation one test passed; official publication validate passed. No authorization of the real plan, history, or gameplay.

## acceptance

- Keep the existing S2 approval intact and record the correction separately. Never require the architect's development authorization to stay false forever, never promote that authorization to historical or engine approval, and keep i00015/S3 waiting for independent acceptance of this fix.
