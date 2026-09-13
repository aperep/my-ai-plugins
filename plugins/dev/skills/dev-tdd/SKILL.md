---
name: dev-tdd
description: Implement scoped behavior changes using meaningful tests before code where practical. Use for features, behavior-preserving refactors, and direct fixes with a known cause; use dev-fix for bug investigation. Documentation, formatting, and asset-only edits do not need this coding workflow.
---

# Dev TDD

Use tests to establish the behavior being implemented, then make the smallest coherent change. Honor an explicit request for strict TDD; otherwise choose verification proportional to the behavior and risk.

## Establish the behavior

- Read the affected implementation, nearby tests, and project test commands before choosing a test boundary.
- Use the current request and relevant repository specs, plans, and ADRs as the contract. Durable defaults live under `docs/`; read only documents connected to this task. The user's latest correction takes precedence over an older artifact.
- State expected observable behavior briefly. Ask only when a missing decision materially changes the implementation and cannot be inferred from the project.
- Inspect repository root, branch, working tree, and index before edits. Preserve unrelated changes, partially staged files, and explicit exclusions. A dirty tree alone is not a blocker.

## Choose the test strategy

For new behavior or a known regression, prefer a focused test that fails on the unchanged implementation. Exercise the real boundary and assert outputs or state transitions; avoid assertions that mirror implementation details.

For behavior-preserving refactors, passing characterization tests on the original implementation are valid evidence. Add coverage for relevant gaps, then keep those tests passing during the refactor.

Low-impact reversible changes need no new test if it would only restate the edit. Use an existing check or direct inspection where sufficient. Respect a user's request to skip TDD without a second permission exchange; run appropriate remaining checks and state the resulting evidence limit. Never call post-implementation tests a completed red/green cycle.

## Implement and verify

1. Run the focused test. For new behavior, confirm failure comes from the missing behavior, not a broken fixture, import, or environment. If a required symbol does not yet exist, establish that the failure is exactly that missing contract; it does not yet prove runtime behavior.
2. Implement the smallest coherent behavior change. Keep assertions intact unless investigation shows the test contradicts the contract.
3. Run the same test and inspect the result. Refactor only what the task needs, and rerun affected checks after further edits.
4. Expand checks according to impact: adjacent paths for a local change, integration and project checks for shared interfaces, persistence, authentication, or other high-risk behavior. Do not repeat sufficient checks without a new change or unresolved concern.

A second reversal of the fix is optional when the original red result already proves the test detects the defect. If additional mutation testing is needed, isolate it in a temporary copy and preserve the regression test; never use a blanket stash or reset on the shared working tree.

## Completion and handoff

Report the changed behavior, commands and observed results, and material limitations. Map evidence to relevant SDD acceptance criteria when present. Use `dev-verify` if available for completion evidence and `dev-code-review` when review is requested or required; their names do not force a new workflow or extra user turn. Without those skills, perform equivalent scoped checks directly. Commit, PR, and branch operations require the corresponding user authorization.
