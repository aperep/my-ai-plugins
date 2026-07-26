# LaTeX → Typst: стандартные замены

## Документ и структура
- `\\section{Title}` → `= Title`
- `\\subsection{Title}` → `== Title`
- `\\subsubsection{Title}` → `=== Title`
- `\\paragraph{Title}` → `==== Title`

## Выделение и текст
- `\\textbf{...}` → `*...*`
- `\\emph{...}` → `_[...]_` или `_..._`
- `\\texttt{...}` → `` `...` ``
- `\\underline{...}` → `#underline[...]`

## Списки
- `\\begin{itemize} ... \\item ... \\end{itemize}` → `- ...`
- `\\begin{enumerate} ... \\item ... \\end{enumerate}` → `+ ...`

## Математика
- `$ ... $` → `$ ... $` (обычно совместимо, но проверить команды)
- `\\[ ... \\]` / `\\begin{equation} ... \\end{equation}` → `$ ... $` (display)
- `\\frac{a}{b}` → `a / b` или `frac(a, b)`
- `\\cdot` → `dot`
- `\\times` → `times`
- `\\sum_{i=1}^n` → `sum_(i=1)^n`
- `\\int_a^b` → `integral_a^b`

## Ссылки и библиография
- `\\label{key}` → `<key>` (label рядом с объектом)
- `\\ref{key}` → `@key`
- `\\cite{key}` → `@key` (или через выбранный citation style)
- `\\bibliography{refs}` / biblatex-пакеты → `#bibliography("refs.bib")`

## Рисунки и таблицы
- `\\includegraphics[width=...]` → `#image("file", width: ... )`
- `\\caption{...}` → `caption: [ ... ]`
- `\\begin{tabular} ... \\end{tabular}` → `#table(...)`

## Типичные anti-patterns
- LaTeX-пакеты (`\\usepackage`) в Typst не нужны.
- Массовый raw-LaTeX внутри Typst усложняет поддержку.
- Механический перенос без стилистической адаптации ухудшает читабельность.
