# Project docs context baseline

With `meta` 0.2.1, starting Codex in a repository containing `docs/*.md`
produces no project-doc inventory. The only bundled `SessionStart` handler emits
auto-evolution guidance, and only inside this marketplace.

The new handler must:

- emit relative Markdown paths and allowlisted scalar frontmatter from a nested
  working directory;
- emit nothing when `docs/` is absent;
- exclude unknown frontmatter fields and symlinked files; and
- bound field length, document count, and total context.
