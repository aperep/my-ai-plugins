#import "@preview/ctheorems:1.1.3": thmplain, thmproof, thmrules, qedhere, thm-qed-symbol, thm-qed-done

// Share one counter, reset at each top-level section, as in the LaTeX scaffold.
// The article show rule installs thmrules; elsewhere, add #show: thmrules.
#let definition-style = thmplain.with(
  "theorem", base_level: 1, inset: 0pt, separator: [. ], titlefmt: strong,
)
#let plain-style = definition-style.with(bodyfmt: emph)
#let remark-style = definition-style.with(titlefmt: emph)

// Plain style
#let theorem = plain-style("Theorem")
#let lemma = plain-style("Lemma")
#let proposition = plain-style("Proposition")
#let statement = plain-style("Statement")
#let corollary = plain-style("Corollary")
#let conjecture = plain-style("Conjecture")
#let conjecture-unnumbered = plain-style("Conjecture").with(numbering: none)
#let question = plain-style("Question")
#let problem = plain-style("Problem")

// Definition style
#let definition = definition-style("Definition")
#let example = definition-style("Example")
#let examples = definition-style("Examples")
#let construction = definition-style("Construction")
#let convention = definition-style("Convention")
#let notation = definition-style("Notation")

// Remark style
#let remark = remark-style("Remark")
#let remarks = remark-style("Remarks")
#let claim = remark-style("Claim")
#let sit = remark-style("")

#let proof = thmproof("proof", "Proof", inset: 0pt, separator: [. ])

// Restore ctheorems state so a nested claim proof does not finish its outer proof.
#let claimproof(body) = context {
  let previous-qed = thm-qed-symbol.get()
  let previous-done = thm-qed-done.get()
  thm-qed-symbol.update($square.filled$)
  thmproof("claimproof", "Proof of the claim", inset: 0pt, separator: [. ])(body)
  thm-qed-symbol.update(previous-qed)
  thm-qed-done.update(previous-done)
}
