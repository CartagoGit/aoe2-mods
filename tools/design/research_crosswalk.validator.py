"""Validate source linkage and declared reading scope; never approve historical facts."""

import datetime
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

CROSSWALK_PATH = 'docs/research/odyssey-research/source-consultation-crosswalk.json'
REPORT_PATH = 'docs/research/odyssey-research/source-consultation-crosswalk.md'
RESEARCH_DIR = Path('docs/research/odyssey-research')
READABLE_ACCESS = {'excerpt', 'summary', 'article-passage', 'translated-passage'}
ACCESS = READABLE_ACCESS | {'metadata-only', 'unavailable'}


def selection_fingerprint(campaign_id, episode):
    evidence = {key: episode[key] for key in ('id', 'date', 'geographyId', 'historicalSelection')}
    encoded = json.dumps({'campaignId': campaign_id, 'selection': evidence},
                         ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(encoded.encode('utf-8')).hexdigest()


def record_at(document, pointer):
    """Resolve a strict JSON Pointer, rejecting ambiguous array indices and escapes."""
    if not isinstance(pointer, str) or not pointer.startswith('/') or re.search(r'~(?![01])', pointer):
        raise ValueError('Invalid record pointer')
    value = document
    for token in pointer[1:].split('/'):
        key = token.replace('~1', '/').replace('~0', '~')
        if isinstance(value, list):
            if not re.fullmatch(r'0|[1-9][0-9]*', key):
                raise ValueError('Invalid array pointer index')
            value = value[int(key)]
        elif isinstance(value, dict):
            value = value[key]
        else:
            raise ValueError('Record pointer traverses a scalar')
    return value


def exact_fields(value, fields, label):
    if not isinstance(value, dict) or set(value) != set(fields):
        raise ValueError(f'{label}: unexpected or missing fields')


def text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label}: expected nonempty text')


def https(value, label):
    text(value, label)
    parsed = urlparse(value)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError(f'{label}: expected an attributed HTTPS source URL')


def unique_rows(rows, label):
    if not isinstance(rows, list):
        raise ValueError(f'{label}: expected a list')
    result = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f'{label}: expected records')
        identity = row.get('id')
        text(identity, f'{label} identity')
        if identity in result:
            raise ValueError(f'{label}: duplicate identity {identity}')
        result[identity] = row
    return result


def checked_archive(root, archive, label):
    """Share byte and path checks for archives and their declared input snapshots."""
    exact_fields(archive, ('path', 'sha256'), label)
    base = (root / RESEARCH_DIR).resolve()
    if not base.is_relative_to(root.resolve()):
        raise ValueError('Research directory must remain inside the project')
    text(archive['path'], 'Source path')
    relative = Path(archive['path'])
    if relative.is_absolute() or '..' in relative.parts or '\\' in archive['path']:
        raise ValueError('Source path must remain inside the research directory')
    path = (root / relative).resolve()
    if not path.is_relative_to(base) or path == base or path.suffix != '.json':
        raise ValueError('Source path must name a local research JSON file')
    if not isinstance(archive['sha256'], str) or not re.fullmatch('[0-9a-f]{64}', archive['sha256']):
        raise ValueError('Source SHA-256 must identify the archived bytes')
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != archive['sha256']:
        raise ValueError(f'Stale archived source bytes: {label}')
    return json.loads(raw)


def checked_upstream_snapshots(root, document):
    """A projection cannot hide changed declared inputs behind its own fresh hash."""
    if not isinstance(document, dict) or 'upstreamSnapshots' not in document:
        return
    snapshots = document['upstreamSnapshots']
    if not isinstance(snapshots, list):
        raise ValueError('Upstream snapshots must be a list')
    paths = set()
    for snapshot in snapshots:
        checked_archive(root, snapshot, 'Upstream snapshot')
        if snapshot['path'] in paths:
            raise ValueError('Duplicate upstream snapshot path')
        paths.add(snapshot['path'])


def checked_sources(root, rows, campaign_ids):
    sources = unique_rows(rows, 'Sources')
    result = {}
    for identity, row in sources.items():
        exact_fields(row, ('id', 'path', 'sha256', 'campaignIds'), f'Source {identity}')
        scope = row['campaignIds']
        if (not isinstance(scope, list) or not scope
                or any(not isinstance(cid, str) or cid not in campaign_ids for cid in scope)
                or len(scope) != len(set(scope))):
            raise ValueError('Source campaign scope must name distinct canonical campaigns')
        document = checked_archive(root, {key: row[key] for key in ('path', 'sha256')}, identity)
        checked_upstream_snapshots(root, document)
        result[identity] = {'path': row['path'], 'campaignIds': scope, 'document': document}
    return result


def checked_consultations(rows):
    consultations = unique_rows(rows, 'Consultations')
    fields = ('id', 'realIdentity', 'date', 'url', 'title', 'locator', 'access', 'readScope', 'finding', 'limits')
    for identity, row in consultations.items():
        exact_fields(row, fields, f'Consultation {identity}')
        for field in ('realIdentity', 'date', 'title', 'locator', 'readScope', 'limits'):
            text(row[field], f'Consultation {identity}/{field}')
        date = datetime.date.fromisoformat(row['date'])
        if date.isoformat() != row['date']:
            raise ValueError('Consultation date must use YYYY-MM-DD')
        https(row['url'], f'Consultation {identity}')
        if row['access'] not in ACCESS:
            raise ValueError('Unknown consultation access scope')
        if row['access'] in READABLE_ACCESS:
            text(row['finding'], f'Consultation {identity} finding')
        elif row['finding'] is not None:
            raise ValueError('Unavailable or metadata-only access cannot claim a consulted passage finding')
    return consultations


def validate_crosswalk(root, campaigns, data):
    """Return an honest coverage report; well-formed linkage is never historical approval."""
    exact_fields(data, ('schemaVersion', 'sources', 'consultations', 'bindings'), 'Crosswalk')
    if type(data['schemaVersion']) is not int or data['schemaVersion'] != 1:
        raise ValueError('Unsupported research crosswalk version')
    consultations = checked_consultations(data['consultations'])
    selected = {}
    summary = []
    for campaign in campaigns:
        cid = campaign['campaignId']
        if any(row['campaignId'] == cid for row in summary):
            raise ValueError('Duplicate canonical campaign')
        summary.append({'campaignId': cid, 'selected': len(campaign['episodeSelection']),
                        'linked': 0, 'architectChecks': 0, 'withPassageRead': 0,
                        'onlyUnavailableOrMetadata': 0, 'linkedWithoutArchitectCheck': 0})
        for episode in campaign['episodeSelection']:
            key = (cid, episode['id'])
            if key in selected:
                raise ValueError('Duplicate canonical selection')
            selected[key] = episode
    sources = checked_sources(root, data['sources'], {row['campaignId'] for row in summary})
    if not isinstance(data['bindings'], list):
        raise ValueError('Bindings must be a list')
    used_sources, used_consultations, seen = set(), set(), set()
    records = []
    fields = ('campaignId', 'scenarioId', 'selectionSha256', 'sourceId', 'recordPointer', 'architectCheck')
    archive_fields = ('sourceUrl', 'locator', 'consultationStatus', 'readScope', 'classification', 'cautions')
    for binding in data['bindings']:
        exact_fields(binding, fields, 'Binding')
        for field in ('campaignId', 'scenarioId', 'sourceId'):
            text(binding[field], f'Binding {field}')
        key = (binding['campaignId'], binding['scenarioId'])
        if key not in selected or key in seen:
            raise ValueError(f'Unknown or duplicate selection binding: {key}')
        seen.add(key)
        episode = selected[key]
        if binding['selectionSha256'] != selection_fingerprint(key[0], episode):
            raise ValueError(f'Stale canonical selection: {key}')
        source = sources.get(binding['sourceId'])
        if not source:
            raise ValueError('Binding refers to an unknown archived source')
        if key[0] not in source['campaignIds']:
            raise ValueError('Binding campaign is outside the archived source scope')
        used_sources.add(binding['sourceId'])
        record = record_at(source['document'], binding['recordPointer'])
        if not isinstance(record, dict) or record.get('id') != key[1]:
            raise ValueError(f'Archived record does not match the semantic scenario identity: {key}')
        for field in archive_fields:
            text(record.get(field), f'Archived {key}/{field}')
        https(record['sourceUrl'], 'Archived source URL')
        check = binding['architectCheck']
        reads = []
        if check is not None:
            exact_fields(check, ('consultationIds', 'scopeNote', 'corrections'), f'Architect check {key}')
            text(check['scopeNote'], 'Architect check scope')
            ids = check['consultationIds']
            if not isinstance(ids, list) or not ids or any(not isinstance(i, str) for i in ids) or len(ids) != len(set(ids)):
                raise ValueError('Architect check needs distinct consultation identities')
            for identity in ids:
                if identity not in consultations:
                    raise ValueError('Architect check refers to an unknown consultation')
                reads.append(consultations[identity])
                used_consultations.add(identity)
            if not isinstance(check['corrections'], list):
                raise ValueError('Architect corrections must be a list')
            for correction in check['corrections']:
                text(correction, 'Architect correction')
        count = next(row for row in summary if row['campaignId'] == key[0])
        count['linked'] += 1
        count['architectChecks'] += int(check is not None)
        count['withPassageRead'] += int(any(row['access'] in READABLE_ACCESS for row in reads))
        count['onlyUnavailableOrMetadata'] += int(bool(reads) and all(row['access'] not in READABLE_ACCESS for row in reads))
        count['linkedWithoutArchitectCheck'] += int(check is None)
        comparison = {
            'source URL': record['sourceUrl'] == episode['historicalSelection']['sourceUrl'],
            'locator': record['locator'] == episode['historicalSelection']['passage'],
            'date': record.get('dateInDesign') == episode['date'],
            'geography': record.get('placeInDesign') == episode['geographyId'],
        }
        records.append({'campaignId': key[0], 'scenarioId': key[1], 'order': episode['order'],
                        'archivePath': source['path'], 'pointer': binding['recordPointer'],
                        'declaredAccess': record['consultationStatus'], 'architectCheck': check,
                        'consultations': reads, 'differences': [name for name, equal in comparison.items() if not equal]})
    if used_sources != set(sources) or used_consultations != set(consultations):
        raise ValueError('Unused sources or consultations must not inflate crosswalk coverage')
    for row in summary:
        row['unlinked'] = row['selected'] - row['linked']
    return {'campaigns': summary, 'records': records}


def audit_crosswalk(root, campaigns, data):
    try:
        return [], validate_crosswalk(root, campaigns, data)
    except (ValueError, KeyError, TypeError, IndexError, OSError) as error:
        return [f'Research crosswalk: {error}'], None
