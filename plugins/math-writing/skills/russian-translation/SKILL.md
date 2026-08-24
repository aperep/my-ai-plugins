---
name: russian-translation
author: A. Perepechko
description: Translate or rewrite mathematical prose into Russian in A. Perepechko's authorial voice, calibrated from `P18_ru.tex` (single-author Russian, bundled). Use whenever producing or revising Russian mathematical text (`main_ru.tex`, `*_ru.tex`, `intro_ru.tex`, `resume_ru.tex`, `*_intro_ru.tex`, abstracts, cover letters), translating English chapters into Russian, or polishing co-authored Russian sources to match the single-author voice. Trigger phrases: "переведи на русский", "по-русски", "in Russian", "translate to Russian", "Russian version", "in my style (Russian)", "rewrite in Russian style", "match my Russian voice".
---

# Russian Translation — A. Perepechko (calibrated on `P18_ru.tex`)

The reference corpus for this skill is **`P18_ru.tex`** (bundled in this skill directory) — the single-author Russian text *Автоморфизмы поверхностей марковского типа*. It is the cleanest available sample of the author's solo Russian voice. Co-authored Russian sources must not be used for calibration.

Use this skill when generating, translating, or revising any Russian mathematical prose. Apply as a soft overlay: project-level conventions always take priority.

## Voice in one paragraph

First-person plural, declarative, restrained. Sentences are short to medium and almost always start the new idea with a connective ("Тогда", "В частности", "Заметим, что", "Значит", "По теореме~\ref{...}", "Из этого следует, что", "С другой стороны") rather than with the subject. The author signposts what is being done ("В этом разделе мы…", "Мы вводим…", "Будем работать с…") and announces results before stating them. Definitions are introduced with `\emph{...}` on the term being defined, followed by a short, self-contained clause; the defined term is in the nominative even when the surrounding sentence would call for an oblique case ("\emph{Граничным дивизором} мы называем …"). Proofs read as a chain of small justified steps and end with a one-clause closer such as "Противоречие.", "Утверждение доказано." or "что и требовалось доказать." (the latter only when not using `\qed`).

## Calibrated patterns

### 1. Pronoun and stance

- Default to **"мы"** for both rhetorical ("мы вводим", "мы описываем", "мы устанавливаем") and inclusive ("имеем", "можем считать", "будем предполагать") uses. Do **not** use "я"; do **not** use the passive to avoid an agent when "мы" works ("в работе вводится" → "мы вводим").
- Use **"автор"** only in acknowledgments and funding notes ("Автор благодарен…", "Автор выражает благодарность…").
- Setup imperatives: **"Пусть …", "Рассмотрим …", "Введём …", "Будем называть …", "Заметим, что …", "Напомним, что …", "Предположим, что …"**. These are the dominant sentence-openers in proofs and definitions, mirroring the English "Let / Consider / Assume / Recall".
- Prefer **"положим …"** over "обозначим … равным …" when defining a symbol by an equality.
- The first-person singular ("я", "по моему мнению") never appears in the body. The dissertation introduction has one place for it — the section "Личный вклад автора" — and even there the author refers to himself in the third person.

### 2. Sentence rhythm

- Short declarative sentences are the default. Two clauses joined by a connective are common; three-clause sentences are rare.
- Lead with the connective or the assumption, not the conclusion: "По теореме~\ref{th:circular} и предложению~\ref{pr:s3}, группа $\Aut(M_c)$ порождается $S_3\ltimes K$ и $\sigma$." — not "Группа $\Aut(M_c)$ порождается $S_3\ltimes K$ и $\sigma$ по теореме~\ref{th:circular} и предложению~\ref{pr:s3}."
- Punctuation: the author uses the spaced triple-hyphen `---` as the standard Russian em-dash (тире) — it is mandatory between subject and predicate when the predicate is a noun ("Пусть $\K$ --- алгебраически замкнутое поле …"), in apposition, and in parenthetical asides. Do **not** use `—` (Unicode em-dash) or single ` -- ` (en-dash) between clauses; let `babel` and `\frenchspacing`-friendly typography render `---` correctly.
- Use a non-breaking space `~` before every internal `\ref`, `\eqref`, `\cite[...]{...}` locator, and before single-character function names: `теорема~\ref{th:aut}`, `\cite[Proposition~2.1]{BCC+}`, `группа~$G$`, `см.~\cite{...}`. In numerical ranges, use `\,` between digit groups and the unit, and `--` (en-dash) between numbers in citations and ranges: "1879--1880 годах".
- Avoid throat-clearing: "Стоит отметить, что…", "Важно подчеркнуть, что…", "Хотелось бы заметить, что…". Replace with "Заметим, что…", "Отметим, что…", "Напомним, что…", or simply state the fact.
- Avoid hedges: "по-видимому", "вероятно", "кажется, что". The voice is assertive within the scope of what has been proved.
- Numerals: write small numbers as words in prose ("из четырёх вершин", "две точки"); use digits for indexed objects ($n$, $k$, $4$ in formulas) and inside symbol-heavy clauses.

### 3. Signature transitions

Use these connectives at the start of sentences. They are the load-bearing rhythm of the Russian text. The right-hand "Avoid" column collects bookish or AI-typical alternatives that drift away from the author's voice.

| Function | Preferred forms | Avoid |
|---|---|---|
| Consequence | **Тогда**, **Значит**, **Следовательно**, **Поэтому**, **Отсюда следует, что**, **Из этого следует, что**, **В частности** | Таким образом (use sparingly), Стало быть, Итак (only at section closers) |
| Justification | **По теореме~\ref{...}**, **По~\cite[...]{...}**, **Действительно**, **По построению**, **По предположению**, **В силу~\cite{...}** | Согласно (use only with people/sources, not theorems), Исходя из, Опираясь на |
| Addition | **Кроме того**, **Также мы …**, **Более того**, **При этом** | Помимо вышесказанного, Дополнительно, Сверх того |
| Contrast | **С другой стороны**, **Однако** (rarely), **Напротив**, **В то же время** | Тем не менее (heavy), Вместе с тем (formal-bureaucratic) |
| Recap | **Напомним, что**, **Как было показано выше**, **Как и выше** | Возвращаясь к…, Вспомним, что… |
| Reformulation | **А именно**, **То есть**, **Иначе говоря**, **Эквивалентно** | Другими словами (only once per chapter), Иными словами |
| Forward ref. | **Следующая теорема/лемма/предложение/замечание…**, **Нам понадобится следующая лемма** | В дальнейшем мы докажем, что …, Ниже будет показано, что … |
| Set-up | **Пусть …**, **Рассмотрим …**, **Зафиксируем …**, **Положим …**, **Обозначим через … (объект)**, **Будем называть … \emph{X}** | Возьмём произвольный …, Предположим теперь, что … |
| Assumption flag | **Без ограничения общности можем считать, что**, **С точностью до~…** | в.о.о., с.т.р. (never use Russian abbreviations of WLOG) |
| Closer | **Противоречие.**, **Утверждение доказано.**, **что и требовалось доказать**, **Имеем (i).** | ч.т.д. (never), QED (never), `\qed` is fine when the environment provides it |

### 4. Result and proof scaffolding

- **Sectioning**: `\section{...}` followed by a one- or two-sentence preview ("В этом разделе мы…", "Здесь мы…", "Раздел~N содержит описание…"). Subsections also begin with a single orienting sentence.
- **Theorems** are introduced and (in the introduction) re-stated with `[{Теорема~\ref{th:...}}]` so the reader sees both the local label and the publishable statement, paralleling the English convention.
- **Definitions** put the defined term in `\emph{...}`. The defined term is given in the case the syntax demands when it is the grammatical subject of the introducing clause; when it is enumerated inside a definition, prefer the nominative: *"\emph{Внутренним раздутием} в ребре $e$ называется преобразование …"*, *"… называется \emph{стандартным}, если выполнено одно из условий: …"*. Do **not** use bold or quotation marks for the defined term.
- **"для краткости"** is the standard abbreviation flag, paralleling English "for short": *"локально нильпотентные дифференцирования (для краткости — ЛНД)"*, *"де Жонкьеро-подобные (для краткости — дЖ-подобные)"*.
- **Forward references**: announce ahead of time — "Следующая теорема даёт положительный ответ на этот вопрос.", "Для доказательства нам понадобится следующая лемма.", "Для формулировки нам потребуется следующее определение."
- **Proof openers**: the first sentence usually invokes the hypothesis or a prior result.
  - "По лемме~\ref{lm:...}, имеем …"
  - "Зафиксируем фильтрацию $G=\bigcup G_i$ как в теореме~\ref{th:...}."
  - "Предположим (i)."
  - "Предположим противное: пусть …"
- **Proof internals** are a chain of small justified steps. `itemize` lists are used freely inside proofs to enumerate inclusions or numbered conditions; each bullet ends in a justification ("…, поскольку $L$ --- подпространство;", "… по следствию~\ref{cr:...};").
- **Proof closers**: prefer one of
  - "Противоречие." (after "Предположим противное …")
  - "Утверждение доказано."
  - "Имеем (i)." / "Имеем (ii)."
  - "что и требовалось доказать"
  - leave `\qedhere` from the source if it is mid-sentence (preserve from English source when porting).
- **Multiple-equivalent results** use `\begin{enumerate}[(i)]` with parenthesized lowercase Roman numerals (or, in tradition-heavy chapters, Cyrillic letters `(а)`, `(б)`, `(в)` — but only if the source uses them; default is Roman). The proof walks the cycle "Предположим (i)…", "Предположим (ii)…", "Предположим (iii)…" rather than proving (i)⇔(ii) separately.
- **Equivalence shorthand**: "(ii)~$\Rightarrow$~(iii)" with non-breaking spaces is the author's habit when explicitly tagging implications.

### 5. Vocabulary preferences

Prefer the left column over the right. Where two right-hand variants are tagged "(ru-bureaucratic)" or "(ai-typical)", they are the most frequent drift symptoms.

| Use | Avoid |
|---|---|
| снабжённый (структурой) | оснащённый, наделённый |
| естественный (изоморфизм / обобщение) | канонический, внутренне присущий |
| аналогичный / аналог | похожий, схожий |
| в частности | в особенности (ai-typical), в том числе (when the predicate is the point) |
| неформально, … | грубо говоря, на пальцах |
| см., например,~\cite{...} | ср.~\cite{...} only sparingly; "там же" only for repeats within the same paragraph |
| Достаточно показать, что | Остаётся показать, что (only when literally remaining) |
| можем считать, что | без ограничения общности (write out — never WLOG / в.о.о.) |
| Хорошо известно, что | Классически (ru-bureaucratic), Общеизвестно, что (ai-typical) |
| обозначим через | назовём (when introducing a symbol — "обозначим" is for symbols, "назовём" for terms) |
| называется \emph{X} | будем именовать \emph{X} (ru-bureaucratic) |
| состоит из | представляет собой множество (ai-typical) |
| сохраняет (при действии группы) | оставляет инвариантным (ok in moderation), удерживает |
| Автор благодарен … за многочисленные обсуждения, замечания и предложения | Я хотел бы поблагодарить … |
| В разделе~\ref{sec:...} мы … | Раздел X посвящён обсуждению … (passive-style, ok occasionally) |
| данная диссертация / данная глава / данный раздел / данная работа | настоящая диссертация / настоящая глава / настоящий раздел (verified author preference: author uses "данном/данной", not "настоящем/настоящей") |
| вводим понятие | определяем понятие (use "определяем" only when literally giving a `\begin{definition}`) |

Lexical tics worth preserving (each at most once per chapter, for emphasis):

- **"наиболее примечательное свойство"** (matches English "remarkable property" / "key ingredient")
- **"ключевую роль"**, **"центральную роль"**, **"в основе лежит"**
- **"кратко опишем конструкцию"** as a meta-line before unpacking a proof idea in the introduction
- Parenthetical re-statement: **"(или, для краткости, X)"** and trailing **"(предложение~\ref{pr:...})"** to point at the formal statement
- **"Несложно проверить, что"** for short verifications that do not deserve a separate lemma
- **"Нетрудно видеть, что"** is acceptable but heavier; prefer "Несложно проверить" or "Заметим, что"

### 6. Mathematical typesetting conventions

These follow `tex/notation.tex` and override anything else in source articles. Most are language-neutral.

- Field of scalars: `$\K$` (algebraically closed, characteristic zero, sometimes uncountable). Canonical opener: *"Пусть $\K$ --- алгебраически замкнутое поле характеристики 0, и $X$ --- неприводимое аффинное алгебраическое многообразие над $\K$."* Note the spaced `---`, the comma, and the absence of "т.\,е." in this opener.
- Operators: `\Aut`, `\Bir`, `\End`, `\Der`, `\LND`, `\Lie`, `\Spec`, `\ker`, `\Frac`, `\ord`, `\Jonq`, `\jonq`. Always rendered via `\operatorname` from `notation.tex` — never raw text or `\mathrm`.
- Algebra of regular functions: `\cO(X)`. Field of fractions: `\K(X)`. Localization: `\cO(X)_h`, `R_h`. Subscript invariants: `\cO(X)^U`, `\K(X)^U`.
- Group `\G_a := (\K, +)`. Use `\G_a` consistently, not `\mathbb{G}_a` directly.
- Affine space: `\AA^n`. `\ZZ`, `\QQ`, `\RR`, `\CC`, `\NN`, `\PP` from `tex/notation.tex`.
- Embedding: `\embed` (`\hookrightarrow`).
- Definitions: emphasized term inline with `\emph{...}`; the symbol introduced by `:=` in display math when nontrivial: *"$L_\FF := \FF \otimes_A L$"*. In Russian, when the assignment is given inline, prefer the asymmetric Russian convention *"положим $L_\FF = \FF \otimes_A L$"* once the definitional intent is clear from context.
- Citations: `\cite[Теорема~5.1.1]{FK}` with non-breaking tilde before the locator. Translate locator words inside citations: `Theorem` → `Теорема`, `Lemma` → `Лемма`, `Proposition` → `Предложение`, `Corollary` → `Следствие`, `Section` → `п.` or `раздел`, `Definition` → `Определение`, `Example` → `Пример`, `Remark` → `Замечание`, `Chapter` → `глава`. **Exception:** if the cited work is in English and the user wants to preserve the original locator (as in `P18_ru.tex`, e.g. `\cite[Definition 2.13]{FKZ}`), keep the English locator. The choice is per-chapter; default to the English locator when the cited source is in English, and to the Russian locator when the source is in Russian.
- Internal cross-references: non-breaking tilde before every `\ref`: `лемме~\ref{lm:...}`, `разделу~\ref{sec:...}`, `теореме~\ref{th:KZ-intro}`, `\eqref{eq:LF}`. The case of the noun follows ordinary Russian agreement: `по теореме~\ref{...}`, `в лемме~\ref{...}`, `из предложения~\ref{...}`.
- Numbered statements share a counter (`\newtheorem{lemma}[theorem]{Лемма}`, etc., per `tex/environments_ru.tex`). Cross-references use the joint numbering. Preserve when adapting.

### 7. Acknowledgments and metadata

- Funding line, italic-free, in `\thanks` on the author macro: *"Исследование поддержано грантом РНФ-DST 22-41-02019."* Update only if the user provides a new grant. Keep the English funding line in `main_en.tex` and the Russian one here in parallel.
- Acknowledgments are a single paragraph at the end of the introduction. Order: (1) collaborators (full given name + patronymic + last name on first mention), (2) mentor figure(s) on a separate sentence, (3) referees on a final sentence. Template, calibrated on `P18_ru.tex`:
  > {\em Благодарность.} Автор благодарен *Имя1 Отчество1 Фамилия1, Имя2 Отчество2 Фамилия2, … и Имя_N Отчество_N Фамилия_N* за многочисленные обсуждения, замечания и предложения. Автор особенно благодарен *Имя Отчество Фамилия* за погружение в тематику и за постоянное внимание к работе. Наконец, автор благодарен рецензентам за внимательное чтение и замечания, обогатившие работу.
- Address block: НИУ ВШЭ, факультет компьютерных наук, Покровский б-р, 11, Москва, 109028, Россия. Электронная почта `a@perep.ru`.

### 8. Introduction architecture

The introduction of `P18_ru.tex` gives the section-level voice. When drafting or rewriting `intro_ru.tex` or a chapter introduction `*_intro_ru.tex`, follow this order:

1. **Section "Описание области исследований"** (dissertation-level only). Open with a one-sentence orienting fact and standing convention: *"В данной диссертации мы работаем над алгебраически замкнутым полем $\K$ характеристики~$0$."*
2. **Степень разработанности темы** — one paragraph naming the gap.
3. **Цели и задачи** — bulleted aims.
4. **Методология и методы исследования.**
5. **Теоретическая и практическая значимость.**
6. **Основные результаты, выносимые на защиту** — main theorems re-stated with `[{Теорема~\ref{th:...}}]` re-labels.
7. **Положения, выносимые на защиту.**
8. **Личный вклад автора** — for each co-authored chapter, one sentence specifying the author's contribution. The author refers to himself in the third person here as well ("Автор внёс …").
9. **Связанные результаты, не вошедшие в диссертацию.**
10. **Достоверность результатов / Апробация работы.**
11. **Структура диссертации** — one paragraph per chapter, each one sentence: *"В разделе~\ref{sec:...} мы…"* / *"Глава~N посвящена…"*.
12. **Благодарности** as in §7.

For chapter introductions (`*_intro_ru.tex`), drop items 1–5 and items 9–11; keep only a local motivation paragraph + a brief construction sketch + the chapter's main results. This matches `tex/CLAUDE.md`'s directive that per-chapter intros carry only local motivation.

### 9. Co-authored chapters

When translating a co-authored chapter (`PR24_ru.tex`, `PR23_ru.tex`, `KPZ17_ru.tex`, `MPS18_ru.tex`, `APS14_ru.tex`, `PZ26_ru.tex`) to single-author Russian voice for the thesis:

- Convert English "we" of the original co-authors to Russian "мы" of authorial plural — usually a direct translation suffices.
- In the local intro, add one sentence specifying the author's contribution: *"Вклад автора в эту главу состоит в…"*. Do **not** move this sentence into the body.
- Do **not** rewrite proofs unless the math has changed; only adjust connectives and signposting to the patterns in §3.
- Preserve original notation if it differs from `tex/notation.tex` only when changing it would force editing source files in subdirectories; otherwise harmonize via `\input{notation.tex}`.

## Anti-patterns to flag

When reviewing or rewriting Russian prose, replace these:

- **AI-typical hedges**: "Важно отметить, что", "Стоит подчеркнуть, что", "Следует обратить внимание на", "Углубимся в…", "Мы можем использовать всю мощь…", "комплексный (в смысле «всеобъемлющий»)", "робастный", "бесшовный". None appear in the calibration corpus and most are calques from English drift.
- **Wrong dash**: `—` (Unicode em-dash) or single `-` between clauses. Use spaced `---` for тире and `--` for numerical ranges only.
- **Long subject-first sentences** ("Понятие вложенной унипотентной подгруппы группы автоморфизмов аффинного многообразия исследовалось во многих работах…"). Recast with a leading connective: "Вложенные унипотентные подгруппы группы $\Aut(X)$ изучались многими авторами; см.~\cite{...}."
- **Bullet lists outside proofs and definitions.** Reserve `itemize` for enumerated equivalences, listed conditions in lemmas, and listed inclusions in proofs.
- **"В заключение", "Подводя итог", "Резюмируя"** as paragraph openers. Sections end with the last theorem or with a one-sentence forward pointer.
- **Bold for emphasis in math prose.** Emphasis is `\emph{...}` only; bold is reserved for volume numbers in the bibliography.
- **Russian bureaucratic abbreviations** "т.е.", "т.к.", "и т.д.", "и т.п.", "т.н.", "в.о.о.", "ч.т.д." in running prose. Spell out: "то есть", "так как", "и так далее", "и тому подобное", "так называемый", "без ограничения общности", "что и требовалось доказать". Inside formulas and tight enumerations, "т.\,е." is acceptable but should not lead a sentence.
- **Calques from English** that the author does not use: "это есть", "имеет место быть", "является сильным/мощным инструментом", "в данной статье/работе мы хотели бы".
- **English locator words mixed with Russian text** when the cited source is in Russian (e.g. `\cite[Theorem 1]{rTim}` for a Russian-language Timashev book). Translate to `\cite[Теорема~1]{rTim}`.
- **"Я"** anywhere in the body. The dissertation introduction has one designated section ("Личный вклад автора") and even there the author uses the third person.
- **Trailing "ч.т.д." or "QED"**. Use the environment-managed `\qed` / `\qedhere`.

## Translation-specific guidance

When the input is an English thesis chapter (e.g. `tex/PR24_en.tex`) and the target is its Russian counterpart (`tex/PR24_ru.tex`), the workflow is *translate-then-calibrate*, not *transliterate*. Two passes:

### Pass 1 — content translation

- Translate paragraph by paragraph, preserving paragraph boundaries, all `\label`, `\ref`, `\eqref`, `\cite{...}`, `\emph{...}` anchors, and all display math verbatim.
- Translate locator words inside `\cite[...]{...}` per §6.
- Translate theorem statements **after** their environment header so that `\begin{theorem}\label{th:...}` and the closing `\end{theorem}` are preserved exactly.
- Where the English uses a connective from the §3 table, replace with the Russian equivalent in the same row. Do not invent connectives; if the English sentence has none, do not add one.
- Where the English uses an `\emph{term}` defined-term anchor, find or coin a Russian equivalent and use the same `\emph{...}` markup. Record the English ↔ Russian pair in a per-chapter glossary at the top of the file (commented out) so the second pass can check consistency.

### Pass 2 — voice calibration

Run the §1–§5 checks on the Russian draft as if it had been written natively. Common drift symptoms after a literal Pass 1:

- *Word-order calques.* English "We now describe …" → drift "Мы теперь опишем …" → calibrated "Опишем теперь …" or "Перейдём к описанию …".
- *Articles → demonstratives.* English "the construction" → drift "эта конструкция" everywhere → calibrated: drop the demonstrative on first/second mention; use "указанная конструкция" or "построенная выше конструкция" only when disambiguation is needed.
- *Tense flattening.* English mathematical present → drift Russian past perfective ("мы построили", "мы получили"). Use Russian present-as-mathematical-default ("строим", "получаем", "имеем") and reserve past perfective for the introduction's "results obtained" framing ("в работе получены / установлены / описаны").
- *Pronoun drift.* English "we" sometimes silently drops in literal translation. Russian voice keeps "мы" for the rhetorical / proof-narrative role and uses impersonal constructions only for genuine impersonals ("известно, что", "несложно проверить, что").
- *Punctuation drift.* English em-dashes survive as `—` Unicode; replace with `---`. English commas before "that" / "which" do not survive in Russian — Russian comma rules apply (subordinate clauses always take a comma; non-restrictive participles do not always).

### Terminology lookup order

When a term has more than one plausible Russian rendering, resolve in this order:

1. **`P18_ru.tex` and `tex/notation.tex`.** If the term appears there, use that form.
2. **The user's prior choice** in the same chapter or elsewhere in the project.
3. **Standard Russian mathematical literature** (Шафаревич, Винберг, Тимашёв) for classical terms (схема, многообразие, дивизор, расслоение, …).

### Seeded glossary (English ↔ Russian)

Calibrated on `P18_ru.tex` and `tex/notation.tex`. The renderings below should be treated as defaults; revise against the project's authoritative sources when a conflict arises.

**The glossary is open and subject to extending.** It is not a closed list: every chapter translation will surface new terms, and the table is meant to grow with the project. When translating a new chapter:

- Whenever an English term has more than one plausible Russian rendering, or has not been used elsewhere in the thesis, **append a row** to the table below in the same format (English | Russian | Notes), and also record the English ↔ Russian pair in the per-chapter commented glossary at the top of the chapter file.
- When a term is already present, **reuse the existing rendering verbatim** so that vocabulary stays consistent across chapters.
- If a term is present but the chapter author wants a different rendering, do not silently overwrite the row — leave the existing rendering, add the alternative in the Notes column with a per-chapter tag (e.g. "P26: …"), and flag the divergence to the user for review.
- Treat each addition as a draft until the user has reviewed it; do not rely on a freshly added row to settle a downstream ambiguity in the same translation pass.

| English | Russian (preferred) | Notes |
|---|---|---|
| algebraically closed field of characteristic 0 | алгебраически замкнутое поле характеристики 0 | canonical opener |
| irreducible affine algebraic variety | неприводимое аффинное алгебраическое многообразие | |
| irreducible affine algebraic surface | неприводимая аффинная алгебраическая поверхность | |
| open embedding | открытое вложение | |
| Zariski closure | замыкание в топологии Зарисского | "Зарисский", not "Зариский" |
| completion (of an affine surface) | пополнение | "пополнение" — verb "пополнить" |
| boundary divisor | граничный дивизор | |
| simple normal crossings | простые нормальные пересечения | |
| NC-pair | NC-пара | |
| weighted dual graph | взвешенный двойственный граф | |
| vertex / edge / weight | вершина / ребро / вес | |
| self-intersection index | индекс самопересечения | |
| multiple edges | кратные рёбра | |
| birational transformation | бирациональное преобразование | |
| inner blow-up | внутреннее раздутие | |
| outer blow-up | внешнее раздутие | |
| contraction (of a divisor) | стягивание | |
| circular weighted graph | циклический взвешенный граф | |
| standard (graph) | стандартный | |
| elementary transformation (of a graph) | элементарное преобразование | |
| automorphism group | группа автоморфизмов | |
| algebraic / holomorphic automorphism group | группа алгебраических / голоморфных автоморфизмов | |
| identity component | связная компонента (единицы) | "$\Aut^\circ(X)$" |
| ind-group | инд-группа | seeded by skill author; used in `tex/ru/resume_ru.tex` |
| ind-variety | инд-многообразие | used in `tex/ru/resume_ru.tex` and `tex/ru/excluded_ru.tex` |
| Lie algebra | алгебра Ли | |
| locally finite | локально конечный | "non-locally-finite derivations" → "не локально-конечные дифференцирования" (`tex/ru/resume_ru.tex`) |
| locally nilpotent derivation (LND) | локально нильпотентное дифференцирование (ЛНД) | the abbreviation flag "(для краткости --- ЛНД)" matches the P18\_ru.tex pattern |
| nested (subgroup) | исчерпаемая (подгруппа) | исправлено автором; не вложенная |
| connected | связная | |
| rigid (variety) | жёсткое (многообразие) | adverb "жёстко"; "rigidity" → "жёсткость" |
| semi-rigid / semirigid | полужёсткое | "semirigidity" → "полужёсткость" |
| flexible (variety) | гибкое (многообразие) | "flexible at $x$" → "гибкое в точке $x$" |
| flexibility | гибкость | |
| generic flexibility / flexibility in codimension one | обобщённая гибкость / гибкость в коразмерности один | май 2026: общая → обобщённая (особенно в контексте кубических конусов) |
| transitive / infinitely transitive | транзитивный / бесконечно транзитивный | "infinite transitivity" → "бесконечная транзитивность" |
| algebraic element (of a group) | алгебраический элемент | |
| affine cone (over $X$) | аффинный конус (над $X$) | macro `\AffCone` |
| Del Pezzo surface (of degree $d$) | поверхность дель Пеццо (степени $d$) | "weak del Pezzo" → "слабая поверхность дель Пеццо" |
| Fano variety / Fano threefold | многообразие Фано / трёхмерное многообразие Фано | |
| universal torsor | универсальный торсор | |
| Cox ring | кольцо Кокса | |
| Mori dream space | пространство мечты Мори | standard rendering in Russian literature |
| total coordinate space | тотальное координатное пространство | "$\overline{X}=\Spec\,\mathcal{R}(X)$" |
| polarized (variety) / polarization | поляризованное (многообразие) / поляризация | "very ample polarization" → "очень обильная поляризация" |
| anticanonical / plurianticanonical | антиканонический / плюриантиканонический | без дефиса: плюриантиканонический (май 2026) |
| ample (cone, divisor) | обильный (конус, дивизор) | "very ample" → "очень обильный" |
| nef cone | nef-конус | kept in Latin per skill convention; alternative "конус Nef" if user prefers |
| effective cone | конус эффективных дивизоров | |
| Picard lattice | решётка Пикара | macro `\Pic` for the group |
| cylinder / cylinder method | цилиндр / цилиндрический метод | "cylinder covering" → "цилиндрическое покрытие" |
| bubble cycle | пузырьковый цикл | |
| $A$-covered (variety) | $A$-покрытое (многообразие) | |
| K-stability / K-stable | K-стабильность / K-стабильный | май 2026: K-устойчивость → K-стабильность |
| birational(ly) rigid | бирационально жёсткий | |
| amalgamated free product | амальгамированное произведение | per P18\_ru.tex; "свободное произведение с объединённой подгруппой" is heavier and avoided |
| Borel subgroup | борелевская подгруппа | |
| reductive / unipotent radical | редуктивный / унипотентный радикал | |
| Levi decomposition | разложение Леви | |
| de Jonquières / de Jonquières-like | (группа) де Жонкьера / де Жонкьеро-подобный | macro `\Jonq`; per P18\_ru.tex pattern "де Жонкьеро-подобные (для краткости --- дЖ-подобные)" |
| Jung--van der Kulk theorem | теорема Юнга-ван дер Кулка | |
| Nagata automorphism | автоморфизм Нагаты | |
| wild / tame | дикий / ручной | |
| identity component / neutral component | связная компонента (единицы) / нейтральная компонента | |
| Makar-Limanov invariant | инвариант Макар-Лиманова | генитив: Макар-Лиманова (не Макара-Лиманова) |
| field Makar-Limanov invariant | полевой инвариант Макар-Лиманова | macro `\FML` |
| Derksen invariant | инвариант Дерксена | генитив: Дерксена (Harm Derksen) |
| Gizatullin surface | поверхность Гизатуллина | |
| $\AA^1$-fibration | $\AA^1$-расслоение | |
| simple normal crossings completion | пополнение с простыми нормальными пересечениями | "minimal NC completion" → "минимальное пополнение с простыми нормальными пересечениями" |
| log-canonical threshold | логканонический порог | |
| Kodaira dimension | размерность Кодаиры | |
| Iskovskikh / Mori--Mukai (classification) | Исковских / Мори--Мукаи | |
| Tian's $\alpha$-invariant | $\alpha$-инвариант Тиана | |
| Andersén--Lempert (theory) | Андерсена--Лемперта | двойное тире `--`; не одиночный дефис |
| Stein manifold | штейново многообразие | |
| Shafarevich | Шафаревич | when citing the Russian author behind `\cite{Sh66,Sh2}` |
| Kutzschebauch | Кутчебаух | не Куцшебаух |
| Ramanujam | Рамануджам | не Раманужам |
| Blanc | Блан | не Бланк |
| Dubouloz | Дюбуло | не Дюбулоз |
| group of components | группа компонент | "$\Aut(X)/\Aut^\circ(X)$" |
| GIT quotient | GIT-фактор | kept in Latin per common Russian usage |
| irreducible / integral / separated (scheme) | неприводимый / целый / отделимый | |
| of finite type | конечного типа | |
| finitely generated | конечно порождённый | "не более чем счётный" for "at most countable" |
| smooth locus | гладкая часть | "$X_{\reg}$"; macro `\reg` |
| open embedding | открытое вложение | macro `\embed` |
| Markov triple / number / surface | тройка Маркова / число Маркова / поверхность Маркова | |
| Markov-type surface | поверхность марковского типа | |
| Diophantine equation | диофантово уравнение | |
| amalgamated product | амальгамированное произведение | |
| Thompson group | группа Томпсона | |
| Klein four-group | группа Клейна $K\cong(\ZZ/2\ZZ)^2$ | |
| holomorphic automorphism | голоморфный автоморфизм | |
| theorem / proposition / lemma / corollary / definition / remark / example / construction / question / conjecture / problem / statement | теорема / предложение / лемма / следствие / определение / замечание / пример / конструкция / вопрос / гипотеза / задача / утверждение | per `environments_ru.tex` |
| proof | доказательство | environment `proof` is babel-localized to "Доказательство" |
| we may assume | можем считать (без ограничения общности) | |
| up to (conjugation, isomorphism, scaling) | с точностью до (сопряжения, изоморфизма, умножения на скаляр) | |
| it is enough to prove that | достаточно показать, что | |
| it is well-known that | хорошо известно, что | |
| recall that | напомним, что | |
| note that | заметим, что / отметим, что | |
| moreover | кроме того / более того | |
| in particular | в частности | |
| equivalently | эквивалентно / а именно | |
| conversely | обратно | |
| see, e.g., | см., например, | |
| for short | для краткости | |
| denote by | обозначим через | symbols only |
| call | назовём / будем называть | terms only, with `\emph{...}` |

When translating new chapters, reuse these renderings verbatim and append any new terms in the same format.

## How to apply this skill

1. Read the target file with `Read`.
2. If translating from English, do **Pass 1 (content)** — paragraph-by-paragraph translation preserving math, labels, and citations — then **Pass 2 (voice)** per the §1–§5 checks.
3. If revising existing Russian prose, identify drift: AI-typical hedges, Unicode em-dashes, subject-first long sentences, missing connectives from §3, definitions without `\emph`, citations without `~`, English locator words inside Russian citations, "т.е."/"т.к." in running prose, third-person passives where "мы" works.
4. Rewrite locally with `Edit`. Keep math symbols and labels untouched; touch only prose, connectives, emphasis, and `\cite`-locator words.
5. After substantive prose changes, recompile per `CLAUDE.md`:
   ```
   cd tex && pdflatex -output-directory=output main_ru.tex
   ```
   (or `main_en.tex` if you are reviewing the parallel English version). Run two or three times if `.aux`/`.toc` warnings persist. **Do not** edit `.aux`, `.toc`, `.out`, or other temporary files by hand.
6. **Do not** edit files in `tex/APS14/`, `tex/KPZ17/`, `tex/MPS18/`, `tex/P13/`, `tex/P18/`, `tex/P21/`, `tex/P25/`, `tex/P26/`, `tex/PR23/`, `tex/PR24/`, `tex/PZ26/` — these are first sources.

## Procedure for long files

Same long-file discipline as `speech-style-adaptation/SKILL.md`:

### Survey pass

1. `wc -l` the file via `Bash` to size it.
2. `Read` the first ~200 lines to capture preamble, abstract / chapter intro, and the first section heading.
3. List the `\section{...}` / `\subsection{...}` headers with `grep -n '^\\\\\(sub\)\?section' <file>` to build a section map. Record line ranges.
4. Skim one ~300-line window per section to gauge drift density.

### Window size

- **400 lines maximum per `Read` window.** Smaller (~250–300) when the section is dense with display math.
- Always use `offset` / `limit`. Never re-read overlapping windows just to "see context".
- Keep at most two windows worth of file content in working memory at any time.

### Editing within a window

- One `\section` or one proof block per editing burst.
- Each `Edit` call rewrites **at most one paragraph** (or one proof step).
- Never rewrite a whole proof in a single `Edit`; walk it step by step.
- Leave display math, labels (`\label`, `\ref`, `\eqref`, `\cite{...}`), and `\emph{...}` defined-term anchors untouched unless calibration explicitly calls for a change.

### Per-section checkpoint

After each section is rewritten, run `cd tex && pdflatex -output-directory=output main_ru.tex` once. If `.aux`/`.toc`/`.out` warnings persist, run `pdflatex` two more times before treating it as a real error.

### Final pass

After all sections are done: re-read the chapter intro window and re-check the §3 connectives table and the anti-patterns list. Recompile. Report which sections were rewritten, which were already in voice, which were skipped (proofs unchanged, source-controlled subdirectories).

### Replacement-verification procedure

When making a systematic terminology replacement (e.g. "K-устойчивость" → "K-стабильность"), do **not** replace-all blindly and consider the job done. Instead:

1. **Grep first.** Before any editing, run:
   ```bash
   grep -n "старый термин" tex/<file>.tex
   ```
   Record every line number. This is the ground truth of what needs to change.
2. **Fix section by section.** Work through the list in line-number order, one `Edit` call per occurrence. Do not batch unrelated occurrences in a single call; this makes it easy to miss context-dependent exceptions.
3. **Grep again after.** Re-run the same `grep` after all replacements. The output must be empty (or show only intentional survivors, e.g. the definition that still says "одного" while the rest says "другого").
4. **Check the dual direction.** After confirming the old term is gone, grep for the new term to ensure it appears in all expected locations and in the correct grammatical forms (именительный, родительный, дательный, …):
   ```bash
   grep -n "новый термин" tex/<file>.tex | wc -l
   ```
   Compare the count against expectations.
5. **Compile once.** Run `pdflatex` to confirm no LaTeX errors were introduced by the change.

This sequential approach prevents the "first half" problem where a replacement pass looks complete but leaves stragglers in sections processed too quickly.

## Sequential translation across chapters

**Never spawn subagents for translation work.** All translation must be done sequentially in the main session, chunk by chunk.

When the user asks to translate or adapt several chapters in one go (e.g. "переведи все `*_intro_en.tex` на русский", or a sweep across `P13_ru.tex`, `APS14_ru.tex`, `MPS18_ru.tex`), process them one file at a time in the main session:

1. **Order the files** by size (smallest first) or by logical dependency (prerequisites before their users).
2. **Translate one file completely** using the window-based procedure in "Procedure for long files" above.
3. **Compile** after each file: `cd tex && pdflatex -output-directory=output main_ru.tex`. Run two to three times if `.aux`/`.toc` warnings persist.
4. **Commit** immediately after each file compiles cleanly:
   ```bash
   git add tex/<file>_ru.tex
   git commit -m "translate <file>_ru.tex to Russian"
   ```
5. **Push** after each commit:
   ```bash
   git push -u origin <branch-name>
   ```
6. **Move to the next file** only after the push succeeds.

This ensures that progress is saved incrementally, no two pdflatex runs collide, and the session can be interrupted and resumed at any commit boundary without losing work.

## Worked micro-examples

**Drift → calibrated**

> *Drift (literal translation):* В этой статье мы собираемся изучить, всеобъемлющим образом, структуру унипотентных подгрупп групп автоморфизмов аффинных алгебраических многообразий.
>
> *Calibrated:* В данной работе мы описываем максимальные унипотентные подгруппы группы $\Aut(X)$, где $X$ --- аффинное алгебраическое многообразие.

> *Drift:* Важно отметить, что, опираясь на мощный аппарат, введённый в [KZ], мы можем всеобъемлюще показать, что любая связная вложенная унипотентная подгруппа на самом деле замкнута — результат, расширяющий более ранние работы.
>
> *Calibrated:* По~\cite{KZ}, всякая связная вложенная подгруппа группы $\Aut(X)$ замкнута. Это обобщает~\cite[Теорема~B]{KZ} с унипотентного случая.

> *Drift:* Следовательно, ясно, что, собирая всё воедино, мы доказали теорему.
>
> *Calibrated:* Утверждение доказано.

> *Drift:* Перейдём теперь к определению нового понятия, которое мы будем называть общим репером и которое будет очень полезно в дальнейшем.
>
> *Calibrated:* Будем говорить, что набор попарно коммутирующих локально нильпотентных дифференцирований $\partial_1,\ldots,\partial_k\in\LND(\cO(X))$, где $k\le\dim(X)$, является \emph{общим репером}, если соответствующие векторные поля линейно независимы в общей точке.

## Calibration source

Single primary source of truth for the voice: **`P18_ru.tex`** (bundled in this skill directory). Re-calibrate this skill if the user replaces or supersedes `P18_ru.tex`, or if a newer single-author Russian text by the same author is available.
