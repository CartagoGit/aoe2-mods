# Shared native serialization signature: closed extraction

Architect: gpt-6, 27 October 2026. The two private controllers already share runtime, spatial, transaction and optional logic. Their tests should also share the native signature directly, without loading the Caesarea-specific builder solely to compare serialization. This is a mechanical extraction, not new support for another map or composed profile.

## Exact ownership

Enter your own official `i00003/S3`, kind `implement`, generation6, topic `shared-native-signature`, after recovering live DelendAI overview/bootstrap and current ownership. Declare the actual MiniMax identity; Git author and committer are Cartago <cartago.relaxingcup@gmail.com>. Claim only these four Files:

- `tools/python/native_signature.helper.py`
- `tools/python/build_delivery_episode.script.py`
- `tests/fixtures/native-history/test_native_delivery_controller.py`
- `tests/fixtures/native-history/test_native_household_controller.py`

If the runtime reports a different current generation/owner, stop and report it rather than superseding a live worker. The previous household generation5 was integrated and retired; do not restore it or perform another publication from that old unit. Do not modify controllers, dossier sources, geography, validators, dependency configuration or tests outside these four Files.

## Extraction boundary and unchanged behavior

Move the complete existing `native_signature(scenario)` function from `build_delivery_episode.script.py` to the new helper. Its only non-builtin dependency is `struct`; move that import if the builder no longer needs it. Load the explicit helper relative to the builder's own file with the established runpy pattern, and bind the named function for existing internal calls. Do not add directory searches, sys.path modifications, package barrels, another writer or an alternate weaker comparison.

The signature's exact coverage and return structure stay unchanged: declared terrain, native object reference/type/owner and IEEE float32 positions, variables, the existing player/economy/diplomacy fields, options, text/message IDs, embedded XS, and the existing trigger/UI/condition/effect fields. It is not a signature of every possible AoE2 field. Preserve field order, None handling, tuple/list distinctions and the float32 conversion. Do not broaden or weaken coverage in this extraction.

Both existing test modules load the new explicit helper for signature comparisons. The delivery tests retain the builder for actual first-episode construction and source loading. The household tests remove their builder load if signature was their sole use. Keep all tests and fixtures otherwise semantically unchanged; add no mirror tests or new dependencies.

Compare the moved function's AST against the integrated original, allowing only an explanatory docstring change if necessary. Run the two existing focused Python test files with the pinned project interpreter. Preserve the immutable first opening's expected signature and XS; the existing regression already covers it, so do not rebuild all six historical variants. Tests establish serialization and static XS only, never game execution.

## Verification and official delivery

No blanket TMPDIR override for the full project gate: an existing map test deliberately writes a temporary generated report outside the repository. Keep explicit logs in your own ignored `.cache`, while standard commands use their normal system temporary directory. Do not alter a test or its timeout to hide an environment or capacity failure.

After focused checks, commit only your four Files with human authorship, report hash/diff/outcomes, then wait for architect review and the serialized `bun run validate` / `bun run test:export` window. No publication is authorized by this packet alone. Never approve the broad S3 yourself.

For later authorized publication, the installed CLI requires `work publish --proposal=i00003 --slice=S3 --kind=implement --generation=6 --topic=shared-native-signature --agent=<actual-identity>` with canonical `--workspace=/home/cartago/_projects/games/aoe2-mods`. `work publish --ref=...` is not the installed publication interface. Save stdout/stderr and the actual exit code on the FIRST invocation; do not run again merely to capture a log. Read `landed` and `certification.passed`, then verify product ancestry on canonical develop. A landed product must never be republished. A rejection stays recorded and the work stays preserved. An upstream move requires review of the current state before any further action; never infer rejection from a filename or mask failure with `tail | echo $?`.

Root retains logs outside the unit before retirement. Only after that instruction, retire your exact own ref through the official operation; never operate another model's unit or modify/push develop manually.
