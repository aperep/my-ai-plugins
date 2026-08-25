# LaTeX conventions for the English voice

Preserve the target project's macros, notation, theorem setup, and citation
style. The bundled paper's macro vocabulary is not a portable default.

When consistent with the project:

- use `\emph{...}` for a defined term rather than bold;
- keep a nonbreaking space before internal references and citation locators,
  such as `Lemma~\ref{...}`, `Section~\ref{...}`, and
  `\cite[Theorem~5.1]{...}`;
- retain `\qedhere` when the proof ends within a displayed line;
- use `:=` for a nontrivial symbol definition when the surrounding document
  follows that convention;
- preserve shared theorem counters, labels, and any existing restatement form
  such as `[{Theorem~\ref{...}}]`;
- use `---` only for a parenthetical aside in TeX prose.

Do not rename symbols or replace macros merely because `jems4.tex` uses `\K`,
`\cO`, `\G_a`, `\AA`, `\Aut`, or related commands. Adopt such notation only
when the project already defines it or the user explicitly requests it.

After editing, use the project's documented build command. Discover the root
file and output policy rather than assuming a directory layout or engine. Keep
generated output outside source directories and do not overwrite source files
as part of validation.
