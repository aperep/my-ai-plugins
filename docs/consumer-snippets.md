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

## Claude project setup

Commit `.claude/settings.json` in a consumer repository. Enable only its groups:

```json
{
  "extraKnownMarketplaces": {
    "aperep": {
      "source": {
        "source": "github",
        "repo": "aperep/my-ai-plugins"
      }
    }
  },
  "enabledPlugins": {
    "math-writing@aperep": true,
    "research@aperep": true,
    "biblio@aperep": true,
    "typst@aperep": true
  }
}
```

Replace the enabled plugins as needed. The CLI equivalent for registration is:

```sh
claude plugin marketplace add aperep/my-ai-plugins --scope project
```

For an always-on group, install it at user scope instead:

```sh
claude plugin install meta@aperep
```
