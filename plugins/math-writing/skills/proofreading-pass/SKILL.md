---
name: proofreading-pass
description: >
  Copyedit a LaTeX paper — typos, grammar, punctuation, LaTeX hygiene — and
  deliver the result as three files: a corrected source, a categorised change
  log, and a latexdiff. Use when asked to "proofread", "copyedit", "вычитать",
  "прочитать на опечатки", "check the language of this paper", or to review a
  coauthor's or referee's draft before submission. Not for mathematical
  correctness: statements, proofs and numbering are out of scope except where a
  language fix would silently change the mathematics.
metadata:
  human-revised: d444bd3
---

# Proofreading pass

## Output

For a source `foo.tex`, in the same directory:

| File | Contents |
|---|---|
| `foo-corrected.tex` | the source with only **unambiguous** fixes applied |
| `foo-changes.tex` | every applied and suggested change, with status, category, original line number, and reason |
| `foo-diff.tex` | `latexdiff foo.tex foo-corrected.tex > foo-diff.tex` |

These files, not a chat list, are the deliverable.

## Workflow

1. For a long paper, split it into independent section or line ranges. Use
   subagents only when parallel review materially helps.
2. Mark each proposed change `Applied` or `Suggested`. Apply only unambiguous
   fixes to `foo-corrected.tex`; leave every suggested change out of it.
3. Write `foo-changes.tex`; all line numbers refer to the original source.
4. Generate `foo-diff.tex` with `latexdiff`.
5. Ensure `output/` is gitignored, then compile both auxiliary files there:
   `latexmk -pdf -outdir=output <file>`.

## Status and category

Every entry has one status and one or more categories. Status and category are
independent: any category can be either applied or suggested.

- `[Applied]`: the original is objectively wrong and the minimal fix is clear.
- `[Suggested]`: the change is optional, uncertain, voice-dependent, or could
  affect mathematical meaning. It does not appear in `foo-corrected.tex`.

Use these categories:

`[Typo]` `[English]` `[Punctuation]` `[LaTeX]` `[Notation]` `[Formatting]`
`[Duplicate]` `[Voice]`

Start `foo-changes.tex`, before the first list, with a short paragraph giving
both the count and original-source line numbers of all major issues across both
statuses, for example: `Major issues: 3 (L61, L144, L189).` Major issues are
probable errors that could affect mathematical meaning, attribution, a
reference, compilation, or the reader's interpretation. If there are none,
write `No major issues found.`

Use separate applied and suggested lists. One `\item` per change: bold line
number, status, category, then the quoted before $\to$ after and the reason.
Define status macros alongside the category macros in the standalone file:

```latex
\newcommand{\statusA}{\textbf{[Applied]}}
\newcommand{\statusS}{\textbf{[Suggested]}}
\item \textbf{L363} \statusA\ \catE\ Subject--verb agreement:
  ``a finitely generated $\fh$
  \dots were not locally finite'' $\to$ ``\dots is not locally finite''.
\item \textbf{L212} \statusS\ \catV\ ``So'' $\to$ ``Thus'' may read more
  formally, but both are correct and the choice belongs to the author's voice.
\item \textbf{L583} \statusS\ \catN\ ``eigenspace of $\delta|_{V_n}$'' $\to$ ``eigenspace
  of $\p|_{V_n}$'' --- $\delta$ is never introduced in this passage; the
  derivation under discussion throughout is $\p$. Confirm the intended symbol.
```

Copy into `foo-changes.tex` the paper macros used in quotations
(`\def\fh{{\mathfrak h}}`, `\def\p{\partial}`, …). Keep quoted math inside real
`$...$`; escaped `\$` prevents math-only macros from expanding.

## What gets suggested instead of applied

Suggest any judgment call, including:

- any voice or style change: choosing a different valid connective, replacing
  a valid phrase with a more formal one, tightening a grammatical sentence, or
  recasting prose for flow;
- any English change with more than one reasonable repair; apply only the
  smallest correction required for grammar;
- a change that could alter mathematical content (a symbol that looks wrong, an
  index that may or may not be a typo);
- a claim that cannot be checked without the author (a name, a date, a citation
  that does not resolve);
- inconsistent notation that is used consistently *within* a section — the
  author may have meant it.

State the problem and proposed fix, but do not apply it. If the user explicitly
requests voice adaptation too, keep that as a separate pass rather than folding
it into the corrected proofreading source.

## Scope discipline

Do not renumber, reorder, apply voice or style rewrites, or review mathematical
correctness. Suggest a suspect proof and move on. Authorial voice belongs to
`speech-style-adaptation`.
