# Catalogue design-risk inventory

Documentary triage of the authored dossier data for d00002/S11. This is not a game test, a balance verdict, a playability approval, a historical review or a replacement for the connected DelendAI workflow. Every finding is a statement about authored data, and every finding keeps its own limits.

| Item | Value |
|---|---|
| Identity | `minimax-m3.1-flash-preview` (observed MiniMax identity; no inherited `gpt-6` identity or session) |
| DelendAI session | `7005c2a9` (own session, issued by `delendai work enter`) |
| Work unit | `refs/heads/wip/minimax-m3.1-flash-preview/implement/d00002-S11-g11/catalogue-design-risk-inventory` |
| Worktree | `.cache/delendai/.worktrees/minimax-m3.1-flash-preview-d00002-S11-g11` |
| Source commit | `1a286985124d43ad43b9c3ade1c3047448fb3a82` (develop, after the Jerusalem source refinement was landed) |
| Date | 2026-10-27 |
| Machine-readable companion | [`catalogue-design-risk-inventory.json`](catalogue-design-risk-inventory.json) |
| Git author and committer | Cartago `<cartago.relaxingcup@gmail.com>` |

## Scope and discriminator

64 materialized `episodes[]` dossiers were inspected: 30 from `docs/design/odysseys/faith-origins.json` and 34 from `docs/design/odysseys/imperial-church.json`. The remaining seven selected odysseys (`jewish-tradition`, `church-of-rome`, `new-rome`, `first-caliphs`, `first-fitna`, `umayyads`, `house-of-ali`) were read and hashed but hold no dossier: only `episodeSelection[]` entries, which are never counted as dossiers. `episodeBlueprints[]` is likewise never counted. `docs/design/geography.json` and `docs/research/odyssey-research/civic-difficulty-mechanical-audit.json` were read for context only.

### Sources read, with the SHA-256 recorded for every pointer

| Path | SHA-256 | Role |
|---|---|---|
| `docs/design/odysseys/faith-origins.json` | `0db4c1c70be830847a73d577922e619e8b1c22cd9faf08f2fa5aac44ee5c1d5a` | full dossier source |
| `docs/design/odysseys/imperial-church.json` | `e15c0f183b5d6fe0c7061530480221fef541573bd2e314d0d615f73f7b45b25b` | full dossier source |
| `docs/design/odysseys/jewish-tradition.json` | `2531c1fdea1ea400d620aeb507ef87f430053e3172208f3896a608b6a764d5a5` | selected odyssey without dossiers |
| `docs/design/odysseys/church-of-rome.json` | `2f16b67dd2c9b1381311596080988ed96d927323f741382f6ceec82f077ad885` | selected odyssey without dossiers |
| `docs/design/odysseys/new-rome.json` | `99da4a9277885cf4d87bd0b3a798a236a698542d4b4f078a768993611b85c7da` | selected odyssey without dossiers |
| `docs/design/odysseys/first-caliphs.json` | `2b86695a649e539bced604a6bd505683fb66b77678a154f0a525bf0a757351c0` | selected odyssey without dossiers |
| `docs/design/odysseys/first-fitna.json` | `36c56f6a38185b7761dda3e549b165cd3aa0dab2a96ec4981000a4d22c6d59c4` | selected odyssey without dossiers |
| `docs/design/odysseys/umayyads.json` | `ceafcad8d3f8b61eaf180a9daee82c623c7f5acc052fef92a9a4a31add93d402` | selected odyssey without dossiers |
| `docs/design/odysseys/house-of-ali.json` | `ab16494bd49144ba3ba243e4231bdf97b1dec8fdc29dfbe1f8b6fbf1f5565a05` | selected odyssey without dossiers |
| `docs/design/geography.json` | `26231728e1cf135b84a50e815efd6a9e286ca8700204421bca7273818baf35c1` | existing geography profiles |
| `docs/research/odyssey-research/civic-difficulty-mechanical-audit.json` | `b2815ef32913d821fcaff5f9ae6d196bc695b04a64767305ddc513acb125224e` | civic difficulty audit |
| `docs/design/odyssey-policy.json` | `44f2126ea6f5dd0969445602230245db0adb7da3f636d0e932acd89d68f8f8fc` | declared campaign coverage |

The `faith-origins` hash is the one that changed with the Jerusalem source refinement landed at `1a28698`; the `imperial-church` hash is unchanged by it. Every pointer in the JSON resolves against the hash recorded for its own source.

The explicit discriminator is `episode.designProfile`. An absent value selects the legacy v2 shape (63 dossiers); the explicit value `alternative-fulfillment-v3` selects the v3 shape (1 dossier: `imperial-church/34-church-transfer-constantinople`). Both shapes were analysed on their own terms. The v3 dossier is never stripped, downgraded to v2 or re-shaped, and its v3-only fields (`accountsByDifficulty`, `referenceCapabilityProfile.fulfillmentPlan`, `optionalFinancialInputs`) are read as authored.

The civic difficulty audit's 54 static risk candidates measure a different property and are not reused, recounted or restated here as if they were these results.

## Summary

| Check | Dossiers with a finding | Finding evidence items | Recorded geometry items | Disposition |
|---|---:|---:|---:|---|
| 1. Exact initial actor position collisions | 25 | 66 | 66 | `design-risk` |
| 2. Main and relief corridor geometry | 19 | 38 | 84 | `design-risk` (15), `needs-physical-binding` (4) |
| 3. Authored building at a receiving centre | 0 | 0 | 70 | none |
| 4. Initial spendable against explicit payments | 50 | 150 | 192 | `conditional-budget` |
| 5. Worker cap without a placed-worker roster | 63 | 368 | 377 | `needs-physical-binding` |
| 6. Repeated role phrases | 44 | 150 | 150 | `editorial-candidate` |

64 dossier rows, 201 dossier-check findings, 4 dispositions in use. Every aggregate above is recomputed from the rows by the verifier, and every recorded pointer resolves against the recorded source hash.

## Actionable patterns

### P1 — Two actors share one authored initial tile (25 dossiers, 66 positions) — `design-risk`

Two or more authored actors in the same dossier carry the same explicit `initialHub` and `offsetTiles`, so they resolve to one authored tile. The overlap is exact in authored tile coordinates. Native body footprints are not certified for any of these dossiers, so the native outcome is unknown and no obstruction is asserted.

Affected dossiers (each row of the JSON lists the colliding entity ids, the hub, the offset, the hub centre and the absolute tile):

- `faith-origins/07-household-relocation-rome-ostia`, `faith-origins/09-district-production-corinth`, `faith-origins/10-copy-and-relay-corinth`, `faith-origins/11-distributed-preservation-ephesus`, `faith-origins/12-bounded-community-aid-ephesus`, `faith-origins/13-consignment-and-correspondence-corinth`, `faith-origins/14-administrative-intrigue-caesarea`, `faith-origins/15-evacuation-and-recovery-rome-ostia`, `faith-origins/18-parallel-archive-logistics-antioch`, `faith-origins/03-the-governors-question`, `faith-origins/22-reading-and-relief-rome-ostia`, `faith-origins/23-petition-escort-sardes`, `faith-origins/24-witness-and-evacuation-lyon`, `faith-origins/26-legal-record-network-carthage`, `faith-origins/27-household-aid-and-memory-carthage`, `faith-origins/28-certificate-and-refuge-egypt-middle-nile`, `faith-origins/29-bounded-evacuation-carthage`, `faith-origins/04-a-different-dawn`
- `imperial-church/01-milvian-bridge`, `imperial-church/02-bounded-negotiation-milan`, `imperial-church/03-property-and-record-restoration-nicomedia`, `imperial-church/04-rival-delegation-reception-rome-ostia`, `imperial-church/05-delegate-logistics-arles`, `imperial-church/07-court-record-logistics-rome-ostia`, `imperial-church/08-disputed-correspondence-alexandria`

### P2 — Main and relief corridors carry identical authored geometry (15 dossiers) — `design-risk`

The `main` and `relief` corridors of these dossiers share the same authored hub sequence and the same `land` movement mode, so no alternate authored route is distinguishable in the data. This is an authored-geometry observation. It is not proof of failed native pathfinding, and it is not a claim that a relief route is unnecessary in play.

- `faith-origins/01-roads-of-antioch`, `faith-origins/02-civilian-refuge-jerusalem`, `faith-origins/03-shared-provision-jerusalem`, `faith-origins/04-testimony-relay-damascus`, `faith-origins/05-witness-comparison-jerusalem`, `faith-origins/07-household-relocation-rome-ostia`, `faith-origins/08-delegate-logistics-jerusalem`, `faith-origins/09-district-production-corinth`, `faith-origins/10-copy-and-relay-corinth`, `faith-origins/11-distributed-preservation-ephesus`, `faith-origins/12-bounded-community-aid-ephesus`, `faith-origins/13-consignment-and-correspondence-corinth`, `faith-origins/14-administrative-intrigue-caesarea`, `faith-origins/15-evacuation-and-recovery-rome-ostia`, `faith-origins/16-comparative-copying-antioch`

### P3 — A relief corridor exists but no alternate polyline is authored (4 dossiers) — `needs-physical-binding`

The `main` and `relief` corridors differ by hub sequence only, and neither authors explicit `points`. The alternate route therefore has no authored geometry that could be certified against the native map. The single dossier that does author explicit points for both corridors, `imperial-church/34-church-transfer-constantinople`, compares as clear.

- `faith-origins/02-after-the-siege`, `faith-origins/03-the-governors-question`, `faith-origins/24-witness-and-evacuation-lyon`, `faith-origins/25-archive-comparison-lyon`

The remaining 44 dossiers author no `main`/`relief` pair at all and are recorded as `not-applicable`, with their authored corridor ids listed per row.

### P4 — Negative no-gathering margin (50 dossiers, 119 profile rows) — `conditional-budget`

The initial spendable stocks were compared against the payment totals read directly from the objective predicates, not from the declared summary vectors. The mandatory total is the sum of `objectivePlan[].predicate.requirements[]` of kind `resource-transaction`; the optional total is the sum of `secondaryObjectives[].predicate.requirements[]` of kind `atomic-payment`. In all 63 legacy dossiers the direct totals reproduce the declared `mandatoryDeliveries` and `maxOptionalCosts` vectors exactly, so the declared summaries are confirmed, not assumed.

In 50 dossiers at least one difficulty profile ends with a negative margin in at least one resource. Every such row is **conditional**: the authored finite `gatherableBank` may legitimately fund the cost, and the dossier itself declares the margin as a static feasibility estimate with native calibration pending. Protected recovery stock and the optional payout reserve are recorded separately and are never subtracted; an optional reward is never treated as mandatory funding.

Negative rows by resource: wood 92, gold 63, food 46, stone 15. Negative rows by campaign: `imperial-church` 91, `faith-origins` 28. The v3 dossier contributes 8 negative rows (2 selections on `standard`, 6 on `hard`), and the authored selection analysis already marks exactly those selections unaffordable.

Affected dossiers: `faith-origins/02-after-the-siege`, `faith-origins/03-the-governors-question`, `faith-origins/04-a-different-dawn`, `faith-origins/09-district-production-corinth`, `faith-origins/11-distributed-preservation-ephesus`, `faith-origins/12-bounded-community-aid-ephesus`, `faith-origins/14-administrative-intrigue-caesarea`, `faith-origins/15-evacuation-and-recovery-rome-ostia`, `faith-origins/16-comparative-copying-antioch`, `faith-origins/18-parallel-archive-logistics-antioch`, `faith-origins/20-reconciliation-deliveries-rome-ostia`, `faith-origins/22-reading-and-relief-rome-ostia`, `faith-origins/23-petition-escort-sardes`, `faith-origins/24-witness-and-evacuation-lyon`, `faith-origins/25-archive-comparison-lyon`, `faith-origins/26-legal-record-network-carthage`, `faith-origins/27-household-aid-and-memory-carthage`, `faith-origins/28-certificate-and-refuge-egypt-middle-nile`, `faith-origins/29-bounded-evacuation-carthage`; and 31 of the 34 `imperial-church` dossiers, that is every one except `imperial-church/01-milvian-bridge`, `imperial-church/06-finite-field-withdrawal-cibalae` and `imperial-church/09-crossing-and-supply-adrianople`.

### P5 — Numeric worker caps without a placed-worker roster (63 legacy dossiers, 189 caps) — `needs-physical-binding`

Every legacy dossier authors `maxVillagers` of 12 / 9 / 6 for easy / standard / hard, and the `difficultyLevers` prose names that many workers. The legacy contract shape carries no placed-worker roster: no entity is bound as a worker unit and no player-controllable worker entity is authored. The worker count exists only as prose and as a cap, so it is neither a roster nor proof that worker units exist.

This finding covers all 63 legacy-v2 dossiers; the JSON row for each carries the three cap pointers, the prose pointer and the empty roster. The v3 dossier is recorded as `not-applicable`: its v3 difficulty shape authors no `maxVillagers` key, and it does carry an explicit worker binding, since both `fulfillmentPlan` recipes' `workerId` values resolve to authored entities.

### P6 — Repeated role phrases in optional objective sentences (44 dossiers, 150 sentences) — `editorial-candidate`

The role noun that the authored optional template already introduces occurs more than once in the same authored sentence, so phrases such as `trader of ... trader` reach the player. The source text is quoted with its pointer and a small bilingual wording alternative is proposed. The inventory does not rewrite the authoring.

By kind: `guide` 78, `repair` 33, `scout` 24, `trade` 10, `copy` 5. By language: `es-ES` 76, `en` 74. Sentences per affected dossier: 6 in nine dossiers, 5 in one, 4 in twelve, 2 in twenty-one, 1 in one.

Worked examples, with the pointer to the authored subject and the full quoted sentence:

| Kind | Pointer | Quoted | Proposed alternative |
|---|---|---|---|
| `trade` | `/episodes/1/secondaryObjectives/3/text/en` | "Escort the trader of olive road trader to the receiving post, then pay 50 gold for one consignment." | "Escort the trader of olive road carrier to the receiving post, then pay 50 gold for one consignment." |
| `trade` | `/episodes/1/secondaryObjectives/3/text/es-ES` | "Escolta al comerciante de comerciante del camino de los olivos hasta el puesto receptor y paga 50 de oro por una sola remesa." | "Escolta al comerciante de portador del camino de los olivos hasta el puesto receptor y paga 50 de oro por una sola remesa." |
| `guide` | `/episodes/0/secondaryObjectives/4/text/en` | "Escort the local guide of north road guide to the marked road junction." | "Escort the local guide of north road route to the marked road junction." |
| `repair` | `/episodes/0/secondaryObjectives/2/text/en` | "Pay 50 wood and restore the damaged store of timber store to full health." | "Pay 50 wood and restore the damaged store of timber shed to full health." |
| `scout` | `/episodes/16/secondaryObjectives/4/text/en` | "Scout both marked viewpoints of western-approach viewpoints." | "Scout both marked viewpoints of western-approach lookout." |
| `copy` | `/episodes/10/secondaryObjectives/0/text/en` | "Recover both separate copies from parallel discussion copies and deliver them to the copyist." | "Recover both separate copies from parallel discussion leaf and deliver them to the copyist." |

The alternatives above are mechanical label-level substitutions and a few of them read awkwardly, for example "parallel discussion leaf". They are candidates for the architect, not finished copy. Where a sentence does not embed the authored label verbatim, the JSON records the label-level alternative only and leaves the sentence wording to the architect.

Affected dossiers: `faith-origins/01-administrative-records-caesarea`, `faith-origins/01-roads-of-antioch`, `faith-origins/02-civilian-refuge-jerusalem`, `faith-origins/02-after-the-siege`, `faith-origins/03-shared-provision-jerusalem`, `faith-origins/03-the-governors-question`, `faith-origins/04-testimony-relay-damascus`, `faith-origins/05-witness-comparison-jerusalem`, `faith-origins/07-household-relocation-rome-ostia`, `faith-origins/08-delegate-logistics-jerusalem`, `faith-origins/09-district-production-corinth`, `faith-origins/10-copy-and-relay-corinth`, `faith-origins/11-distributed-preservation-ephesus`, `faith-origins/12-bounded-community-aid-ephesus`, `faith-origins/13-consignment-and-correspondence-corinth`, `faith-origins/14-administrative-intrigue-caesarea`, `faith-origins/15-evacuation-and-recovery-rome-ostia`, `faith-origins/16-comparative-copying-antioch`, `faith-origins/18-parallel-archive-logistics-antioch`, `faith-origins/19-hospitality-network-antioch`, `faith-origins/20-reconciliation-deliveries-rome-ostia`, `faith-origins/22-reading-and-relief-rome-ostia`, `faith-origins/23-petition-escort-sardes`, `faith-origins/24-witness-and-evacuation-lyon`, `faith-origins/25-archive-comparison-lyon`, `faith-origins/26-legal-record-network-carthage`, `faith-origins/27-household-aid-and-memory-carthage`, `faith-origins/28-certificate-and-refuge-egypt-middle-nile`, `faith-origins/29-bounded-evacuation-carthage`; `imperial-church/02-bounded-negotiation-milan`, `imperial-church/02-nicaea`, `imperial-church/03-property-and-record-restoration-nicomedia`, `imperial-church/03-new-capital`, `imperial-church/05-delegate-logistics-arles`, `imperial-church/10-land-and-strait-logistics-chrysopolis`, `imperial-church/13-finite-works-logistics-jerusalem`, `imperial-church/15-long-distance-dispatch-nicomedia`, `imperial-church/16-witness-record-comparison-tyre`, `imperial-church/17-rumour-and-source-investigation-constantinople`, `imperial-church/18-administrative-transition-nicomedia`, `imperial-church/20-separate-reception-logistics-sardica`, `imperial-church/23-bounded-political-pressure-milan`, `imperial-church/24-night-civilian-withdrawal-alexandria`, `imperial-church/34-church-transfer-constantinople`.

### Check 3 — No authored building at a receiving centre (0 findings, 64 clear)

An earlier draft of this inventory reported every authored building as a finding because it shared a hub with a receiving circle and was inside the authored hub radius. That reading was wrong and has been withdrawn. The authored `worldContract` zone radius is what defines reception; the authored hub radius is activity geography, and same-hub membership is not a finding.

The rule now applied is: a finding requires the explicit distance from the authored building to the authored receiving-circle centre to be less than or equal to the authored receiving radius. Under that rule no authored building qualifies. The 70 recorded geometry items (63 authored `repair` stores in the legacy shape and 7 authored objects in the v3 shape) are kept in the JSON with their hub, hub centre, lonLat, offsets, absolute tile, distance to hub centre, closest receiving circle and its radius.

One authored margin is worth the architect's attention even though it is not a finding. In 46 of the 70 recorded buildings the closest authored receiving circle is 3.606 tiles away against its 3-tile radius, that is about 0.6 authored tiles of clearance. No authored building is inside its receiving circle, so the check is clear, but a margin that thin is sensitive to any later change of the authored offsets or radii. The per-row note `authoredClearanceAtOrBelowOneTile` records how many buildings in that dossier have this thin margin, and the JSON keeps every distance so the margin can be re-read after any authoring change.

The native footprint of every one of these buildings is still uncertified, so the physical clearance of a building that stands outside the authored receiving circle remains unknown. That unknown is recorded in the JSON notes and is deliberately not counted as a finding.

## What is not established here

- No native body footprint, radius, pathfinding result or engine behaviour is certified. A P1 overlap is an authored coordinate collision, not a proved native obstruction.
- A P2 or P3 corridor observation says nothing about whether a route works in play. Only one dossier authors explicit corridor points, and that one is not flagged.
- The P4 margins are conditional on authored gathering, not failures. No gathering rate, travel time or player behaviour was measured.
- The P5 caps are authored numbers. Whether worker units would be placed, and how many, is an open design decision for the owning dossier slice.
- The P6 wording candidates are editorial proposals; the authored sentences are unchanged.
- The 54 static risk candidates of the civic difficulty audit are a different metric and are not restated here.
- The seven selected odisseys without dossiers were read, not analysed as dossiers. Their authored selection text may repeat the same optional templates when the dossiers are written.

## Recommendation to the architect

1. Decide the P6 wording policy first, because it is the cheapest to close and it touches 44 dossiers in both languages. Either accept the mechanical label substitution recorded per row, or state one house rule for the optional templates and let the owning slices apply it.
2. Assign P1 per dossier slice. Each collision is two authored entity ids at one hub and offset, so a fix is a placement decision inside the owning slice, not a catalogue-wide change. No contract, identifier or count changes.
3. Assign P2 and P3 to the map owner of the affected dossiers, and ask for an explicit alternate polyline or an explicit statement that the hub sequence is the whole authored geometry. One decision per dossier.
4. Decide the thin authored clearance recorded under check 3. No authored building is inside its receiving circle, but 46 of the 70 recorded buildings sit about 0.6 authored tiles outside it. Confirm that margin as authored, or move the affected offsets inside the owning slice.
5. Treat P4 as a confirmation exercise, not a repair list. The declared summary vectors already agree with the direct objective payment totals in all 63 legacy dossiers, so the remaining question is whether the authored gathering bank is intended to cover the negative rows, per dossier.
6. Treat P5 as one contract question for the architect: either the legacy shape should gain a worker binding, or the legacy dossiers should stop asserting a worker count that no authored entity realises. That decision belongs outside the dossier slices and outside this inventory.
7. No change to the catalogue metrics: 64 dossiers, 214 pending selections, 2645 screens and 398 secondary objectives are unchanged by this work.

## Verification and evidence

A one-off generator and a one-off verifier were used. Neither is a repository test, neither mirrors an existing repository tool and no dependency was added. Both live outside the tracked tree, in the unit-local ignored directory `.cache/catalogue-risk-evidence/` of this work unit.

The verifier re-reads the recorded sources and confirms:

- every recorded source SHA-256 still matches the file on disk, and every dossier row carries the hash of its own source;
- every recorded JSON pointer resolves against the recorded source, including the nested actor, building, circle, corridor, cap, payment, subject and text pointers;
- the budget arithmetic reproduces from the objective predicates: the direct mandatory and optional totals, the margin without gathering, the mandatory-only margin, the negative resource set, the declared-vector cross-checks and, for the v3 dossier, the unaffordable selection count and the binding selection;
- the corridor identity and comparison basis reproduce from the source corridors;
- the building distances, the absolute tiles, the hub distances and the inside-receiving-circle flags reproduce, and no dossier reports a building finding without an intrusion, or a clear result with one;
- the collision tiles and actor counts reproduce, and no dossier with a duplicated authored position is reported as clear;
- the worker caps reproduce per difficulty level;
- the quoted role-phrase subjects and texts reproduce, the role noun really occurs more than once in the quoted sentence, the proposed alternative removes the repetition, and no dossier with a repeated sentence is reported as clear;
- the row counts, the per-check findings, the finding evidence items, the recorded geometry items, the disposition totals and the finding pairs all reconcile with the rows;
- the Markdown report states the same per-check counts and the same source hashes as the JSON.

Result: 17 verification checks, 0 failures.

## Limitations

This is documentary triage of authored data. It approves no historical claim, no geography, no balance, no playability and no native capability. It introduces no citation, no voice and no historical assertion. It changes no contract, string range, campaign identity, dossier count, selection count, screen count, secondary-objective count, identifier or registry. The shared `develop` checkout was not modified; all work is confined to this work unit and is offered for root review before any official publication.
