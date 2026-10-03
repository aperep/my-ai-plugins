# Interlinear sidecar contract

The package automatically loads `<jobname>.interlinear.tex`. The sidecar is
TeX-native document data, not package code.

```latex
\ic{dJ2z}{translation}[ru]{Всякое конечное поле совершенно.}
\ic{dJ2z}{explanation}{Frobenius is bijective on a finite field.}
\ic{dJ2z}{reference}[candidate]{Possible source match.}
\ic{dJ2z}{formal}[planned]{Prove finite injective implies surjective.}
```

`\ic{id}{type}[qualifier]{content}` has four fields:

| field | rule |
|---|---|
| `id` | exactly four alphanumeric characters, matching one source `\itag` |
| `type` | `translation`, `explanation`, `context`, `reference`, `formal`, or `example` |
| `qualifier` | optional language, trust state, or formal state |
| `content` | ordinary LaTeX rendered by the selected view |

Use qualifiers consistently:

- `translation`: language code such as `en` or `ru`;
- `reference`: `candidate` or `checked`;
- `formal`: `planned`, `generated`, `checked`, or `failed`.

Each ID/type pair occurs at most once. Put the Lean declaration and toolchain in
a `formal[checked]` comment; put unchecked lexical references in
`reference[candidate]`, never `reference[checked]`.
