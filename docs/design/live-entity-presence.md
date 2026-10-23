# Live entity presence / implementation contract

Architect gpt-6, 14 October 2026. Official proposal [i00005](../delendai/proposals/ready/infras/i00005-presencia-actual-de-entidades-distinta-del-historial-de-entregas.md). Reference implementation completed and independently approved in i00005/S1 on15October2026; native observers and actual AoE2 QA remain pending. The approved i00003/S1 semantics are preserved.

## Problem and required behavior

An `arrived` ledger records that a particular identity reached a particular destination. Moving that identity somewhere else does not erase that historical fact. It cannot establish current presence, permanent residence, custody transfer, carried inventory or simultaneous delivery with a second actor.

Milan350 requires a different condition: when the three reporting clerks finish their receipt-backed return, each of three stores must currently contain its own original civilian bundle and original custodian, alive. An earlier delivery followed by departure must leave final completion unavailable. The same original may return to its assigned store; this restores eligibility. Leaving a store earlier does not itself defeat the mission. No actor is frozen, handed to another owner or recreated by this contract.

Other episodes whose intended goal is merely receipt history must say so. Orders15/16/18/21/23 use recorded receptions and causal returns without a current-residence claim. The hypothetical residence of historical bishops or real communities is never a gameplay observable.

## Source and design representation

The design dossier uses `kind=current-entity-presence`, explicit original `entities`, `requiredCount` and a complete per-entity `destinations` mapping. It declares `observable=current-alive-position`, `reevaluateBeforeTerminal=true`, `deliveryLedgerSubstitute=false`, `implementationStatus=unimplemented` and `proposalId=i00005`. Those last fields are planning provenance, not proof of an executable operation.

Milan22/o3 binds req3–6 through `presencePlan`: three separate one-bundle requirements and one three-custodian requirement mapping ordinally to west/northeast/southeast stores. The existing reporting-clerk departure remains o2/req5 → o3/req1, followed by its guarded arrival in req2. No entity IDs, historical source IDs or string ranges change.

The design validator checks unique valid identities, feasible cardinalities, complete known destinations, exact presence bindings and the explicit unimplemented gate. Replacing a required presence predicate with `entity-state/arrived`, omitting its capability or claiming implementation fails. These are specification checks; they do not execute presence or the game.

## Reference implementation decisions for i00005/S1

Extend the existing strict capability schema, compiler, validator, snapshot and immutable reducer. Reuse the shared duplicate, identity, zone and diagnostic helpers. Keep files in their existing domains with descriptive responsibility/type names; no barrels. The source envelope remains schemaVersion1 and the composed profile remains explicitly version2. Preserve existing contracts and fingerprints for profiles that do not opt into the new predicate.

Use the same predicate kind and explicit identity/destination mapping in the typed reference profile. Planning provenance must remain distinct from the executable profile schema; the architect supplies any required conversion. Do not admit arbitrary unknown fields or claim the reference implementation can validate ancient geography.

The reference observer receives a typed **live spatial batch**, containing a monotonically increasing safe-integer observation sequence and per-identity alive status plus current zone memberships. Zone memberships are computed by the eventual native observer from actual current unit position, calibrated hub/zone footprints and collision policy. This reference profile presently carries hub names and offsets, rather than surveyed global XY geometry: do not invent global coordinates or infer membership from arrival history.

Every accepted batch replaces current observations, rather than accumulating membership. An omitted identity is unknown and cannot satisfy presence; an empty membership means outside all observed relevant zones. Unknown identities/zones, duplicates, inconsistent batches, invalid sequence values and malformed status fail closed. A batch can identify overlapping zones, but a requirement counts each distinct original identity once and only against its own assigned destination. Destroyed identities never become alive through another observation.

Alive status is checked against both live observation and the existing irreversible destruction state. An observation of death must preserve existing survivor/essential-loss defeat priority; an alive observation cannot resurrect an identity. Unknown location cannot become a positive arrival, payment, derivation or ownership-transfer fact.

Maintain current observation state separately from `arrivalLedger`, `arrivedEntities`, receipt facts and exported ledgers. Moving out updates current membership while all historic receipts survive. No `record-predicate` flag, `record-arrival`, paid receipt, elapsed time, objective latch or saved positive Boolean may substitute for live evidence.

An objective containing presence requires a fresh batch supplied with its latch attempt. A saved positive observation alone is insufficient. Victory also requires a new batch immediately before the terminal decision, rechecking the relevant current-presence requirements; an earlier successful objective latch must not allow victory after a custodian moves away. Native S2 must observe after same-tick movement/death processing and before victory. Defeat takes precedence. Missing spatial evidence leaves completion unavailable rather than granting victory or introducing an invented defeat.

The trusted native observer produces these inputs; tests may supply them explicitly as reference observations. Such tests are not game evidence. Persist observation sequence and canonical state with the existing fingerprint. On load, fresh latch/terminal batches are still mandatory. Older version2 snapshots without presence fields must remain loadable for their original profiles; do not change the serialized shape of unrelated profiles unnecessarily. A new runtime does not promise that an old strict parser can understand a new predicate. Document compatibility and rejection in ADR0005.

## Required adversarial verification

- Arrive at a store, leave it, retain the historic arrival and fail current presence.
- Return the same live original and regain presence; a similarly named replacement fails.
- A three-custodian requirement maps one original to each store; three at one store fail.
- One bundle outside its own store, dead or unobserved keeps the final incomplete, despite all old arrivals and clerk-return receipts.
- Missing, partial, duplicate, unknown or stale spatial input cannot reuse a previous positive membership; input snapshots remain immutable.
- A fresh successful objective latch followed by movement before terminal requires a fresh failing batch and cannot win. Same-tick death plus victory uses defeat priority.
- Save/load preserves identity, fingerprint and observation sequence; no automatic trust in a saved positive spatial observation. Repeated actions do not duplicate receipts, rewards or terminal effects.
- Existing profiles keep their arrival/phase/payment behavior. Source schema, TypeScript, unit suite, docs and export guards pass; unsupported native profile still rejects explicitly.

## Native and content promotion

i00005/S2 additionally requires the native foundation in i00003/S3. Bind the current-position/health observer to real unit IDs and tested zone geometry. A current-membership batch cannot be implemented by a historical Enter Area receipt, timeout or script Boolean. Capture XS/parser/build versions, callbacks, round-trips, same-tick ordering and saved-game behavior. Actual game evidence remains a separate gate.

i00005/S3 updates the dossier support states and designated handoff only after actual implementation and independent review. MiniMax may then materialize the exact approved content contract. Until those gates close, Milan22 stays a full **design draft with an unimplemented requirement**, rather than an implementable historical campaign.


## Reference delivery, 15 October 2026

Implementation corrections landed in `983ef905`; formal fresh review landed in `d793ae4652e64df87afd5015ed24fbfaa31ad707`. [GPT-6.1 technical reevaluation](../qa/campaign-design/entity-presence-gpt61-round2.md) confirmed both prior findings were corrected. Its formal approval was rejected by the runtime’s reviewer rotation rule; [fresh gpt-6-luna review](../qa/campaign-design/entity-presence-luna-fresh-review.md) independently inspected the diff and executed checks before formal approval. Both reports retain their actual scope.

The shared generation helper now prevents a future derived token or receipt-generated identity from counting as present before its producer has run. A rejected spatial batch does not prevent a tick from processing an independent deadline or defeat. Own reviewer checks passed102tests/389assertions and export3variants/2round-trips with unsupported mode rejected and gameVerified=false.

Milan22 records this reference provenance separately. Its requirement implementationStatus remains unimplemented for native materialization; required-capability status now accurately distinguishes the reviewed reference from the pending native implementation. This documentation correction does not execute or approve S2/S3, unlock campaign authorship, certify current observations in AoE2 or prove historical geography. Those gates remain as stated above.
