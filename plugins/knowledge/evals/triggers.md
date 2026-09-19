---
parent: plugins/knowledge/README.md
---

# Behavioral cases

Fixture: research vault `Lab` has professional people information only;
`Personal/people/` holds private information; `Family` is shared. A storage map
provides purpose, inbox instructions, and relationships, but no concrete private
inbox path is supplied in these requests. `Lab/inbox/raw.md` is temporary;
`Lab/sources/2026-09-18-chat.md` is durable. `Lab/people/Mira.md` exists;
no family note about Mira exists. Lab currently mixes source records and scraps
in its inbox and uses `#in-progress`.

| Case | Request | Expected behavior / routing |
|---|---|---|
| A | Save chat/42: “Mira proved lemma X; I should email her Friday; her private medical appointment is Tuesday.” | `knowledge-rule`, plus `cross-boundary` if filing across stores. Resolve inbox; preserve provenance and audience; no invented source folder or unrequested processing. |
| B | Save the same message after its capture exists. | `knowledge-rule`: reuse the capture; no duplicate. |
| C | Extract a paragraph with its own open status and inbound reference from a long coherent note. | `knowledge-rule`: preserve paragraph identity/references; do not split the rest for length. |
| D | Move the private person note to Family; sharing is authorized only for public email, and Family is unavailable. | `cross-boundary`: retain source; report pending authorized excerpt; no private transfer. |
| E | Process raw inbox with the only copy of a message and a dated durable transcript; local policy permits removing processed raw items. | `process-inbox`: preserve source and provenance before permitted removal; retain dated artifact. |
| F | Audit orphan, similar author names, unavailable external link, old operational fact, expired inbox, unattached image, and manual index with authored text. | `audit-knowledge`: evidence and unapplied proposals; unknown age threshold is a gap; preserve authored content. |
| G | Run maintenance whose MAINTENANCE.md lists audit only. | `meta:maintenance` delegates audit; does not process or clean. |
| H | Reformat a Markdown table. | None of these skills should load. |

Additional routing boundaries: a repository doc-tree check belongs to
`meta:doc-map`; a routine rename inside one vault does not need
`cross-boundary`. Zotero library edits stay with `biblio:zotero-library`.

Use fresh context, the fixture and requests, and skill instructions. Do not give
the evaluating agent expected answers or the baseline conclusions.
