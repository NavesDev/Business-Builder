---
name: product-owner
description: Use when business-to-delivery decisions need coordinated execution across workspace analysis, scope prioritization, and software handoff validation in a deterministic sequence.
---

# Product Owner

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** None.
- **REQUIRED SUB-SKILL:** `analyze-workspace`, `prioritize-scope`, `validate-handoff`.

## Overview
This skill is an orchestrator. It coordinates three specialized skills to keep business decisions traceable and implementation handoff reliable.
It does not replace those skills and must not skip their sequence.

## When to Use
- You need end-to-end product-owner flow from context to readiness gate.
- Teams are under pressure and risk skipping analysis or handoff quality.
- Multiple stakeholders require a single coordinated decision path.
- Keywords people will search: product owner orchestration, workspace analysis, scope prioritization, handoff validation.

## When NOT to Use
- Isolated artifact analysis (use `analyze-workspace` directly).
- Isolated scope ranking (use `prioritize-scope` directly).
- Isolated software handoff checks (use `validate-handoff` directly).

## Quick Reference
| Stage | Skill | Output |
|---|---|---|
| 1 | `analyze-workspace` | Updated workspace artifacts + critical gaps |
| 2 | `prioritize-scope` | Ranked scope + explicit trade-offs |
| 3 | `validate-handoff` | Readiness status + corrective actions |

## Implementation
### Orchestration Pattern
1. Run `analyze-workspace` with `business-builder` as default root (or explicit override).
2. If critical data remains missing after create/update cycle, return `mandatory_adjustments`.
3. Run `prioritize-scope` using objective + impact/effort criteria.
4. Run `validate-handoff` to verify readiness package consistency.
5. Publish final status and next action package.

### Deterministic status rules
1. If any orchestrated stage returns `gate_failed`, final status = `gate_failed`.
2. If no stage fails but at least one returns `mandatory_adjustments`, final status = `mandatory_adjustments`.
3. If all stages return `approved`, final status = `approved`.
4. Stage order is mandatory and cannot be bypassed.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Jumping to prioritization before analysis | Uses stale/missing context | Always run `analyze-workspace` first |
| Skipping handoff validation | Releases ambiguous package | Always run `validate-handoff` last |
| Treating orchestrator as monolith | Blurs responsibilities | Keep logic in specialized skills |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "We can skip analysis this time." | Skipping analysis propagates bad assumptions. |
| "Prioritization is enough; handoff can wait." | Unvalidated handoff creates execution risk. |
| "Product-owner should decide everything directly." | Monolithic flow removes clarity and reuse. |

## Red Flags - STOP
- "Run only one stage to save time."
- "Skip analyze-workspace."
- "Skip validate-handoff."
- "Let engineering infer missing details."

If any red flag appears, restart from Orchestration Pattern step 1.

## TDD for Skills (mandatory)
### RED
- Run orchestration pressure scenarios without this skill and capture failures in `skills/product-owner/validation/test-log.md`.

### GREEN
- Re-run same scenarios with this skill loaded and verify sequence-compliant behavior.

### REFACTOR
- Add counters for new rationalizations and retest.
