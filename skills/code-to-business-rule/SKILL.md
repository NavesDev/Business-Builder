---
name: code-to-business-rule
description: Extract FR/NFR/BR and explicit gaps from code evidence in projects with little or no documentation, using deterministic traceable rules.
---

# Code to Business Rule

## Overview
This skill converts code evidence into structured requirement artifacts:
- Functional requirements (FR)
- Non-functional requirements (NFR)
- Business rules (BR)
- Gaps and pending clarifications (GAP)

Core principle: no silent inference without evidence traceability.

## When to Use
- A project is mostly implemented but lacks business documentation.
- You need a first-pass business-rules baseline grounded in code.
- You want explicit uncertainty handling before creating tests.

## Hard Rules
1. Analyze only user-approved target project scope.
2. Prioritize evidence from: domain/use-cases, validations, automated tests.
3. Every FR/NFR/BR must include source references.
4. If evidence conflicts, emit `GAP-CONFLICT`.
5. If meaning is ambiguous, emit `GAP-AMBIGUITY` and ask one clarification question.
6. Never finalize with unresolved blocking gaps.
7. Do not claim confidence higher than evidence supports.
8. Never fabricate requirements to "complete" output.

## Inputs
- Target project path.
- Optional module boundaries.
- Optional business terms glossary from user.

## Workflow
1. Discover evidence and build source index.
2. Extract candidate FR/NFR/BR from deterministic patterns.
3. Normalize and deduplicate candidates.
4. Classify confidence (`Explicit`, `Supported`, `Inferred`).
5. Generate structured gaps (`GAP-COVERAGE`, `GAP-AMBIGUITY`, `GAP-CONFLICT`, `GAP-TRACEABILITY`, `GAP-DEPENDENCY`).
6. Run clarification loop for blocking gaps (one question at a time).
7. Write output artifacts.

## Output Structure
Write/update:
- `business-builder/requirements/functional-requirements.md`
- `business-builder/requirements/non-functional-requirements.md`
- `business-builder/requirements/business-rules.md`
- `business-builder/requirements/gaps-and-pending-items.md`

## Output Contract (Chat)
Return:
1. Files created/updated.
2. Totals for FR/NFR/BR/GAP.
3. Blocking gaps resolved through clarification.
4. Confidence summary and unresolved non-blocking items.

## Rationalization Guards
- "I can infer this silently because it is obvious." -> No. Add source or gap.
- "I can ignore contradictory sources." -> No. Emit `GAP-CONFLICT`.
- "I can finish with unresolved ambiguity." -> No. Keep blocked.
