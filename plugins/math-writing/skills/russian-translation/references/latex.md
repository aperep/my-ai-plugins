# Translating LaTeX

Read enough project documentation and preamble to identify local macros,
language packages, theorem environments, bibliography conventions, and the
actual build entry point.

## Preserve structure

Unless restructuring is requested, preserve:

- formulas and math delimiters;
- environment boundaries and optional arguments;
- `\label`, `\ref`, `\eqref`, `\cite`, and citation keys;
- macro names and arguments;
- paragraph boundaries and theorem order;
- existing `\emph{...}` anchors for defined terms.

Translate prose inside theorem environments and textual macro arguments. Do not
translate identifiers, command names, or bibliography keys. Check every edited
command for balanced braces.

## Russian TeX conventions

Follow the project first. In the calibration corpus:

- a Russian dash is written as spaced `---`; numerical ranges use `--`;
- non-breaking `~` joins a locator to its reference or citation;
- `\emph{...}` marks a defined term;
- Russian grammatical case belongs outside the reference number: `по
  теореме~\ref{...}`, `в лемме~\ref{...}`;
- citation locators follow the cited work or project convention. Do not convert
  all English locators blindly.

Keep custom math macros inside real math mode. Never use escaped `\$` to quote
math snippets in prose.

## Validation

Use the project's build instructions. If none exist, identify the likely root
document from `\documentclass`, `\input`, and `\include` relationships. For a
standalone project, prefer `latexmk -pdf -outdir=output <root>.tex`; first ensure
`output/` is ignored. Do not edit generated auxiliary files.

After compilation, distinguish errors introduced by the edit from pre-existing
or environment failures. Report skipped validation plainly.
