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

## One dataset serves Typst and LaTeX

**Task.** Label matching statements in a Typst source and a LaTeX source, then
validate both against one CSV sidecar.

**Baseline failure.** The LaTeX adapter wraps whole passages in
`\sent{semantic.label}{...}`, so sentence boundaries disappear inside nested
arguments and labels expose document structure.

**Expected behavior.** Put every LaTeX sentence or independently meaningful
clause on one physical source line ending in a stable marker such as
`\itag{dJ2z}`. Require one unique four-character alphanumeric ID per
line, keep the command implementation in `interlinear.sty`, parse matching
Typst units, and apply the same label/row invariants to both formats.

## Candidate matches are not confirmed references

**Task.** Fill likely Stacks matches by lexical similarity.

**Baseline failure.** `stack_lookup.py --fill` writes directly to `stacks_ref`,
which the renderer presents as a reference.

**Expected behavior.** Write `stacks_candidate`; change `stacks_ref` only after
the result and hypotheses have been checked.

## Local context is filtered by tags

**Task.** Dump the currently effective definitions for one proof step.

**Baseline failure.** The context dump returns every earlier row whose source
span is active, even if it is an unrelated translation or topic.

**Expected behavior.** First apply source-span lifetime, then require a shared
context tag when tag filters are supplied. Return the selected text and its
metadata so `reason` and `formalize` see the same context.
