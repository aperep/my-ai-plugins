# Calibrated English voice

The calibration source is the bundled single-author paper `../jems4.tex`.
These are tendencies, not quotas. Preserve a sound passage when a proposed
change would only make it imitate the corpus more visibly.

## Stance and rhythm

- Use first-person plural for mathematical narrative: “we describe”, “we
  show”, “we may assume”. In acknowledgments, use “the author”.
- Use “Let us” sparingly for a setup or proof goal. Imperatives such as
  “Consider”, “Let”, “Recall that”, “Assume that”, and “Write” are common setup
  moves.
- Prefer short or medium declarative sentences. Split a sentence when its
  logical chain becomes hard to follow, but do not flatten necessary
  qualifications.
- State the governing reason near the start of a proof step: “By
  Lemma~\ref{...}, ...” or “By construction, ...”. Ordinary subject-first
  sentences are also part of the corpus; never add a connective mechanically.
- Use an assertive tone within what has been proved. Preserve genuine
  uncertainty from the source.
- Use commas and semicolons for ordinary clause boundaries. In TeX, the corpus
  uses `---` for a true parenthetical aside, not an em dash as generic
  punctuation.

## Transitions

Choose a transition for its logical function, not for surface variety.

| Function | Typical forms |
|---|---|
| Consequence | Then; Thus; Hence; It follows that; In particular |
| Justification | By Lemma~\ref{...}; By construction; By assumption; Indeed |
| Addition | Moreover; We also ... |
| Contrast | Conversely; On the other hand; However |
| Recall | Recall that; As above |
| Reformulation | Equivalently; Namely; That is |
| Forward reference | We will need the following lemma; The following theorem ... |
| Short proof close | The assertion follows; as required; a contradiction |

Do not replace a precise causal or adversative relation with a vague
transition. Do not add a transition where the source does not justify one.

## Definitions, results, and proofs

- Introduce a defined term inline with `\emph{...}` and a short self-contained
  defining clause. Use “for short” for an abbreviation when that form fits the
  sentence.
- Orient a section with one or two sentences when the reader needs a map:
  “In this section we describe ...” or “Here we ...”.
- Announce a result or required lemma before its statement when this explains
  its role. Avoid announcements that merely repeat the theorem title.
- Begin a proof from a hypothesis, construction, or prior result. Develop it as
  a sequence of justified steps.
- For several equivalent conditions, the corpus often walks through the
  implications with “Assume (i)” and “We have (ii)”. Preserve the source's
  proof organization unless restructuring was requested.
- End a proof at the mathematical endpoint. Short closers such as “The
  assertion follows” are characteristic when they add useful closure.

## Word choices

These preferences apply when both forms express the same claim.

| Prefer | Less characteristic |
|---|---|
| endowed with | equipped with |
| a natural structure or generalization | canonical or intrinsic without need |
| in particular | specifically; notably |
| informally | loosely speaking |
| It is enough to prove | It suffices to show |
| we may assume | WLOG |
| denote by, for a symbol | call, for a symbol |
| consists of | is the set of |
| In Section~\ref{...}, we ... | Section X discusses ... |

Prefer “Note that” or a direct statement to an empty importance announcement.
Do not force a listed preference when it changes technical meaning or conflicts
with established project usage.

## Small examples

> It is worth noting that we can comprehensively show the following result.

Use the claim itself, or a precise lead-in: “The following theorem gives a
positive answer to this question.”

> Therefore, putting everything together, we have proven the theorem.

When the preceding steps already contain the proof: “The assertion follows.”

These examples calibrate tone. Removing filler or reorganizing an argument as
a separate task belongs to `occam-no-slop`.
