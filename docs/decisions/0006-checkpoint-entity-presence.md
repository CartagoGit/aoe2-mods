# ADR 0006: Add checkpoint-scoped entity presence

## Status

Accepted for the reference profile and reducer by i00006/S1. Native support remains unimplemented.

## Context

ADR 0005 defines `current-entity-presence` as a live condition, including reevaluation of latched predecessor requirements before victory. That behavior is intentional and must remain stable for existing profiles. A distinct use case needs simultaneous presence only when an intermediate objective completes, followed by movement to a later receiver. Arrival history is not equivalent to observing simultaneous current presence.

## Decision

Add the strict, opt-in `checkpoint-entity-presence` kind with the same `entities`, `destinations`, and `requiredCount` contract. A fresh monotonic spatial batch is required to latch it. It shares identity validation, generation readiness, destination matching, and cardinality with current presence. `record-predicate` cannot satisfy either kind. A checkpoint objective cannot directly govern a transition to victory.

The checkpoint latch is retained as an intermediate objective fact and is not reevaluated during terminal ancestor presence checks. Those checks continue to include only `current-entity-presence`. Profile schema version 2, snapshot schema version 2, existing IDs, and legacy serialized shapes remain unchanged. The compiler carries the new discriminant through the reference IR; the native exporter continues to reject this unimplemented capability.

## Consequences

Authors can represent an observed, simultaneous checkpoint without making it a permanent victory condition. A separate final current-presence objective remains live at victory. Reference tests do not establish native runtime behavior, historical accuracy, fun, or balance; those need independent gates.

## Rejected alternatives

- Reinterpreting arrivals as simultaneous presence: arrivals are historical and do not certify a checkpoint.
- Weakening ADR 0005 or excluding legacy current presence from terminal ancestor reevaluation: this would silently alter approved behavior and existing profiles.
- Claiming native support from a reducer test: no native observer has been implemented or certified.
