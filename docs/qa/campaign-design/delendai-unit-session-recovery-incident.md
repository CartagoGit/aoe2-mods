# Empty authoring unit: lost entry result and official cleanup

Cut: 26 October 2026. Scope: operational evidence for i00009/S2; not a replacement implementation of DelendAI. The installed connected server remains authoritative.

The original gpt-6-luna entry created `wip/gpt-6-luna/implement/i00009-S2-g1/authored-secondary-reward-projection`, but its wrapper result did not give the worker a usable session/path receipt. Later `work enter` rejected another session, while `work claim` replied that the ref already belonged to that model. The agent preserved the refusal and made no edits. The official MCP enter also rejected the mismatched session. Reading another session's token, borrowing identity, forcing a claim or manually editing the runtime were not attempted.

The bounded diagnostic consulted overview, the served `delendai_work` schema, knowledge, work help, status/doctor and documentation search. No general secure session-recovery action was found. This is a limitation of the observed surface, not proof that all runtime versions lack one.

Root subsequently ran the official `work reap` dry run. It specifically classified this unit as removable, with empty edited/regenerable lists; its tip was the already integrated `d6acfed`. After inspecting that result, root ran official `work reap --apply`. The response confirmed removal of the empty unit and release of `refs/claims/slice/i00009/s2`. The new implementation can now request a fresh official unit. That is safe cleanup of this demonstrably empty unit, not recovery of another session or permission to discard unmerged work. Reopening, claiming and actual implementation must still be confirmed by the worker before reporting the task active or done.

For future entries, retain the official result immediately and use the worker's own stable session. Review actions should use the explicit own checkout through the capability resolver: the CLI `review approve` wrapper selected `review/batch-all-g2/verdicts` during i00010/S1 despite an own review checkout, leading to a refusal against the worker's own claim. The explicit official MCP `proposal_review` with the correct checkout succeeded; the resulting independent verdict was published in `f4a2599b3ed6c1055d41c73de690c375ae7b752a`. This is an observed invocation correction, not authority to take a genuinely different unit.

No proposal is marked done by this note. No user Git authorship, source identity, public contract or historical permission changes. All cleanup results and rejected operations remain in the runtime's logs; this document records the bounded outcome and distinguishes it from a general infrastructure fix.


## Existing committed unit and shared snapshot — i00010/S2

MiniMax committed its implementation in its own unit as fa29d7f, then invoked `work checkpoint` from the clean shared checkout. The resulting 5319f11 snapshotted the shared tree into the work ref and removed the product there. The implementer preserved that history and reapplied its own unchanged product in 625c3dd, then submitted through the official capability and corrected a review naming finding in ba86f7b3. Publication merged the net intended diff into develop at d86c561 with its gate. No shared develop commit, manual merge/push, reset or rewritten history was used. For an already committed isolated unit, continue in that unit and publish it; do not snapshot a clean shared checkout as though it contained that unit’s edits.

Publication retired the completed implementation worktree automatically. Its ignored build logs disappeared with it, while external OpenCode event captures retained executed commands and captured outputs. Those are different evidence forms. Preserve complete logs and private diagnostics outside a disposable unit before publication; never reconstruct lost logs and label them originals. The independent integrated review is keeping new complete logs outside its unit. This note does not approve i00010/S2.
