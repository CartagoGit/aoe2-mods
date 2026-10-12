"""Check authored episode contracts without asserting native behavior or balance."""
import math
from secondary import check_optional_objectives


def audit_dossier(episode):
    failures=[]
    def check(condition,message):
        if not condition: failures.append(message)
    label=episode['id']
    check(300 <= episode['mapSize'] <= 400, f'{label}: historical map outside 300–400 range')
    for field in ('event','historicalOutcome','title','dramatizationNotice'):
        check(set(episode[field])=={'en','es-ES'} and all(episode[field].values()),f'{label}: missing bilingual {field}')
    entities={e['id']:e for e in episode['worldContract']['entities']}
    zones={z['id']:z for z in episode['worldContract']['zones']}
    check(len(entities)==len(episode['worldContract']['entities']),f'{label}: duplicate main identity')
    check(len(zones)==len(episode['worldContract']['zones']),f'{label}: duplicate main zone')
    objectives={o['id']:o for o in episode['objectivePlan']}
    check(len(objectives)==len(episode['objectivePlan']),f'{label}: duplicate main objective')
    check(episode['stateMachine']['campaignProgressWrite'] is False,f'{label}: intermediate episode can end campaign')
    check(episode['qa']['gameVerified'] is False,f'{label}: design promoted to game verification')
    for position,objective in enumerate(episode['objectivePlan']):
        context=f'{label}/{objective["id"]}'
        check(objective['after']==([] if position==0 else [episode['objectivePlan'][position-1]['id']]),f'{context}: broken main dependency')
        check(objective['predicate']['operator']=='all',f'{context}: compound predicate reduced to alternatives')
        requirements={r['id']:r for r in objective['predicate']['requirements']}
        check(len(requirements)==len(objective['predicate']['requirements']),f'{context}: duplicate main requirement')
        for req in requirements.values():
            if req['kind']=='entity-state':
                check(len(set(req['entities']))==len(req['entities']),f'{context}: duplicate entity in counter')
                check(set(req['entities'])<=set(entities) and req['requiredCount']<=len(req['entities']),f'{context}: impossible counter')
                if req['state']=='arrived':
                    check(set(req.get('destinations',{}))==set(req['entities']),f'{context}: incomplete receiving map')
                    check(set(req.get('destinations',{}).values())<=set(zones),f'{context}: unknown receiving zone')
                    for eid,zid in req.get('destinations',{}).items():
                        if eid not in entities or zid not in zones:
                            continue
                        entity,zone=entities[eid],zones[zid]
                        check(entity['initialHub']!=zone['hub'] or math.dist(entity['offsetTiles'],zone['offsetTiles'])>zone['radiusTiles'],f'{context}: initial arrival incorrectly counts')
                if req.get('eligibleEntitiesFromLedger'):
                    ref=req['eligibleEntitiesFromLedger'];source=objectives.get(ref['objective'])
                    ledgers=source['predicate'].get('exportedLedgers',[]) if source else []
                    ledger=next((l for l in ledgers if l['id']==ref['ledger']),None)
                    check(ledger is not None,f'{context}: missing prior recipient ledger')
                    source_position=next((i for i,o in enumerate(episode['objectivePlan']) if o['id']==ref['objective']),len(objectives))
                    check(source_position<position,f'{context}: recipient ledger is not from a prior objective')
                    if ledger:
                        arrival_sets=[set(r['entities']) for r in source['predicate']['requirements'] if r['id'] in ledger['fromRequirements'] and r['kind']=='entity-state' and r['state']=='arrived']
                        common=set.intersection(*arrival_sets) if arrival_sets else set()
                        check(len(arrival_sets)==len(ledger['fromRequirements']) and set(req['entities'])<=common and ledger['minimumCount']>=req['requiredCount'],f'{context}: recipient identities escape supplied intersection')
            elif req['kind']=='resource-transaction':
                check(len(set(req['receivingZones']))==len(req['receivingZones']) and set(req['receivingZones'])<=set(zones),f'{context}: invalid payment receivers')
                check(req.get('atomic') is True and req['once'] is True and req['account']=='spendable',f'{context}: unsafe payment transaction')
                check(set(req['allocations'])==set(req['receivingZones']),f'{context}: incomplete payment receivers')
                for resource in ('food','wood','gold','stone'):
                    check(sum(v.get(resource,0) for v in req['allocations'].values())==req['amounts'].get(resource,0),f'{context}: payment allocations not conserved')
            elif req['kind']=='derived-token':
                check(set(req['inputEntities'])<=set(entities) and set(req['outputEntities'])<=set(entities),f'{context}: broken derived identity')
                collected={eid for earlier in episode['objectivePlan'][:position+1] for r in earlier['predicate']['requirements'] if r['kind']=='entity-state' and r['state']=='collected' for eid in r['entities']}
                check(set(req['inputEntities'])<=collected,f'{context}: derivation without input collection')
            else:
                check(False,f'{context}: unsupported dossier predicate {req["kind"]}')
    for group in episode['worldContract']['survivorGroups']:
        check(len(group['entities'])==len(set(group['entities'])),f'{label}: duplicate survivor identity')
        check(set(group['entities'])<=set(entities) and group['minimumAliveOrAlreadySafe']<=len(set(group['entities'])),f'{label}: impossible survival threshold')
    screens=episode['screens'];keys=[s['key'] for s in screens]
    check(len(keys)==len(set(keys)),f'{label}: duplicate screen key')
    check([s['id'] for s in screens[:4]]==['title','fact-intro','handover','persona-intro'],f'{label}: incorrect opening narrator sequence')
    check(screens[1]['narrator']=='collection-narrator' and screens[2]['narrator']=='collection-narrator' and screens[3]['narrator']==episode['knowledgeBasis']['speaker'],f'{label}: incorrect opening narrator voice')
    closing={s['id']:s for s in screens}
    check(closing['fact-outro']['narrator']=='collection-narrator' and closing['persona-outro']['narrator']==episode['knowledgeBasis']['speaker'],f'{label}: incorrect closing narrator voice')
    for s in screens:
        check(set(s['text'])=={'en','es-ES'} and all(s['text'].values()),f'{label}/{s["id"]}: incomplete localization')
    hubs=episode['mapPlan']['hubs']
    check(all(0<=value<episode['mapSize'] for h in hubs for value in h['centre']),f'{label}: district outside map')
    check(all(math.dist(a['centre'],b['centre'])>6 for a,b in zip(hubs,hubs[1:])),f'{label}: main receiving districts overlap')
    check(all(b['mainFeasibleSkippingAllOptionals'] and b['allOptionalCostsAffordable'] for b in episode['difficulty'].values()),f'{label}: funding proof fails')
    costs={resource:sum(req.get('amounts',{}).get(resource,0) for objective in episode['objectivePlan'] for req in objective['predicate']['requirements'] if req['kind']=='resource-transaction') for resource in ('food','wood','gold','stone')}
    for level,budget in episode['difficulty'].items():
        check(budget['mandatoryDeliveries']==costs,f'{label}/{level}: main payment budget drift')
    check_optional_objectives(episode,check,label)
    return failures
