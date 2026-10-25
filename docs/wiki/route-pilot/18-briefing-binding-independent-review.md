# Independent review: T01 briefing binding correction

Reviewer: `gpt-6-luna` · 2026-10-25  
Scope: correction commit `8d28250` (`docs(pilot): bind existing factual notice to required T01 scenario intro`) compared with integrated baseline `4c5ae8485577313ed3541de2e75136982f28eb12`.

This is an independent review of the three-file correction only. The previous f00001/S1 record remains `done`; its earlier review predates this amendment. This report does not reopen or re-approve the complete S1 specification, approve S2, certify a bundle, or claim native presentation or game behavior.

## Findings

No defect found in the correction's stated scope.

The corrected binding is consistent with the existing schema. `packages/schemas/campaign.schema.ts` requires `scenario.narrative.intro` to contain at least one `lineSchema` record. Each line has its own `id`, `speaker`, and `textKey`; the schema does not require each surface to have a different key. The specified T01 line can therefore reuse `campaign.route-pilot.fact` and `collection-narrator` while retaining a distinct scenario line ID alongside its existing campaign-introduction line ID.

The source catalog's key collection deduplicates line references (`packages/localization/localization.catalog.ts`, `campaignKeys`), so referencing the same semantic key on the campaign and scenario surfaces does not add a 44th key or allocate a second string ID. The scenario compiler maps scenario line IDs to their referenced text IDs (`packages/scenario-compiler/scenario.compiler.ts`); a distinct line ID avoids a collision within T01's scenario narrative. The existing fact is already spoken by the collection narrator and its EN/es-ES wording explicitly identifies a fictional laboratory without historical claims. Repeating that short factual notice at scenario entry is coherent with the implementation brief.

The amendment preserves T02's inventoried `scenario.route-successor-recap.intro`, and the specification keeps the full recap before scenario start rather than moving recap branches into the timed in-scenario intro. No conditional surface, new narrator, text, schema field, source event, or unsupported adapter operation is introduced.

## Diff and inventory checks

The candidate diff against `4c5ae848` contains exactly:

- two added sentences in `02-implementation-specification.md`, binding T01's required intro to the existing factual key and pointing to the amendment;
- one `sourceBinding` change for `campaign.route-pilot.fact` in `15-text-inventory.json`;
- the new scoped amendment `17-briefing-binding-amendment.md`.

I parsed the candidate inventory and compared it entry-by-entry with the integrated baseline. It remains 43 semantic keys: 36 `s2-materialize` and 7 `native-pending-documentary-only`. All 43 keys, all EN/es-ES text values, all source dispositions, and all bindings except the `campaign.route-pilot.fact` binding are unchanged. The amendment correctly describes the T01 scenario line as reusing that key and speaker with a separate line ID; it also states that no extra string or full campaign introduction is copied.

The official review queue returned zero proposals at inspection time. `proposal review status` reports the existing S1 slice `done` with the earlier limited review. I opened my own alongside review unit and claimed only this report. I did not record a new proposal verdict because the requested scope is a correction report, not a second approval of S1. No validation command was run: the reviewed diff contains documentation only and does not alter schema, runtime, staging content, tests, or the adapter. Root's later integration gate remains the evidence for any integrated result.
