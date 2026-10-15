---
parent: AGENTS.md
---

# AI tools for working mathematicians / ИИ-инструменты для работающих математиков

[Русский](#русский) · [English](#english)

## Русский

Это marketplace плагинов Codex для чтения математических статей, разбора
доказательств, работы с LaTeX и Typst, библиографией, Lean и исследовательскими
заметками. Устанавливайте только нужные плагины.

### Установка

Добавьте marketplace и установите первый плагин:

```sh
codex plugin marketplace add aperep/my-ai-plugins --ref main
codex plugin add research@aperep
codex plugin list
```

Другие плагины устанавливаются так же: например,
`codex plugin add math-writing@aperep`. После установки начните новую сессию
Codex.

### Использование

- Плагин — устанавливаемая группа навыков; навык — инструкция для определённого
  типа задачи.
- Обычно достаточно описать задачу обычным языком: Codex выбирает подходящий
  навык по контексту.
- При необходимости назовите навык явно: например, «используй
  `research:reason`».
- Навык может включать инструкции, справочные материалы, шаблоны, локальные
  скрипты, hooks или обращение к внешнему сервису. Существенные механизмы
  перечислены ниже.

### `research`

Чтение и разбор математических текстов, аннотирование и явно запрошенная
формализация.

| Навык | Когда нужен | Результат |
|---|---|---|
| [`extracting-precise-results`](plugins/research/skills/extracting-precise-results/SKILL.md) | Пересказ статьи теряет номер, гипотезы или точное место результата | Номер, полные гипотезы, заключение и положение теоремы, леммы или следствия в источнике |
| [`reason`](plugins/research/skills/reason/SKILL.md) | Объяснение использует неявный или посторонний контекст либо смешивает неформальный разбор с формальной проверкой | Локальный разбор шага, предположений, примеров или пробела без заявления о формальной проверке |
| [`interlinear`](plugins/research/skills/interlinear/SKILL.md) | Переводы, комментарии и ссылки теряют связь с конкретными предложениями исходника | LaTeX-текст со стабильными `\itag`-метками и отдельный типизированный файл аннотаций |
| [`formalize`](plugins/research/skills/formalize/SKILL.md) | Сгенерированный Lean-код ошибочно принимают за проверенное доказательство | Lean-файл, зафиксированный toolchain и явный статус `planned`, `generated`, `checked` или `failed` |

Встроено: LaTeX-пакет `interlinear.sty`, схема аннотаций и режимы отображения.
`formalize` использует локальный Lean; Aristotle подключается только по явному
выбору, через закреплённый `aristotlelib`, и получает только явно выбранные
файлы.

### `math-writing`

Подготовка и языковая правка математических текстов.

| Навык | Когда нужен | Результат |
|---|---|---|
| [`proofreading-pass`](plugins/math-writing/skills/proofreading-pass/SKILL.md) | Языковая правка может незаметно изменить математику или потеряться в списке замечаний | Исправленный `.tex`, категоризированный журнал и `latexdiff`; сомнительные изменения только предлагаются |
| [`simple-english`](plugins/math-writing/skills/simple-english/SKILL.md) | Корректный английский остаётся излишне сложным для чтения | Более прямой английский без смены смысла и голоса автора |
| [`occam-no-slop`](plugins/math-writing/skills/occam-no-slop/SKILL.md) | Текст разрастается за счёт наполнителя, лишних случаев и риторики | Сокращённый текст с сохранёнными утверждениями |
| [`project-scaffold`](plugins/math-writing/skills/project-scaffold/SKILL.md) | Новая статья получает случайный или несовместимый набор пакетов, окружений и обозначений | Минимальный LaTeX-каркас либо осторожное обновление существующего проекта |
| [`russian-translation`](plugins/math-writing/skills/russian-translation/SKILL.md) | Буквальный перевод ломает русскую математическую норму или LaTeX | Русский математический текст в персональном стиле А. Перепечко |
| [`speech-style-adaptation`](plugins/math-writing/skills/speech-style-adaptation/SKILL.md) | Общая редактура стирает узнаваемый английский голос автора | Английский математический текст в персональном стиле А. Перепечко |

Встроено: LaTeX-каркас, окружения, обозначения, `latexmk`/`latexdiff` workflow,
терминология и два авторских корпуса. Файл контактов в `project-scaffold` и оба
voice-навыка персональны; не используйте их как общие данные без проверки.
Typst-каркас в этом плагине пока зарезервирован, но не является готовым
шаблоном.

### `biblio`

Проверка библиографии и синхронизация библиографических записей.

| Навык | Когда нужен | Результат |
|---|---|---|
| [`bibliography-check`](plugins/biblio/skills/bibliography-check/SKILL.md) | Правдоподобная ссылка содержит неверные авторов, год, страницы, DOI или переводные данные | Сверка каждого поля с Semantic Scholar и, для русских публикаций, MathNet |
| [`zotero-library`](plugins/biblio/skills/zotero-library/SKILL.md) | Ручное добавление создаёт дубликаты или перезаписывает устойчивый citation key | Проверенная запись, дедупликация и синхронизация Zotero с локальными записями |
| [`mathscinet`](plugins/biblio/skills/mathscinet/SKILL.md) | MR-номер угадывается или переносится без проверки | Найденный и сопоставленный MR-номер либо явный отчёт, что совпадение не найдено |
| [`personal-bibliography`](plugins/biblio/skills/personal-bibliography/SKILL.md) | Личная библиография копируется из разных версий и расходится по ключам | Выбранные записи из встроенного корпуса А. Перепечко |

Встроено: Python-парсер `\bibitem`, web-запросы к Semantic Scholar и MathNet,
правила citation keys и персональные TeX-корпуса. `zotero-library` требует
доступного Zotero connector. `mathscinet` требует частной конфигурации доступа
и сети ВШЭ или VPN; значения credentials в плагин не входят.

### `typst`

Нативное написание Typst-документов и перенос из LaTeX.

| Навык | Когда нужен | Результат |
|---|---|---|
| [`typst`](plugins/typst/skills/typst/SKILL.md) | Механический перенос оставляет LaTeX-команды и неидиоматические конструкции | Typst-документ с нативными формулами, ссылками, списками, таблицами и рисунками |

Встроено: таблица LaTeX → Typst, шаблоны русской заметки и слайдов и локальный
`check_typst_migration.py`. Для компиляции нужен Typst; шаблоны содержат
персональные элементы, которые следует заменить.

### `knowledge`

Поиск и обслуживание исследовательских заметок и связанных хранилищ.
[Подробное описание плагина](plugins/knowledge/README.md).

| Навык | Когда нужен | Результат |
|---|---|---|
| [`find`](plugins/knowledge/skills/find/SKILL.md) | Поиск только в текущей папке пропускает каноническую заметку в связанном хранилище | Поиск по документированной карте источников с указанием найденного места |
| [`knowledge-rule`](plugins/knowledge/skills/knowledge-rule/SKILL.md) | Заметки складываются в случайные папки или получают несколько канонических копий | Выбор одного канонического места по локальным правилам |
| [`move`](plugins/knowledge/skills/move/SKILL.md) | После переноса остаются дубликаты, битые ссылки или потерянные вложения | Перенос канонического объекта с проверкой зависимостей и источника |
| [`cross-boundary`](plugins/knowledge/skills/cross-boundary/SKILL.md) | Частный источник копируется в общее хранилище целиком либо доставка ошибочно становится переносом | Явное различение ссылки, доставки копии и смены канонического места |
| [`process-inbox`](plugins/knowledge/skills/process-inbox/SKILL.md) | Сырой inbox бесконечно смешивает временные материалы и долговечные записи | Обработка серии по lifecycle конкретного хранилища |
| [`audit-knowledge`](plugins/knowledge/skills/audit-knowledge/SKILL.md) | Дубликаты, сироты, битые ссылки и устаревшие факты накапливаются незаметно | Отчёт и предлагаемые изменения без автоматической чистки по умолчанию |
| [`agent-charter`](plugins/knowledge/skills/agent-charter/SKILL.md) | Долговечное устройство прикреплённого агента расходится между runtime-инструкциями | Канонический `docs/charter` и явный отчёт о самоизменениях агента |

Встроено: карты хранилищ, локальные lifecycle и правила границ. Плагин не
зашивает личные пути; он использует инструкции текущего хранилища и доступные
connectors.

### `dev`

Разработка программного обеспечения, в том числе математического.

| Навык | Когда нужен | Результат |
|---|---|---|
| [`flow`](plugins/dev/skills/flow/SKILL.md) | Агент повторяет уже выполненные стадии, смешивает чужие изменения или неясно распоряжается Git | Один процесс от текущего состояния до проверенной доставки с явным Git-режимом |
| [`grill-docs`](plugins/dev/skills/grill-docs/SKILL.md) | Реализация начинается до согласования пользователя, границ и проверяемого результата | Компактный контракт требований и только существенные вопросы |
| [`debug`](plugins/dev/skills/debug/SKILL.md) | Правка маскирует симптом, не находя первую нарушенную величину или состояние | Диагноз причины, ограниченное исправление и воспроизведение исходного сбоя |
| [`tdd`](plugins/dev/skills/tdd/SKILL.md) | Изменение поведения не имеет проверки, способной поймать регрессию | Осмысленный тест и минимальная реализация |
| [`verify`](plugins/dev/skills/verify/SKILL.md) | «Готово» заявляется без выполнения относящихся к задаче проверок | Свежие команды, результаты и явно названные ограничения доказательства |
| [`review`](plugins/dev/skills/review/SKILL.md) | Review превращается в стилистические предпочтения или рассматривает не тот diff | Находки по корректности и/или сложности с точным scope |
| [`audit`](plugins/dev/skills/audit/SKILL.md) | Лишние зависимости и абстракции видны только по одной и не оцениваются по всему репозиторию | Ранжированный repo-wide список того, что удалить или заменить стандартными средствами |

Встроено: инструкции и общий Occam-reference. Плагин использует Git, тесты и
инструменты самого проекта; отдельного сервиса или фонового процесса нет.

### `meta`

Разработка этого marketplace и других наборов навыков; обычному пользователю
математических плагинов он не нужен.

| Навык | Когда нужен | Результат |
|---|---|---|
| [`doc-map`](plugins/meta/skills/doc-map/SKILL.md) | Операционные документы расползаются и перестают быть доступны из `AGENTS.md` | Проверенная карта агентской документации |
| [`skill-quality`](plugins/meta/skills/skill-quality/SKILL.md) | Навык добавляется без повторяемой проблемы, trigger-тестов или отрицательного случая | Baseline, минимальная инструкция и свежие evals |
| [`maintenance`](plugins/meta/skills/maintenance/SKILL.md) | Inbox, roadmap и проверки репозитория дрейфуют независимо | Один maintenance-проход по документированному checklist |
| [`editing-this-marketplace`](plugins/meta/skills/editing-this-marketplace/SKILL.md) | Manifest, версия и установленный cache расходятся | Синхронизированные wrappers, валидация и локальная установка |
| [`trusting-foreign-skills`](plugins/meta/skills/trusting-foreign-skills/SKILL.md) | Безобидный README скрывает исполняемый код, hooks или внешние соединения | Проверка фактически устанавливаемого payload и его происхождения |
| [`evolving-plugins`](plugins/meta/skills/evolving-plugins/SKILL.md) | Полезный урок сессии теряется либо сразу превращается в непроверенное общее правило | Минимальный проверяемый draft изменения навыка |

Встроено: два Python session-start hook, eval-файлы и review guards из
`.gitattributes`. Один hook включает guarded evolution только внутри этого
marketplace; второй добавляет ограниченный индекс документации текущего
репозитория.

Пакет `obsidian` зарезервирован и сейчас недоступен для установки.

## English

This is a Codex plugin marketplace for reading mathematical papers, analysing
proofs, working with LaTeX and Typst, maintaining bibliographies, using Lean,
and managing research notes. Install only the plugins you need.

### Installation

Add the marketplace and install a first plugin:

```sh
codex plugin marketplace add aperep/my-ai-plugins --ref main
codex plugin add research@aperep
codex plugin list
```

Install other plugins in the same way, for example
`codex plugin add math-writing@aperep`. Start a new Codex session after
installation.

### Usage

- A plugin is an installable group of skills; a skill is an instruction set for
  a particular task shape.
- Usually, describe the task normally and Codex selects the relevant skill from
  context.
- Name a skill explicitly when needed, for example: “use `research:reason`.”
- A skill may include instructions, references, templates, local scripts,
  hooks, or an external service. Material mechanisms are listed below.

### `research`

Reading and analysing mathematical texts, annotation, and explicitly requested
formalisation.

| Skill | When to use it | Result |
|---|---|---|
| [`extracting-precise-results`](plugins/research/skills/extracting-precise-results/SKILL.md) | A summary loses the result number, hypotheses, or exact source location | The number, full hypotheses, conclusion, and location of a theorem, lemma, or corollary |
| [`reason`](plugins/research/skills/reason/SKILL.md) | An explanation relies on implicit or unrelated context, or conflates informal analysis with formal verification | A local analysis of a step, assumptions, example, or gap without claiming formal verification |
| [`interlinear`](plugins/research/skills/interlinear/SKILL.md) | Translations, comments, and references lose their connection to exact source sentences | LaTeX source with stable `\itag` labels and a separate typed annotation file |
| [`formalize`](plugins/research/skills/formalize/SKILL.md) | Generated Lean code is mistaken for a checked proof | A Lean file, pinned toolchain, and explicit `planned`, `generated`, `checked`, or `failed` status |

Bundled mechanisms: the `interlinear.sty` LaTeX package, annotation schema, and
rendering modes. `formalize` uses local Lean; Aristotle is opt-in, uses a pinned
`aristotlelib`, and receives only explicitly selected files.

### `math-writing`

Preparing and editing mathematical prose.

| Skill | When to use it | Result |
|---|---|---|
| [`proofreading-pass`](plugins/math-writing/skills/proofreading-pass/SKILL.md) | Language editing may silently change mathematics or disappear into an informal list | A corrected `.tex`, categorised change log, and `latexdiff`; uncertain changes remain suggestions |
| [`simple-english`](plugins/math-writing/skills/simple-english/SKILL.md) | Correct English remains unnecessarily difficult to read | More direct English with the meaning and authorial voice preserved |
| [`occam-no-slop`](plugins/math-writing/skills/occam-no-slop/SKILL.md) | Prose grows through filler, needless cases, and rhetoric | Shorter prose with its claims preserved |
| [`project-scaffold`](plugins/math-writing/skills/project-scaffold/SKILL.md) | A new paper accumulates an arbitrary or conflicting set of packages, environments, and notation | A minimal LaTeX scaffold or a cautious refresh of an existing project |
| [`russian-translation`](plugins/math-writing/skills/russian-translation/SKILL.md) | Literal translation breaks Russian mathematical usage or LaTeX | Russian mathematical prose in A. Perepechko's personal style |
| [`speech-style-adaptation`](plugins/math-writing/skills/speech-style-adaptation/SKILL.md) | Generic editing erases a recognisable English authorial voice | English mathematical prose in A. Perepechko's personal style |

Bundled mechanisms: a LaTeX scaffold, environments, notation,
`latexmk`/`latexdiff` workflow, terminology, and two authorial corpora. The
contact file in `project-scaffold` and both voice skills are personal; do not
treat them as generic data without confirmation. The Typst scaffold in this
plugin is reserved but not yet a usable template.

### `biblio`

Bibliography verification and record synchronisation.

| Skill | When to use it | Result |
|---|---|---|
| [`bibliography-check`](plugins/biblio/skills/bibliography-check/SKILL.md) | A plausible citation has incorrect authors, year, pages, DOI, or translation metadata | Field-by-field verification against Semantic Scholar and, for Russian publications, MathNet |
| [`zotero-library`](plugins/biblio/skills/zotero-library/SKILL.md) | Manual entry creates duplicates or overwrites a stable citation key | A verified record, deduplication, and synchronisation between Zotero and local records |
| [`mathscinet`](plugins/biblio/skills/mathscinet/SKILL.md) | An MR number is guessed or copied without verification | A matched MR number or an explicit report that no match was found |
| [`personal-bibliography`](plugins/biblio/skills/personal-bibliography/SKILL.md) | A personal bibliography is copied from divergent versions with inconsistent keys | Selected records from A. Perepechko's bundled corpus |

Bundled mechanisms: a local `\bibitem` parser, web requests to Semantic Scholar
and MathNet, citation-key rules, and personal TeX corpora. `zotero-library`
requires an available Zotero connector. `mathscinet` requires private access
configuration and the HSE network or VPN; credentials are not bundled.

### `typst`

Native Typst authoring and LaTeX migration.

| Skill | When to use it | Result |
|---|---|---|
| [`typst`](plugins/typst/skills/typst/SKILL.md) | Mechanical conversion leaves LaTeX commands and non-idiomatic structures | A Typst document with native mathematics, references, lists, tables, and figures |

Bundled mechanisms: a LaTeX-to-Typst map, Russian note and slide templates, and
the local `check_typst_migration.py` checker. Typst is required for compilation;
the templates contain personal elements that should be replaced.

### `knowledge`

Finding and maintaining research notes and related stores.
[Detailed plugin documentation](plugins/knowledge/README.md).

| Skill | When to use it | Result |
|---|---|---|
| [`find`](plugins/knowledge/skills/find/SKILL.md) | Searching only the current directory misses a canonical note in a linked store | Search through the documented source map with the recorded location returned |
| [`knowledge-rule`](plugins/knowledge/skills/knowledge-rule/SKILL.md) | Notes are filed arbitrarily or acquire several canonical copies | One canonical home selected from local rules |
| [`move`](plugins/knowledge/skills/move/SKILL.md) | A move leaves duplicates, broken links, or missing attachments | Relocation of the canonical object with dependency and source checks |
| [`cross-boundary`](plugins/knowledge/skills/cross-boundary/SKILL.md) | A private source is copied wholesale into a shared store, or delivery is mistaken for relocation | An explicit distinction between linking, delivering a copy, and changing canonical home |
| [`process-inbox`](plugins/knowledge/skills/process-inbox/SKILL.md) | A raw inbox indefinitely mixes temporary material and maintained records | Batch processing under the store's own lifecycle |
| [`audit-knowledge`](plugins/knowledge/skills/audit-knowledge/SKILL.md) | Duplicates, orphans, broken links, and stale facts accumulate unnoticed | A report and proposed changes, without automatic cleanup by default |
| [`agent-charter`](plugins/knowledge/skills/agent-charter/SKILL.md) | An attached agent's durable design drifts across runtime instruction files | A canonical `docs/charter` and explicit reporting of agent self-changes |

Bundled mechanisms: storage maps, local lifecycles, and boundary rules. The
plugin does not hard-code personal paths; it uses the current store's
instructions and available connectors.

### `dev`

Software development, including mathematical software.

| Skill | When to use it | Result |
|---|---|---|
| [`flow`](plugins/dev/skills/flow/SKILL.md) | An agent repeats completed phases, mixes unrelated changes, or handles Git ambiguously | One workflow from the actual current state to verified delivery under an explicit Git mode |
| [`grill-docs`](plugins/dev/skills/grill-docs/SKILL.md) | Implementation begins before the user, boundaries, and observable outcome are aligned | A compact requirements contract and only material questions |
| [`debug`](plugins/dev/skills/debug/SKILL.md) | A patch hides the symptom without finding the first invalid state or value | Root-cause diagnosis, a scoped fix, and reproduction of the original failure |
| [`tdd`](plugins/dev/skills/tdd/SKILL.md) | A behaviour change lacks a check capable of catching its regression | A meaningful test and the smallest implementation |
| [`verify`](plugins/dev/skills/verify/SKILL.md) | “Done” is claimed without running checks relevant to the task | Fresh commands, observed results, and explicit limits of the evidence |
| [`review`](plugins/dev/skills/review/SKILL.md) | Review becomes stylistic preference or examines the wrong diff | Findings about correctness and/or complexity over an exact scope |
| [`audit`](plugins/dev/skills/audit/SKILL.md) | Dependencies and abstractions are seen individually rather than as repository-wide bloat | A ranked repository-wide list of what to delete or replace with native facilities |

Bundled mechanisms: instructions and a shared Occam reference. The plugin uses
Git, tests, and tools from the target project; it has no separate service or
background process.

### `meta`

Developing this marketplace and other skill collections. Ordinary users of the
mathematics plugins do not need it.

| Skill | When to use it | Result |
|---|---|---|
| [`doc-map`](plugins/meta/skills/doc-map/SKILL.md) | Operational documents sprawl and cease to be reachable from `AGENTS.md` | A checked map of agent-facing repository documentation |
| [`skill-quality`](plugins/meta/skills/skill-quality/SKILL.md) | A skill is added without a repeatable problem, trigger cases, or a negative control | A baseline, minimal instruction, and fresh evaluations |
| [`maintenance`](plugins/meta/skills/maintenance/SKILL.md) | The inbox, roadmap, and repository checks drift independently | One maintenance pass under the documented checklist |
| [`editing-this-marketplace`](plugins/meta/skills/editing-this-marketplace/SKILL.md) | A manifest, version, and installed cache disagree | Synchronised wrappers, validation, and a local installation |
| [`trusting-foreign-skills`](plugins/meta/skills/trusting-foreign-skills/SKILL.md) | A harmless README conceals executable code, hooks, or external connections | Inspection of the installed payload and its provenance |
| [`evolving-plugins`](plugins/meta/skills/evolving-plugins/SKILL.md) | A useful session lesson is lost or immediately becomes an untested general rule | The smallest testable draft of a skill change |

Bundled mechanisms: two Python session-start hooks, evaluation files, and
review guards in `.gitattributes`. One hook enables guarded evolution only
inside this marketplace; the other adds a bounded index of documentation in
the current repository.

The `obsidian` package is reserved and currently unavailable for installation.

## Compatibility / Совместимость

Codex is the primary client. Each plugin also has an Agent Plugins 1.0 manifest;
installation in other clients is client-specific. See
[packaging compatibility](docs/DUAL.md) and
[consumer setup](docs/consumer-snippets.md).

## Development / Разработка

Marketplace layout and validation rules are documented in this repository's
[agent instructions](AGENTS.md). Maintainers should validate both plugin
manifests, every changed skill, and a local Codex installation.

## License / Лицензия

The `dev` plugin is MIT-licensed and preserves its upstream notices. The
repository does not yet have one license covering every plugin, corpus, and
template; do not assume redistribution rights for unlicensed bundled material.
