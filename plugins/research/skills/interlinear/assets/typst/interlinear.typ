// Interlinear sentence labels backed by CSV metadata.

// Copy this file beside the consumer document and metadata, or pass a CSV path
// relative to this module with --input data=.... Choose a view with
// --input mode=plain|draft|badges|focus|translation|comment|parallel|
// inline-example|example-only|gap-check|review.

#let mode = sys.inputs.at("mode", default: "badges")
#let data-path = sys.inputs.at("data", default: "sentences.csv")
#let focus-labels = sys.inputs.at("focus", default: "").split(";").map(it => it.trim())

// --- загрузка данных -------------------------------------------------------
// row-type: dictionary использует первую строку CSV как имена колонок.
#let _rows = csv(data-path, row-type: dictionary)
#let _data = (:)
#for r in _rows { _data.insert(r.label, r) }

#let _has(label) = _data.at(label, default: none) != none

#let _field(label, name) = {
  let row = _data.at(label, default: none)
  if row == none { return none }
  let v = row.at(name, default: "")
  if v == "" { none } else { v }
}

#let _first-field(label, names) = {
  for name in names {
    let value = _field(label, name)
    if value != none { return value }
  }
  none
}

#let _translation(label) = _first-field(label, ("translation", "translation_en", "translation_ru"))
#let _explanation(label) = _first-field(label, ("explanation", "ai_comment"))
#let _lean(label) = {
  let status = _field(label, "lean_status")
  let reference = _field(label, "lean_ref")
  let note = _field(label, "lean_note")
  (status, reference, note).filter(it => it != none).join("; ")
}

#let _is-proof-step(label) = {
  let t = _field(label, "tags")
  if t == none { return false }
  let tags = t.split(";").map(tag => tag.trim())
  tags.contains("proof") or tags.contains("claim")
}

// --- оформление ------------------------------------------------------------
#let _label-tag(label) = text(size: 0.72em, fill: rgb("#3366cc"))[#raw(label)]
#let _badge(label) = super(text(size: 0.68em, fill: rgb("#315c9b"))[ann])

#let _missing(label) = text(fill: rgb("#cc0000"), weight: "bold")[⟨нет данных в CSV: #label⟩]

// подстрочная строка: маленький отступ, серый, с коротким префиксом-меткой
#let _under(prefix, body) = block(
  inset: (left: 1.4em, top: 0.15em, bottom: 0.35em),
  text(size: 0.85em, fill: rgb("#555555"))[#text(weight: "bold")[#prefix] #body],
)

// баннер с объектом примера (выводится один раз в начале блока доказательства)
#let _subject-banner(subj) = block(
  width: 100%, inset: 0.5em, radius: 3pt, fill: rgb("#eef3ff"),
  above: 0.6em, below: 0.4em,
  text(size: 0.85em)[#text(weight: "bold")[Пример:] #subj],
)

#let _annotation-rows(label) = {
  let tr = _translation(label)
  let explanation = _explanation(label)
  let lean = _lean(label)
  let confirmed = _field(label, "stacks_ref")
  let candidate = _field(label, "stacks_candidate")
  if tr != none { _under("Translation:", emph(tr)) }
  if explanation != none { _under("Explanation:", explanation) }
  if lean != "" { _under("Lean:", lean) }
  if confirmed != none {
    _under("Stacks:", link("https://stacks.math.columbia.edu/tag/" + confirmed)[Tag #confirmed (checked)])
  }
  if candidate != none {
    _under("Candidate:", [Stacks Tag #candidate — not checked])
  }
}

// --- основной макрос -------------------------------------------------------
#let sent(label, body) = {
  let subj = _field(label, "example_subject")
  let ex = _field(label, "example_step")

  // потоковые режимы: предложения сливаются в обычный абзац
  if mode == "plain" {
    body
  } else if mode == "draft" {
    [#body#h(0.15em)#super(_label-tag(label))]
  } else if mode == "badges" {
    [#body#h(0.15em)#_badge(label)]
  } else if mode == "focus" {
    block(breakable: true, width: 100%, {
      [#body#h(0.15em)#_badge(label)]
      if focus-labels.contains(label) { _annotation-rows(label) }
    })

  // --- фаза 3: только прогон на примере -----------------------------------
  } else if mode == "example-only" {
    if subj != none { _subject-banner(subj) }
    if ex != none {
      block(breakable: true, width: 100%, {
        grid(columns: (3.2em, 1fr), gutter: 0.4em,
          align(top + right, _label-tag(label)), ex)
      })
    }

  // --- фаза 3: две колонки «общее | на примере» ---------------------------
  } else if mode == "parallel" {
    if subj != none { _subject-banner(subj) }
    block(breakable: true, width: 100%, inset: (y: 0.15em), {
      grid(
        columns: (2.4em, 1fr, 1fr),
        gutter: 0.6em,
        align(top + right, _label-tag(label)),
        body,
        if ex != none {
          text(fill: rgb("#444444"))[#ex]
        } else if _is-proof-step(label) {
          text(fill: rgb("#bbbbbb"), style: "italic")[— нет примера —]
        } else [],
      )
      line(length: 100%, stroke: 0.3pt + rgb("#dddddd"))
    })

  // --- фаза 3: предложение + прогон на примере строкой ниже ----------------
  } else if mode == "inline-example" {
    block(breakable: true, width: 100%, {
      if subj != none { _subject-banner(subj) }
      grid(columns: (3.2em, 1fr), gutter: 0.4em,
        align(top + right, _label-tag(label)), body)
      if ex != none { _under("на примере:", ex) }
    })

  // --- фаза 3: подсветка непрогнанных шагов доказательства ----------------
  } else if mode == "gap-check" {
    let gap = _is-proof-step(label) and ex == none
    block(breakable: true, width: 100%, inset: 0.3em, radius: 2pt,
      fill: if gap { rgb("#fff3f0") } else { none }, {
        grid(columns: (3.2em, 1fr), gutter: 0.4em,
          align(top + right, _label-tag(label)), body)
        if gap {
          _under("⚠", text(fill: rgb("#cc3300"))[шаг доказательства не прогнан на примере])
        } else if ex != none {
          _under("ex:", text(fill: rgb("#2e7d32"))[#ex])
        }
      })

  // --- фазы 0–1 и сводный review ------------------------------------------
  } else {
    block(breakable: true, width: 100%, {
      if (mode == "review") and subj != none { _subject-banner(subj) }
      grid(
        columns: (3.2em, 1fr),
        gutter: 0.4em,
        align(top + right, _label-tag(label)),
        body,
      )
      if not _has(label) { _under("", _missing(label)) }
      if mode == "translation" or mode == "review" {
        let tr = _translation(label)
        if tr != none { _under("EN:", emph(tr)) }
      }
      if mode == "comment" or mode == "review" {
        let c = _explanation(label)
        if c != none { _under("ИИ:", c) }
      }
      if mode == "review" {
        if ex != none { _under("Пример:", ex) }
        let s = _field(label, "stacks_ref")
        if s != none {
          _under("Stacks:", link("https://stacks.math.columbia.edu/tag/" + s)[Tag #s (checked)])
        }
        let candidate = _field(label, "stacks_candidate")
        if candidate != none {
          _under("Candidate:", [Stacks Tag #candidate — not checked])
        }
        let lean = _lean(label)
        if lean != "" { _under("Lean:", lean) }
      }
    })
  }
}
