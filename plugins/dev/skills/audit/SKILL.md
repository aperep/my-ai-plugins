---
name: audit
description: "Audit a whole repository only for over-engineering: rank what to delete, simplify, or replace with stdlib or native features. Use for explicit requests to audit for over-engineering, find bloat, or identify what can be deleted across a codebase. Do not use for correctness, security, performance, or diff-only review."
---

Apply the complexity lens from `review` repo-wide. Scan the whole tree and rank
findings biggest cut first.

## Tags

Use the same tags as the complexity review lens:

- `delete:` dead code, unused flexibility, speculative feature. Replacement: nothing.
- `stdlib:` hand-rolled thing the standard library ships. Name the function.
- `native:` dependency or code doing what the platform already does. Name the feature.
- `yagni:` abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` same logic, fewer lines. Show the shorter form.

## Hunt

Deps the stdlib or platform already ships, single-implementation interfaces,
factories with one product, wrappers that only delegate, files exporting one
thing, dead flags and config, hand-rolled stdlib.

## Output

One line per finding, ranked: `<tag> <what to cut>. <replacement>. [path]`.
End with `net: -<N> lines, -<M> deps possible.` Nothing to cut: `Lean already. Ship.`

## Boundaries

Scope: over-engineering and complexity only. Correctness bugs, security holes,
and performance are explicitly out of scope. Route them to a normal review
pass. List findings, apply nothing, and stop after the report.
