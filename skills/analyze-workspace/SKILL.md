---
name: analyze-workspace
description: Use when checking whether an existing business-builder workspace already contains enough evidence to extract functional requirements, non-functional requirements, business rules, and explicit gaps.
---

# Analyze Workspace

## Overview
This is a read-only analysis skill for an existing `business-builder/` folder at repository root.

It extracts evidence and returns a structured diagnosis in chat. It never creates, edits, or deletes files.

## When to Use
- You need to understand what business requirements already exist.
- You need to identify missing requirement evidence before downstream skills.
- You need a quick RF/RNF/business-rules diagnosis from current workspace artifacts.

## Hard Rules
1. Analyze only `business-builder/` at repository root.
2. If `business-builder/` is missing or empty, return this exact message:
   - `No business-builder workspace found (or it is empty), so there is no business base to extract requirements or rules yet.`
3. Never synthesize evidence from `docs/`, `skills/`, or other folders.
4. Never create, update, or delete files.
5. Do not infer full requirements when evidence is missing; report gaps instead.

## Analysis Workflow
1. Confirm whether `business-builder/` exists and has files.
2. Collect relevant text evidence inside `business-builder/`.
3. Build a diagnosis using this exact section order:
   1. Context found
   2. Functional requirements
   3. Non-functional requirements
   4. Business rules
   5. Gaps and pending items
   6. Confidence level

## Classification Rules

### Functional requirements
User-visible capabilities, business processes, inputs/outputs, validations, and expected outcomes.

### Non-functional requirements
Performance, security, compliance, reliability, observability, maintainability, scalability, and operational constraints.

### Business rules
Deterministic decision rules, eligibility/approval criteria, calculation policies, thresholds, lifecycle rules, and governance constraints.

## Gaps and Pending Items
Add a gap when at least one condition applies:
- `GAP-COVERAGE`: required dimension has no evidence (owner, acceptance criteria, KPI, SLA, policy)
- `GAP-AMBIGUITY`: statement allows multiple interpretations
- `GAP-CONFLICT`: contradictory statements across sources
- `GAP-TRACEABILITY`: finding has no source pointer or rationale
- `GAP-DEPENDENCY`: requirement depends on undefined external system/policy

Each gap should include:
- `id`
- `tag`
- `description`
- `impact`
- `required-clarification`

## Confidence Level
Use only evidence quality from `business-builder/`.

- **High**: explicit, consistent, multi-source evidence
- **Medium**: mostly explicit evidence with minor ambiguity
- **Low**: sparse or conflicting evidence requiring inference

Return:
- `level`: High | Medium | Low
- `rationale`: 1-2 lines
- `drivers`: key factors (coverage, consistency, traceability)

## Output Template
Use this shape in chat:

```markdown
## Context found
...

## Functional requirements
- FR-001: ...

## Non-functional requirements
- NFR-001: ...

## Business rules
- BR-001: ...

## Gaps and pending items
- GAP-001 (`GAP-COVERAGE`): ...

## Confidence level
- level: ...
- rationale: ...
- drivers: ...
```

## Rationalization Guards
- "I can use docs for context" -> No. Out of scope.
- "I should generate requirement files now" -> No. This skill is analysis-only.
- "I can infer everything if folder is missing" -> No. Return the exact absence message.
