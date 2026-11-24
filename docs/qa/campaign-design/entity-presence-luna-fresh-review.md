# i00005/S1 fresh independent review — gpt-6-luna

Formal verdict: **approved**. DelendAI accepted the approval from a fresh reviewer and marked S1 done. The reviewer is distinct from implementer `gpt-6-sol` and prior reviewer `gpt-6.1-sol`.

## DelendAI review and publication

- Fresh review unit: `wip/gpt-6-luna/review/batch-all-g1/i00005-presence-review`, entered under the real identity `gpt-6-luna` from develop.
- Formal `proposal_review approve` returned `ok=true`, reviewer `gpt-6-luna`, status `done`, quorum 1, and “approved; the slice is done and its lock is released.” Evidence used resubmission `909d7bb28cebfdb5158c97e71f8001b09171db4d` and exact coverage for both S1 acceptance criteria.
- The approval metadata commit automatically renamed unrelated blocked proposal f00003. At the owner's instruction I restored only its prior path and kept the body byte-identical (SHA-256 `854c6eb315ffc09e67d3afc09f6e8b1397fd09cdce1c4a447825ad06dd01594d`). No code or other proposal content was changed.
- Official `work publish` landed the review unit on develop at `d793ae4652e64df87afd5015ed24fbfaa31ad707`; certification passed against `909d7bb28cebfdb5158c97e71f8001b09171db4d` with `bun install --frozen-lockfile` and `bun run validate`. DelendAI removed the completed review worktree and refs.

## Source inspected

Inspected the full focused diff for fix commit `b7f2fc97660f1420695f28018467cd941a43d0d7` in the fresh review unit. It changes the shared generation predicate, live-presence evaluation, tick handling, S1 tests, and ADR 0005. S2 native observation and S3 campaign promotion remain outside this slice.

### P1: generated identity counted before production

`packages/gameplay-state/capability-generation.helper.ts` checks derived-token output facts and exact `generatedByReceipts` ancestry/arrival. Normal entity-state/arrival paths and current-presence qualification use the helper. `livePresenceSatisfied` applies it per identity, and the same predicate is used during victory recheck. Tests distinguish a present-but-unproduced token from the produced token after its source input is collected and `derive-token` runs, including JSON save/load. The receipt-generated test rejects a wrong destination and accepts the exact source arrival.

Finding: the P1 condition reported against integrated `8c55de5` is addressed in the changed code and focused tests; I found no conflicting pathway in the inspected evaluator/reducer.

### P1: invalid/stale batch bypassed deadline defeat

On a failed batch, reducer still rejects non-tick actions. For `tick`, it leaves `freshLiveBatch=false` and continues into ordinary clock/deadline/defeat evaluation. Invalid observations do not overwrite the last accepted spatial map; presence-dependent victory still requires a fresh valid batch. The regression covers duplicate/stale batches, pre-deadline clock advance, deadline defeat, death, latched and loaded states, and a profile without live-presence requirements.

Finding: deadline/explicit/irrecoverable defeat remains independently evaluated; invalid/stale input cannot certify victory. No new blocking defect found in these paths.

## Executed checks

- `bun test tests/unit/entity-presence.test.ts`: PASS, 13 tests / 88 assertions.
- `bun run validate`: PASS, TypeScript/Biome, 102 tests / 389 assertions, docs links, campaign validation.
- First `bun run test:export` failed because the worktree lacked `AoE2ScenarioParser`.
- Ran official pinned `python3 tools/python/setup.py`: installed AoE2ScenarioParser 0.9.6 and compiled pinned `rge_campaign` source commit `3c40203b650de9888ca82fae1276ea67bf3d3d93` locally.
- Reran `bun run test:export`: PASS, 3 variants, 2 round-trips, unsupported mode rejected, `gameVerified: false`.

No repository implementation source edits were made by this reviewer. S2/S3, native observation, AoE2 game verification, and historical approval were not reviewed or approved here.
