---
name: project-scaffold
description: >
  Start or refresh a mathematical typesetting project using reusable LaTeX
  article assets and a reserved Typst layout. Use for article scaffolding,
  Russian or English theorem setups, or project preambles. Not for copyediting.
metadata:
  reviewed: ae6e368
---

# Mathematical project scaffold

Copy only the files the project needs from `assets/latex/`; do not overwrite an
existing preamble, notation file, or author block without comparing it first.

Wrap prose by sentence: put one sentence on each source line. If a sentence is
too long, break it at a natural clause boundary; do not hard-wrap by column.

The bundled files are personal starting points, not universal style rules:

- `main.tex` shows the include structure and AMS article layout.
- `common/packages.tex` is a conservative package baseline.
- `common/notation.tex` contains algebraic-geometry notation.
- `common/environments.tex` and `environments_ru.tex` provide English and
  Russian theorem families.
- `common/contacts.tex` contains A. Perepechko's HSE affiliation and must be
  confirmed before reuse.

`assets/typst/` reserves the matching project structure but is not yet a usable
template.

After copying, adjust relative `\input` paths, language/font setup, title,
abstract, acknowledgements, and bibliography source. Compile the smallest
document before adding optional packages.

For the original TinyTeX package inventory and safe setup boundaries, read
[references/tex-environment.md](references/tex-environment.md). Never run a
remote installer or system package manager without the user's approval.
