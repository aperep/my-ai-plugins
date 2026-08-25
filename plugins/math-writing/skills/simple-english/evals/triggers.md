# Trigger cases

| Request | Expected |
|---|---|
| "Rewrite this paragraph in simple English." | Load `simple-english`. |
| "Make this abstract easier for non-native readers." | Load `simple-english`. |
| "Put this email into plain English without changing its tone." | Load `simple-english`. |
| "Cut the AI slop from this proof." | Load `occam-no-slop`, not this skill. |
| "Proofread this paper for grammar." | Load `proofreading-pass`, not this skill. |
| "Audit this maintenance manual for ASD-STE100 compliance." | Do not load this skill. |

## Behavioral cases

- Keep a necessary technical term and explain it instead of replacing it with
  an inaccurate common word.
- Retain passive voice when the actor is unknown or irrelevant.
- Delete vague praise without inventing a measurable replacement.
- Preserve the source's uncertainty, emphasis, and logical relations.
