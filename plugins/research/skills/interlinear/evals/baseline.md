# Interlinear research baseline cases

## Stable package, separate document data

**Task.** Add sentence-level LaTeX annotations without coupling a distributable
package to one document.

**Baseline failure.** Document data is stored in CSV, transformed by Python,
and input as generated TeX; the workflow also carries an unrelated Typst
renderer.

**Expected behavior.** Keep source text in `<jobname>.tex`, typed comments in
the automatically loaded `<jobname>.interlinear.tex`, and reusable mechanics in
`interlinear.sty`. Require no Python, CSV, generated data file, or Typst adapter.

## Meaning is separate from presentation

**Task.** Record a Russian translation, an unchecked reference, and planned
formal work for one tagged clause.

**Expected behavior.** Use explicit `translation[ru]`,
`reference[candidate]`, and `formal[planned]` comments. Select badge, focus,
inline, or footnote rendering independently; never infer trust from display.

## Package ownership is narrow

**Task.** Explain or formalize a tagged statement.

**Expected behavior.** `reason` writes informal typed comments and `formalize`
writes formal status only after explicit invocation. Neither changes package
code or the tagged source claim.
