# Yavneh design candidate: materialization report

Worker: `minimax-m3.1-flash-preview` · 27 October 2026 · proposal `d00002` · slice `S4` ·
generation 2 · topic `yavneh-blueprint-materialization`.

**Update — 28 October 2026 (finalization).** The architect's four pinned source inputs
landed officially on `develop` at `44e89db7e52228fbddda80be1adae18ae90595cf`, and an
independent GPT-6.1-Sol technical review confirmed this candidate. The four open questions
raised by the first version of this report are now **resolved** and recorded below. The
candidate JSON and the SVG are **unchanged, byte for byte**; only this report was edited.
This remains an **unregistered design candidate**: it does not count a canonical dossier,
does not approve history, terrain, native support or gameplay, and does not approve S4.

## Delivered files (exactly three)

| File | Bytes | SHA-256 |
|---|---|---|
| `docs/design/episode-plans/jewish-tradition/02-yavneh-blueprint-candidate.json` | 196017 | `6a4aebef62b240325407121b5366d5de2277d1a95eaeba1782645ea5411e7690` |
| `docs/design/episode-plans/jewish-tradition/02-yavneh-blueprint-map.svg` | 14377 | `4696813df3d5a384586386a4c2dab18e23e5719206e138a656751a4d6c26d34d` |
| `docs/qa/campaign-design/yavneh-blueprint-materialization-report.md` | this file | — |

The candidate and the map were produced in commit `d6321cb88eb63e41346d9f30203fc2e9522d1ab0`
and are **byte-identical after the finalization merge** of `44e89db7` and after the
finalization pipeline re-run; only this report changed afterwards.

No other tracked file, schema, code path, dependency, source campaign, identifier,
geography registry, source registry or catalogue counter changed. Temporary assembly and
verification scripts and evidence live only in the worker unit's ignored `.cache/yavneh/`.

## Pinned source inputs (read-only, not copied into tracked Files)

Four inputs were pinned. At materialization time they were read from the architect's
read-only unit
`/home/cartago/_projects/games/aoe2-mods/.cache/delendai/.worktrees/gpt-6-d00002-S4-g2`
at commit `458178f`; two of them (world plan and allocation decision) were already
integrated on `develop` and were read byte-identically from there.

| Input | SHA-256 | Status on 28 October 2026 |
|---|---|---|
| `docs/design/episode-plans/jewish-tradition/02-yavneh-materialization-specification.json` (revision 2) | `dd44ee643069ae6f38f3fa3457cc7c3768c233588720604422b2860b46835b57` | landed officially on `develop` at `44e89db7` |
| `docs/design/episode-plans/jewish-tradition/02-yavneh-profile-architect-decisions.json` | `5a7b63d3c00d8a748717298f48d4615ba1250317b73e5614f9533ac01c73de26` | landed officially on `develop` at `44e89db7` |
| `docs/design/episode-plans/jewish-tradition/02-yavneh-world-plan.json` | `388e2d27b707b35d73a07423c415653e02482a2620ea208ce4ee05cc03942046` | already integrated before materialization; unchanged |
| `docs/wiki/jewish-tradition/research/yavneh-allocation-decision.json` | `80ec2b2bfe683f5c116f7bc082df801a5f308b9db3860018dc554ddf82c12f47` | already integrated before materialization; unchanged |

Provenance, preserved: the architect commits were not cherry-picked, the architect's agent
and session were not used, and no source input was copied into tracked `Files`. The first
version of this report said that "the three source documents above still live only in the
architect's unit"; that was inaccurate on two counts and is corrected here. The table lists
**four** inputs, not three, and only the two architect-authored documents (the revision-2
specification and the profile architect decisions) were architect-unit-only at
materialization time — the world plan and the allocation decision were already integrated
on `develop` and were consumed from there. The pending-source state is now **superseded**:
all four inputs are canonical, and the finalization run re-verified all four SHA-256
values from this unit's own merged `develop`.

## Independent technical review (GPT-6.1-Sol)

Root reports an independent conformity review of commit
`d6321cb88eb63e41346d9f30203fc2e9522d1ab0` by **GPT-6.1-Sol**: 673 source/candidate checks
and the actual `project_batch` → factory → audit run with **0 errors**, 44 screens and
8/5/3 affordable selections, with a **byte-identical SVG**. Root's evidence artifacts are
at `/home/cartago/.codex/artifacts/aoe2-mods/yavneh-blueprint-review-20261028/`.

That review is a **technical conformity review of this candidate only**. It is not a broad
`S4` approval, not a historical approval, not a native or game approval, and it does not
create dossier 65.

## Finalization pipeline re-run (28 October 2026)

The focused real pipeline was re-run from the **committed candidate** and this unit's own
canonical sources (after merging `44e89db7`), with every output written under the
worker unit's ignored `.cache/yavneh/finalization/`. No tracked file was written, the
assembly script was not re-run, and no architect worktree is required any more.

| Result | Value |
|---|---|
| `project_batch` (real typed bridge, strict v3 schema + semantic validator) | ok, `02-refuge-and-school-supply-yavneh` |
| `build_fulfillment_dossier` (real campaign, order-1/order-3 selections, unregistered region) | composed |
| `audit_dossier` (real `projection_context`) | **`audit errors: []`** |
| Screens / text variants | 44 / 88 |
| Services / secondary objectives | 3 / 7 |
| Affordable selections easy/standard/hard | 8 / 5 / 3 |
| Re-rendered map vs committed map | **identical** (`renderedSvgMatchesCommittedSvg: true`) |
| Candidate JSON SHA-256 after re-run | `6a4aebef62b240325407121b5366d5de2277d1a95eaeba1782645ea5411e7690` (unchanged) |
| Map SVG SHA-256 after re-run | `4696813df3d5a384586386a4c2dab18e23e5719206e138a656751a4d6c26d34d` (unchanged) |

Evidence files: `.cache/yavneh/finalization/projection-request.json`,
`projection.json`, `episode.json`, `audit.json`, `rendered-map.svg` and
`finalization-summary.json`.

## Pipeline actually executed

No operation was emulated, no validator was weakened and no operation was invented.
The real components were used in this order.

1. **`tools/design/fulfillment-dossier.helper.py::project_batch`** — one typed batch over
   the real Bun bridge `tools/design/fulfillment-dossier.script.ts` →
   `tools/design/fulfillment-dossier.mapper.ts` → `capabilityProfileV3Schema` (strict
   `packages/schemas/alternative-fulfillment.schema.ts`) and
   `validateScenarioCapability`. Result: `projection ok:
   02-refuge-and-school-supply-yavneh`. The projection request is the candidate envelope
   **minus** `designProfile` and `dossierMetadata`; no foreign key was inserted into the
   strict request.
2. **`tools/design/episode_dossier.factory.py::build_fulfillment_dossier`** — composed with
   the real `jewish-tradition` campaign (`campaignId`, `editorialContract`), the real
   selection `02-refuge-and-school-supply-yavneh` (order 2), the real order-1 selection
   `01-a-city-of-names` and the real order-3 selection `03-distributed-study-network-yavneh`,
   and an explicitly passed **unregistered** candidate regional profile
   (`id=yavneh`, `bbox=[34.71, 31.83, 34.79, 31.9]`, `registrationStatus=unregistered
   candidate region; not a canonical geography profile`). No canonical geography insertion

## Pipeline actually executed

No operation was emulated, no validator was weakened and no operation was invented.
The real components were used in this order.

1. **`tools/design/fulfillment-dossier.helper.py::project_batch`** — one typed batch over
   the real Bun bridge `tools/design/fulfillment-dossier.script.ts` →
   `tools/design/fulfillment-dossier.mapper.ts` → `capabilityProfileV3Schema` (strict
   `packages/schemas/alternative-fulfillment.schema.ts`) and
   `validateScenarioCapability`. Result: `projection ok:
   02-refuge-and-school-supply-yavneh`. The projection request is the candidate envelope
   **minus** `designProfile` and `dossierMetadata`; no foreign key was inserted into the
   strict request.
2. **`tools/design/episode_dossier.factory.py::build_fulfillment_dossier`** — composed with
   the real `jewish-tradition` campaign (`campaignId`, `editorialContract`), the real
   selection `02-refuge-and-school-supply-yavneh` (order 2), the real order-1 selection
   `01-a-city-of-names` and the real order-3 selection `03-distributed-study-network-yavneh`,
   and an explicitly passed **unregistered** candidate regional profile
   (`id=yavneh`, `bbox=[34.71, 31.83, 34.79, 31.9]`, `registrationStatus=unregistered
   candidate region; not a canonical geography profile`). No canonical geography insertion
   was attempted: `docs/design/geography.json` still holds 26 profiles and no `yavneh`
   profile.
3. **`tools/design/episode_dossier.validator.py::audit_dossier`** with the actual
   `projection_context={'request': ..., 'projection': ...}`. Result: **`audit errors: []`**.
   The audit revalidates the typed request against the bridge, so the composed dossier is
   the one the projector produced.
4. **`tools/design/episode_dossiers.script.py::diagram(actual_episode, [])`** — the only
   renderer used, producing `02-yavneh-blueprint-map.svg` (14377 bytes).
5. **`tools/design/civic_difficulty_audit.script.py::episode_audit`** on the composed
   episode takes the real opt-in v3 branch and reports `designProfile
   alternative-fulfillment-v3`, `affordableSelectionCountByDifficulty {easy 8, standard 5,
   hard 3}` and the authored accounts.

### Reproduction from the committed candidate only

```sh
python3 - <<'PY' > /tmp/yavneh-request.json
import json
b = json.load(open('docs/design/episode-plans/jewish-tradition/02-yavneh-blueprint-candidate.json'))
print(json.dumps({"requests": [{k: v for k, v in b.items() if k not in ("designProfile", "dossierMetadata")}]}))
PY
python3 tools/design/fulfillment-dossier.helper.py \
  < .cache/yavneh/finalization/projection-request.json \
  > .cache/yavneh/finalization/projection.json
```

```sh
python3 - <<'PY'
import importlib.util, json, runpy, sys
from pathlib import Path
root = Path.cwd(); sys.path.insert(0, str(root / "tools/design"))
def load(name):
    p = root / "tools/design" / f"{name}.py"
    s = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m); return m
factory = runpy.run_path(str(root / "tools/design/episode_dossier.factory.py"))
validator = load("episode_dossier.validator"); pipeline = load("episode_dossiers.script")
blueprint = json.load(open("docs/design/episode-plans/jewish-tradition/02-yavneh-blueprint-candidate.json"))
campaign = json.load(open("docs/design/odysseys/jewish-tradition.json"))
projection = json.load(open(".cache/yavneh/finalization/projection.json"))["projections"][0]
selection = {r["id"]: r for r in campaign["episodeSelection"]}
region = {"id": "yavneh", "bbox": [34.71, 31.83, 34.79, 31.9], "registrationStatus": "unregistered candidate region"}
compose = factory["build_fulfillment_dossier"]
episode = compose(
    {"campaignId": campaign["campaignId"], "editorialContract": campaign["editorialContract"]},
    selection["02-refuge-and-school-supply-yavneh"], blueprint, projection, region,
    selection["01-a-city-of-names"], selection["03-distributed-study-network-yavneh"])
request = {k: v for k, v in blueprint.items() if k not in ("designProfile", "dossierMetadata")}
errors = validator.audit_dossier(episode,
    {"campaignId": campaign["campaignId"], "editorialContract": campaign["editorialContract"]},
    projection_context={"request": request, "projection": projection})
print("audit errors:", errors)
print("screens:", len(episode["screens"]), "services:", len(episode["fulfillmentServices"]))
print("svg bytes:", len(pipeline.diagram(episode, [])))
PY
```

These commands read only the committed candidate and this unit's canonical sources and
write only into the worker unit's ignored `.cache/yavneh/finalization/`; they do not
depend on any architect worktree remaining alive.

Observed output: `audit errors: []`, `screens: 44 services: 3`, `svg bytes: 14366`
(the renderer returns 14366 characters; the committed UTF-8 file is 14377 bytes because
the Spanish text uses multi-byte characters).

## Focused checks

103 focused checks, **0 failures**, evidence in the worker unit's ignored
`.cache/yavneh/focused-checks.json` (per-check result, recomputed totals and the
24 reproduced financial rows). They establish:

- **Strict schema and real scenario validation.** The candidate envelope is exactly
  `FULFILLMENT_BLUEPRINT_FIELDS` and `dossierMetadata` is exactly
  `FULFILLMENT_METADATA_FIELDS`; the strict v3 profile, both validators, the typed
  request schema, the 32-word caption limit, the screen-key uniqueness, the distinct
  preview/reserve/cancel/commit/final plan IDs and the distinct service goal/completion
  IDs all pass in the real bridge.
- **Factory composition.** `build_fulfillment_dossier` composes the closed intermediate v3
  envelope only; the composed dossier equals the projection view for `worldContract`,
  `objectivePlan`, `stateMachine`, `secondaryObjectives`, `secondaryBudget`,
  `fulfillmentServices`, `selectionAnalysisByDifficulty`, `optionalFinancialInputs`,
  `optionalPrefixAnalysisByDifficulty`, `mapBindings`, `planScreenIds` and `screens`.
- **Audit.** `audit_dossier` returns an empty failure list with the actual
  `projection_context`.
- **44 screens / 88 texts.** 40 source screens preserved in source order with their IDs,
  texts and narrators; the two explicit text overrides (`copy-offer`, `guide-offer`) and
  the four explicit condition overrides (`copy-offer`, `copy-complete`, `copy-hint`,
  `guide-offer`) applied; four appended surfaces (`shared-attendance-goal`,
  `plan-complete`, `copy-north-offer`, `copy-north-complete`) built with the existing
  screen helper, whose regenerated captions and duration estimates reproduce the
  architect's own values byte for byte; every caption segment preserves its full text.
- **7 tasks / 9 optional originals.** Seven secondary objectives, nine finite optional
  originals/objects, and every new original ID matches the supplied
  `campaign.episode.side-n.entity-i` mapping (`aid-cart-1/2`, `record-west-carrier`,
  `record-north-carrier`, `damaged-store`, `trade-carrier`, `guide`, `guest-1/2`), each
  inside its own side namespace.
- **True distinct copy origins, receipts and failures.** `side-2` and `side-3` are two
  separate tasks with one original each, true origins `record-west` and `record-north`
  (never the same hub), exclusive zone IDs that deliberately share the `reader-court`
  offset `[0,8]` radius 3, distinct completion flags and reward flags, and distinct
  failure policies that stay local-only (`no main-goal defeat`, no reward, no
  replacement, no reserve withdrawal).
- **3 services / 6 exclusive methods.** `provisions`, `meeting`, `materials`, two
  methods each, three distinct original workers, three distinct original recipients and
  six distinct selected results. The shared western work site is used by two different
  services without substituting their workers or results.
- **Exact accounts and documented financial totals.** The three difficulty accounts equal
  the pinned specification; the optional reward total is exactly `70F/60W/30G/0S`, the
  optional cost total exactly `20F/30W/20G/0S`, and both equal the declared reserved
  reward account and maximum optional costs; every directly affordable selection still
  funds all seven optionals after immediate funding; trade and guest pay **after** the
  real arrival while repair pays before its reward.
- **Narrative boundary.** The common narrator states that Judith of Tiberias speaks
  centuries later from received accounts; her personal introduction says the names reached
  her through other voices; the northern note attributes the Gittin 56a–b narrative and
  says it is not a contemporary transcript; no screen claims a finalized later Babylonian
  Talmud or a first-person 70 CE witness.
- **Map honesty.** 22 activity hubs and 22 activity points, 28 corridors of which 27 are
  the source physical links with their original endpoints and exactly one is the
  `northern-approach` information alias that reuses the two already proposed links
  `path-timber-work-to-western-junction` and `path-northern-junction-to-timber-work` and
  creates no new road; no water mode, no modern water controls, no fabricated shoreline;
  the 20 documented local approaches remain in the source world as documentary geometry.

## Financial witnesses (source preserved separately)

The source finance witnesses live in
`docs/wiki/jewish-tradition/research/yavneh-allocation-decision.json` (24 cases) and are
**not** smuggled into the strict profile. They were recomputed with the real
`tools/design/finite_allocation.helper.py::optional_states` and `::balance` using the
seven authored cost/reward vectors — no `build_report` preset substitution — and every
case reproduces. Resource vectors are `food/wood/gold/stone`.

| level | recipes | main cost | source direct | source prefix | source all-seven | source funding witness | source all-goals witness | spendable after | reserve after | recomputed direct | recomputed all-seven | recomputed prefix |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| easy | ACE | 160/160/0/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 70,50,220,0 | 0,0,0,0 | True | True | True |
| easy | ACF | 140/130/60/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 90,80,160,0 | 0,0,0,0 | True | True | True |
| easy | ADE | 140/80/70/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 90,130,150,0 | 0,0,0,0 | True | True | True |
| easy | ADF | 120/50/130/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 110,160,90,0 | 0,0,0,0 | True | True | True |
| easy | BCE | 70/140/70/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 160,70,150,0 | 0,0,0,0 | True | True | True |
| easy | BCF | 50/110/130/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 180,100,90,0 | 0,0,0,0 | True | True | True |
| easy | BDE | 50/60/140/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 180,150,80,0 | 0,0,0,0 | True | True | True |
| easy | BDF | 30/30/200/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 200,180,20,0 | 0,0,0,0 | True | True | True |
| standard | ACE | 160/160/0/0 | False | True | None | aid → main | aid → copy → repair → main → trade → guide → guest | 40,0,150,0 | 0,0,0,0 | False | None | True |
| standard | ACF | 140/130/60/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 60,30,90,0 | 0,0,0,0 | True | True | True |
| standard | ADE | 140/80/70/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 60,80,80,0 | 0,0,0,0 | True | True | True |
| standard | ADF | 120/50/130/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 80,110,20,0 | 0,0,0,0 | True | True | True |
| standard | BCE | 70/140/70/0 | False | True | None | aid → main | aid → main → copy → repair → trade → guide → guest | 130,20,80,0 | 0,0,0,0 | False | None | True |
| standard | BCF | 50/110/130/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 150,50,20,0 | 0,0,0,0 | True | True | True |
| standard | BDE | 50/60/140/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 150,100,10,0 | 0,0,0,0 | True | True | True |
| standard | BDF | 30/30/200/0 | False | False | None | — | — | — | — | False | None | False |
| hard | ACE | 160/160/0/0 | False | False | None | — | — | — | — | False | None | False |
| hard | ACF | 140/130/60/0 | False | True | None | aid → main | aid → copy → repair → main → trade → guide → guest | 40,10,90,0 | 0,0,0,0 | False | None | True |
| hard | ADE | 140/80/70/0 | False | True | None | aid → main | aid → main → copy → repair → trade → guide → guest | 40,60,80,0 | 0,0,0,0 | False | None | True |
| hard | ADF | 120/50/130/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 60,90,20,0 | 0,0,0,0 | True | True | True |
| hard | BCE | 70/140/70/0 | False | True | None | aid → main | aid → copy → repair → main → trade → guide → guest | 110,0,80,0 | 0,0,0,0 | False | None | True |
| hard | BCF | 50/110/130/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 130,30,20,0 | 0,0,0,0 | True | True | True |
| hard | BDE | 50/60/140/0 | True | True | True | main | main → aid → copy → repair → trade → guide → guest | 130,80,10,0 | 0,0,0,0 | True | True | True |
| hard | BDF | 30/30/200/0 | False | False | None | — | — | — | — | False | None | False |

The source witnesses predate revision 2 and name a single `copy` optional step; the
revision splits it into `copy-west` and `copy-north`, so the recomputation uses the seven
authored vectors of the revision while the *reachability verdicts* of every case are
unchanged. Totals: **direct affordability 8 / 5 / 3** and **optional-prefix affordability
8 / 7 / 6** (easy/standard/hard), matching the pinned specification exactly.

## Two real schema rejections, and how they were resolved

The typed bridge rejected the profile twice. Both rejections are recorded verbatim below;
neither was worked around by weakening a validator.

1. `02-refuge-and-school-supply-yavneh: invalid schemaVersion 3 referenceCapabilityProfile:
   … "path": ["stateMachine","terminalPriority"] … expected "defeat evaluated first; one
   terminal latch, choice order documented"` and `… "path": ["secondaryBudget","nativeStatus"]
   … expected "design-only; requires certified reusable predicates and native QA"`.
   The strict schema pins those two strings as literals. The architect paraphrases them
   ("defeat evaluated first; one terminal latch" and "reference specification; native QA
   pending"). **Resolution:** the contract literals were used inside the profile; the
   architect's paraphrases are preserved here and in
   `dossierMetadata.failureRecovery.nativeStatus`. No schema, validator or contract was
   changed.
2. `02-refuge-and-school-supply-yavneh: semantic validation failed:
   capability.side-destination(side-5) … (side-6) … (side-7) …: Destino de llegada
   opcional no declarado`. The helper's positional side namespace had not been remapped
   onto the authored side IDs. **Resolution:** the helper's positional IDs were rewritten
   deterministically onto the authored side namespace, so every arrival destination,
   payment receipt, completion flag and reward flag is now scoped by its real side ID.

## Authoring decisions taken inside the closed contract

These are assembly decisions, not new design. Each one stays inside the pinned source.

- **Helper reuse.** `tools/design/secondary.py::build_optional_objectives` was reused for
  the five tasks whose structure matches the source (`side-1` aid, `side-4` repair,
  `side-5` trade, `side-6` guide, `side-7` extract), reusing its common predicate, effect,
  state-contract, receipt and reward structures. The two copy tasks were **not** forced
  through the helper's two-copy preset: `side-2` and `side-3` are authored in the
  complete profile with exactly one original, one receiving zone, `requiredCount` 1 and
  their own origin, receipt and failure.
- **Optional goal text.** Each side objective's `text` is the pinned source offer-screen
  text (with the two spec overrides applied), so the option panel and the optional goal
  cannot drift apart. The helper's generated benefit suffix was dropped for that reason.
- **Repair geometry.** The repair receiving zone is `repair-yard` offset `[0,0]` radius 3
  as the specification requires, and the damaged store keeps its own six-tile offset
  `[6,0]`, so the store is outside its own receiving circle and the initial position
  cannot count as a delivery. The repair-only approach marker stays centred on the yard.
- **Fictional identity fields.** Every strict entity carries `identity`, `finite`,
  `replacement`, `initiallyDelivered`, `originRule` and `historicalPerson: false`; every
  strict zone carries `placement` and `protectedCivilian: false`. Optional identity
  strings reuse the source world plan's own actor classification wording (for example
  "invented ordinary store; native footprint/health action still to bind").
- **World-contract policy strings.** `ledgerPolicy`, `resourcePolicy`, `defeatPolicy` and
  `earlyDelivery` are composed from the source world plan's own `stateAndEvents`
  sentences; no new mechanic was introduced.
- **Distinct copy failures.** The source failure sentence is shared by all six source
  optional tasks, so each copy task states its own original explicitly ("Loss of the
  western original working-record carrier …" / "Loss of the northern original
  working-record carrier …") to satisfy the required independent failure, receipt and
  source.
- **Main contracts unchanged.** Main identities, zones, recipes, service bindings, the
  shared attendance objective, the state machine, the narrator (`judith-copyist`), the
  campaign, the episode title and the continuation to
  `03-distributed-study-network-yavneh` are exactly the architect's pinned values.

## Limits and what is NOT established

- This is a **design candidate**. `gameVerified` is `false`, native status is `pending`,
  and no native run, native export, scenario run or play test was performed or is
  claimed. Nothing here is game or engine evidence.
- No canonical dossier is created. No global or catalogue counter is changed or claimed:
  the candidate adds no dossier, no selection, no screen and no secondary objective to
  the catalogue, and it is **not** dossier 65.
- No canonical geographic profile was inserted. The `yavneh` region was passed explicitly
  as an unregistered candidate with the source documentary citations (IAA Tel Yavne Area A
  figure 1–2 and the New Israel Grid convention); no ancient land, slope, watercourse,
  footprint, native spawn position or passability is certified.
- The SVG is a schematic of the authored candidate geometry produced by the existing
  renderer. It is not a surveyed path, terrain raster or playable map, and the 28th
  corridor is an information alias, not a road.
- The financial totals are reachability under the assumption that every actor and spatial
  predicate succeeds. They are not a difficulty rating, a duration, a challenge balance or
  player evidence.
- Historical, editorial, geographic, native and gameplay acceptance remain pending, as
  does the general combined multi-origin capability of `i00011`. `f00005/S8` remains
  unavailable for historical materialization.
- `bun run validate`, `bun run test:export`, publication and retirement were **not** run
  here: root serializes them after independent review. The heavy repository-wide suites
  were deliberately skipped while another worker held the focused portfolio suite.
- The independent GPT-6.1-Sol review is a technical conformity review of this candidate
  only. This report does not approve S4 and does not approve its own slice.
- No publication is authorized or performed at this point. When publication happens it
  must log to a stable external path supplied by root, because the official publish step
  can remove the worker unit and with it this unit's ignored `.cache/` evidence.

## Resolved confirmations (28 October 2026)

The four questions raised by the first version of this report are resolved by the
architect. These are confirmations of the reviewed design, not new mechanics; the
candidate JSON and the SVG were not changed for them.

1. **Strict literals confirmed.** The two strict-schema literal strings
   (§"Two real schema rejections") stand as the authored wording inside the profile. The
   contract literals are used without any contract, schema or validator change; the
   architect's paraphrases remain recorded here and in
   `dossierMetadata.failureRecovery.nativeStatus`.
2. **Scoped independent copy failure wording confirmed.** The distinct west/north failure
   wording stays as authored for `side-2` and `side-3`; each copy task keeps its own
   original, receipt and failure.
3. **Offer text equals optional goal text confirmed.** Each exact pinned offer text is
   reused as its optional goal text, so the option panel and the optional goal cannot
   drift apart.
4. **Pinned sources are canonical.** The architect's four pinned inputs landed officially
   on `develop` at `44e89db7`; the earlier pending-source state is superseded and the
   four SHA-256 values were re-verified from this unit's own merged `develop`.

No further open question remains for this candidate. What remains outside it is
unchanged: canonical dossier registration, historical, editorial, geographic, native and
gameplay acceptance, the `i00011` general capability and the `S4` gate itself.
