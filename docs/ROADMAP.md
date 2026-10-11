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
3. Test in fresh context, validate the portable and Codex manifests, and bump
   both synchronized plugin versions.
4. Keep shared skills client-neutral and provide fallbacks for optional
   dependencies.

## Knowledge and Obsidian

The `knowledge` plugin subsumes general knowledge management: canonical homes,
capture, inbox processing, boundary crossing, and audits.

Whether a separate `obsidian` technical plugin is needed is not yet known.
Reason from concrete Obsidian-only workflows, the ownership and update cost of
any third-party skills, and portable client support. If no repeated gap
justifies it, remove the reserved empty wrapper rather than duplicating
`knowledge`.

## `research`

### Architecture

The sentence-level research workflow has three stable skill names:

- `interlinear` owns line-tagged LaTeX sources, typed TeX sidecars, and PDF
  views. The distributable `interlinear.sty` contains only stable mechanics;
  `<jobname>.interlinear.tex` contains document data. The usual view uses
  compact badges throughout and expands comments inline only in the requested
  theorem block or subsection.
- `reason` supplies informal or semiformal explanations, local-context notes,
  examples, and gap analysis to `interlinear`.
- `formalize` owns Lean and formal prover work. It runs only when explicitly
  requested and records evidence without silently rewriting the source claim.

`reason` may identify a formalization target, but it does not invoke Lean or
claim formal verification. `formalize` may use Aristotle when that service is
available; the skill must still work with a local Lean toolchain alone.

### Active work

#### `interlinear`

Priority: medium. The stable package, typed sidecar contract, six semantic
comment types, and section-3 fixture exist without Python, CSV, or generated
data.

- Compile every documented mode in a TeX-enabled environment.
- Check focus/badge layout on a longer mixed theorem-and-proof block.

Done when the fixture and a longer proof compile under the supported TeX
engines and fresh routing selects the skill for typed annotation work.

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

### `knowledge`

- `find-knowledge`: run fresh-context routing and a positive retrieval case with
  a known record in a mapped secondary source. Compare it with the recorded
  unskilled negative control; do not claim measured improvement before an
  observable baseline failure clears.

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
