#!/usr/bin/env bash
# Configure git so Claude Code can clone and auto-update this private
# marketplace from a cloud sandbox. Run once per environment.
#
#   GH_TOKEN=github_pat_... ./scripts/setup-cloud-auth.sh
#
# See docs/cloud-setup.md for what each piece is for.

set -euo pipefail

OWNER="${MARKETPLACE_OWNER:-aperep}"
REPO="${MARKETPLACE_REPO:-my-claude-marketplace}"
URL="https://github.com/${OWNER}/${REPO}"

TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"
if [[ -z "$TOKEN" ]]; then
  echo "GH_TOKEN (or GITHUB_TOKEN) is not set." >&2
  exit 1
fi

# Credential helper: covers manual /plugin install and the re-clone fallback.
if command -v gh >/dev/null 2>&1; then
  gh auth setup-git
else
  echo "note: gh not found, relying on the URL rewrite alone" >&2
fi

# URL rewrite scoped to this repository only: covers the background auto-update,
# which disables credential helpers for its git pull.
git config --global \
  "url.https://x-access-token:${TOKEN}@github.com/${OWNER}/${REPO}.insteadOf" \
  "$URL"

# Keep the last good clone if a background pull fails, instead of re-cloning.
export CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1
# owner/repo shorthand clones over SSH by default; there is no key here.
export CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1

echo "Configured. Verifying access..."
git ls-remote "$URL" >/dev/null && echo "OK: ${OWNER}/${REPO} is reachable."
