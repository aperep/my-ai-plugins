# Artifact checks — 2026-10-16

Typst 0.15.1; direct compilation and PDF inspection, not a fresh-context
model routing evaluation.

Run from the repository root:

```sh
mkdir -p output/template-check
typst compile plugins/math-writing/skills/project-scaffold/assets/typst/main.typ output/template-check/article.pdf
typst compile --root . --input lang=en plugins/math-writing/skills/project-scaffold/evals/typst-smoke.typ output/template-check/scaffold-en.pdf
typst compile --root . --input lang=ru plugins/math-writing/skills/project-scaffold/evals/typst-smoke.typ output/template-check/scaffold-ru.pdf
```

All three builds passed without diagnostics.
Checked all 89 LaTeX macro names against the Typst exports, mapping `0` to
`compose`, and exercised every binding in rendered formulas.
The two language builds exercise all 19 theorem environments, shared
numbering across subsections, reset at the next section, and native references
and citations.
The QED checks include sequential proofs, `qedhere`, and a claim proof nested
in an ordinary proof; only the claim proofs end with filled squares.

The scaffold was copied to isolated English and Russian projects before
testing, so its imports do not depend on the marketplace checkout.
Inspected article and notation/theorem PDF pages as images.
Agent Skills validation, manifest schema/version checks, and local Codex
installation also passed.
