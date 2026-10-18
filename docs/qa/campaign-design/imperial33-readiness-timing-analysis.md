# Sirmium readiness: conditional timing analysis

18 October 2026 · architect gpt-6 · d00002/S1/S3. This supplements the 63-dossier source without changing the authored deadline or any gameplay contract. It does not certify difficulty, a viable native schedule, actual gathering, historical geometry or enjoyment.

## Finding

The proposed hard 720-second window is sensitive to proxy speed and native detours. In the explicitly assumed grid, the same all-skip parallel plan produces 697.743 seconds at 0.6 tiles/game-second on corridor centerlines, leaving only 22.257 seconds; a 20% route-length increase produces 822.291 seconds and misses the window by 102.291 seconds. At 0.8 tiles/game-second with that same 20% increase, the estimate is 635.468 seconds, leaving 84.532 seconds. These are consequences of authored hypotheses, not observations of units or a measured success rate. Do not approve 720 seconds from the existence of a timer predicate or a positive sample.

There are 18 samples per difficulty, 54 in total. Easy falls inside its assumed window in 18, standard in 15, hard in 9. These counts sample a deliberately chosen grid; they are not probabilities, game runs, independent strategies or coverage of every permitted mistake. The most demanding selected sample estimates 1071.388 seconds. Actual native costs can exceed every sample.

## Method and explicit assumptions

The [author's plan](../../research/odyssey-research/imperial33-readiness-timing-plan.json) selects one physically distinct staging assignment: crew 1–2 west, 3–4 central, 5–6 east, leaving 7–8 free; supply units 1/2/3 go west/central/east respectively. All nine moving identities retain their actual source offsets. The [audit](../../research/odyssey-research/imperial33-readiness-timing-audit.json) hashes the actual episode and hypothesis input. The longest shortest route on the authored bidirectional land graph, including offset connector lengths, is 373.64554 tiles. This is centerline arithmetic, not a traversable native path.

All moving actors are assumed independently commandable in parallel. An entirely separate hypothetical 12/9/6-gatherer pool works at fixed integer food/wood allocations. The model reads the exact 240 F 180 W first-phase debit and each profile's actual starting stock. On hard that leaves 189 F 146 W to gather; at 0.2 net resource/worker/game-second the selected fixed split is 3 food/3 wood, 315 seconds of harvesting plus 45 assumed setup, 360 seconds total. This pool has not been spawned or positioned; the main eight-person crew is not silently counted as gatherers. No optional reward, protected stock or phase 2 payment funds readiness.

Sample speeds 0.45/0.6/0.8 tiles/game-second, net rates 0.15/0.2/0.3 resource/worker/game-second, and route factors 1.0/1.2 are deliberately unmeasured hypotheses. The estimate adds 30 seconds for collection to the maximum actor movement time, 45 seconds for economic setup to the maximum harvest time, then takes the larger of those parallel branches and adds 45 seconds for payment/positioning/observation. Those allowances are not guarantees or native operation durations. Actual movement, packing, worker walking/drop-off, input order or observer delay may invalidate a positive sample. At the exact deadline the reference loses; the report uses a strict comparison before rounding displayed numbers.

## Consequences for the architect and native gate

- First materialize the exact separate gatherers and finite operating nodes, with drop sites, footprints, yields, availability and net rates. Record resource movement assumptions rather than assuming the profile's worker cap creates a working economy.
- Select actual legal unit proxies and measure normal game-speed movement, pickup/control transfer, collision, turns and terrain path length. Verify all three original supply units and all six crew fit their receivers; center clearance is not packing.
- Run the same all-skip plan and the authored repair/trade portfolios on every difficulty. Early optional benefits require their own routes, payment and collection; they are not free opening stock. Include two permitted crew losses and an honestly playable recovery, as well as ordinary newcomer command delay.
- If the measured hard all-skip plan has no reasonable recovery margin, the architect must revise the deadline, geography or operating setup and re-review it. MiniMax is not authorized to retune it. A faster proxy must not be chosen merely to force this spreadsheet to pass.
- Preserve actual game version, artifact hash, route, pauses and timings under the existing civic playability matrix. An easy victory is also insufficient if the result is mostly unproductive waiting. No approval follows automatically from falling below a time estimate.

## Reproduction and checks

```sh
python3 tools/design/readiness_timing_audit.script.py
python3 tools/design/test_readiness_timing_audit.py
```

The default command is read-only and rejects a stale report. After an intentional source/assumption revision, inspect the changes and run the script with `--write`, then check again. The evaluator never mutates a dossier, IDs, schema or native output. Its four tests cover authored detours and disconnection, fixed integer allocation, actual first-stage costs, missing/duplicate/wrong-destination actors, invalid assumptions, changed source fingerprints and movement sensitivity. They are tests of this conditional arithmetic, not additional AoE2 tests. The [independent technical review](imperial33-timing-independent-review.md) of candidate cd6e53a is conforming within its stated scope: four tests, 54hypotheses, extra shortest-path/stale-input checks and explicit exclusion of native/game approval. Root bun run validate passed 107 tests/424 expectations, docs links and campaign validation. The separate original Sirmium review remains scoped to its earlier hash; neither review approves the whole d00002 slice. Official merge certification remains separate.
