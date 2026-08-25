# Research and math-writing skill roadmap

This roadmap records the 2026-08-25 review of `plugins/research` and
`plugins/math-writing`. Product expansion remains in
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

## Research

### `extracting-precise-results`

Priority: medium. Keep the skill.

- Replace “close to verbatim” with faithful paraphrase by default. Quote only
  when wording matters.
- Require a direct source link plus theorem number and page or section when
  available.
- Add evals for exact hypotheses, multiple distinct results, inaccessible full
  text, and abstract-only relevance triage that must not trigger the skill.

Done when a bibliography note remains traceable to a numbered source statement
without silently dropping hypotheses or overquoting it.

### `interlinear-research`

Priority: high. Keep the skill and helpers.

- Separate unverified Stacks matches from confirmed `stacks_ref` values. Either
  add `stacks_candidate` or require explicit confirmation before writing.
- Update the schema, renderer, helper, and tests together.
- Add parser tests for Typst strings, comments, escaped delimiters, and malformed
  `sent` bodies.
- Compile every rendering mode in a test environment with Typst installed.
- Add skill evals for label maintenance and for ordinary Typst formatting that
  must not trigger the skill.

Done when lexical matches cannot appear as verified references, helper tests
pass, and every documented rendering mode compiles.

## Math writing

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

### `proofreading-pass`

Priority: high. Revise before relying on it.

- Change the symbol-replacement example into a flagged, unapplied issue; it
  contradicts the scope rule.
- Make section splitting adaptive. Use subagents only for long independent
  ranges, not unconditionally or one per section.
- Provide or generate a standalone `-changes.tex` skeleton and test both it and
  the latexdiff output.
- Add evals separating language fixes, notation suspicions, style rewrites, and
  mathematical review.

Done when every applied edit is unambiguous, every judgment call is only
flagged, and all three promised artifacts compile.

### `russian-translation`

Priority: critical. Remove unsafe workflow first.

- Delete instructions to commit and push automatically. Version-control actions
  require separate user authority.
- Replace `Read`, `Edit`, `Bash`, `CLAUDE.md`, fixed `tex/` paths, and fixed
  compile commands with host-neutral, project-discovered operations.
- Move dissertation layout, source-directory exclusions, long-file procedure,
  and terminology-replacement procedure into focused references.
- Treat grant, affiliation, address, and email text as examples that require
  confirmation, never active defaults.
- Keep the calibrated corpus and core Russian voice rules; remove repetition
  and rules not supported by a recorded failure.
- Add translation, revision, voice-only, metadata, long-file, and must-not-load
  evals.

Done when the core skill has one job, performs no unrequested repository or
network action, and can be used outside the original thesis layout.

### `speech-style-adaptation`

Priority: high. Preserve the calibration, replace the orchestration.

- Replace Claude tool names, `.claude/` paths, `CLAUDE.md`, fixed thesis paths,
  and fixed compile commands with host-neutral guidance.
- Move thesis architecture, protected source directories, long-file mechanics,
  and parallel-dispatch details into focused references.
- Make delegation conditional on file size and independence; do not prescribe
  obsolete host-specific agent types.
- Remove duplicated advice shared with `occam-no-slop`; keep voice calibration
  distinct from structural de-slopping.
- Add evals for voice adaptation, ordinary proofreading, multi-file work, and
  prose that already matches the author.

Done when the skill adapts authorial voice in any project without assuming a
specific host, repository layout, or agent API.

## Suggested order

1. `russian-translation`: remove commit/push instructions.
2. `interlinear-research`: separate candidate and verified references.
3. `proofreading-pass`: restore scope consistency.
4. `speech-style-adaptation`: make the shared skill host-neutral.
5. `extracting-precise-results`: improve attribution and quoting.
6. `latex-project-scaffold`: add coverage and refresh tests.

After human review, consider exact `guard=human-revised` entries for the two
authorial-voice skills. Do not stamp agent-written revisions.
