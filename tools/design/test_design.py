"""Adversarial tests for the high-impact geographic and design acceptance checks."""

import copy
import json
import runpy
import unittest
from unittest.mock import patch
import tempfile
import hashlib
import xml.etree.ElementTree as ET
from pathlib import Path
from geography import clip_segment, tile_point
from verify import ROOT, verify
from test_civic_difficulty_audit import CivicDifficultyAuditTests
from test_research_crosswalk import ResearchCrosswalkTests


class FulfillmentBridgeAcceptanceTests(unittest.TestCase):
    def test_bridge_fails_closed_when_bun_or_json_response_is_unavailable(self):
        helper = runpy.run_path(str(ROOT / "tools/design/fulfillment-dossier.helper.py"))
        with patch.object(helper["shutil"], "which", return_value=None):
            with self.assertRaisesRegex(RuntimeError, "Bun is required"):
                helper["project_batch"]([{"episodeId": "fixture.episode"}])

        completed = type("Completed", (), {"returncode": 0, "stdout": "not-json", "stderr": ""})()
        with patch.object(helper["shutil"], "which", return_value="/fixture/bun"), \
             patch.object(helper["subprocess"], "run", return_value=completed):
            with self.assertRaisesRegex(RuntimeError, "malformed JSON"):
                helper["project_batch"]([{"episodeId": "fixture.episode"}])

    def test_v3_auditor_dispatches_before_legacy_and_detects_derived_view_drift(self):
        validator = runpy.run_path(str(ROOT / "tools/design/episode_dossier.validator.py"))
        self.assertTrue(validator["audit_dossier"]({"id": "fixture", "designProfile": "future-profile"})[0]
                        .endswith("unsupported designProfile 'future-profile'"))
        episode = {
            "id": "fixture.episode",
            "designProfile": "alternative-fulfillment-v3",
            "referenceCapabilityProfile": {
                "schemaVersion": 3,
                "worldContract": {"entities": []},
                "objectivePlan": [],
                "stateMachine": {},
                "secondaryObjectives": [],
                "secondaryBudget": {},
                "fulfillmentPlan": {"services": []},
            },
            "worldContract": {"entities": [{"id": "drift"}]},
            "geographyId": "fixture.region",
            "mapPlan": {
                "terrainProfile": "fixture.region",
                "hubs": [{"id": "fixture.hub", "centre": [100, 100]}],
                "points": [{"id": "fixture.point", "tile": [120, 100]}],
            },
            "mapBindings": {
                "hubs": [{"id": "fixture.hub", "centre": [100, 100]}],
                "points": [{"pointId": "fixture.point", "tile": [120, 100]}],
            },
        }
        errors = validator["audit_dossier"](episode)
        self.assertTrue(any("derived worldContract differs" in error for error in errors))
        self.assertFalse(any("historical map" in error for error in errors))
        episode["mapBindings"]["points"][0]["tile"] = [121, 100]
        errors = validator["audit_dossier"](episode)
        self.assertTrue(any("projected point-zone bindings differ" in error for error in errors))


class DesignAcceptanceTests(unittest.TestCase):
    def test_main_counters_reject_empty_negative_fractional_and_boolean_thresholds(self):
        examples = {}
        for campaign in self.odysseys:
            for episode in campaign.get('episodes', []):
                for oi, objective in enumerate(episode['objectivePlan']):
                    for ri, requirement in enumerate(objective['predicate']['requirements']):
                        if 'requiredCount' in requirement:
                            examples.setdefault(requirement['kind'], (campaign, episode, oi, ri))
        self.assertEqual(set(examples), {
            'entity-state', 'current-entity-presence', 'checkpoint-entity-presence',
            'area-state', 'transport-journey',
        })
        for kind, (campaign, episode, oi, ri) in examples.items():
            self.assertEqual(self.dossier_validator(episode, campaign, self.catalogue['campaigns']), [])
            for value in (0, -1, True, False, 0.5, 1.0, None, '1', float('nan'), float('inf')):
                with self.subTest(kind=kind, value=value):
                    invalid = copy.deepcopy(episode)
                    invalid['objectivePlan'][oi]['predicate']['requirements'][ri]['requiredCount'] = value
                    errors = self.dossier_validator(invalid, campaign, self.catalogue['campaigns'])
                    self.assertTrue(any('counter must be a positive integer' in e for e in errors))
            invalid = copy.deepcopy(episode)
            del invalid['objectivePlan'][oi]['predicate']['requirements'][ri]['requiredCount']
            self.assertTrue(any('counter must be a positive integer' in e
                                for e in self.dossier_validator(invalid, campaign, self.catalogue['campaigns'])))

    def test_survival_and_ledger_minima_reject_malformed_counts_before_comparison(self):
        survivor_episode = next(
            e for c in self.odysseys for e in c.get('episodes', [])
            if e['worldContract']['survivorGroups']
        )
        ledger_episode = next(
            e for c in self.odysseys for e in c.get('episodes', [])
            if any(o['predicate'].get('exportedLedgers') for o in e['objectivePlan'])
        )
        for value in (0, -1, True, 0.5, None, '1'):
            with self.subTest(value=value):
                invalid = copy.deepcopy(survivor_episode)
                invalid['worldContract']['survivorGroups'][0]['minimumAliveOrAlreadySafe'] = value
                self.assertTrue(any('survival threshold must be a positive integer' in e
                                    for e in self.dossier_validator(invalid)))
                invalid = copy.deepcopy(ledger_episode)
                objective = next(o for o in invalid['objectivePlan'] if o['predicate'].get('exportedLedgers'))
                objective['predicate']['exportedLedgers'][0]['minimumCount'] = value
                self.assertTrue(any('ledger minimum must be a positive integer' in e
                                    for e in self.dossier_validator(invalid)))

    def test_empty_authored_collection_is_rejected_before_dossier_rendering(self):
        pipeline = runpy.run_path(str(ROOT / 'tools/design/episode_dossiers.script.py'))
        original_read = pipeline['read']

        def empty_collection(path):
            data = original_read(path)
            if path == 'docs/design/odysseys/faith-origins.json':
                data['episodeBlueprints'][0]['mainObjectives'][0]['requirements'][0]['requiredCount'] = 0
            return data

        with patch.dict(pipeline['run'].__globals__, {'read': empty_collection}):
            with self.assertRaisesRegex(ValueError, 'counter must be a positive integer'):
                pipeline['run'](check=True)

    def test_legacy_objectives_share_strict_count_validation(self):
        from objectives import check_objectives
        scenario = self.catalogue['campaigns'][0]['scenarios'][0]
        for field in ('requiredCount', 'distinctDestinationCount', 'minimumPerDestination'):
            for value in (0, -1, True, 0.5, '1', None):
                with self.subTest(field=field, value=value):
                    invalid = copy.deepcopy(scenario)
                    req = next(r for o in invalid['objectivePlan'] for r in o['predicate']['requirements']
                               if r['kind'] == 'entity-state')
                    req[field] = value
                    errors = []
                    check_objectives(invalid, lambda ok, message: errors.append(message) if not ok else None, 'legacy')
                    self.assertTrue(any('counter must be a positive integer' in e for e in errors))

    def test_optional_counts_are_strict_in_both_catalogue_and_expanded_dossiers(self):
        from secondary import check_optional_objectives
        catalogues = (
            [s for c in self.catalogue['campaigns'] for s in c['scenarios']],
            [e for c in self.odysseys for e in c.get('episodes', [])],
        )
        for candidates in catalogues:
            for kind in ('entity-arrival', 'visit-zones'):
                original = next(s for s in candidates if any(
                    r['kind'] == kind for o in s['secondaryObjectives'] for r in o['predicate']['requirements']))
                for value in (0, -1, True, 0.5, 1.0, None, '1'):
                    with self.subTest(scenario=original['id'], kind=kind, value=value):
                        invalid = copy.deepcopy(original)
                        req = next(r for o in invalid['secondaryObjectives'] for r in o['predicate']['requirements']
                                   if r['kind'] == kind)
                        req['requiredCount'] = value
                        errors = []
                        check_optional_objectives(invalid, lambda ok, message: errors.append(message) if not ok else None, 'side')
                        self.assertTrue(any('optional counter must be a positive integer' in e for e in errors))

    def test_conserved_payment_totals_cannot_hide_invalid_individual_allocations(self):
        from objectives import check_objectives
        originals = (self.catalogue['campaigns'][0]['scenarios'][0], self.draft(11))
        for original in originals:
            for value in (-1, True, 0.5, float('nan'), float('inf')):
                with self.subTest(scenario=original['id'], value=value):
                    invalid = copy.deepcopy(original)
                    req = next(r for o in invalid['objectivePlan'] for r in o['predicate']['requirements']
                               if r['kind'] == 'resource-transaction')
                    resource, total = next((k, v) for k, v in req['amounts'].items() if v > 0)
                    allocations = list(req['allocations'].values())
                    self.assertGreaterEqual(len(allocations), 2)
                    for row in allocations:
                        row[resource] = 0
                    allocations[0][resource], allocations[1][resource] = value, total - value
                    if original is originals[0]:
                        errors = []
                        check_objectives(invalid, lambda ok, message: errors.append(message) if not ok else None, 'legacy')
                    else:
                        errors = self.dossier_validator(invalid)
                    self.assertTrue(any('Resource amounts must be nonnegative integers' in e for e in errors))
            invalid = copy.deepcopy(original)
            req = next(r for o in invalid['objectivePlan'] for r in o['predicate']['requirements']
                       if r['kind'] == 'resource-transaction')
            req['amounts']['unknown'] = 999
            next(iter(req['allocations'].values()))['unknown'] = 999
            if original is originals[0]:
                errors = []
                check_objectives(invalid, lambda ok, message: errors.append(message) if not ok else None, 'legacy')
            else:
                errors = self.dossier_validator(invalid)
            self.assertTrue(any('Unknown resource' in e for e in errors))

    def test_legacy_stock_and_compound_totals_use_the_shared_resource_validator(self):
        from objectives import check_objectives
        scenario = next(s for c in self.catalogue['campaigns'] for s in c['scenarios']
                        if any(r['kind'] == 'minimum-stock' for o in s['objectivePlan']
                               for r in o['predicate']['requirements']))
        for target in ('stock', 'compound-total'):
            invalid = copy.deepcopy(scenario)
            if target == 'stock':
                req = next(r for o in invalid['objectivePlan'] for r in o['predicate']['requirements']
                           if r['kind'] == 'minimum-stock')
                req['amounts']['food'] = -1
            else:
                invalid['objectivePlan'][0]['predicate']['resourceAmounts']['unknown'] = 1
            errors = []
            check_objectives(invalid, lambda ok, message: errors.append(message) if not ok else None, 'legacy')
            self.assertTrue(any('Resource amounts must be nonnegative integers' in e or 'Unknown resource' in e
                                for e in errors))

    def test_optional_payments_rewards_and_budgets_reject_invalid_resource_vectors(self):
        from secondary import check_optional_objectives
        for value in (-1, True, 0.5, None, '1'):
            for target in ('payment', 'reward', 'stock', 'reserve'):
                with self.subTest(value=value, target=target):
                    invalid = self.draft()
                    if target == 'payment':
                        req = next(r for o in invalid['secondaryObjectives'] for r in o['predicate']['requirements']
                                   if r['kind'] == 'atomic-payment')
                        req['resources']['wood'] = value
                    elif target == 'reward':
                        invalid['secondaryObjectives'][0]['effects'][0]['resources']['food'] = value
                    elif target == 'stock':
                        invalid['difficulty']['hard']['startingResources']['food'] = value
                    else:
                        invalid['secondaryBudget']['reservedRewards']['food'] = value
                    errors = []
                    check_optional_objectives(invalid, lambda ok, message: errors.append(message) if not ok else None, 'side')
                    self.assertTrue(any('Resource amounts must be nonnegative integers' in e for e in errors))

    def test_source_crosswalk_claims_cannot_bypass_global_documentation_gate(self):
        original_read = Path.read_text

        def false_approval(path, *args, **kwargs):
            text = original_read(path, *args, **kwargs)
            if path == ROOT / 'docs/research/odyssey-research/source-consultation-crosswalk.json':
                data = json.loads(text)
                data['historicalApproval'] = True
                return json.dumps(data)
            return text

        with patch.object(Path, 'read_text', false_approval):
            errors, counts = verify()
        self.assertTrue(any('Research crosswalk:' in error for error in errors))
        self.assertEqual(counts['expandedApprovedDossiers'], 0)

    def test_scope_prose_cannot_disable_expanded_assignment_and_voice_audits(self):
        original_read = Path.read_text

        def altered_read(path, *args, **kwargs):
            text = original_read(path, *args, **kwargs)
            if path == ROOT / 'docs/design/assignments.json':
                data = json.loads(text)
                data['scope'] = 'future editorial target; arbitrary prose'
                data['assignments'][0]['episodeSlices'][0]['sliceId'] = 'S99999'
                return json.dumps(data)
            if path == ROOT / 'docs/design/voices/odyssey-narrators.json':
                data = json.loads(text)
                data['narrators'][0]['episodeKnowledgePlan'][0]['scenarioId'] = 'absent'
                return json.dumps(data)
            return text

        with patch.object(Path, 'read_text', altered_read):
            errors, counts = verify()
        self.assertTrue(any('proposal identity/order diverges' in e for e in errors))
        self.assertTrue(any('knowledge plan scenarioId drift' in e for e in errors))
        self.assertEqual(counts['expandedSelectedEpisodes'], sum(
            len(campaign['episodeSelection']) for campaign in self.odysseys))

    def test_invalid_authored_observation_hubs_never_fall_back_to_default_sites(self):
        from secondary import build_optional_objectives
        campaign = json.loads((ROOT / 'docs/design/odysseys/imperial-church.json').read_text())
        episode = next(e for e in campaign['episodes'] if e['order'] == 26)
        task = copy.deepcopy(next(b for b in campaign['episodeBlueprints']
                                  if b['order'] == 26)['optionalTasks'][0])
        task['placement']['observationHubs'] = ['hub-3', 'hub-4']
        valid = build_optional_objectives(episode, [task])[0]
        self.assertEqual([zone['hub'] for zone in valid['world']['zones']], ['hub-3', 'hub-4'])
        for invalid in ([], None, '', ['hub-3'], ['absent', 'hub-4'], [7, 'hub-4']):
            with self.subTest(hubs=invalid):
                task['placement']['observationHubs'] = invalid
                with self.assertRaisesRegex(ValueError, 'one hub per scout/watch zone'):
                    build_optional_objectives(episode, [task])

    def test_authored_side_actor_offsets_separate_shared_origin_actors(self):
        from secondary import build_optional_objectives
        campaign = json.loads((ROOT / 'docs/design/odysseys/imperial-church.json').read_text())
        episode = next(e for e in campaign['episodes'] if e['order'] == 26)
        task = copy.deepcopy(next(b for b in campaign['episodeBlueprints']
                                  if b['order'] == 26)['optionalTasks'][-1])
        task['placement']['entityOffsetsTiles'] = [[-10, -6]]
        side = build_optional_objectives(episode, [task])[0]
        self.assertEqual(side['world']['entities'][0]['offsetTiles'], [-10, -6])
        self.assertNotEqual(side['world']['entities'][0]['offsetTiles'], [-6, 3])
        self.assertEqual(side['effects'][0]['kind'], 'mark-alternative-route')
        for invalid in ([], [[float('nan'), 0]], [[1, 2], [3, 4]], [[True, 0]]):
            with self.subTest(offsets=invalid):
                task['placement']['entityOffsetsTiles'] = invalid
                with self.assertRaisesRegex(ValueError, 'finite coordinate pair per identity'):
                    build_optional_objectives(episode, [task])

    def test_optional_authored_placement_never_silently_uses_defaults(self):
        from secondary import build_optional_objectives
        campaign = json.loads((ROOT / 'docs/design/odysseys/imperial-church.json').read_text())
        episode = next(e for e in campaign['episodes'] if e['order'] == 25)
        task = copy.deepcopy(next(b for b in campaign['episodeBlueprints']
                                  if b['order'] == 25)['optionalTasks'][0])
        for bad in ({'hub': 'hub-7'}, {'originHub': 'hub-7', 'offsetTiles': [21, -17]}):
            with self.subTest(placement=bad):
                task['placement'] = bad
                with self.assertRaisesRegex(ValueError, 'Unknown optional placement fields'):
                    build_optional_objectives(episode, [task])

    def test_optional_editorial_instruction_keeps_funded_benefit(self):
        from secondary import objective_text
        subject = {'en': 'local household yard', 'es-ES': 'patio de hogares locales'}
        text = objective_text('aid', subject, {'food': 100, 'wood': 50},
                              instruction={'en': 'Take the two original crates to their separate hosts.',
                                           'es-ES': 'Lleva las dos cajas originales a sus anfitriones separados.'})
        self.assertTrue(text['en'].startswith('Take the two original crates'))
        self.assertTrue(text['en'].endswith('Benefit: 100 food, 50 wood, once.'))
        self.assertTrue(text['es-ES'].endswith('Ventaja: 100 de alimento, 50 de madera, una vez.'))
        for invalid in ({'en': 'Only English'}, {'en': '', 'es-ES': 'Texto'}):
            with self.subTest(instruction=invalid):
                with self.assertRaisesRegex(ValueError, 'nonempty English and Spanish'):
                    objective_text('aid', subject, {}, instruction=invalid)

    def journey_draft(self):
        return self.imperial_draft(8)

    def test_water_journeys_keep_shared_capacity_and_unimplemented_gate(self):
        draft = self.journey_draft()
        self.assertEqual(self.imperial_errors(draft), [])
        draft["transportPlan"]["sharedManifestAuthority"] = False
        self.assertTrue(any("unimplemented capability gate" in e for e in self.imperial_errors(draft)))
        draft = self.journey_draft()
        draft["transportPlan"]["implementationStatus"] = "native-implemented"
        self.assertTrue(any("unimplemented capability gate" in e for e in self.imperial_errors(draft)))
        draft = self.journey_draft()
        draft["requiredCapabilities"] = [c for c in draft["requiredCapabilities"]
                                        if c["id"] != "manifest-backed-water-journeys"]
        self.assertTrue(any("unimplemented capability gate" in e for e in self.imperial_errors(draft)))

    def test_water_journeys_reject_land_routes_wrong_shores_and_stale_receipts(self):
        for change in ("land", "wrong-shore", "wrong-passenger", "future"):
            with self.subTest(change=change):
                draft = self.journey_draft()
                journey = draft["objectivePlan"][1]["predicate"]["requirements"][0]
                if change == "land":
                    next(c for c in draft["mapPlan"]["corridors"] if c["id"] == "lower-ferry")["mode"] = "land"
                elif change == "wrong-shore":
                    journey["destinationZone"] = journey["originZone"]
                elif change == "wrong-passenger":
                    journey["readyReceipt"]["requirement"] = "req-3"
                else:
                    journey["readyReceipt"]["objective"] = "o3"
                self.assertTrue(any("journey" in e for e in self.imperial_errors(draft)))

    def test_water_journeys_reject_missing_steps_duplicate_actors_and_empty_capacity(self):
        for change in ("transit", "identity", "duplicate", "passenger-as-carrier", "capacity"):
            with self.subTest(change=change):
                draft = self.journey_draft()
                journey = draft["objectivePlan"][1]["predicate"]["requirements"][0]
                if change == "transit":
                    journey["eventOrder"].remove("water-transit")
                elif change == "identity":
                    journey["proofPolicy"]["sameCarrierWithinJourney"] = False
                elif change == "duplicate":
                    journey["entities"].append(journey["entities"][0])
                elif change == "passenger-as-carrier":
                    journey["carriers"][0] = journey["entities"][0]
                else:
                    draft["transportPlan"]["capacityByCarrier"][journey["carriers"][0]] = 0
                self.assertTrue(any("journey" in e or "carrier capacity" in e
                                    for e in self.imperial_errors(draft)))

    def test_chrysopolis_optionals_stay_on_the_authored_european_bank(self):
        draft = self.imperial_draft(9)
        self.assertEqual(self.imperial_errors(draft), [])
        for side in draft["secondaryObjectives"]:
            self.assertEqual(side["reachability"]["corridorIds"], ["west-support"])
            self.assertTrue(all(e["initialHub"] == "hub-1" for e in side["world"]["entities"]))
            self.assertTrue(all(z["hub"] in {"hub-1", "hub-7"} for z in side["world"]["zones"]))
        draft["secondaryObjectives"][0]["world"]["zones"][0]["hub"] = "absent"
        self.assertTrue(any("undefined side hub" in e for e in self.imperial_errors(draft)))

    def test_authored_chronology_rejects_post_victory_correspondence_before_war(self):
        helper = runpy.run_path(str(ROOT / 'tools/design/odyssey_catalog.helper.py'))
        policy, campaigns = helper['odyssey_catalog']()
        self.assertEqual(helper['audit_selections'](policy, campaigns), [])
        imperial = next(c for c in campaigns if c['campaignId'] == 'imperial-church')
        by_id = {e['id']: e for e in imperial['episodeSelection']}
        before = by_id['10-land-and-strait-logistics-chrysopolis']
        after = by_id['08-disputed-correspondence-alexandria']
        before['order'], after['order'] = after['order'], before['order']
        imperial['episodeSelection'].sort(key=lambda e: e['order'])
        self.assertTrue(any('chronology constraint violated' in e
                            for e in helper['audit_selections'](policy, campaigns)))
        imperial['chronologyConstraints'][0]['before'] = 'absent'
        self.assertTrue(any('absent ->' in e
                            for e in helper['audit_selections'](policy, campaigns)))

    def imperial_draft(self, order=1):
        return copy.deepcopy(next(e for e in self.odysseys[1]["episodes"] if e["order"] == order))

    def imperial_errors(self, draft):
        return self.dossier_validator(draft, self.odysseys[1], self.catalogue["campaigns"])

    def test_live_presence_cannot_be_replaced_with_historical_arrival(self):
        draft = self.imperial_draft(22)
        self.assertEqual(self.imperial_errors(draft), [])
        requirement = draft["objectivePlan"][2]["predicate"]["requirements"][2]
        requirement.update(kind="entity-state", state="arrived")
        self.assertTrue(any("current presence replaced with delivery history" in e
                            for e in self.imperial_errors(draft)))

    def test_live_presence_rejects_false_support_and_invalid_assignments(self):
        for change in ("native", "missing-capability", "missing-zone", "duplicate", "ledger"):
            with self.subTest(change=change):
                draft = self.imperial_draft(22)
                requirement = draft["objectivePlan"][2]["predicate"]["requirements"][2]
                if change == "native":
                    requirement["implementationStatus"] = "native-implemented"
                elif change == "missing-capability":
                    draft["requiredCapabilities"] = [c for c in draft["requiredCapabilities"]
                                                     if c["id"] != "live-entity-presence"]
                elif change == "missing-zone":
                    requirement["destinations"] = {}
                elif change == "duplicate":
                    requirement["entities"].append(requirement["entities"][0])
                else:
                    requirement["deliveryLedgerSubstitute"] = True
                self.assertTrue(any("current presence" in e
                                    for e in self.imperial_errors(draft)))

    def test_entry_requires_first_episode_and_canonical_predecessor(self):
        draft = self.imperial_draft()
        self.assertEqual(self.imperial_errors(draft), [])
        self.assertTrue(any("canonical campaign context" in e for e in self.dossier_validator(draft)))
        draft.pop("entryContract")
        self.assertTrue(any("needs a predecessor entry" in e for e in self.imperial_errors(draft)))
        draft = self.imperial_draft(2)
        draft["entryContract"] = self.imperial_draft()["entryContract"]
        self.assertTrue(any("first episode" in e for e in self.imperial_errors(draft)))
        draft = self.imperial_draft()
        draft["entryContract"]["predecessors"][0]["progressKey"] = "progress.other.done"
        self.assertTrue(any("unsafe entry predecessor" in e for e in self.imperial_errors(draft)))

    def test_entry_rejects_hard_gates_progress_writes_and_missing_localization(self):
        for field, value in [("enforcePrerequisite", True), ("proceedWithoutPredecessor", False),
                             ("recapAvailableAlways", False), ("writesProgress", True)]:
            with self.subTest(field=field):
                draft = self.imperial_draft()
                draft["entryContract"][field] = value
                self.assertTrue(any("unsafe entry predecessor" in e for e in self.imperial_errors(draft)))
        draft = self.imperial_draft()
        del draft["entryContract"]["recap"]["es-ES"]
        self.assertTrue(any("incomplete entry localization" in e for e in self.imperial_errors(draft)))
        draft = self.imperial_draft()
        next(s for s in draft["screens"] if s["id"].startswith("recommended-"))["condition"] = "block start until predecessor"
        self.assertTrue(any("incorrect entry screen" in e for e in self.imperial_errors(draft)))

    def test_continuous_control_cannot_end_in_its_own_or_a_past_objective(self):
        for target in ("o1", "o2", "absent"):
            draft = self.imperial_draft()
            draft["objectivePlan"][1]["predicate"]["requirements"][0]["mustRemainUntilObjective"] = target
            self.assertTrue(any("invalid continuous control interval" in e for e in self.imperial_errors(draft)))
        draft = self.imperial_draft()
        draft["objectivePlan"][1]["predicate"]["requirements"][0]["state"] = "visited-and-passable"
        self.assertTrue(any("invalid continuous control interval" in e for e in self.imperial_errors(draft)))

    def test_mandatory_guards_are_instantiated_in_every_difficulty_roster(self):
        draft = self.imperial_draft()
        blockers = draft["objectivePlan"][1]["predicate"]["requirements"][0]["blockingEnemies"]
        self.assertEqual(len(blockers), 6)
        for level in ("easy", "standard", "hard"):
            self.assertTrue(set(blockers) <= set(draft["oppositionPlan"]["byDifficulty"][level]["initialEntityIds"]))
            invalid = copy.deepcopy(draft)
            roster = invalid["oppositionPlan"]["byDifficulty"][level]["initialEntityIds"]
            roster.remove(blockers[0])
            invalid["difficulty"][level]["enemyTotalCap"] -= 1
            self.assertTrue(any("mandatory blocker not instantiated" in e for e in self.imperial_errors(invalid)))

    def finale_errors(self, draft):
        return self.dossier_validator(draft, self.odysseys[0], self.catalogue["campaigns"])

    def test_finale_requires_canonical_last_episode_and_complete_choice(self):
        draft = self.draft(30)
        self.assertEqual(self.finale_errors(draft), [])
        self.assertTrue(any("canonical campaign context" in error for error in self.dossier_validator(draft)))
        draft["id"] = self.draft(29)["id"]
        draft["order"] = 29
        self.assertTrue(any("intermediate episode" in error for error in self.finale_errors(draft)))
        draft = self.draft(30)
        draft.pop("finaleContract")
        self.assertTrue(any("needs a finale contract" in error for error in self.finale_errors(draft)))

    def test_finale_rejects_progress_erasure_defeat_writes_and_automatic_launch(self):
        for section, field, value in [
            ("victoryCommit", "resetOtherKeys", True),
            ("victoryCommit", "preserveOtherKeys", False),
            ("victoryCommit", "onDefeat", "write chosen key"),
            ("selectionPolicy", "writesProgress", True),
            ("recommendationPolicy", "autoLaunch", True),
            ("recommendationPolicy", "enforcePrerequisite", True),
        ]:
            with self.subTest(field=field):
                draft = self.draft(30)
                draft["finaleContract"][section][field] = value
                self.assertTrue(any("unsafe finale" in error for error in self.finale_errors(draft)))

    def test_finale_rejects_wrong_successor_namespace_and_skipped_selection(self):
        for field, value in [("progressKey", "progress.other.completed"), ("successor", None)]:
            draft = self.draft(30)
            draft["finaleContract"]["routeChoices"][0][field] = value
            self.assertTrue(any("unsafe finale" in error for error in self.finale_errors(draft)))
        draft = self.draft(30)
        draft["stateMachine"]["phaseTransitions"][-2]["to"] = "victory"
        self.assertTrue(any("bypasses pending route" in error for error in self.finale_errors(draft)))
        draft = self.draft(30)
        draft["finaleContract"]["routeChoices"].pop()
        self.assertTrue(any("every canonical route" in error for error in self.finale_errors(draft)))

    def test_finale_rejects_missing_spanish_or_wrong_successor_screen(self):
        draft = self.draft(30)
        del draft["finaleContract"]["choicePrompt"]["es-ES"]
        self.assertTrue(any("finale localization" in error for error in self.finale_errors(draft)))
        draft = self.draft(30)
        del draft["finaleContract"]["routeChoices"][0]["chronologyWarning"]["es-ES"]
        self.assertTrue(any("finale localization" in error for error in self.finale_errors(draft)))
        draft = self.draft(30)
        screen = next(s for s in draft["screens"] if s["id"] == "next-campaign-jewish-perspective")
        screen["text"]["en"] = "Start an unrelated campaign automatically."
        self.assertTrue(any("incorrect finale screen" in error for error in self.finale_errors(draft)))

    def test_departure_cannot_use_a_future_receipt_or_arrival_of_different_actors(self):
        draft = self.draft(21)
        departure = draft["objectivePlan"][3]["predicate"]["requirements"][0]
        departure["receiptObjective"] = "o4"
        self.assertTrue(
            any(
                "departure is not gated by a prior receipt" in e
                for e in self.dossier_validator(draft)
            )
        )
        draft = self.draft(21)
        onward = draft["objectivePlan"][3]["predicate"]["requirements"][1]
        onward["arrivalAfterDeparture"] = {"objective": "o2", "requirement": "req-1"}
        self.assertTrue(
            any(
                "arrival lacks exact prior departing identities" in e
                for e in self.dossier_validator(draft)
            )
        )

    def test_expanded_information_cannot_reference_invented_routes_or_enemy_reserves(
        self,
    ):
        draft = self.draft(19)
        guide = next(s for s in draft["secondaryObjectives"] if s["kind"] == "guide")
        guide["effects"][0]["corridorId"] = "imaginary-route"
        guide["reachability"]["corridorIds"] = ["imaginary-route"]
        errors = self.dossier_validator(draft)
        self.assertTrue(any("undefined information corridor" in e for e in errors))
        self.assertTrue(any("undefined optional access corridor" in e for e in errors))
        guide["effects"][0]["kind"] = "reveal-enemy-approach"
        guide["effects"][0]["rosterIds"] = ["uncreated-wave"]
        self.assertTrue(
            any(
                "undeclared enemy reserve information" in e
                for e in self.dossier_validator(draft)
            )
        )

    def test_evacuation_rejects_unbound_or_reproducing_opposition_and_impossible_route_count(
        self,
    ):
        draft = self.draft(17)
        draft["oppositionPlan"]["byDifficulty"]["hard"]["initialEntityIds"][0] = (
            "absent-enemy"
        )
        draft["oppositionPlan"]["byDifficulty"]["standard"]["productionEnabled"] = True
        route = draft["objectivePlan"][1]["predicate"]["requirements"][1]
        route["requiredCount"] = 3
        errors = self.dossier_validator(draft)
        self.assertTrue(
            any("undefined or duplicate hostile identity" in e for e in errors)
        )
        self.assertTrue(
            any("finite opposition count or production drift" in e for e in errors)
        )
        self.assertTrue(any("impossible route observation" in e for e in errors))

    def test_map_diagram_preserves_two_hosting_branches_and_their_actual_final_district(
        self,
    ):
        episode = self.draft(19)
        renderer = runpy.run_path(
            str(ROOT / "tools/design/episode_dossiers.script.py")
        )["diagram"]
        svg = ET.fromstring(renderer(episode, []))
        paths = {
            node.attrib["data-corridor"]: node.attrib["points"].split()
            for node in svg.iter()
            if "data-corridor" in node.attrib
        }
        self.assertEqual(
            set(paths), {"north-host-road", "east-host-road", "hosting-relief"}
        )
        self.assertEqual(len(paths["north-host-road"]), 3)
        self.assertEqual(len(paths["east-host-road"]), 3)
        self.assertEqual(paths["north-host-road"][-1], paths["east-host-road"][-1])
        self.assertNotEqual(paths["north-host-road"][0], paths["east-host-road"][0])
        self.assertEqual(len(paths["hosting-relief"]), 2)

    def test_derivation_cannot_use_a_smaller_or_future_payment_receipt(self):
        draft = self.draft(9)
        requirement = draft["objectivePlan"][1]["predicate"]["requirements"][1]
        requirement["requiredPaymentReceipts"][0]["amounts"]["wood"] = 1
        self.assertTrue(
            any(
                "derived payment receipt amount or owner drift" in error
                for error in self.dossier_validator(draft)
            )
        )
        draft = self.draft(9)
        payment = draft["objectivePlan"][1]["predicate"]["requirements"].pop(0)
        payment["id"] = "future-production-payment"
        draft["objectivePlan"][2]["predicate"]["requirements"].append(payment)
        receipt = draft["objectivePlan"][1]["predicate"]["requirements"][0][
            "requiredPaymentReceipts"
        ][0]
        receipt["fromObjective"] = "o3"
        self.assertTrue(
            any(
                "derived payment comes from a future objective" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_expanded_persona_cannot_change_identity_or_become_historical_evidence(
        self,
    ):
        voices = json.loads(
            (ROOT / "docs/design/voices/odyssey-narrators.json").read_text()
        )
        voices["narrators"][0]["id"] = "historical-eye-witness"
        voices["narrators"][0]["episodeKnowledgePlan"][0]["biographyIsEvidence"] = True
        audit = runpy.run_path(
            str(ROOT / "tools/design/odyssey_narrators.validator.py")
        )["audit_narrators"]
        errors = audit(voices, self.odysseys)
        self.assertTrue(any("identity differs" in error for error in errors))
        self.assertTrue(
            any("became historical witness evidence" in error for error in errors)
        )

    def test_expanded_persona_rejects_wrong_lifespan_and_missing_emotional_act(self):
        voices = json.loads(
            (ROOT / "docs/design/voices/odyssey-narrators.json").read_text()
        )
        voices["narrators"][0]["deathYearApprox"] = 200
        voices["narrators"][0]["fiveActEmotionalArc"].pop()
        audit = runpy.run_path(
            str(ROOT / "tools/design/odyssey_narrators.validator.py")
        )["audit_narrators"]
        errors = audit(voices, self.odysseys)
        self.assertTrue(any("invalid narrator lifespan" in error for error in errors))
        self.assertTrue(any("five ordered acts" in error for error in errors))

    def test_marcus_cannot_inherit_legacy_eyewitness_or_mismatched_episode(self):
        voices = json.loads(
            (ROOT / "docs/design/voices/odyssey-narrators.json").read_text()
        )
        marcus = next(
            row for row in voices["narrators"] if row["campaignId"] == "imperial-church"
        )
        marcus["episodeKnowledgePlan"][0]["mode"] = (
            "fictional-local-life-plus-received-reports"
        )
        marcus["episodeKnowledgePlan"][0]["scenarioId"] = "some-other-episode"
        audit = runpy.run_path(
            str(ROOT / "tools/design/odyssey_narrators.validator.py")
        )["audit_narrators"]
        errors = audit(voices, self.odysseys)
        self.assertTrue(any("Marcus cannot remember" in error for error in errors))
        self.assertTrue(
            any("knowledge plan scenarioId drift" in error for error in errors)
        )

    @staticmethod
    def authoring_graph(parallel=False):
        dependencies = {
            "S1": [], "S2": ["S1"], "S3": ["S2"],
            "S7": ["S2"] if parallel else ["S3"],
            "S8": ["S2"] if parallel else ["S7"],
            "S6": ["S3", "S7", "S8"] if parallel else ["S8"],
        }
        return {sid: "- **DependsOn**: [" + ", ".join(deps) + "]\n"
                for sid, deps in dependencies.items()}

    @staticmethod
    def audit_authoring_graph(slices):
        audit = runpy.run_path(str(ROOT / "tools/design/odyssey_assignments.validator.py"))[
            "audit_authoring_dependencies"]
        return audit(slices, ["S3", "S7", "S8"], "S6")

    def test_authoring_dependencies_accept_serial_parallel_and_mixed_work(self):
        for parallel in (False, True):
            self.assertEqual(self.audit_authoring_graph(self.authoring_graph(parallel)), [])
        mixed = self.authoring_graph(True)
        mixed["S8"] = "- **DependsOn**: [S7]\n"
        mixed["S6"] = "- **DependsOn**: [S3, S8]\n"
        self.assertEqual(self.audit_authoring_graph(mixed), [])

    def test_authoring_promotion_must_await_every_parallel_episode(self):
        for omitted in ("S3", "S7", "S8"):
            with self.subTest(omitted=omitted):
                graph = self.authoring_graph(True)
                graph["S6"] = "- **DependsOn**: [" + ", ".join(
                    sid for sid in ("S3", "S7", "S8") if sid != omitted) + "]\n"
                self.assertTrue(any("promotion precedes" in e for e in self.audit_authoring_graph(graph)))

    def test_authoring_dependencies_reject_cycles_unknown_and_duplicate_edges(self):
        mutations = {
            "cycle": ("S7", "- **DependsOn**: [S8]\n"),
            "unknown dependency": ("S3", "- **DependsOn**: [S99]\n"),
            "duplicate dependency": ("S3", "- **DependsOn**: [S2, S2]\n"),
        }
        for expected, (sid, body) in mutations.items():
            with self.subTest(expected=expected):
                graph = self.authoring_graph()
                graph[sid] = body
                self.assertTrue(any(expected in e for e in self.audit_authoring_graph(graph)))
        graph = self.authoring_graph(True)
        graph["S3"] = "- **DependsOn**: [S3, S2]\n"
        self.assertTrue(any("cycle" in e for e in self.audit_authoring_graph(graph)))

    def test_authoring_dependencies_reject_missing_metadata_and_malformed_fields(self):
        for body in ("", "- **DependsOn**: [S1]\n", "- **DependsOn**: []\n"):
            graph = self.authoring_graph(True)
            graph["S7"] = body
            self.assertTrue(any("bypasses shared metadata" in e for e in self.audit_authoring_graph(graph)))
        for body in ("- **DependsOn**: S2\n", "- **DependsOn**: [S2] trailing\n",
                     "- **DependsOn**: [S2]\n- **DependsOn**: [S1]\n"):
            graph = self.authoring_graph(True)
            graph["S3"] = body
            self.assertTrue(any("malformed" in e for e in self.audit_authoring_graph(graph)))
        for sid, body in (("S1", "- **DependsOn**: [S3]\n"),
                          ("S2", "- **DependsOn**: []\n")):
            graph = self.authoring_graph(True)
            graph[sid] = body
            self.assertTrue(any("metadata: S1" in e for e in self.audit_authoring_graph(graph)))

    def test_odyssey_assignments_reject_shared_slice_and_early_promotion(self):
        assignments = json.loads((ROOT / "docs/design/assignments.json").read_text())
        invalid = copy.deepcopy(assignments)
        row = invalid["assignments"][0]
        row["episodeSlices"][1]["sliceId"] = row["episodeSlices"][0]["sliceId"]
        row["promotionSlice"] = row["episodeSlices"][0]["sliceId"]
        audit = runpy.run_path(
            str(ROOT / "tools/design/odyssey_assignments.validator.py")
        )["audit_assignments"]
        errors = audit(ROOT, self.odysseys, invalid)
        self.assertTrue(any("share one authoring slice" in error for error in errors))
        self.assertTrue(any("promotion precedes" in error for error in errors))

    def test_odyssey_status_rejects_false_approval_and_stale_artifact_coverage(self):
        assignments = json.loads((ROOT / "docs/design/assignments.json").read_text())
        audit = runpy.run_path(str(ROOT / "tools/design/odyssey_assignments.validator.py"))["audit_assignments"]
        self.assertEqual(audit(ROOT, self.odysseys, assignments), [])
        for status in ("approved-complete-dossier", "selection only"):
            with self.subTest(status=status):
                invalid = copy.deepcopy(assignments)
                invalid["assignments"][0]["episodeSlices"][0]["dossierStatus"] = status
                self.assertTrue(any("dossier status diverges" in error for error in audit(ROOT, self.odysseys, invalid)))
        missing = copy.deepcopy(self.odysseys)
        missing[0]["episodes"] = []
        self.assertTrue(any("dossier status diverges" in error for error in audit(ROOT, missing, assignments)))

    def test_clipped_geographic_layer_keeps_crossing_without_interior_vertices(self):
        helper = runpy.run_path(str(ROOT / "tools/design/geographic_layers.helper.py"))
        layer = {
            "features": [
                {
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[-2, 0.5], [2, 0.5]],
                    }
                },
                {"geometry": {"type": "LineString", "coordinates": [[-2, 2], [2, 2]]}},
            ]
        }
        segments = helper["clipped_tile_segments"](
            helper["index_layer"](layer), [0, 0, 1, 1], 320
        )
        self.assertEqual(
            segments,
            [
                [
                    tile_point([0, 0, 1, 1], [0, 0.5], 320),
                    tile_point([0, 0, 1, 1], [1, 0.5], 320),
                ]
            ],
        )

    def test_geographic_padding_is_clipped_without_rescaling_existing_controls(self):
        helper = runpy.run_path(str(ROOT / "tools/design/geographic_layers.helper.py"))
        frame = runpy.run_path(str(ROOT / "tools/map/geographic_frame.helper.py"))["make_frame"]([0, 0, 1, 1], 400)
        coordinates = [[-0.05, 0.5], [-0.01, 0.5]]
        indexed = helper["index_layer"]({"features": [{"geometry": {"type": "LineString", "coordinates": coordinates}}]})
        self.assertEqual(helper["clipped_tile_segments"](indexed, [0, 0, 1, 1], 400), [])
        self.assertEqual(helper["clipped_tile_segments"](indexed, [0, 0, 1, 1], 400,
                                                        clip_bbox=frame.bounds_at(0, 399)),
                         [[tile_point([0, 0, 1, 1], point, 400) for point in coordinates]])
        crossing = helper["index_layer"]({"features": [{"geometry": {"type": "LineString", "coordinates": [[-2, 0.5], [2, 0.5]]}}]})
        self.assertEqual(helper["clipped_tile_segments"](crossing, [0, 0, 1, 1], 400,
                                                        clip_bbox=frame.bounds_at(0, 399)),
                         [[[0.0, 199.5], [399.0, 199.5]]])

    def test_exact_clip_keeps_a_vertical_line_position_and_legacy_rounding(self):
        exact = clip_segment([0.123456789, -1], [0.123456789, 2], [0, 0, 1, 1], precision=None)
        self.assertEqual(exact, [[0.123456789, 0.0], [0.123456789, 1.0]])
        self.assertEqual(clip_segment([0.123456789, -1], [0.123456789, 2], [0, 0, 1, 1]),
                         [[0.123457, 0.0], [0.123457, 1.0]])

    def test_expanded_captions_cannot_drop_historical_qualification(self):
        draft = self.draft()
        draft["screens"][1]["captionSegments"]["en"] = ["An invented certainty"]
        self.assertTrue(
            any(
                "caption content lost" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_research_reference_rejects_hash_drift_and_external_path_without_reading_it(
        self,
    ):
        audit = runpy.run_path(
            str(ROOT / "tools/design/research_references.validator.py")
        )["audit_references"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data.json").write_text("{}")
            asset = {
                "id": "fixture",
                "path": "data.json",
                "bytes": 2,
                "sha256": hashlib.sha256(b"{}").hexdigest(),
                "license": "Public domain",
                "author": "Fixture",
                "sourcePage": "https://example.org/fixture",
                "productionApproved": False,
            }
            self.assertEqual(audit(root, {"assets": [asset]}), [])
            (root / "data.json").write_text("[]")
            self.assertTrue(
                any("hash drift" in error for error in audit(root, {"assets": [asset]}))
            )
            asset["path"] = "../outside.json"
            self.assertEqual(
                audit(root, {"assets": [asset]}), ["Unsafe reference path: fixture"]
            )

    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((ROOT / "docs/design/catalog.json").read_text())
        cls.odyssey_helper = runpy.run_path(
            str(ROOT / "tools/design/odyssey_catalog.helper.py")
        )
        cls.odyssey_policy, cls.odysseys = cls.odyssey_helper["odyssey_catalog"]()
        cls.dossier_validator = staticmethod(
            runpy.run_path(str(ROOT / "tools/design/episode_dossier.validator.py"))[
                "audit_dossier"
            ]
        )

    def draft(self, order=1):
        return copy.deepcopy(
            next(e for e in self.odysseys[0]["episodes"] if e["order"] == order)
        )

    def test_playstyles_cannot_reference_missing_or_duplicate_optional_tasks(self):
        draft = self.draft()
        draft["playstyles"][0]["optionalObjectives"] = ["side-missing"]
        draft["playstyles"][2]["optionalObjectives"] = copy.deepcopy(
            draft["playstyles"][1]["optionalObjectives"]
        )
        errors = self.dossier_validator(draft)
        self.assertTrue(any("invalid playstyle portfolio" in error for error in errors))
        self.assertTrue(
            any("repeated playstyle portfolio" in error for error in errors)
        )

    def test_expanded_dossiers_reject_wrong_narrator_and_incomplete_translation(self):
        draft = self.draft()
        draft["screens"][1]["narrator"] = "miriam-archive"
        del draft["screens"][3]["text"]["es-ES"]
        errors = self.dossier_validator(draft)
        self.assertTrue(any("narrator voice" in error for error in errors))
        self.assertTrue(any("incomplete localization" in error for error in errors))

    def test_expanded_dossiers_reject_impossible_arrival_and_duplicate_survivors(self):
        draft = self.draft(2)
        draft["objectivePlan"][0]["predicate"]["requirements"][0]["requiredCount"] = 9
        draft["worldContract"]["survivorGroups"][0]["entities"].append(
            draft["worldContract"]["survivorGroups"][0]["entities"][0]
        )
        errors = self.dossier_validator(draft)
        self.assertTrue(any("impossible counter" in error for error in errors))
        self.assertTrue(any("duplicate survivor" in error for error in errors))

    def test_checkpoint_presence_requires_i00006_gate_and_cannot_be_terminal(self):
        draft = self.draft(2)
        objective = draft["objectivePlan"][1]
        entity = next(iter(draft["worldContract"]["entities"]))["id"]
        zone = next(iter(draft["worldContract"]["zones"]))["id"]
        requirement = {
            "id": "checkpoint-test",
            "kind": "checkpoint-entity-presence",
            "entities": [entity],
            "destinations": {entity: zone},
            "requiredCount": 1,
            "observable": "current-alive-position",
            "latchAtObjectiveCompletion": True,
            "deliveryLedgerSubstitute": False,
            "implementationStatus": "unimplemented",
            "proposalId": "i00006",
        }
        objective["predicate"]["requirements"].append(requirement)
        objective["predicate"].setdefault("requiredLedgers", []).append(requirement["id"])
        draft["requiredCapabilities"].append({
            "id": "checkpoint-entity-presence",
            "status": "reference model implemented; native implementation pending",
        })
        draft["checkpointPresencePlan"] = {
            "capabilityId": "checkpoint-entity-presence",
            "implementationStatus": "unimplemented",
            "proposalId": "i00006",
            "bindings": [{"objective": objective["id"], "requirement": requirement["id"]}],
        }
        errors = self.dossier_validator(draft)
        self.assertFalse(any("checkpoint presence needs its i00006 pending gate" in e for e in errors))
        draft["requiredCapabilities"][-1]["status"] = "implemented"
        errors = self.dossier_validator(draft)
        self.assertTrue(any("checkpoint presence needs its i00006 pending gate" in e for e in errors))
        self.assertTrue(any("checkpoint presence capability must remain native pending" in e for e in errors))
        draft["requiredCapabilities"][-1]["status"] = "reference model implemented; native implementation pending"
        transition = next(t for t in draft["stateMachine"]["phaseTransitions"] if t.get("to") == "victory")
        transition["objectiveId"] = objective["id"]
        errors = self.dossier_validator(draft)
        self.assertTrue(any("checkpoint presence must be an intermediate objective" in e for e in errors))

    def test_dossier_phase_deadline_rejects_hidden_invalid_or_promoted_clock(self):
        campaign = next(c for c in self.odysseys if c['campaignId'] == 'imperial-church')
        source = next(e for e in campaign['episodes'] if e['id'].startswith('33-'))
        self.assertEqual(self.dossier_validator(source), [])
        for case in ('phase', 'zero', 'warning', 'bindings', 'translation', 'native'):
            draft = copy.deepcopy(source)
            deadline = next(r for r in draft['objectivePlan'][0]['predicate']['requirements']
                            if r['kind'] == 'phase-deadline')
            if case == 'phase':
                deadline['phase'] = 'phase-absent'
            elif case == 'zero':
                deadline['secondsByDifficulty']['hard'] = 0
            elif case == 'warning':
                deadline['warningSeconds'] = deadline['secondsByDifficulty']['hard']
            elif case == 'bindings':
                draft['deadlinePlan']['bindings'][0]['requirement'] = 'missing'
            elif case == 'translation':
                del draft['deadlinePlan']['warningText']['es-ES']
            else:
                draft['deadlinePlan']['implementationStatus'] = 'implemented'
            with self.subTest(case=case):
                self.assertTrue(any('deadline' in e for e in self.dossier_validator(draft)))

    def test_expanded_withdrawal_cannot_use_unsupplied_recipient_ledger(self):
        draft = self.draft(2)
        draft["objectivePlan"][2]["predicate"]["requirements"][0][
            "eligibleEntitiesFromLedger"
        ]["ledger"] = "missing"
        self.assertTrue(
            any(
                "prior recipient ledger" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_expanded_dossiers_reject_funding_booleans_that_hide_overdraw(self):
        draft = self.draft()
        draft["difficulty"]["hard"]["gatherableBank"]["wood"] = 0
        draft["difficulty"]["hard"]["mainFeasibleSkippingAllOptionals"] = True
        self.assertTrue(
            any(
                "nonoptional stock drift" in error
                or "main goal needs optional" in error
                for error in self.dossier_validator(draft)
            )
        )

    def test_expanded_dossiers_reject_early_campaign_finale_and_initial_arrival(self):
        draft = self.draft(2)
        draft["stateMachine"]["campaignProgressWrite"] = True
        req = draft["objectivePlan"][0]["predicate"]["requirements"][0]
        eid = req["entities"][0]
        zone = next(
            z
            for z in draft["worldContract"]["zones"]
            if z["id"] == req["destinations"][eid]
        )
        entity = next(e for e in draft["worldContract"]["entities"] if e["id"] == eid)
        entity["initialHub"] = zone["hub"]
        entity["offsetTiles"] = zone["offsetTiles"][:]
        errors = self.dossier_validator(draft)
        self.assertTrue(
            any("intermediate episode can end campaign" in error for error in errors)
        )
        self.assertTrue(
            any("initial arrival incorrectly counts" in error for error in errors)
        )

    def test_act_targets_reject_drift_even_when_campaign_total_stays_equal(self):
        self.assertEqual(self.odyssey_helper['audit_selections'](self.odyssey_policy, self.odysseys), [])
        invalid = copy.deepcopy(self.odyssey_policy)
        targets = invalid['campaigns'][0]['actEpisodeTargets']
        targets[0] -= 1
        targets[1] += 1
        errors = self.odyssey_helper['audit_selections'](invalid, self.odysseys)
        self.assertTrue(any('act targets differ from authored membership' in e for e in errors))
        self.assertFalse(any('act target total differs' in e for e in errors))

    def test_act_targets_require_five_positive_integer_counts_and_correct_total(self):
        for targets in (None, [], [1, 2, 3, 4], [0, 7, 6, 6, 11],
                        [True, 7, 6, 6, 10], [8.0, 7, 6, 6, 3], [8, 7, 6, 6, 4]):
            with self.subTest(targets=targets):
                invalid = copy.deepcopy(self.odyssey_policy)
                invalid['campaigns'][0]['actEpisodeTargets'] = targets
                errors = self.odyssey_helper['audit_selections'](invalid, self.odysseys)
                self.assertTrue(any('act targets must' in e or 'act target total differs' in e for e in errors))

    def test_odyssey_expansion_cannot_discard_baseline_semantic_identity(self):
        invalid = copy.deepcopy(self.odysseys)
        episode = next(
            e for e in invalid[0]["episodeSelection"] if e["existingContract"]
        )
        episode["id"] = "replacement-id-that-loses-progress"
        errors = self.odyssey_helper["audit_selections"](self.odyssey_policy, invalid)
        self.assertTrue(any("semantic identity was lost" in e for e in errors))

    def test_odyssey_selection_cannot_claim_three_repeated_cores_as_variety(self):
        invalid = copy.deepcopy(self.odysseys)
        for episode in invalid[0]["episodeSelection"][:3]:
            episode["coreMechanic"] = "identical-escort"
        errors = self.odyssey_helper["audit_selections"](self.odyssey_policy, invalid)
        self.assertTrue(any("three consecutive identical cores" in e for e in errors))

    def test_odyssey_predecessor_notice_must_remain_nonblocking(self):
        invalid = copy.deepcopy(self.odysseys)
        invalid[1]["continuityContract"]["proceedWithoutPredecessor"] = False
        errors = self.odyssey_helper["audit_selections"](self.odyssey_policy, invalid)
        self.assertTrue(
            any("predecessor progress would gate play" in e for e in errors)
        )

    def test_crossing_segment_keeps_intersections_even_with_no_inner_vertices(self):
        self.assertEqual(
            clip_segment([-2, 0.5], [2, 0.5], [0, 0, 1, 1]), [[0, 0.5], [1, 0.5]]
        )
        self.assertIsNone(clip_segment([-2, 2], [2, 2], [0, 0, 1, 1]))

    def test_north_and_east_preserved_at_high_latitude(self):
        centre = tile_point([8, 44, 10, 46], [9, 45], 320)
        self.assertGreater(tile_point([8, 44, 10, 46], [9.5, 45], 320)[0], centre[0])
        self.assertLess(tile_point([8, 44, 10, 46], [9, 45.5], 320)[1], centre[1])

    def test_missing_spanish_and_witness_voice_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        screen = invalid["campaigns"][0]["scenarios"][0]["screens"][1]
        del screen["text"]["es-ES"]
        screen["narrator"] = "partisan-voice"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("bilingual" in e for e in errors))
        self.assertTrue(any("voice order" in e for e in errors))

    def test_overspent_finite_reserve_and_continuity_cycle_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        invalid["campaigns"][0]["scenarios"][0]["difficulty"]["hard"]["waves"][0][
            "count"
        ] += 1
        invalid["campaigns"][1]["routes"][0]["next"] = invalid["campaigns"][0]["id"]
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("reserve" in e for e in errors))
        self.assertTrue(any("cycle" in e for e in errors))

    def test_insolvent_recovery_budget_is_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        profile = invalid["campaigns"][0]["scenarios"][0]["difficulty"]["hard"]
        profile["gatherableBank"]["food"] = 0
        profile["startingResources"]["food"] = 0
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("insolvent food" in e for e in errors))

    def test_missing_workshop_ledger_is_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "new-rome")[
            "scenarios"
        ][1]
        pred = mission["objectivePlan"][1]["predicate"]
        pred["requirements"] = [
            r for r in pred["requirements"] if r["id"] != "workshop-ledger"
        ]
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("missing required ledger" in e for e in errors))

    def test_karbala_supplies_must_follow_same_families(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "house-of-ali")[
            "scenarios"
        ][3]
        water = next(
            r
            for r in mission["objectivePlan"][1]["predicate"]["requirements"]
            if r["id"] == "water-to-six-families"
        )
        water["pairs"][0]["receiver"] = "another-family"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("same surviving families" in e for e in errors))

    def test_payment_allocation_and_double_receipt_are_rejected(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "church-of-rome")[
            "scenarios"
        ][1]
        payment = mission["objectivePlan"][1]["predicate"]["requirements"][0]
        payment["allocations"][payment["receivingZones"][0]]["gold"] = 0
        mission["objectivePlan"][2]["predicate"]["requirements"][0]["paidFlag"] = (
            payment["paidFlag"]
        )
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("unbalanced delivery" in e for e in errors))
        self.assertTrue(any("duplicated receipt" in e for e in errors))

    def test_local_supply_gap_must_preserve_feasibility_and_difficulty(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = invalid["campaigns"][0]["scenarios"][0]
        for balance in mission["difficulty"].values():
            for index, wave in enumerate(balance["waves"]):
                wave["offsetSeconds"] = 150 * (index + 1)
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("two local supply trips" in e for e in errors))
        self.assertTrue(any("identical wave pressure" in e for e in errors))

    def test_northern_access_cannot_alias_southern_rally(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "imperial-church")[
            "scenarios"
        ][0]
        north = mission["objectivePlan"][0]["predicate"]["requirements"][0]["zones"][0]
        next(z for z in mission["worldContract"]["zones"] if z["id"] == north)[
            "hub"
        ] = "hub-3"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("wrong geographic district" in e for e in errors))

    def test_truce_deliveries_require_two_separate_receivers(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "house-of-ali")[
            "scenarios"
        ][1]
        delivery = mission["objectivePlan"][1]["predicate"]["requirements"][0]
        same_zone = next(iter(delivery["destinations"].values()))
        delivery["destinations"] = {e: same_zone for e in delivery["entities"]}
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("distinct destination distribution" in e for e in errors))
        self.assertTrue(any("actual delivery receipt" in e for e in errors))

    def test_withdrawal_cannot_substitute_unsupplied_families(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = next(c for c in invalid["campaigns"] if c["id"] == "house-of-ali")[
            "scenarios"
        ][3]
        withdrawal = next(
            r
            for r in mission["objectivePlan"][2]["predicate"]["requirements"]
            if r["id"] == "withdraw-same-families"
        )
        withdrawal["eligibleEntitiesFromLedger"]["ledger"] = "all-families"
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("supplied survivor intersection" in e for e in errors))

    def test_side_reward_cannot_spend_main_recovery_or_create_resources(self):
        invalid = copy.deepcopy(self.catalogue)
        mission = invalid["campaigns"][0]["scenarios"][0]
        reward = next(o for o in mission["secondaryObjectives"] if o["kind"] == "aid")[
            "effects"
        ][0]
        reward["resources"]["food"] = 10000
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(any("optional reward budget drift" in e for e in errors))

    def test_two_optional_receivers_or_lookouts_cannot_share_one_footprint(self):
        invalid = copy.deepcopy(self.catalogue)
        objective = next(
            o
            for o in invalid["campaigns"][0]["scenarios"][0]["secondaryObjectives"]
            if o["kind"] == "aid"
        )
        objective["world"]["zones"][1]["offsetTiles"] = objective["world"]["zones"][0][
            "offsetTiles"
        ]
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(
            any("secondary receiving/observation zones overlap" in e for e in errors)
        )

    def test_loading_a_save_cannot_reopen_an_optional_reward(self):
        invalid = copy.deepcopy(self.catalogue)
        objective = invalid["campaigns"][0]["scenarios"][0]["secondaryObjectives"][0]
        objective["stateContract"]["persistentAcrossSave"] = False
        objective["stateContract"]["rewardTransaction"].remove("debit reserved stock")
        errors, _ = verify(catalogue=invalid)
        self.assertTrue(
            any("incomplete optional state/persistence guard" in e for e in errors)
        )
        self.assertTrue(
            any("undefined atomic optional funding transaction" in e for e in errors)
        )


if __name__ == "__main__":
    unittest.main()
