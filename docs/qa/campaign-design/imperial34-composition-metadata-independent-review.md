# Independent review — Constantinople composition metadata

Reviewer: `gpt-6-luna` · 2026-10-25 · d00002/S3, limited to the root-authored composition metadata file. Review target: root commit `3274ef7`, `docs/design/episode-plans/imperial-church/34-dossier-composition-metadata.json` (SHA-256 `54143ba65720bb493b5cb7615cf16fab02ddfb52d33bddbe3007db100f6d1828`). The envelope checked was the closed blueprint decision in `FULFILLMENT-DOSSIER-S2-PACKET.md` at `ba1f8be`. This report does not approve the full S3 slice, a composed blueprint/dossier 64, historical interpretation, native integration, or gameplay.

## Result

No blocking envelope or source-concordance defect was found in this metadata artifact. The JSON has exactly the fourteen `dossierMetadata` keys allowed by the envelope, and `mapPlan` contains only the required fields and declared optional fields. `terrainInstructions` is a string with all seven authored paragraphs. Root commit `3274ef7` corrects the earlier candidate's array/string mismatch; it changes only this metadata file. No blueprint, campaign selection, or dossier-count file is changed by the metadata commits inspected.

The required bilingual documentary text fields `factualIntro`, `factualOutro`, and `dramatizationNotice` are present; `factualIntro` and `factualOutro` match the EN/es-ES text of their assigned `fact-intro` and `victory-fact` screens exactly. The eight role IDs are distinct and resolve to supplied screens: `title`, `fact-intro`, `handover`, `personal-intro`, `victory-fact`, `victory-personal`, `main-defeat`, and `continue-next`. The opening role order is preserved. The factual screens and handover use `collection-narrator`; both personal screens use the existing campaign narrator `imperial-clerk`. The handover identifies Marcus as the fictional clerk. The source-date qualification remains explicit: separate November events in Socrates and a December account in Marcellinus, without harmonizing the disagreement.

## Source and geometry checks

The metadata’s three `mapPlan.sourceBindings` hashes match the current world plan, UI supplement, and profile-bindings file. The companion bindings’ source plan, UI, decision, architecture, study, and allocation-plan hashes also match their current files. The candidate profile inspected for concordance has SHA-256 `8b8b47ea6c9060a19968b00bfc7b661852dea93f8d3e917aeb309e6e169235f7`; its eleven main-world entity IDs exactly match the eleven keys in `historicalMaterialPolicyByEntity`. Those documentary policies remain outside the strict v3 profile.

All nineteen point IDs and authored geographic fields match `worldPlan.map.places`. Reapplying the existing `tools/design/geography.py::tile_point` frame helper reproduces all nineteen tile coordinates. The nineteen metadata hubs retain the source IDs, centres, lon/lat, names, radii, and fictional-site classifications, and their ID/centre pairs match the projection request’s hubs. All ten point-zone bindings resolve to metadata points and retain the same authored tiles. The candidate bbox lies inside the `constantinople` regional bbox in `docs/design/geography.json`.

All twenty-one corridor IDs match the source map. Each retains its source point sequence as `hubOrder`; all are declared `land` corridors of width six, and all endpoints resolve. The `corridorStraightLengthsTiles` values agree with the sums across their mapped hub centres to the stored three-decimal precision. Terrain, shore, and footprint text continues to identify candidate geometry only: it preserves the north/south-bank qualification and current OSM/Natural Earth distinction, says modern DSM samples are not ancient ground, and leaves land masks, buildings, slopes, and native navigation pending.

Every asset ID in `mapPlan.geographicLayers` and `artDirection.referenceAssets` resolves in `docs/research/odyssey-research/reference-manifest.json`. The metadata retains `productionApproved: false`; the referenced modern coast/DSM and mixed-period city assets remain subject to the manifest’s stated licenses and limitations. The map asset path is a declared output location, not evidence that a generated map or playable terrain exists.

## Policies, portfolios, and continuity

The three playstyles preserve the source portfolio IDs and side IDs in order: `provision-first` → `side-1, side-7`; `informed-movement` → `side-5, side-4, side-6`; `household-source-care` → `side-2, side-3`. Every referenced side ID exists in the v3 profile, and each record keeps both invariance flags true. Their opportunity statements describe movement/attention and avoid claiming historical outcome changes or new gameplay operations.

One nonblocking editorial delta: `provision-first.costOfOpportunity` describes the two aid deliveries and repair, but does not repeat the source portfolio reason’s specific “hard shared-hearth+rented remaining20W” comparison. The separate authored QA case states that exact 20-wood constraint and the repair’s 50-wood cost. The metadata therefore retains the relevant tradeoff without contradicting the source; root may choose whether to make the opportunity sentence more specific.

The continuation object has exactly the required three fields, points to the actual next selection `29-council-and-final-perspective-constantinople`, and sets `campaignComplete` false. The current episode is order 33 and the successor is order 34; the stable `continue-next` screen uses “episode 34.” A previous selected episode also exists, and the campaign narrator is available, so the intermediate-episode envelope condition is met.

`failureRecovery` distinguishes free preview, unaffordable confirmation, pre-commit cancellation of only the escrow, locked methods after commitment, main defeat on the specified original-identity losses, post-work worker loss, and optional-only failure. It preserves the separation between spendable, optional reserve, and protected recovery. Capability statuses say native integration and QA remain pending; the authored QA list contains cases but no passed or game-verified result. No prose adds resurrection, grace, external-payment, timer, or campaign-progress operations.

## Verification and limits

Verification was read-only: parsed the JSON, compared field sets and source hashes, checked manifest IDs, compared all point/hub/corridor identities, and recomputed point and corridor geometry with the existing helper/formula. No project test suite was run. No source file was edited by the reviewer. The reviewer identity is `gpt-6-luna`; Git commit authorship uses the configured user identity as directed by the user.

This is a review of root-authored composition metadata only. It does not validate a future composed blueprint, run the typed mapper, change the 63/215 dossier counts, approve historical/geographic claims, or establish native capability or AoE2 playability. Those gates remain open.
