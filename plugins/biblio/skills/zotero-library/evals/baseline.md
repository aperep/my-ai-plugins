# Baseline failures

Recorded 2026-09-02 against `my-ai-plugins` revision `e4be520` and AGora's project-local `zotero-mcp` revision `bff9db0`.

1. Reusable Zotero safety and synchronization rules exist only inside an AGora Claude skill, so Codex and other repositories cannot discover them.
2. General Zotero behavior is mixed with AGora's collection, note schema, taxonomy, and automation details.
3. The old workflow forbids local-only bibliography notes, contrary to the current policy that an empty repository Zotero key is meaningful.
4. Citation-key rules are copied between files and can drift.
5. Host-specific tool names and orchestration requirements make the guidance brittle.

The revision passes when one host-neutral skill governs Zotero mutations and one canonical reference governs citation keys, while each repository retains its own schema and collection rules.
