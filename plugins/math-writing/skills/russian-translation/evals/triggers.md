# Trigger tests — russian-translation

## Must load

- "Translate this algebraic-geometry abstract into Russian in Perepechko's style."
- "Переведи эту главу диссертации на русский."
- "Приведи русский текст доказательства к моему авторскому стилю."
- "Revise this Russian theorem statement using the established authorial voice."
- "Check terminology consistency in this Russian mathematical chapter."

## Must not load

| Request | Expected handling |
|---|---|
| "Proofread this Russian paper for typos only." | `proofreading-pass` |
| "Translate this business email into Russian." | ordinary translation |
| "Check whether the theorem is true." | mathematical review |
| "Adapt this English paper to Perepechko's English voice." | `speech-style-adaptation` |
| "Set up Russian theorem environments in a new LaTeX project." | `latex-project-scaffold` |
| "Remove filler from this English mathematical paragraph." | `occam-no-slop` |
