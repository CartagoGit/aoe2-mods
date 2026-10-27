# Private household controller: bounded independent review

27 October 2026. Implementer: **minimax-m3.1-flash-preview**. Reviewers: **gpt-6** and **gpt-6.1**, independently of the implementer. Git author and committer: Cartago <cartago.relaxingcup@gmail.com>.

## Exact delivered product

Product `111d4967fb1d0291990a295d661544b8b06718a3` was officially integrated into develop at `5bdd1fa33f60b50f4567edc8aab6076c09483cf2`. Its two Files are `tools/python/native_household.adapter.py` and `tests/fixtures/native-history/test_native_household_controller.py`. Final SHA-256 values are respectively `42a78e9d97fbe7486f069dbd9883553b4cf16d69c2fc83f2060618c7b01e94c3` and `8bf37490831705b2bb09d4c3ff18608265cb6952770eb295f56feda768d2e531`.

This implements the [closed private controller packet](../../handoffs/MINIMAX-HOUSEHOLD-NATIVE-CONTROLLER-PACKET.md), using shared runtime, spatial, transaction and secondary compilers. It does not supply the historical map or a second playable historical mission. The synthetic 64 × 64 fixture verifies a restricted native binding; composed public v2/v3 export remains unsupported. No source dossier, campaign identity, string range or dependency was changed.

## Corrections and final semantics

Eight distinct original households feed a cumulative court-arrival ledger. O1 requires six historical arrivals plus six currently living originals globally; it does not add an unwritten current-life filter to the historical arrival ledger. Any living original household currently in the court during phase2 can authorize the single 240-food payment. Refuge visits can precede payment and persist as historical facts. Final success intersects court, refuge and held flags for the same originals with a fresh current-life census, requiring six. The third original death defeats before a successful terminal decision.

Review closed these concrete issues:

- Activation guards now run before any mutation in the final action. A fresh census gives loss precedence and writes final objective plus terminal success atomically within that invocation; no latched undecided-success window remains.
- Canonical JSON comparisons reject numeric substitutes for booleans or integer counts. Required original actors have explicit owners and allowed native types; the repair object is the original player2 house. Labels are nonempty in EN and es-ES, and narration preserves the authored neutral-before-persona sequence.
- Binding validation uses actual floor-plus-half native starts. Optional actors are checked against every optional arrival circle through a nonmutating snapped view passed to the existing shared secondary validator. This rejects free initial completion after coordinate snapping without duplicating the six secondary rules.
- Route information requires unique route IDs, finite in-map pairs, at least two points, a nonzero segment and a positive finite width if supplied. Empty or degenerate route data cannot award a guide benefit.
- Unknown composed/profile/fulfillment fields are rejected by presence, including null values. Source input stays immutable. UID0 remains valid, with distinct integer handles and boolean rejection.
- Test-only mirror decision functions were removed. The retained focused cases exercise the production parser, compiler, serialization and negative boundaries.

The final GPT-6.1 conformity concerns exactly the clean product above and found no remaining P1/P2 in this bounded controller scope. It is not formal approval of the entire i00003/S3 slice, geographical approval or an engine-play verdict. Generic secondary transactions retain terminal guards; actual same-tick engine scheduling remains a game QA obligation.

## Verification and its limits

- The final focused household suite passed **26 tests**. A previous full native-fixture run passed55 before the last six focused additions; no later full61-case run is claimed.
- `bun run validate` passed **158 tests / 2,138 assertions**. The successful official frozen-install/validate certification judged the merged candidate and landed the product above.
- `bun run test:export` passed **3 variants / 2 round-trips**, with unsupported-mode rejection. These are the existing technical export fixtures, not historical gameplay.
- The architect compiled and exercised the unchanged C-compatible generated final-action fragment with mocked native variables and original-life queries: **65,536** alive/qualified mask combinations, **128** independent fact/life truth-table cases and **23** invalid activation cases, all passing after corrections. Before correction, all23 invalid activations mutated state. This is a C++ harness, not AoE2 or an XS runtime.

The checked embedded XS hash was `178682d62f34fba4d9882334fe9802824835930b571159b2082da2c50865668f`; its final-action fragment hash was `6d592e3ef98319bca6aee67999400ead1a8001f84db1bd177c4cc73a46d605d4`. These identify this synthetic verification, not a historical scenario distributed to the player.

Private evidence is retained outside the retired unit at `/home/cartago/.codex/artifacts/aoe2-mods/household-native-review-20261027/`: source diff/hashes, focused results, generated-fragment checks and initial failures, final validate/export logs, raw publication events and `minimax-evidence/publish-success.json`. Initial validation attempts include an incorrect repository-local TMPDIR imposed by the architect and a later portfolio-test timeout; the environment was corrected without weakening tests. The successful publication was then mistakenly retried and rejected as stale after landing. All attempts remain preserved; ancestry and the successful JSON certify the actual integration. The worker's exact generation5 unit was subsequently retired officially.

## Historical and production gates still open

The [physical binding review](jerusalem-household-design-review.md) and its23 prospective cases remain design evidence. Draft19 deliberately has no approved corridors or native elevation and is not approved for a historical build. Modern DSM samples do not reconstruct ancient bare earth. Terrain, routes, building footprints, command discovery, engine ordering, save/load, UI, difficulty calibration and real gameplay remain unverified. Catalogue counts remain64 draft dossiers/214 missing, with one private opening prototype and zero fully game-verified historical episodes.
