# Rendering modes

LaTeX provides `\InterlinearMode{...}`, `\InterlinearFocus{...}`, and
`\InterlinearPrintAppendix`.

| mode | output |
|---|---|
| `plain` | author text only |
| `draft` | author text with visible IDs |
| `badges` | compact linked badges; default |
| `focus` | badges plus inline comments for selected IDs |
| `inline` | inline comments for every tagged line |
| `footnote` | the translation as a short footnote |

Default to `badges`. Use `focus` for the requested theorem block or subsection,
and keep the printable appendix because badges link to it. An explicit user
request for another mode wins.
