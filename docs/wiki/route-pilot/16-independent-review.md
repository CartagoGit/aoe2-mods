# Independent S1 review: route-pilot specification

Reviewer: gpt-6-luna  
Reviewed commit: `5b722b1b2f37f56d53aa3ca84c6f9aa3e2615f73`  
Review date: 2026-10-24

This report records an independent specification review. It is not a formal S1 approval, engine test, or claim that native conditional presentation works.

## Review observations

The review of `9d60d99` found three material inconsistencies, which are corrected in the reviewed commit:

1. T02 had no victory route or progress key, while the staging validator requires fixture status to permit a final scenario without progress output. Both campaigns now declare `status: fixture`; this permits source/staging validation without implying review or release status.
2. Seven conditional victory/recap texts could not be included as unreferenced catalog entries, and inert `narrative.events` would fail the gameplay validator. The inventory now distinguishes 36 `s2-materialize` entries from seven `native-pending-documentary-only` entries and states their current bindings or deliberate omission. The specification and SRC04 require the seven to remain outside runtime catalogs and lines until a certified capability exists.
3. The legacy exporter generates `cdf-react-<difficulty>-targets` task effects for the castles, despite there being no content-authored attack order. The specification now documents the generated behavior and ENG25 requires inspection of the exported triggers and observed building behavior; no engine behavior is presumed.

The earlier mismatch between the proposed T02 predecessor recommendation and the single-key `recommendedPrevious` contract is also resolved: both source fixtures use `recommendedPrevious: []`, while T02 keeps a static optional recommendation in its introduction. The specification explicitly says this metadata cannot encode the two-key read/error truth table.

The precedence note in `00-brief.md` establishes that the implementation specification, acceptance matrix, and updated text inventory supersede the preliminary brief and screen-contract wording. The reviewed docs consistently mark adaptive recap, conditional endings, profile reads, timing, and engine behavior as pending native evidence. The matrix separates source/staging checks from blocked engine cases.

## Validation

Ran `bun run validate` at the reviewed commit. It exited 0: TypeScript/Biome checks passed; 142 tests and 2069 expectations passed; documentation/link checks passed; one campaign passed campaign validation. These checks do not establish gameplay or native UI behavior.

No further blocking specification inconsistency was found in this review. Formal S1 acceptance remains with the proposal owner and DelendAI workflow.
