# Trigger cases

| Request | Expected |
|---|---|
| "Start an English mathematical LaTeX article from my scaffold." | Load `project-scaffold`. |
| "Set up Russian theorem environments in a new LaTeX project." | Load `project-scaffold`. |
| "Merge the preambles from these papers into my project template." | Load `project-scaffold`. |
| "Proofread this existing LaTeX paper for grammar." | Load `proofreading-pass`, not this skill. |
| "Scaffold a React application." | Do not load this skill. |

## Behavioral case

When source preambles use `fullpage` versus `geometry` or `enumerate` versus
`enumitem`, preserve the existing choice. Group the alternatives and leave new
ones commented unless the user asks to switch.
