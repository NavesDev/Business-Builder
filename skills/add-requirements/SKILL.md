---
name: add-requirements
description: Use when converting a free-form user request into structured requirements documentation in a resolved business-builder workspace with strict BDD and INVEST quality gates.
---

# Add Requirements

## Overview
This skill transforms a natural-language user request into high-quality requirements documentation under the resolved `business-builder` workspace `requirements/` folder.

Core principle: **no final delivery without full BDD + INVEST compliance**.

## When to Use
- A user provides an idea or request in free-form text.
- You need formal requirements documentation before planning or implementation.
- Requirements must be testable, traceable, and unambiguous.
- You must keep outputs inside the resolved `business-builder` workspace.

Do not use this skill to implement code.

## Hard Rules
1. Before any write operation, run **analyze-workspace** to resolve architecture/workspace and baseline requirement evidence.
2. Work only inside the resolved `business-builder` workspace.
3. Output documentation in English.
4. Use BDD (`Given/When/Then`) for every user story.
5. Validate every requirement/story with INVEST.
6. If any quality gate fails, block final delivery.
7. Never finish in warnings-only mode.
8. For failed items, use guided clarification questions (one at a time) until all gates pass.
9. Use incremental merge behavior; do not destructively rewrite unless explicitly requested.

## Inputs
- Primary input: user request in natural language.
- Optional input: existing docs in `<resolved-workspace>/requirements/`.

## Workspace Resolution Dependency
This skill depends on `analyze-workspace` for path resolution in modular layouts.

Accepted workspace locations:
1. `docs/business-builder/`
2. `apps/*/docs/business-builder/` (if multiple, ask user to choose)
3. `business-builder/` (legacy repository-root layout)

If no workspace exists, ask the user where to create it and only proceed after explicit confirmation.

## Workflow
1. Run `analyze-workspace` first to identify current architecture and existing requirement evidence.
2. Intake the user request.
3. Normalize context:
   - actors
   - goals
   - constraints
   - assumptions
   - business terms
4. Extract candidate requirements:
   - functional requirements
   - non-functional requirements
   - user stories
   - acceptance criteria
5. Convert user stories to BDD scenarios.
6. Apply INVEST validation to each requirement/story.
7. If all items pass, write/update output files.
8. If any item fails, enter Guided Refinement Loop.
9. Update traceability mapping from source request to generated items.

## BDD Rules
For each user story:
- Include at least one `Given`.
- Include at least one `When`.
- Include at least one `Then`.
- `Then` must be measurable and testable.
- Reject vague outcomes (for example: "works well", "better UX", "fast enough") unless made measurable.

## INVEST Validation
Evaluate each item against:
- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

If any INVEST dimension fails, mark the item as blocked and move it to guided refinement.

## Guided Refinement Loop
When a requirement/story fails BDD or INVEST:
1. Ask one targeted clarification question focused on the highest-impact gap.
2. Apply the answer only to affected items.
3. Re-run BDD + INVEST validation for affected items.
4. Repeat until all items pass.

### Clarification Strategy
- Prefer specific multiple-choice questions when possible.
- If needed, ask short free-form questions.
- Resolve conflicts explicitly by asking the user to choose one interpretation.
- Keep output blocked while conflicts or ambiguities remain.

## Output Structure
Write/update inside `<resolved-workspace>/requirements/`:
- `functional-requirements.md`
- `non-functional-requirements.md`
- `user-stories-bdd.md`
- `acceptance-criteria.md`
- `requirements-traceability.md`

## Merge Strategy
- Preserve valid existing content.
- Update entries by stable identifiers when available.
- Append new entries when no identifier match exists.
- Never silently delete existing content.
- Full replacement is allowed only when the user explicitly requests it.

## File Content Expectations

### functional-requirements.md
- FR IDs (`FR-001`, `FR-002`, ...)
- concise description
- rationale/business value

### non-functional-requirements.md
- NFR IDs (`NFR-001`, `NFR-002`, ...)
- measurable quality constraints (performance, security, reliability, etc.)

### user-stories-bdd.md
- Story IDs (`US-001`, `US-002`, ...)
- story statement
- BDD scenarios (`Given/When/Then`)

### acceptance-criteria.md
- AC IDs (`AC-001`, `AC-002`, ...)
- objective pass/fail criteria linked to FR/NFR/US

### requirements-traceability.md
- source-to-requirement mapping
- links among FR/NFR/US/AC
- notes about clarifications that changed scope/meaning

## Quality Gate Before Final Delivery
Final delivery is allowed only when:
1. All stories contain valid BDD scenarios.
2. All requirements/stories pass INVEST.
3. All acceptance criteria are testable.
4. All unresolved ambiguities/conflicts are cleared.
5. Traceability mapping is complete.

If any check fails, continue Guided Refinement Loop.

## Output Contract (Chat)
Return a concise summary with:
1. Files created/updated in `<resolved-workspace>/requirements/`.
2. Total requirements/stories accepted.
3. Clarification questions used to resolve blocked items.
4. Confirmation that all BDD + INVEST gates passed.

## Rationalization Guards
- "This is good enough with warnings." -> No. Keep blocked until all gates pass.
- "I can infer missing constraints silently." -> No. Ask a clarification question.
- "BDD is optional for simple stories." -> No. Every story requires Given/When/Then.
- "INVEST can be partial this time." -> No. All six dimensions must pass.
