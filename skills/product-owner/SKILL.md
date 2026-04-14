---
name: product-owner
description: Use when MVP scope, backlog priorities, or handoff readiness are ambiguous and engineering needs implementation-ready stories with explicit acceptance criteria and dependency ownership.
---

# Product Owner

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** None.
- **REQUIRED SUB-SKILL:** None.

## Overview
This skill enforces Product Owner rigor between strategy and execution. It prevents ambiguous scope, weak prioritization, and low-quality handoffs from entering development.

## When to Use
- Strategy exists, but MVP boundaries are still unclear.
- Backlog prioritization is disputed across functions.
- Engineering requests implementation-ready stories now.
- Acceptance criteria are vague or missing.
- Dependencies exist without explicit owners and due dates.
- Keywords people will search: MVP scope, backlog ambiguity, acceptance criteria, dependency ownership, handoff quality gate, rework risk.

## When NOT to Use
- Detailed legal/fiscal interpretation with no product-scope impact (use legal-dpo).
- Channel-level execution choices where growth-lead already owns prioritization.

## Quick Reference
| Situation | Action | Why |
|---|---|---|
| Scope pressure with deadline | Freeze coding start, define in-scope and out-of-scope first | Avoids hidden scope growth |
| Stakeholder conflict on priorities | Rank by objective and impact/effort, log DEC-* rationale | Keeps trade-offs auditable |
| Engineering asks for stories immediately | Block handoff until acceptance criteria and dependency owners are explicit | Prevents rework and blocked execution |

## Implementation
### Core Pattern
1. Validate mandatory input quality (thesis, constraints, objective, stage).
2. Define MVP in-scope and out-of-scope boundaries.
3. Prioritize backlog against explicit objective and impact/effort criteria.
4. Write story-level acceptance criteria before handoff.
5. Assign owner and due date for every critical dependency.
6. Evaluate gates and produce deterministic status.
7. Publish next action package (owner + due date + expected output).

### Mandatory skill input
| Field | Mandatory | Example |
|---|---|---|
| skill_id | Yes | `product-owner` |
| segment | Yes | `B2B`, `B2C`, `Hybrid` |
| revenue_model | Yes | `Monthly subscription` |
| maturity_stage | Yes | `Level 1`, `Level 2` |
| thresholds | Yes | `CAC_MAXIMO`, `MARGEM_MINIMA`, `CHURN_MAXIMO_SEGMENTO` |

### Mandatory skill output
| Section | Mandatory minimum content |
|---|---|
| Final status | `approved`, `mandatory_adjustments`, `gate_failed` |
| Summary diagnosis | 3-5 lines with context and primary conclusion |
| Decisions made | IDs (`DEC-001`, `DEC-002`) with decision and rationale |
| Executed checklist | IDs (`CHK-*`) with status (`ok`, `pending`, `blocked`) |
| KPIs and limits | KPI, current value, target, limit, unit |
| Risks | IDs (`RSK-*`), level, mitigation, owner |
| Gates | IDs (`GATE-*`) with `pass` or `fail` and corrective action |
| Next action package | Action, owner, due date |

### Deterministic status rules
1. If any gate has `fail`, final status = `gate_failed`.
2. If no gate fails and checklist has `pending` or `blocked`, final status = `mandatory_adjustments`.
3. If all gates pass and checklist has no pending items, final status = `approved`.
4. IDs (`DEC-*`, `CHK-*`, `RSK-*`, `GATE-*`) must stay stable across iterations.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Prioritizing by stakeholder pressure only | Breaks objective alignment and traceability | Apply objective + impact/effort and record DEC-* |
| Releasing stories with vague criteria | Creates implementation drift | Require explicit acceptance criteria per story |
| Handoff with unresolved dependencies | Team blocks mid-sprint | Assign owner + due date for each critical dependency |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "With a 30-minute ask, don't keep engineers idle; start low-regret work while acceptance criteria are drafted in parallel." | Parallel drafting still starts work without a clear gate. Scope and criteria must be explicit before development handoff. |
| "We can refine acceptance criteria later." | Late criteria increases rework and inconsistent delivery. |
| "Engineering can infer missing details." | Inference creates hidden decisions and inconsistent outputs. |

## Red Flags - STOP
- "Ship now, clarify later."
- "Criteria are obvious, no need to write."
- "Dependency ownership can be handled in standup."
- "This deadline justifies skipping the handoff gate."

If any red flag appears, stop and restart from Core Pattern step 1.

## TDD for Skills (mandatory)
### RED
- Run pressure scenarios without this skill and capture failures in `skills/product-owner/validation/test-log.md`.

### GREEN
- Re-run the same scenarios with this skill loaded and verify compliant decisions.

### REFACTOR
- Add counters for new rationalizations, then re-run failing scenarios until stable.

## Quality Gate Before Publishing
- [ ] Frontmatter is valid and trigger-focused.
- [ ] Description starts with "Use when..." and stays under 500 characters.
- [ ] Mandatory input/output contract is complete.
- [ ] Deterministic status rules are explicit.
- [ ] Rationalizations observed in RED are explicitly countered.
- [ ] GREEN evidence is recorded in validation logs.
