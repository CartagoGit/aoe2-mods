# Pooled original survivors in the design source

Architect: gpt-6 · 25 October 2026 · i00010/S1. Proposed design-source projection; independent review pending. Public `survivorGroupSchema` already represents an explicit array of existing entities and a positive minimum. `capability-predicates.validator.ts` already evaluates the distinct surviving originals across that array. No new survival mechanic or public schema is proposed.

## Real limitation and reproduction

The current `tools/design/episode_dossier.factory.py::world_and_objectives` projects each authored survivor row using `groups[row['group']]`. Its output cannot express a single union of four existing two-person origin groups. Omitting the pool loses impossible-threshold defeat; four per-court thresholds impose a different rule; moving all originals to one origin changes the map problem. None is an acceptable substitute.

Root executed this artificial fixture against the existing factory and observed `KeyError('group')`. It is a missing internal projection, not an accepted key today:

```sh
python3 - <<'PY'
import runpy, sys
sys.path.insert(0, 'tools/design')
api = runpy.run_path('tools/design/episode_dossier.factory.py')
keys = ['west', 'east', 'south', 'central']
authored = {
    'objectGroups': [
        {'key': key, 'count': 2, 'role': 'artificial originals',
         'originHub': f'hub-{i}',
         'historicalMaterialPolicy': 'Artificial reference, not history'}
        for i, key in enumerate(keys, 1)],
    'mainObjectives': [],
    'survivorGroups': [{'groups': keys, 'minimumAliveOrAlreadySafe': 6}],
}
world, _ = api['world_and_objectives'](
    'artificial', {'id': 'pooled-originals'}, authored,
    [{'id': f'hub-{i}'} for i in range(1, 5)])
print(world['survivorGroups'])
PY
```

After accepted S2, the single survivor row must contain exactly the eight already generated original IDs and minimum 6. The four origin hubs, every entity object and its initial offsets stay unchanged. There is no extra party entity or engine alias.

## Fixed authoring decision

An authored survivor row selects exactly one of `group` (the existing nonempty string) or `groups` (a nonempty array of distinct nonempty strings), alongside `minimumAliveOrAlreadySafe`. Every selected name must exist in the existing generated main-object-group dictionary and resolve to at least one original. Reject both selectors, neither, null, wrong types, empty names/lists, duplicate names, unknown names and a pool that repeats any entity ID. Do not silently deduplicate malformed input or create an alias.

Flatten the selected existing groups in the authored order; preserve each group's existing generated order. A valid single-group row produces the exact old output. `minimumAliveOrAlreadySafe` must satisfy the existing shared positive-integer primitive and be at most the number of distinct pooled IDs; reject Boolean, float (including integral float), string, zero, negative and oversized minima. Do not coerce or clamp. Reuse `design_numbers.helper.py` primitives instead of a second numeric policy.

Output remains precisely the current dossier survivor-row shape: `entities` and `minimumAliveOrAlreadySafe`. It feeds the unchanged validator and public v2 representation. No source `groups` selector reaches a runtime schema, no identity is generated twice, and no actor is moved. Main requirements can continue naming their already generated explicit entity sets using existing fields; this proposal does not add a second selector language to every predicate.

The reference must still tolerate any two losses from eight, regardless of their starting court, and defeat on the third before a possible simultaneous victory. Arrival receipts do not certify final living presence. Existing `current-entity-presence` remains required where authored. A separate pool for three required original bearers can keep its own minimum of three; an optional person cannot enter either pool as a replacement.

## Sequencing and boundaries

S2 depends on independently accepted S1 and the integrated, independently accepted i00009/S2 because the two mechanical changes share the factory and design test runner. One implementer/claim at a time for those files. Do not copy an unreviewed reward implementation or broaden that earlier slice to include survival.

Current sources all use the original single-group row. All 64 dossiers, 2,645 screens, 398 secondaries, 49 research records and their generated outputs must stay unchanged after implementation. No historic source, public schema, IDs, native adapter, game statistics or campaign identity changes. No historical dossier is created to test the feature. The [mechanical packet](../handoffs/POOLED-SURVIVOR-PROJECTION-PACKET.md) fixes the implementation and evidence. Jerusalem remains partial in d00002/S4; native observers, terminal batching, pathfinding and game QA retain their existing proposals.
