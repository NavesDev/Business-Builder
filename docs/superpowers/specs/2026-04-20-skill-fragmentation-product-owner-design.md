# Product Owner Skill Fragmentation Design

## Problem
The current `product-owner` skill concentrates too many responsibilities in one document. This reduces clarity, weakens discoverability by intent, and makes behavior less deterministic under pressure scenarios.

## Approved Approach
Fragment behavior into clear verb-based skills in English, while keeping `product-owner` as an orchestrator:
1. `analyze-workspace` (generic)
2. `prioritize-scope`
3. `validate-handoff` (focused on product/software handoff)
4. `product-owner` remains as an orchestration entrypoint that routes in sequence.

## Scope
In scope:
- Define contracts and boundaries for the three new skills.
- Redefine `product-owner` as orchestrator.
- Keep `business-builder/` as default workspace root with explicit override support.

Out of scope:
- Replacing the business artifact model.
- Expanding into additional domains beyond product/software handoff for `validate-handoff`.

## Target Skill Set
### 1) `analyze-workspace`
- Purpose: inspect workspace artifacts, identify gaps, and normalize context before decisions.
- Default target: `business-builder/`.
- Override: allowed only when explicitly requested by user.
- Lifecycle rule: ask questions, create missing artifacts, update existing/outdated artifacts.

### 2) `prioritize-scope`
- Purpose: rank scope using explicit objective and impact/effort criteria.
- Output: prioritized scope decisions with rationale and traceability.
- Pressure behavior: no priority decision by hierarchy-only or urgency-only shortcuts.

### 3) `validate-handoff`
- Purpose: validate software/product readiness package before execution.
- Focus checks: requirements clarity, business rules consistency, acceptance criteria quality, dependency ownership.
- Output: deterministic readiness status with corrective actions when needed.

### 4) `product-owner` (orchestrator)
- Purpose: coordinate the three skills in deterministic order.
- Sequence:
  1. `analyze-workspace`
  2. `prioritize-scope`
  3. `validate-handoff`

## Status and Decision Rules
- No immediate hard-block when artifacts are missing.
- First action is discovery + artifact create/update cycle.
- `mandatory_adjustments` only when critical data remains missing after that cycle.
- Preserve deterministic outputs (`approved`, `mandatory_adjustments`, `gate_failed`) for orchestration compatibility.

## Situation Standards (cross-skill)
1. Deadline pressure: do not skip analysis or quality gates.
2. Incomplete data: run focused question loops and persist answers in artifacts.
3. Stakeholder conflict: use objective criteria and record decision rationale.

## Migration Strategy
1. Introduce the 3 new skills with narrow responsibilities.
2. Reduce `product-owner` to orchestration semantics and references to new skills.
3. Update validation scenarios/logs to test orchestration and role boundaries.
4. Keep backward compatibility by preserving `product-owner` entrypoint.

## Testing Impact
- Add pressure scenarios per new skill plus orchestration scenarios.
- Validate that each skill rejects out-of-scope actions.
- Validate that orchestrator respects order and does not bypass steps.

## Success Criteria
1. Skills are verb-based, clear, and single-purpose.
2. `analyze-workspace` is generic with `business-builder` default + explicit override.
3. `validate-handoff` is explicitly product/software-focused.
4. `product-owner` acts as orchestrator, not monolith.
5. Pressure scenarios confirm no “skip analysis for speed” loophole.
