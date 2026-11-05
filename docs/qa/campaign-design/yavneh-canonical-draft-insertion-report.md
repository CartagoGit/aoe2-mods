# Yavneh canonical draft insertion — d00002/S4

Worker `minimax-m3.1-flash-preview` (MiniMax M3.1 Flash, Preview) · 28 October 2026 ·
proposal `d00002` · slice `S4` · assignment
`docs/handoffs/YAVNEH-CANONICAL-DRAFT-PROMOTION-PACKET.md` (architect gpt-6, 28 October 2026).

This report records the promotion of the independently reviewed Yavneh candidate to a
**canonical authored draft**. It asserts no historical approval, no native scenario, no
engine result and no game verification. Section 10 separates auxiliary material, the
canonical draft, and actual game execution.

---

## 1. Session, ref and checkout

| Item | Value |
|---|---|
| Agent identity | `minimax-m3.1-flash-preview` |
| Work ref | `wip/minimax-m3.1-flash-preview/implement/d00002-S4-g1/yavneh-canonical-draft-insertion` |
| Unit checkout | `.cache/delendai/.worktrees/minimax-m3.1-flash-preview-d00002-S4` |
| Generation | `g1`, chosen by the live runtime (no guessed takeover) |
| Integration base | `origin/develop` at `28642f9` |
| File lock | `d00002-S4-yavneh-canonical-draft-insertion`, 8 files, agent `minimax-m3.1-flash-preview` |
| Git author and committer | Cartago `<cartago.relaxingcup@gmail.com>` |

A sibling `d00002-S4` unit (`wip/gpt-6-luna/implement/d00002-S4-g2/yavneh-modern-surface-reference`)
carries a different topic and different files. It was neither read nor modified here, and
nothing from it was cherry-picked.

## 2. Exact change set

Seven files changed, all inside the eight claimed product files. The eighth claimed file is
this report.

| File | +/- |
|---|---|
| `docs/design/odysseys/jewish-tradition.json` | +40418 / -4 |
| `docs/wiki/jewish-tradition/episodes/02-refuge-and-school-supply-yavneh/15-odyssey-dossier.md` | +2930 / -0 (new) |
| `docs/design/maps/jewish-tradition/odyssey/02-refuge-and-school-supply-yavneh.svg` | +107 / -0 (new) |
| `docs/research/odyssey-research/civic-difficulty-mechanical-audit.json` | +742 / -8 |
| `docs/wiki/jewish-tradition/14-odyssey-arc.md` | +5 / -2 |
| `docs/design/assignments.json` | +1 / -1 |
| `docs/design/odyssey-selections.md` | +1 / -1 |

Total: **7 files, +44204 / -16**, plus this report and one test count pin (section 2).

One further file changes, outside the eight claimed product files and recorded explicitly
here: `tools/design/test_pooled_survivor_projection.py`. Its
`test_generated_dossiers_keep_their_counts_and_numeric_audit` pins the authored dossier
count and the screen and secondary-objective totals (64 / 2645 / 398) so that a silent
loss is caught. The promotion makes those pins false, and `bun run validate` failed with
`AssertionError: 65 != 64` at `tools/design/test_pooled_survivor_projection.py:218` until
they were moved to the measured values (65 / 2689 / 405). The file was claimed on the same
file lock before editing. The repository's established practice is to move these pins in
lockstep with the real generated set — the same file was moved when the set last grew —
and leaving them at 64 would make the repository assert a falsehood about its own content.
No test logic, contract, schema or behaviour was changed; only the three pinned numbers.

No adapter, native, engine, schema, string-lock, registry, code or other-campaign file was
touched. The three aggregate diffs are exactly the mechanical consequences of one new
authored dossier:

- `assignments.json` — one `dossierStatus` promoted from `selection and mechanic authored;
  full world/objective/balance/screen/map dossier pending` to `authored full draft;
  independent source/geometry/native/balance gates pending`.
- `odyssey-selections.md` — the `jewish-tradition` row's *Authored expanded drafts* column
  goes from `0` to `1`.
- `14-odyssey-arc.md` — `authoredDossierCount` becomes `1`, the dossier-status line is
  updated, and the authored-dossier link is added.

## 3. The transformation actually performed

The reviewed candidate was **deep-copied** as the sole new `episodeBlueprints` member of
`docs/design/odysseys/jewish-tradition.json`, inserted after `episodeSelection` to match the
canonical key order used by `faith-origins.json` and `imperial-church.json`.

**Exactly one leaf of the copied blueprint was changed:**

```
dossierMetadata.mapPlan.asset:
  "docs/design/episode-plans/jewish-tradition/02-yavneh-blueprint-map.svg"
  → "docs/design/maps/jewish-tradition/odyssey/02-refuge-and-school-supply-yavneh.svg"
```

A leaf-by-leaf diff of the copy against the source candidate reports **zero** other
differing leaves. Every profile, entity, zone, condition, receipt, account, side
payment/reward, screen text and metadata caution is unchanged. The source candidate and its
auxiliary SVG remain byte-identical.

| Artifact | SHA-256 | State |
|---|---|---|
| `02-yavneh-blueprint-candidate.json` | `6a4aebef62b240325407121b5366d5de2277d1a95eaeba1782645ea5411e7690` | unchanged, matches the packet pin |
| `02-yavneh-blueprint-map.svg` | `4696813df3d5a384586386a4c2dab18e23e5719206e138a656751a4d6c26d34d` | unchanged, matches the packet pin |
| `maps/jewish-tradition/odyssey/02-refuge-and-school-supply-yavneh.svg` | `4696813df3d5a384586386a4c2dab18e23e5719206e138a656751a4d6c26d34d` | rendered output, **byte-identical to the preserved auxiliary** |

`episodes[]` was **not** hand-populated, no approval flag was set, no separate renderer was
created, no alternative recipe was flattened to a concurrent payment and no shortcut
projection was used. The canonical generator did all of it.

## 4. Canonical projector, factory and audit results

Commands run inside the unit, in order, with stdout/stderr/exit retained:

| Command | Exit | Result |
|---|---|---|
| `python3 tools/design/episode_dossiers.script.py` | 0 | `65 explicit expanded dossiers checked; no historical/native approval asserted` |
| `python3 tools/design/odyssey_render.script.py` | 0 | `Checked 9 campaigns / 278 selections; expanded dossiers not certified` |
| `python3 tools/design/civic_difficulty_audit.script.py --write --author minimax-m3.1-flash-preview --date 2026-10-28` | 0 | audit written with the real author and client date |
| `python3 tools/design/episode_dossiers.script.py --check` | 0 | 65 dossiers checked, no stale artifact |
| `python3 tools/design/odyssey_render.script.py --check` | 0 | 9 campaigns / 278 selections |
| `python3 tools/design/civic_difficulty_audit.script.py` | 0 | counters reproduced identically |
| `python3 tools/design/verify.py` | 0 | `status: passed`, `errors: []` |

The projector path exercised is the real one: `fulfillment.project_batch` produced the
closed v3 projection, `build_fulfillment_dossier` composed the dossier from it, and
`audit_dossier` returned an empty failure list with the actual `projection_context`. The
candidate's `designProfile` is `alternative-fulfillment-v3`.

`bun run validate` was run inside the unit and passed with **exit 0**: `tsc --noEmit` and
biome clean, `bun test tests` → **161 pass / 0 fail** across 15 files (2153 expect calls),
`docs:check` → *Documentación y enlaces locales válidos*, `campaign:validate` → *3 campaña(s)
comprobadas*. The first run failed only on the three dossier-count pins described in
section 2; after moving them to the measured values the whole gate is green.

This packet changes no adapter or native source, so `test:export` is not newly required for
its own content-only diff.

## 5. Before / after counts

All counts below are read directly from the generated artifacts or from the nine source
campaigns; none is typed into generated data.

| Measure | Before | After |
|---|---:|---:|
| Authored draft dossiers | 64 | **65** |
| Expanded selections | 278 | 278 |
| Selections without a dossier | 214 | **213** |
| Draft screens | 2645 | **2689** |
| Optional drafts (secondary objectives) | 398 | **405** |
| Main objectives | 215 | **216** |
| Static risk candidates | 54 | **54** |
| Dossiers by campaign | faith-origins 30, imperial-church 34 | faith-origins 30, imperial-church 34, **jewish-tradition 1** |
| Baseline historical scenarios | 39 | 39 |
| Base geographic profiles | 26 | 26 |
| Supplemental geographic profiles | 19 | 19 |
| Effective profiles (union, no overlap) | 45 | 45 |
| Registered media assets | 50 | 50 |

The civic report's risk-candidate counters were **recomputed**, not copied: the audit
script re-derives them from the dossier set, and the resulting counters are
`staticRiskCandidates 54` (unchanged, because the new episode introduces no new static
risk candidate), `withFiniteHostiles 8`, `withExplicitStructuredDeadlines 1`,
`sameAccessibleBudgetsAcrossDifficulties 63`, `totalMainObjectives 216`,
`totalSecondaryObjectives 405`, `totalScreens 2689`. The audit's `snapshot.date` is
`2026-10-28` and `snapshot.realIdentity` is `minimax-m3.1-flash-preview`, replacing the
previous snapshot's `gpt-6-luna`.

`yavneh` is a **supplemental** profile only; it is not registered in the base catalogue and
no base profile was added or altered.

## 6. Preservation manifest

The manifest was taken **before** any mutation from `HEAD` and again after generation, over
the complete preserved surface:

| Class | Count |
|---|---:|
| `episodes[]` objects (canonical JSON, sorted keys) | 64 → 65 |
| Authored episode wiki dossiers | 64 → 65 |
| Odysseus SVG maps | 64 → 65 |
| The two other authored source campaign files | 2 |
| Baseline output files of the canonical generators | 21 |
| Baseline historical scenario files | 39 |
| Original Yavneh candidate and auxiliary SVG | 2 |

The diff between the two manifests contains **only** the expected additions:

- one new `episode-object jewish-tradition.json 02-refuge-and-school-supply-yavneh`
- one new `wiki-dossier` and one new `svg-map` (both previously `MISSING`)
- four changed `baseline-output` files: `assignments.json`, `odyssey-selections.md`,
  `civic-difficulty-mechanical-audit.json`, `wiki/jewish-tradition/14-odyssey-arc.md`

Every one of the 64 pre-existing episode objects, the 64 pre-existing wiki dossiers, the 64
pre-existing SVG maps, the two other authored source campaign files, the 39 baseline
historical scenario files, the remaining 17 baseline generator outputs and both auxiliary
Yavneh artifacts are **byte-identical**. No prior output drifted.

The manifest, its generator script and the verification evidence are copied to the shared
root's stable external artifact directory
`.cache/artifacts/d00002-S4-yavneh-minimax-20261028/` before publication, because a
successful publication may remove the worktree.

## 7. Acceptance checks

**43 of 43 checks passed** (`.cache/preservation/verification.json`).

| Claim | Verified result |
|---|---|
| 44 screens | 44 |
| 88 localized texts | 88 |
| 3 services | 3 (`provisions`, `meeting`, `materials`) |
| 6 exclusive methods | 6 (2 per service) |
| 3 distinct original workers / recipients | 3 / 3 |
| 7 distinct optional tasks | 7 (`side-1` … `side-7`) |
| 9 optional original identities | 9, each inside its own side namespace |
| Two independent copy originals | `side-2` starts at `record-west`, `side-3` at `record-north` |
| Same physical receiving location, distinct qualified receipts | both copy tasks receive at `reader-court`, with distinct completion flags |
| Once flags | 7 distinct `…completed` flags |
| Payment before award | repair `30W` → `+20W`; trade `20G` → `+20F/+10G`; hospitality `20F` → `+10F`; aid `+40F/+40W/+20G` |
| 3 difficulty accounts | `easy`, `standard`, `hard` |
| 8/5/3 direct affordable selections | 8 / 5 / 3 |
| 8/7/6 affordable with optional prefixes | 8 / 7 / 6 |
| 24 main financial witnesses | 24 preserved |
| Guide information alias | exactly one `northern-approach` corridor, reusing `path-timber-work-to-western-junction` and `path-northern-junction-to-timber-work`, creating no new road |
| 28 corridors, all `land` | 28, mode set `{land}`; no water mode, no modern water control asserted |
| Candidate and auxiliary byte-identical | confirmed |
| Only the map asset path adapted | confirmed |

### Financial witnesses recomputed with the real solver

The 24 witness verdicts were recomputed with
`tools/design/finite_allocation.helper.py::balance` and `::optional_states` — the canonical
solver, **no new solver was written** — using the seven authored cost/reward vectors that
the generator produced. The source decision's own `analysisMethod` (a BFS over once-only
optional flags plus a once-only main-funding flag, where the main allocation may be funded
at any point in the optional order) was reproduced.

| Level | `initiallyAffordable` | `affordableWithOptionalPrefix` | `allGoalsReachable` |
|---|---:|---:|---:|
| easy | 8 / 8 | 8 / 8 | 8 / 8 |
| standard | 5 / 5 | 7 / 7 | 7 / 7 |
| hard | 3 / 3 | 6 / 6 | 6 / 6 |

Recomputed counts equal the source counts exactly. **0 verdict mismatches** across all 24
cases, and the final spendable and remaining reserve are identical to the source witness in
**21 of 21** cases that carry a witness (the other three are the `None` witness rows).

The seven authored vectors sum to a reward total of `70F/60W/30G/0S`, which equals the
declared reserved reward account, and a cost total of `20F/30W/20G/0S`. These are
finite-account results with spatial assumptions — all actors and physical predicates assumed
to succeed — and **not** a played balance.

### Narrative boundary

The episode is order 2, act 1, `c.70–80 CE`. The common factual introduction precedes
Judith's inherited account; the dramatization notice states that all local workers,
recipients, supplies, records, rooms and errands are invented, that no rabbinic autograph,
exact academy parcel, contemporary negotiation or canon-closing event is represented, and
that Judith's account is framed as centuries later from received accounts. `sourceIds`
carries the single ID the factory derives (`odyssey-source.jewish-tradition.02-refuge-and-school-supply-yavneh`);
no new global source registration was fabricated. `continuation.nextEpisodeId` is
`03-distributed-study-network-yavneh` with `campaignComplete: false`, so the scenario
concludes an intermediate episode and recommends order 3; it does not complete the campaign
and does not gate play on a predecessor save.

## 8. Actual rendered-layer observations

The rendered map is 14 377 bytes, a 400 × 400 north-up frame, `yavneh` terrain profile,
WGS84 bbox `[34.714, 31.846, 34.755, 31.884]`, cosine-corrected longitude.

Element census: 22 `<circle>` activity hubs, 28 `<polyline>` corridors, 53 `<text>` labels
(22 numbered activity sites plus the frame and disclaimer captions), 28 `<title>` corridor
titles, 2 `<rect>`, 1 `<svg>`.

The diagram states, in its own captions:

- "Geographic district controls only"
- "Olive dashed: proposed narrow land connections under 10 tiles"
- "Not a surveyed path or terrain raster"
- "Native footprints and navigation pending"
- "**No ancient shore or elevation inferred**"

A search for `water|river|soreq|stream|wadi` in the rendered SVG returns **0** matches. The
canonical diagram therefore uses only the established geographic-layer inputs and draws no
modern line at all; nothing in it overrides the unresolved hydrology recorded in the map
plan. The `yavneh` profile's `waterControlStatus` remains unresolved and no shoreline,
elevation or water mode was invented.

## 9. Scope of the independent review still required

This slice is **not** marked done. It requires a scoped independent review of:

1. the actual insertion diff (seven files) and whether the transformation stayed within the
   one authorized leaf change;
2. the preservation manifest and the 24-case witness recomputation;
3. the rendered-layer observations above, including the absence of hydrology assertions;
4. whether the narrative boundary and the draft status are honestly stated.

The implementer does not approve its own slice. The previously recorded independent review
of the *candidate* by GPT-6.1-Sol (673 source/candidate checks at `d6321cb`) covers the
candidate, not this promotion.

## 10. What this does and does not establish

**Auxiliary material.** `02-yavneh-blueprint-candidate.json` and
`02-yavneh-blueprint-map.svg` are reviewed *auxiliary* artifacts. They remain byte-identical
and are not the canonical outputs.

**Canonical draft.** `docs/design/odysseys/jewish-tradition.json` now carries one
`episodeBlueprints` member and one `episodes[]` entry; the wiki dossier and the map SVG are
the canonical rendered outputs of the canonical generators. The episode status is
`authored-dossier; source approval, map geometry, native capabilities and game balance
pending`, and the campaign status keeps independent approval pending.

**Actual game execution.** Nothing here was played. There is no native scenario, no engine
result, no export, no build and no game verification for this episode.

### Remaining gates

- **Historical** — the episode's source record, editorial review and the wider
  historical/terrain gates are still pending; the candidate's historical conditions were
  checked, but the promoted draft carries no historical approval.
- **Geographic** — the Yavneh regional profile remains a *candidate*; the padded 400 frame
  extends about 58 m beyond the west edge of the regional bounds and is covered separately
  by the modern DSM reference; hydrology is still unresolved; no elevation or shoreline is
  asserted.
- **Native** — no native footprint, navigation, trigger, variable write, menu or save/load
  behavior is implemented or verified for this episode.
- **Motor / balance** — the 8/5/3 and 8/7/6 figures are finite-account results under
  assumed spatial success, not a played balance; no motor or difficulty calibration was run.

## 11. Reproduction

```sh
python3 tools/design/episode_dossiers.script.py
python3 tools/design/odyssey_render.script.py
python3 tools/design/civic_difficulty_audit.script.py --write --author minimax-m3.1-flash-preview --date 2026-10-28
python3 tools/design/episode_dossiers.script.py --check
python3 tools/design/odyssey_render.script.py --check
python3 tools/design/civic_difficulty_audit.script.py
python3 tools/design/verify.py
```

Evidence scripts used by this slice (kept in the unit's ignored `.cache`, copied to
`.cache/artifacts/d00002-S4-yavneh-minimax-20261028/`):

- `manifest.py` — the before/after preservation manifest.
- `recompute_witnesses.py` — the 24-case recomputation with the canonical solver.
- `verify_s4.py` — the 43 acceptance checks.

This packet changes no adapter or native source, so `test:export` is not newly required for
its own content-only diff.
