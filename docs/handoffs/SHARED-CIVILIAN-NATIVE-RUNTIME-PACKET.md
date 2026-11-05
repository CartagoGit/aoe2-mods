# Shared civilian native runtime: bounded extraction

Assigned to Luna on 27 October 2026. Root owns architecture and review. This task prepares code reuse for the second episode while source refinement and the first private playtest proceed. It does not implement a new historical scenario, add a generic framework, or complete i00003/S3.

## Exact Files and behavior

- Modify only `tools/python/native_delivery.adapter.py`.
- Add `tools/python/native_mission.controller.py`.
- Add `tools/python/native_secondary.adapter.py`.

Extract the common native runtime and the six existing optional circuits without changing output or behavior. Keep the original delivery validator and the Caesarea-specific main provenance/commissioning sequence in the delivery adapter. The builder, sources, contracts, public exporter, datasets, dependency locks and existing tests remain untouched.

`NativeMissionController` owns the existing common context: scenario/managers, original-handle binding, authored entities/zones/screens, spatial/transaction helpers, persistent-variable writer, generated XS function names, one caption slot and native objective UI. Move the actual existing methods `variable`, `set`, `equal`, `trigger`, `function`, `expression`, `in_zone`, `condition`, `call`, `captions`, `advance_after` and `objective_ui`. DeliveryController inherits the common class.

Preserve allocation order exactly: ready/phase/terminal/busy first; then the existing register-issued/copy-payment; then original handles and optional reserves. A concrete base constructor followed by explicit `initialize_originals_and_reserves()` after the two delivery roles is acceptable. Do not invoke an abstract/subclass callback before construction or reorder variables to simplify extraction. Preserve original initialization effects, semantic flag mapping, names, zero work-rate XS operation and ready-last compilation.

The six-circuit function becomes `compile_native_secondary(controller, side)` in the secondary adapter and uses the actual common runtime. Do not duplicate payment, spatial checks, repair HP capture, information captions, reserved payout or terminal closure. No new interpretation of an optional identity or arrival. Shared code must not hardcode the Caesarea narrator or main record semantics.

Use explicit relative runpy loading as in the current Python tools; no circular import, sys.path mutation, implicit barrel or module filesystem search. Preserve `cdf-delivery-initialize`, `cdf_delivery_*` and `cdf_delivery_action_*` for this caller, through explicit constructor parameters if necessary. A common finalizer may retain the existing ready-last, XS validation and report logic. Do not weaken the delivery validator or public composed rejection.

## Regression evidence and workflow

Read connected overview/bootstrap and live i00003/S3. Enter an own implementation unit, generation4/topic `shared-civilian-native-runtime`, with real Luna identity/session and `--alongside`; claim the three Files only. Human Git author and committer remain Cartago. No operation on another worker's unit or manual develop integration. Work already assigned by root can use official `work enter` directly; `auto_work` is not required to select it. A runtime refusal is preserved and returned, never bypassed.

Run the existing eight native delivery tests and a strict semantic signature comparison with the immutable es-ES/hard opening scenario at:

`/home/cartago/.codex/artifacts/aoe2-mods/caesarea-opening-20261027-c55c3bd/native/es-ES/hard/01-administrative-records-caesarea.aoe2scenario`.

Use the existing builder's `native_signature` on the old and newly built scenarios, without dropping fields or relaxing comparisons. Expected current product: 143 triggers, 87 persistent variables and unchanged generated XS. Binary byte identity is not required because parser metadata can vary; native semantics and exact XS must match. No new test mirroring extraction internals is requested.

Keep source/binding snapshots in the unit. A later full-campaign source hash update for episode02 must not be mistaken for a changed episode01 semantic signature. Do not rewrite the existing immutable kit or attribute its old binary hashes to a new build.

Return source commit, diff, evidence and logs. Ask root for the serialized heavy gate window: `bun run validate`, `bun run test:export`, independent review, then official publication. Never approve your own implementation or mark the broad S3 done. Root will review subsequent code to ensure household eligibility and atomic terminal checks are separate orchestration, rather than hidden changes inside these shared helpers.
