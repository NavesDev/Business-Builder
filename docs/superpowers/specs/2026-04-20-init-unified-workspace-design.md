# Init Unified Workspace Design

## Problem
The current init design and implementation plan still target `business-builder/` and do not fully capture the intake branch where the business already exists or is already in construction. We need one canonical workspace folder per project and a deterministic intake+validation flow before downstream handoff.

## Approved Approach
1. Replace the canonical workspace root with `business-builder/` across spec and implementation plan.
2. Update `init` behavior to always ensure `business-builder/` exists before artifact handling.
3. Make business state mandatory in intake with fixed values: `novo`, `existente`, `em_construcao`.
4. Route all states through `product-owner` validation before continuing the flow.
5. Ensure `idea.md` and `users.md` are baseline artifacts for the flow branch where business is `existente` or `em_construcao`, with deterministic create-or-update behavior.

## Alternatives Considered
1. **Full update of current spec+plan (selected):** keeps one source of truth and avoids drift.
2. Plan-only change: faster short-term, but leaves architectural contradiction.
3. Addendum document only: preserves history, but introduces parallel specs for same flow.

## Workspace Structure
```text
business-builder/
  context/
  product-management/
  product-output/
  idea.md
  users.md
```

## Init Flow
1. User triggers `init`.
2. `init` collects idea inputs and mandatory business state (`novo|existente|em_construcao`).
3. `init` guarantees `business-builder/` exists.
4. If state is `existente` or `em_construcao`, `init` creates `idea.md` and `users.md` when missing, or updates them when present.
5. `init` sends the structured package to `product-owner` for validation.
6. With `product-owner` OK, flow proceeds with existing downstream orchestration.

## Responsibility Boundaries
- `init`: intake, state normalization, workspace bootstrap, baseline artifact creation/update.
- `product-owner`: quality gate validation for scope/readiness.
- Downstream skills: deeper management and final output package.

## Error Handling
- Missing mandatory state or minimal idea fields returns `mandatory_adjustments` with explicit missing fields list.
- `init` does not finalize business viability decisions in this step; it relies on `product-owner` validation in the approved flow.

## Testing Impact
- Update validation scenarios to include:
  1. Missing state in intake.
  2. Existing business with prefilled artifacts (update path).
  3. Business in construction with missing artifacts (create path).

## Success Criteria
1. Canonical path is `business-builder/` in spec and plan.
2. `init` deterministic state handling includes `novo`, `existente`, `em_construcao`.
3. `idea.md` and `users.md` follow create-or-update behavior for `existente` and `em_construcao`.
4. `product-owner` validation is explicit in the orchestration flow before continuation.
