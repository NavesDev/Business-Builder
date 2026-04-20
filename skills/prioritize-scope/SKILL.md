---
name: prioritize-scope
description: Use when multiple scope options compete for limited capacity and decisions need objective prioritization with explicit trade-offs and traceable rationale.
---

# Prioritize Scope

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** superpowers:test-driven-development
- **REQUIRED SUB-SKILL:** None.

## Overview
This skill prioritizes scope using explicit objectives and impact/effort criteria.
It prevents urgency-only or hierarchy-only decisions and enforces clear in-scope/out-of-scope boundaries.

## When to Use
- Capacity is limited and priorities conflict.
- Stakeholders push competing items in the same cycle.
- Teams request “include everything now” shortcuts.
- Keywords people will search: prioritize scope, impact effort, trade-off, scope boundary, MVP ordering.

## When NOT to Use
- Artifact gap discovery and workspace normalization (use `analyze-workspace`).
- Final software handoff readiness validation (use `validate-handoff`).

## Quick Reference
| Situation | Action | Why |
|---|---|---|
| Urgency pressure | Ask explicit objective first, then impact/effort | Avoids reactionary prioritization |
| Stakeholder conflict | Compare options with same criteria and log rationale | Keeps decision auditable |
| Scope inflation | Define in-scope and out-of-scope before ranking | Prevents hidden scope growth |

## Implementation
### Core Pattern
1. Confirm objective and constraint context for the decision window.
2. Define candidate items and explicit in-scope/out-of-scope boundaries.
3. Score each candidate by impact and effort.
4. Resolve ties with strategic fit and dependency risk.
5. Publish ranking with rationale and trade-offs.
6. Record decisions in stable IDs for future iterations.

### Deterministic output
| Section | Mandatory content |
|---|---|
| Final status | `approved`, `mandatory_adjustments`, `gate_failed` |
| Priority decision | Ordered list with objective reference |
| Trade-offs | What was excluded and why |
| Evidence | Impact/effort rationale |
| Decision IDs | Stable IDs (`DEC-*`) |

### Deterministic status rules
1. If objective or scope boundary is missing, status = `mandatory_adjustments`.
2. If priority cannot be justified with explicit criteria, status = `mandatory_adjustments`.
3. If gate constraints fail, status = `gate_failed`.
4. If ordering is explicit and justified, status = `approved`.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Prioritizing by urgency only | Ignores value trade-offs | Use objective + impact/effort |
| Splitting scope politically | Hides true trade-off costs | Rank explicitly and exclude with rationale |
| Letting engineering infer boundaries | Creates drift and rework | Define boundaries before ranking |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "Urgency is enough to decide." | Urgency without objective leads to misaligned outcomes. |
| "Let's split and show progress." | Partial split can maximize waste, not value. |
| "Engineering can infer scope quickly." | Inference hides decisions and breaks accountability. |

## Red Flags - STOP
- "Prioritize now, justify later."
- "Split everything a little."
- "Boundaries are obvious, skip them."

If any red flag appears, restart from Core Pattern step 1.

## TDD for Skills (mandatory)
### RED
- Capture failures without this skill in `skills/prioritize-scope/validation/test-log.md`.

### GREEN
- Re-run same pressure scenarios with this skill loaded.

### REFACTOR
- Add counters for new rationalizations and re-test.
