#set par(justify: true)

#set text(
  font: "New Computer Modern",
  size: 13pt
)
#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 1.5cm),
  numbering: "1",
)
#set par(
  justify: true,
)
#set text(lang: "ru")
#show link: set text(blue)
#show link: it => { underline(it) }

#show heading: it => [
  #set align(left)
  #set text(weight: "bold")
  #block(it.body)
]


//#import "@preview/cetz:0.2.2"
//#import "@preview/fletcher:0.5.1" as fletcher: node, edge
#import "@preview/ctheorems:1.1.3": *
#import "@preview/xarrow:0.3.0": xarrow
//#import "@preview/numbly:0.1.0": numbly


// Theorems configuration by ctheorems
#show: thmrules.with(qed-symbol: $square$)
#let theorem = thmbox("theorem", "Теорема", fill: rgb("#eeffee")).with(numbering: none)
#let corollary = thmplain(
  "corollary",
  "Следствие",
  base: "theorem",
  titlefmt: strong
).with(numbering: none)
#let definition = thmbox("definition", "Определение", inset: (x: .0em, top: .0em, bottom: -.5em)).with(numbering: none)
#let fact = thmbox("fact", "Факт", inset: (x: .0em, top: .0em)).with(numbering: none)
#let lemma = thmbox("lemma", "Лемма", inset: (x: .0em, top: .0em)).with(numbering: none)
#let example = thmplain("example", "Пример", inset: (x: .0em, top: .0em)).with(numbering: none)
#let question = thmplain("question", "Вопрос", inset: (x: .0em, top: .0em)).with(numbering: none)
#let proof = thmproof("proof", "Доказательство")


#let Aut="Aut"
#let LND="LND"
#let Der="Der"
#let Aut="Aut"

//#set heading(numbering: numbly("{1}.", default: "1.1"))

#grid(
  columns: (1fr, 1fr),
  align(left)[
    ГГГГ-ММ-ДД
  ],
  align(right)[
    Название учреждения
  ]
)

#align(center, text(17pt)[Заголовок])



//#outline()
