# Test status

On 2026-08-25, revision `e2aa78f` received an independent fresh-context
evaluation after local installation as version 0.3.8. The evaluation
environment exposed no model identifier, so the exact model could not be
recorded.

The behavioral case preserved genuine uncertainty, claims, paragraph shape,
and non-corpus notation while replacing only two calibrated wording choices.
The routing cases selected `proofreading-pass`, `occam-no-slop`,
`russian-translation`, and `speech-style-adaptation` as expected.

The skill validator, JSON parsing, the Claude plugin and marketplace
validators, and local Codex installation passed. The Claude validators
reported the repository's existing warnings that its plugin manifests omit
version fields.
