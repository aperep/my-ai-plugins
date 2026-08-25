# Change log

## 2026-08-25

- Reduced `occam-no-slop` to structural economy and continuity in mathematical
  prose. Its trigger is now explicit, and stronger mathematical claims are
  flagged instead of edited in.
- Replaced the separate `simple-english` dependency with a local skill. Plain
  technical English is the default; rigid ASD-STE100 constraints load only for
  explicit controlled-English requests.

## 2026-08-24

- Rewrote `meta` around Codex, added guarded suggestion harvesting, and moved
  Claude-only behavior into one reference.
- Updated operational references to the current `aperep/my-ai-plugins`
  repository name.
- Renamed the `latex` plugin to `math-writing` with a migration mapping.
- Created the `research` plugin for precise mathematical literature reading.
- Moved `extracting-precise-results` from `biblio` to `research`.
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
