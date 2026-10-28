---
id: t00001
title: "Measured time budget for the heavy alternative-fulfillment reference tests"
kind: test
status: ready
type: proposal
track: campaign-factory
date: 2026-10-27
---

# t00001 — Measured time budget for the heavy alternative-fulfillment reference tests

## goal

Give the two heavy reference tests an explicit, measured and proportionate time budget so the shared validation gate is not red for every agent when several workers run in parallel, without weakening any assertion or hiding a performance regression.

## why

The shared validation gate went red for every agent in this workspace on 27 October 2026: the alternative-fulfillment reference suite timed out twice, the 95-row portfolio test at 39.030s against its explicit 30_000ms budget and the lifecycle-checkpoint test at 5.400ms against Bun's implicit 5_000ms default. The cause is measured, not hypothetical: the architect's own archived validation logs record the same 95-row test at 23.234s, 25.516s and 28.258s, so the 30s budget was already 92% consumed while the machine was idle, and the workspace now runs several workers concurrently (load average 19.03 on 10 cores). The lifecycle-checkpoint test carries no explicit budget at all, so it inherits Bun's 5s default and flakes as soon as the suite runs beside another agent. The DelendAI test-convention plugin already uses testTimeout 30_000, so the reference suite is expected to run heavy tests with an explicit budget. The runtime reports this failure as shared-branch breakage that blocks every agent's publication, so it must be repaired rather than retried.

## non-goals

- No change to any assertion, expectation, fixture, reducer, schema, public contract, string identity, ID or campaign source.
- No change to the number of portfolio rows, the matrix coverage, the difficulty set or the causal checks the test performs.
- No global test-timeout relaxation: only the two measured tests receive an explicit budget, and the budget is derived from recorded uncontended baselines rather than chosen to make a red run green.
- No claim that the workspace can host unbounded parallel heavy gates; serialization of heavy gates remains the architect's decision.
- No engine, gameplay, balance, historical or localisation approval.

## slices

- global_gate: e2e

### S1 — Measured time budget for the two heavy reference tests
- **Status**: pending
- **Files**: `tests/alternative-fulfillment/reference/alternative-fulfillment.test.ts`, `docs/qa/alternative-fulfillment/reference-budget.md`
- **Gate**: e2e
- acceptance:
  - "Record the measured uncontended baseline of the 95-row portfolio test from the architect's own archived validation logs (23.234s, 25.516s and 28.258s) and the observed contended measurement (39.030s at load 19 on 10 cores), and state that the current explicit 30s budget is already 92% consumed before any contention."
  - "Give the 95-row portfolio test an explicit budget that keeps a proportional margin over the worst recorded uncontended baseline and tolerates the documented parallel workflow, and give the lifecycle-checkpoint test the same explicit budget its sibling already uses instead of Bun's 5s implicit default, without touching any assertion, expectation, row count, matrix coverage or fixture."
  - "Re-run the affected test file and the full gate, record the exact commands and outcomes, and state the remaining limits: this does not make the workspace safe for unbounded parallel heavy gates, does not certify a performance improvement, and does not authorize skipping or relaxing any check."

## acceptance

- Record the measured uncontended baseline of the 95-row portfolio test from the architect's own archived validation logs (23.234s, 25.516s and 28.258s) and the observed contended measurement (39.030s at load 19 on 10 cores), and state that the current explicit 30s budget is already 92% consumed before any contention.
- Give the 95-row portfolio test an explicit budget that keeps a proportional margin over the worst recorded uncontended baseline and tolerates the documented parallel workflow, and give the lifecycle-checkpoint test the same explicit budget its sibling already uses instead of Bun's 5s implicit default, without touching any assertion, expectation, row count, matrix coverage or fixture.
- Re-run the affected test file and the full gate, record the exact commands and outcomes, and state the remaining limits: this does not make the workspace safe for unbounded parallel heavy gates, does not certify a performance improvement, and does not authorize skipping or relaxing any check.
