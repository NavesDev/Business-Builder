---
name: analyze-workspace
description: Use when decisions are about to be made from project artifacts and you need a deterministic workspace analysis flow with create-or-update behavior before downstream planning.
---

# Analyze Workspace

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** superpowers:test-driven-development
- **REQUIRED SUB-SKILL:** None.

## Overview
This skill analyzes workspace artifacts before strategic or delivery decisions are made.
It enforces a default root (`.business-builder`), discovery-first gap handling, and deterministic create-or-update artifact lifecycle.

## When to Use
- Artifacts exist but quality/completeness is unknown.
- Teams want to move fast and risk skipping workspace checks.
- Missing or outdated files may compromise prioritization and handoff.
- Keywords people will search: workspace analysis, `.business-builder`, missing artifact, outdated artifact, create or update.

## When NOT to Use
- Prioritizing scope decisions (use `prioritize-scope`).
- Final readiness gate for software handoff (use `validate-handoff`).

## Quick Reference
| Situation | Action | Why |
|---|---|---|
| Artifact missing | Ask focused questions, then create file | Prevents inferred data drift |
| Artifact outdated | Update with validated inputs | Avoids stale decisions |
| Non-default path request | Ask for explicit user confirmation | Prevents unsafe override |

## Implementation
### Core Pattern
1. Use `.business-builder/` as default analysis root.
2. If another path is proposed, require explicit user confirmation before override.
3. Inspect required artifacts for completeness and freshness.
4. Ask focused discovery questions for missing critical data.
5. Create missing artifacts and update existing outdated artifacts.
6. Return structured analysis output and unresolved critical gaps.

### Required artifacts (default)
| Artifact | Minimum checks | Lifecycle rule |
|---|---|---|
| `.business-builder/idea.md` | Objective, value proposition, constraints | Create if missing, update if outdated |
| `.business-builder/users.md` | Segment, goals, pains, priority | Create if missing, update if outdated |
| `.business-builder/context/brief.md` | Audience, stage, assumptions | Create if missing, update if outdated |
| `.business-builder/context/decisions.md` | Stable IDs, rationale, owner/date | Create if missing, append/update safely |

### Deterministic status rules
1. If critical data is missing, run discovery first (no immediate hard-block).
2. If critical data still missing after discovery + create/update cycle, status = `mandatory_adjustments`.
3. If artifact analysis completes with no critical gaps, status = `approved`.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Inferring missing artifact content | Produces unverifiable assumptions | Ask and create artifact from explicit inputs |
| Trusting outdated artifact | Creates stale recommendations | Update artifact before output |
| Overriding root without confirmation | Breaks deterministic scope | Require explicit override approval |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "I can infer users to save time." | Inference corrupts traceability and quality. |
| "Let's keep old artifact just for speed." | Stale context causes wrong downstream decisions. |
| "I'll check both roots to be safe." | Multi-root analysis without consent creates scope ambiguity. |

## Red Flags - STOP
- "Infer now, document later."
- "Old artifact is probably good enough."
- "Use alternate folder without asking."

If any red flag appears, restart from Core Pattern step 1.

## TDD for Skills (mandatory)
### RED
- Run pressure scenarios without this skill and log failures in `skills/analyze-workspace/validation/test-log.md`.

### GREEN
- Re-run the same scenarios with this skill loaded and verify compliant behavior.

### REFACTOR
- Add counters for new rationalizations and retest.
