"""Validate compound authoring contracts without pretending they are executable DSL."""
import math
from secondary import RESOURCES, audit_objective_numbers

ENTITY_STATES = {
    'arrived', 'alive', 'alive-and-held', 'collected', 'destroyed', 'prepared',
    'registered-after-arrival', 'repaired-to-full-health', 'sealed-and-delivered',
}
KINDS = {
    'entity-state', 'area-state', 'resource-transaction', 'minimum-stock',
    'civilian-protection', 'paired-delivery', 'route-choice', 'finite-wave-resolution',
    'hold-area', 'receipt-exists', 'derived-token', 'ordered-departure',
    'forbidden-entry', 'phase-deadline',
}


def check_objectives(scenario, check, label):
    numeric_errors = audit_objective_numbers(scenario)
    for error in numeric_errors:
        check(False, error)
    if numeric_errors:
        return
    world = scenario.get('worldContract', {})
    entities = {e['id']: e for e in world.get('entities', [])}
    zones = {z['id']: z for z in world.get('zones', [])}
    hubs = {h['id']: h for h in scenario['mapPlan']['hubs']}
    check(len(entities) == len(world.get('entities', [])), f'{label}: duplicate world entity')
    check(len(zones) == len(world.get('zones', [])), f'{label}: duplicate world zone')
    for entity in entities.values():
        check(entity['initialHub'] in hubs, f'{label}: undefined entity origin')
        check(entity['finite'] and entity['initiallyDelivered'] is False, f'{label}: infinite or pre-delivered entity')
    for zone in zones.values():
        check(zone['hub'] in hubs, f'{label}: undefined zone district')
        check(math.hypot(*zone['offsetTiles']) <= 12, f'{label}: zone outside authorised footprint')
    receipts = {}
    objectives = {o['id']: o for o in scenario['objectivePlan']}
    for objective in objectives.values():
        pred = objective['predicate']
        reqs = pred.get('requirements', [])
        req_ids = [r['id'] for r in reqs]
        check(pred.get('operator') == 'all' and pred.get('allRequired') is True, f'{label}: secondary conditions may be omitted')
        check(bool(reqs) and len(req_ids) == len(set(req_ids)), f'{label}: missing/duplicate requirement')
        check(set(req_ids) == set(pred.get('requiredLedgers', [])), f'{label}: missing required ledger')
        total = {k: 0 for k in RESOURCES}
        for req in reqs:
            kind = req['kind']
            name = f'{label}/{objective["id"]}/{req["id"]}'
            check(kind in KINDS, f'{name}: unknown world predicate')
            refs = req.get('entities', []) + req.get('inputEntities', []) + req.get('outputEntities', [])
            refs += req.get('blockingEnemies', []) + req.get('inputRecords', []) + req.get('departingEntities', []) + req.get('accountEntityIds', [])
            refs += [p[k] for p in req.get('pairs', []) for k in ('cargo', 'receiver')]
            check(all(e in entities for e in refs), f'{name}: undefined entity reference')
            zrefs = req.get('zones', []) + req.get('receivingZones', []) + list(req.get('destinations', {}).values())
            if 'destination' in req:
                zrefs.append(req['destination'])
            check(all(z in zones for z in zrefs), f'{name}: undefined destination')
            if kind == 'entity-state':
                targets = req['entities']
                check(req['state'] in ENTITY_STATES, f'{name}: undefined entity state')
                check(0 < req['requiredCount'] <= len(set(targets)), f'{name}: impossible entity threshold')
                check(req['oncePerEntity'], f'{name}: repeated entity counting')
                if 'destinations' in req:
                    check(set(req['destinations']) == set(targets), f'{name}: missing individual destination')
                    for entity_id, zone_id in req['destinations'].items():
                        if entity_id not in entities or zone_id not in zones:
                            continue
                        entity, zone = entities[entity_id], zones[zone_id]
                        if entity['initialHub'] == zone['hub']:
                            check(math.dist(entity['offsetTiles'], zone['offsetTiles']) > zone['radiusTiles'], f'{name}: arrival counts initial spawn')
                if 'distinctDestinationCount' in req:
                    counts = {z: list(req['destinations'].values()).count(z) for z in set(req['destinations'].values())}
                    check(len(counts) == req['distinctDestinationCount'] and all(n >= req['minimumPerDestination'] for n in counts.values()), f'{name}: distinct destination distribution missing')
                if 'eligibleEntitiesFromLedger' in req:
                    source = req['eligibleEntitiesFromLedger']
                    exports = objectives[source['objective']]['predicate'].get('exportedLedgers', [])
                    check(any(e['id'] == source['ledger'] and e['operator'] == 'intersection' and e['minimumCount'] >= req['requiredCount'] for e in exports), f'{name}: missing supplied survivor intersection')
                for receipt in req.get('generatedByReceipts', []):
                    producer = next((p for p in objectives[receipt['fromObjective']]['predicate']['requirements'] if p['id'] == receipt['fromRequirement']), {})
                    check(receipt['output'] in targets and producer.get('destinations', {}).get(receipt['receivedEntity']) == receipt['destination'], f'{name}: record lacks actual delivery receipt')
            elif kind == 'area-state':
                check(0 < req['requiredCount'] <= len(set(req['zones'])), f'{name}: impossible area threshold')
                if req['id'] == 'main-access':
                    check(all(zones.get(z, {}).get('hub') == objective['targetHub'] for z in req['zones']), f'{name}: access assigned to wrong geographic district')
            elif kind == 'forbidden-entry':
                check(req.get('actorSelector') == 'all-player-controlled-units', f'{name}: entry restriction omits player units')
            elif kind == 'resource-transaction':
                check(req['once'] and req['atomic'] and req['account'] == 'spendable', f'{name}: repeatable/unprotected payment')
                check(req['paidFlag'] not in receipts, f'{name}: duplicated receipt flag')
                receipts[req['paidFlag']] = objective['id']
                check(set(req['allocations']) == set(req['receivingZones']), f'{name}: delivery receivers do not match allocations')
                for resource, amount in req['amounts'].items():
                    check(resource in RESOURCES and amount > 0, f'{name}: unsupported resource')
                    check(sum(a.get(resource, 0) for a in req['allocations'].values()) == amount, f'{name}: unbalanced delivery allocation')
                    if resource in total:
                        total[resource] += amount
            elif kind == 'paired-delivery':
                pairs = req['pairs']
                check(0 < req['requiredCount'] <= len(pairs), f'{name}: impossible paired delivery')
                check(len({p['cargo'] for p in pairs}) == len(pairs) and len({p['receiver'] for p in pairs}) == len(pairs), f'{name}: repeated cargo or receiver')
                family = next((r for r in reqs if r['id'] == 'families-arrived'), {})
                check({p['receiver'] for p in pairs} == set(family.get('entities', [])) and req['requiredCount'] == family.get('requiredCount'), f'{name}: supplies do not follow same surviving families')
            elif kind == 'receipt-exists':
                check(receipts.get(req['flag']) == req['fromObjective'] and not req['newDebit'], f'{name}: absent or repeated predecessor payment')
            elif kind == 'phase-deadline':
                check(set(req['secondsByDifficulty']) == {'easy', 'standard', 'hard'} and min(req['secondsByDifficulty'].values()) > req['warningSeconds'] > 0, f'{name}: blind deadline')
                check(req['clock'] == 'relative-to-phase-entry', f'{name}: incorrect deadline clock')
            elif kind == 'finite-wave-resolution':
                check(req['waves'] == ['wave-1', 'wave-2', 'wave-3'] and req['requiredCount'] == 3, f'{name}: missing finite siege effort')
        for exported in pred.get('exportedLedgers', []):
            check(set(exported['fromRequirements']).issubset(set(req_ids)), f'{label}: supplied survivor ledger omits required receipt')
        check(total == {k: pred['resourceAmounts'].get(k, 0) for k in RESOURCES}, f'{label}: compound resource ledger diverged')
    initial_guards = sum(e['role'] in {'military-guard', 'military-post'} for e in entities.values())
    for level, balance in scenario['difficulty'].items():
        check(initial_guards <= balance['initialEnemy'], f'{label}/{level}: objective guards exceed finite initial roster')
        allocation = scenario['economicAnalysis'].get('optionalCacheAllocation', {})
        check(all(balance['supplyMargins'][k] >= allocation.get(k, 0) for k in RESOURCES), f'{label}: compulsory economy depends on optional cache')
    supply = scenario['mapPlan'].get('phaseSupply', {})
    points = supply.get('waypoints', [])
    check(len(points) >= 2, f'{label}: missing local supply circuit')
    if len(points) < 2:
        return
    distance = sum(math.dist(a, b) for a, b in zip(points, points[1:]))
    floor = math.ceil(4 * distance / .7 + 90)
    check(abs(distance - supply['distanceTiles']) < .01, f'{label}: supply circuit measurement drift')
    gaps = {}
    for level, balance in scenario['difficulty'].items():
        gap = balance['waves'][0]['offsetSeconds']
        gaps[level] = gap
        check(gap >= floor, f'{label}/{level}: waves prevent two local supply trips')
        check([w['offsetSeconds'] for w in balance['waves']] == [gap, gap*2, gap*3], f'{label}/{level}: inconsistent wave clock')
        if any(r['kind'] == 'finite-wave-resolution' for o in objectives.values() for r in o['predicate']['requirements']):
            check(gap*3 + 180 < balance['roughDurationMinutes'][1]*60, f'{label}/{level}: mandatory siege exceeds duration estimate')
    check(gaps['easy'] > gaps['standard'] > gaps['hard'], f'{label}: difficulties have identical wave pressure')
