# Translating LaTeX

Project macros and conventions win.

## Preserve structure

Unless restructuring is requested, preserve formulas, math delimiters,
environment boundaries, optional arguments, labels, references, citation keys,
macro names, paragraph boundaries, theorem order, and defined-term markup.

Translate prose inside theorem environments and textual macro arguments. Do not
translate identifiers, command names, or bibliography keys. Check every edited
command for balanced braces.

## Russian TeX conventions

In the calibration corpus:

- a Russian dash is written as spaced `---`; numerical ranges use `--`;
- non-breaking `~` joins a locator to its reference or citation;
- `\emph{...}` marks a defined term;
- Russian grammatical case belongs outside the reference number: `по
  теореме~\ref{...}`, `в лемме~\ref{...}`;
- citation locators follow the cited work or project convention. Do not convert
  all English locators blindly.

Keep custom math macros inside real math mode. Never use escaped `\$` to quote
math snippets in prose.
