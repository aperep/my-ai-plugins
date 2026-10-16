#import "../assets/typst/common/packages.typ": article
#import "../assets/typst/common/notation.typ": *
#let lang = sys.inputs.at("lang", default: "en")
#let environment-path = if lang == "ru" {
  "../assets/typst/common/environments_ru.typ"
} else {
  "../assets/typst/common/environments.typ"
}
#import environment-path as envs

#show: article.with(
  title: [Scaffold smoke check],
  lang: lang,
  abstract: [Exercise all notation and theorem environments in both languages.],
)

= Notation

$ Aut(X) quad Inn(G) quad End(V) quad Hom(A, B) quad Isom(X, Y) $
$ Bir(X) quad SAut(X) quad Mor(X, Y) quad Aff(X) $
$ GL(V) quad PGL(V) quad SL(V) quad PSL(V) $
$ Br(X) quad Vert(X) quad Pic(X) quad AffCone(X) quad Ample(X) $
$ Div(X) quad supp(D) quad Spec(A) quad Stab(x) $
$ codim(Z) quad rank(A) quad reg(X) quad sing(X) $
$ Obj(C) quad LND(A) quad HLND(A) quad ML(A) quad FML(A) $
$ Lie(G) quad Ker(f) quad Der(A) quad Frac(A) $
$ alg(G) quad ord(f) quad ad(x) quad Jonq(n) quad LHC(X) $
$ Span(V) quad relint(C) quad Cone(X) quad Pol(X) quad Forb(X) quad Subd(X) $
$ gr(A) quad Im(f) quad id(X) quad Deg(X) quad NR(X) $
$ AA quad PP quad ZZ quad CC quad RR quad QQ quad NN quad FF quad KK quad LL $
$ GG quad Ga quad Gm quad TT $
$ cO quad cU quad cUX quad cV quad cC quad cH quad cR quad cJ $
$ gl quad #g quad #u quad #h quad #t quad #p quad #m quad jonq $
$ #T quad Eff quad #x quad compose $
$ X embed Y quad X isom Y quad x coloneq y quad bangle(x + y) $
#bangle[$x, y$]

= Environments

#envs.theorem[Theorem body.] <smoke-theorem>
#envs.lemma[Lemma body.]
#envs.proposition[Proposition body.]
#envs.statement[Statement body.]
#envs.corollary[Corollary body.]
#envs.conjecture[Conjecture body.]
#envs.conjecture-unnumbered[Unnumbered conjecture body.]
#envs.question[Question body.]
#envs.problem[Problem body.]
#envs.definition[Definition body.]
#envs.example[Example body.]
#envs.examples[Examples body.]
#envs.construction[Construction body.]
#envs.convention[Convention body.]
#envs.notation[Notation body.]
#envs.remark[Remark body.]
#envs.remarks[Remarks body.]
#envs.claim[Claim body.]
#envs.sit[Untitled statement body.]

#envs.proof[Ordinary proof: open square.]
#envs.claimproof[Claim proof: filled square.]
#envs.proof[
  The open square must return, including beside a final equation:
  $ x = x #envs.qedhere $
]
#envs.proof[
  Outer proof.

  #envs.claimproof[Inner claim proof: filled square.]

  The outer proof must still end with its open square.
]

== Subsection

#envs.lemma[The shared counter continues at 2.19.] <smoke-subsection>

= Counter reset

#envs.theorem[The counter resets to 3.1.] <smoke-reset>

References must show 2.1, 2.19, and 3.1:
@smoke-theorem, @smoke-subsection, @smoke-reset.

The following citation uses deliberately fictitious fixture data: @sample.

#bibliography("typst-smoke.bib")
