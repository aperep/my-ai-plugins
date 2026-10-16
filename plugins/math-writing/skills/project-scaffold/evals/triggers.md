# Trigger cases

| Request | Expected |
|---|---|
| "Start an English mathematical LaTeX article from my scaffold." | Load `project-scaffold`. |
| "Set up Russian theorem environments in a new LaTeX project." | Load `project-scaffold`. |
| "Start a Typst article with all notation from my LaTeX scaffold." | Load `project-scaffold` and use native Typst notation and references. |
| "Merge the preambles from these papers into my project template." | Load `project-scaffold`. |
| "Proofread this existing LaTeX paper for grammar." | Load `proofreading-pass`, not this skill. |
| "Scaffold a React application." | Do not load this skill. |

## Behavioral case

When source preambles use `fullpage` versus `geometry` or `enumerate` versus
`enumitem`, preserve the existing choice. Group the alternatives and leave new
ones commented unless the user asks to switch.

For a Typst article, copy the usable `assets/typst/` tree, choose one theorem
language, and fill only confirmed contact details.
Every LaTeX notation macro must have an equivalent, including the documented
`compose` replacement for the macro named `0` and `#` for single-letter bindings.
Compile English and Russian copies that use the notation, shared theorem
counter across section changes, proof symbols, references, and citations.
A LaTeX-pattern scan alone does not establish that a template works.
