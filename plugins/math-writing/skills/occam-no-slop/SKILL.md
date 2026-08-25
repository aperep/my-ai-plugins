---
name: occam-no-slop
description: >
  Remove filler, needless case splits, and rhetorical clutter from English or
  Russian mathematical prose while preserving its claims. Use for explicit
  de-slopping requests such as "cut the AI slop", "remove filler", "this reads
  like AI", or "make this argument flow". Do not use for ordinary drafting,
  proofreading, voice matching, controlled English, or mathematical review.
reviewed: 13f6807
---

# Occam / No-Slop

Make the argument no longer than its logic requires. Preserve the author's
claims, hypotheses, notation, and degree of emphasis.

## Pass 1: structure

Work from large units to small ones:

1. **Necessity.** Cut a sentence, paragraph, remark, or heading if it adds no
   fact, inference, orientation, or useful warning.
2. **Unification.** Merge cases that use the same argument. Keep a split when
   the hypotheses, mechanism, or reader's task differs.
3. **Generality.** State an established argument at the cleanest level already
   justified by the source. If a broader statement needs new mathematics,
   flag the possibility instead of editing it in.

Repeat this pass after a cut or merge. Earlier scaffolding can become obsolete.

## Pass 2: continuity

Read what remains as one argument. Repair these failures:

- An opening announces importance but supplies no content.
- A sentence repeats the previous sentence with stronger adjectives.
- Emphasis or a rhetorical question replaces a logical transition.
- A vague transition hides the real relation. Use a precise connective only
  when it is true, for example *hence*, *conversely*, or *by construction*.
- A list fragments a chain of reasoning. Use prose when order or implication
  matters; keep a list when the items are genuinely parallel.

Valid emphasis can orient the reader or mark a real warning. Do not flatten it
merely because generated text often overuses emphasis.

## Deliver

Rewrite only after both passes. Keep mathematical notation and references
intact. Report any suspected mathematical defect separately; do not silently
repair it during this editorial pass.

If the user also requests authorial voice, apply the relevant voice skill after
this pass. Use `simple-english` for technical instructions or controlled
English, not as a mechanical filter for mathematical narrative.
