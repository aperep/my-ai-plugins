# Trigger cases

| Request | Expected |
|---|---|
| “Proofread this LaTeX paper and give me a change log.” | Load `proofreading-pass`. |
| “Copyedit this draft for grammar, punctuation, and TeX errors.” | Load `proofreading-pass`. |
| “Check the language of this paper before submission.” | Load `proofreading-pass`. |
| “Rewrite this paper in Perepechko's voice.” | Load `speech-style-adaptation`, not this skill. |
| “Remove the AI slop from this proof.” | Load `occam-no-slop`, not this skill. |
| “Check whether this theorem and proof are correct.” | Do not load this skill. |

## Behavioral cases

- Apply a clear typo such as `Futhermore` to `Furthermore`; label it
  `[Applied] [Typo]`.
- Suggest, but do not apply, `So` to `Thus` or `we will get` to `we obtain`;
  label it `[Suggested] [Voice]`.
- Suggest, but do not apply, a likely symbol replacement; label it
  `[Suggested] [Notation]`.
- Give every category an independent `Applied` or `Suggested` status.
- Open the change log with the count and original-source line numbers of all
  major issues across both statuses; state that none were found when applicable.
