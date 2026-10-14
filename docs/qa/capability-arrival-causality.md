# Arrival after an observed departure — reference implementation

Author gpt-6, 2026-10-13; i00003/S1 remains pending independent review. This report does not approve the slice or claim native game behavior.

A guarded entity arrival references its exact ordered-departure requirement. That departure records per-objective actor facts after the receipt during the active phase. The arrival must have its own later observation; buffered global arrivals and a different departure of the same actor cannot satisfy it. Exported recipient ledgers and arrival-generated receipts reuse the guarded arrival check; a globally buffered arrival cannot create a return receipt before its exact causal producer. Structural validation rejects mismatched actors, missing/future references and indirect receipt/departure/arrival cycles. Mandatory objective ancestry is shared with funded production.

The optional source field preserves old unguarded profiles, source version 1, capability version 2 and the existing snapshot shape. Its presence changes the existing contract fingerprint, so old saves for a different contract are rejected rather than silently migrated. Existing native renderers continue rejecting all composed-world-ledger v2 profiles.

The prior local DelendAI gate passed with 81 Bun tests. The subsequent stronger exported-ledger and generated-receipt assertions also passed in the targeted suite (37 cases, 142 assertions); the publication gate validates the final integrated candidate. Five new cases cover buffered arrivals, exact departure scope, save/load and repeats, phase/death rejection and malformed/cyclic references. No adapter code changed, native export was not extended, and no AoE2 playtest is asserted. Engine observations and transport geometry remain i00003/S2–S3 work.

The authorized GPT-6.1 reviewer remains unavailable after the reported service usage limit. No independent verdict exists for this new reference capability; prior reports remain confined to their own hashes and scope.
