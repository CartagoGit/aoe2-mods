# Faith Origins: design checkpoint, episodes 26–30

Author: gpt-6 · 2026-10-13 · d00002/S1/S2/S11 · independent review pending.

All 30 selected episodes now have explicitly authored expanded drafts: 1,191 EN/es-ES screens and 180 optional objectives. This is design coverage, not 30 playable scenarios or historical approval. The other 243 selected episodes still require complete dossiers. MiniMax historical assignments remain blocked.

## Five distinct historical frames

- 26: Tertullian’s advocacy and reported voluntary contributions; three local fictional dispatches, then receipt-backed departure and return of the same couriers. No acquittal or imperial answer.
- 27: attributed first-person and editorial parts of the Passion of Perpetua and Felicity; four separate fictional neighbors and three care parcels. Historical executions remain fixed and visions do not create gameplay miracles.
- 28: P.Oxy. XII 1464, dated 27 June 250, records a household’s declaration. Gaion’s religion and independent verification of the declared acts remain unknown. Six independent fictional neighbors and two funded care allocations use separate north/south receivers. No sacrifice choice or certificate forgery.
- 29: distinguish Cyprian’s report from Pontius’ narration of his death. At least eight actual staged household identities and all four original property chests continue onward; unstaged substitutes cannot satisfy the ledger.
- 30: distinguish measures from 303, regional variation, the Milan agreement and the letter published at Nicomedia in 313. Two separately funded fictional inventory registers do not demonstrate historical restitution. Preserve semantic ID `04-a-different-dawn` at display order 30.

## Reusable design finale

`tools/design/odyssey_continuity.helper.py` composes canonical route keys, successor IDs and EN/es-ES titles. The final mandatory objective enters a pending route-selection state. Canceling writes nothing; only a valid selected route permits victory. Its design commit writes that key to 1 once per run, preserves all other keys and writes nothing on defeat. Side rewards close upon entering selection. The recommendation prioritizes the selected perspective and also exposes accumulated completions; it neither launches a campaign nor enforces a predecessor. The Christian successor returns to 312; the Jewish successor returns to 70, with explicit overlap messages.

This helper emits documentation only. Native menu input, campaign-variable persistence and save/load are required capabilities, not implemented by this Python composition. No numeric string IDs or schema contracts were changed.

## Geography and assets

Oxyrhynchus uses a new approximate regional profile anchored by CNR-ISPC, with the Bahr Yussuf to the east and the principal Nile outside the local crop. Four fictional care yards remain west of the schematic branch; the Oxford site account does not certify a c.250 bank line. The architect inspected the Egypt and Milan SVG previews; they are geographic controls, not DEMs, ancient building footprints or navigable maps. Carthage reuses a local inland frame and existing licensed modern reference images. No temple, prison, martyrdom address or actual emperor’s palace is invented.

Source consultations and the delegated Oxyrhynchus audit are local and preserve access failures. The architect separately read the specified BL catalogue, CNR gazetteer, Oxford site sections, Eusebius chapters and complete Latin DMP 48; no wholesale modern translation or unlicensed facsimile is distributed. Imperial Church’s first ten source checks are collected separately and still await architectural interpretation.

## Verification

- `python3 tools/design/render.py`: 30 drafts regenerated; 273 selections retained.
- `python3 tools/design/verify.py`: zero errors; zero approved expanded dossiers.
- `python3 tools/design/test_design.py`: 40 tests passed. New adverse cases reject an early/missing finale, wrong route namespace or successor, skipped choice, progress erasure, writes before victory/on defeat, automatic launch, predecessor gating and missing bilingual recommendation text.
- Official DelendAI validation: Bun type/format checks, 82 tests / 277 assertions, documentation and campaign gates; final result recorded in the unit journal.
- Adapter unchanged; no new binary-export or in-game evidence claimed.

Historical approval, dated geography/terrain, native observation of receipts/departures/arrivals, environmental risk in episode 15, final menu/persistence and easy/standard/hard playtesting remain open. Static affordability and explicit routes do not measure challenge or enjoyment.
