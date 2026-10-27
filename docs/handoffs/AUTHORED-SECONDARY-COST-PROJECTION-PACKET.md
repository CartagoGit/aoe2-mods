# Authored optional cost projection: closed reference-only packet

Architect gpt-6,27 October2026. Addresses `yavneh-authored-optional-cost-projection`, discovered while designing three alternative services. Current `tools/design/secondary.py` fixes repair50wood/trade50gold and has no arrival-qualified hospitality cost. The reviewed Yavneh financial candidate needs repair30wood, trade20gold and guest20food, with70F/60W/30G finite rewards. Do not change that content to fit hard-coded presets.

## Exact assignment and boundary

Assigned to gpt-6-luna under its own official i00003/S3 implement unit, **generation6 alongside** the disjoint MiniMax signature extraction; recover overview/current generation before entering. Topic `authored-secondary-cost-projection`. Only three Files:

- `tools/design/secondary.py`
- `tools/design/episode_dossier.factory.py` (only opt-in field forwarding, see below)
- `tools/design/test_optional_cost_projection.py` (new focused responsibility)

No native adapter, contract schema, source dossier, global ID/range, catalogue output, counter, dependency or infrastructure configuration changes. This is a reference authoring projection only. `native_secondary.adapter.py` must continue rejecting the new extract payment shape until its separately designed native task is implemented. Do not claim Yavneh authoring ready, a complete dossier or game support.

## Architect decisions to implement exactly

The real dossier factory currently constructs secondary authored items through an allowlist. Forward `resourceCost` only when present, exactly as it already forwards `resourceReward`; no other factory refactor or source-default change. Verify the complete real factory path carries the new costs into its existing optional budget totals.

Add one optional authored-item field `resourceCost`, parallel to existing `resourceReward`. It is allowed only for `repair`, `trade` and `extract`. Normalize/validate with existing `resource_amounts`; unknown resources, booleans, floats, negative/nonfinite/null/string values fail under that shared validator. Require at least one positive component for an explicit cost; an explicit empty/all-zero override is an error. The default path when the field is absent preserves existing preset values and entire generated output exactly.

Every explicit cost requires a nonempty bilingual `instruction` via the existing instruction validation. The author supplies its actual physical requirement and displayed cost; do not generate a contradictory default instruction or silently accept a missing language. The helper still appends its existing independently authored reward/benefit text. Do not invent new historical text in this task.

For repair, retain the same health requirement, original target and once payment receipt. Replace only the preset payment vector. Its restoration description on the opt-in branch states an atomic authored-cost restoration to full health with no additional engine repair charge; it must not continue claiming50wood. The legacy restoration string remains byte-identical when the override is absent.

For trade, retain arrival of its own original trader followed by one atomic payment and then the separately reserved reward. For an extract cost, retain the **two existing original voluntary guests**, their original arrival/destination mapping and all existing no-substitute/life/once requirements; append one `atomic-payment` requirement after that arrival, using the exact cost and normal scoped payment receipt. `afterArrival` is true for trade and extract, false for repair. Payment is not completion and the reward cannot finance its own cost. No additional cost is charged by the engine in this reference projection.

No changes to counters, actor count, source input mutation, optional failure isolation, protected recovery, reward reserve or main-goal dependence. Reuse the existing budget summation and optional validator so the new costs appear in totals once. Avoid duplicate numeric validation, a second reducer or hard-coded Yavneh IDs/amounts in production code.

## Meaningful focused verification

Exercise the real builder and validator with small authored items, not a copied implementation formula. Cover repair30W/trade20G/guest20F, exact requirement order/receipt identity/afterArrival, repair health receipt and restoration text, finite reward vector unchanged, resulting maxOptionalCosts30W20G20F, source-input immutability and rejection boundaries. Include invalid override kinds and missing/empty bilingual instructions, as well as shared numeric rejection and zero vector. Existing no-override calls must preserve legacy generated outputs; compare against the integrated baseline or existing full fixtures rather than regenerate/commit historical files.

Run the new focused module and the existing design test suite with correct import setup. Report real exit codes/logs in own ignored cache, exact diff and Cartago author/committer commit, then STOP before heavy gates/publication. Root reviews and allocates a serial gate window. No self-approval of the broad S3. Never use shared-checkout checkpoint for local worktree edits; use normal Git in your own unit with your actual declared identity. Never read/edit the runtime database.
