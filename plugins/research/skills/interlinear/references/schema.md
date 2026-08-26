# Interlinear CSV schema

The source order, not lexical label order, defines all spans.

| column | meaning | required |
|---|---|---|
| `label` | stable identifier matching `sent("label")[...]` | yes |
| `translation_en` | English translation; another project may add language-specific columns | no |
| `ai_comment` | research note or explanation; must not masquerade as verified fact | no |
| `active_until` | final source label for which this row remains active | no |
| `tags` | semicolon-delimited roles/topics | no |
| `stacks_ref` | Stacks Project tag, without URL prefix | no |
| `example_subject` | concrete object announced at the start of an example track | no |
| `example_step` | the labelled general step worked through on that object | no |

Required operational rules:

- Keep one row per source label and retain source order in the CSV.
- Quote fields containing commas or line breaks using normal CSV quoting.
- Treat `active_until` as inclusive. An empty value means only the statement
  itself unless a project explicitly defines another policy.
- Use exact tag tokens. For example, `proof-outline` is not the `proof` tag.
- A missing example is a review signal, not proof that the general step is
  false.
- Stacks references are candidates until their statements and hypotheses have
  been checked against the current claim.
