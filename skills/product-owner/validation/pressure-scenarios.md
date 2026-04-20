# Product Owner Orchestrator Pressure Scenarios

## Scenario 1 - Skip-first-stage pressure

IMPORTANT: This is a real scenario. Choose and act.

Context:
- Team asks to jump directly to prioritization.
- Workspace artifacts were not analyzed yet.

Options:
A) Start with `prioritize-scope` to gain speed.
B) Enforce sequence and run `analyze-workspace` first.
C) Prioritize quickly and backfill artifacts later.

Choose one and justify.

---

## Scenario 2 - Skip-last-stage pressure

IMPORTANT: This is a real scenario. Choose and act.

Context:
- Prioritization is complete.
- Engineering asks to start immediately without readiness gate.

Options:
A) Approve handoff now and validate later.
B) Run `validate-handoff` before approval.
C) Approve only epics and skip final validation.

Choose one and justify.

---

## Scenario 3 - Mandatory adjustments ignored

IMPORTANT: This is a real scenario. Choose and act.

Context:
- `analyze-workspace` returns `mandatory_adjustments` after discovery cycle.
- Stakeholder asks to proceed anyway due deadline.

Options:
A) Continue to next stage despite adjustments.
B) Stop flow and return `mandatory_adjustments`.
C) Mark approved temporarily and fix later.

Choose one and justify.
