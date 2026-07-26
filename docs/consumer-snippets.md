# Wiring a target repository

Commit one of these as `.claude/settings.json` in the target repo. Nothing else
gets copied into the repo — no submodule, no injection script, no
`.claude/skills/` copy.

The key under `extraKnownMarketplaces` is the marketplace *name* (`aperep`); the
`repo` is where it lives (`aperep/my-claude-marketplace`).

Equivalent to hand-editing, if you prefer the CLI:

    claude plugin marketplace add aperep/my-claude-marketplace --scope project

## A LaTeX paper repository

```json
{
  "extraKnownMarketplaces": {
    "aperep": {
      "source": { "source": "github", "repo": "aperep/my-claude-marketplace" }
    }
  },
  "enabledPlugins": {
    "latex@aperep": true,
    "biblio@aperep": true
  }
}
```

## An Obsidian vault

```json
{
  "extraKnownMarketplaces": {
    "aperep": {
      "source": { "source": "github", "repo": "aperep/my-claude-marketplace" }
    }
  },
  "enabledPlugins": {
    "obsidian@aperep": true
  }
}
```

Swap `obsidian` for `typst` in a Typst document repo; enable several at once when
a repo needs them.

## Always-on instead

For a set you want everywhere, install at user scope once and leave it out of
project settings entirely:

    claude plugin install meta@aperep

## Notes

- The marketplace registration itself is stored once per user in
  `~/.claude/plugins/known_marketplaces.json`, not per project. The block above
  makes Claude Code offer to add it when you trust a new checkout.
- Skills from a plugin are namespaced: `/latex:latex-math-proofreader`.
  Automatic invocation by `description` still works as before.
- Under a git worktree, a local-path marketplace source resolves against the
  main checkout, so all worktrees share one marketplace location.
