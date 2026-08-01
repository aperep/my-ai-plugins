---
name: occam-no-slop
author: A. Perepechko
description: >
  Catch AI slop and bad AI-generated style in mathematical prose, English or
  Russian, before it ships. Two checks: a slop tell (does the narrative flow
  smoothly and logically, or does it lean on cheap rhetorical effects and
  emphasis?) and Occam's razor (does every passage generalize correctly, could
  cases be merged, is the passage needed at all?). Use when the user says
  "de-slop", "cut the AI slop", "this reads like AI", "too much filler", "bad
  AI style", "sounds robotic", or before finalizing any LLM-drafted or
  LLM-revised passage. Complements speech-style-adaptation and
  russian-translation (which calibrate authorial voice) — run this skill
  first, since a passage in perfect voice can still be slop underneath. For
  English text, delegates sentence-level mechanics to
  `simple-english:simple-english` (ASD-STE100), pulled in as a dependency.
---

# Occam / No-Slop

Two independent checks, run in order. The first catches slop at the level of
the sentence and paragraph; the second catches it at the level of what got
written at all. Neither is about mathematical correctness — that is out of
scope, same as in `proofreading-pass`.

## Check 1 — the slop tell

Slop rarely announces itself as an error; it announces itself as a *texture*.
The tell: **the narrative is not smooth and logical — it leans on cheap
effects and emphasis instead.** Concretely, read the passage as a single
uninterrupted argument and flag it if:

- a sentence exists to sound impressive rather than to advance the argument
  (throat-clearing, grand framing, "this reveals a profound connection");
- emphasis (bold, italics, exclamation, a rhetorical question) is doing the
  work that logical sequencing should be doing;
- the connective between two sentences is vague or absent where a specific
  one (*hence*, *by construction*, *conversely*) is available and true;
- structure lists things instead of arguing them — a bullet list where a
  chain of implications belongs;
- a paragraph could be cut to one clause without losing content, only losing
  decoration.

If the argument reads as one continuous line of reasoning a reader can follow
without re-reading, it passes. If it reads as a sequence of assertive beats,
it is slop — rewrite for logical flow, not for polish.

## Check 2 — Occam's razor (base rule)

**Very important, the base rule of this skill: re-check yourself for
generalization, for merging cases, and for whether the written piece is
needed at all.** Apply this to every passage before treating it as done, not
only to passages flagged by Check 1:

1. **Generalization.** Is the statement made at the right level of
   generality? A special case dressed up as if it were general is slop; so is
   an over-general statement that then needs three exceptions.
2. **Unification of cases.** If the text handles two or three cases
   separately, could one argument cover all of them? Separate cases that
   differ only in notation are a sign the case split is doing rhetorical
   work, not logical work.
3. **Necessity.** For each sentence, paragraph, or remark: does removing it
   lose information the reader needs? If not, cut it — a shorter correct
   argument beats a longer one that merely looks more thorough.

Apply this recursively: after cutting or merging, re-run the check on what
remains, since merging two cases often reveals that a *third* passage
(motivating the split) is now unnecessary too.

## Workflow

1. Read the target passage or file with `Read`.
2. Run Check 2 first at the structural level — decide what should exist at
   all, before polishing sentences that might get cut.
3. Run Check 1 at the sentence/paragraph level on what survives.
4. For English prose, after both checks, load `simple-english:simple-english`
   (via the `Skill` tool) and apply its ASD-STE100 rules — sentence-length
   limits, active voice, one instruction per sentence — as the mechanical
   layer under the structural one. It is a third-party skill (MIT,
   AminBlg/SimpleEnglish); this skill's two checks above are original and
   independent of it.
5. For Russian prose, there is no equivalent third-party mechanical layer —
   apply `russian-translation`'s anti-pattern list (AI-typical hedges,
   wrong dashes, subject-first long sentences) alongside Checks 1–2.
6. Edit locally with `Edit`. Do not batch unrelated cuts into one edit —
   a reviewer needs to see each removal separately, same discipline as
   `speech-style-adaptation`'s per-paragraph edits.

## Scope discipline

Mathematical correctness, notation, and numbering are out of scope — flag and
move on, do not start reviewing the mathematics under cover of a slop pass.
Authorial voice (word choice, signature transitions) is a different concern,
covered by `speech-style-adaptation` and `russian-translation`; this skill
runs upstream of both, since voice calibration on top of a slop-riddled
structure just produces well-voiced slop.
