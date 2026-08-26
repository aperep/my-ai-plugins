# Typst rendering modes

`assets/typst/interlinear.typ` exports `sent` and `mode`. It reads the metadata
path from `--input data=...`; the default is `sentences.csv`.

| mode | output |
|---|---|
| `plain` | author text only |
| `draft` | author text with visible labels |
| `translation` | text plus `translation_en` |
| `comment` | text plus `ai_comment` |
| `parallel` | general step beside its concrete example |
| `inline-example` | example underneath each general step |
| `example-only` | only the example track |
| `gap-check` | visually flags proof/claim rows missing examples |
| `review` | translation, comments, examples, and Stacks links |

Example after copying the asset beside a document:

```sh
typst compile --input mode=review --input data=sentences.csv document.typ review.pdf
```

Typst resolves the CSV path relative to the file containing `csv(...)`. Keep
the imported library beside the metadata, or pass the appropriate relative
path.

## PDF annotation policy

Keep the sidecar metadata canonical; PDF annotations are only views of it.

- An explicit user request for a rendering mode overrides these defaults.
- By default, show compact popup badges beside annotated statements throughout
  the document.
- Within the current focus, expand selected annotations inline. Define the
  focus by a source label and a structural extent, such as a theorem block or
  subsection; never infer it from PDF page boundaries.
- Use a footnote only for one short note. Do not pack translation, explanation,
  active context, and verification state into one footnote.
- Also provide a printable annotation appendix because PDF popup support varies
  between viewers.

The bundled Typst renderer does not yet implement this focus-aware policy. The
policy is a requirement for future matching LaTeX and Typst adapters.
