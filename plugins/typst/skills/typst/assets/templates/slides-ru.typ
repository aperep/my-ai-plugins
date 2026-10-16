#import "@preview/touying:0.6.1": *
#import themes.university: *
#import "@preview/cetz:0.3.2"
#import "@preview/fletcher:0.5.5" as fletcher: node, edge
#import "@preview/ctheorems:1.1.3": *
#import "@preview/numbly:0.1.0": numbly


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


#show: university-theme.with(
  aspect-ratio: "16-9",
  header-right: none,
  // config-common(handout: true),
  config-info(
    title: [Максимальные унипотентные подгруппы автоморфизмов],
    short-title: [Максимальные унипотентные подгруппы автоморфизмов],
    subtitle: [],
    author: [Александр Перепечко],
    date: "2024-11-13", //"18.10.2024"
    institution: [НИУ ВШЭ],
    logo: image("HSE_logo_2.png", width:20%),
  ),
)

#set text(size: 22pt)

#title-slide()


//#outline()

==

#slide(self => [
  #align(center + horizon)[
    #set text(size: 3em, weight: "bold", fill: self.colors.primary)

     Спасибо!

  ]
])


== Литература
