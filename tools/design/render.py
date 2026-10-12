"""Render the architect's authored catalogue into linked wiki and geographic SVG plans.

Run from any directory. The catalogue is the sole editorial input; output is not AoE2 code.
"""
import argparse
import html
import json
from pathlib import Path
from geography import geometry_lines, tile_point

ROOT = Path(__file__).resolve().parents[2]
CHECK = False


def load(path):
    return json.loads((ROOT / path).read_text())


def save(path, content):
    path = ROOT / path
    if CHECK:
        if not path.is_file() or path.read_text(encoding='utf-8') != content:
            raise ValueError(f'Stale generated document: {path.relative_to(ROOT)}; run render.py')
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def linked_sources(ids, sources):
    return '\n'.join(f"- [{sources[i]['title']}]({sources[i]['url']}): {sources[i]['locator']}. {sources[i]['qualification']}" for i in ids)


def screen_table(screens):
    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', '<br>')
    rows = ['| Key / condition | Narrator → destination | English | Español |', '|---|---|---|---|']
    for screen in screens:
        rows.append('| ' + ' | '.join(cell(v) for v in [f"`{screen['key']}` / {screen.get('condition', 'always')}", f"{screen['narrator']} → {screen.get('destination', 'next')}", screen['text']['en'], screen['text']['es-ES']]) + ' |')
    return '\n'.join(rows)


def map_svg(campaign, scenario, profile, layers):
    size = scenario['mapSize']
    def point(coords):
        x, y = tile_point(profile['bbox'], coords, size)
        return x / (size - 1) * 700 + 40, y / (size - 1) * 700 + 85
    def tile(coords):
        return coords[0] / (size - 1) * 700 + 40, coords[1] / (size - 1) * 700 + 85
    def poly(points, color, width, dashed=False, geographic=True):
        transform = point if geographic else tile
        coords = ' '.join(f'{x:.2f},{y:.2f}' for x, y in map(transform, points))
        dash = ' stroke-dasharray="9 7"' if dashed else ''
        return f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"{dash}/>'
    title = html.escape(scenario['title']['en'])
    pieces = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 855" role="img" aria-label="{title}: geographic design controls">', '<rect width="1080" height="855" fill="#f5f0df"/>', f'<text x="40" y="35" font-family="sans-serif" font-size="23">{title}</text>', f'<text x="40" y="61" font-family="sans-serif" font-size="14">{html.escape(profile["name"])} · {size} × {size} tiles · {html.escape(scenario["date"])}</text>', '<rect x="40" y="85" width="700" height="700" fill="#dfdfba" stroke="#5c6542"/>']
    for n in range(1, 10):
        x = 40 + 70 * n; y = 85 + 70 * n
        pieces.append(f'<path d="M {x} 85 V785 M40 {y} H740" stroke="#c7c8a7" fill="none"/>')
    for layer in layers:
        for feature in layer['features']:
            if feature['properties']['region'] == profile['id']:
                for line in geometry_lines(feature['geometry']):
                    pieces.append(poly(line, '#306a88', 2))
    if profile['waterControlLine']['coordinates']:
        pieces.append(poly(profile['waterControlLine']['coordinates'], '#419fc0', 6, dashed=True))
    for route, color in zip(scenario['mapPlan']['corridors'], ['#94542f', '#7463a3']):
        pieces.append(poly(route['waypoints'], color, 4, dashed=route['mode'] != 'land', geographic=False))
    for sector in scenario['mapPlan'].get('explorationPlan', {}).get('sectors', []):
        x, y = tile(sector['centreTiles'])
        pieces.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="45" fill="#b6c997" fill-opacity=".3" stroke="#75875a" stroke-dasharray="4 4"/>')
        pieces.append(f'<text x="{x-16:.2f}" y="{y+4:.2f}" font-family="sans-serif" font-size="12">{sector["id"]}</text>')
    for objective in scenario.get('secondaryObjectives', []):
        centres = {h['id']: h['centre'] for h in scenario['mapPlan']['hubs']}
        for zone in objective['world']['zones']:
            coords = [a+b for a,b in zip(centres[zone['hub']], zone['offsetTiles'])]
            x, y = tile(coords)
            pieces.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6" fill="#43714b" fill-opacity=".65"/>')
    for i, landmark in enumerate(scenario['mapPlan']['landmarks']):
        x, y = tile(landmark['tile'])
        pieces.extend([f'<circle cx="{x:.2f}" cy="{y:.2f}" r="7" fill="#2e3740"/>', f'<text x="{x+10:.2f}" y="{y-9:.2f}" font-family="sans-serif" font-size="16">{i+1}</text>'])
    for hub in scenario['mapPlan']['hubs']:
        x, y = tile(hub['centre'])
        pieces.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="24" fill="none" stroke="#ab522c" stroke-width="2"/>')
    legend = ['N ↑ · East →', 'Solid blue: modern Natural Earth', 'Dashed blue: schematic water control', 'Brown: main route proposal', 'Purple: relief route proposal', 'Circles: objective districts', 'Green dots: optional task controls', 'Routes require terrain/footprint QA', 'Ancient coast/camps remain qualified', 'Reference plan, not a native game map']
    for i, text in enumerate(legend):
        pieces.append(f'<text x="770" y="{105+i*24}" font-family="sans-serif" font-size="14">{html.escape(text)}</text>')
    for i, landmark in enumerate(scenario['mapPlan']['landmarks']):
        pieces.append(f'<text x="770" y="{395+i*63}" font-family="sans-serif" font-size="13">{i+1}: {html.escape(landmark["name"][:37])}</text>')
        pieces.append(f'<text x="770" y="{415+i*63}" font-family="monospace" font-size="12">{landmark["lonLat"]} → {landmark["tile"]}</text>')
    pieces.append(f'<text x="40" y="821" font-family="sans-serif" font-size="13">WGS84 bounds {profile["bbox"]} · cosine-corrected, padded square; positions approximate</text>')
    pieces.append('</svg>\n')
    return '\n'.join(pieces)


def render():
    catalog = load('docs/design/catalog.json')
    sources = {s['id']: s for s in load('docs/design/sources.json')['sources']}
    profiles = {r['id']: r for r in load('docs/design/geography.json')['profiles']}
    layers = [load('docs/design/reference/geography/regional-coastline.geojson'), load('docs/design/reference/geography/regional-rivers_lake_centerlines.geojson')]
    campaigns = catalog['campaigns']
    index = ['# Campaign production catalogue', '', 'Authoritative editorial input: [catalog.json](catalog.json). This is a design contract, not campaignSchema or a playable mod. English is the source; Spanish is supplied for every player-facing screen. Architecture documentation remains in Spanish.', '', 'Nine historical campaigns / 39 historical scenarios, plus two separately specified technical lab scenarios. The Milvian pilot reuses the C01 mission, rather than adding a contradictory fortieth historical scenario.', '', '| Identity | English / Español | Period | Missions | Narrator |', '|---|---|---|---:|---|']
    for c in campaigns:
        index.append(f"| {c['publicId']} / `{c['id']}` | [{c['title']['en']}](../wiki/{c['id']}/12-production-blueprint.md) / {c['title']['es-ES']} | {c['period']} | {len(c['scenarios'])} | {c['narrator']['name']} |")
        n = c['narrator']; base = f"docs/wiki/{c['id']}"
        narrator = [f"# {n['name']} — campaign narrator", '', 'Fictional, independently voiced person. The collection narrator remains objective; this person supplies situated feeling and memory, never changes the documented result.', '', f"Life: {n['lifespan']}. Occupation: {n['occupation']}.", '', n['temperament'], '', n['backstory'], '', n['knowledgeLimits'], '', f"Opening EN: {n['opening']['en']}", '', f"Apertura ES: {n['opening']['es-ES']}", '', '## Witness and retrospective frame', '', '| Scenario | Approximate age | Knowledge basis |', '|---|---:|---|']
        for w in n['witnessByScenario']:narrator.append(f"| {w['scenarioId']} | {w['ageAtMainEventApprox'] if w['ageAtMainEventApprox'] is not None else 'not born'} | {w['basis']} |")
        narrator.extend(['', '## Performance and depiction', '', json.dumps(n['delivery'], ensure_ascii=False, indent=2), '', n['voice']['en'], '', n['voice']['es-ES'], '', '\n'.join('- '+x for x in n['restrictions']), ''])
        save(f'{base}/13-narrator-bible.md', '\n'.join(narrator))
        body = [f"# {c['title']['en']} / {c['title']['es-ES']}", '', f"Identity: `{c['id']}` / {c['publicId']} / `{c['internalName']}`. Source locale `en`. Period {c['period']}.", '', c['theme'], '', 'This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.', '', f"[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)", '', '## Arc, inflection points and ending', '', c['end'], '', c['chronologyPolicy'], '', 'The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.', '', '| Scenario | Event / dramatic task | Map |', '|---|---|---|']
        for s in c['scenarios']:body.append(f"| [{s['title']['en']}](scenarios/{s['id']}.md) | {s['date']} / {s['mechanic']} | {s['mapSize']} × {s['mapSize']} / {s['geographyId']} |")
        body.extend(['', '## Engine representation', '', json.dumps(c['representation'], ensure_ascii=False, indent=2), '', '## Art assignments', '', json.dumps(c['artDirection'], ensure_ascii=False, indent=2), '', '## Predecessors and campaign screens', '', 'Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.', '', screen_table(c['screens']), '', '## Historical source ledger', '', linked_sources(list(dict.fromkeys(i for s in c['scenarios'] for i in s['sourceIds'])), sources), ''])
        save(f'{base}/12-production-blueprint.md', '\n'.join(body))
        for s in c['scenarios']:
            r = profiles[s['geographyId']]
            save(s['mapPlan']['asset'], map_svg(c, s, r, layers))
            lines = [f"# {s['title']['en']} / {s['title']['es-ES']}", '', f"`{c['id']}/{s['id']}` · {s['date']} · {s['mechanic']}", '', f"[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/{c['id']}/{s['id']}.svg)", '', '## Historical frame and outcome', '', s['historicalBrief']['en'], '', s['historicalFrame'], '', s['historicalOutcome'], '', linked_sources(s['sourceIds'], sources), '', 'Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.', '', '## Personal voice', '', s['personalNarration']['en'], '', s['personalNarration']['es-ES'], '', '## Geography and map construction', '', f"{r['name']} — {s['mapSize']} × {s['mapSize']} tiles; north-up design controls {r['bbox']}.", '', r['terrain'], '', r['water'], '', r['hills'], '', r['roads'], '', 'Exclude: '+r['anachronisms'], '', 'Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.', '', '| Control | WGS84 longitude,latitude | Tile x,y |', '|---|---|---|']
            for lm in s['mapPlan']['landmarks']:lines.append(f"| {lm['name']} | {lm['lonLat']} | {lm['tile']} |")
            lines.extend(['', '```json', json.dumps(s['mapPlan'], ensure_ascii=False, indent=2), '```', '', '## Objectives, entity ledgers and state machine', '', 'Every predicate requires the actual world-state operation, not a timer approximating success. Coordinates below specify district plus local offset; validate actual footprint and terrain before assigning engine IDs.', '', '```json', json.dumps({'objectives':s['objectivePlan'],'worldContract':s['worldContract'],'states':s['stateMachine'],'roster':s['tacticalRoster'],'secondaryObjectives':s.get('secondaryObjectives',[]),'secondaryBudget':s.get('secondaryBudget',{}),'playstyles':s.get('playstyles',[])}, ensure_ascii=False, indent=2), '```', '', '## Difficulty and finite budget', '', 'These are explicit estimates for calibration, not measured wins or evidence of perfect balance. Player starting military is preplaced; enemy initial/waves are one roster with production disabled. Nominal militia/spearman/archer/scout costs audit the plan, not historical army numbers. Resource banks include mandatory delivery, replacement allowance, protected recovery and a surplus.', '', '| Profile | Start F/W/G/S | Gatherable F/W/G/S | Escort | Initial + waves | Warning / gap seconds |', '|---|---|---|---:|---|---|'])
            for level,b in s['difficulty'].items():
                fmt=lambda x:'/'.join(str(x[k]) for k in ['food','wood','gold','stone'])
                lines.append(f"| {level} | {fmt(b['startingResources'])} | {fmt(b['gatherableBank'])} | {b['startingEscortCount']} | {b['initialEnemy']} + {' + '.join(str(w['count']) for w in b['waves'])} = {b['enemyTotalCap']} | {b['reactionMarginSeconds']} / {b['waves'][0]['offsetSeconds']} |")
            lines.extend(['', '```json', json.dumps({'profiles':s['difficulty'],'analysis':s['economicAnalysis'],'secondaryBudget':s.get('secondaryBudget',{})}, ensure_ascii=False, indent=2), '```', '', '## Choice, failure and recovery', '', s['choice'], '', s['recovery'], '', json.dumps(s['failureRecovery'], ensure_ascii=False, indent=2), '', '## Events and every player-facing screen', '', 'The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.', '', screen_table(s['screens']), '', '## Adversarial QA', '', '\n'.join(f"- `{q['id']}` ({q['status']}): {q['expected']}" for q in s['qa']), ''])
            save(f'{base}/scenarios/{s["id"]}.md', '\n'.join(lines))
    index.extend(['', '## Cross-campaign order', '', '| Route remembered | Recommended next | Entry policy |', '|---|---|---|'])
    for c in campaigns:
        for route in c['routes']:index.append(f"| `{route['key']} = 1` | {route['next'] or 'No designated direct sequel; offer parallel catalogue'} | recommendation + recap, never a lock |")
    index.extend(['', '[Production contract](production-contract.md) · [references and licensing](reference/CREDITS.md) · [sources](sources.json) · [QA](../qa/campaign-design/verification.md)', '', 'Regenerate: `python3 tools/design/render.py`; verify: `python3 tools/design/verify.py`. Do not hand-edit generated dossiers or SVGs; modify the authored catalogue or geographic profiles and regenerate. No generated file is native scenario input.', ''])
    save('docs/design/README.md', '\n'.join(index))
    lab = ['# Technical laboratory screens', '', 'Two fictional campaigns, 32×32 exception. English source with complete Spanish; all persistence/UI tests remain pending.', '']
    for pilot in catalog['pilots']:
        lab.extend(['## '+pilot['title']['en'], '', json.dumps(pilot['narrator'], ensure_ascii=False, indent=2), '', screen_table(pilot['screens']), ''])
    save('docs/wiki/route-pilot/14-screen-contract.md', '\n'.join(lab))
    manifest = load('docs/design/reference/manifest.json')
    credits = ['# Downloaded research references', '', 'Local files were actually downloaded and hashed on 2026-10-12. Research-only reference set; no asset is approved for a distributable mod. Each license remains attached to its original asset. Modern photographs, restored buildings and modern GIS are never evidence of an unchanged ancient landscape.', '', '| Local file | Creator / source | License | Cautions / modifications |', '|---|---|---|---|']
    for a in manifest['assets']:credits.append(f"| [{a['id']}]({Path(a['path']).relative_to('docs/design/reference').as_posix()}) | {a['author']} / [{a['title']}]({a['sourcePage']}) | [{a['license']}]({a['licenseUrl']}) | {a['usage']} {a['modifications']} |")
    credits.extend(['', 'CC BY requires attribution; CC BY-SA adaptations also preserve the corresponding ShareAlike license. The collection’s own license does not override these. Public-domain datasets still receive provenance credit. SHA-256, bytes, exact download URL and, for clipped GIS, upstream snapshot hashes are in manifest.json. No protected article text or entire paywalled publication has been mirrored.', '', 'The 10m regional coast/river extracts contain only clipped segments for the 26 profiles. Minor-river controls are authored schematic overlays and have a separate uncertainty label, rather than being falsely attributed to Natural Earth.', ''])
    save('docs/design/reference/CREDITS.md', '\n'.join(credits))
    print(f"Rendered {len(campaigns)} campaigns and {sum(len(c['scenarios']) for c in campaigns)} scenarios")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail on stale outputs without writing')
    CHECK = parser.parse_args().check
    render()
