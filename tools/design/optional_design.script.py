"""Materialise the architect's explicit optional recipes into the baseline catalogue.

This preserves native campaign files and IDs. --check audits deterministic derived fields.
"""
import argparse
import json
from pathlib import Path
from secondary import RESOURCES, build_optional_objectives

ROOT = Path(__file__).resolve().parents[2]

REACTIONS = {
 'faith-origins': ('A name, a road, a household: these were the margins I learned to read.', 'Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer.'),
 'imperial-church': ('The official register seldom recorded who made the journey bearable.', 'El registro oficial rara vez anotaba quién hacía soportable el viaje.'),
 'jewish-tradition': ('A spare copy is less impressive than a monument. It can last longer.', 'Una copia de reserva impresiona menos que un monumento. Puede durar más.'),
 'church-of-rome': ('Sing of the road, and leave a verse for the hands that kept it open.', 'Canta al camino, y deja un verso para las manos que lo mantuvieron abierto.'),
 'new-rome': ('A city holds together piece by piece. I know that work.', 'Una ciudad se sostiene pieza a pieza. Conozco ese oficio.'),
 'first-caliphs': ('A caravan ledger starts with goods; the road teaches you to count people.', 'Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas.'),
 'first-fitna': ('The next wound could wait. Someone had made a little room for care.', 'La siguiente herida podía esperar. Alguien había dejado un poco de sitio para los cuidados.'),
 'umayyads': ('Ask what a road carries before you ask who owns it.', 'Pregunta qué lleva un camino antes de preguntar quién lo posee.'),
 'house-of-ali': ('I would remember the small acts as well. They left marks no seal could make.', 'También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer.'),
}


def enrich(campaign, scenario, recipe):
    objectives = build_optional_objectives(scenario, recipe)
    reward = {k: sum(e['resources'].get(k, 0) for o in objectives for e in o['effects']) for k in RESOURCES}
    cost = {k: sum(r.get('resources', {}).get(k, 0) for o in objectives for r in o['predicate']['requirements']) for k in RESOURCES}
    budget = {'reservedRewards': reward, 'maxOptionalCosts': cost,
              'reallocatedCacheAllowance': {'food': 600, 'wood': 300, 'gold': 150, 'stone': 0},
              'fundingPolicy': 'replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped',
              'nativeStatus': 'design-only; requires certified reusable predicates and native QA'}
    by_kind = {o['kind']: o['id'] for o in objectives}
    preferences = [
        ('careful-supply', ['repair', 'trade', 'aid', 'extract']),
        ('informed-movement', ['guide', 'scout', 'watch', 'copy']),
        ('civilian-and-memory', ['extract', 'aid', 'copy', 'guide']),
    ]
    styles = []
    for sid, kinds in preferences:
        selected = [by_kind[k] for k in kinds if k in by_kind][:3]
        for o in objectives:
            if len(selected) >= 2:
                break
            if o['id'] not in selected:
                selected.append(o['id'])
        styles.append({'id': sid, 'optionalObjectives': selected,
                       'mainObjectivesUnchanged': True, 'historicalOutcomeUnchanged': True,
                       'tradeoff': 'optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution'})
    return objectives, budget, styles


def apply(root=ROOT, check=False):
    path = root / 'docs/design/catalog.json'
    data = json.loads(path.read_text())
    for campaign in data['campaigns']:
        recipes = json.loads((root / 'docs/design/odysseys' / f'{campaign["id"]}.json').read_text())['baselineOptionalRecipes']
        for scenario in campaign['scenarios']:
            if scenario['id'] not in recipes:
                continue  # long-odyssey episodes have their own authored recipes, never guess them
            objectives, budget, styles = enrich(campaign, scenario, recipes[scenario['id']])
            fields = {'secondaryObjectives': objectives, 'secondaryBudget': budget, 'playstyles': styles}
            if check:
                for name, value in fields.items():
                    if scenario.get(name) != value:
                        raise ValueError(f'Stale optional contract: {campaign["id"]}/{scenario["id"]}/{name}')
                continue
            scenario.update(fields)
            scenario['mapPlan']['explorationPlan'] = {
                'classification': 'optional fictional tasks within dated geographic districts; not surveyed ancient locations',
                'sectors': [],
                'secondaryObjectiveIds': [o['id'] for o in objectives],
                'connectingTrails': 'use main/relief corridors to the task districts; optional travel must not create an extra mandatory crossing',
                'qualityGate': 'certify each task path, safe delivery zone and footprint at all difficulties; geography remains authoritative',
            }
            for level, b in scenario['difficulty'].items():
                b['accessibleWithoutOptionalRewards'] = {k: b['startingResources'][k] + b['gatherableBank'][k] - budget['reservedRewards'][k] for k in RESOURCES}
            scenario['screens'] = [x for x in scenario['screens'] if not x['id'].startswith('optional-') and not x['id'].startswith('side-')]
            for o in objectives:
                for suffix, condition, text in [
                    ('brief', 'optional objectives tab, always available', o['text']),
                    ('completed', f'{o["completionFlag"]} latched; once', {loc: ('Optional task completed: ' if loc == 'en' else 'Tarea opcional completada: ') + o['title'][loc] + '. ' + REACTIONS[campaign['id']][i] for i, loc in enumerate(('en','es-ES'))}),
                    ('unavailable', 'unique optional entity irrecoverably lost; once', {'en': 'This optional task is no longer available. The main objectives remain active.', 'es-ES': 'Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos.'}),
                ]:
                    segments = {loc: [' '.join(value.split()[j:j+32]) for j in range(0, len(value.split()), 32)] for loc, value in text.items()}
                    scenario['screens'].append({'id': f'{o["id"]}-{suffix}', 'key': f'scenario.{campaign["id"]}.{scenario["id"]}.{o["id"]}-{suffix}',
                                               'text': text, 'narrator': campaign['narrator']['id'], 'condition': condition,
                                               'destination': 'return-to-game', 'skippable': True,
                                               'referenceAsset': None, 'captionSegments': segments})
    if not check:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    apply(check=parser.parse_args().check)
