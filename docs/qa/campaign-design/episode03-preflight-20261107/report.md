# Episode 03 preflight inventory

Read-only mechanical inventory of `03-shared-provision-jerusalem` (source `docs/design/odysseys/faith-origins.json`, order 3). No source files were changed. Entity starts below apply the existing native-start snap convention `floor(x)+0.5`; distances compare those snapped entity centers against continuous authored zone centers, without rounding. This is authored geometry arithmetic, not a certified map or path test.

## Map and original identities

- Map: 320×320; bbox `[35.12, 31.7, 35.3, 31.86]`; WGS84, cosine-corrected longitude, square padding; terrain profile `jerusalem`.
- Three authored hubs (x,y): hub-1 [165.55, 125.68] (West market court); hub-2 [180.69, 157.72] (Domestic kitchen district); hub-3 [186.74, 204.0] (South households).
- Status: georeferenced proposal; neither raster/DEM nor native footprint/pathfinding certified. Main and relief corridors are authored land proposals; relief intermediate geometry remains pending.

| Original | Hub + offset | Native snapped start | Nearest receiving circle (continuous authored center) |
|---|---|---:|---|
| `meal-baskets-1` (fictional-food-consignment) | hub-1 + [-10, 8] | [155.5, 133.5] | destination-1: 12.734005654152982 tiles / r3; overlap=False |
| `meal-baskets-2` (fictional-food-consignment) | hub-1 + [-8, 8] | [157.5, 133.5] | destination-1: 11.222963066855387 tiles / r3; overlap=False |
| `meal-baskets-3` (fictional-food-consignment) | hub-1 + [-6, 8] | [159.5, 133.5] | destination-1: 9.887107767188544 tiles / r3; overlap=False |
| `meal-baskets-4` (fictional-food-consignment) | hub-1 + [-4, 8] | [161.5, 133.5] | destination-1: 8.806525989287715 tiles / r3; overlap=False |
| `distribution-notes-1` (fictional-delivery-note) | hub-2 + [-10, 8] | [170.5, 165.5] | destination-2: 12.820471910191136 tiles / r3; overlap=False |
| `distribution-notes-2` (fictional-delivery-note) | hub-2 + [-8, 8] | [172.5, 165.5] | destination-2: 11.296216180650934 tiles / r3; overlap=False |
## Main predicates and phases

| Phase | Predicate |
|---|---|
| o1 / phase-1 after [] | collected 4 originals (meal-baskets-1, meal-baskets-2, meal-baskets-3, meal-baskets-4); destinations={} |
| o2 / phase-2 after ['o1'] | arrived 4 originals (meal-baskets-1, meal-baskets-2, meal-baskets-3, meal-baskets-4); destinations={'faith-origins.03-shared-provision-jerusalem.meal-baskets-1': 'faith-origins.03-shared-provision-jerusalem.destination-2', 'faith-origins.03-shared-provision-jerusalem.meal-baskets-2': 'faith-origins.03-shared-provision-jerusalem.destination-2', 'faith-origins.03-shared-provision-jerusalem.meal-baskets-3': 'faith-origins.03-shared-provision-jerusalem.destination-2', 'faith-origins.03-shared-provision-jerusalem.meal-baskets-4': 'faith-origins.03-shared-provision-jerusalem.destination-2'}<br>one atomic spendable payment {'food': 160} at ['faith-origins.03-shared-provision-jerusalem.destination-2'] |
| o3 / phase-3 after ['o2'] | arrived 2 originals (distribution-notes-1, distribution-notes-2); destinations={'faith-origins.03-shared-provision-jerusalem.distribution-notes-1': 'faith-origins.03-shared-provision-jerusalem.destination-3', 'faith-origins.03-shared-provision-jerusalem.distribution-notes-2': 'faith-origins.03-shared-provision-jerusalem.destination-3'} |

## Initial-spendable affordability

Main and optional payments are computed from objective predicates only. No gatherable bank, protected recovery stock, optional award, or replacement budget is credited. Optional award is applied after its own payment; optional rewards are excluded from affordability.

- Main payment: `{'food': 160, 'wood': 0, 'gold': 0, 'stone': 0}`.
- Sum of all six optional payment vectors: `{'food': 0, 'wood': 50, 'gold': 50, 'stone': 0}`; exact optional award sum (not credited): `{'food': 550, 'wood': 200, 'gold': 25, 'stone': 0}`.

| Profile | Initial spendable | After main | After main + all optional payments before any award |
|---|---|---|---|
| easy | {'food': 402, 'wood': 172, 'gold': 86, 'stone': 0} | {'food': 242, 'wood': 172, 'gold': 86, 'stone': 0} | {'food': 242, 'wood': 122, 'gold': 36, 'stone': 0} |
| standard | {'food': 350, 'wood': 150, 'gold': 75, 'stone': 0} | {'food': 190, 'wood': 150, 'gold': 75, 'stone': 0} | {'food': 190, 'wood': 100, 'gold': 25, 'stone': 0} |
| hard | {'food': 297, 'wood': 127, 'gold': 63, 'stone': 0} | {'food': 137, 'wood': 127, 'gold': 63, 'stone': 0} | {'food': 137, 'wood': 77, 'gold': 13, 'stone': 0} |

For each profile, main-only and all-optionals portfolios are arithmetically affordable from initial spendable stock. This is resource arithmetic, not evidence of available UI, native account placement, route feasibility, or gameplay.

## Six optional objectives

| ID / kind | Authored payment | Award after payment |
|---|---|---|
| side-1 / aid — Market families | {'food': 0, 'wood': 0, 'gold': 0, 'stone': 0} | {'food': 100, 'wood': 50} |
| side-2 / copy — Household lists | {'food': 0, 'wood': 0, 'gold': 0, 'stone': 0} | {} |
| side-3 / repair — Kitchen store | {'food': 0, 'wood': 50, 'gold': 0, 'stone': 0} | {'food': 200, 'wood': 100} |
| side-4 / trade — Grain carrier | {'food': 0, 'wood': 0, 'gold': 50, 'stone': 0} | {'food': 150, 'wood': 50} |
| side-5 / guide — Western footpath | {'food': 0, 'wood': 0, 'gold': 0, 'stone': 0} | {} |
| side-6 / extract — Guests seeking lodging | {'food': 0, 'wood': 0, 'gold': 0, 'stone': 0} | {'food': 100, 'gold': 25} |

No authored payment for side-1, side-2, side-5, side-6; side-3 costs 50 wood; side-4 costs 50 gold.

## Screens and narrator flow

The episode has 39 screens. Flow: fact intro (collection narrator) → narrator handover → Miriam persona intro; route/economy help and three main phases; six optional goal/completion/loss triplets; fact outro (collection narrator) → persona outro (Miriam) → continuation prompt. Estimated authored voice durations sum to 347 seconds across all screens; optional/conditional screens are not necessarily all played in one run.

Continuation is order 4, `04-testimony-relay-damascus`: “The Road He Remembered” / “El camino que recordaba”.

## Reusable current helpers

- `tools/python/native_mission.controller.py`: phase/terminal state and trigger scaffolding.
- `tools/python/native_spatial.helper.py`: snapped/circle identity observation predicates.
- `tools/python/native_transactions.helper.py`: guarded finite resource transactions.
- `tools/python/native_secondary.adapter.py`: bounded authored secondary objective validation/rendering.

These are reusable components; their presence does not mean this episode composes into a supported native controller.

## Why existing native validators reject episode 03

- `native_delivery.adapter.py` accepts one specific archive-copy pattern: phase 2 must contain payment + derived token + arrival of originals at copy court, followed by delivery of one derived output. Episode 03 phase 2 has four baskets arriving at kitchen plus payment; phase 3 delivers two notes. It has no derived token or physical copy-arrival operation; counts and provenance are different.
- `native_household.adapter.py` is fixed to episode 02: eight specified household identities, court/refuge zones, 6-of-8 threshold, and a survivor loss contract. Episode 03 has six different identities, three receiving districts and no survivor group. The validator rejects both episode ID and source/binding contract mismatch.
- Exact operation gap observed: current private native adapters do not implement the authored combination “four originals arrive at kitchen + one payment, then two different originals arrive at southern households” with this identity ledger and phase graph. No replacement semantics are proposed here.

## Source and status boundaries

- Canonical dossier and embedded episode blueprint are both in `docs/design/odysseys/faith-origins.json`; the generated wiki dossier is `docs/wiki/faith-origins/episodes/03-shared-provision-jerusalem/15-odyssey-dossier.md`.
- Editorial approval, geographic/terrain certification, native composition, and game play evidence remain pending in source. No history or game approval is inferred.
