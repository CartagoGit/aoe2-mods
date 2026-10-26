# Caesarea: closed decisions for the first playable iteration

The owner has asked for the first historical campaign to become playable while the remaining architecture and dossiers advance. This is the opening of **Embers of the Covenant**, not another boat diagnostic. The accompanying [native binding](16-native-binding.json) fixes the physical interpretation and lists the remaining source refinements explicitly. It is a review candidate, not historical approval or a claim that a native mission already exists.

Update (2026-10-26): the architect unit completed a native prototype implementation and the first es-ES/standard binary round-trip; code review, full variants and actual gameplay remain pending.

## Historical boundaries and narrative

The surviving inscription is evidence for Pilate's **prefecture** and a dedication. Neither the lost wording nor the trial of Jesus can be recovered from it. The Israel Museum object record describes a reused stone in a theater stairway; its suggested original temple association is probable. Its English catalogue title and descriptive prose use “procurator”, whereas the translated surviving titulature reads prefect. The campaign's 27–36 CE selection is an editorial window, not a date inscribed on the stone. See the two institutional source records and qualifications in the binding.

The common narrator first gives a sober, attributed account. Miriam is the campaign's fictional later copyist, born centuries after the opening setting. Her first-person voice concerns her own later archival experience and inherited information. She does not witness Pilate, a first-century copying job, or the 1961 discovery. The three working records, all participants, exact courts and paths are fictional gameplay. They are not three surviving fragments, an ancient transcription of the complete inscription, or independent corroboration of a trial.

The mission closes with the limit of the evidence, Miriam's personal reflection, then the actual next selection, `02-civilian-refuge-jerusalem`. This does not complete the campaign. Literal private captions may be embedded separately for EN and es-ES while certified campaign UI remains pending; this must not allocate or replace global string IDs or claim native SequenceItems support.

## Geography and physical actions

Keep the real Caesarea regional frame, 320 × 320, and the three canonical inland hubs. Reuse the existing cosine-corrected frame and the local Natural Earth shoreline identified by SHA-256. Sea stays west and land east. The source resolves only a coarse modern segment here; flattened native elevation is an explicitly declared gameplay abstraction. Do not invent Herod's harbor outline, aqueduct phases, Crusader walls or a modern museum to fill the map. The official park brochure distinguishes successive site phases and is not a 27–36 CE street plan.

The auxiliary SVG still draws from `hubOrder` and does not render the new route points; its 94.45-tile straight-chain metric is not the 175.05-tile relief path. The native compiler must use the explicit points in this binding. The main corridor follows the three hubs. The relief route bends inland through three explicit intermediate points and exists from the start. The guide's reward marks this actual route; it never builds a road, clears an invented crossing or creates combat units. Keep receiving circles and approaches clear. The initial store also intruded into a household court approach; moving it to same-hub offset [0,8] leaves the receiving area clear. The draft reused several exact actor positions and courts; the binding separates those positions without changing identity or district.

Each main record has a distinct living fictional bearer. Move those originals from their pickup positions into the coastal collection circle. Collection records each identity once. Bring each of the three living original bearers to the copying court at least once, then select its original copyist in that court to authorize the stated payment. Arrivals accumulate by identity; simultaneous presence of all three is not required, but every input original remains alive until issuance. A failed affordability check changes nothing; success debits 40 wood and 20 gold once, keeps all three provenance identities and issues the logical register. The body of the copyist is already present, explicitly labelled as uncommissioned; it becomes the register courier after issuance. It is not a register before that fact. A visit to the archive before issuance never counts. Deliver that same original courier to the northern archive afterward.

The additional physical arrival requirement at the copying court has been appended as `o2/req-3` in the authored source refinement commit `817c061`. Preserve `req-1` payment, `req-2` derivation, their IDs and paid receipt. The binding does not silently add a simultaneous-presence condition. The source and the binding now agree on accumulated arrivals.

## Six optional circuits

| Task | Actual player action | Bounded outcome |
|---|---|---|
| Harbor households | Each of two original consignment bearers reaches its assigned, distinct household circle | One withdrawal of 100 food and 50 wood from reserved optional stock |
| Two damaged labels | Both original label bearers reach the coastal copyist circle | Context and main-goal hint; no recovery of missing ancient words |
| Timber store | Select the original damaged store and authorize 50 wood | Restore its captured original full HP once, with no second worker repair charge; reserved 200 food and 100 wood reward |
| Coastal consignment | Escort the original trader, then select it to authorize 50 gold | One reserved 150 food and 50 wood reward |
| North road guide | Escort the original guide to the actual northern junction | Mark the already existing relief path once |
| Working families | Both voluntary original groups reach their refuge circle alive | One reserved 100 food and 25 gold reward |

All bodies and receiving markers have bilingual task-specific names; internal IDs are not displayed as their names. The original copyist is essential before issuance and remains essential as the courier until final delivery. Input bearers are essential until issuance; after the register is issued, their loss cannot erase its provenance. No matching unit type or repeated arrival replaces a missing identity. Optional loss fails that task alone. The final main latch closes all available optional actions before outcome captions; no late reward is credited. Save/load persistence, atomic execution and same-tick defeat priority require native inspection and actual engine observation.

## Difficulty and iteration limits

This opening teaches collection, provenance, consent to payment, independent side circuits and final delivery. It has no hostile roster or secret deadline. The initial draft failed this check on hard: 63 gold could not cover the main 20 gold and optional trade 50 gold without a prior optional reward. The authored refinement raises the initial blueprint gold from 75 to 85, yielding 97/85/72 gold for easy/standard/hard. These corrected vectors cover the main cost and all optional costs without optional income. This is useful for a functional first mission; it is not evidence of a challenging hard mode.

The first native iteration must show what is actually implemented. Only spendable starting stock is put in the player's native bank. The private civilian proxies have economic work rate zero in every profile and all new building/unit production disabled; this prevents a separate manual repair charge or unsupported gathering. This bounded-prototype setting is disclosed, not a final-campaign economy or a difficulty stat boost. Optional reserves stay in separate persistent variables. Protected recovery, a replacement budget and the draft's gatherable bank are not free money or implemented recovery. Until gathering and a complete worker roster exist, the 12/9/6 worker caps and estimated 30–75 minute durations cannot be claimed as difficulty controls. Resource rewards can therefore be mechanically verified before their final strategic value is balanced. Do not add an unauthored war to conceal this limitation.

The next calibration pass must measure route legibility, parallel delivery decisions, optional detour costs, whether rewards create meaningful choices, and the actual duration. If the large regional frame leaves too much inactive space, refine the authored local activity footprint and interests with evidence rather than treating rectangle area as a successful giant map. None of the existing global dossier or historical approval counts increases because this binding exists.
