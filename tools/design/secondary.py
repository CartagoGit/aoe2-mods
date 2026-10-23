"""Build and audit authored optional objectives; these are design contracts, not native triggers."""
import math

RESOURCES = ('food', 'wood', 'gold', 'stone')
REWARDS = {
    'scout': {}, 'aid': {'food': 100, 'wood': 50}, 'copy': {},
    'repair': {'food': 200, 'wood': 100},
    'trade': {'food': 150, 'wood': 50}, 'guide': {},
    'extract': {'food': 100, 'gold': 25}, 'watch': {},
}
COSTS = {'repair': {'wood': 50}, 'trade': {'gold': 50}}
EFFECTS = {
    'scout': ('reveal-enemy-approach', 'wave-2 approach'),
    'aid': ('finite-supply-withdrawal', 'optional supply stock'),
    'copy': ('unlock-context-and-hint', 'documented context and a main-goal hint'),
    'repair': ('finite-supply-withdrawal', 'optional supply stock'),
    'trade': ('finite-supply-withdrawal', 'optional supply stock'),
    'guide': ('mark-alternative-route', 'relief corridor'),
    'extract': ('finite-supply-withdrawal', 'optional supply stock'),
    'watch': ('reveal-enemy-approach', 'wave-1 and wave-3 approaches'),
}


def bilingual(en, es):
    return {'en': en, 'es-ES': es}


def objective_text(kind, subject, reward, information_benefit=None, instruction=None):
    name_en, name_es = subject['en'], subject['es-ES']
    texts = {
        'scout': (f'Scout both marked viewpoints of {name_en}.', f'Explora los dos miradores señalados de {name_es}.'),
        'aid': (f'Bring each of the two aid crates to its assigned household at {name_en}.', f'Lleva cada una de las dos cajas de ayuda a su hogar asignado en {name_es}.'),
        'copy': (f'Recover both separate copies from {name_en} and deliver them to the copyist.', f'Recupera las dos copias distintas de {name_es} y entrégalas al copista.'),
        'repair': (f'Pay 50 wood and restore the damaged store of {name_en} to full health.', f'Paga 50 de madera y repara por completo el almacén dañado de {name_es}.'),
        'trade': (f'Escort the trader of {name_en} to the receiving post, then pay 50 gold for one consignment.', f'Escolta al comerciante de {name_es} hasta el puesto receptor y paga 50 de oro por una sola remesa.'),
        'guide': (f'Escort the local guide of {name_en} to the marked road junction.', f'Escolta al guía local de {name_es} hasta el cruce señalado.'),
        'extract': (f'Bring both voluntary evacuee groups from {name_en} to the receiving refuge alive.', f'Lleva con vida los dos grupos de evacuados voluntarios de {name_es} al refugio receptor.'),
        'watch': (f'Visit both observation posts overlooking {name_en}.', f'Visita los dos puestos de observación sobre {name_es}.'),
    }
    if instruction is not None:
        if (not isinstance(instruction, dict) or set(instruction) != {'en', 'es-ES'}
                or not all(isinstance(value, str) and value.strip()
                           for value in instruction.values())):
            raise ValueError('Optional instruction needs nonempty English and Spanish text')
        en, es = instruction['en'], instruction['es-ES']
    else:
        en, es = texts[kind]
    if reward:
        nouns_en = {'food': 'food', 'wood': 'wood', 'gold': 'gold', 'stone': 'stone'}
        nouns_es = {'food': 'alimento', 'wood': 'madera', 'gold': 'oro', 'stone': 'piedra'}
        en += ' Benefit: ' + ', '.join(f'{v} {nouns_en[k]}' for k, v in reward.items()) + ', once.'
        es += ' Ventaja: ' + ', '.join(f'{v} de {nouns_es[k]}' for k, v in reward.items()) + ', una vez.'
    elif information_benefit is not None:
        en += ' Benefit: ' + information_benefit['en']
        es += ' Ventaja: ' + information_benefit['es-ES']
    else:
        suffix = {
            'scout': ('Benefit: reveal the second reserve approach.', 'Ventaja: revela la aproximación de la segunda reserva.'),
            'copy': ('Benefit: unlock a historical note and an explicit main-goal hint.', 'Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.'),
            'guide': ('Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.', 'Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.'),
            'watch': ('Benefit: reveal the first and last reserve approaches.', 'Ventaja: revela las aproximaciones de la primera y la última reserva.'),
        }[kind]
        en += ' ' + suffix[0]; es += ' ' + suffix[1]
    return bilingual(en, es)


def build_optional_objectives(scenario, authored):
    """Authors choose every task/context; only IDs, ledgers, captions and bounded math are shared."""
    result = []
    known_hubs = {hub['id'] for hub in scenario['mapPlan']['hubs']}
    for number, item in enumerate(authored, 1):
        kind = item['kind']
        oid = f'side-{number}'
        ns = f'{scenario["id"]}.{oid}'
        origin = 'hub-2' if kind == 'repair' else 'hub-1' if kind in ('aid', 'guide', 'trade') else 'hub-3'
        destination = 'hub-1' if kind in ('extract', 'copy') else ('hub-3' if kind == 'guide' else 'hub-2')
        placement = item.get('placement', {})
        if (not isinstance(placement, dict)
                or set(placement) - {'originHub', 'receivingHub', 'observationHubs', 'entityOffsetsTiles'}):
            raise ValueError('Unknown optional placement fields; use explicit hubs and entityOffsetsTiles')
        for field in ('originHub', 'receivingHub'):
            if field in placement and (not isinstance(placement[field], str)
                                       or placement[field] not in known_hubs):
                raise ValueError(f'Optional {field} must name an existing hub')
        origin = placement.get('originHub', origin)
        destination = placement.get('receivingHub', destination)
        entity_count = 2 if kind in ('aid', 'copy', 'extract') else 1
        entities = [] if kind in ('scout', 'watch') else [
            {'id': f'{ns}.entity-{i}', 'role': kind, 'initialHub': origin,
             'offsetTiles': [-6, i * 3], 'finite': True, 'initiallyDelivered': False,
             'historicalPerson': False, 'playerControllable': kind != 'repair'}
            for i in range(1, entity_count + 1)
        ]
        if kind == 'repair':
            entities[0].update(initialHub=origin, initialHealthFraction=0.5, damageSource='fictional prior damage')
        if 'entityOffsetsTiles' in placement:
            offsets = placement['entityOffsetsTiles']
            if (not isinstance(offsets, list) or len(offsets) != len(entities)
                    or any(not isinstance(point, list) or len(point) != 2
                           or any(not isinstance(value, (int, float)) or isinstance(value, bool)
                                  or not math.isfinite(value) for value in point)
                           for point in offsets)):
                raise ValueError('Optional entityOffsetsTiles needs one finite coordinate pair per identity')
            for entity, point in zip(entities, offsets):
                entity['offsetTiles'] = list(point)
        zones = [
            {'id': f'{ns}.zone-{i}', 'hub': ('hub-2' if i == 1 else 'hub-3') if kind == 'watch' else ('hub-1' if i == 1 else 'hub-3') if kind == 'scout' else destination, 'offsetTiles': [0, -8 if i == 1 else 8] if kind == 'watch' else [-8 if i == 1 and kind in ('aid', 'scout') else 8, 0], 'radiusTiles': 3}
            for i in range(1, 3 if kind in ('aid', 'scout', 'watch') else 2)
        ]
        if 'observationHubs' in placement:
            points = placement['observationHubs']
            if (kind not in ('scout', 'watch') or not isinstance(points, list)
                    or len(points) != len(zones)
                    or any(not isinstance(hub, str) or hub not in known_hubs for hub in points)):
                raise ValueError('Observation placement needs one hub per scout/watch zone')
            for zone, hub in zip(zones, points):
                zone['hub'] = hub
        requirements = []
        if kind in ('scout', 'watch'):
            requirements.append({'kind': 'visit-zones', 'zones': [z['id'] for z in zones],
                                 'actor': 'any-player-controlled-unit', 'requiredCount': 2,
                                 'observationsPersistent': True, 'countInitialVisibility': False})
        elif kind == 'repair':
            requirements.append({'kind': 'entity-health', 'entity': entities[0]['id'],
                                 'health': 'full', 'paymentReceipt': f'{ns}.payment',
                                 'restoration': 'atomic 50-wood repair transaction restores full health; no additional engine repair charge'})
        else:
            destinations = {e['id']: zones[i % len(zones)]['id'] for i, e in enumerate(entities)}
            requirements.append({'kind': 'entity-arrival', 'entities': [e['id'] for e in entities],
                                 'destinations': destinations, 'requiredCount': entity_count,
                                 'aliveAtDelivery': True, 'oncePerEntity': True,
                                 'noSubstitutes': True, 'initialPlacementDoesNotCount': True})
        cost = COSTS.get(kind, {})
        if cost:
            requirements.append({'kind': 'atomic-payment', 'resources': cost,
                                 'receipt': f'{ns}.payment', 'afterArrival': kind == 'trade',
                                 'once': True, 'protectedRecoveryCannotBeSpent': True})
        effect_kind, target = EFFECTS[kind]
        effect = {'kind': effect_kind, 'target': target, 'resources': REWARDS[kind],
                  'onceFlag': f'{ns}.rewarded', 'funding': 'reserved-optional-stock',
                  'changesHistoricalOutcome': False}
        if kind == 'copy':
            effect['sourceIds'] = scenario['sourceIds']
            effect['historicalNote'] = scenario['historicalBrief']
            effect['hint'] = scenario['goals'][0]
        if kind in ('scout', 'watch'):
            effect['rosterIds'] = ['wave-2'] if kind == 'scout' else ['wave-1', 'wave-3']
            effect['alreadyReleasedPolicy'] = 'reveal current surviving members, never spawn a replacement'
        if kind == 'guide':
            effect['corridorId'] = 'relief'
        information = item.get('information')
        if information is not None:
            if kind not in ('scout', 'watch', 'guide'):
                raise ValueError('Only information tasks may override an information effect')
            for field in ('rosterIds', 'alreadyReleasedPolicy', 'corridorId'):
                effect.pop(field, None)
            effect.update(information['effect'])
        text = objective_text(kind, item['subject'], REWARDS[kind],
                              information['benefit'] if information else None,
                              item.get('instruction'))
        result.append({
            'id': oid, 'kind': kind, 'title': item['title'], 'subject': item['subject'],
            'classification': 'fictional local activity anchored to the documented scenario; not an asserted ancient event',
            'rationale': item['rationale'], 'text': text, 'mandatory': False,
            'activation': 'available from scenario start; known requirement and benefit shown in optional goals',
            'dependencies': [], 'predicate': {'operator': 'all', 'requirements': requirements,
                                           'neverUseTimerInstead': True},
            'world': {'entities': entities, 'zones': zones}, 'effects': [effect],
            'completionFlag': f'{ns}.completed',
            'stateContract': {'states': ['available', 'completed', 'failed-optional', 'closed-at-terminal'],
                              'requiresNonterminalScenario': True, 'persistentAcrossSave': True,
                              'completionAndEffectsAtomic': True, 'paymentBeforeReward': True,
                              'paymentIsNotCompletion': True, 'failedGoalCannotReward': True,
                              'latchAtFirstCompletion': True, 'noMainVictoryDependency': True,
                              'rewardTransaction': ['verify all predicate ledgers and nonterminal state', 'verify reserved stock', 'debit reserved stock', 'credit spendable stock', 'set reward onceFlag', 'set completionFlag'],
                              'transactionIsolation': 'all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing',
                              'persistentLedgers': ['visited-zone IDs', 'delivered-entity IDs', 'payment receipt', 'reserved-stock remainder', 'reward onceFlag', 'completionFlag', 'failed-optional flag'],
                              'terminalPriority': 'main defeat/victory closes side actions first; never credit after terminal'},
            'unavailablePolicy': 'show failed-optional if its unique entity is lost; no main-goal defeat or restart',
            'terminalPolicy': 'optional goals close at main victory/defeat; never delay campaign progression',
            'difficultyPolicy': 'same identities, counts and cost in all profiles; no hidden time limit',
            'reachability': {'originHub': origin, 'receivingHub': destination,
                             'corridorIds': ['main', 'relief'],
                             'maxRequiredRoundTrips': 1, 'spawnOutsideReceivingZone': True,
                             'placementGate': 'certify land/transport path and footprints in native map; relocate within same historical district, never alter river'},
            'qa': ['skip-all-main-still-solvent', 'complete-in-each-difficulty',
                   'save-before-and-after-reward', 'repeat-arrival-no-double-reward',
                   'entity-loss-optional-only', 'early-main-victory-does-not-wait',
                   'no-reward-taken-from-protected-recovery'],
        })
        if 'corridorIds' in item:
            result[-1]['reachability']['corridorIds'] = list(item['corridorIds'])
    return result


def check_optional_objectives(scenario, check, label):
    objectives = scenario.get('secondaryObjectives', [])
    check(6 <= len(objectives) <= 8, f'{label}: require 6–8 authored secondary objectives')
    check(len({o['kind'] for o in objectives}) >= 4, f'{label}: insufficient optional mechanic variety')
    check(len({o['id'] for o in objectives}) == len(objectives), f'{label}: duplicate optional ID')
    check(len({o['title']['en'] for o in objectives}) == len(objectives), f'{label}: repeated optional title')
    rewards = {k: 0 for k in RESOURCES}
    costs = {k: 0 for k in RESOURCES}
    all_entity_ids = {e['id'] for e in scenario['worldContract']['entities']}
    seen_flags = set()
    for o in objectives:
        context = f'{label}/{o["id"]}'
        check(o['kind'] in REWARDS and o['mandatory'] is False, f'{context}: unsupported or mandatory side goal')
        check(o['predicate']['operator'] == 'all' and o['predicate']['neverUseTimerInstead'], f'{context}: incomplete optional predicate')
        check(not o['dependencies'], f'{context}: unreviewed optional dependency')
        for field in ('title', 'subject', 'text'):
            check(set(o[field]) == {'en', 'es-ES'} and all(o[field].values()), f'{context}: missing bilingual {field}')
        entities = {e['id']: e for e in o['world']['entities']}
        zones = {z['id']: z for z in o['world']['zones']}
        check(len(entities) == len(o['world']['entities']) and len(zones) == len(o['world']['zones']), f'{context}: duplicate optional world ID')
        check(not all_entity_ids.intersection(entities), f'{context}: optional reuses mandatory or another side entity')
        all_entity_ids.update(entities)
        for z in zones.values():
            check(math.hypot(*z['offsetTiles']) <= 12, f'{context}: optional zone outside district')
        hub_centres = {h['id']: h['centre'] for h in scenario['mapPlan']['hubs']}
        positions = {}
        for zid, zone in zones.items():
            check(zone['hub'] in hub_centres, f'{context}: undefined side hub')
            if zone['hub'] in hub_centres:
                positions[zid] = [a+b for a,b in zip(hub_centres[zone['hub']], zone['offsetTiles'])]
        zids = list(positions)
        for i, zid in enumerate(zids):
            for other in zids[i+1:]:
                check(math.dist(positions[zid], positions[other]) > zones[zid]['radiusTiles']+zones[other]['radiusTiles'], f'{context}: secondary receiving/observation zones overlap')
        check(all(e['initialHub'] == o['reachability']['originHub'] for e in entities.values()), f'{context}: optional origin differs from entity placement')
        state = o.get('stateContract', {})
        check(all(state.get(flag) is True for flag in ('requiresNonterminalScenario', 'persistentAcrossSave', 'completionAndEffectsAtomic', 'paymentBeforeReward', 'paymentIsNotCompletion', 'failedGoalCannotReward', 'latchAtFirstCompletion', 'noMainVictoryDependency')), f'{context}: incomplete optional state/persistence guard')
        for req in o['predicate']['requirements']:
            if req['kind'] == 'entity-arrival':
                check(set(req['entities']) == set(entities) and req['requiredCount'] <= len(entities), f'{context}: impossible optional arrival')
                for eid, zid in req['destinations'].items():
                    check(zid in zones, f'{context}: undefined receiving zone')
                    if zid not in zones or eid not in entities:
                        continue
                    entity, zone = entities[eid], zones[zid]
                    check(entity['initialHub'] != zone['hub'] or math.dist(entity['offsetTiles'], zone['offsetTiles']) > zone['radiusTiles'], f'{context}: initially completed optional arrival')
            elif req['kind'] == 'atomic-payment':
                for k, v in req['resources'].items():
                    costs[k] += v
                check(req['once'] and req['protectedRecoveryCannotBeSpent'], f'{context}: unsafe optional payment')
            elif req['kind'] == 'visit-zones':
                check(set(req['zones']) == set(zones) and req['requiredCount'] == len(zones), f'{context}: impossible optional exploration')
            elif req['kind'] == 'entity-health':
                check(req['entity'] in entities and entities[req['entity']].get('initialHealthFraction') == 0.5, f'{context}: missing repair target')
            else:
                check(False, f'{context}: unknown optional predicate')
        check(state.get('rewardTransaction') == ['verify all predicate ledgers and nonterminal state', 'verify reserved stock', 'debit reserved stock', 'credit spendable stock', 'set reward onceFlag', 'set completionFlag'], f'{context}: undefined atomic optional funding transaction')
        for effect in o['effects']:
            check(not effect['changesHistoricalOutcome'], f'{context}: reward changes history')
            check(effect['onceFlag'] not in seen_flags, f'{context}: duplicate reward flag')
            seen_flags.add(effect['onceFlag'])
            for k, v in effect['resources'].items():
                rewards[k] += v
        check('no main-goal defeat' in o['unavailablePolicy'], f'{context}: side goal can softlock main route')
    budget = scenario.get('secondaryBudget', {})
    check(rewards == budget.get('reservedRewards'), f'{label}: optional reward budget drift')
    check(costs == budget.get('maxOptionalCosts'), f'{label}: optional cost budget drift')
    for level, b in scenario['difficulty'].items():
        for k in RESOURCES:
            available_without = b['startingResources'][k]+b['gatherableBank'][k]-rewards[k]
            main_need = b['mandatoryDeliveries'][k]+b['replacementBudget'][k]+b['protectedRecoveryStock'][k]
            check(available_without >= main_need, f'{label}/{level}: main goal needs optional {k} reward')
            check(b.get('accessibleWithoutOptionalRewards', {}).get(k) == available_without, f'{label}/{level}: nonoptional stock drift')
            check(rewards[k] + costs[k] <= b['supplyMargins'][k], f'{label}/{level}: all side goals overdraw {k} surplus')
            check(rewards[k] <= budget.get('reallocatedCacheAllowance', {}).get(k, 0), f'{label}: rewards created beyond old cache allowance')
    approaches = scenario.get('playstyles', [])
    check(len({tuple(sorted(style['optionalObjectives'])) for style in approaches}) == len(approaches), f'{label}: identical playstyle alternatives')
    check(len(approaches) >= 3, f'{label}: fewer than three declared playstyles')
    ids = {o['id'] for o in objectives}
    for style in approaches:
        check(set(style['optionalObjectives']) <= ids and len(style['optionalObjectives']) >= 2, f'{label}: vague/undefined playstyle')
        check(style['mainObjectivesUnchanged'] and style['historicalOutcomeUnchanged'], f'{label}: style alters mandatory history')
