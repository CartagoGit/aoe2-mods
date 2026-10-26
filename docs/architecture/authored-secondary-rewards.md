# Authored optional resource rewards

Architect: gpt-6 · 25 October 2026 · i00009/S1. Decision status: proposed, independent approval pending. This is a narrow design-source projection change, not a new gameplay operation or an amendment to a public scenario/capability schema. Implementation belongs to S2 after S1 is formally accepted. No historical source is edited by this proposal.

## Observed limitation

`tools/design/secondary.py::build_optional_objectives` chooses `REWARDS[kind]`. `tools/design/episode_dossier.factory.py::build_dossier` separately sums those same global defaults for reward stock, even though the generated existing effects already contain the actual resource vectors. An architect cannot currently author a different or zero resource bonus through that path. The current generic builder does not inspect the proposed `resourceReward` field; including it today is not a supported operation.

Root executed the following against the integrated source carried by `e1f5636249c4e115a4a9841593b61da0d4e85b5e`. Everything in the fixture is artificial:

```sh
python3 - <<'PY'
import json, runpy
api = runpy.run_path('tools/design/secondary.py')
pair = lambda text: {'en': text, 'es-ES': text}
scenario = {'id': 'artificial-reference', 'mapPlan': {
    'hubs': [{'id': f'hub-{n}'} for n in range(1, 4)]}}
task = {
    'kind': 'extract', 'title': pair('Artificial optional extraction'),
    'subject': pair('artificial household groups'),
    'rationale': pair('Artificial fixture, no historical claim'),
    'resourceReward': {},
}
result = api['build_optional_objectives'](scenario, [task])[0]
print(json.dumps({'requested': task['resourceReward'],
                  'actual': result['effects'][0]['resources']}))
PY
```

Observed before implementation: `{"requested": {}, "actual": {"food": 100, "gold": 25}}`. The goal text also promises that default bonus. Expected after accepted S2: the effect has an empty resource vector and the goal text promises no resource bonus. This is a missing authoring projection, not evidence of a native reward bug or an attempt to change historical content using an ignored key.

## Closed decision

Introduce exactly one optional internal source field, `optionalTasks[].resourceReward`, in the existing expanded legacy dossier builder. It is permitted only for `aid`, `extract`, `repair` and `trade`, whose existing effect is `finite-supply-withdrawal`. Omission retains the current default vector and exact current output. Explicit `{}` means no extra resources. A vector containing only zeros also means no extra resources. Positive entries specify a finite bonus; they do not fund themselves, cause the main result or imply a new use for the resources.

Use `tools/design/design_numbers.helper.py::resource_amounts` to validate the field. Only `food`, `wood`, `gold` and `stone`, with nonnegative Python integer values, are accepted. Reject Boolean, float, string, negative, null, array and unknown-resource inputs rather than coercing or falling back. Normalize an explicit override to resource order with zero entries omitted; do not normalize an omitted field in a way that changes legacy output. The source object and global default dictionaries must remain unmodified.

An override on `copy`, `guide`, `watch` or `scout` is rejected, including an empty override. Their existing information effect is not an implicitly working resource transfer. This proposal changes neither information targets nor their real authored references. It also introduces no optional payment override: repair remains the existing 50-wood restoration operation; trade retains its existing 50-gold payment and arrival rule. A zero reward does not remove a repair/trade cost, alter its predicate, or grant a reward before that predicate completes.

For a positive override, the existing bilingual goal renderer names exactly the effective amounts once. For a zero override on an allowed resource kind, append these explicit lines instead of falling through the information-kind suffix table:

- EN: “No resource bonus. Completing this task achieves the optional local outcome described above.”
- es-ES: «Sin bonificación de recursos. Al completar esta tarea se consigue el resultado local opcional indicado arriba».

The task's actual goal/instruction still explains the local outcome. The implementer does not invent a benefit, narrator line, healing, recruitment, passability change or historical claim to compensate for a zero monetary bonus. Existing informational tasks keep their exact captions. The existing completed-task flag/presentation may represent the declared optional outcome; that is not a new game operation.

## One effective contract, one account calculation

The existing objective builder remains the owner of IDs, original participants, predicates, atomic payment, once-only effect and optional failure/terminal semantics. Forward `resourceReward` only when actually present in the author input; use the shared numeric primitive at the builder boundary. Do not duplicate the builder or introduce a second source schema/secondary DSL.

After building `secondaryObjectives`, derive `reservedRewards` by summing the resource vectors of their actual effects, and `maxOptionalCosts` by summing the resources of their actual `atomic-payment` requirements. Feed these effective totals into the unchanged difficulty/account construction and optional budget validation. Do not sum the `REWARDS`/`COSTS` lookup tables a second time. The validator already independently compares actual contracts with the declared budget and checks isolated reward stock, all-skip main solvency, surplus and cache allowance; keep those checks.

Changing an authored reward does not relax a funding limit. A valid resource vector may still produce an invalid dossier if it exceeds the authored envelope/cache allowance or another existing invariant. That failure must remain a diagnostic. No reward comes from protected recovery, no payment uses its own unearned reward, and optional failure/terminal closure cannot credit a bonus. Existing reference transactions own persistence and once-only semantics; S2 does not reimplement them or claim that the native adapter supports them.

## Compatibility and acceptance

S2 uses artificial fixtures only. With no new field in the current historical sources, all 64 dossiers, 2,645 screens, 398 secondaries, 49 registered reference records and their existing generated outputs must remain identical. All public schemas, v1/v2/v3 discriminators, scenario identities, string IDs, main predicates, fixed optional costs and native rejection behavior remain unchanged. The v3 projection already consumes authored effects; this proposal must not create a different v3 reward path or rewrite its complete source.

Independent review must compare omission/default, positive and explicit zero cases, reject malformed/misplaced overrides, check mixed effective totals through the real legacy factory/validator, and show that optional money never becomes a hidden main prerequisite. Review also checks all-skip and pre-reward affordability in the existing accounting representation. These are static/reference checks, not played tactics. Historical designers still owe every reward a useful or honestly intrinsic local outcome, geography, source qualifications and an individually approved mechanical packet.

The [closed implementation packet](../handoffs/AUTHORED-SECONDARY-REWARDS-PACKET.md) fixes files, tests and escalation. Jerusalem70 remains partial in d00002/S4. S1 approval alone implements no projection and unlocks no historical authoring.
