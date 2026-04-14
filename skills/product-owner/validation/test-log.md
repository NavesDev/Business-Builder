# Product Owner Skill Test Log

## RED Baseline (without skill)

| Scenario | Agent choice | Why this fails PO standard | Rationalization captured verbatim |
|---|---|---|---|
| Scenario 1 | C | Allows coding before explicit acceptance criteria and full MVP scope gate. | "With a 30-minute ask, don't keep engineers idle; start low-regret work while acceptance criteria are drafted in parallel." |
| Scenario 2 | B | Baseline behavior happened to comply in this run. | "One-slot capacity means a hard tradeoff, so use a clear business objective plus impact/effort to choose." |
| Scenario 3 | B | Baseline behavior happened to comply in this run. | "Do a quick readiness pass (clear criteria + dependency owners), then hand off immediately." |

## GREEN Verification (with skill)

| Scenario | Agent choice | Compliance result (pass/fail) | Evidence |
|---|---|---|---|
| Scenario 1 | B | pass | "Rule 1 requires explicit MVP scope boundaries and acceptance criteria before coding or handoff." |
| Scenario 2 | B | pass | "Rule 2 requires prioritization from an explicit objective plus impact/effort rationale." |
| Scenario 3 | B | pass | "Rule 1 blocks handoff with vague acceptance criteria, and Rule 3 requires critical dependencies to have an owner and due date before engineering release." |

## REFACTOR Iterations

| Iteration | New rationalization | Counter added to SKILL.md | Re-test result |
|---|---|---|---|
| 1 | None observed in GREEN run | Not required | Stable pass (3/3 scenarios) |
