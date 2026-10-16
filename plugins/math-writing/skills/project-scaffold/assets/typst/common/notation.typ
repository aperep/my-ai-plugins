// Algebraic-geometry notation matching common/notation.tex in the LaTeX scaffold.
// Use multi-letter names directly in math: $Aut(X)$, $cO(X)$.
// One-letter bindings require #: $#g$, $#x$, $#T$; the native composition symbol
// $compose$ replaces the LaTeX macro named 0, which is not a Typst identifier.

// Named operators

// Morphisms and transformation groups
#let Aut = math.op("Aut")
#let Inn = math.op("Inn")
#let End = math.op("End")
#let Hom = math.op("Hom")
#let Isom = math.op("Isom")
#let Bir = math.op("Bir")
#let SAut = math.op("SAut")
#let Mor = math.op("Mor")
#let Aff = math.op("Aff")
#let GL = math.op("GL")
#let PGL = math.op("PGL")
#let SL = math.op("SL")
#let PSL = math.op("PSL")

// Algebraic geometry
#let Br = math.op("Br")
#let Vert = math.op("Vert")
#let Pic = math.op("Pic")
#let AffCone = math.op("AffCone")
#let Ample = math.op("Ample")
#let Div = math.op("Div")
#let supp = math.op("supp")
#let Spec = math.op("Spec")
#let Stab = math.op("Stab")
#let codim = math.op("codim")
#let rank = math.op("rank")
#let reg = math.op("reg")
#let sing = math.op("sing")

// Algebra, Lie theory, and invariants
#let Obj = math.op("Obj")
#let LND = math.op("LND")
#let HLND = math.op("HLND")
#let ML = math.op("ML")
#let FML = math.op("FML")
#let Lie = math.op("Lie")
#let Ker = math.op("Ker")
#let Der = math.op("Der")
#let Frac = math.op("Frac")
#let alg = math.op("alg")
#let ord = math.op("ord")
#let ad = math.op("ad")
#let Jonq = math.op("Jonq")
#let LHC = math.op("LHC")

// Convex geometry and combinatorics
#let Span = math.op("Span")
#let relint = math.op("relint")
#let Cone = math.op("Cone")
#let Pol = math.op("Pol")
#let Forb = math.op("Forb")
#let Subd = math.op("Subd")

// General operators
#let gr = math.op("gr")
#let Im = math.op("Im")
#let id = math.id
#let Deg = math.op("Deg")
#let NR = math.op("NR")

// Blackboard bold symbols

// Spaces
#let AA = sym.AA
#let PP = sym.PP

// Number systems and fields
#let ZZ = sym.ZZ
#let CC = sym.CC
#let RR = sym.RR
#let QQ = sym.QQ
#let NN = sym.NN
#let FF = sym.FF
#let KK = sym.KK
#let LL = sym.LL

// Algebraic groups
#let GG = sym.GG
#let Ga = $GG_upright(a)$
#let Gm = $GG_upright(m)$
#let TT = sym.TT

// Calligraphic symbols

// Sheaves and families
#let cO = $cal(O)$
#let cU = $cal(U)$
#let cUX = $cU(X)$

// General calligraphic symbols
#let cV = $cal(V)$
#let cC = $cal(C)$
#let cH = $cal(H)$
#let cR = $cal(R)$
#let cJ = $cal(J)$

// Fraktur symbols

// Lie algebras
#let gl = $frak(g l)$
#let g = $frak(g)$
#let u = $frak(u)$
#let h = $frak(h)$
#let t = $frak(t)$
#let p = $frak(p)$
#let m = $frak(m)$

// Other fraktur symbols
#let jonq = $frak(j o n q)$

// Roman and decorated symbols
#let T = $upright(T)$
#let Eff = $overline(op("NE"))$
#let x = $overline(x)$
#let compose = sym.compose

// Arrows and delimiters
#let embed = sym.arrow.r.hook
#let isom = $limits(stretch(->))^tilde.eq$
#let coloneq = sym.colon.eq
#let bangle = body => $lr(chevron.l #body chevron.r)$
