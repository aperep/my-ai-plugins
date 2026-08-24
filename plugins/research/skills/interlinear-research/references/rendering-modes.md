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
