# Composed objectives capability profile v2

The campaign and scenario source envelope remains schema version 1. A scenario may opt in to the separately versioned `capabilityProfile` with `profile: "composed-world-ledger"` and `schemaVersion: 2`. This separates source-envelope compatibility from the semantics of the profile and its compiled intermediate representation (IR). Existing v1 sources, fixtures, localization IDs, and string IDs do not change.

The v2 compiler validates the profile and emits a scenario IR marked `schemaVersion: 2` with a distinct `capability` payload. It preserves author-supplied identifiers. It does not lower compound predicates to the older v1 condition list. Legacy v1 scenarios continue to compile as v1.

Native campaign rendering, the candidate/export path, and the direct Python exporter reject any v2 profile with `capability-not-implemented` until the native predicates and their save/load behavior are implemented and certified in i00003/S3. No entrypoint may silently remove the profile or approximate its all-required logic using legacy conditions.

The zod contracts, structural validator, deterministic compiler output, and pure reducer in this slice are technical references for authoring and adversarial unit tests. They are not a claim of native engine support, a substitute for engine QA, or proof that game triggers implement these semantics.
