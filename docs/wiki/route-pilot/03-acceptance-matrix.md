# Route laboratory acceptance and adversarial matrix

f00001/S1, architect gpt-6,2026-10-24. **Every engine case below is pending.** This is a reproducible plan, not a test-results report. The [specification](02-implementation-specification.md) fixes the oracle; [inventory](15-text-inventory.json) fixes copy. Link real results to `tests/compatibility/progression.json` and `localization.json` without changing their pending status merely because this plan exists.

## Execution record

For each run record case ID, actual model/tester, exact game build/platform, difficulty, language, ordered installed mods/priorities, source commit, exported ZIP path/SHA256, original save hash, prior A/B values, numbered actions, observed terminal/write/recap, attachment paths, result(passed/failed/blocked) and deviations. Unknown profile reads must be logged as unknown. Never fabricate a profile value by interpreting a screenshot alone. Use a disposable test profile; preserve the player's real profile and record how the sandbox was isolated. Do not claim arbitrary profile mutation is a supported production operation.

The tester prepares independent baseline saves/artifacts for clean profile, A-only, B-only and both through actual completions. Test forced simultaneous destruction, essential loss and pre-prepare destruction only with a clearly marked separate diagnostic artifact/harness and its own hash. This plan does not assert a debug harness exists. If unavailable, mark the case blocked; do not call two visibly close deaths the same engine tick. Diagnostic artifacts cannot substitute for release ZIP verification.

## Source/export checks before engine runs

| ID | Steps | Required result |
|---|---|---|
| SRC01 | Compare both source bundles with identities, maps, units, routes and closed43-key inventory. | Exact campaign/scenario/progress identities; both campaign status=fixture; no new narrative decisions or unrelated schema/config changes. |
| SRC02 | Run both `bun run staging:check route-pilot` and `bun run staging:check route-successor` in S2 without `--partial`. | Both succeed; all declared sources,17actual draft catalogues, narrators, references and present asset bytes are complete. No campaign activation or lock mutation. |
| SRC03 | Independently inspect victory arrays, objective dependencies and terminal effects. | Global prepare only; alternative A/B routes ordered A,B; defeat-first; no clearing a progress key, unconditional double outro or both-targets-required error. |
| SRC04 | Compare all36 S2-materialize keys in EN/es-ES, required labels and speaking cast with15-text-inventory.json. Verify the7 native-pending intentions are documentary only, absent from all runtime catalogues/lines. Review other translations with real attribution. | Exactly the36 representable keys, no missing/blank/copied-placeholder translation or extra unreferenced entry; draft status remains honest; no unlisted speaker or historical claim. Do not fabricate inert event lines to bind the7 pending keys. |
| SRC05 | In S3 promote both bundles jointly, allocate IDs, inspect prior-ID immutability, update glossary and run validate/test:export plus both campaign:build exports. | All actual commands pass on the promoted commit. A fixture container is labelled fixture; previous export success is not evidence for the new bundle. |
| SRC06 | Inspect real native templates, conditional branches, progress-read operators and bound media/string IDs against their accredited origin/build. | No fabricated SequenceItems operator or template. Missing layout/read/error handling blocks native completion while preserving source work. |
| SRC07 | Compare manifests and packaged bytes for every referenced asset. | Exact hash/license/path and allowed use; no missing file or paid generation assumed. Audio/translation approval remains separate. |

## Engine progression and failure cases

A/B values below are profile progress, independent of scenario-local cdf-terminal. An arrow describes expected state, not a result already observed.

| ID | Initial state and steps | Expected observation |
|---|---|---|
| ENG01 / fresh-profile | New isolated profile; install/start T02 without T01 installed. | No lock or forced prequel. One missing recap explains both endings; player may start; T02 completes after10active scenario seconds. No predecessor data written. |
| ENG02 / route-a | Empty A/B; T01 keep guard safe, wait prepare, destroy only A. Reopen T02. | Exactly one victory; profile(1,0); T02 A-only recap and optional B recommendation. |
| ENG03 / route-b | Separate empty baseline; destroy only B; open T02. | Exactly one victory; profile(0,1); B-only recap. |
| ENG04 / route-a-then-b | Starting from ENG02, replay T01 and complete B; open T02. | Profile(1,1), not(0,1); one both recap; first completion retained. |
| ENG05 / route-b-then-a | Starting from ENG03, replay T01 and complete A; open T02. | Profile(1,1), not(1,0); same both recap independent of order. |
| ENG06 / repeated-route | A-only baseline; complete A twice across replay; repeat symmetrically for B. | Flags remain booleans/one; no duplicate reward, counter or duplicate outro. Other route remains available. |
| ENG07 / both-same-tick | Empty baseline; diagnostic artifact destroys A/B in one verified engine evaluation after prepare. Repeat with B's effect listed first in the diagnostic harness. | Declared A priority both times; only A key written in each fresh run. No accidental both record from one run. Requires actual tick evidence. |
| ENG08 / defeat-and-route | Empty baseline; diagnostic same-evaluation guard loss and A destruction; repeat with B and both targets. | Defeat first, neither key written, no victory/route outro. |
| ENG09 / timeout-and-route | Empty baseline; diagnostic target completion at900second timeout, compare899/900/901 boundary with actual engine resolution documented. | Before boundary may win; at/beyond defeat boundary defeats. Never two terminals. Record timing granularity rather than assert sub-tick precision. |
| ENG10 / destroyed-before-prepare | Diagnostic destruction of A before1second prepare; keep guard alive. Repeat for B and both. | Recorded destruction remains eligible after prepare; A/B/both priority as defined. No permanently stuck objective or early victory before prepare. |
| ENG11 / lost-guard | Empty baseline; lose guard before any target. | One defeat; keys unchanged; restart/reload offered. |
| ENG12 / lost-rams | Lose one ram while guard survives, then finish with the other if possible. Separately lose both. | Ram loss alone does not invoke defeat. If both are gone, no invented replacements; timeout/reload handles exhausted fixture. Report any unwanted automatic defeat. |
| ENG13 / terminal-late-action | After route A terminal, a separately queued B destruction would occur; test symmetrically. | Closed terminal cannot write the other key or replay an ending in that run. Requires engine evidence if game immediately exits. |
| ENG14 / save-before-victory | Save with prepare done, targets alive and empty prior profile; complete A; restore pre-victory save and complete B. | First completion's profile A is retained; second yields both; loading a scenario snapshot does not clear external progress. If engine semantics differ, report infrastructure mismatch. |
| ENG15 / save-after-route | Save/reload immediately after terminal if engine allows it; otherwise record restriction and test supported transition/menu save behavior. | No duplicate terminal, erased external key or invented save capability. Unsupported timing is blocked, not passed. |
| ENG16 / save-before-prepare | Save/reload before prepare and after an early target destruction in diagnostic artifact. | Dependency/objective memory follows oracle once prepare becomes eligible; no timer reset falsely credited as destruction. |
| ENG17 / successor-only | Keep profile A-only or both, uninstall/disable T01, leave T02. | T02 remains accessible and reads actual available record or explicitly unknown. Missing mod is not an enforced prerequisite. |
| ENG18 / read-failure | Simulate genuine unavailable/error progress read through accredited native/test seam; do not silently clear profile. | Exactly unknown recap, neutral sufficient summary, no write/repair to either key; gameplay accessible. Without a real seam record blocked. |
| ENG19 / no-record-success | Successful read confirms both absent/zero, with T01 installed. | Missing recap rather than unknown; no double recap or contradictory recommendation. |
| ENG20 / no-engine-auto-win | Load T02 and record game clock/terminal; inspect lack of opponent. | No accidental stock-game auto-victory/defeat; only10second fixture objective ends it. Any mismatch blocks affected export behavior. |
| ENG21 / source-outro | Exercise A and B using only supported source narrative and then real native candidate separately. | Generic source outro never asserts wrong route; native candidate shows exactly its route-specific ending if that capability is certified. |
| ENG22 / layout-timing | Read full recap slowly, skip it, return to menu, then start T02. | Pre-scenario recap not cut off by the gameplay10second timer; skip changes no flags; control starts once. No unsupported relative clock assumed. |
| ENG23 / update | Complete A; replace both mods with a separately hashed compatible rebuild retaining identities; launch/replay B. | Existing A survives update, both obtained; no campaign namespace migration or progress reset. |
| ENG24 / footprint-path | Inspect castle and ram footprints and walk/ram approach to both targets from origin. Keep guard in west. | No overlap/out-of-bounds/blocked lane; both candidate routes reachable, guard outside unsolicited target fire initially. Record failures before relocating within technical design. |

| ENG25 / generated-castle-reaction | Inspect native cdf-react-<profile>-targets triggers and their task_object targets; load each difficulty, wait past1second, inspect both castle positions/behavior and guard safety. | Exporter-generated attack-order effects exist even though content has none. Record whether the engine ignores or applies building orders; no claimed stationary behavior without evidence. Any unsafe/unintended behavior returns to the architect as infrastructure mismatch. |

## Difficulty, localisation and coexistence cross-product

Run ENG02/03/07/08/20/24/25 for easy, standard and hard on separately recorded states; source oracle and route identities must agree across all three. This does not certify interesting challenge or historical balance. Record actual durations only after measured runs; no estimated duration becomes measured by passing validation.

Run ENG01–05 and ENG14 in English and es-ES. Switch EN→es-ES and es-ES→EN between T01 completion and T02 launch, before/after scenario save restore, and after both routes are obtained. Every flag must remain identical; titles/objectives/unit labels/recaps must use the selected locale, preserve accents and remain readable. Check all17 locales' engine-folder mapping separately because `folderVerified=false` is still recorded in configuration. Source-complete catalogues do not prove the folder mapping.

Coexistence runs follow localization.json for1,2,5and10mods, reversed priorities and update. T01+T02 counts as2mods; larger sets require actual additional test mods and hashes, not a claim based on two. Verify text-ID/namespace independence and both progress keys for each supported composition. A missing5/10mod fixture marks those cases blocked. T00's es-ES source and prior allocated IDs must remain unchanged.

## Expected evidence versus release

f00001/S1 acceptance: reviewed specification, both minimal maps/oracles/continuity, complete bilingual text/cast inventory and this executable matrix, integrated through DelendAI. It may be accepted while engine cases remain pending. S2 closes source/staging for the36 representable keys only, with static summary; it does not close the7 conditional presentation intentions. ENG01–06/17–19/21–22 require the accredited adaptive native candidate, and remain blocked for that behavior on a static source fixture. This expected limitation is recorded rather than passed. S2 closes source/staging only; S3 closes real promotion/export for the supported artifact; S4 documents actual capability evidence and unresolved dependencies. No slice can claim GAME VERIFIED, approved17languages, full dubbing, native conditional recaps or PRODUCTION READY from a green unit test suite. Mod publication remains outside this assignment.
