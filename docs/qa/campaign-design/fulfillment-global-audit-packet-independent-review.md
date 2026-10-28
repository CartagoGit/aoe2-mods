# Independent review: fulfillment global-audit packet

Reviewer: gpt-6-luna. Date: 2026-10-25. Scope: root decision packet `ad8400f`, amended by `3421ee9`, checked against accepted S2 implementation `6f06737`, its independent acceptance `e08a5cbd`, the accepted projection contract, and the prior static consumer inventory at `/tmp/i00008-v3-global-consumer-inventory.md`.

## Result

The packet's technical boundary is coherent after `3421ee9` clarified the two inputs that matter: `referenceCapabilityProfile` is authoritative for the shared v3 runtime contracts, while `accountsByDifficulty` is a separate authored `ProjectionRequest` input. This matches the accepted mapper and composer. The initial wording could have been read as making the profile the source of spendable and protected-recovery accounts; the amendment closes that ambiguity and correctly leaves `optionalReserve == secondaryBudget.reservedRewards` to the accepted typed projection rather than adding another financial validator to the civic report.

## Cross-checks

- The known failure is correctly scoped to the global Civic audit. Its legacy branch requires `difficulty[level].accessibleWithoutOptionalRewards` and `enemyTotalCap`; the accepted v3 projection instead exposes the exact `difficulty` view of `selectionAnalysisByDifficulty`, plus accounts and the profile's explicit roster. A `designProfile` dispatch is therefore necessary. `verify.py` reaches this audit, so its caught `KeyError` fails `docs:check` as described. This agrees with the previous global-consumer inventory.
- The required v3 financial view maps to actual fields: each selection-analysis difficulty contains `spendable`, `protectedRecovery`, `optionalReserve`, `selections`, and `affordableSelections`; the dossier's `difficulty` is copied exactly from that analysis. Accounts are separately supplied in the request. Their vectors are strict nonnegative safe-integer maps, and the accepted projection checks the optional reserve against `secondaryBudget.reservedRewards`.
- The roster instruction points to `referenceCapabilityProfile.enemyRoster`, whose accepted contract carries `initialEntityIds`, `mobilizations`, and `productionEnabled: false`. Reporting this one authored roster without manufacturing difficulty caps or a release schedule preserves the source contract. The existing role-name heuristic remains only a static signal.
- Reusing `predicate_kinds` and `deadline_fields`, keeping the legacy risk conjunction, describing spendable-only cross-difficulty comparison, and labeling financial alternatives as non-game evidence do not introduce payment lowering, an economic oracle, a native behavior claim, or a playability approval.
- The packet preserves the current legacy-only report byte-for-byte, defers report regeneration until a later historical insertion, and specifies an opt-in V3 row with no fabricated legacy cap, worker or gathering fields. Its focused-test list covers dispatch, malformed views, roster/deadline signals and unchanged legacy rows. The readiness auditor remains a plan-targeted legacy diagnostic and is expressly out of scope for V3 timing.
- The packet's reproduction statement is consistent with the field mismatch. I did not execute the preview, episode 64, tests or gates; this report is a static decision review.

No additional blocking inconsistency remains in the reviewed packet after `3421ee9`. This is a bounded review of the packet, not a formal approval of i00008/S3 or of the S3 implementation.
