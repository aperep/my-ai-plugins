# Interlinear test status

On 2026-08-26, revision `ac7d6c0` was installed locally as
`research@aperep` version `0.4.1` under Codex 0.149.1.

- Ten helper tests passed, including balanced Typst/LaTeX parsing, tag-filtered
  context, candidate/reference separation, and Lean evidence validation.
- The shared `rigid-section3` CSV validated against both its LaTeX and Typst
  sources.
- pdfTeX from TeX Live 2026 compiled the section-3 presentation fixture into a
  valid two-page PDF. `mutool` parsed both pages and rendered the focus block,
  short footnote, native popup badge, and printable appendix.
- A fresh `gpt-5.6-sol` routing probe selected `research:interlinear` for
  focus-aware LaTeX annotation rendering.

Typst compilation remains untested because no Typst executable is installed in
the test environment.
