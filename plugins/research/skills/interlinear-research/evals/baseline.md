# Interlinear research baseline cases

## PDF annotations follow the current focus

**Task.** Present a sentence's translation, explanation, active context, and
Lean status in a PDF. The current focus is its theorem block. Consider inline
annotations, footnotes, and clickable popup badges, including an explicit user
request for a different mode.

**Failure to avoid.** Put all four records in one dense footnote, or make a PDF
popup their only representation. Do not derive focus from a PDF page.

**Expected behavior.** Keep the sidecar records canonical. Recommend an inline
view for selected annotations within the current theorem block or subsection,
with compact popup badges beside annotated statements elsewhere. An explicit
rendering request wins. Restrict footnotes to one short note and provide a
printable annotation appendix because popup support varies. State that the
bundled Typst renderer does not implement this focus-aware policy yet.

**Observed fixture.** On 2026-08-26, a three-page pdfTeX fixture using the same
Section 3 claim showed a readable but tall inline block, a dense footnote, and
a compact native text annotation whose icon depended on the PDF viewer.
