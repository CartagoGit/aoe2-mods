# Continuous-control interval structural validation

Author gpt-6 · 2026-10-13 · i00003/S1 · independent review pending. Base e4f4d5ed8fb3b786d1699fc9bacd1bbaa561c02e.

A composed area-state predicate could name a nonexistent, current, predecessor or independent objective as mustRemainUntilObjective. The reducer continuously enforces control until that target latches, so an invalid target could make the interval impossible to close or allow an unrelated objective to end protection early. A visited-and-passable predicate also records historical visits rather than current control and cannot promise continuous control.

The structural validator now accepts the interval only for controlled-and-passable state and an existing distinct target with the control objective as a mandatory transitive predecessor. It reuses objective-ancestry.helper.ts; array order alone cannot authorize an independent target. The compiler emits capability.control-interval on invalid contracts. No schema, reference reducer, save format or native adapter behavior changed.

Regression coverage accepts a valid three-objective transitive chain and rejects missing/self/prior targets, a later-listed independent target and visit-only state at both validator and compiler gates. The existing live reference test still enforces defeat when control is lost before the endpoint latches.

Verification: local official DelendAI gate passed at 2026-10-13T20:58:17.073Z; 86 Bun tests / 289 assertions, type/format checks, documentation and campaign validation. No binary export or game test is claimed; native v2 and certified continuous observers remain pending. This author report does not approve i00003/S1.
