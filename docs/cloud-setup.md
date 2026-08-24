# Claude Code on the web

A cloud sandbox needs HTTPS credentials for this private marketplace.

1. Create a fine-grained GitHub token limited to this repository with
   `Contents: Read-only`.
2. Set:

   ```text
   GH_TOKEN=<token>
   CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1
   CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1
   ```

3. Run `scripts/setup-cloud-auth.sh` from the environment startup script.

The script configures Git credentials and a URL rewrite scoped to this
repository. The token is stored in Git configuration, so keep its permissions
and lifetime minimal.
