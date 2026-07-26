---
name: speech-style-adaptation
author: A. Perepechko
description: Adapt drafted mathematical prose to A. Perepechko's authorial voice, calibrated from `jems4.tex` (JEMS 2026). Use whenever writing or revising English text for the thesis (`main_en.tex`, `*_en.tex`, `intro_en.tex`, English `*_intro_en.tex`, abstracts, cover letters), or when polishing prose lifted from co-authored sources to match the single-author voice. Trigger phrases: "in my style", "match my voice", "rewrite to my style", "adapt to author's style", "Perepechko style".
---

# Speech-Style Adaptation — A. Perepechko (calibrated on jems4.tex)

The reference corpus for this skill is `jems4.tex` — the JEMS 2026 single-author paper *Structure of Connected Nested Automorphism Groups*. It is the cleanest sample of the author's solo voice; co-authored papers should not be used for calibration.

Use this skill when generating or rewriting any English mathematical prose for the thesis. Apply as a soft overlay: discipline conventions and the constraints in `tex/CLAUDE.md` always take priority. Do not modify the source files in `tex/P26/`, `tex/APS14/`, etc.

## Voice in one paragraph

First-person plural, declarative, restrained. Sentences are short to medium and almost always start the new idea with a connective ("Then", "Indeed", "Thus", "In particular", "Moreover", "Conversely", "By Lemma X.Y") rather than with the subject. The author signposts what is being done ("In this article, we describe…", "Here we show…", "We extend…") and announces results before stating them. Definitions are introduced with `\emph{...}` on the term being defined, followed by a brief, self-contained clause. Proofs read as a chain of small justified steps, each beginning with the rule being applied; they end with a one-clause closer such as "The assertion follows" or "We have (i)."

## Calibrated patterns

### 1. Pronoun and stance

- Default to **"we"** for both rhetorical ("we describe", "we show", "we obtain") and inclusive ("we have", "we may assume") uses. Do not use "I"; do not use the passive to avoid an agent when "we" works.
- Use **"the author"** only in acknowledgments and funding notes ("The author is grateful to…", "The author thanks…").
- Use **"Let us …"** sparingly, for setup beats: "Let us choose a filtration", "Let us show that…".
- Use the imperative **"Consider …", "Let …", "Recall that…", "Assume that…", "Write …"** to set up objects. These are the dominant sentence-openers in proofs and definitions.

### 2. Sentence rhythm

- Short declarative sentences are the default. Two clauses joined by a connective are common; three-clause sentences are rare.
- Lead with the connective or the assumption, not the conclusion: "By Lemma~\ref{lm:L-structure}, $L$ is a Lie subalgebra of $\jonq_u(k,A_h)$ for some $k>0$ and $h\in\ker L$."
- Avoid em dashes. The author uses commas, semicolons, and the spaced double-hyphen `---` (only for asides like "tuples of pairwise commuting locally nilpotent derivations --- which play an equally central role").
- Avoid throat-clearing ("It is worth noting that…", "It should be mentioned that…"). Instead use "Note that…", "Recall that…", or simply state the fact.
- Avoid hedges ("perhaps", "arguably", "it seems"). The voice is assertive within the scope of what has been proved.

### 3. Signature transitions

Use these connectives at the start of sentences. They are the load-bearing rhythm of the paper.

| Function | Preferred forms |
|---|---|
| Consequence | **Then**, **Thus**, **Hence**, **So**, **It follows that**, **In particular** |
| Justification | **By Lemma~\ref{...}**, **By~\cite[...]{...}**, **Indeed**, **By construction**, **By assumption** |
| Addition | **Moreover**, **We also …**, **Furthermore** (sparingly) |
| Contrast | **Conversely**, **On the other hand**, **However** (rarely) |
| Recap | **Recall that**, **As above** |
| Reformulation | **Equivalently**, **Namely**, **That is** |
| Forward ref. | **The following theorem/lemma/proposition/remark…**, **We will need the following lemma** |
| Closer | **The assertion follows.**, **We have (i).**, **as required**, **a contradiction** |

### 4. Result and proof scaffolding

- **Sectioning**: `\section{...}`, then a one- or two-sentence preview ("In this section we describe…", "Here we…"). Subsections also begin with a single orienting sentence.
- **Theorems** are introduced and re-stated under intro labels with `[{Theorem~\ref{th:...}}]` so the reader sees both the local label and the publishable statement.
- **Definitions** put the defined term in `\emph{...}` inline; multiple sub-definitions go into an `itemize`. Do not use bold for the defined term.
- **"For short"** is the standard abbreviation flag: *"de Jonqui\`eres-like (or, for short, dJ-like)"*, *"locally nilpotent derivations (LNDs for short)"*.
- **Forward references**: announce ahead of time — "The following theorem gives a positive answer to this question.", "To prove this, we will need the following lemma.", "In order to prove it, we need the following definition."
- **Proof openers**: the first sentence usually invokes the hypothesis or a prior result. Examples:
  - "By Lemma~\ref{lm:L-structure}, $L:=\log U$ is a Lie subalgebra of $\jonq_u(k,\cO(X)_h)$…"
  - "Let us choose a filtration $G=\bigcup G_i$ as in Theorem~\ref{th:LU}."
  - "Assume (i)." / "Assume the contrary…"
- **Proof internals** are a chain of small justified steps. Itemize lists are used freely inside proofs to enumerate closed inclusions or numbered conditions; each bullet ends in a justification ("…, since $L$ is a subspace;", "… by Corollary~\ref{cr:jonq-closed};").
- **Proof closers**: one of
  - "The assertion follows."
  - "We have (i)." / "we have (ii)."
  - "as required."
  - "a contradiction."
  - `\qedhere` when the closer is mid-sentence (preserve from source).
- **Multiple-equivalent results** use `\begin{enumerate}[(i)]` with parenthesized lowercase Roman numerals; the proof then walks the cycle "Assume (i)…", "Assume (ii)…", "Assume (iii)…" rather than proving (i)⇔(ii) separately.
- **Equivalence shorthand**: "(ii)~$\Rightarrow$~(iii)" with non-breaking spaces is the author's habit when explicitly tagging implications.

### 5. Vocabulary preferences

Prefer the left column over the right.

| Use | Avoid |
|---|---|
| endowed with | equipped with |
| natural (structure / generalization) | canonical, intrinsic (when "natural" suffices) |
| analogous to / an analogue of | similar to / a similar |
| in particular | specifically, notably |
| informally, … | loosely speaking |
| see, e.g., \cite{...} | (cf. \cite{...}) — use sparingly; "loc.\ cit." for repeats within the same paragraph |
| It is enough to prove | It suffices to show |
| we may assume | without loss of generality (use "WLOG" never) |
| It is known that | classically, |
| denote by | call (denote is preferred for symbols) |
| call \emph{X} | term \emph{X} |
| consists of | is the set of (when the predicate is the point) |
| stabilizes | preserves (when group action is meant) |
| The author is grateful to … for numerous useful discussions and remarks. | I would like to thank … |
| In Section~\ref{sec:...}, we … | Section X discusses … |

Lexical tics worth preserving:
- "remarkable property", "key ingredient", "cornerstone", "central role", "infinitesimal counterpart" — used at most once each per chapter for emphasis.
- "Let us briefly describe the construction." as a meta-line before unpacking a proof idea in the introduction.
- Parenthetical re-statement: "(or, for short, X)" and "(Proposition~\ref{...})" trailing a sentence to point at the formal statement.

### 6. Mathematical typesetting conventions

These are calibrated against `jems4.tex`; many also appear in `tex/notation.tex` and override anything else in source articles.

- Field of scalars: `$\K$` (algebraically closed, characteristic zero, sometimes uncountable). "Let $X$ be an irreducible affine algebraic variety over an algebraically closed field $\K$ of characteristic zero." is the canonical opener.
- Operators: `\Aut`, `\Bir`, `\End`, `\Der`, `\LND`, `\Lie`, `\Spec`, `\ker`, `\Frac`, `\ord`, `\Jonq`, `\jonq` (lowercase fraktur for Lie algebras of `\Jonq`). Always with `\operatorname` (already defined in the preamble) — never raw text.
- Algebra of regular functions: `\cO(X)`. Field of fractions: `\K(X)`.
- Subscript invariants: `\cO(X)^U`, `\K(X)^U`. Localization: `\cO(X)_h`, `R_h`.
- Group `\G_a := (\K, +)`. Use `\G_a` consistently, not `\mathbb{G}_a` directly.
- Affine space: `\AA^n`. Integer / rational / real / complex: `\ZZ`, `\QQ`, … from `tex/notation.tex`.
- Arrow for embedding: `\embed` (`\hookrightarrow`).
- Definitions: emphasized term inside the prose with `\emph{...}`; the symbol introduced by `:=` in display math when nontrivial: `$L_\FF := \FF \otimes_A L$`.
- Citations: `\cite[Theorem~5.1.1]{FK}`, with non-breaking tilde before the locator, "see~\cite[Section~4]{Ku}" or "see, e.g.,~\cite{...}". Use a non-breaking tilde before every internal `\ref`: `Lemma~\ref{lm:L-structure}`, `Section~\ref{sec:nested}`, `Theorem~\ref{th:KZ-intro}`, `\eqref{eq:LF}`.
- Numbered statements share a counter: `\newtheorem{lemma}[theorem]{Lemma}` etc., so cross-references use the joint numbering. Preserve when adapting.
- "For short" parenthetical and "(LNDs for short)" form abbreviations on first use.

### 7. Acknowledgments and metadata

- Funding line, italic-free, in `\thanks` on the author macro: "The research was supported by the grant RSF-DST 22-41-02019." Update only if user provides a new grant.
- Acknowledgments are a single paragraph at the end of the introduction, in this order: collaborators (alphabetical first names + last names), mentor figure(s) on a separate sentence, referees on a final sentence. Template:
  > The author is grateful to *Name1, Name2, …,* and *NameN* for numerous useful discussions and remarks. The author thanks *Mentor* for his lasting encouragement and motivation. Finally, the author thanks the referees for their thorough reports that substantially shaped the final form of the paper.
- Address block: HSE University, Faculty of Computer Science, Pokrovsky blvd. 11, Moscow, 109028, Russia. Email `a@perep.ru`. Adjust per chapter only if the user changes affiliation.

### 8. Introduction architecture

The intro of `jems4.tex` is the template. When drafting or rewriting an English chapter introduction (`*_intro_en.tex`), follow this order:

1. **Hook from classical theory.** Open with a one-sentence orienting fact ("The cornerstone of the structure theory of algebraic groups, the Lie--Kolchin triangularization theorem, states that…").
2. **Limitation / generalization gap.** One or two sentences naming what is unknown or only partially known.
3. **What we do.** "We generalize this notion to an arbitrary affine variety so that an analogue of the Lie--Kolchin theorem holds."
4. **Setup paragraph.** Standing assumptions in one block: field, variety, ind-group structure, key definition (e.g., *nested*, *unipotent*).
5. **Featured prior result.** A theorem from the literature (Theorem~\ref{th:KZ-intro} pattern), then "We establish a similar property for…".
6. **Brief construction sketch.** "Let us briefly describe the construction." followed by a short paragraph naming the auxiliary objects.
7. **Main theorems** as numbered statements with `[{Theorem~\ref{th:...}}]` re-labels.
8. **"We now describe the contents of the paper in more detail."** — a paragraph per section, each one sentence: "In Section~\ref{sec:...}, we…".
9. **Acknowledgments paragraph** as in §7.

For the thesis as a whole, the same architecture transfers to `intro_en.tex`, with the part-level intros (`tex/part1_intro_en.tex`) carrying the broad framing and the per-chapter `*_intro_en.tex` files giving local motivation only — no repetition of the global background. This matches the `tex/CLAUDE.md` directive "сокращены до локальной мотивации и формулировок результатов без повтора общего фона".

### 9. Co-authored chapters

When adapting a co-authored chapter (`PR24_en.tex`, `PR23_en.tex`, `KPZ17_en.tex`, `MPS18_en.tex`, `APS14_en.tex`, `PZ26_en.tex`) to single-author voice for the thesis:

- Convert "we" of the original co-authors to the same "we" of authorial plural — usually no change is needed.
- In the local intro, add one sentence specifying the author's contribution, e.g., "The author's contribution to this chapter consists in…". Do not move this sentence into the body.
- Do **not** rewrite proofs unless the math has changed; only adjust connectives and signposting to the patterns in §3.
- Preserve original notation if it differs from `tex/notation.tex` only when changing it would force editing source files in subdirectories; otherwise harmonize via `\input{notation.tex}`.

## Anti-patterns to flag

When reviewing or rewriting, replace these:

- **AI-typical hedges**: "It is important to note", "It is worth mentioning", "Crucially," "In essence," "delve into", "leverage", "robust", "seamless", "comprehensive". None appear in the calibration corpus.
- **Em dashes** (`—` or ` -- ` between clauses) in running prose. Use commas, semicolons, or `---` for asides only.
- **Long subject-first sentences** ("The notion of a nested unipotent subgroup of the automorphism group of an affine variety is one that has been studied extensively…"). Recast with a leading connective: "Nested unipotent subgroups of $\Aut(X)$ have been studied extensively; see~\cite{...}."
- **Bullet lists outside proofs and definitions.** The author keeps prose flowing in paragraphs; itemize is reserved for enumerated equivalences, listed conditions in lemmas, and listed inclusions in proofs.
- **"In conclusion"**, **"To summarize"**, **"In summary"** as paragraph openers. Sections end with the last theorem or with a one-sentence forward pointer; chapters end with a `\section*{Discussion}` or the body's last result, not with rhetorical wrap-up.
- **Bold for emphasis in math prose.** Emphasis is `\emph{...}` only; bold is reserved for volume numbers in the bibliography.
- **"WLOG"** abbreviation. Write "we may assume".
- **Trailing "Q.E.D."** Use the environment-managed `\qed` / `\qedhere`.

## How to apply this skill

1. Read the target file with `Read`.
2. Identify drift: hedges, em dashes, subject-first heavy sentences, missing connectives, definitions without `\emph`, citations without `~`.
3. Rewrite locally with `Edit`. Keep math symbols and labels untouched; touch only prose, connectives, and emphasis.
4. After substantive prose changes, recompile per `CLAUDE.md`:
   ```
   cd tex && pdflatex -output-directory=output main_en.tex
   ```
   Run two or three times if `.aux`/`.toc` warnings persist.
5. Do not edit files in `tex/APS14/`, `tex/KPZ17/`, `tex/MPS18/`, `tex/P13/`, `tex/P18/`, `tex/P21/`, `tex/P25/`, `tex/P26/`, `tex/PR23/`, `tex/PR24/`, `tex/PZ26/` — these are first sources.

## Procedure for long files

`Read` refuses files above ~25k tokens (`jems4.tex` itself is ~38k) and defaults to 2000 lines. For a long chapter, do not attempt a single global rewrite — that pattern fails on token limits and produces sloppy edits. Instead, follow this segmented procedure.

### Survey pass

1. `wc -l` the file via `Bash` to size it.
2. `Read` the first ~200 lines to capture preamble, abstract / chapter intro, and the first section heading.
3. List the `\section{...}` / `\subsection{...}` headers with `grep -n '^\\\\\(sub\)\?section' <file>` to build a section map. Record line ranges.
4. Skim one ~300-line window per section to gauge drift density. If a section is already in voice, mark it skip.

### Window size

- **400 lines maximum per `Read` window.** Smaller (~250–300) when the section is dense with display math, since prose density per line is lower.
- Always use `offset` / `limit`. Never re-read overlapping windows just to "see context"; if you need surrounding lines, expand the window once and continue.
- Keep at most two windows worth of file content in working memory at any time. Older windows have been edited and superseded.

### Editing within a window

- One `\section` or one proof block per editing burst. Do not jump between sections.
- Each `Edit` call rewrites **at most one paragraph** (or one proof step). Smaller diffs are easier for the user to review and harder to corrupt.
- Never rewrite a whole proof in a single `Edit`; walk it step by step.
- Leave display math, labels (`\label`, `\ref`, `\eqref`, `\cite{...}`), and `\emph{...}` defined-term anchors untouched unless the calibration explicitly calls for a change.
- After finishing a window, move to the next section. Do not revisit completed sections in the same pass.

### Per-section checkpoint

After each section is rewritten:

1. Run `cd tex && pdflatex -output-directory=output main_en.tex` once to confirm the file still compiles.
2. If `.aux`/`.toc`/`.out` warnings persist, run `pdflatex` two more times before treating it as a real error.
3. Only proceed to the next section if compilation succeeded. A broken section that never compiled is harder to disentangle once a second section's edits are layered on top.

### Final pass

After all sections are done:

1. Read the chapter intro window again and re-check anti-patterns from the list above; intro language often drifts back during section-by-section work.
2. Recompile.
3. Report: which sections were rewritten, which were skipped as already in voice, which were left untouched (proofs, source-controlled subdirectories).

### When the file exceeds your read budget entirely

If even a survey pass risks exhausting context:

- Delegate the survey to a subagent (`Explore` or general-purpose) with the prompt "list `\section`/`\subsection` line ranges and flag drift indicators (em dashes, throat-clearing openers, subject-first long sentences) per section; report under 300 words." Apply the rewrite yourself based on its map.
- Or split the chapter literally — operate on one section per turn and end with a summary so the next session can pick up.

## Parallel dispatch across chapters

When the user asks to adapt several files in one go (e.g., "rewrite all `*_intro_en.tex` to my voice", or a sweep across `P13_en.tex`, `APS14_en.tex`, `MPS18_en.tex`), do not serialize. Fan out.

### When to fan out

- 2+ independent files, no shared state between rewrites.
- The user has not asked for a single coordinated diff.
- Each file fits comfortably within a subagent's context (most `*_intro_en.tex` and most `*_en.tex` chapters do).

### How to fan out

Dispatch one subagent per file in a single message with multiple `Agent` tool uses:

- `subagent_type: general-purpose` (it has `Edit` / `Write`).
- Each prompt is self-contained and includes:
  - the absolute file path,
  - "load `.claude/skills/speech-style-adaptation/SKILL.md` and apply it",
  - the segmentation rules above (or a `Read` of the procedure section),
  - explicit do-not-edit list (`tex/APS14/`, `tex/KPZ17/`, …),
  - "report under 200 words: sections rewritten, sections skipped, compile status."
- Do not have subagents recompile in parallel — `pdflatex` writes to `tex/output/` and concurrent runs collide. Ask each subagent to skip the compile step; the orchestrator runs `pdflatex` once after all subagents finish.

### When not to fan out

- Cross-chapter coordination required (e.g., harmonizing notation between `intro_en.tex` and `P26_en.tex`). Do this serially in the main session so symbol choices stay consistent.
- A single very long file. That's a job for the long-file procedure above, not for parallelism.
- The user wants to review each chapter before the next is touched — keep it serial and pause for confirmation between chapters.

## Worked micro-examples

**Drift → calibrated**

> *Drift:* It is worth noting that, by leveraging the powerful framework introduced in [KZ], we can comprehensively show that any nested unipotent subgroup which is connected is in fact closed — a result which extends earlier work.
>
> *Calibrated:* By~\cite{KZ}, a connected nested subgroup of $\Aut(X)$ is closed. This extends~\cite[Theorem~B]{KZ} from the unipotent case.

> *Drift:* In this paper we are going to study, in a comprehensive manner, the structure of unipotent subgroups of automorphism groups of affine algebraic varieties.
>
> *Calibrated:* In this article, we describe the maximal unipotent subgroups of $\Aut(X)$, where $X$ is an affine algebraic variety.

> *Drift:* Therefore it is clear that, putting everything together, we have proven the theorem.
>
> *Calibrated:* The assertion follows.

> *Drift:* Let us now move on to define a new concept which we shall call a generic frame, which will be very useful in what follows.
>
> *Calibrated:* We say that a tuple of pairwise commuting locally nilpotent derivations $\partial_1,\ldots,\partial_k\in\LND(\cO(X))$, where $k\le\dim(X)$, is a \emph{generic frame} if the corresponding vector fields are linearly independent at the general point.

## Calibration source

Single source of truth for the voice: `jems4.tex` (lines 130--215 for introduction patterns, 348--553 for proof rhythm, 700--900 for definition/proposition cadence, 1150--1240 for bibliography style). Re-calibrate this skill if the user replaces or supersedes that file.
