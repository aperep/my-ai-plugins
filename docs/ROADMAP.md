---
parent: AGENTS.md
---

# Repository roadmap

This is the only active roadmap. Move completed or rejected work to the
[change log](LOG.md) with the decision and reason.

## Shared plugin rules

For every skill change:

1. Record baseline, trigger, and must-not-trigger cases under the skill's
   `evals/` directory.
2. Make the smallest change that clears the baseline failure.
3. Test in fresh context, validate both plugin wrappers, and bump the Codex
   plugin version.
4. Keep shared skills host-neutral. Put Claude-only instructions in the meta
   compatibility reference and provide fallbacks for optional dependencies.

## `research`

### Architecture

The sentence-level research workflow has three stable skill names:

- `interlinear` owns labelled Typst and LaTeX sources, tag-scoped local
  context, sidecar metadata, and PDF views. The usual view uses compact badges
  throughout and expands annotations inline only in the requested theorem
  block or subsection.
- `reason` supplies informal or semiformal explanations, local-context notes,
  examples, and gap analysis to `interlinear`.
- `formalize` owns Lean and formal prover work. It runs only when explicitly
  requested and records evidence without silently rewriting the source claim.

`reason` may identify a formalization target, but it does not invoke Lean or
claim formal verification. `formalize` may use Aristotle when that service is
available; the skill must still work with a local Lean toolchain alone.

### Active work

#### `interlinear`

Priority: medium. The shared schema, parsers, safe candidate fields, tag-scoped
context, both adapters, and the section-3 LaTeX presentation fixture exist.

- Install Typst in a test environment and compile every documented Typst mode.
- Check focus/badge layout on a longer mixed theorem-and-proof block.

Done when both adapters consume the same fixture, helper tests pass, and the
documented Typst modes compile.

#### `reason`

Priority: medium. Routing and the section-3 context behavior pass. Test a full
proof with a real gap, a valid repair, and a concrete example track.

Done when a full-proof case reports the real gap without strengthening the
claim and completes its example track.

#### `formalize`

Priority: high. Routing and generated-versus-checked behavior pass. Test a
small local Lean declaration and an Aristotle round trip when those tools are
available.

Done when a local Lean fixture compiles, an Aristotle result is checked, and
ordinary proof discussion still routes elsewhere.

## `math-writing`

### `proofreading-pass`

Priority: high. Revise before relying on it.

- Replace the applied symbol-replacement example with a flagged, unapplied
  issue; the current example contradicts the scope rule.
- Make section splitting adaptive. Use subagents only for long independent
  ranges.
- Provide or generate a standalone `-changes.tex` skeleton and test both it and
  the latexdiff output.
- Add evals separating language fixes, notation suspicions, style rewrites, and
  mathematical review.

Done when every applied edit is unambiguous, every judgment call is only
flagged, and all three promised artifacts compile.

### `project-scaffold`

Priority: low. Keep the skill.

- Add trigger evals for new or refreshed mathematical article scaffolds and a
  must-not-trigger copyediting case.
- Test English and Russian minimal projects with `latexmk`, compiling into an
  ignored `output/` directory.
- Test that refresh mode compares existing preamble, notation, and contact
  files instead of overwriting them.
- Keep affiliation and contact reuse behind explicit confirmation.

Done when both minimal variants compile and an existing project is preserved.

## Validation debt

### `meta`

- `managing-repository-docs`: teach migration to keep top-level `docs/*.md`
  as direct children of `AGENTS.md`, route nested documentation through
  `docs/MAP.md` or a relevant top-level document, and group sibling component
  readmes under a common directory readme such as `core/mcp/README.md`.

### `biblio`

- `zotero-library`: run fresh-context routing, live add/update/dedup checks, and
  a local Codex install; structural validation only was available when the
  skill was introduced.

### `research`

- `extracting-precise-results`: run behavioral extraction cases against real
  papers, including multiple results and inaccessible full text.

### `math-writing`

- `russian-translation`: run and record an independent fresh-context evaluation
  of the reviewed revision.
- `speech-style-adaptation`: repeat fresh-context routing and behavior checks
  after the later Occam pass and shortening.
