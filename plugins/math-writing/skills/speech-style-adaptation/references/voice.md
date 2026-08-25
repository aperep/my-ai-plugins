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
- State the governing reason near the start of a proof step: “By
  Lemma~\ref{...}, ...” or “By construction, ...”. Ordinary subject-first
  sentences are also part of the corpus; never add a connective mechanically.
- Use an assertive tone within what has been proved. Preserve genuine
  uncertainty from the source.

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

Use no transition where the source does not justify one.

## Definitions, results, and proofs

- Introduce a defined term inline with `\emph{...}` and a short self-contained
  defining clause. Use “for short” for an abbreviation when that form fits the
  sentence.
- Orient a section with one or two sentences when the reader needs a map:
  “In this section we describe ...” or “Here we ...”.
- Announce a result or lemma only when the lead-in explains its role.
- Begin a proof from a hypothesis, construction, or prior result, then use
  small justified steps.
- For several equivalent conditions, the corpus often walks through the
  implications with “Assume (i)” and “We have (ii)”. Preserve the source's
  proof organization unless restructuring was requested.
- End a proof at the mathematical endpoint. Short closers such as “The
  assertion follows” are characteristic when they add useful closure.

## Word choices

These preferences apply when both forms express the same claim.

| Prefer | Less characteristic |
|---|---|
| in particular | specifically; notably |
| informally | loosely speaking |
| It is enough to prove | It suffices to show |
| we may assume | WLOG |
| denote by, for a symbol | call, for a symbol |
| In Section~\ref{...}, we ... | Section X discusses ... |

Do not force a listed preference when it changes technical meaning or conflicts
with established project usage.
