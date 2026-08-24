---
name: proofreading-pass
author: A. Perepechko
description: >
  Copyedit a LaTeX paper — typos, grammar, punctuation, LaTeX hygiene — and
  deliver the result as three files: a corrected source, a categorised change
  log, and a latexdiff. Use when asked to "proofread", "copyedit", "вычитать",
  "прочитать на опечатки", "check the language of this paper", or to review a
  coauthor's or referee's draft before submission. Not for mathematical
  correctness: statements, proofs and numbering are out of scope except where a
  language fix would silently change the mathematics.
---

# Proofreading pass

A copyediting pass over a `.tex` paper. Language only. The deliverable is not a
list of remarks in chat — it is three files the author can compile, read and
apply piecewise.

## Output

For a source `foo.tex`, in the same directory:

| File | Contents |
|---|---|
| `foo-corrected.tex` | the source with every **unambiguous** fix applied |
| `foo-changes.tex` | every applied change, by line number, with a reason; plus a separate section of issues flagged and left alone |
| `foo-diff.tex` | `latexdiff foo.tex foo-corrected.tex > foo-diff.tex` |

Compile to `output/` (`latexmk -pdf -outdir=output foo-changes.tex`), and make
sure `output/` is gitignored first.

## Workflow

1. **Split by section, one subagent per section.** A 3000-line paper gets ~6
   passes. Each subagent proofreads only its own line range and reports entries
   in the format below. Splitting is what keeps attention uniform — a single
   pass over a whole paper degrades badly after the first few hundred lines.
2. **Apply only unambiguous fixes** to `-corrected.tex`. Everything else goes in
   the flagged list, unedited.
3. **Write `-changes.tex`** as the log. All line numbers refer to the
   **original** file, not the corrected one — the author reads them against the
   source they know.
4. **Run latexdiff** for the visual check: `latexdiff foo.tex foo-corrected.tex > foo-diff.tex`.
5. **Compile both** `-changes.tex` and `-diff.tex` before reporting. A change log
   that does not compile is not a deliverable.

## Change-log format

Categorise every entry. The category is what lets the author skim 90 entries and
approve the mechanical ones in one pass:

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

`-changes.tex` quotes math from the paper, so its preamble must carry the
paper's own macros (`\def\fh{{\mathfrak h}}`, `\def\p{\partial}`, …). Copy the
ones you actually quote. Quoted math stays inside real `$...$` — never escaped
`\$`, which stops macro expansion and breaks the compile.

## What gets flagged instead of fixed

Anything where the fix is a judgment call:

- a change that could alter mathematical content (a symbol that looks wrong, an
  index that may or may not be a typo);
- a claim that cannot be checked without the author (a name, a date, a citation
  that does not resolve);
- inconsistent notation that is used consistently *within* a section — the
  author may have meant it.

Say what is wrong and what you would do; do not do it.

## Scope discipline

Mathematical correctness is out of scope. If a proof looks wrong, note it in the
flagged section and move on — do not start reviewing the mathematics under cover
of a copyediting pass, and do not renumber, reorder, or rewrite for style.
Authorial voice is a different skill (`speech-style-adaptation`).
