# Episode-02 household native builder — historical-build refusal and labelled synthetic fixture

Author minimax-m3.1-flash-preview · 27 October 2026 · i00014/S1. Base
`ed020fd3ed7b70d52f871f6392bc69e8eef59ae9` (develop). The implementer did not
approve this slice.

## What the builder is

`tools/python/build_household_episode.script.py` is the missing build entry
point for episode 02. Until now the only builder,
`tools/python/build_delivery_episode.script.py`, is hard-wired to the episode-01
Caesarea delivery binding, so the implemented and reviewed episode-02 household
ledger controller (product `111d4967`, integrated `5bdd1fa3`) had no way to be
produced at all. The new builder verifies the authored source, refuses a
historical Jerusalem build by naming every open gate, and compiles the household
controller on a separately labelled synthetic physical fixture.

It reuses the existing household adapter, the shared base factory and the
optional-circuit adapter. It adds no new native capability, no composed v2/v3
export, no schema, no public contract, no string identity, no ID range and no
campaign source change. The existing household adapter remains the only
household-ledger controller.

## The historical build is refused, and the real draft is genuinely uncompilable

The real draft is
`docs/wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/19-native-binding-draft.json`
(`sha256 55d1c27acc7e55c5caeb070c016d1d364a3b6b5a5255a6797b3471101863f713`),
whose source is `docs/design/odysseys/faith-origins.json`
(`sha256 0db4c1c70be830847a73d577922e619e8b1c22cd9faf08f2fa5aac44ee5c1d5a`).

Its `map.corridors` is `[]` and its `map.nativeElevation` is `null`. Those two
empties are the physical blockers the architect named, and they are not merely
missing metadata: the guide circuit's `mark-alternative-route` effect needs the
authored `relief` corridor, so the household adapter refuses the real binding
with `optional guide effect needs an authored corridor in the binding`. The
refusal is the correct behaviour of an existing contract, not a new rule.

The builder therefore reports these eight named gates and refuses:

```
historical Jerusalem build refused; missing gates:
  the binding is not approved for a historical build;
  dated-ground route/topographic decision;
  real native building footprint and approach inspection;
  household adapter independent review and serialization;
  engine pathfinding and difficulty playtest;
  no approved topographic/route decision;
  no authored corridor geometry;
  no native elevation assignment
```

The first entry comes from the binding's own
`nativeReadiness.bindingApprovedForHistoricalBuild` being `false`; the next four
are the binding's own `nativeReadiness.blockedBy` list verbatim. The last three
are the builder's own reading of the physical frame: `map.routeApproved` is
`false`, `map.corridors` is empty and `map.nativeElevation` is `null`. The
builder also derives a `no native footprint and approach inspection` gate from
an absent `layoutEvidence`; on this draft `layoutEvidence` is present, so that
gate is carried instead by the binding's own `real native building footprint and
approach inspection` entry, and the two are not duplicated. `refuse_historical_build`
raises on this list, and
`build_preview` additionally refuses to proceed if the list ever becomes empty,
because even an approved binding would still need an explicit architect decision
before a historical build existed. There is no code path in this builder that
can emit a historical Jerusalem campaign, container or mod.

## Source verification fails closed

`load_household_source` verifies the authored source through the binding's own
pins and fails closed on any mismatch instead of continuing with a changed
source. It checks the source `sha256`, the `campaignId`
(`faith-origins`), the `episodeId` (`02-civilian-refuge-jerusalem`) against the
campaign source, and the per-difficulty starting-resource vectors for `easy`,
`standard` and `hard` against the dossier.

## The synthetic fixture and what it drops

`synthetic_physical_binding` derives a physical frame that keeps the authored
semantics and drops the real geometry. It keeps the entity and zone identities,
unit types, player assignments, labels, households, optional payments, the
narration and the per-difficulty starting resources. It drops `layoutEvidence`,
`nativeReadiness`, `sourcePosition`, `sourceOffsetTiles` and `offsetTiles`, and
replaces the real map with a synthetic one whose `routeApproved` is `False`,
whose `nativeElevation` is `None` and which carries a single synthetic `relief`
corridor — the minimum needed to make the guide circuit's authored effect
compilable. The derived binding satisfies the adapter's own
`validate_household_contract`.

Every body is kept outside every circle: the synthetic positions and zone
centres are re-derived on a separate labelled frame and checked for clearance,
so the fixture cannot smuggle the real geography back in. The synthetic frame is
a separate fixture, not a repaired map.

## Commands and measured results

```
COF_PYTHON=.venv/bin/python
$COF_PYTHON tools/python/build_household_episode.script.py \
  docs/wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/19-native-binding-draft.json \
  .cache/scratch/hh-evidence
```

The run exits 0 and produces, per locale (`en`, `es-ES`) and per difficulty
(`easy`, `standard`, `hard`), six variants of
`faith-origins-02-household-synthetic-fixture.aoe2scenario` plus
`native-controller.xs` and `native-receipt.json`, and a top-level
`preview-report.json`.

Measured on the `en`/`easy` variant:

| Field | Value |
| --- | --- |
| scenario | `faith-origins-02-household-synthetic-fixture.aoe2scenario` |
| scenario version | 1.59 |
| triggers | 152 |
| initial units including markers | 17 |
| native original handles | 17 (8 households + 9 side-circuit entities) |
| `nativeSignature` round-trip | equal before and after write/read |
| XS validation | `raise_on_error = True`, `validate_scenario_xs()` passes |
| `scenarioSha256` | `e0e0f76e67fa5122df723671ab396ee00236f96581165196bd513b6f1dc6a306` |

The receipt records `syntheticFixture true`, `syntheticScenarioId
faith-origins-02-household-synthetic-fixture`, the nonhistorical
`syntheticNotice`, `historicalApproval false`, `generalComposedExportEnabled
false`, `gameVerified false` and a status that states the artifact is a
synthetic household controller fixture, not a historical build, not a campaign
release and not game verified. `preview-report.json` additionally records
`historicalBuild { attempted: false, refused: true, blockers: [...8 gates...] }`
and the five pending gates:

- an approved topographic and route decision for the real frame;
- real native building footprint and approach inspection;
- engine pathfinding, save/load and terminal arbitration evidence;
- difficulty and reward utility calibration;
- certified campaign UI/SequenceItems and release localization IDs.

The nonhistorical label is carried in three places and was verified on the
written-and-reopened artifact: the scenario identity (the artifact's own
`name` is `faith-origins-02-household-synthetic-fixture`), the messages (the
instructions begin with the nonhistorical notice, followed by the title and the
authored goals) and the receipt.

## Evidence tests

`tests/fixtures/native-history/test_native_household_controller.py` gains nine
tests in `HouseholdBuilderTests`, covering: the source pins are verified and
fail closed; the historical-build blockers name every open gate; the real draft
is not compilable because its corridor is missing; the builder refuses a
historical build with the named gates; the synthetic binding keeps the authored
semantics; the synthetic frame drops the real geometry; the synthetic frame
keeps every body outside every circle; the synthetic binding satisfies the
adapter contract; and the builder compiles the labelled synthetic fixture.

The file now runs 35 tests (26 pre-existing plus 9 new) and passes. The other
native fixture files are unaffected: delivery controller, resource transactions,
scenario factory and spatial predicates all still pass.

```
$COF_PYTHON tests/fixtures/native-history/test_native_household_controller.py
Ran 35 tests in 7.472s
OK
```

## Explicit non-claims

- This is not a historical Jerusalem build, campaign container, mod or release.
  No such artifact exists and the builder cannot emit one.
- The fixture is not game-verified. `gameVerified` is `false`; there is no
  engine, pathfinding, save/load or terminal-arbitration evidence, and the XS
  validation that did run is a static script check, not a playthrough.
- No geography, route, terrain, elevation or footprint decision is made. The
  unresolved route and the native elevation stay visible as blockers.
- No approval of i00003/S3 or of d00002 is claimed or implied by this slice.
- No historical, balance, localisation or engine claim is made for episode 02.
