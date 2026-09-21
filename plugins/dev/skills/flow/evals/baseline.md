# Baseline — flow

Date: 2026-09-21
Baseline: dev plugin 0.1.2 instruction audit; no model-behavior claim

- A direct implementation request could route straight to `tdd` or
  `debug`, bypassing `dev-start`, because that skill triggered only for
  ambiguous requests.
- `dev-start` did not establish a session Git mode or handle a dirty tree before
  new edits.
- `dev-start` prohibited all setup mutations, so it could not establish a
  selected branch or worktree before implementation.
- `dev-finish` could not reuse a start-of-session delivery contract and therefore
  had to reconstruct permissions and destination at the end.
- The split skills duplicated lifecycle boundaries without one instruction that
  distinguished new work from continuation or delivery.

## Structural necessity

The imported Ponytail ladder asked whether a requested change needed to exist,
but did not explicitly apply the same test to relevant existing structure. A
request to add a second implementation through a single-implementation
registry and factory must evaluate both the existing machinery and the new
proposal instead of treating either as necessary by default.
