---
name: personal-bibliography
description: >
  Reuse or maintain A. Perepechko's bundled LaTeX bibliography corpus and list
  of authored papers when starting a paper, CV-like publication list, or
  bibliography cleanup. Use only when the user wants this personal corpus;
  use bibliography-check for generic metadata verification.
---

# Personal bibliography

The `assets/` directory contains two source corpora migrated from the academic
workshop:

- `bibliography.tex`: a large `\bibitem` collection used as a source library;
- `biblio_me.tex`: A. Perepechko's authored-paper list.

Copy selected entries into the target project rather than editing the bundled
corpus for a one-off paper. Preserve citation keys unless the target project has
a documented key policy. Deduplicate by work identity, not merely by key: the
large corpus intentionally contains historical and alternate-form entries.

Before presenting metadata as current or correct, use the bibliography-check
workflow or verify against authoritative sources. Confirm affiliation,
publication status, and year-sensitive entries before producing a public CV.
