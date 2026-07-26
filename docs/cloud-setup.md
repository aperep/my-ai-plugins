# Using this private marketplace from Claude Code on the web

A cloud sandbox has no `ssh-agent` and no `gh` login, so the two things that make
a private marketplace work locally are both absent. Three settings fix it.

## 1. Create the token

GitHub → Settings → Developer settings → **Fine-grained personal access token**.

- Repository access: **only** `aperep/my-claude-marketplace`
- Permissions: `Contents: Read-only`
- Expiration: as short as you tolerate re-issuing

Nothing else. This token should not be able to touch your paper repos.

## 2. Set the environment variables

In the cloud environment's settings, add:

| Variable | Value | Why |
|---|---|---|
| `GH_TOKEN` | the PAT | read by the `gh` credential helper |
| `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` | `1` | `owner/repo` shorthand sources clone over SSH by default; without this the clone fails in a sandbox |
| `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` | `1` | keeps the working clone when a background pull fails instead of deleting and re-cloning |

## 3. Authenticate git

Run `scripts/setup-cloud-auth.sh` once per sandbox, or paste its contents into
your environment's startup script.

The script does two things. `gh auth setup-git` configures the credential
helper, which covers manual installs and the re-clone fallback. The scoped URL
rewrite covers the *background* auto-update, which deliberately disables
credential helpers for its `git pull` and would otherwise fail every session.

## Why the rewrite is scoped to one repository

A rewrite whose base is just `https://github.com/` applies to every fetch and
push to GitHub on that machine and overrides your normal credentials, including
pushes to your own repositories. The token also lands in plaintext in the
gitconfig. Scoping it to this single repo, with a read-only token, keeps the
blast radius at "someone can read my skill prompts".

## Fallback

If the environment makes tokens awkward, vendor the one plugin you need into the
target repo's `.claude/skills/` for that session. It is a copy and it will drift,
so treat it as temporary rather than a second distribution channel.
