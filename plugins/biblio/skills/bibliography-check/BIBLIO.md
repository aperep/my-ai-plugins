# Bibliography Structure

- **Current bib file:** `bibliography.tex`
- **Source bib segments:** `src_biblio/`
- **Combined segments:** `src_biblio/all.tex`
- **Correspondence table:** `src_biblio/correspondence.csv`

## Key Format

Use the plugin's canonical [citation-key convention](../../references/citekeys.md). Preserve established legacy keys unless the user explicitly asks for a coordinated rename.

## Bibitem Format

```latex
\bibitem{key}
A.~B. Surname, \emph{Title of the paper}, Journal Name \textbf{volume} (year), no.~issue, pages--pages.
```

Example:
```latex
\bibitem{Sh66}
I.~R. Shafarevich, \emph{On some infinite-dimensional groups}, Rend. Mat. Appl. (5) \textbf{25} (1966), no.~1-2, 208--212.
```

Notes:
- Initials tied to surname with `~` (non-breaking space)
- Journal volume in `\textbf{}`
- Title in `\emph{}`
- Page range with `--`
- Issue number preceded by `no.~`

## LaTeX compiler access

The project is compiled with pdflatex x2. If you have full access, then the path could be `C:\Users\kotokel\AppData\Roaming\texlive\2024\bin\windows\pdflatex.exe`. If you don't have access, skip compilation.
