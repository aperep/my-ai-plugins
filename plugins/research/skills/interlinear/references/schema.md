# Interlinear CSV schema

The source order, not lexical label order, defines all spans.

| column | meaning | required |
|---|---|---|
| `label` | stable identifier matching `sent("label")[...]` | yes |
| `translation_<lang>` | translation, with a language suffix such as `translation_en` | no |
| `explanation` | informal explanation; must not masquerade as verified fact | no |
| `active_until` | final source label for which this row remains active | no |
| `tags` | semicolon-delimited roles/topics used to select local context | no |
| `stacks_candidate` | unchecked lexical Stacks match, without URL prefix | no |
| `stacks_ref` | human-checked Stacks tag, without URL prefix | no |
| `example_subject` | concrete object announced at the start of an example track | no |
| `example_step` | the labelled general step worked through on that object | no |
| `lean_status` | blank, `planned`, `generated`, `checked`, or `failed` | no |
| `lean_ref` | Lean file and declaration name | no |
| `lean_toolchain` | exact Lean version or pinned project revision | no |
| `lean_note` | short formalization note or checker failure | no |

Required operational rules:

- Keep one row per source label and retain source order in the CSV.
- Quote fields containing commas or line breaks using normal CSV quoting.
- Treat `active_until` as inclusive. An empty value means only the statement
  itself unless a project explicitly defines another policy.
- Use exact tag tokens. Source lifetime is the first context filter; a requested
  tag set is the second. For example, `proof-outline` is not the `proof` tag.
- A missing example is a review signal, not proof that the general step is
  false.
- A lexical lookup may change `stacks_candidate`, never `stacks_ref`.
- Set `lean_status=checked` only when the recorded declaration passed a Lean
  checker, and record both `lean_ref` and `lean_toolchain`. Aristotle
  suggestions and generated Lean start as `generated`.
- Keep richer prover logs and Lean source in separate artifacts; the CSV stores
  only a stable summary and reference.
