# Private pilot test kit

Architect: gpt-6. Cut: 26 October 2026. Proposal f00001/S4, partial delivery; independent review and actual game observations pending. The read-only independent inspection by gpt-6-luna compared both ZIP hashes/sizes and all18entries against the receipt, all17language destinations, source profile parameters and pending/blocked test dispositions without a blocking documentary finding. Formal slice review remains pending. This kit starts testing the existing technical base while historical design continues. It contains two fictional fixtures, not historical chapters or finished campaigns.

The [receipt](private-engine-test-manifest.json) identifies the exact source commit, ZIP hashes, contained files and real export commands. Both exports succeeded and their scenario/container round-trips passed. Each ZIP contains one campaign container and seventeen draft string catalogues. There are no native narrative/layout templates or audio files. The [results template](private-engine-test-results.template.json) is unexecuted; copy it for observations rather than changing its pending entries into inferred successes.

## What to try first

1. Record the AoE2: Definitive Edition build, platform, operating system, tester, actual UI language and difficulty. Use a separate test setup and record other enabled mods. Keep the original ZIPs and their hashes. No game profile has been installed or changed by the build.
2. Verify the ZIP hash. In PowerShell, use `Get-FileHash .\route-pilot-fixture.zip -Algorithm SHA256`; on Linux use `sha256sum route-pilot-fixture.zip`. Compare the complete value in the receipt. Repeat for route-successor.
3. With the game closed, locate the active profile's local mod directory through the game's mod-manager folder facility if available. On a Windows profile the candidate structure is `Games/Age of Empires 2 DE/<profile>/mods/local/`. Its exact location and UI controls must be confirmed on the target installation; this kit has not tested them. Extract each ZIP into its own newly named test folder, so `resources` is immediately inside that folder. Keep T01 and T02 separate. Enable the test mod and restart. Record failure to appear or launch as a test result; do not add invented JSON/layout files or change the game installation to conceal it.
4. Attempt to open the fixture in the custom-campaign UI. Record the exact menu, label and launch result. Missing campaign UI or inaccessible content is a useful failure: the fixture lacks accredited native layout templates. Stop that branch if it cannot load; retain logs/screenshots. An editor-based diagnostic, if subsequently prepared, will have its own hash and cannot certify this campaign ZIP's UI.
5. If T01 loads, keep its essential guard safe in the west. Move the two rams to the northern castle for route A, then repeat from a fresh scenario state against the southern castle for B. Observe footprints, approach routes, castle behavior, objectives and a single ending. The prepare prerequisite is one active second; the timeout is 900 seconds. There are no replacement rams. A lost guard must produce defeat. Record elapsed game time and any inability to complete either route.
6. Test a normal save/reload before victory. Separately enable only T02 and attempt its independent launch. T02 contains a static summary and a ten-active-second objective, with no opponent. Record an unexpected early automatic ending or inaccessible campaign. Repeat ordinary launch/objective observations in English and Spanish, then the available UI difficulty choices.

The supplied JSON keeps these observations separate. Start with loading and normal A/B routes; do not make the first test session depend on the larger compatibility matrix. New map/pathfinding issues return to the architect with artifact hash, reproduction and actual result. Fixes create a new artifact and invalidate evidence for the changed bytes.

The private kit also retains the two original separate exported scenarios under `diagnostics/<campaign-id>/`. Their hashes are listed in the receipt. If campaign UI is unavailable, the tester can attempt to open a copy through the scenario editor and use its test facility, keeping the matching locale mod enabled for strings. Record the real editor controls, selected language/difficulty, exact scenario hash and `launchMode=editor diagnostic`. Do not save or edit over the original. This is a separate way to investigate scenario load, movement and normal terminal behavior; it cannot pass campaign-menu load, cross-campaign persistence or missing narrative templates. Failure to load either form remains useful evidence. No custom editor harness or same-tick instrumentation is implied.

## Boundaries that affect the result

T01 exports distinct progress writes, but this kit provides no accredited reader of profile flags. Winning A then B does not by itself demonstrate cumulative stored state. T02 does not inspect predecessor flags or select a conditional recap. The A/B/both/unknown recap and persistence cases stay blocked until a real native candidate can observe them. Do not report a static summary as a successful adaptive recap.

No same-tick diagnostic harness is included. Two deaths that look close together cannot prove terminal arbitration. Test normal guard loss and normal victories now; leave same-evaluation priority blocked. All three authored balance profiles have equal zero resources and one-second reaction in this fixture. Repeating UI choices is compatibility testing, not a measurement of historical difficulty or proof of the unverified XS-to-UI mapping.

Seventeen exported catalogues remain draft; engine-folder mappings, string collisions, coexistence beyond these two mods, native slideshow/audio, Return of Rome and public release remain separate gates. No `gameVerified`, campaign QA or configuration flags are changed by completing this checklist. Full [acceptance cases](../../wiki/route-pilot/03-acceptance-matrix.md) and [compatibility proposal](../../delendai/proposals/blocked/s00001-acreditar-compatibilidad-nativa-y-pruebas-de-motor.md) remain authoritative.

The official [custom campaign guide](https://www.ageofempires.com/news/custom-campaigns-for-age-of-empires-ii-definitive-edition-2/) describes discovery through the game mod manager for published campaigns; it does not certify this private local installation or supply our missing templates. The local procedure above is a target-installation test, not an assertion of verified support. No portal upload or public distribution is part of this kit.

## Reproduce without the game

Use the pinned environment from the [development guide](../../guides/development.md): install dependencies and Python/toolchain once, then run the following from an isolated DelendAI unit. Existing external tool overrides may select that pinned environment; do not version machine-specific paths.

```sh
bun run validate
bun run test:export
bun run campaign:build route-pilot --export
bun run campaign:build route-successor --export
```

Exports write `dist/<id>-fixture.zip`, `build/<id>/build-report.json` and `build/<id>/native-checks/export-report.json`. Scenario diagnostic files stay outside the mod ZIP. Parser metadata may vary across runs: compare each new actual hash and retain its report instead of assuming binary identity. The receipt records this run's exports; the validation and export-suite results are added only after execution.

## Next parallel deliveries

The architect continues historical dossiers and reusable missing operations while a tester exercises this kit. Luna or MiniMax implements only a closed assigned slice; the independent reviewer checks its exact product. The next candidate must address a demonstrated missing capability or a reviewed design, rather than silently adding historical content to this lab. A first historical playable slice needs its approved dossier, real geography/terrain, native operations and a reviewable small test objective set before growing into the full episode. Existing 400-tile plans remain plans until materialized and tested.
