#import "common/packages.typ": article
#import "common/notation.typ": *
#import "common/environments.typ": *
#import "common/contacts.typ": contact

// For Russian, import environments_ru.typ instead and set lang: "ru".
#show: article.with(
  title: [Article Template],
  author: contact.name,
  affiliation: contact.affiliation,
  email: contact.email,
  lang: "en",
  abstract: [Describe the question, result, and main hypotheses.],
)

= Introduction

Introduce the problem and fix notation here.
For example, write $Aut(AA^n)$, $Lie(G)$, and $cO(X)$.

#theorem[
  The identity belongs to $Aut(X)$.
] <thm-identity>

#proof[
  The identity map is its own inverse.
]

Refer to @thm-identity with a native Typst reference.

// Add entries to references.bib, cite them with @key, then enable:
// #bibliography("references.bib")
