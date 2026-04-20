---
name: validate-handoff
description: Use when a product/software package is about to be handed to engineering and you need deterministic readiness validation for requirements, rules, acceptance, and dependencies.
---

# Validate Handoff

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** superpowers:test-driven-development
- **REQUIRED SUB-SKILL:** None.

## Overview
This skill validates software handoff readiness before execution starts.
It blocks ambiguous or contradictory packages and enforces explicit dependency ownership.

## When to Use
- Engineering requests implementation-ready input.
- Requirements, rules, or acceptance are incomplete or conflicting.
- Critical dependencies may be unresolved.
- Keywords people will search: handoff readiness, acceptance criteria, dependency owner, gate validation, requirements consistency.

## When NOT to Use
- Workspace artifact discovery and maintenance (use `analyze-workspace`).
- Scope ranking and trade-off prioritization (use `prioritize-scope`).

## Quick Reference
| Situation | Action | Why |
|---|---|---|
| Vague acceptance criteria | Block handoff until criteria are explicit | Prevents implementation drift |
| Dependency owner missing | Require owner + due date | Avoids blocked execution |
| Requirement conflict | Fail gate and request consistency | Prevents contradictory build behavior |

## Implementation
### Core Pattern
1. Validate package completeness: requirements, business rules, acceptance criteria, dependencies.
2. Check internal consistency between requirements and acceptance criteria.
3. Confirm each critical dependency has owner and due date.
4. Mark gates pass/fail with corrective action.
5. Return deterministic status and next action package.

### Mandatory output
| Section | Mandatory content |
|---|---|
| Final status | `approved`, `mandatory_adjustments`, `gate_failed` |
| Gate results | `GATE-*` pass/fail with corrective action |
| Consistency notes | Requirement vs acceptance alignment |
| Dependency map | Owner + due date for each critical dependency |
| Next action | Responsible owner and expected deliverable |

### Deterministic status rules
1. If any gate fails, status = `gate_failed`.
2. If no gate fails but package has pending critical items, status = `mandatory_adjustments`.
3. If all gates pass with no critical pending items, status = `approved`.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Approving epics without explicit criteria | Handoff is not implementation-ready | Require explicit acceptance criteria |
| Auto-assigning dependency owner | Hides accountability contract | Require explicit owner acknowledgment |
| Ignoring requirement contradictions | Produces unpredictable outcomes | Fail gate and fix consistency first |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "We'll detail criteria during sprint." | Late criteria drives rework and inconsistency. |
| "Assigning a default owner is faster." | Unagreed ownership breaks accountability. |
| "Team can interpret contradictions." | Interpretation creates divergent implementations. |

## Red Flags - STOP
- "Approve now, clarify later."
- "Dependencies can be solved in standup."
- "Contradictions are acceptable for speed."

If any red flag appears, restart from Core Pattern step 1.

## TDD for Skills (mandatory)
### RED
- Capture failures without this skill in `skills/validate-handoff/validation/test-log.md`.

### GREEN
- Re-run same scenarios with this skill loaded and verify compliant decisions.

### REFACTOR
- Add counters for new rationalizations, then retest.
