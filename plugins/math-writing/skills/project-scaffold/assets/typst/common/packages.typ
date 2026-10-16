#import "@preview/ctheorems:1.1.3": thmrules

// Apply document settings through one show rule; imports do not set styles.
#let article(
  body,
  title: [],
  author: "",
  affiliation: [],
  email: "",
  abstract: [],
  lang: "en",
) = {
  set document(title: title, author: author)
  set page(paper: "a4", margin: 2.54cm, numbering: "1")
  set text(font: "New Computer Modern", size: 12pt, lang: lang)
  set par(justify: true)
  set heading(numbering: "1.1")
  show link: set text(fill: blue)
  show ref: set text(fill: blue)
  show: thmrules.with(qed-symbol: $square$)

  align(center)[
    #block(text(size: 16pt, weight: "bold", title))
    #block(author)
    #block(text(size: 10pt, affiliation))
    #if email != "" { block(link("mailto:" + email, email)) }
  ]
  block(inset: (x: 2em), above: 1em, below: 1.5em)[
    #strong(if lang == "ru" { [Аннотация.] } else { [Abstract.] })
    #abstract
  ]
  body
}
