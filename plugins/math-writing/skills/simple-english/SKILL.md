---
name: simple-english
description: >
  Write or rewrite English technical instructions and explanations for quick,
  unambiguous reading. Use for plain-language documentation, runbooks, error
  messages, or explicit Simplified Technical English and ASD-STE100 requests.
  Do not use as a general de-slopping, marketing, literary, or mathematical
  prose style.
---

# Simple English

Preserve facts and technical meaning. Simplify the language, not the subject.

## Choose the mode

- **Plain technical English** is the default. Prefer direct sentences and
  stable terminology without enforcing an aerospace standard.
- **ASD-STE100** applies only when the user names STE, ASD-STE100, controlled
  English, or compliance. Read [references/asd-ste100.md](references/asd-ste100.md)
  before editing.

## Rewrite

1. Separate procedures, which tell the reader what to do, from descriptions,
   which explain facts.
2. Use one term for each concept. Do not rotate synonyms for variety.
3. Put the actor and action early. Prefer active voice when it identifies who
   acts; retain a useful passive when the actor is unknown or irrelevant.
4. In procedures, use direct commands, one action per step. Put a condition
   before the command that depends on it.
5. In descriptions, keep one topic per paragraph. Split a sentence when it
   carries unrelated facts.
6. Delete framing, hedges, and praise that add no fact. Replace vague claims
   such as "robust" with the stated property; do not invent a measurement.

Keep code, identifiers, commands, paths, quoted messages, product names, UI
labels, and mathematical notation exact unless the user asks to change them.

Before delivery, check that terminology is stable, references are clear, each
procedure step has one action, and no condition trails its command.

This skill is adapted from AminBlg's MIT-licensed SimpleEnglish skill. See
[UPSTREAM-LICENSE.md](UPSTREAM-LICENSE.md).
