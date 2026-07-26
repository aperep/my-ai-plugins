# Bibliography Structure

- **Current bib file:** `bibliography.tex`
- **Source bib segments:** `src_biblio/`
- **Combined segments:** `src_biblio/all.tex`
- **Correspondence table:** `src_biblio/correspondence.csv`

## Key Format

- **1 author:** three letters of the surname + two last digits of year.
  Example: Petrov 2019 → `Pet19`. (Legacy `\bibitem` keys predating this rule used 1–2 letters inconsistently. `Pe09`→`Per09` and `P13`→`Per13` have been renamed to the new convention. `Sh66` (Shafarevich) stays grandfathered — it's cited from a first-source file (`.claude/skills/speech-style-adaptation/jems4.tex`, not to be edited) and used as a worked example across multiple skill docs/scripts, so renaming it has a much wider blast radius than the other two did. 3 letters applies to new keys going forward, chosen specifically to avoid collisions like Sawahara vs. van Santen both reducing to `Sa`.)
- **2 authors:** two letters of each surname + two last digits of year.
  Example: Arzhantsev & Perepechko 2014 → `ArPe14`
- **3 or more authors:** one letter of each surname + two last digits of year.
  Example: Arzhantsev, Perepechko & Süß 2014 → `APS14`
- **Duplicates:** when the same authors publish multiple works in one year, append `a`, `b`, `c`, etc.
  Example: Daigle 2008 (two papers) → `Da08a`, `Da08b`
- **Which year:** while the paper is only an arXiv preprint, key off the arXiv submission year. Once it has a real journal/proceedings publication (volume+pages, not just "accepted"), switch the key to the *publication* year and rename everywhere — the point of the key is to place the work in the literature, and that's the publication, not whenever it happened to go on arXiv. "Accepted" without volume/pages assigned yet does not count as published; keep the preprint-year key until it does.
- **Dash modifiers:** a bibkey may carry a trailing `-<modifier>` suffix, e.g. `-preprint` for a key deliberately kept pinned to the preprint version instead of following the "which year" rule above. Other dash modifiers may exist for other special cases. Deciding when to introduce one, and what it means, is the user's call — don't invent a new modifier unprompted.

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