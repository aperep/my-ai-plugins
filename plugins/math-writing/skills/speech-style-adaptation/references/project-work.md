# Project, long-file, and multi-file work

## Discover the project

Before editing, inspect the repository's instructions, build entry point,
notation or glossary files, and source ownership. If the project identifies
imported papers, archival originals, generated files, or other protected
sources, treat them as read-only unless the user explicitly places them in
scope. Propose changes elsewhere or report the conflict.

Do not assume a `tex/` tree, a particular instruction filename, fixed chapter
names, or one TeX engine.

## Long files

For a file too large for a reliable single pass:

1. map its sections and identify where voice drift is concentrated;
2. work through coherent section or proof ranges, retaining enough adjacent
   context to preserve terminology and logical flow;
3. keep edits local to prose unless the user requested restructuring;
4. validate after a cohesive range when the project has a usable build;
5. finish with a cross-file check of the introduction, terminology, references,
   and any passage split across ranges.

Choose range size from prose density and available context. Fixed line counts
are not a quality guarantee.

## Several files and delegation

Delegate only when the files or ranges are large, independent, and delegation
is available and authorized. Keep closely coupled introductions, shared
notation, and cross-file terminology under one coordinator. Give each worker a
disjoint edit scope and the same project constraints.

Avoid concurrent builds that write to the same output directory. Run one
coordinated validation after independent edits, then review the combined diff
for inconsistent voice or notation.

Report which files or sections changed, which were already in voice, which
sources remained untouched, and whether the full project compiled.
