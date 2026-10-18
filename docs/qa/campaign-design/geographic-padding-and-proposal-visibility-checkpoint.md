# Geographic padding and proposal visibility correction

18 October 2026 · gpt-6 · isolated d00002 unit based on officially integrated develop d71a61d0. This is design-tool and handoff work, not terrain/history approval or native campaign generation.

## Drawing correction

The old diagram clipped vectors to the authored rectangular bbox while projecting them into a larger padded square. It therefore omitted geographic controls in the square's margins. The renderer now reuses the S2 frame's full sample-center bounds for clipping and keeps the original bbox for projection. The helper's optional viewport separates those responsibilities; its old default remains compatible. Exact intersection coordinates are retained only in the explicit viewport mode to avoid rounding outside the border. Source vectors may now retain finer coordinates; actor hubs and routes are not rescaled.

Regeneration changes 47 expanded SVGs. Both actual episode-source files, all 63 dossiers and blueprints in them, and the global string-ID lock are byte-identical to the base. The remaining seven campaign-source files are untouched. The base 39 scenario contracts/maps and public identities are not migrated. Root rendered and viewed Corinto and Tesalónica before and after; the controls now continue through the margins to the border. These remain diagrams of modern/schematic controls, not surveyed terrain or ancient coastline. Sirmium's final diagram remains unchanged; its modern Sava control is outside the full frame.

This drawing correction does not resolve the 26 regional-reference coverage questions recorded by the new audit. The appropriate source extent, dated terrain, resource locations, actor packing and native routes need their own decisions; no global shrink, expanded source assertion or invented land bridge was applied.

## Runtime criteria visibility

The server's actual i00003 detail view initially returned three acceptance criteria for S3 and two for S4. The pending Sirmium clock and pre-briefing input requirements were present in Markdown after a blank line, outside the contiguous indented acceptance block recognized by the installed parser. The fix removes exactly those two blank lines. Existing criterion texts, proposal frontmatter, lifecycle, dependency lists and S1 review history stay unchanged. No runtime code was copied or changed.

A read-only one-off invocation of the actual installed `parseProposalSlicePlan` against the candidate returns S3 four criteria and S4 three, including those two requirements. This supplements runtime discovery; it is not a substitute for checking the official server after publication. Server confirmation on the integrated source remains pending. Neither requirement becomes implemented or approved from being visible.

## Checks

Dossier/render/verify pass 63 drafts/278 selections, 2594 bilingual screens, 391 secondaries, 36 additional references and zero expanded approvals. Python design 66 tests pass, including padding-without-rescaling and exact-vs-legacy clipping regressions. The actual source/lock byte comparison passed. Root bun run validate passed 108 tests/426 expectations, docs and campaign checks. Independent technical review by gpt-6-luna found no blockers in candidate d60694a; its report is committed as 62d7e3c and independently repeats design 66, dossier check and Bun 108/426. See [bounded review](geographic-padding-independent-review.md). Official merge certification and the live post-publication criteria check remain pending. The conditional Sirmium timing audit still matches its unchanged episode input and 54 hypotheses. No adapter change or new export/game result is claimed.
