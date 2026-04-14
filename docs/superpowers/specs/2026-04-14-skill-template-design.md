# Skill Template Design (based on writing-skills + obra/superpowers)

## Context
We need a reusable Markdown template for new skills, using the `writing-skills` discipline as the baseline and patterns observed in `https://github.com/obra/superpowers`.

The user requested:
- A single template file in English.
- Path: `skills/templates/SKILL_TEMPLATE.md`.
- Mandatory TDD-for-skills flow (RED/GREEN/REFACTOR + checklist).

## Goal
Create one complete, copy/paste-ready skill template that is:
1. Discoverable (strong CSO metadata and trigger language).
2. Actionable (clear sections and placeholders).
3. Testable (subagent pressure scenarios and anti-rationalization loops).
4. Publish-safe (quality gates before release).

## Reference principles adopted
From `writing-skills` and `obra/superpowers`:
- Description must be trigger-focused ("Use when..."), not workflow summary.
- Structured SKILL.md layout for scanability.
- TDD discipline for skills:
  - RED: baseline failure without skill.
  - GREEN: minimal skill implementation to address concrete failures.
  - REFACTOR: close loopholes, re-test, preserve compliance.
- Anti-rationalization by design:
  - red flags section
  - excuse vs reality table
  - explicit negations for common loopholes.

## Output file
- `skills/templates/SKILL_TEMPLATE.md`

## Planned template structure
1. YAML frontmatter template (`name`, `description`).
2. Overview.
3. When to Use / When NOT to Use.
4. Quick Reference.
5. Implementation.
6. Common Mistakes.
7. Rationalization Table (Excuse vs Reality).
8. Red Flags — STOP.
9. TDD for Skills:
   - RED checklist
   - GREEN checklist
   - REFACTOR checklist
10. Quality Gate Before Publishing.
11. Optional references/supporting files guidance.

## Placeholder strategy
Each section contains:
- Minimal heading scaffold.
- Fill-in placeholders (`<...>`) for fast authoring.
- One short example line to anchor expected level of specificity.

## Quality Gate Before Publishing (mandatory)
Template will include objective checks:
- Discoverability: name/description comply with CSO style.
- Clarity: triggers and non-triggers explicit.
- Testability: at least one pressure scenario and baseline failure captured.
- Anti-rationalization: explicit counters for observed loopholes.
- Token-efficiency: no redundant prose in high-load sections.

## Risks and mitigations
- Risk: template becomes too verbose and hard to adopt.
  - Mitigation: concise default blocks + optional extension notes.
- Risk: skills written from template still ambiguous.
  - Mitigation: hard gate requiring trigger precision and pressure-test evidence.
- Risk: people skip RED phase.
  - Mitigation: publish gate requires baseline failure evidence.
