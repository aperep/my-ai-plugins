# Trigger cases

| Request | Expected |
|---|---|
| "Cut the AI slop from this proof introduction." | Load `occam-no-slop`. |
| "Remove filler and merge needless cases in this lemma." | Load `occam-no-slop`. |
| "Make this mathematical argument flow without changing its claims." | Load `occam-no-slop`. |
| "Proofread this paper for grammar and LaTeX errors." | Load `proofreading-pass`, not this skill. |
| "Is this theorem true? Check the proof." | Do not load this skill. |
| "Rewrite this runbook in ASD-STE100." | Load `simple-english`, not this skill. |
| "Adapt this section to Perepechko's voice." | Load the relevant voice skill, not this skill unless de-slopping is also requested. |

## Behavioral cases

- Filler: remove grand framing that adds no claim.
- Case split: merge notation-only cases; retain cases with different arguments.
- Emphasis: retain emphasis that marks a genuine warning or logical pivot.
- Generality: suggest, but do not apply, a stronger theorem not proved by the
  source.
