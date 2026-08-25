# Research and math-writing skill roadmap

This roadmap tracks unfinished work in `plugins/research` and
`plugins/math-writing` after the 2026-08-25 review. Product expansion remains in
[`academic-workshop-roadmap.md`](academic-workshop-roadmap.md). Work on one
skill at a time; move completed or rejected items to [`LOG.md`](LOG.md) with
the decision and reason.

For every skill change:

1. Record baseline, trigger, and must-not-trigger cases under the skill's
   `evals/` directory.
2. Make the smallest change that clears the baseline failure.
3. Test in fresh context, validate both plugin wrappers, and bump the Codex
   plugin version.
4. Keep shared skills host-neutral. Put Claude-only instructions in the meta
   compatibility reference and provide fallbacks for optional dependencies.

## Active work

### `interlinear-research`

Priority: critical. Candidate Stacks matches currently write directly into the
confirmed `stacks_ref` field.

- Add `stacks_candidate`; reserve `stacks_ref` for human-confirmed results.
- Update the schema, example CSV, renderer, lookup helper, validator, and tests
  together.
- Add parser tests for Typst strings, comments, escaped delimiters, and malformed
  `sent` bodies.
- Compile every rendering mode in a test environment with Typst installed.
- Add skill evals for label maintenance and for ordinary Typst formatting that
  must not trigger the skill.

Done when lexical matches cannot appear as verified references, helper tests
pass, and every documented rendering mode compiles.

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

### `latex-project-scaffold`

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

- `extracting-precise-results`: run behavioral extraction cases against real
  papers, including multiple results and inaccessible full text.
- `russian-translation`: run and record an independent fresh-context evaluation
  of the reviewed revision.
- `speech-style-adaptation`: repeat fresh-context routing and behavior checks
  after the later Occam pass and shortening.

## Suggested order

1. `interlinear-research`: stop candidates entering verified data.
2. `proofreading-pass`: restore scope consistency and test its artifacts.
3. `extracting-precise-results`: close the real-source behavioral gap.
4. `russian-translation` and `speech-style-adaptation`: close recorded
   fresh-context validation gaps.
5. `latex-project-scaffold`: add coverage and refresh tests.
