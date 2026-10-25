# Independent review — fulfillment blueprint composition envelope

Reviewer: `gpt-6-luna` · 2026-10-25 · d00002/S11, scoped to the new “Closed blueprint envelope and composition” section in the S2 packet.

Compared root commits `fc0a51e`, `4ae8934` and the correction `ba1f8be` against the i00008/S1 decision, the current v3 schema, dossier factory/validator and the authored Constantinople screens. This is a document-level review of the composition contract, not an S11/S2 approval, a profile or history approval, or an assertion that a composer has been implemented.

## Initial findings

1. **Screen-role target IDs were not required to be pairwise distinct.** `screenRoles` required the eight named roles to reference supplied screens, and screen records themselves had unique IDs/keys, but the packet did not say the eight role values must be unique. Different roles could therefore alias one screen.

2. **The map-field allowlist was referenced but not enumerated or located.** `mapPlan` listed core fields, then permitted “other existing documentary map fields” through an unspecified allowlist, leaving the accepted nested map shape ambiguous.

3. **Preserving authored closing IDs lacked an explicit v3 validation route.** The packet correctly prohibited renaming screen IDs to legacy constants and bound roles by supplied IDs. The existing `tools/design/episode_dossier.validator.py::audit_dossier` directly indexes `fact-outro` and `persona-outro`; the current Constantinople source uses `victory-fact` and `victory-personal`, so legacy checks would raise a missing-key error on those authored IDs.

4. **The derived-view list did not explicitly name `secondaryBudget`.** The ADR requires it, like `worldContract`, `objectivePlan`, `stateMachine`, and `secondaryObjectives`, to be an exact derived copy of its profile field. “Secondary views” could mean only `secondaryObjectives`.

## Follow-up on `ba1f8be`

All four points are resolved in the packet update. The eight `screenRoles` targets must now be distinct; the eleven required and seven optional `mapPlan` fields are enumerated and other fields rejected; audit dispatch checks `designProfile` before legacy-only checks and the v3 closing narrator check resolves role IDs; and the packet names all five exact profile-derived views, including `secondaryBudget`. I found no remaining discrepancy in this scoped section.

## Checks that aligned

- The request envelope names exactly the ten ADR `ProjectionRequest` fields, keeps `designProfile` as a single discriminator, places one complete profile at `referenceCapabilityProfile`, and excludes documentary metadata from the strict profile. The corrected count in `4ae8934` is ten.
- Geography checks compare selection geography, regional bounds, projected hub IDs/centres, and each binding’s point ID/tile against the authored `mapPlan` record. The authored point remains evidence and cannot override the zone-derived point; corridor checks retain their existing qualifications.
- The intermediate-only guard requires actual previous and next selections and the existing narrator; entry/finale and other unsupported envelope families are rejected as composer limitations, without changing the v3 contract or legacy continuity.
- The packet explicitly preserves the 63 legacy outputs and validation path, rejects malformed opt-in inputs instead of falling back, and requires fingerprint comparison before and after implementation. The commits reviewed here change documentation only.

## Limits

Read-only inspection; no tests or heavy validation run. This review does not approve the S11 slice, the implementation, source claims, native behavior, or the historical consumer.
