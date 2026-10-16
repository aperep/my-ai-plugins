# Compilation baseline

On 2026-10-16, at `12c9682`, the LaTeX-pattern scanner passed
`references/slides.typ`, but Typst 0.15.1 rejected its `angle.l` and `angle.r`
symbols.
The Russian slide starter compiled with a convergence warning caused by its
empty final bibliography slide.

The check passes when both source files compile without diagnostics, the
slide example uses native chevron symbols, and the bibliography starter has
visible placeholder content.
