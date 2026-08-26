---
name: latex-project-scaffold
description: >
  Start or refresh a mathematical LaTeX article project using reusable theorem,
  notation, package, contact, and bibliography-input files. Use when asked to
  scaffold a LaTeX paper, create a Russian or English theorem setup, or prepare
  the TeX environment for this template. Not for copyediting an existing paper.
reviewed: d9f00dd
---

# LaTeX project scaffold

Copy only the files the project needs from `assets/latex/`; do not overwrite an
existing preamble, notation file, or author block without comparing it first.

The bundled files are personal starting points, not universal style rules:

- `main.tex` shows the include structure and AMS article layout.
- `common/packages.tex` is a conservative package baseline.
- `common/notation.tex` contains algebraic-geometry notation.
- `common/environments.tex` and `environments_ru.tex` provide English and
  Russian theorem families.
- `common/contacts.tex` contains A. Perepechko's HSE affiliation and must be
  confirmed before reuse.

After copying, adjust relative `\input` paths, language/font setup, title,
abstract, acknowledgements, and bibliography source. Compile the smallest
document before adding optional packages.

For the original TinyTeX package inventory and safe setup boundaries, read
[references/tex-environment.md](references/tex-environment.md). Never run a
remote installer or system package manager without the user's approval.
