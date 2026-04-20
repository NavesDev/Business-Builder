---
name: init
description: Use when starting or restructuring a business initiative and you need deterministic intake, workspace bootstrap in business-builder, and validation routing before downstream specification work.
---

# Init

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** superpowers:test-driven-development
- **REQUIRED SUB-SKILL:** None.

## Overview
This skill initializes a unified `business-builder/` workspace and structures the first business intake package.
It enforces mandatory business state classification, protects existing context artifacts, and routes validation to `product-owner` before continuation.

## When to Use
- New initiative with no structured business artifacts yet.
- Existing business needs improvement and artifacts are partial/outdated.
- Business is in construction and needs deterministic continuation rules.
- Keywords people will search: init workspace, business intake, `business-builder`, idea.md, users.md, product-owner validation.

## When NOT to Use
- Deep product-management analysis (use `product-management`).
- Final dev handoff package generation (use output skill).
- Viability/go-no-go ownership decisions outside the validation flow.

## Quick Reference
| Situation | Action | Why |
|---|---|---|
| Missing `business_state` | Return `mandatory_adjustments` with missing field list | Prevents wrong routing |
| State is `existente` or `em_construcao` | Create/update `idea.md` and `users.md` | Preserves continuity |
| Intake complete | Route package to `product-owner` | Enforces quality gate |
| User pressures for direct output | Refuse bypass and keep validation order | Avoids rework and ownership drift |

## Implementation
### Core Pattern
1. Collect mandatory intake fields: idea, `business_state` (`novo|existente|em_construcao`), objective, audience, constraints, stage, assumptions.
2. Ensure `business-builder/` exists before any artifact generation.
3. If `business_state` is `existente` or `em_construcao`, create `idea.md`/`users.md` when missing and update when present.
4. Write normalized context artifacts in `business-builder/context/`.
5. Prepare handoff package and send to `product-owner` for validation.
6. Return deterministic status.

### Mandatory skill output
| Section | Mandatory content |
|---|---|
| Final status | `approved`, `mandatory_adjustments`, `gate_failed` |
| Intake summary | 3-5 lines of normalized context |
| Missing fields | Explicit list or `none` |
| Artifacts initialized | Paths created/updated in `business-builder/` |
| Validation route | `product-owner` + expected validation outcome |

### Deterministic gate rules
1. If `business_state`, objective, or audience is missing, status = `mandatory_adjustments`.
2. If `business_state` is `existente` or `em_construcao`, `idea.md` and `users.md` must follow create-or-update behavior.
3. Validation must go through `product-owner` before downstream output artifacts.
4. If required artifacts and validation routing are complete, status = `approved`.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Assuming `business_state` | Breaks deterministic flow | Require explicit state |
| Recreating existing artifacts from zero | Discards valid context | Update existing files and create only missing ones |
| Skipping `product-owner` gate | Breaks ownership and readiness control | Route validation before continuation |
| Generating RF/RNF inside init | Mixes responsibilities | Keep init as intake/orchestration only |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "Skipping state discovery speeds delivery." | Speed without state creates invalid routing and rework. |
| "Let's bypass validation to generate docs now." | Bypassing validation shifts risk downstream and breaks ownership. |
| "Recreating all files is cleaner." | Destroying context loses business signal needed for continuity. |

## Red Flags - STOP
- "Assume `novo` and continue."
- "Skip `business_state` to save time."
- "Bypass `product-owner` and generate RF/RNF now."
- "Discard old `idea.md` and start from zero."

If any red flag appears, restart from Core Pattern step 1.

## TDD for Skills (mandatory)
### RED
- Capture baseline failures without this skill in `skills/init/validation/test-log.md`.

### GREEN
- Re-run the same pressure scenarios with this skill loaded.

### REFACTOR
- Add new rationalizations and explicit counters, then retest.

## Quality Gate Before Publishing
- [ ] Frontmatter is valid and trigger-focused.
- [ ] Description starts with "Use when..." and stays under 500 characters.
- [ ] Deterministic gate rules are explicit.
- [ ] Rationalizations observed in RED are countered.
- [ ] GREEN evidence is recorded in validation logs.
