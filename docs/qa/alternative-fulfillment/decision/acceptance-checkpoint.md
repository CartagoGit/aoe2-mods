# i00007/S1 acceptance checkpoint

18 October 2026 · implementer gpt-6 · unit `wip/gpt-6/implement/i00007-S1-g1/alternative-fulfillment-decision` · base `216c033eacf91d003e20340c7d532eea80521e4e`. Architecture proposed; independent review and official integration pending at this checkpoint.

| Slice acceptance | Concrete evidence | Limit |
|---|---|---|
| Inspect current operations and choose explicit compatible capability | [Decision](../../../architecture/alternative-fulfillment.md), reuse/rejection table and [source hashes](source-inspection.json). Explicit v3 opt-in selected; existing v2/source envelope unchanged | No v3 schema/action/runtime/native implementation in S1 |
| Specify identity, joint reservation, once-only spending, cancellation and terminal recovery | Decision lifecycle, conservation, failure, load and native-input sections; [33 specification cases](decision-cases.json), especially C01–C16 and C18–C21/C28–C33 | Cases are prose/numerical expectations, not executed reference transitions or a gameplay DSL |
| Exact selected outputs, prerequisites, reception, survivors and portfolio QA | Artificial fixture declares five original inputs/recipients, six mutually eligible output IDs and recipe-specific zones; selected-output and original-recipient fresh final presence, irreversible-loss policy and all-skip/all-complete/three-portfolio acceptance | Not a campaign world or ancient map. Its small worksite dependency is not evidence of interesting RTS play |

The implementer ran `bun run validate`: 108 tests / 426 expectations; documentation and campaign validation passed. The existing finite-allocation audit still reports nine combinations and 9/7/3 all-skip affordability, with native/game flags false. A read-only one-off check verified all recorded inspection hashes against actual base bytes, all 33 case IDs are unique, and the six fully specified initial reservation/cancellation/commitment resource examples obey conservation. These arithmetic checks execute no new reference or native transition.

The current schema, snapshot-v2 file and string-ID lock were byte-compared with the base and are unchanged. No package, compiler, adapter, Python exporter, campaign or generated design file changes. No `test:export` claim: export code is unaffected, and unimplemented composition remains rejected.

The independent reviewer must challenge semantic gaps (including replay/cancellation, causal work proof and native UI feasibility), not just approve arithmetic. i00007/S2 may proceed only after this decision is independently accepted and officially integrated. S3 additionally retains i00003 native/template/input and s00001 prerequisites. Historical production and MiniMax remain blocked by their actual dossiers, geography and engine gates.
