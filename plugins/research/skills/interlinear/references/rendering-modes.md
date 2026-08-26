# Rendering modes

Typst reads `--input data=...`, `--input mode=...`, and optional semicolon-
delimited `--input focus=...`. LaTeX provides `\InterlinearMode{...}`,
`\InterlinearFocus{...}`, and `\InterlinearPrintAppendix`.

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

Example:

```sh
typst compile --input mode=focus --input focus=s008\;s009 \
  --input data=sentences.csv document.typ review.pdf
```

Typst resolves the CSV path relative to the file containing `csv(...)`.

## PDF annotation policy

Keep the sidecar metadata canonical; PDF annotations are only views of it.

- An explicit rendering request overrides the defaults.
- Default to compact badges throughout. Within the requested theorem block or
  subsection, expand selected annotations inline; never infer focus from PDF
  pages.
- Use a footnote only for one short note. Do not pack translation, explanation,
  active context, and verification state into one footnote.
- Provide a printable appendix because popup support varies by viewer.

Native PDF popups are a pdfLaTeX-only enhancement; Typst provides visual badges
and focus-aware inline blocks.
