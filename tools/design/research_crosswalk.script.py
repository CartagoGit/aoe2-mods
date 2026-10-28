"""Render source consultation coverage; no campaign, approval or DelendAI state is changed."""

import argparse
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE = runpy.run_path(str(Path(__file__).with_name('research_crosswalk.validator.py')))
CATALOG = runpy.run_path(str(Path(__file__).with_name('odyssey_catalog.helper.py')))
CROSSWALK_PATH = MODULE['CROSSWALK_PATH']
REPORT_PATH = MODULE['REPORT_PATH']


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def render_report(report):
    lines = ['# Source consultation crosswalk', '',
             'Research linkage only. Archived declarations, fresh bounded consultations and historical approval are different things. No row approves a dossier, map, campaign or game behavior.', '',
             'This sidecar supplements existing inline annotations; unlinked here does not mean no earlier research exists. Hashes and exact semantic identities prevent silent source or selection substitution. Missing architect checks remain missing. A readable passage can be irrelevant or contradict the intended claim; its count is not a support or acceptance score.', '',
             '| Campaign | Selected | Linked archive records | Architect checks | With a readable passage | Only unavailable/metadata | Linked without architect check | Unlinked here |',
             '|---|---:|---:|---:|---:|---:|---:|---:|']
    for row in report['campaigns']:
        lines.append('| ' + ' | '.join(cell(row[key]) for key in (
            'campaignId', 'selected', 'linked', 'architectChecks', 'withPassageRead',
            'onlyUnavailableOrMetadata', 'linkedWithoutArchitectCheck', 'unlinked')) + ' |')
    lines += ['', '## Exact archived record links', '',
              'Access in the next table is the archived author’s declaration, not a new reading by the architect. Differences are reported rather than silently copied into campaign contracts.', '',
              '| Campaign / episode | Archived record | Declared access | Fresh consultation IDs | Differences from canonical selection |',
              '|---|---|---|---|---|']
    for row in report['records']:
        link = f"[{row['pointer']}]({Path(row['archivePath']).name}#{row['pointer']})"
        checks = ', '.join(item['id'] for item in row['consultations']) or 'none recorded'
        differences = ', '.join(row['differences']) or 'none in compared fields'
        lines.append(f"| {cell(row['campaignId'])}/{cell(row['scenarioId'])} | {link} | {cell(row['declaredAccess'])} | {cell(checks)} | {cell(differences)} |")
    lines += ['', '## Architect consultation scope', '']
    emitted = set()
    for row in report['records']:
        for consultation in row['consultations']:
            if consultation['id'] in emitted:
                continue
            emitted.add(consultation['id'])
            lines += [f"### {consultation['id']}", '',
                      f"{consultation['date']} · {consultation['realIdentity']} · `{consultation['access']}`", '',
                      f"[{consultation['title']}]({consultation['url']}) — {consultation['locator']}", '',
                      consultation['readScope'], '',
                      consultation['finding'] or 'No passage finding: access did not expose the source text.', '',
                      'Limits: ' + consultation['limits'], '']
    lines += ['## Binding-specific cautions and corrections', '']
    for row in report['records']:
        check = row['architectCheck']
        if check is None:
            continue
        lines += [f"**{row['campaignId']}/{row['scenarioId']}**: {check['scopeNote']}", '']
        for correction in check['corrections']:
            lines += ['- ' + correction, '']
    lines += ['No historical authoring or native gate is unlocked. The crosswalk is not a replacement for DelendAI review or its live proposal state.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Regenerate only the tracked research report')
    args = parser.parse_args()
    _, campaigns = CATALOG['odyssey_catalog']()
    data = json.loads((ROOT / CROSSWALK_PATH).read_text())
    report = MODULE['validate_crosswalk'](ROOT, campaigns, data)
    rendered = render_report(report)
    target = ROOT / REPORT_PATH
    if args.write:
        target.write_text(rendered, encoding='utf-8')
    elif target.read_text(encoding='utf-8') != rendered:
        raise ValueError('Stale research crosswalk report; regenerate with --write')
    print(json.dumps(report['campaigns'], ensure_ascii=False))


if __name__ == '__main__':
    main()
