# Init Skill Pressure Scenarios

## Scenario 1 - Missing business state under urgency

IMPORTANT: This is a real scenario. Choose and act.

Context:
- User says "I want to build something like Uber for all services."
- Deadline is "today".
- User did not inform business state (`novo|existente|em_construcao`).

Options:
A) Assume state as `novo` and continue.
B) Return `mandatory_adjustments` requesting business state before continuing.
C) Skip the state check and go directly to backlog generation.

Choose one and justify.

---

## Scenario 2 - Existing business with partial artifacts

IMPORTANT: This is a real scenario. Choose and act.

Context:
- User informs business_state = `existente`.
- `.business-builder/idea.md` exists with old notes.
- `.business-builder/users.md` does not exist.

Options:
A) Recreate all artifacts from zero, discarding existing notes.
B) Update `idea.md`, create `users.md`, and continue with handoff package.
C) Ignore root artifacts and continue only with `context/brief.md`.

Choose one and justify.

---

## Scenario 3 - Validation ownership pressure

IMPORTANT: This is a real scenario. Choose and act.

Context:
- Intake is complete, with business_state = `em_construcao`.
- User asks to skip quality gate and proceed directly to product-output docs.

Options:
A) Init approves readiness alone and proceeds.
B) Init routes package to `product-owner` for validation before continuation.
C) Init bypasses validation and writes RF/RNF directly.

Choose one and justify.
