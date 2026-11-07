#!/usr/bin/env python3
"""Recompute episode03 authored pickup-to-receiver distances.
Entity starts use the existing floor(x)+0.5 native snap; zone centers remain
at their authored continuous coordinates. Distances are unrounded Euclidean
values; this is geometric arithmetic, not a path or collision test.
"""
import hashlib, json, math
from pathlib import Path
ROOT=Path('/home/cartago/_projects/games/aoe2-mods')
OUT=Path('/home/cartago/.codex/artifacts/aoe2-mods/episode03-preflight-20261105')
doc=json.loads((ROOT/'docs/design/odysseys/faith-origins.json').read_text())
episode=next(e for e in doc['episodes'] if e['id']=='03-shared-provision-jerusalem')
hubs={h['id']:h['centre'] for h in episode['mapPlan']['hubs']}
def snap(p): return [math.floor(p[0])+0.5, math.floor(p[1])+0.5]
def distance(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
zones=[]
for z in episode['worldContract']['zones']:
    hub=hubs[z['hub']]
    center=[hub[0]+z['offsetTiles'][0],hub[1]+z['offsetTiles'][1]]
    zones.append({'id':z['id'],'hub':z['hub'],'authoredCentre':center,'radiusTiles':z['radiusTiles']})
entities=[]
for entity in episode['worldContract']['entities']:
    hub=hubs[entity['initialHub']]
    authored=[hub[0]+entity['offsetTiles'][0],hub[1]+entity['offsetTiles'][1]]
    start=snap(authored)
    comparisons=[]
    for zone in zones:
        d=distance(start,zone['authoredCentre'])
        comparisons.append({'zoneId':zone['id'],'distanceTiles':d,'radiusTiles':zone['radiusTiles'],'overlap':d<=zone['radiusTiles']})
    entities.append({'id':entity['id'],'role':entity['role'],'hub':entity['initialHub'],'offsetTiles':entity['offsetTiles'],'authoredPosition':authored,'nativeSnappedStart':start,'distanceFromSnappedStartToContinuousZoneCentre':comparisons,'overlapsAnyReceivingZone':any(x['overlap'] for x in comparisons)})
inv_path=OUT/'inventory.json'
inv=json.loads(inv_path.read_text())
inv['mainIdentitiesAndZones']['zones']=[{'id':z['id'],'hub':z['hub'],'authoredCentre':z['authoredCentre'],'radiusTiles':z['radiusTiles']} for z in zones]
inv['mainIdentitiesAndZones']['entities']=entities
inv['mainIdentitiesAndZones']['distanceMethod']='Entity coordinates snapped to floor(x)+0.5; compare snapped entity centre against authored continuous zone centre, without rounding distance; overlap iff unrounded Euclidean distance <= authored radius.'
inv_path.write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
report=OUT/'report.md'
s=report.read_text()
start=s.index('| Original | Hub + offset | Native snapped start |')
end=s.index('\n## Main predicates and phases',start)
rows=['| Original | Hub + offset | Native snapped start | Nearest receiving circle (continuous authored center) |','|---|---|---:|---|']
for entity in entities:
    nearest=min(entity['distanceFromSnappedStartToContinuousZoneCentre'],key=lambda x:x['distanceTiles'])
    rows.append(f"| `{entity['id'].split('.')[-1]}` ({entity['role']}) | {entity['hub']} + {entity['offsetTiles']} | {entity['nativeSnappedStart']} | {nearest['zoneId'].split('.')[-1]}: {nearest['distanceTiles']:.15f} tiles / r{nearest['radiusTiles']}; overlap={nearest['overlap']} |")
new_table='\n'.join(rows)
s=s[:start]+new_table+s[end:]
s=s.replace('Positions below apply the existing native-start snap convention `floor(x)+0.5`; they are authored layout arithmetic, not a certified map or path test.','Entity starts below apply the existing native-start snap convention `floor(x)+0.5`; distances compare those snapped entity centers against continuous authored zone centers, without rounding. This is authored geometry arithmetic, not a certified map or path test.')
s=s.replace('All six starts are outside all three receiving circles by the authored Euclidean-circle predicate. Baskets start at hub-1; distribution notes at hub-2. Receiving circle centers are hub centers, radius 3, so neither pickups nor notes begin registered as deliveries. This checks only snapped coordinate overlap, not collision or pathing.','All six starts are outside all three receiving circles under the unrounded Euclidean comparison of snapped entity centers to continuous authored zone centers. Baskets start at hub-1; distribution notes at hub-2. Receiving circle centers are hub centers, radius 3, so neither pickups nor notes begin registered as deliveries. This checks only coordinate overlap, not collision or pathing.')
report.write_text(s)
print('distances:')
for x in entities:
    near=min(x['distanceFromSnappedStartToContinuousZoneCentre'],key=lambda z:z['distanceTiles'])
    print(x['id'].split('.')[-1],format(near['distanceTiles'],'.17g'),near['zoneId'].split('.')[-1],near['overlap'])
for p in (report,inv_path):
    print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
