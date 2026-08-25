# Voice calibration

This guide extracts recurring choices from the single-author Russian article
in [`corpus/P18_ru.tex`](corpus/P18_ru.tex). Treat them as tendencies, not laws.
Match the local project when it has an established voice.

## Stance and rhythm

- Use authorial plural for the author's actions: `мы вводим`, `мы находим`,
  `мы будем работать`. Use an impersonal form when the action is genuinely
  impersonal: `хорошо известно`, `несложно проверить`.
- Use direct setup verbs found in the corpus: `Пусть`, `Рассмотрим`, `Введём`,
  `Заметим`.
- Prefer short claims joined by explicit logical links. Put the reason first
  when that makes the inference clearer: `По теореме~..., ...`.
- Do not manufacture a connective merely to imitate the corpus. Use one only
  when it states the actual relation.
- Prefer present tense for the mathematical argument. Use past tense for
  historical facts or genuinely completed work.

Corpus-backed transitions include `Тогда`, `Значит`, `Следовательно`,
`Из этого следует, что`, `В частности`, `С другой стороны`, `А именно`, and
`С точностью до`. Vary them according to logic, not rhythm.

## Definitions and proofs

- Introduce terms with `\emph{...}` and a direct definition: `... называется
  \emph{стандартным}, если ...` or `\emph{Пополнением} будем называть ...`.
- Use `обозначим через` for a symbol and `назовём` or `будем называть` for a
  term.
- Keep proofs as explicit, justified steps. The corpus uses the terse closer
  `Противоречие.`; preserve environment-managed proof marks.
- Use lists when the mathematics is genuinely a list of cases, conditions, or
  objects. Prose is preferable for a mere sequence of remarks.

## Diction

Prefer plain mathematical Russian:

| Prefer | Avoid unless the meaning requires it |
|---|---|
| `Заметим, что` | `Важно отметить, что`, `Стоит подчеркнуть, что` |
| `состоит из` | `представляет собой совокупность` |
| `можем считать, что` | `в.о.о.`, `WLOG` |
| `то есть`, `так как` | `т.е.`, `т.к.` in running prose |
| `см., например,` | bulky source preambles |

Avoid promotional adjectives, bureaucratic padding, literal English word
order, and first-person singular. Do not replace a precise cautious statement
with a stronger one merely to sound decisive.
