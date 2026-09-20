# Baseline — dev-flow

Date: 2026-09-21
Baseline: dev plugin 0.1.2 instruction audit; no model-behavior claim

- A direct implementation request could route straight to `dev-tdd` or
  `dev-fix`, bypassing `dev-start`, because that skill triggered only for
  ambiguous requests.
- `dev-start` did not establish a session Git mode or handle a dirty tree before
  new edits.
- `dev-start` prohibited all setup mutations, so it could not establish a
  selected branch or worktree before implementation.
- `dev-finish` could not reuse a start-of-session delivery contract and therefore
  had to reconstruct permissions and destination at the end.
- The split skills duplicated lifecycle boundaries without one instruction that
  distinguished new work from continuation or delivery.
