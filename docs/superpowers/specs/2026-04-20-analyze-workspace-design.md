# Analyze Workspace Skill Design

## Problem
The repository may or may not contain a root `business-builder/` workspace with business-service artifacts. We need a skill that inspects only this workspace and returns a structured diagnostic (RF, RNF, business rules, and gaps) without mutating files.

## Approved Scope
1. Analyze only `business-builder/` at repository root.
2. Never create, edit, or delete files.
3. If `business-builder/` does not exist or is empty, return an explicit message that there is no business base to extract requirements/rules.
4. If it exists, produce chat output with:
   - Context summary
   - Functional requirements
   - Non-functional requirements
   - Business rules
   - Gaps/unknowns
   - Confidence level

## Approach Options Considered
- **A (approved):** strict analysis of `business-builder/` only, explicit absence messaging.
- B: fallback to full-repository analysis.
- C: analyze only docs/skills.

## Behavior Contract
### Input assumptions
- Root path available.
- Optional root folder: `business-builder/`.

### Output contract
- Plain chat diagnosis, deterministic section order:
  1. Context found
  2. Functional requirements
  3. Non-functional requirements
  4. Business rules
  5. Gaps and pending items
  6. Confidence level

### Definition of "gaps and pending items"
Add an item to this section when at least one condition applies:
- **Coverage gap:** a required business dimension has no supporting evidence (e.g., missing acceptance criteria, SLA/performance target, or owner).
- **Ambiguity:** wording allows more than one interpretation and cannot be resolved from current files.
- **Conflict:** two or more sources define incompatible behavior, rules, or constraints.
- **Traceability gap:** a requirement/rule exists but lacks source pointer or rationale.
- **Dependency gap:** a requirement depends on an external policy/system not described inside `business-builder/`.

Use one tag per item: `GAP-COVERAGE`, `GAP-AMBIGUITY`, `GAP-CONFLICT`, `GAP-TRACEABILITY`, `GAP-DEPENDENCY`.

### Definition of "confidence level"
Confidence is assigned from evidence quality in `business-builder/` only:
- **High:** findings are explicit, consistent, and confirmed by multiple reliable sources.
- **Medium:** most findings are explicit, but depth is limited or minor ambiguities remain.
- **Low:** sparse or conflicting evidence requires substantial inference.

Mandatory confidence fields:
- `level`: High | Medium | Low
- `rationale`: 1-2 lines explaining why this level was assigned
- `drivers`: short list of the main factors (coverage, consistency, traceability)

### Error and edge handling
- Missing folder: return absence message (no speculative inference).
- Empty folder: same absence message.
- Unsupported/binary files: ignore and continue.
- Contradictory sources: list under gaps with low confidence tag.

## Non-Goals
- No requirements synthesis from outside `business-builder/`.
- No document generation.
- No auto-remediation or workspace bootstrap.

## Testing Plan for Skill Authoring (TDD for skills)
1. **RED:** run pressure scenarios without skill, verify common failure modes:
   - analyzes outside target folder
   - invents requirements when folder missing
   - writes files instead of reporting
2. **GREEN:** implement minimal skill instructions to block these failures.
3. **REFACTOR:** add explicit counters for rationalizations and re-test.
