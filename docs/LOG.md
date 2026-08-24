# Change log

## 2026-08-24

- Added Codex catalogs and manifests around the shared skill tree.
- Made Codex the primary host while retaining Claude Code compatibility.
- Kept only `meta` available pending shared-skill validation.

## 2026-08-03

- Split `meta` into `skill-quality`, `editing-this-marketplace`, and
  `trusting-foreign-skills`.
- Scoped `meta` and `skillforge` to repositories that edit skills.
- Replaced wildcard content guards with explicit paths and made missing guards a
  reminder rather than a block.

## 2026-08-02

- Added hook-backed content guards and the `skill-quality` gate.
- Pinned `skillforge` and `self-learning` as third-party dependencies.

Older implementation detail remains available in Git history.
