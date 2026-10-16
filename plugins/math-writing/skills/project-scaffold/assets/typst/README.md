# Typst article starter

Copy this directory into your project, fill `common/contacts.typ`, and edit
the title and abstract in `main.typ`.
Run from the copied directory:

```sh
mkdir -p output
typst compile main.typ output/main.pdf
```

The layout uses A4 paper, 12 pt New Computer Modern, numbered sections,
and the same one-inch margins as the LaTeX starter's `fullpage` setup.
`common/packages.typ` defines the `article` show rule; importing it alone
does not change the document's styles.
The sole package dependency is pinned to `@preview/ctheorems:1.1.3`, also
used by the bundled note and slides; the first build downloads it.

For Russian, import `common/environments_ru.typ` in place of
`common/environments.typ`, set `lang: "ru"`, and translate the document text.
Both theorem families share one counter across all numbered environments,
reset at each top-level section.
They preserve the LaTeX plain, definition, and remark styles.
Use `#theorem[Statement.] <thm-name>`, `@thm-name`, and `#proof[Proof.]`.
`conjecture-unnumbered` replaces the starred conjecture; `claimproof` ends
with a filled square.
Inside a proof, `#qedhere` puts the QED symbol beside a final display equation.

Every macro in the LaTeX starter's `common/notation.tex` has an equivalent
in `common/notation.typ`.
Operators use `math.op`, with proper operator spacing.
Keep native Typst notation for fractions, scripts, lists, and references.
See the official [template guide](https://typst.app/docs/tutorial/making-a-template/)
and [math operator reference](https://typst.app/docs/reference/math/op/).

| LaTeX | Typst after importing `common/notation.typ` |
|---|---|
| `\Aut(X)`, `\Lie(G)`, `\Spec A` | `$Aut(X)$`, `$Lie(G)$`, `$Spec A$` |
| `\AA^n`, `\Ga`, `\cO(X)`, `\gl` | `$AA^n$`, `$Ga$`, `$cO(X)$`, `$gl$` |
| `\g`, `\u`, `\h`, `\t`, `\p`, `\m`, `\T`, `\x` | `$#g$`, `$#u$`, `$#h$`, `$#t$`, `$#p$`, `$#m$`, `$#T$`, `$#x$` |
| `\0` | `$compose$` (Typst identifiers cannot start with a digit) |
| `X \embed Y`, `X \isom Y`, `x \coloneq y` | `$X embed Y$`, `$X isom Y$`, `$x coloneq y$` |
| `\bangle{x + y}` | `$bangle(x + y)$` |

Single letters in Typst math are literal symbols; `#` selects an imported
one-letter binding.
Pass one expression to `bangle`; for comma-separated content, use
`#bangle[$x, y$]`.

Add your entries to `references.bib`, cite them with `@key`, and enable
the commented `#bibliography` call in `main.typ`.
Use native citations rather than a hand-written bibliography.
