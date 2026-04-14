# Product Owner Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and validate `skills/product-owner/SKILL.md` as a role-based, documentation-driven skill that operationalizes scope definition, backlog prioritization, acceptance criteria, and cross-functional handoffs.

**Architecture:** Use RED-GREEN-REFACTOR for skill authoring. Start with baseline failure scenarios without the skill, write a minimal Product Owner skill grounded in `BUSINESS_DOCUMENTAION.md`, then pressure-test and refactor against rationalizations. Keep outputs deterministic and aligned with the role-based naming and file layout convention.

**Tech Stack:** Markdown (GitHub-flavored), git, shell utilities (`grep`, `awk`, `wc`), Copilot task/subagent workflow.

---

## File Structure and Responsibilities

- Create: `skills/product-owner/SKILL.md`  
  Canonical role-based skill for Product Owner decisions and outputs.

- Create: `skills/product-owner/validation/pressure-scenarios.md`  
  Baseline/pressure scenarios used for RED and GREEN cycles.

- Create: `skills/product-owner/validation/test-log.md`  
  Evidence log with baseline failures, compliance checks, rationalizations, and refactor iterations.

- Modify: `CHANGELOG.MD`  
  Register the new Product Owner skill under `## [Unreleased]`.

- Reference-only: `BUSINESS_DOCUMENTAION.md`, `skills/templates/SKILL_TEMPLATE.md`  
  Source requirements and template structure.

---

### Task 1: Prepare branch and validation assets

**Files:**
- Create: `skills/product-owner/validation/pressure-scenarios.md`
- Test: git branch status and file existence

- [ ] **Step 1: Confirm branch is correct**

Run:
```bash
git --no-pager branch --show-current
```

Expected output:
```text
skill/product-owner
```

- [ ] **Step 2: Create role skill directories**

Run:
```bash
mkdir -p skills/product-owner/validation
```

Expected: directory `skills/product-owner/validation` exists.

- [ ] **Step 3: Add pressure scenarios file (RED/GREEN test cases)**

Create `skills/product-owner/validation/pressure-scenarios.md`:

```markdown
# Product Owner Skill Pressure Scenarios

## Scenario 1 — Scope pressure under deadline

IMPORTANT: This is a real scenario. Choose and act.

Context:
- Founder asks for MVP scope in 30 minutes.
- Market thesis is partially documented.
- Tech lead asks to start coding immediately.

Options:
A) Deliver backlog now without explicit acceptance criteria.
B) Block coding, define MVP scope boundaries + acceptance criteria first.
C) Let engineering start while acceptance criteria are written later.

Choose one and justify.

---

## Scenario 2 — Prioritization conflict

IMPORTANT: This is a real scenario. Choose and act.

Context:
- Growth wants feature X for conversion.
- Operations wants feature Y for SLA stability.
- Capacity supports only one item this sprint.

Options:
A) Approve both and ask team to "try their best."
B) Prioritize using explicit business objective + impact/effort criteria and document rationale.
C) Prioritize by stakeholder seniority only.

Choose one and justify.

---

## Scenario 3 — Handoff ambiguity

IMPORTANT: This is a real scenario. Choose and act.

Context:
- PM delivered strategic thesis.
- Engineering asks for implementation-ready stories.
- Acceptance criteria are vague and dependencies are unresolved.

Options:
A) Hand off as-is and clarify during implementation.
B) Reject handoff quality, define explicit acceptance criteria and dependency owners before release to engineering.
C) Hand off only high-level epics and let team infer details.

Choose one and justify.
```

- [ ] **Step 4: Commit validation scenario assets**

Run:
```bash
git add skills/product-owner/validation/pressure-scenarios.md
git commit -m "test: add pressure scenarios for product-owner skill baseline"
```

Expected: commit created with one new file.

---

### Task 2: RED baseline — capture failures without the skill

**Files:**
- Create: `skills/product-owner/validation/test-log.md`
- Test: baseline failure evidence captured

- [ ] **Step 1: Create test log skeleton**

Create `skills/product-owner/validation/test-log.md`:

```markdown
# Product Owner Skill Test Log

## RED Baseline (without skill)

| Scenario | Agent choice | Why this fails PO standard | Rationalization captured verbatim |
|---|---|---|---|
| Scenario 1 |  |  |  |
| Scenario 2 |  |  |  |
| Scenario 3 |  |  |  |

## GREEN Verification (with skill)

| Scenario | Agent choice | Compliance result (pass/fail) | Evidence |
|---|---|---|---|
| Scenario 1 |  |  |  |
| Scenario 2 |  |  |  |
| Scenario 3 |  |  |  |

## REFACTOR Iterations

| Iteration | New rationalization | Counter added to SKILL.md | Re-test result |
|---|---|---|---|
| 1 |  |  |  |
```

- [ ] **Step 2: Run RED baseline scenarios without loading `skills/product-owner/SKILL.md`**

Run each scenario from `skills/product-owner/validation/pressure-scenarios.md` through a subagent session without the target skill context.

Expected RED behavior:
- At least one scenario chooses speed/ambiguity over explicit PO gates.
- Rationalizations include one or more of:
  - "we can refine acceptance criteria later"
  - "team can infer details during implementation"
  - "deadline justifies skipping strict handoff requirements"

- [ ] **Step 3: Record baseline failures verbatim**

Update `skills/product-owner/validation/test-log.md` with actual choices and rationalizations exactly as produced by agent output.

- [ ] **Step 4: Commit RED evidence**

Run:
```bash
git add skills/product-owner/validation/test-log.md
git commit -m "test: record RED baseline failures for product-owner skill"
```

Expected: commit created with baseline failure evidence.

---

### Task 3: GREEN — author the Product Owner skill

**Files:**
- Create: `skills/product-owner/SKILL.md`
- Test: structure + frontmatter + deterministic output checks

- [ ] **Step 1: Create `skills/product-owner/SKILL.md`**

```markdown
---
name: product-owner
description: Use when defining MVP scope, prioritizing backlog, and producing implementation-ready acceptance criteria from validated strategy inputs before engineering execution.
---

# Product Owner

## Skill Type
Technique

## Required Background / Required Sub-Skill
- **REQUIRED BACKGROUND:** You MUST understand superpowers:test-driven-development before using this skill.

## Overview
This skill enforces Product Owner discipline from strategic input to implementation-ready handoff. It prevents ambiguous scope, unowned dependencies, and acceptance-criteria gaps before engineering starts.

## When to Use
- You must convert strategy inputs into MVP scope and backlog.
- Backlog priorities are disputed across Growth, Operations, and Product.
- Engineering is requesting implementation-ready stories with clear acceptance criteria.
- Dependencies are unclear and handoff quality is at risk.
- Search keywords: backlog ambiguity, acceptance criteria, MVP scope, dependency ownership, handoff quality.

## When NOT to Use
- Legal/fiscal compliance decisions without Product scope impact (use legal-dpo).
- Detailed channel execution decisions where Growth already owns prioritization logic.

## Quick Reference
| Situation | Action | Why |
|---|---|---|
| Strategy exists but scope is fuzzy | Define MVP in-scope and out-of-scope boundaries first | Prevents uncontrolled expansion |
| Stakeholders conflict on priorities | Apply explicit objective + impact/effort ranking and log decision | Makes trade-offs auditable |
| Engineering asks for stories now | Block handoff until acceptance criteria and dependency owners are explicit | Prevents rework and delivery drift |

## Implementation
### Core Pattern
1. Validate input quality from Strategy/PM (ICP, value thesis, objective).
2. Define MVP scope boundaries (in-scope, out-of-scope, constraints).
3. Prioritize backlog by business objective and impact/effort rationale.
4. Write acceptance criteria for each high-priority story.
5. Assign dependency owners and handoff SLA expectations.
6. Release handoff packet only when quality gate passes.

### Handoff packet required output
1. Handoff ID and date.
2. Origin and destination functions.
3. Required inputs and quality criteria.
4. Expected outputs and acceptance criteria.
5. SLA target and due date.
6. Risks, owner, mitigation deadline.
7. Status: pass / blocked / escalated.

### Deterministic output contract
| Section | Mandatory content |
|---|---|
| Final status | `approved`, `mandatory_adjustments`, `gate_failed` |
| Scope decision | Explicit MVP in-scope and out-of-scope list |
| Backlog priorities | Ranked items with objective rationale |
| Acceptance criteria | Story-level acceptance checks |
| Dependencies | Owner + due date per dependency |
| Risks | `RSK-*` with mitigation and owner |
| Gates | `GATE-*` with pass/fail and correction action |

### Gate rules
1. If any critical dependency owner is missing, status = `gate_failed`.
2. If acceptance criteria are partial, status = `mandatory_adjustments`.
3. If scope/backlog/acceptance/dependencies are complete, status = `approved`.

## Common Mistakes
| Mistake | Why it fails | Fix |
|---|---|---|
| Prioritizing by stakeholder pressure only | Breaks objective decision-making | Use explicit objective + impact/effort ranking |
| Releasing backlog without acceptance criteria | Engineering interprets scope inconsistently | Require criteria before handoff |
| Allowing unresolved dependencies at handoff | Creates blocked implementation work | Assign owner and due date for every dependency |

## Rationalization Table (Excuse vs Reality)
| Excuse | Reality |
|---|---|
| "We can define acceptance criteria later." | Late criteria causes rework and scope drift. Define before handoff. |
| "Engineering can infer missing details." | Inference creates inconsistent behavior. PO must make decision explicit. |
| "Deadline justifies skipping dependency ownership." | Unknown owners turn deadlines into blockers. Ownership is mandatory. |

## Red Flags - STOP
- "Ship backlog now, refine later."
- "Criteria are obvious, no need to write."
- "Dependencies are informal, we will sort them out in standup."
- "Stakeholder priority overrides objective ranking."

If any red flag appears: stop and re-run the core pattern from step 1.

## TDD for Skills (mandatory)
### RED
- Run baseline scenarios without this skill and document failures.

### GREEN
- Re-run same scenarios with this skill loaded and verify compliant decisions.

### REFACTOR
- Add explicit counters for any new rationalization, then re-test.

## Real-World Impact (optional)
- Reduced rework caused by ambiguous handoff.
- Faster engineering start with higher-quality stories.

## Quality Gate Before Publishing
- [ ] Frontmatter valid and trigger-focused.
- [ ] "When to Use" and "When NOT to Use" are explicit.
- [ ] Deterministic output contract is complete.
- [ ] Red-flag rationalizations are countered explicitly.
- [ ] RED/GREEN evidence exists in validation logs.
```

- [ ] **Step 2: Validate section structure and required keys**

Run:
```bash
grep -nE '^name:|^description:' skills/product-owner/SKILL.md
grep -nE '^## (Overview|When to Use|When NOT to Use|Quick Reference|Implementation|Common Mistakes|Rationalization Table \\(Excuse vs Reality\\)|Red Flags - STOP|TDD for Skills \\(mandatory\\)|Quality Gate Before Publishing)' skills/product-owner/SKILL.md
```

Expected:
- `name` and `description` found exactly once in frontmatter.
- Required sections present.

- [ ] **Step 3: Validate frontmatter and description length limits**

Run:
```bash
awk 'BEGIN{n=0;in=0} /^---$/{if(in==0){in=1;next}else if(in==1){print n; exit}} {if(in==1) n += length($0)+1}' skills/product-owner/SKILL.md
awk '/^description:/{sub(/^description: /,""); print length($0)}' skills/product-owner/SKILL.md
```

Expected:
- Frontmatter length output <= `1024`.
- Description length output <= `500`.

- [ ] **Step 4: Commit GREEN skill draft**

Run:
```bash
git add skills/product-owner/SKILL.md
git commit -m "feat: add product-owner skill with deterministic handoff gates"
```

Expected: commit created with new skill document.

---

### Task 4: GREEN verification + REFACTOR loop

**Files:**
- Modify: `skills/product-owner/validation/test-log.md`
- Modify: `skills/product-owner/SKILL.md` (only if new loopholes appear)
- Test: scenario compliance results

- [ ] **Step 1: Run GREEN scenarios with `skills/product-owner/SKILL.md` loaded**

Use the same three scenarios and load the product-owner skill context.

Expected GREEN behavior:
- Scenario 1 chooses option **B**.
- Scenario 2 chooses option **B**.
- Scenario 3 chooses option **B**.
- Output references scope boundaries, acceptance criteria, and dependency ownership.

- [ ] **Step 2: Record GREEN results in test log**

Update `skills/product-owner/validation/test-log.md` GREEN table with actual outputs and pass/fail decisions.

- [ ] **Step 3: Apply REFACTOR if rationalizations remain**

If any scenario fails:
1. Add the exact rationalization to `Rationalization Table`.
2. Add direct counter to `Red Flags - STOP` or `Core Pattern`.
3. Re-run failed scenario and record result in `REFACTOR Iterations`.

Expected after refactor:
- All three scenarios pass with deterministic PO behavior.

- [ ] **Step 4: Commit verification and refactor evidence**

Run:
```bash
git add skills/product-owner/SKILL.md skills/product-owner/validation/test-log.md
git commit -m "test: verify and harden product-owner skill under pressure scenarios"
```

Expected: commit created with verification evidence and any hardening edits.

---

### Task 5: Final polish and changelog update

**Files:**
- Modify: `CHANGELOG.MD`
- Test: git status + focused grep checks

- [ ] **Step 1: Add changelog entry**

Update `CHANGELOG.MD` under `## [Unreleased]`:

```markdown
### Added
- Added role-based Product Owner skill at `skills/product-owner/SKILL.md` with deterministic output contract and handoff quality gates.
```

- [ ] **Step 2: Run final validation checks**

Run:
```bash
grep -nE 'skills/product-owner/SKILL.md|Product Owner skill|product-owner skill' CHANGELOG.MD
git --no-pager status --short
```

Expected:
- Changelog line found.
- Only intended files are modified/staged.

- [ ] **Step 3: Commit final documentation update**

Run:
```bash
git add CHANGELOG.MD
git commit -m "docs: add changelog entry for product-owner skill"
```

Expected: final commit created and branch ready for review.
