# Interaction progress checkpoints

This is a documentary checkpoint, not a runtime queue, source-data schema, forecast, or per-model usage report. It keeps repository progress, formal review, native evidence, and game evidence separate.

## observation-001

**first reconstructed interval; user interaction timestamps unavailable; not a measured per-model duration/token sample**

The client cut date is 2026-10-26 (Europe/Madrid). The requested interval is pinned to the historical baseline and develop cut below; the Git author timestamp is recorded independently and is not treated as the user-interaction timestamp.

| Measure | Baseline `c5533f777dfb7e0f9c9c76157109725aa5288ed8` | Cut `d6acfed489e332a614d4a2731e450c53e619c65b` | Delta |
|---|---:|---:|---:|
| Selected episodes | 278 | 278 | 0 |
| Design dossiers (draft) | 63 | 64 | +1 |
| Selected episodes without a dossier | 215 | 214 | -1 |
| Bilingual screens | 2,594 | 2,645 | +51 |
| Secondary objectives | 391 | 398 | +7 |
| Local research resources | 47 | 49 | +2 |
| Geographic profiles | 26 | 26 | 0 |
| Unresolved geographic identities | 22 | 22 | 0 |
| Selections affected by unresolved geography | 25 | 25 | 0 |

The baseline values are corroborated by `README.md` at the baseline commit, lines 34–36. The cut values are from `README.md` at the cut commit, lines 34–36, and are also summarized in `docs/production/plan.md` and `docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md`. The cut commit timestamp is `2026-10-25T20:36:56+01:00`; the client date is 2026-10-26. The isolated worktree used to prepare this record started at `6e3bbf51e05337dc054750bffed00f456805bc68`, later than the requested `d6acfed` measurement cut. The counts above remain pinned to `d6acfed`; later worktree state is excluded.

Between the two cuts, i00008/S3 was formally closed and i00009/S1 was independently approved. Those are status events, not additional dossier, source, native, or game counts. At the cut, two f00001 source campaigns (`route-pilot`, `route-successor`) had recorded fixture export evidence in the [independent S3 report](../route-pilot/s3-joint-promotion-independent-review.md); no game-verified campaign is counted. Export and round-trip evidence does not establish that AoE2 loaded or played the campaigns.

Work allocation is recorded separately from observed throughput: the architect owns 214 remaining dossier selections, review of 64 dossiers, 54 civic flags, and 22 unresolved geographic identities affecting 25 selections. Luna and MiniMax share a pool of 278 episode tasks; it is not a 278-per-worker target. The repository has no observed MiniMax implementation sample for this interval. Codex quota is unknown. The 39 legacy contracts and seven Jerusalem WIP secondary objectives are excluded from the odyssey counts. Unintegrated work is not counted; these figures describe develop snapshots only.

One reconstructed interval is insufficient for an average or ETA. Do not convert the 214 remaining dossiers into an interaction or time estimate. A moving average requires at least three comparable intervals. Count each new user interaction, not tool messages or context compactions; report hours only from directly measured comparable timestamps. Repository progress does not measure model duration, token use, or remaining quota.

## Evidence pointers

- Historical baseline: [`README.md` at `c5533f7`](https://github.com/CartagoGit/aoe2-mods/blob/c5533f777dfb7e0f9c9c76157109725aa5288ed8/README.md#L34-L36).
- Cut snapshot: [`README.md` at `d6acfed`](https://github.com/CartagoGit/aoe2-mods/blob/d6acfed489e332a614d4a2731e450c53e619c65b/README.md#L34-L36), [`production plan`](../../production/plan.md), and [`design assignments`](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md).
- Export scope: [`f00001/S3 independent report`](../route-pilot/s3-joint-promotion-independent-review.md) and [`quality gates`](../../handoffs/MINIMAX-M3.1-QUALITY-GATES.md).
- Current documentary counters: [`README.md`](../../../README.md), [`production plan`](../../production/plan.md), and [`design assignments`](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md).
