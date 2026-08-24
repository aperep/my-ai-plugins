# Claude project setup

Commit `.claude/settings.json` in a consumer repository. Enable only its groups:

```json
{
  "extraKnownMarketplaces": {
    "aperep": {
      "source": {
        "source": "github",
        "repo": "aperep/my-claude-marketplace"
      }
    }
  },
  "enabledPlugins": {
    "latex@aperep": true,
    "biblio@aperep": true
  }
}
```

Replace the enabled plugins as needed. The CLI equivalent for registration is:

```sh
claude plugin marketplace add aperep/my-claude-marketplace --scope project
```

For an always-on group, install it at user scope instead:

```sh
claude plugin install meta@aperep
```
