#import "@preview/ctheorems:1.1.3": thmplain, thmproof, thmrules, qedhere, thm-qed-symbol, thm-qed-done

// Share one counter, reset at each top-level section, as in the LaTeX scaffold.
// The article show rule installs thmrules; elsewhere, add #show: thmrules.
#let definition-style = thmplain.with(
  "theorem", base_level: 1, inset: 0pt, separator: [. ], titlefmt: strong,
)
#let plain-style = definition-style.with(bodyfmt: emph)
#let remark-style = definition-style.with(titlefmt: emph)

// Plain style
#let theorem = plain-style("Теорема")
#let lemma = plain-style("Лемма")
#let proposition = plain-style("Предложение")
#let statement = plain-style("Утверждение")
#let corollary = plain-style("Следствие")
#let conjecture = plain-style("Гипотеза")
#let conjecture-unnumbered = plain-style("Гипотеза").with(numbering: none)
#let question = plain-style("Вопрос")
#let problem = plain-style("Задача")

// Definition style
#let definition = definition-style("Определение")
#let example = definition-style("Пример")
#let examples = definition-style("Примеры")
#let construction = definition-style("Конструкция")
#let convention = definition-style("Соглашение")
#let notation = definition-style("Обозначение")

// Remark style
#let remark = remark-style("Замечание")
#let remarks = remark-style("Замечания")
#let claim = remark-style("Утверждение")
#let sit = remark-style("")

#let proof = thmproof("proof", "Доказательство", inset: 0pt, separator: [. ])

// Restore ctheorems state so a nested claim proof does not finish its outer proof.
#let claimproof(body) = context {
  let previous-qed = thm-qed-symbol.get()
  let previous-done = thm-qed-done.get()
  thm-qed-symbol.update($square.filled$)
  thmproof("claimproof", "Доказательство утверждения", inset: 0pt, separator: [. ])(body)
  thm-qed-symbol.update(previous-qed)
  thm-qed-done.update(previous-done)
}
