# DelendAI startup recovery — 5 November2026

Architect gpt-6 · x00001/S1 · requested log inspection before resuming campaign work. Independent review and official publication pending at this source cut.

The supplied VSCode log reached running/ready transport but reported a degraded startup. Seven visible tools and lazy plugin loading are the declared managed surface, not missing tools. VSCode labels stderr lines as warnings, including ordinary startup summaries. The automatic error-reporting notice describes an existing enabled preference; this task does not change that preference or send messages/issues manually.

## Findings and bounded fixes

- **Eight absent official Git guards:** `delendai guard status` reproduced all eight missing. `delendai guard install` created pre-commit, commit-msg, reference-transaction, pre-push, post-checkout, post-merge, post-commit and post-index-change through the supplied installer. The optional generated-file merge driver remains absent because this game project does not supply that driver script; no server implementation was copied into the game.
- **Invalid validation declaration:** the installed schema requires a string `expect` for every command. Add `expect: "exit0"` to the unchanged `bun install --frozen-lockfile` and `bun run validate` commands. This describes success and does not weaken the gate.
- **Nonexistent release branch:** the configured release was `master`. Read-only GitHub calls on CartagoGit/aoe2-mods returned only develop/main plus a review work ref, with default main; master/protection returned explicit "Branch not found". main/protection returned explicit "Branch not protected" with admin access. Set the project’s release name to **main** and keep integration **develop**. An unprotected existing branch is a readable observed-policy fact, not an authenticated/protected branch claim. No branch or protection setting was changed on GitHub.
- **Source selection:** `.vscode/mcp.json --branch=main` selects DelendAI’s own cached main source via its supplied branch-runtime helper. It does not select the game repository’s work base. Leave the user’s MCP launcher unchanged. The connected Codex server reports0.3.0; the supplied VSCode main-branch report says0.1.0. Record each interface/version rather than assuming the banner identifies the other process.

## Verification boundary

GitHub permission was ADMIN and the main protection response was an explicit absence, not a guessed interpretation of generic404. Both negative API responses were inspected without changing credentials or branch rules. Official guard install succeeded; confirm status after installation. A fresh main-source MCP smoke, installed-schema check, independent scope review and official project gate are required before calling this repair integrated. Archive the actual evidence outside the unit. Existing game playtests, historic approval and campaign counters are unaffected.

## Executed configured-main startup verification

A real MCP client connected to the same cached DelendAI **main** host used by VSCode, with workspace set to the **shared checkout** and `--config` pointing at this unit’s corrected file. The server identifies itself as0.1.0 and its fresh startup reports **READY**, blockers0, repairTasks0, no skipped phases. Overview has no configIssues. The captured log contains neither missing-expect diagnostics nor the nonexistent-master governance blocker. Official guard status reports all eight hooks installed. The launcher file is unchanged.

The first probe mistakenly used the implementation worktree itself as the host workspace. That older main-source startup reconciler interpreted its legitimate isolated work-ref as a moved shared checkout and could not read CI for an unpublished unit commit. That failed setup and its local cache repair record are preserved separately; no shared branch was reset or repaired to hide it. The corrected probe above uses the actual configured canonical workspace. The successful startup does not turn readable unprotected-main into a protected branch or a tested game.

Evidence: `/home/cartago/.codex/artifacts/aoe2-mods/delendai-startup-recovery-20261105/` contains `canonical-main-server-smoke.json`, `canonical-main-server.stderr.log`, the first failed unit probe, and `guard-status.json`. The installed0.3.0 CLI’s doctor also passed before the fix; that generic doctor did not detect the schema warnings and is not substituted for the real main-server startup.
