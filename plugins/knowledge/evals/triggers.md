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
| D | Move the private person note to Family; sharing is authorized only for public email, and Family is unavailable. | `move` plus `cross-boundary`: retain source; report pending authorized excerpt; no private transfer. |
| E | Process raw inbox with the only copy of a message and a dated durable transcript; local policy permits removing processed raw items. | `process-inbox` plus `move`: preserve source and provenance before permitted removal; retain dated artifact. |
| F | Audit orphan, similar author names, unavailable external link, old operational fact, expired inbox, unattached image, and manual index with authored text. | `audit-knowledge`: evidence and unapplied proposals; unknown age threshold is a gap; preserve authored content. |
| G | Run maintenance whose MAINTENANCE.md lists audit only. | `meta:maintenance` delegates audit; does not process or clean. |
| H | Reformat a Markdown table. | None of these skills should load. |
| I | Move one inbox item and its attachment into a canonical Lab note; the storage provides no atomic move for embedded records. | `move`, without `cross-boundary`: stage/copy, verify content, provenance, and attachment at the destination, then remove only the verified source if local rules permit; report both locations and outcome. |
| J | Move 300 inbox pieces to a cloud store; item 117 fails and the job is retried. | `move` plus `cross-boundary`: inventory intended mappings, track and reconcile each item, retain item 117 at source, and resume without duplicating verified items; report moved, retained, failed, and pending counts plus manifest location. |
| K | Move a note between folders in one vault using a storage primitive documented as atomic and no-clobber. | `move`, without `cross-boundary`: the guaranteed primitive may replace copy/verify/delete; resolve both paths, refuse an overwrite, verify the destination, update references as appropriate, and report the mapping. |
| L | Process several mixed inbox lists containing clusters of related people, project, source, and task items; one item's destination cannot be verified. | `process-inbox`: inventory all in-scope items with their sources, build and review a temporary similarity-grouped view before mutations, then process one section at a time. Apply `move` per item; retain the unverifiable item at its source, reconcile the inventory, and report source-to-destination results by section. |
| M | Capture a note when `meta:*` skills are available but none has been invoked. | `knowledge-rule`: do not warn that `meta` is unavailable; availability, not prior invocation, satisfies the check. |
| N | Create a blueprint for the agent attached to a repository. | `agent-charter`: use `docs/charter/` with the six standard files; keep runtime state and live tasks elsewhere. |
| O | Add an AGora charter that inherits the main Рэсси charter in `me`. | `agent-charter`: name the parent, read it first, keep only local additions, and require explicit local text for overrides. |
| P | The attached agent updates its internal `SOUL.md`. | `agent-charter`: do not edit the charter; report the exact changed path and exact diff or before-and-after change. |
| Q | Update ordinary repository editing guidance in `AGENTS.md`; no attached-agent blueprint or self-change is involved. | `agent-charter` should not load. |
| R | Materially change a recurring charter workflow that is executed by GPT-6 and GPT-6 Luna. | `agent-charter`: give the scenario a user-facing name, require the agent to name it to the user when active, and test the affected scenario end to end on both executing models while recording scenario, model, revision, date, and outcome. |
| S | Correct a typo in `CONTEXT.md` without changing agent behavior. | `agent-charter`: preserve the correction, but do not require a scenario run for the cosmetic edit. |
| T | Add a scenario whose agent may need one clarification before an authorized write. | `agent-charter`: ask the focused question with one safe concrete default, then act without asking again when the user approves that proposal by message or a supported reaction unambiguously attached to it. Do not let the default widen authority. |

Additional routing boundaries: a repository doc-tree check belongs to
`meta:doc-map`; a relocation inside one vault may need `move` but not
`cross-boundary`. A title edit with no relocation needs neither. Zotero library
edits stay with `biblio:zotero-library`.

Use fresh context, the fixture and requests, and skill instructions. Do not give
the evaluating agent expected answers or the baseline conclusions.
