---
parent: README.md
---

# Knowledge

Reusable operations for knowledge in vaults, Git repositories, clouds, and
private stores. Paths, schemas, and lifecycles stay in the consuming storage.

- [find-knowledge](skills/find-knowledge/SKILL.md): source-mapped retrieval with explicit coverage.
- [knowledge-rule](skills/knowledge-rule/SKILL.md): placement and capture.
- [move](skills/move/SKILL.md): safe relocation and source retirement.
- [cross-boundary](skills/cross-boundary/SKILL.md): audience-aware transfers.
- [process-inbox](skills/process-inbox/SKILL.md): classify and process inbox series.
- [audit-knowledge](skills/audit-knowledge/SKILL.md): findings and proposed diffs.
- [agent-charter](skills/agent-charter/SKILL.md): repository blueprints for attached agents and reconciliation with runtime Markdown.

Use with `meta` for documentation conventions and repository maintenance.
If no `meta:*` skill is available, warn once and use the available local
instructions.
No Obsidian dependency, storage connector, or background scheduler is bundled.

The root `plugin.json` packages these skills as a portable Agent Plugin. Codex
uses its client-specific manifest; both formats share the same `skills/`
directory.

A consumer links its storage map from `AGENTS.md`. Each entry needs only
purpose, inbox (what and how), and relationships. Resolve maintenance and
lifecycle instructions inside the relevant repository. Local work needs a
brief routing map, not an inventory of other storages' contents.

Existing vault migrations are separate changes: flag conflicting local rules
instead of silently replacing their schemas or moving their notes.

Plugin evaluation: [baseline](evals/baseline.md), [cases](evals/triggers.md),
[results](evals/TESTED.md). Newer skills keep their own evals beside the skill.
