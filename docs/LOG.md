---
parent: docs/ROADMAP.md
---

# Change log

## 2026-10-03

- Replaced LaTeX `\sent{label}{...}` wrappers in `interlinear` with one
  sentence-or-clause per source line ending in a stable four-character
  `\itag`; kept its behavior and validation in `interlinear.sty`.
- Split stable package mechanics from document data: `interlinear.sty` now
  auto-loads typed comments from `<jobname>.interlinear.tex`. Removed the CSV,
  generated-TeX, Python, popup, and Typst paths.

## 2026-09-19

- Removed the unused `human-only` guard and its write-blocking hooks; retained
  `human-revised` review tracking through repository maintenance.
- Renamed `managing-repository-docs` to `doc-map`. The map now explicitly
  includes only agent-facing operational documents; Markdown templates,
  fixtures, eval artifacts, and domain references remain repository content.
  Removed automatic migration because paths and syntax cannot determine that
  distinction safely.
- Removed Claude Code packaging and configuration, added Agent Plugins 1.0
  manifests to every plugin, and synchronized portable and Codex versions.
- Documented every plugin in the repository README. Made `knowledge` the
  canonical knowledge-management plugin and left the need for an
  Obsidian-specific technical plugin as an explicit roadmap question.
- Added a repository inbox and maintenance policy, exposed their roles through
  the meta plugin, and made the roadmap repository-wide.
- Moved content-guard review-drift reminders from session startup into
  repository maintenance.

## 2026-09-02

- Added the host-neutral `zotero-library` skill for verified, deduplicated, non-destructive Zotero updates and repository synchronization.
- Centralized the user's citation-key convention in one plugin-level reference and made local-only bibliography records an explicit supported state.
- Recorded routing and behavioral cases; live Zotero and fresh-context validation remain on the roadmap.

## 2026-08-26

- Added a bounded meta-plugin `SessionStart` inventory for `docs/**/*.md` paths
  and allowlisted scalar frontmatter. Repository values are labelled untrusted;
  unknown fields, symlinks, and oversized output are excluded.
- Replaced the stale academic-workshop roadmap with one canonical three-skill
  plan: `interlinear`, `reason`, and `formalize`.
- Extended `interlinear` to one CSV-backed Typst/LaTeX workflow with balanced
  source parsing, tag-filtered context, separate candidate references, Lean
  evidence fields, focus-aware views, and a section-3 PDF fixture.
- Added `reason` for context-bound informal analysis and `formalize` for
  explicit Lean/Aristotle work. Fresh routing and boundary probes passed.
- Replaced the dead Claude `aperep-dev` convention with the manifest-owned
  `aperep` marketplace name after a local install exposed the stale path.
- Shortened the three research skill entrypoints by about one fifth without
  removing their tested boundaries; also removed the roadmap's obsolete build
  order.

## 2026-08-25

- Rebuilt `russian-translation` as a host-neutral voice skill with focused
  references, guarded metadata reuse, and routing fixtures. Kept fresh-context
  behavioral validation as explicit roadmap debt.
- Replaced project-specific orchestration in `speech-style-adaptation` with
  portable voice calibration and routing evals. A later shortening invalidated
  the earlier behavioral run, so reevaluation remains on the roadmap.
- Reduced `extracting-precise-results` to traceable numbered statements,
  faithful paraphrase, direct links, and source locations. Routing checks pass;
  real-paper behavioral cases remain.
- Reduced `occam-no-slop` to structural economy and continuity in mathematical
  prose. Its trigger is now explicit, and stronger mathematical claims are
  flagged instead of edited in.
- Replaced the separate `simple-english` dependency with one local general-prose
  pass. Removed its modes, manual taxonomy, procedure rules, and upstream
  attribution layer.

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
