# Imperial25–26 — independent design review

Reviewer gpt-6.1-sol,2026-10-15. Read-only inspection of author WIP `/home/cartago/_projects/games/aoe2-mods/.cache/delendai/.worktrees/gpt-6-new-all`.25 checkpoint identified by coordinator78b1860;26 local draft. No Git writes, source edits, claims or formal historical/native verdicts. Prior review unit g6 retired officially after its i00005 verdict integrated62ec0d4; unrelated to this review.

## P2 — explicit malformed observation placement silently falls back

`tools/design/secondary.py:105` uses `if placement.get('observationHubs')`. For26 side-1, authored northern/eastern observation hubs are hub-3/hub-4. Replacing this field with [] or None or empty string is accepted and generated zones silently become default hub-1/hub-3. No error is raised. Strict placement keys alone do not prevent explicit but malformed placement losing its authored meaning. Detect key presence first, require a correctly typed nonempty list with exactly one known hub per generated observation zone; reject this field on non-scout/watch tasks even when empty. Preserve omission/default behavior for legacy source. This does not invalidate current25/26 coordinates, whose fields are well formed.

Reproduction executed by reviewer: deepcopy26 optionalTasks[0], set placement.observationHubs to [],None,'' independently; build_optional_objectives returns zone hubs[hub-1,hub-3] each time.

## Design risk — difficulty and duration need native pacing evidence

Both episodes deliberately have zero enemies, no regeneration and no deadline. In each episode start+bank totals are identical across difficulties; easy/standard/hard mostly adjust initial liquid stock and12/9/6 workers. Different command allocation is plausible, but lower worker count can primarily increase idle gathering time. The quoted30–55/35–65/40–75-minute ranges are estimates, not a measured challenge curve. Retain the existing pending fun/balance label and test time-to-meaningful-decision, unavoidable waiting and useful parallel tasks before promotion; this review does not require inventing enemies or a historical hunger countdown.

## Contract and economy inspection

25 keeps two accounts/copies and two distinct three-assistant cohorts separate. o2 derives three different outputs against one exact120W30G payment. o3 assigns the two copies/cohorts to distinct west/east courts and conserves240F as120each. o4 has separate departure receipts o3/req3 and req4 and guarded return arrival requirements for the same cohorts; independent provision index goes to southern archive. Text correctly says receipts, not present residence or synodal votes.

26 has six original helpers plus three original notes, explicit pair destinations2/2/3/3/5/5, notes2/3/5, and one atomic allocation360F240W60S conserving120F80W20S at each of three courts. All nine originals are protected by survivor groups. No new derivation, return or presence operation is claimed. Optional goals use separate namespaces/entities/receipts; none is a main dependency or religion-affinity goal.

Own24 resource inequalities (2episodes×3difficulties×4resources): accessible nonoptional stock covers mandatory payment+protected recovery+replacement+all optional costs without rewards. Reserved rewards25=550F200W25G and26=450F200W are finite/segregated; max optional costs50W50G. No exact same-position collisions between optional actors in either current episode.26 aid crates and guide share origin but guide offset[-10,-6] differs from aid[-6,3]/[-6,6]. Unit/building footprints and shoreline/path width remain unverified.

Helper instruction overrides validate complete nonempty EN/es and retain the same funded Benefit suffix; factory forwards instruction and placement. Finite per-identity offsets reject wrong count/NaN/bools. Omitted fields preserve the visible default branches; no blanket historical legacy-output equivalence was independently computed across every old commit.

## Historical/voice basis and limits

Personally read displayed AmmianusXXII.2.1–5 andXXII.5.1–4: entry narrative places arrival11December;5.2 describes reopening/sacrifice orders, while5.4 motives/polemics are authorial assertions. The broad December361–early362 frame does not invent one local implementation day.26 common narrator attributes the account and distinguishes policy from universal belief; Marcus27 is an explicitly invented temporary visitor, not a palace witness. No temple site, ritual actor or creed quota is placed. Source https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html .

Personally read SulpiciusChronicaII.41–44 selected Latin text and displayed opening portions of SocratesII.37, not both complete books. The25 source limits appropriately separate Ariminum/Seleucia, attribute later partisan reports, distinguish Taurus from magistri officials, and avoid turning council drafts into authenticated in-map books or votes. Marcus25 receives reports; fictional copying/provision work does not cause the formula. Sources https://www.thelatinlibrary.com/sulpiciusseveruschron2.html and https://www.newadvent.org/fathers/26012.htm . Prior own selective Markauskas73–74 reading exists; no new whole-thesis read. Municipal archaeology/PDF plates were NOT personally re-read here: their coverage remains architect-reported. No ancient footprint, drainage, shoreline or native traversability approval.

The title Altars of a New Reign is consistent with an attributed policy backdrop, though gameplay deliberately covers civic logistics rather than building altars. Ages25/27 match proposed c.334 birth within the declared fictional biography. General-to-persona handoff and own ignorance are explicit; later writings are external narration, not carried canonical autographs.

## Verification

Own audit_dossier25/26 returns[];24 solvency checks pass. Full bun run validate result recorded below when complete. No new source-confirmed P1 found in this bounded review; the P2 malformed-placement case and pacing limitation remain. This is not approval of d00002, historical accuracy overall, terrain, native support or fun.

Full own bun run validate exit0:99/99Bun,357expect,docs:check and campaign:validate pass. Log /tmp/gpt61-imperial25-26-validate.log. Python adversarial suite is included by docs:check; its individual count was not separately emitted by that wrapper. No test:export repeated: this review changes no adapter and prior run reported missing local AoE2ScenarioParser, not game evidence.


Architect follow-up, 15 October 2026: the reproduced P2 is corrected in the design generator. A present observationHubs key must contain one existing hub per observation zone; empty, null, string, wrong-length, unknown and non-string entries reject instead of selecting defaults. Explicit origin/receiving hubs must also exist. A regression preserves the requested north/east sites and rejects all six malformed cases. This follow-up is a correction record, not an independent approval of the new code or of episode 27, which was authored later.
