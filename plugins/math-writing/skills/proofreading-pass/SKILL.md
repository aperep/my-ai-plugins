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
reviewed: d444bd3
---

# Proofreading pass

## Output

For a source `foo.tex`, in the same directory:

| File | Contents |
|---|---|
| `foo-corrected.tex` | the source with every **unambiguous** fix applied |
| `foo-changes.tex` | every applied change, by line number, with a reason; plus a separate section of issues flagged and left alone |
| `foo-diff.tex` | `latexdiff foo.tex foo-corrected.tex > foo-diff.tex` |

These files, not a chat list, are the deliverable.

## Workflow

1. Split the paper by section, one subagent per line range; use about six ranges
   for 3000 lines so attention stays uniform.
2. Apply only unambiguous fixes to `foo-corrected.tex`. Flag the rest without
   editing them.
3. Write `foo-changes.tex`; all line numbers refer to the original source.
4. Generate `foo-diff.tex` with `latexdiff`.
5. Ensure `output/` is gitignored, then compile both auxiliary files there:
   `latexmk -pdf -outdir=output <file>`.

## Change-log format

Categorise every entry so the author can skim mechanical changes:

`[Typo]` `[English]` `[Punctuation]` `[LaTeX]` `[Notation]` `[Formatting]`
`[Duplicate]` `[Flagged — not changed]`

One `\item` per change: bold line number, category, then the quoted before →
after and the reason.

```latex
\item \textbf{L363} \catE\ Subject--verb agreement: ``a finitely generated $\fh$
  \dots were not locally finite'' $\to$ ``\dots is not locally finite''.
\item \textbf{L583} \catT\ ``eigenspace of $\delta|_{V_n}$'' $\to$ ``eigenspace
  of $\p|_{V_n}$'' --- $\delta$ is never introduced in this passage; the
  derivation under discussion throughout is $\p$.
```

Copy into `foo-changes.tex` the paper macros used in quotations
(`\def\fh{{\mathfrak h}}`, `\def\p{\partial}`, …). Keep quoted math inside real
`$...$`; escaped `\$` prevents math-only macros from expanding.

## What gets flagged instead of fixed

Flag any judgment call, including:

- a change that could alter mathematical content (a symbol that looks wrong, an
  index that may or may not be a typo);
- a claim that cannot be checked without the author (a name, a date, a citation
  that does not resolve);
- inconsistent notation that is used consistently *within* a section — the
  author may have meant it.

State the problem and proposed fix, but do not apply it.

## Scope discipline

Do not renumber, reorder, rewrite for style, or review mathematical correctness.
Flag a suspect proof and move on. Authorial voice belongs to
`speech-style-adaptation`.
