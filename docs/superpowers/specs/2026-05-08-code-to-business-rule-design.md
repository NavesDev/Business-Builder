# Code-to-Business-Rule Skill Design (v1)

## 1. Problem and Goal
Many projects have mature code but no business documentation. The goal of this skill is to produce a reliable first-pass requirements package from code evidence, focused on:
- Functional requirements (FR)
- Non-functional requirements (NFR)
- Business rules (BR)
- Explicit gaps and pending clarifications (GAP)

The skill must prioritize traceability and avoid silent invention of rules.

## 2. Scope (v1)
### In scope
- Analyze domain/use-case logic, validations, and automated tests.
- Extract FR/NFR/BR candidates with source pointers.
- Classify confidence per extracted item.
- Generate structured gap items and block on critical ambiguity.
- Write output in English under `business-builder/requirements/`.

### Out of scope
- Automatic generation of full BDD stories.
- Automatic acceptance criteria and full traceability matrix generation.
- Deep UI/infra behavior mining.
- Automatic code fixes to align code with documented rules.

## 3. Architecture
The skill follows a deterministic evidence pipeline:

1. **Evidence Discovery**
   - Scan only approved sources: domain/use-cases, validations, tests.
   - Build an evidence index with `source_refs` (file path + snippet reference).

2. **Rule Extraction**
   - Detect candidate FR/NFR/BR from explicit patterns:
     - conditionals and eligibility checks
     - thresholds and limits
     - state/lifecycle transitions
     - calculation policies
     - validation constraints

3. **Confidence Scoring**
   - `Explicit` (high): direct rule in code/tests.
   - `Supported` (medium): strong supporting evidence, minor interpretation.
   - `Inferred` (low): plausible but indirect interpretation.

4. **Gap Engine**
   - Emit structured gaps:
     - `GAP-COVERAGE`
     - `GAP-AMBIGUITY`
     - `GAP-CONFLICT`
     - `GAP-TRACEABILITY`
     - `GAP-DEPENDENCY`
   - Block and ask one clarification question at a time for critical gaps.

5. **Writers**
   - Produce:
     - `business-builder/requirements/functional-requirements.md`
     - `business-builder/requirements/non-functional-requirements.md`
     - `business-builder/requirements/business-rules.md`
     - `business-builder/requirements/gaps-and-pending-items.md`

## 4. Data Flow
1. Input: target project path and optional module scope.
2. Collect evidence from approved layers.
3. Extract candidate FR/NFR/BR items with `source_refs`.
4. Normalize and deduplicate while preserving rationale.
5. Assign confidence levels.
6. Generate gaps.
7. If blocking gaps exist, run clarification loop (one question at a time).
8. Write final requirement artifacts.

## 5. Decision Rules
- No `source_refs` => item cannot be high confidence.
- Contradictory evidence => mandatory `GAP-CONFLICT`.
- Ambiguous critical rule => block output finalization until clarified.
- Inferred items must stay explicitly labeled as inferred.
- Never silently promote low-confidence inference to explicit rule.

## 6. Error Handling
- Invalid target path or no analyzable files: fail with actionable message.
- Parser failure on specific file: record partial analysis and explicit warning.
- Unresolved blocking ambiguity: keep generation blocked and request user input.

## 7. Quality and Test Strategy
Use the repository validation protocol for skills:
- `skills/code-to-business-rule/validation/pressure-scenarios.md`
- `skills/code-to-business-rule/validation/test-log.md`

Minimum GREEN checks for v1:
1. Extract explicit BR from conditional validation.
2. Extract threshold/cap policy from code or tests.
3. Raise `GAP-AMBIGUITY` for multi-interpretation behavior.
4. Raise `GAP-CONFLICT` for contradictory evidence.
5. Prevent promotion of unsupported inference.

## 8. Expected Outcome
The skill provides a high-value documentation baseline for teams with legacy or undocumented systems, enabling faster unit test authoring and code-to-rule conformance auditing while keeping uncertainty explicit.
