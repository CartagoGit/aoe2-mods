# Independent decision review — i00008/S1

Reviewer: gpt-6-luna  
Reviewed candidate: architect commits `b6c8b8d41c5925d991d1bda10c4b5e0f8334b8e5` and `73d9eb3ccd56ab23b8050cea7403a5e18257fbab`, integrated into this review checkout.
Scope: the S1 projection decision and acceptance matrix, checked against the existing v3 schema, semantic validator, reducer, factory/rendering/accounting helpers, and current world-plan point representation. This is a document/design review, not a formal proposal verdict or an implementation test.

## Finding status

The original point/hub identity ambiguity is **addressed in the reviewed candidate**. `pointZoneBindings` now carries separate `pointId`, `zoneId`, `hubId`, and `offsetTiles`; point and zone IDs are independently unique; hub and offset must match the authoritative zone; and a recipe resolves its point ID through that table. The new `same-hub-distinct-points`, `point-alias-collision`, and `point-offset-drift` cases cover the previously missing alias and binding checks. This permits distinct recipe points in one hub without conflating a presentation point with the hub ID.


The reviewed `b6c8b8d` candidate initially left one geometric binding question: whether hub centre plus zone offset had to equal the authored map-point tile. The architect addressed it in `73d9eb3ccd56ab23b8050cea7403a5e18257fbab`: each binding now carries the existing point `tile`; computed hub-plus-offset must match it on both axes within absolute tolerance `0.000001`, used only for floating-point arithmetic; the wrapper must take that tile from the authored point record; snapping and relocation are prohibited. The new `authored-point-relocation` and `point-floating-tolerance` cases specify this behavior. I confirm this closes the remaining geometry ambiguity without making the authored point a runtime coordinate override. The matrix now has 34 unique cases, all still explicitly `specified-not-executed`.

## Cross-checks

- The design keeps one strict `CapabilityProfileV3` as authority and makes dossier shared views exact copies; the existing v3 profile schema contains the world, objective, state, secondary-objective, and budget fields required by that rule. The shared validator is called alongside the alternative-fulfillment validator.
- The described selected-plan terminal conjunction is consistent with the existing reducer’s committed selection, completed selected receipts, and fresh living arrival checks. The document does not invent a `fulfillment-complete` predicate or present reservation/payment as completion.
- The account split preserves spendable, protected recovery, and optional reserve; requiring optional reserve to match declared reserved rewards is consistent with the existing secondary budget model. The explicit ban on lowering alternatives into simultaneous fixed-payment predicates is scoped as a mapper limitation, not a v3 schema restriction.
- Existing helper boundaries are stated accurately: the Python helper can call a JSON bridge, the factory remains the dispatcher, rendering can show plan-specific rows, and the allocation helper remains the source for optional-payment reachability. The spec leaves selector/native/UI behavior and historical authoring out of this slice.
- The proposal now has filled `why`/`non-goals` text and records provenance for auto-created snapshot `077a5b7`; it does not attribute that snapshot’s inherited Git author to a human.
- The acceptance matrix contains 34 unique cases after the coordinate-binding clarification. All 34 are marked `specified-not-executed`; none are test evidence. The document correctly reserves implementation, legacy artifact comparison, and validation for S2.

## Boundary

This review has not run `bun run validate` or any implementation suite, and makes no claim that the mapper, bridge, dossier, native runtime, historical interpretation, or gameplay has been implemented or verified. I did not record a formal approve/reject proposal action. The design binding questions identified in this review are addressed by the current candidate; implementation and execution evidence remain for S2.
