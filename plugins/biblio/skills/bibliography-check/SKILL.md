---
name: bibliography-check
description: >
  Verify LaTeX bibitem entries against authoritative external metadata and report confirmed fields, discrepancies, and suggested corrections. Use for bibliography verification, DOI checks, or Russian and international mathematical references.
---

# Bibliography Check — Semantic Scholar + MathNet

This skill cross-checks LaTeX `\bibitem{...}` entries against two canonical sources:

1. **Semantic Scholar Graph API** (`https://api.semanticscholar.org/graph/v1/paper/...`) — covers virtually all English-language math, CS, and physics journals; matches by DOI, title, or arXiv ID; returns title, authors, venue, year, externalIds (`DOI`, `MAG`, `ArXiv`).
2. **MathNet (mathnet.ru)** — the canonical Russian mathematical bibliography; covers all Soviet/Russian journals (Изв. АН СССР, Матем. сб., Мат. заметки, УМН, Функц. анал. и прил., Сиб. мат. журн., и т. д.); only an HTML-search interface (no JSON API); fetched and parsed.

Use this skill for any verification of a repo's `bibliography*.tex`. The output is
per-entry, terse, and editable directly.

Paths below name the layout of a typical paper repo (`tex/bibliography*.tex`).
In a repo that files them elsewhere, ask or glob for `\bibitem` instead of
assuming; nothing here depends on the specific directory.

## Iron rules

1. **Do not edit a bibitem just because Semantic Scholar reports a different value.** Always present the discrepancy to the user and propose a fix; the user decides.
2. **MathNet is the authority for Russian-original publications** (Изв. АН СССР, etc.). When MathNet and Semantic Scholar disagree on a Russian paper, MathNet wins.
3. **Cite both sources** in the report so the user can verify quickly: include the Semantic Scholar `paperId` URL and the MathNet `mathnet.ru/rus/...` URL.
4. **Never invent a DOI**. If neither source returns a DOI, leave the entry's DOI absent.
5. Skip arXiv-only preprints, software citations (e.g. SageMath), conference proceedings without ISBN/DOI, and entries marked "in preparation" — they are out of scope; note them in the report as "skipped".

## Inputs

The skill accepts:
- A path to a `.tex` file (`tex/bibliography_resume.tex`, `tex/bibliography_resume_ru.tex`, or `tex/bibliography.tex`) — checks every `\bibitem{...}` in the file.
- A subset specified by bibkey (`Sh66`, `Is78`, `KPZ17`) — checks only those.
- A single inline `\bibitem{...}` block — checks just that one.

If the user does not specify, default to `tex/bibliography_resume.tex` (smaller, more likely to be in active use) and offer to expand to the full bibliography after the first pass.

## Workflow

1. **Parse** each `\bibitem` block and extract:
   - `key` (the `{...}` argument)
   - `authors` (comma- or `and`-separated, with initials and surnames; preserve order)
   - `title` (between `\emph{...}` or `\textit{...}` or `\newblock {\em ...}`)
   - `venue` (journal name or proceedings volume)
   - `year`
   - `volume` (`\textbf{...}`)
   - `issue` (after `no.~` or `вып.~`)
   - `pages` (`A--B`)
   - `doi` (after `doi:` or in a URL)
   - `arxiv` (after `arXiv:`)
2. **Decide source priority:**
   - If `venue` matches a Russian-journal pattern (`Изв.\ АН СССР`, `Матем.`, `Мат.\ зам.`, `УМН`, `Функц.\ анал.`, `Сиб.\ мат.`) or the title is in Cyrillic, query **MathNet first**, then Semantic Scholar.
   - Else query **Semantic Scholar first**, then optionally MathNet (only if the authors include a known Russian name and the entry might have a Russian original).
   - If `doi` is present, use the DOI lookup directly.
3. **Compare** every parsed field against the source's record. Mark each as `OK`, `MINOR` (whitespace, transliteration, abbreviation), or `MAJOR` (different volume, year, pages, or authors).
4. **Report** in a compact table per `\bibitem`. Group: confirmed entries (one line each), entries with `MINOR` issues, entries with `MAJOR` issues, skipped entries.

## Implementation

The skill works in two modes depending on network access available to the harness.

### Mode A — web search (primary in a restricted sandbox)

When direct calls to `api.semanticscholar.org` or `mathnet.ru` are blocked by
the active sandbox, use the available web-search capability.

For each bibitem, issue **two queries**:

1. **Semantic Scholar / general:** search for `<authors> <distinctive title words> <year> doi`; indexed results typically expose canonical metadata.
2. **MathNet:** search for `<author surname> <Russian title or transliteration> mathnet <year>`; results include a `mathnet.ru/eng/<slug>` or `mathnet.ru/rus/<slug>` URL.

If search returns the canonical record inline, record it directly. Do not keep
opening the same URL after the sandbox has rejected it.

The skill helper script at `scripts/check_bibitems.py` will fall back to printing `MISS` in this environment because direct HTTPS to the APIs is blocked. Use it only for **offline parsing** (`--offline`), which extracts fields from the bibitem block (title, volume, year, issue, pages, DOI, arXiv) without network. The parsed metadata is then handed to `WebSearch`.

```bash
# offline parse — produces the input rows for the WebSearch loop
python3 /absolute/path/to/bibliography-check/scripts/check_bibitems.py tex/bibliography_resume.tex --offline
python3 /absolute/path/to/bibliography-check/scripts/check_bibitems.py tex/bibliography_resume.tex --offline --keys Sh66,Is78,KPZ11
```

### Mode B — direct API (only when the harness has full network)

In a non-sandboxed shell, the same script does the lookups itself:

```bash
python3 /absolute/path/to/bibliography-check/scripts/check_bibitems.py tex/bibliography_resume.tex
python3 /absolute/path/to/bibliography-check/scripts/check_bibitems.py tex/bibliography_resume.tex --keys Sh66,Is78,KPZ11
```

Emits one block per bibitem to stdout:

```
[Is78] MAJOR
  parsed: V.A.~Iskovskikh | "Fano threefolds, II" | Math. USSR Izv. 12 (1978), no.~3, 469--506.
  ss[doi]: hit  paperId=...
  mathnet: https://www.mathnet.ru/rus/im1822
    - year matches; mathnet says: Изв. АН СССР Сер. матем., 42:3 (1978), 506--549 (Russian original)
  suggest: keep English translation OR switch to Russian original via mathnet:im1822
```

If the script returns `MISS`/`error` for every entry, you are in Mode A — switch to `WebSearch` per bibitem.

### Output

Whichever mode is used, write the final report as a Markdown table in the assistant message. Columns: `key | parsed (vol/year/pp/DOI) | source | status | discrepancies | suggested fix`. For `MAJOR` discrepancies, surface the proposed edit to the user before applying it via the `Edit` tool.

```
[Sage20] skipped (software citation)
```

**Always** offer to save the report to `tex/BIBLIO_REPORT.md` so the user has a record between sessions.

## Manual lookup (fallback)

When the helper script is not usable, query directly:

### Semantic Scholar by title

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=Fano+threefolds+Iskovskikh&limit=5&fields=title,authors,year,venue,externalIds" \
  | python3 -m json.tool
```

### Semantic Scholar by DOI

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1090/S0002-9939-09-09913-4?fields=title,authors,year,venue,externalIds"
```

### MathNet by title (HTML; parse with grep/regex)

```bash
curl -s --data "query=$(printf 'Трёхмерные многообразия Фано' | jq -sRr @uri)" \
  "https://www.mathnet.ru/php/search.phtml?wshow=search&option_lang=rus" \
  | grep -oE 'href="/rus/[a-z0-9_]+"' | head -10
```

Each `mathnet.ru/rus/<slug>` URL exposes canonical metadata. Open it with the
available web-reading capability:

```text
https://www.mathnet.ru/rus/im1822
```

## Output format

Write the final report as a Markdown table in the assistant message and (if the user agrees) save to `tex/BIBLIO_REPORT.md`. Columns: `key | parsed | source | status | discrepancies | suggested fix`.

## How to apply this skill

When the user asks to verify the bibliography:
1. Confirm the target file (default: `tex/bibliography_resume.tex`).
2. Resolve this skill's installed directory from `SKILL.md`, then run
   `python3 <skill-directory>/scripts/check_bibitems.py <file>`.
3. Read the report; for each `MAJOR` discrepancy, surface it to the user with the proposed fix.
4. Apply edits only after the user confirms.
5. Re-run the script to verify all issues are resolved.

When verifying a single new bibitem mid-edit, pass it as a one-shot via stdin:

```bash
echo '\bibitem{Test} ...' | python3 /absolute/path/to/bibliography-check/scripts/check_bibitems.py -
```

## Calibration notes

- The helper script's parser has been calibrated against the format spelled out in `BIBLIO.md` (bundled in this skill directory) (initials tied with `~`, `\textbf{}` for volume, `\emph{}` for title, `--` for page ranges, `no.~` for issue, `doi:` prefix). Variant inputs (`{\em ...}`, `\newblock`, `\href {...} {...}`) are also supported.
- Semantic Scholar's title-search is fuzzy enough to match minor typos but not transliteration differences — for Russian authors search by surname + a distinctive English word from the title.
- MathNet HTML is brittle; if the regex stops matching, dump the page with `WebFetch` and parse with the model's reading rather than re-scraping.
