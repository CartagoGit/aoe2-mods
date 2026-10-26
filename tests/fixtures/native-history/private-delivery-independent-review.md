# Independent technical review: private Caesarea delivery prototype

Reviewer: `gpt-6.1`; 26 October 2026. Own DelendAI review unit: i00003/S3, generation 3, session `caesarea-private-independent-review`.

Product commit: `c55c3bd0104158f5e2cf40ccbec7782e327338e7`, officially integrated in `e443aaaa5281291acfa855c68a68d0da35cb1c02`. The preserved implementation in parent `9145fed581904500d7e9dc53d5fb0bea02d965f5` is included in this reviewed tip. The final delta was independently inspected: exact six optional IDs and the private container name/title derived from the authored editorial contract. The reviewer merged that integration into the isolated review unit before publishing this report.

## Scope and result

This is a limited technical review of `tools/python/native_delivery.adapter.py` and `tools/python/build_delivery_episode.script.py`, their use of the shared native factory/spatial/transaction helpers, the opening episode's authored source, physical binding and focused native inspection tests. No new blocking issue was identified in the corrected private subset by the checks below.

This report does not approve all of i00003/S3, d00002/S2, the other historical dossiers, general composed v2/v3 export, historical release or game behavior. It is not a formal whole-slice approval. `gameVerified` remains false.

## Corrections independently checked

The first review found three P2 issues. The corrected code resolves them:

- The EN/es tutorial now explains one arrival per original bearer, continued life until issuance and no simultaneous-presence requirement. Payment still requires the original copyist in the copying circle.
- The contract validator rejects `o2.predicate.operator = "any"`, repair `health = "half"` and trade `afterArrival = false`. The reviewer independently executed these three mutations against the corrected validator; all raised `ValueError`, while the unchanged source was accepted.
- Native round-trip signatures now include player stocks, disabled building/unit/technology lists, diplomacy, victory/team options, localized panels, objective display fields and embedded XS, in addition to terrain, bodies, variables, conditions and effects. Coordinate normalization explicitly models native IEEE float32 serialization.

The earlier design review also checked the corrected 97/85/72 gold profiles, bilingual body/zone labels, store relocation, identity-loss phases and institutional source qualifications. The current binding's source digest matches the canonical source bytes. That agreement establishes which source is consumed, not historical approval.

## Implementation inspection

Collection and copying arrivals use original handles and circular spatial predicates. The three copying-arrival facts accumulate independently. Main validity checks keep all inputs alive until paid issuance; afterward their deaths cannot erase provenance. The original copyist/courier remains essential until the first terminal latch. A pre-issuance archive visit cannot satisfy the final delivery. Required loss is ordered before final delivery and optional rewards in the generated trigger list.

Payment helpers check every required balance before mutation and record one receipt. Reward helpers check named optional reserves before debiting reserves and crediting spendable stock; completion prevents repeated grants. Assigned household IDs and destinations remain explicit. Optional identity loss only fails its own unfinished task. Terminal guards prevent later grants. Caption release timers clear the shared busy flag even after a terminal decision, allowing outcome captions to proceed.

The guide's auxiliary route markers are emitted within the same successful guarded grant invocation. No additional original participant or enemy is created. Work-rate zero is emitted through native XS with pinned dataset IDs for all `VILLAGER_` variants, avoiding the parser's zero-float effect serialization problem. This does not establish that manual economic commands are blocked in the game.

The private builder constructs a new explicit physical base through the shared factory. It does not strip capability metadata from public IR. Public composed v2/v3 rejection remains separate. Literal EN/es panels and captions use private variants without reallocating global string IDs. The single-episode campaign container is extracted and compared with the scenario digest; it is not the completed historical campaign. Existing output directories are rejected and candidate output is assembled separately before final placement.

## Evidence and limitations

Reviewer-executed evidence: source/code inspection, source/binding digest comparison and the three focused validator mutations above. Before report publication, no Bun suite, native export build, game session or paid generation was run by this reviewer. The author's eight focused delivery tests were read; the author reports 35 combined native tests passing in 31.866 seconds, Ruff 0.14.4 checks passing, local validation with 158 tests / 2,138 assertions and export verification with three variants / two round-trips / unsupported export rejection. Those executions are author evidence, not independent executions claimed here. Product integration `e443aaaa` passed its declared frozen-install and validation gate; this report's official publication runs its own declared gate. Neither gate establishes game behavior.

Actual AoE2 observations remain necessary for original-handle APIs, selection, circular arrival, work-rate effects across task variants, atomic execution and same-tick defeat priority, caption scheduling, save/load persistence, geographic navigation and marker behavior. The map uses modern shoreline controls and flattened elevation, not an ancient harbor reconstruction. Difficulty, duration and reward utility remain uncalibrated. Auxiliary dossier SVG/straight-hub-chain metrics must not be presented as the new relief route's native geometry or measured duration.

The four optional receiving-court relocations for side-2/3/4/6 remain explicit physical-binding refinements; canonical generated zone offsets have not yet incorporated them. This prototype reads their reviewed binding coordinates and preserves zone IDs. It must not be described as proof that canonical source geometry is fully materialized or historically approved.

## Reviewed file digests

| File | SHA-256 |
|---|---|
| `tools/python/native_delivery.adapter.py` | `c85e7f1438ce42948fe4fb257e1ddf4197e1a039332c65b52bed1fc505d3c8c8` |
| `tools/python/build_delivery_episode.script.py` | `c076a8e0a25381ae91daa7a1fb9de4571534e1a97441729247b4bb5f053acf59` |
| `tests/fixtures/native-history/test_native_delivery_controller.py` | `fac137e0824947125d4765804d05707c92eebfded0794d6241b29c1bca4fcde7` |
| `16-native-binding.json` | `b3f6eb2d6151981cfa5bd8c4ad57065e8f67ba129fc0c2a88554fdc7ae34ce2e` |
| `docs/design/odysseys/faith-origins.json` | `f86bcecfc918beb8e0e94c9832d188ad619fb9693b5b8540b109afa046c417c2` |
