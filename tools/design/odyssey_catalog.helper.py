"""Read and audit odyssey selections separately from approved mission dossiers."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DRAFT_DOSSIER_STATUS = 'authored full draft; independent source/geometry/native/balance gates pending'
SELECTION_ONLY_STATUS = 'selection and mechanic authored; full world/objective/balance/screen/map dossier pending'


def authored_dossier_status(campaign, episode_id):
    """Describe artifact coverage; this renderer cannot issue an approval."""
    return (DRAFT_DOSSIER_STATUS
            if any(e['id'] == episode_id for e in campaign.get('episodes', []))
            else SELECTION_ONLY_STATUS)


def load_json(relative):
    return json.loads((ROOT / relative).read_text(encoding='utf-8'))


def odyssey_catalog():
    policy = load_json('docs/design/odyssey-policy.json')
    campaigns = [load_json(f"docs/design/odysseys/{c['id']}.json") for c in policy['campaigns']]
    return policy, campaigns


def audit_selections(policy, campaigns):
    failures = []

    def require(condition, message):
        if not condition:
            failures.append(message)

    baseline = {c['id']: c for c in load_json('docs/design/catalog.json')['campaigns']}
    campaign_policies = {c['id']: c for c in policy['campaigns']}
    targets = {cid: c['targetScenarios'] for cid, c in campaign_policies.items()}
    require({c['campaignId'] for c in campaigns} == set(targets), 'Campaign identities differ from policy')
    total = 0
    for campaign in campaigns:
        cid = campaign['campaignId']
        episodes = campaign.get('episodeSelection', [])
        total += len(episodes)
        require(len(episodes) == targets[cid], f'{cid}: selected count differs from target')
        require([e['order'] for e in episodes] == list(range(1, len(episodes) + 1)), f'{cid}: broken chronological display order')
        ids = [e['id'] for e in episodes]
        require(len(ids) == len(set(ids)), f'{cid}: duplicate episode identity')
        old_ids = {s['id'] for s in baseline[cid]['scenarios']}
        require(old_ids <= set(ids), f'{cid}: a baseline semantic identity was lost')
        acts = {a['id']: a for a in campaign['acts']}
        require(len(acts) == 5, f'{cid}: five acts required')
        act_targets = campaign_policies[cid].get('actEpisodeTargets')
        valid_targets = (isinstance(act_targets, list) and len(act_targets) == 5
                         and all(type(count) is int and count > 0 for count in act_targets))
        require(valid_targets, f'{cid}: act targets must contain five positive integers')
        if valid_targets:
            require(sum(act_targets) == targets[cid], f'{cid}: act target total differs from campaign target')
            require([len(act['episodeIds']) for act in campaign['acts']] == act_targets,
                    f'{cid}: act targets differ from authored membership')
        assigned = [i for a in acts.values() for i in a['episodeIds']]
        require(len(assigned) == len(set(assigned)) and set(assigned) == set(ids), f'{cid}: missing or multiply assigned act episode')
        for episode in episodes:
            label = f"{cid}/{episode['id']}"
            require(episode['actId'] in acts and episode['id'] in acts.get(episode['actId'], {}).get('episodeIds', []), f'{label}: incorrect act association')
            require(set(episode['title']) == {'en', 'es-ES'} and all(episode['title'].values()), f'{label}: missing localized title')
            historical = episode['historicalSelection']
            require(historical['sourceUrl'].startswith('https://') and bool(historical['passage']), f'{label}: no attributed source passage')
            require(episode['knowledgeBasis']['noOmniscience'], f'{label}: unlimited narrator knowledge')
            require(bool(episode['coreMechanic']) and bool(episode['geographyId']), f'{label}: unspecified local operation')
        for first, second, third in zip(episodes, episodes[1:], episodes[2:]):
            if first['coreMechanic'] == second['coreMechanic'] == third['coreMechanic']:
                require(bool(third.get('repeatCoreReason')), f"{cid}/{third['id']}: three consecutive identical cores without a reason")
        require(len({e['coreMechanic'] for e in episodes}) >= 4, f'{cid}: insufficient authored core variety')
        by_id = {e['id']: e for e in episodes}
        for constraint in campaign.get('chronologyConstraints', []):
            earlier = by_id.get(constraint.get('before'))
            later = by_id.get(constraint.get('after'))
            require(
                earlier is not None and later is not None
                and earlier['order'] < later['order']
                and bool(constraint.get('basis')),
                f"{cid}: authored chronology constraint violated: {constraint.get('before')} -> {constraint.get('after')}",
            )
        continuity = campaign['continuityContract']
        require(continuity['proceedWithoutPredecessor'] is True, f'{cid}: predecessor progress would gate play')
    require(total == policy['targetScenarioCount'], 'Total selected count differs from policy')
    manifest = load_json('docs/research/odyssey-research/reference-manifest.json')
    for asset in manifest['assets']:
        path = (ROOT / asset['path']).resolve()
        require(path.is_relative_to(ROOT), f"{asset['id']}: asset outside project")
        if path.is_file():
            data = path.read_bytes()
            require(len(data) == asset['bytes'] and hashlib.sha256(data).hexdigest() == asset['sha256'], f"{asset['id']}: download hash or bytes changed")
        else:
            failures.append(f"{asset['id']}: missing downloaded reference")
    return failures
