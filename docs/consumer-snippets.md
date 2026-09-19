---
parent: README.md
---

# Academic project setup

## Codex

Install the groups needed by the repository:

```sh
codex plugin add research@aperep
codex plugin add typst@aperep
codex plugin add math-writing@aperep
codex plugin add biblio@aperep
```

Record the expected groups in the consumer repository's `AGENTS.md`; Codex
installation is user-level. An academic workshop using interlinear research
normally lists `research`, `typst`, `math-writing`, and `biblio`.

## Agent Plugins clients

Point the client at each required `plugins/<name>/` directory. Root
`plugin.json` supplies portable metadata and the client discovers skills from
`skills/`. Installation and repository pinning are client-specific because the
Agent Plugins 1.0 specification does not define a marketplace.
