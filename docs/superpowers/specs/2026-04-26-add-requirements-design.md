# Add Requirements Skill Design

## Context
We need a new skill at `skills/add-requirements/SKILL.md` that transforms a user request (free-form text) into high-quality requirements documentation inside `business-builder/`.

The skill must:
- enforce BDD (`Given/When/Then`) and INVEST quality,
- output documentation in English,
- write to `business-builder/`,
- use incremental merge behavior (not full overwrite),
- block final delivery until quality gates pass,
- use guided follow-up questions to close gaps when validation fails.

## Goal
Define a deterministic, efficient, and maintainable skill contract for `add-requirements` that produces requirement artifacts ready for downstream planning and implementation.

## Recommended approach (approved)
Adopt a **hybrid approach**:
1. A strict execution pipeline (for consistency and quality gates).
2. Reusable per-file templates (for maintainability and output quality).

This balances predictability, speed, and long-term maintainability.

## Skill architecture
1. **Input intake**: receive user request in natural language.
2. **Normalization**: extract actors, objectives, constraints, assumptions, and domain terms.
3. **Candidate extraction**: derive candidate requirements and user stories.
4. **BDD shaping**: convert stories into clear Given/When/Then scenarios.
5. **INVEST validation**: evaluate each item against Independent, Negotiable, Valuable, Estimable, Small, Testable.
6. **Quality gate**:
   - If all items pass: proceed to write outputs.
   - If any item fails: enter guided refinement loop.
7. **Guided refinement loop**:
   - Ask one targeted question at a time to remove ambiguity or missing data.
   - Revalidate impacted items after each answer.
   - Repeat until all items pass.
8. **Persist outputs**: update requirement docs in `business-builder/requirements/` using merge semantics.
9. **Traceability update**: maintain mapping from source request to generated artifacts.

## Output structure (approved)
The skill writes/updates:
- `business-builder/requirements/functional-requirements.md`
- `business-builder/requirements/non-functional-requirements.md`
- `business-builder/requirements/user-stories-bdd.md`
- `business-builder/requirements/acceptance-criteria.md`
- `business-builder/requirements/requirements-traceability.md`

## Merge strategy
- Preserve existing valid content.
- Update by stable identifiers when available.
- Append new items when no identifier match exists.
- Avoid destructive rewrites unless explicitly requested by the user.

## Quality gates
For each requirement/story:
- BDD scenario is explicit and testable.
- INVEST passes in full.
- Language is unambiguous and concise.
- Acceptance criteria are objectively verifiable.

If any gate fails:
- Final output remains blocked.
- Skill performs guided, sequential clarification questions.
- No "warnings-only completion" path is allowed.

## Error handling behavior
- Missing critical context triggers clarifying questions, not silent assumptions.
- Contradictions are surfaced explicitly and resolved through user confirmation.
- Unresolvable ambiguity keeps output blocked until clarified.

## Efficiency principles
- Keep wording concise and non-redundant.
- Prefer deterministic templates for repeatability.
- Minimize back-and-forth by asking highest-impact clarification first.
- Revalidate only affected items after each clarification.

## Success criteria
The skill is successful when:
1. Output files exist under `business-builder/requirements/`.
2. Every generated story has valid BDD scenarios.
3. Every generated requirement/story passes INVEST.
4. Traceability links source request to produced artifacts.
5. No blocked issue remains unresolved at final delivery.

## Scope boundaries
In scope:
- Requirement documentation generation and refinement inside `business-builder/`.

Out of scope:
- Code implementation,
- architectural refactoring outside requirement docs,
- changes outside configured output scope unless user explicitly requests them.
