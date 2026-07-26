---
name: extracting-precise-results
description: Use when summarizing a paper's contributions for a bibliography note, literature survey, or citation, where a prose paraphrase without theorem/proposition numbers would lose citability — e.g. writing "main result: shows existence of X" instead of the exact numbered statement with its hypotheses.
---

# Extracting Precise Results

## Overview

A paraphrased "main result" isn't citable — a numbered theorem with its exact hypotheses is. This skill pulls precise numbered statements (theorem/proposition/lemma/corollary) from a paper's full text, for use in bibliography notes, surveys, or citations.

## When to use

- Writing or updating a bibliography note, survey section, or literature review that needs to cite "Theorem X.Y" rather than summarize.
- **Not for** first-pass relevance triage — an abstract is enough to decide "is this on-topic?"; only pull full text once a paper is already worth citing precisely.

## Workflow

1. Prefer arXiv's HTML rendering: `https://arxiv.org/html/<id>` (or the "HTML (experimental)" link on the abstract page). Numbered theorem/proposition/lemma environments usually come through as plain, extractable text — cheaper and more reliable than PDF parsing.
2. No HTML version (older paper, non-arXiv source)? Fetch the PDF and explicitly ask for exact numbered statements, not a summary — prompts asking for "the abstract" or "main results" in general terms tend to return paraphrase even when given the full text.
3. Record each relevant result close to verbatim: number + hypotheses + conclusion, e.g. "Theorem 3.2 ($S$ smooth, $\deg\ge 2$, $H$ ample): $S$ admits an $H$-polar cylinder." Don't collapse two distinct numbered results into one unnumbered sentence, and don't drop the hypotheses to save words — the hypotheses are usually the point of the theorem.
4. If full text is genuinely inaccessible (paywalled, no HTML/PDF found), say so explicitly wherever the result gets used, instead of reconstructing it from the abstract and presenting it as precise.

## Common mistakes

- Working from the abstract or a search snippet and writing "shows that X holds" — reads like a citation but isn't traceable to a specific statement.
- Merging multiple theorems into one summary sentence — loses which hypotheses go with which conclusion.
- Silently falling back to abstract-level paraphrase when the PDF/HTML fetch fails, instead of flagging the gap.

## Used by

`zotero-mcp` (survey/auto-fill mode when creating biblio notes) and any paper-writing or review skill that needs to cite specific results rather than summarize a paper generally.
