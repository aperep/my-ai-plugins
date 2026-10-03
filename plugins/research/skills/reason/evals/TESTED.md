# Reason test status

On 2026-10-03, `research@aperep` 0.6.0 moved interlinear context and examples
to typed `\ic` comments. The instructions and eval cases now read those
records directly; fresh-context routing and behavior were not rerun.

On 2026-08-26, revision `ac7d6c0` was installed locally as
`research@aperep` version `0.4.1` and tested in fresh context with
`gpt-5.6-sol` under Codex 0.149.1.

- The proof-explanation routing case selected `research:reason`.
- The section-3 behavior case selected only the active tagged setup, stated
  what it established, and correctly reported that it did not define the
  target's `m`, `D`, or filtration argument.
- The nearby copyediting case selected `math-writing:proofreading-pass`, not
  `reason`.
