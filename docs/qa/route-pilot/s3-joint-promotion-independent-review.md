# Independent joint-promotion review — f00001/S3

Reviewer: gpt-6. Implementer: gpt-6-luna. Date: 2026-10-25. Materialization receipt: candidate `70c3950cf9e8bc4ad4593aa55e6f22b3f2f34b41`, merged with accepted develop `e08a5cbd` at `8581805794e489534f9b612beedbd03146285d71`. Git author/committer remains configured Cartago; model implementation/review responsibilities remain separate in DelendAI. This is technical source/export review before official publication and formal verdict.

No blocking discrepancy remains. The four promoted JSON files are byte-for-byte equal to their frozen staging sources and to the accepted source snapshot. Both staging directories retain PROMOTED.md identifying source product/review and referring to this materialization receipt; neither note invents a self-referential commit hash. Subsequent source edits belong in campaigns. This review does not close S4 or approve historical authoring.

The nine prior string IDs and retired list are unchanged. Exactly 36 unique runtime keys were allocated: 23 from route-pilot and 13 from route-successor, equal to the authored English catalogues. Each campaign preserves seventeen complete draft catalogues, unchanged text, identities, conditions, durations and scenario geometry. No seven documentary native intentions were promoted as runtime keys. Empty assets require no copied files or path changes. The unchanged glossary has no canonical terms; no new canonical term/equivalence set was specified by this technical promotion. Its emptiness does not approve the draft translations.

## Independent execution

`bun run validate` passed: 157 tests/13 files, 2,134 expectations, valid documentation/local links and three active campaigns. `bun run test:export` passed with three variants, two round-trips and unsupported mode rejected. `bun run campaign:build route-pilot --export` and the corresponding route-successor command both passed. ZIP inspection found the campaign container and seventeen locale files in each; no external tool sources/executable are packaged. All generated reports retain gameVerified=false.

The isolated checkout needed the existing pinned tool environment. Reviewer used COF_PYTHON pointing to the shared installed .venv/bin/python (AoE2ScenarioParser 0.9.6) and RGE_CAMPAIGN_BIN pointing to the external cached tool at configured revision `3c40203b650de9888ca82fae1276ea67bf3d3d93`. All three cached C/header source hashes match config/toolchain.json; executable SHA-256 is `1846fc5265d38aa8f963ecc75c0bf28264b813e138df732ce94377fe2697bcde`. The implementer's initial missing-parser failure and the reviewer's mistyped external tool path were environment/invocation failures, preserved before successful corrected runs; no repository code or gate was weakened.

| Artifact | Source SHA-256 | ZIP SHA-256 |
|---|---|---|
| route-pilot | `097c38b301eb2f37c9cf341090c60a0e8e41de4aeab343809b910e512898934d` | `e97052c9d7a36770d92263490c536d3ced761dc2314418e33821de3c65bbc7a2` |
| route-successor | `046fd51e0094ae3ee2258e07731b8c3dba36a01268968ce7d3161458c5c8ec19` | `8532e224ca30aeaa2d6e56ff5fe022d8721167c5655767551bb5ccc88a8fc4ce` |

These hashes identify this execution's outputs, not a general promise of deterministic binary metadata. Independent test-export also generated technical-pilot; that existing fixture is not a new S3 source delivery. Artifacts remain local build/dist output, with no mod distribution or publication to the game service.

Formal S3 approval follows official integration against its exact SHA. Actual AoE2 load, pathfinding/footprints, native route persistence/conditional recap, language review and gameplay remain pending. Static source recap does not acquire a saved-record reader merely because it exports. GAME VERIFIED and PRODUCTION READY are not asserted.
