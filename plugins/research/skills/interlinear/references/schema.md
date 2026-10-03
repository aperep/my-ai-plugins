# Interlinear CSV schema

The source order, not lexical label order, defines all spans.

| column | meaning | required |
|---|---|---|
| `label` | stable ID matching a source `sent` or `\itag`; use four random alphanumeric characters for new labels | yes |
| `translation_<lang>` | translation, e.g. `translation_en` | no |
| `explanation` | informal explanation; must not masquerade as verified fact | no |
| `active_until` | final source label for which this row remains active | no |
| `tags` | semicolon-delimited roles/topics used to select local context | no |
| `stacks_candidate` | unchecked lexical Stacks match, without URL prefix | no |
| `stacks_ref` | human-checked Stacks tag, without URL prefix | no |
| `example_subject` | object used for an example track | no |
| `example_step` | general step worked through on that object | no |
| `lean_status` | blank, `planned`, `generated`, `checked`, or `failed` | no |
| `lean_ref` | Lean file and declaration name | no |
| `lean_toolchain` | exact Lean version or pinned project revision | no |
| `lean_note` | short formalization note or checker failure | no |

Required operational rules:

- Keep one row per source label in source order.
- Treat `active_until` as inclusive. An empty value means only the statement
  itself unless a project explicitly defines another policy.
- Filter context first by source lifetime, then by exact requested tags;
  `proof-outline` is not `proof`.
- A missing example is a review signal, not a disproof.
- A lexical lookup may change `stacks_candidate`, never `stacks_ref`.
- Set `lean_status=checked` only when the recorded declaration passed a Lean
  checker, and record both `lean_ref` and `lean_toolchain`. Aristotle
  suggestions and generated Lean start as `generated`.
- Keep prover logs and Lean source outside the CSV; store only their stable
  summary and reference there.
