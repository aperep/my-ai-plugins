# Test status

On 2026-08-25, revision `7ebcd5d` passed JSON parsing, `git diff --check`,
Claude validation of the plugin and marketplace, and local Codex installation
as `research@aperep` version `0.2.1`.

Fresh-context routing probes used `gpt-5.6-sol` via Codex 0.149.1:

- Exact Theorem 3.2 hypotheses, conclusion, and location: loaded
  `research:extracting-precise-results`.
- Abstract relevance triage: loaded no skill.
- General-audience paper summary: loaded no skill.

The behavioral extraction cases still need tests against real papers.
