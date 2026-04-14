# Init Skill Orchestration Design

## Problem
The project needs an entry skill (`init`) that does more than scaffold folders: it must capture the core business idea scope, structure the initial business context, and orchestrate handoff to downstream skills without prematurely validating final product output.

## Approved Approach
Use an orchestration-first `init` skill:
1. Collect and structure core business context.
2. Persist context and management artifacts in a canonical workspace tree.
3. Handoff to `product-management` for pre-product management analysis.
4. Leave final development package generation to a separate output skill.

This keeps responsibilities separated:
- `init`: intake and structuring
- `product-management`: pre-product business management depth
- output skill: final dev-facing deliverables (RF/RNF/BR/CA/backlog)

## Alternatives Considered
1. **Init first (selected):** provides end-to-end workflow early with clear role boundaries.
2. Skills first, init later: better isolated quality per skill but no unified intake flow.
3. Parallel hybrid: faster parallel progress but higher consistency risk.

## Target Workspace Structure
```text
business-builder/
  context/
    brief.md
    decisions.md
  product-management/
    rules.md
    users.md
    finance.md
    risks.md
  product-output/
    product-spec.md
    requirements-rf.md
    requirements-rnf.md
    business-rules.md
    acceptance-criteria.md
    backlog.md
```

## Component Responsibilities

### 1) `init` skill
- Ask for core idea inputs (idea, objective, audience, constraints, stage, assumptions).
- Normalize and write `context/brief.md`.
- Register global decisions in `context/decisions.md` with stable IDs (`DEC-*`).
- Prepare handoff packet to `product-management` (no final product validation decision).

### 2) `product-management` skill
- Own all pre-product management outputs:
  - Product/business rules
  - Actors/users model
  - Financial scope and guardrails
  - Risks and management notes
- Write/manage artifacts in `product-management/`.

### 3) Output skill (separate)
- Consume `context/` + `product-management/`.
- Produce final dev-facing package in `product-output/`:
  - RF, RNF, BR, acceptance criteria, and backlog.

## Data Flow
1. User triggers `init`.
2. `init` gathers and structures core scope in `context/`.
3. `product-management` deepens pre-product management artifacts.
4. Output skill compiles final development package.

## Status and Error Handling
- If critical input is missing during `init` (e.g., objective or audience), return status `mandatory_adjustments` and list missing fields.
- `init` must not generate incomplete `product-output/` artifacts.
- Only the output skill is responsible for final dev handoff package completeness.

## Testing Strategy
Use skill-level TDD with validation artifacts:
- `skills/init/validation/pressure-scenarios.md`
- `skills/init/validation/test-log.md`

Minimum pressure scenarios:
1. Confused/overbroad scope under time pressure.
2. Missing budget or financial constraints.
3. Contradictory objective vs audience inputs.

Validation mode:
- RED: run without `init` and capture poor structuring behavior.
- GREEN: run with `init` and verify structured context output + proper status.
- REFACTOR: harden against new rationalizations and retest.

## Out of Scope
- Building persistence/database engine.
- Implementing final output skill logic in this step.
- Replacing role-specific skills with `init`.

## Success Criteria
1. `init` consistently creates `business-builder/context/*` with usable quality.
2. `init` prepares, but does not finalize, product dev outputs.
3. Responsibility boundaries between `init`, `product-management`, and output skill are explicit and non-overlapping.
