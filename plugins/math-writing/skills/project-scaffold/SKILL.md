---
name: project-scaffold
description: >
  Start or refresh a mathematical typesetting project using reusable LaTeX
  and Typst article assets. Use for article scaffolding,
  Russian or English theorem setups, or project preambles. Not for copyediting.
metadata:
  human-revised: ae6e368
---

# Mathematical project scaffold

Choose `assets/latex/` or `assets/typst/` for the project's typesetter.
Copy only the files the project needs; do not overwrite an
existing preamble, notation file, or author block without comparing it first.

Wrap prose by sentence: put one sentence on each source line. If a sentence is
too long, break it at a natural clause boundary; do not hard-wrap by column.

The bundled files are starting points, not universal style rules:

- `main.tex` shows the include structure and AMS article layout.
- `common/packages.tex` is a conservative package baseline.
- `common/notation.tex` contains algebraic-geometry notation.
- `common/environments.tex` and `environments_ru.tex` provide English and
  Russian theorem families.
- `common/contacts.tex` contains author, affiliation, and email placeholders;
  fill them only from the user or target project's confirmed details.

`assets/typst/` provides a working article with the same notation and English
or Russian theorem families.
Read its [README](assets/typst/README.md) for imports, language selection,
contacts, native citations, and the few macro names whose syntax differs.
Use native Typst math operators, symbols, and markup; preserve the meaning of
LaTeX notation without imitating TeX expansion or layout commands.
Check the generated PDF, including theorem numbering and references, rather
than relying only on the LaTeX-pattern checker.

After copying, adjust relative `\input` paths, language/font setup, title,
abstract, acknowledgements, and bibliography source. Compile the smallest
document before adding optional packages.
For Typst, run `typst compile main.typ output/main.pdf` from the copied
directory after creating and ignoring `output/`.

For the original TinyTeX package inventory and safe setup boundaries, read
[references/tex-environment.md](references/tex-environment.md). Never run a
remote installer or system package manager without the user's approval.
