"""Check authored design integrity and downloaded references, without claiming gameplay QA."""
import argparse
import hashlib
import json
import math
import re
from pathlib import Path
from geography import tile_point
from objectives import check_objectives

ROOT = Path(__file__).resolve().parents[2]


def verify(root=ROOT, catalogue=None):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    def read(path):
        return json.loads((root / path).read_text())
    data = catalogue if catalogue is not None else read('docs/design/catalog.json')
    campaigns = data['campaigns']
    sources = {s['id']: s for s in read('docs/design/sources.json')['sources']}
    profiles = {r['id']: r for r in read('docs/design/geography.json')['profiles']}
    check(len(campaigns) == 9, 'Catalogue must have nine historical campaigns')
    check(sum(len(c['scenarios']) for c in campaigns) == 39, 'Catalogue must have 39 historical scenarios')
    for field in ['id', 'publicId', 'internalName']:
        check(len({c[field] for c in campaigns}) == len(campaigns), f'Duplicate campaign {field}')
    check(len({c['narrator']['id'] for c in campaigns}) == len(campaigns), 'Campaign narrator must be distinct per campaign')
    ids = {c['id'] for c in campaigns}
    keys = set()
    routes = {r['key'] for c in campaigns for r in c['routes']}
    edges = {c['id']: [r['next'] for r in c['routes'] if r['next']] for c in campaigns}
    visiting, visited = set(), set()
    def visit(id):
        if id in visiting:
            errors.append(f'Continuity cycle: {id}')
            return
        if id in visited or id not in edges:
            return
        visiting.add(id)
        for successor in edges[id]:
            visit(successor)
        visiting.remove(id)
        visited.add(id)
    for id in ids:
        visit(id)
    for c in campaigns:
        cid = c['id']
        check(c['sourceLocale'] == 'en', f'{cid}: new historical source must be en')
        check(c['enforceRequirement'] is False, f'{cid}: predecessor may not lock gameplay')
        for previous in c['recommendedPrevious']:
            check(previous['campaignId'] in ids, f'{cid}: missing predecessor')
            check(f"progress.{previous['campaignId']}.{previous['route']}" in routes, f'{cid}: nonexistent predecessor route')
        for route in c['routes']:
            check(route['key'] == f"progress.{cid}.{route['id']}", f'{cid}: invalid progress namespace')
            check(route['next'] is None or route['next'] in ids, f'{cid}: missing successor')
        witnesses = {w['scenarioId']: w for w in c['narrator']['witnessByScenario']}
        for s in c['scenarios']:
            label = f"{cid}/{s['id']}"
            check(s['id'] in witnesses, f'{label}: missing witness contract')
            check(300 <= s['mapSize'] <= 400, f'{label}: giant map outside agreed range')
            profile = profiles.get(s['geographyId'])
            check(profile is not None, f'{label}: missing geography')
            if not profile:
                continue
            check(s['mapPlan']['bbox'] == profile['bbox'], f'{label}: geographic extent diverged')
            check(len(s['mapPlan']['landmarks']) >= 3, f'{label}: insufficient location controls')
            for landmark in s['mapPlan']['landmarks']:
                expected = tile_point(profile['bbox'], landmark['lonLat'], s['mapSize'])
                check(landmark['tile'] == expected, f'{label}: coordinate transform drift')
                check(all(0 <= x < s['mapSize'] for x in expected), f'{label}: landmark outside map')
            for path in s['mapPlan']['corridors']:
                check(path['widthTiles'] >= 6, f'{label}: corridor too narrow')
                for pos in path['waypoints']:
                    check(all(0 <= x < s['mapSize'] for x in pos), f'{label}: route outside map')
            check((root / s['mapPlan']['asset']).is_file(), f'{label}: SVG not rendered')
            for source in s['sourceIds']:
                check(source in sources and sources[source]['consulted'], f'{label}: unconsulted or missing source {source}')
            check({o['id'] for o in s['objectivePlan']} == {'o1', 'o2', 'o3'}, f'{label}: missing objective')
            for o in s['objectivePlan']:
                check(o['operation'] and o['threshold'] > 0, f'{label}: vague objective')
                check(o['predicate']['neverUseTimerInstead'], f'{label}: timer substitutes a world predicate')
                check(o['predicate']['requiredCount'] == o['threshold'], f'{label}: threshold mismatch')
                check(all(e['countedOnce'] for e in o['entities']), f'{label}: repeatable entity delivery')
            check_objectives(s, check, label)
            required = {k:sum(o['predicate']['resourceAmounts'].get(k,0) for o in s['objectivePlan']) for k in ['food','wood','gold','stone']}
            check(required == s['deliveryRequirements'], f'{label}: unaccounted delivery')
            check(set(s['difficulty']) == {'easy', 'standard', 'hard'}, f'{label}: missing difficulty')
            for level, b in s['difficulty'].items():
                check(b['basis'].startswith('estimated'), f'{label}: unmeasured balance presented as measured')
                check(len(b['waves']) == 3 and all(not w['repeat'] for w in b['waves']), f'{label}: infinite or missing waves')
                check(b['initialEnemy'] + sum(w['count'] for w in b['waves']) == b['enemyTotalCap'], f'{label}/{level}: finite reserve does not add up')
                check(sum(b['initialComposition'].values()) == b['initialEnemy'], f'{label}: initial roster count mismatch')
                for wave in b['waves']:
                    check(sum(wave['composition'].values()) == wave['count'], f'{label}: wave count mismatch')
                    check(wave['offsetSeconds'] >= wave['warningSeconds'] > 0, f'{label}: blind/negative warning')
                check(not b['enemyProduction'] and not b['regeneratingResources'], f'{label}: hidden infinite economy')
                check(b['mandatoryDeliveries'] == required, f'{label}: difficulty changes mandatory supply')
                for resource, amount in required.items():
                    available = b['startingResources'][resource] + b['gatherableBank'][resource]
                    need = amount + b['replacementBudget'][resource] + b['protectedRecoveryStock'][resource]
                    check(available >= need, f'{label}/{level}: insolvent {resource} budget')
                    check(b['supplyMargins'][resource] == available - need, f'{label}: surplus arithmetic drift')
            intro = [x['narrator'] for x in s['screens'] if x['id'] in ['fact-intro', 'personal-intro']]
            outro = [x['narrator'] for x in s['screens'] if x['id'] in ['victory-fact', 'victory-personal']]
            check(intro == ['collection-narrator', c['narrator']['id']], f'{label}: wrong introduction voice order')
            check(outro == ['collection-narrator', c['narrator']['id']], f'{label}: wrong ending voice order')
            check(all(q['status'] == 'pending' for q in s['qa']), f'{label}: design-only QA may not claim passed')
        for screen in c['screens'] + [x for s in c['scenarios'] for x in s['screens']]:
            key = screen['key']
            check(key not in keys, f'Duplicate screen key: {key}')
            keys.add(key)
            check(set(screen['text']) == {'en', 'es-ES'} and all(screen['text'].values()), f'Missing bilingual text: {key}')
            check(screen.get('skippable', False), f'Unskippable screen: {key}')
            for loc, chunks in screen.get('captionSegments', {}).items():
                check(' '.join(chunks) == ' '.join(screen['text'].get(loc, '').split()), f'Caption content lost: {key}')
                check(all(len(chunk.split()) <= 32 for chunk in chunks), f'Caption too long: {key}')
    manifest = read('docs/design/reference/manifest.json')
    for a in manifest['assets']:
        path = (root / a['path']).resolve()
        check(path.is_relative_to(root.resolve()), f"Unsafe reference path: {a['id']}")
        if not path.is_file():
            errors.append(f"Missing reference: {a['id']}")
            continue
        content = path.read_bytes()
        check(len(content) == a['bytes'], f"Reference size drift: {a['id']}")
        check(hashlib.sha256(content).hexdigest() == a['sha256'], f"Reference hash drift: {a['id']}")
        check(a['license'] and a['author'] and a['sourcePage'], f"Missing rights: {a['id']}")
        check(a['productionApproved'] is False, f"Research photo falsely approved: {a['id']}")
    assignments = read('docs/design/assignments.json')['assignments']
    check({a['campaignId'] for a in assignments} == ids, 'Missing official proposal per campaign')
    return errors, {'campaigns':len(campaigns), 'historicalScenarios':sum(len(c['scenarios']) for c in campaigns), 'technicalScenarios':len(data['pilots']), 'historicalScreens':len(keys), 'regions':len(profiles), 'sources':len(sources), 'downloadedReferences':len(manifest['assets'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    errors, counts = verify()
    report = {'status':'failed' if errors else 'passed', 'scope':'design integrity only; game QA pending', 'counts':counts, 'errors':errors}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(1 if errors else 0)
