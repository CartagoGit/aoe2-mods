# Constantinople 380 — architect check of the materialized profile

Reviewer: gpt-6 · 25 October 2026. This report checks Luna's bounded profile materialization (`c3eb8b1`, corrected bindings `7c5bb72`, presentation bindings `7d0433c`) against the architect's world plan and authoring decision. It is independent of that materialization, but is not an independent approval of the architect's own design. The separate [decision/UI review](imperial34-profile-decision-independent-review.md) covers the root-authored decision and six-screen supplement. Neither report approves d00002/S3 as a whole.

## Checked artifacts

| Source | SHA-256 |
|---|---|
| [Reference capability profile](../../design/episode-plans/imperial-church/34-reference-capability-profile.json) | `8b8b47ea6c9060a19968b00bfc7b661852dea93f8d3e917aeb309e6e169235f7` |
| [Bindings and retained metadata](../../design/episode-plans/imperial-church/34-reference-profile-bindings.json) | `a9921fc3d323d4242ab46fce53feaf6b9096545d3dcc6741da3dc64122b87c6d` |
| [Six-screen UI supplement](../../design/episode-plans/imperial-church/34-profile-ui-supplement.json) | `5e35b496c3140045c580c1ba48db71af6015b50bb6651c0c2cb0347fd372528b` |

The actual profile passed `capabilityProfileV3Schema.parse` and `validateScenarioCapability` with zero diagnostics: two services, six exclusive recipes, eleven main entity identities, ten main zones and seven secondary contracts. The existing v3 contracts and reducer were not edited. Initial output identities do not constitute generated availability or delivery receipts.

## Source and geometry comparison

The six consulted decision/source hashes and the presentation-source hash match the current bytes. All nineteen geographic place records are retained exactly in `hubGeography`; their hub centres equal the authored tiles. Each of the ten zone bindings has a unique point ID and zone ID, copies the authored tile, names the actual zone's hub and offset, and agrees with hub centre plus offset on both axes. The full circles lie inside the existing map frame and retain the authored radii. No snap or relocation was used to pass a check.

The five original actors retain IDs, roles, initial hubs and offsets. All six recipe identities, workers, costs, original outputs, recipients and work/reception bindings match the world plan. The seven secondary contracts match their source after only the explicitly authorized strict-schema additions (`identity`, `replacement`, `originRule`, zone `placement` and `protectedCivilian`) and relocation of presentation-only fields to the companion. Each original `slotId`, route point list, centreline length and interpretation remains present there. No side objective was made mandatory or removed to satisfy validation.

The reserved rewards and maximum optional costs are numerically unchanged. The strict budget's `reallocatedCacheAllowance` equals the same reserve and is descriptive; it creates no additional credit. The source policy text remains in the world plan. The companion copies all five plan-screen bindings, both service bindings and six recipe bindings exactly from the UI supplement. The forty-five source screens plus six additional records produce fifty-one unique IDs with a complete explicit order; no duplicate text inventory or numeric string ID was introduced.

## Static financial check

I compared the actual service/recipe costs and three operating accounts against the existing analysis plan, normalizing only missing resource components to zero. I extracted the actual atomic-payment and finite-withdrawal vectors from each materialized side contract and compared their kinds/vectors to the original analysis inputs. The old analysis labels differ from runtime side IDs; the check preserved `side-1` through `side-7` and passed those actual IDs and vectors directly to the existing `optional_states` helper. It did not rename source identities to fit `resolved_inputs`.

| Difficulty | Affordable complete selections with every optional skipped | Those selections with a financially reachable prefix completing all seven optionals after funding |
|---|---:|---:|
| Easy | 9 of 9 | 9 |
| Standard | 7 of 9 | 7 |
| Hard | 3 of 9 | 3 |

The optional reserve totals 400 food, 150 wood, 25 gold and 0 stone. Protected recovery is zero. The helper pays each optional cost before its once-only reward; neither future income nor a second allowance funds a selection. The local diagnostic report was written to `/tmp/imperial34-materialized-profile-accounting-check.json`; the existing committed inputs, profile and helper determine the result. This was an inspection command, not a new production accounting engine or an automated test added to the suite.

These are financial witnesses conditional on accessible stocks, actors and successful spatial predicates. They establish neither route duration, native footprints, workload balance nor a playthrough. In particular, the nine/seven/three counts do not mean that every choice has been played or that Hard is calibrated.

## Result and remaining gates

No blocking discrepancy remains in the checked materialization. The initial companion field mismatch was corrected before this report. Modern DSM samples remain modern surface evidence; fictional activity sites are not excavated addresses. The historical event claims, source disputes and narrator boundaries still need the full dossier and historical/editorial review.

The reusable dossier mapper is not implemented at this checkpoint; i00008/S2 remains its separate task. This auxiliary profile and UI supplement do not create dossier 64 or change 63 drafts, 215 selections without a full dossier, 2,594 counted screens or 391 counted secondaries. Native composition, choice UI, terrain/navigation, exports and AoE2 evidence remain pending. No game test or historical approval is asserted.
