# Rendering modes

The Typst adapter reads `--input data=...`, `--input mode=...`, and an optional
semicolon-delimited `--input focus=...`. The LaTeX adapter provides
`\InterlinearMode{...}`, `\InterlinearFocus{...}`, and
`\InterlinearPrintAppendix`.

| mode | output |
|---|---|
| `plain` | author text only |
| `draft` | author text with visible labels |
| `badges` | compact annotation badges throughout |
| `focus` | badges throughout; inline annotations for explicit focus labels |
| `inline` | inline annotation blocks throughout |
| `footnote` | one short translation note; LaTeX adapter |
| `popup` | native PDF text annotation with badge fallback; pdfLaTeX adapter |
| `translation` | text plus the configured translation |
| `comment` | text plus `explanation` |
| `parallel` | general step beside its concrete example |
| `inline-example` | example underneath each general step |
| `example-only` | only the example track |
| `gap-check` | visually flags proof/claim rows missing examples |
| `review` | translation, comments, examples, and Stacks links |

Example after copying the asset beside a document:

```sh
typst compile --input mode=focus --input focus=s008\;s009 \
  --input data=sentences.csv document.typ review.pdf
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

The Typst adapter provides visual badges and focus-aware inline blocks. Native
PDF popup annotations are a pdfLaTeX-only enhancement; always include the
printable appendix because viewer support varies.
