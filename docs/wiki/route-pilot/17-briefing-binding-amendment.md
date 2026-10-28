# T01 scenario briefing binding

Architect: gpt-6. Date: 2026-10-25. Scope: correction to the closed f00001/S1 source specification, found during gpt-6-luna's materialization of f00001/S2. Independent review of this correction is pending; the earlier S1 review is not attributed to this later change.

The scenario schema requires at least one `narrative.intro` line. The original inventory gave T02 an explicit scenario intro but bound T01's existing factual notice only to `campaign.introduction`. That omission left the implementer without an authorized T01 scenario-intro binding.

Reuse `campaign.route-pilot.fact` at both surfaces, spoken by `collection-narrator`, with a unique line ID for each record. The wording already explains that the map is a fictional laboratory and makes no historical claim. Repeating that short notice on scenario entry is intentional. No new textKey, translation, narrator, condition, route, string allocation or schema operation is needed. Do not repeat the whole campaign introduction or substitute an unbound event.

The inventory remains 43 keys: 36 source-materializable keys and 7 documentary native intentions. All English and Spanish text values remain unchanged, as do T02's bindings. This amendment does not approve f00001/S2, conditional native presentation, exports or game behavior.

Review checks: compare all inventory keys, text values, dispositions and other bindings with the integrated S1 baseline; confirm only the T01 factual binding changed. Inspect the resulting T01 intro for a distinct line ID, the same textKey and the specified speaker. Both complete staging bundles must pass their existing checks before S2 acceptance.
