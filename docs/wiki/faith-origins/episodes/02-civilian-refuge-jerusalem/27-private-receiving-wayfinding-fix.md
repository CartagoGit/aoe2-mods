# Private receiving-zone wayfinding correction

Architect gpt-6 · 7 November2026 · x00003. This is a closed implementation instruction, not implemented support or a game result. The earlier private kit `37f4db30982fff05efb2290fbdacb073dd6ad0a1655ed8296aff686fdd674748` is preserved. Its native/XS/container checks remain real; their scope did not establish initial receiver visibility.

## Evidence and ownership

`build_geographic_household_preview.script.py::build_variant` constructs17source bodies, compiles the household controller and writes the scenario. No initial zone annotation is added. `NativeMissionController` names original entities and provides predicates/captions, not an initial marker renderer. `native_secondary.adapter.py` creates FLAG_B/revealers only after the optional guide succeeds. The original Cesarea `build_delivery_episode.script.py::paint_world` already adds FLAG_A, a localized name trigger and MAP_REVEALER at every receiving centre. Extract that operation instead of copying it or painting a different map.

S1 has exactly five code/test files declared by x00003. Root owns this design, the real plan/source decisions and S2 rebuild/guide/receipt. Another model reviews each delivered slice. Do not change canonical campaign data, source bindings/plan, string IDs, controller semantics, extraction/quantisation, datasets/dependencies or approval flags.

## Shared operation

Create `tools/python/private_wayfinding.renderer.py` with a narrow explicit operation receiving the actual scenario, authored receiving-zone data and locale. Its only world writes are one FLAG_A and one MAP_REVEALER per zone plus one localized change-object-name trigger for that flag. Use existing pinned OtherInfo IDs and the parser API already used by Cesarea. Preserve the old player's value1, order flag→label trigger→revealer, label prefix `cdf-label-`, exact source label and continuous centre coordinates. Return actual created object/trigger references and semantic zone ID/locale/centre/label as provenance; do not reclassify auxiliary markers as canonical original bodies.

Validate the entire input before adding anything: unique nonempty zone IDs, finite in-frame centres, valid receiving radii, nonempty locale labels and no duplicate label-trigger names. Reuse an existing appropriate primitive where possible, not a new world solver. On unsupported/missing data reject, without partially decorating the scenario. Do not silently substitute English for missing Spanish or use stale cached input.

In the Cesarea caller, keep coast checks in the caller and retain its terrain painting and easy corridor reveal behaviour. Delegate only the marker operation, preserving actual valid-output ordering and native semantics. Capture its prechange semantic/XS baseline before editing. Its current canonical binding already pins the current source; do not repin it or rewrite the old delivered kit to make a check pass.

In the geographic caller, decorate **after** `compile_household_controller` and before `write_and_verify_artifact`. This keeps original native handles, XS and controller triggers unchanged and appends only annotation labels. The binding's17original entities and10zones remain exact. New initial native counts are17originals plus20auxiliary annotations; actual references must be recorded rather than guessed from numeric order. Add explicit receipt provenance; the same function serves labelled synthetic geographic and modern geographic builds. Do not add decorations to the old64nongeographic household builder.

The renderer never writes terrain types/heights, paints roads/circles, smooths a slope, moves the store, relocates a source entity or changes a receiving radius. Adding a UI flag is not approval of that location as an ancient address. Marker collision and real visibility remain engine questions even after native serialization succeeds.

## Concrete verification

- Verify ten FLAG_A and ten MAP_REVEALER at the ten exact receiving centres; inspect both EN and es-ES name effects against authored labels and targets. Compare actual native originals, their ownership/positions and every terrain cell before/after rendering.
- Verify the geographic controller's XS and152existing triggers/variables against the captured current build; append only ten label triggers. If the prechange source has changed, capture actual counts rather than weakening this preservation invariant.
- Exercise duplicate IDs/trigger names, invalid/missing labels, nonfinite/bool/out-of-frame positions and invalid radii, checking rejection before mutation. Keep tests meaningful and bounded; do not write a mock that merely mirrors the helper.
- Use existing native discovery for the new test file and keep its positive serialization/XS cases actually running. Run focused cases, then coordinate one heavy `test:export` and the official publish validation gate with root. Never call a skipped or synthetic case a real geographic or game check.
- Preserve failed attempts and logs outside the unit before publication. The private builder's complete signature service must still compare before/reopened terrain, units and triggers.

After accepted S1, root rebuilds six real variants into a new r2 directory. Independently compare the actual R2originals, controller/terrain, marker names/objects,12containers, original Caesarea scenario bytes and all source pins. The original0d589ef2and37f4db30kits stay untouched. Update the guide to say that the flag identifies the centre of the logical radius3receiving area; modern preview terrain does not have painted road circles. A private development handback remains distinct from game, balance, history and public-release acceptance.
