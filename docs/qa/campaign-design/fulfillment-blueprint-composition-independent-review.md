# Independent review — fulfillment blueprint composition envelope

Reviewer: `gpt-6-luna` · 2026-10-25 · d00002/S11, scoped to the new “Closed blueprint envelope and composition” section in the S2 packet.

Compared root commits `fc0a51e` and `4ae8934` (including the ten-field correction) against the i00008/S1 decision, the current v3 schema, dossier factory/validator and the authored Constantinople screens. This is a document-level review of the composition contract, not an S11/S2 approval, a profile or history approval, or an assertion that a composer has been implemented.

## Findings

1. **Screen-role target IDs are not required to be pairwise distinct.** `screenRoles` requires the eight named roles to reference supplied screens, and screen records themselves have unique IDs/keys. The packet does not say the eight role values must be unique. Consequently, different roles such as `factualOutro` and `continuation` could bind the same screen while passing the stated envelope, despite the screen role table representing distinct authored beats. The four opening positions constrain the first four roles, but do not resolve aliases among `factualOutro`, `personalOutro`, `defeat`, and `continuation`. Add an explicit distinct-target check (or document any deliberately shared role pair) before the envelope is called closed.

2. **The map-field allowlist is referenced but not enumerated or located.** `mapPlan` lists its core fields, then permits “other existing documentary map fields” through an explicitly declared allowlist. No allowlist or authoritative location for it is identified in this section or the referenced ADR. That leaves the accepted nested map shape ambiguous: an implementer cannot know which existing fields must survive projection, and an auditor cannot distinguish an allowed field from an unknown one. Name the allowlist or make the listed map fields the complete accepted set, with any extra fields handled through a separately versioned decision.

3. **Preserving authored closing IDs needs an explicit v3 validation route.** The packet correctly says not to rename screen IDs to legacy constants and binds roles by supplied IDs. The existing `tools/design/episode_dossier.validator.py::audit_dossier` nevertheless directly indexes `fact-outro` and `persona-outro`; the current Constantinople source uses `victory-fact` and `victory-personal`, so feeding those authored screens through that audit raises a missing-key error. The legacy branch can remain unchanged, but the composition instructions should explicitly require role-aware v3 audit dispatch (or equivalent common-check extraction) instead of applying those legacy ID assumptions to v3. The opening roles do match the existing first-four sequence in the current screen source.

4. **The derived-view list does not explicitly name `secondaryBudget`.** The ADR says that `secondaryBudget`, like `worldContract`, `objectivePlan`, `stateMachine`, and `secondaryObjectives`, is an exact derived copy of its profile field. The packet says “objective/world/state/secondary views” remain exact copies, which could mean only `secondaryObjectives`, and elsewhere only says the accounts are supplied separately. Spell out all five view names so a composer cannot omit `secondaryBudget` or treat it as independently authored metadata.

## Checks that aligned

- The request envelope names exactly the ten ADR `ProjectionRequest` fields, keeps `designProfile` as a single discriminator, places one complete profile at `referenceCapabilityProfile`, and excludes documentary metadata from the strict profile. The corrected count in `4ae8934` is ten.
- Geography checks compare selection geography, regional bounds, projected hub IDs/centres, and each binding’s point ID/tile against the authored `mapPlan` record. The authored point remains evidence and cannot override the zone-derived point; corridor checks retain their existing qualifications.
- The intermediate-only guard requires actual previous and next selections and the existing narrator; entry/finale and other unsupported envelope families are rejected as composer limitations, without changing the v3 contract or legacy continuity.
- The packet explicitly preserves the 63 legacy outputs and validation path, rejects malformed opt-in inputs instead of falling back, and requires fingerprint comparison before and after implementation. The commits reviewed here change documentation only.

## Limits

Read-only inspection; no tests or heavy validation run. This review does not approve the S11 slice, the implementation, source claims, native behavior, or the historical consumer.
