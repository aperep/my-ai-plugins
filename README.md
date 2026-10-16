---
parent: AGENTS.md
---

# AI tools for mathematicians / ИИ-инструменты для математиков

[Русский](#русский) · [English](#english)

## Русский

Это набор (точнее, marketplace) плагинов Codex для чтения математических статей, разбора
доказательств, работы с LaTeX и Typst, библиографией, Lean и исследовательскими
заметками. Устанавливайте только нужные плагины.

### Установка

Достаточно дать своему агенту ссылку на этот репозиторий и попросить установить.

Явные команды установки плагинов для OpenAI-агента `codex`:

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

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`extracting-precise-results`](plugins/research/skills/extracting-precise-results/SKILL.md) | При чтении статьи для обзора литературы или точного цитирования результата | Извлекает номер, гипотезы, заключение и точное место утверждения в источнике |
| [`reason`](plugins/research/skills/reason/SKILL.md) | Когда ищете доказательство или разбираете существующее | Неформально разбирает шаги, предположения, примеры и пробелы по указанному контексту |
| [`interlinear`](plugins/research/skills/interlinear/SKILL.md) | Когда нужен подстрочник с пояснениями, переводом или замечаниями | Размечает предложения LaTeX стабильными `\itag`-метками и хранит типизированные аннотации в отдельном файле |
| [`formalize`](plugins/research/skills/formalize/SKILL.md) | Когда формализуете выбранное утверждение или проверяете доказательство в Lean | Готовит Lean-код, запускает проверку, фиксирует toolchain и отделяет сгенерированное от проверенного |

Встроено: LaTeX-пакет `interlinear.sty`, схема аннотаций и режимы отображения.
`formalize` использует локальный Lean; Aristotle подключается только по явному
выбору, через закреплённый `aristotlelib`, и получает только явно выбранные
файлы.

### `math-writing`

Подготовка и языковая правка математических текстов.

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`proofreading-pass`](plugins/math-writing/skills/proofreading-pass/SKILL.md) | При вычитке LaTeX-статьи перед отправкой соавторам или в журнал | Исправляет однозначные языковые и LaTeX-ошибки; готовит исправленный исходник, журнал и `latexdiff` |
| [`simple-english`](plugins/math-writing/skills/simple-english/SKILL.md) | Когда хотите упростить английский текст | Переписывает его прямым языком, сохраняя смысл и авторский голос |
| [`occam-no-slop`](plugins/math-writing/skills/occam-no-slop/SKILL.md) | Когда сокращаете математический текст и убираете словесный наполнитель | Убирает лишнюю риторику, повторы и разбиения на случаи, сохраняя утверждения |
| [`project-scaffold`](plugins/math-writing/skills/project-scaffold/SKILL.md) | Когда начинаете новую статью или обновляете преамбулу существующей | Подбирает LaTeX-каркас, пакеты, обозначения и окружения; сравнивает с существующими файлами перед изменением |
| [`russian-translation`](plugins/math-writing/skills/russian-translation/SKILL.md) | Когда переводите, пишете или редактируете математический текст по-русски | Применяет русскую математическую терминологию и стиль автора плагина, сохраняя смысл и LaTeX |
| [`speech-style-adaptation`](plugins/math-writing/skills/speech-style-adaptation/SKILL.md) | Когда хотите написать или переработать английский текст в стиле автора плагина | Применяет правила авторского стиля из корпуса: лексику, ритм и логические переходы |

Встроено: LaTeX-каркас, окружения, обозначения, `latexmk`/`latexdiff` workflow,
терминология и два авторских корпуса. `project-scaffold` содержит заглушки для
контактов; оба voice-навыка настроены на стиль автора плагина.
Typst-каркас в этом плагине пока зарезервирован, но не является готовым
шаблоном.

### `biblio`

Проверка библиографии и синхронизация библиографических записей.

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`bibliography-check`](plugins/biblio/skills/bibliography-check/SKILL.md) | При проверке списка литературы или отдельной библиографической записи | Сверяет авторов, название, год, страницы и DOI с Semantic Scholar и MathNet |
| [`zotero-library`](plugins/biblio/skills/zotero-library/SKILL.md) | Когда ищете, добавляете или обновляете записи в Zotero | Проверяет метаданные, ищет дубликаты, сохраняет ключи цитирования и синхронизирует локальные записи |
| [`mathscinet`](plugins/biblio/skills/mathscinet/SKILL.md) | Когда нужен MR-номер статьи | Ищет совпадение в MathSciNet через указанный прокси; сообщает, если получить номер не удалось |
| [`personal-bibliography`](plugins/biblio/skills/personal-bibliography/SKILL.md) | Когда готовите список работ автора плагина или используете его библиографию | Выбирает или обновляет записи во встроенных TeX-корпусах, сохраняя ключи цитирования |

Встроено: Python-парсер `\bibitem`, web-запросы к Semantic Scholar и MathNet,
правила citation keys и персональные TeX-корпуса. `zotero-library` требует
доступного Zotero connector. `mathscinet` требует частной конфигурации доступа
и сети вашего учреждения или VPN; значения credentials в плагин не входят.

### `typst`

Нативное написание Typst-документов и перенос из LaTeX.

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`typst`](plugins/typst/skills/typst/SKILL.md) | Когда пишете статью или слайды в Typst, переносите LaTeX либо проверяете `.typ` | Применяет нативный синтаксис Typst, использует шаблоны и проверяет остаточные LaTeX-конструкции |

Встроено: таблица LaTeX → Typst, шаблоны русской заметки и слайдов и локальный
`check_typst_migration.py`. Для компиляции нужен Typst; шаблоны содержат
заглушки для автора, даты, учреждения и логотипа, которые следует заменить.

### `knowledge`

Поиск и обслуживание исследовательских заметок и связанных хранилищ.
[Подробное описание плагина](plugins/knowledge/README.md).

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`find`](plugins/knowledge/skills/find/SKILL.md) | Когда ищете записанную идею, решение или разговор и не помните точное место | Ищет по карте связанных хранилищ и возвращает найденные источники |
| [`knowledge-rule`](plugins/knowledge/skills/knowledge-rule/SKILL.md) | Когда сохраняете сообщение, факт или заметку и выбираете для них место | Выбирает каноническое место по локальным правилам и сохраняет материал с указанием происхождения |
| [`move`](plugins/knowledge/skills/move/SKILL.md) | Когда переносите заметки или другие объекты на новое постоянное место | Переносит объекты и вложения, удаляет исходники после проверки результата и обновляет известные ссылки |
| [`cross-boundary`](plugins/knowledge/skills/cross-boundary/SKILL.md) | Когда передаёте материалы между личным и общим хранилищами или разными сервисами | Определяет аудиторию и способ передачи: ссылку, копию или перенос; проверяет доступ и доставку |
| [`process-inbox`](plugins/knowledge/skills/process-inbox/SKILL.md) | Когда разбираете накопившийся inbox или серию материалов | Классифицирует материалы и обрабатывает их по правилам конкретного хранилища |
| [`audit-knowledge`](plugins/knowledge/skills/audit-knowledge/SKILL.md) | При плановой проверке базы заметок | Ищет дубликаты, сироты, битые ссылки и устаревшие сведения; предлагает исправления |
| [`agent-charter`](plugins/knowledge/skills/agent-charter/SKILL.md) | Когда задаёте или меняете назначение, правила и личность прикреплённого к репозиторию агента | Ведёт `docs/charter`, сравнивает его с рабочими инструкциями и сообщает точные самоизменения агента |

Встроено: карты хранилищ, локальные lifecycle и правила границ. Плагин не
зашивает личные пути; он использует инструкции текущего хранилища и доступные
connectors.

### `dev`

Разработка программного обеспечения, в том числе математического.

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`flow`](plugins/dev/skills/flow/SKILL.md) | Когда поручаете агенту разработку или завершение изменения кода | Ведёт задачу через нужные стадии: требования, реализацию, проверки и согласованную работу с Git |
| [`grill-docs`](plugins/dev/skills/grill-docs/SKILL.md) | Перед реализацией новой функции, когда нужно согласовать требования | Задаёт существенные вопросы и описывает границы, поведение и критерии приёмки |
| [`debug`](plugins/dev/skills/debug/SKILL.md) | Когда программа работает неверно или падает тест | Воспроизводит сбой, находит причину и, если запрошено исправление, меняет код и проверяет результат |
| [`tdd`](plugins/dev/skills/tdd/SKILL.md) | Когда добавляете поведение, исправляете известную ошибку или делаете рефакторинг | Подбирает содержательные тесты, пишет их до реализации, где это применимо, и проверяет изменение |
| [`verify`](plugins/dev/skills/verify/SKILL.md) | Перед тем как считать изменение готовым | Запускает относящиеся к задаче проверки, фиксирует результаты и недостающие подтверждения |
| [`review`](plugins/dev/skills/review/SKILL.md) | Когда нужен разбор конкретного diff или подготовленного коммита | Проверяет корректность и/или сложность изменений и указывает конкретные проблемы с их расположением |
| [`audit`](plugins/dev/skills/audit/SKILL.md) | Когда хотите упростить весь репозиторий | Ранжирует лишние зависимости, абстракции и код, который можно удалить или заменить стандартными средствами |

Встроено: инструкции и общий Occam-reference. Плагин использует Git, тесты и
инструменты самого проекта; отдельного сервиса или фонового процесса нет.

### `meta`

Разработка этого marketplace и других наборов навыков; обычному пользователю
математических плагинов он не нужен.

| Навык | Когда использовать | Что делает |
|---|---|---|
| [`doc-map`](plugins/meta/skills/doc-map/SKILL.md) | При создании или перестройке документации для агента | Проверяет дерево от `AGENTS.md`, размещение документов и ссылки между ними |
| [`skill-quality`](plugins/meta/skills/skill-quality/SKILL.md) | При создании или изменении навыка, а также проверке его срабатываний | Сопоставляет инструкцию с исходной проблемой и проверяет задачи, где навык должен и не должен включаться |
| [`maintenance`](plugins/meta/skills/maintenance/SKILL.md) | Когда запускаете плановое обслуживание репозитория | Разбирает inbox, сверяет roadmap и выполняет документированные проверки |
| [`editing-this-marketplace`](plugins/meta/skills/editing-this-marketplace/SKILL.md) | Когда меняете плагины этого marketplace или проверяете их установку | Согласует manifests и версии, проверяет структуру и переустанавливает плагин из локального источника |
| [`trusting-foreign-skills`](plugins/meta/skills/trusting-foreign-skills/SKILL.md) | Перед установкой или обновлением чужого навыка или плагина | Проверяет происхождение и содержимое пакета, включая скрипты, hooks и внешние подключения |
| [`evolving-plugins`](plugins/meta/skills/evolving-plugins/SKILL.md) | Когда работа над marketplace выявила подтверждённое улучшение его навыков | Записывает урок сессии и готовит минимальный черновик изменения навыка |

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

| Skill | When to use it | What it does |
|---|---|---|
| [`extracting-precise-results`](plugins/research/skills/extracting-precise-results/SKILL.md) | When reading a paper for a literature survey or citing a specific result | Extracts the statement's number, hypotheses, conclusion, and exact source location |
| [`reason`](plugins/research/skills/reason/SKILL.md) | When working out a proof or examining an existing one | Analyses steps, assumptions, examples, and gaps informally using the specified context |
| [`interlinear`](plugins/research/skills/interlinear/SKILL.md) | When adding sentence-level explanations, translations, or comments to a text | Labels LaTeX sentences with stable `\itag` IDs and stores typed annotations in a separate file |
| [`formalize`](plugins/research/skills/formalize/SKILL.md) | When formalising a selected statement or checking a proof in Lean | Prepares Lean code, runs checks, records the toolchain, and distinguishes generated code from checked proofs |

Bundled mechanisms: the `interlinear.sty` LaTeX package, annotation schema, and
rendering modes. `formalize` uses local Lean; Aristotle is opt-in, uses a pinned
`aristotlelib`, and receives only explicitly selected files.

### `math-writing`

Preparing and editing mathematical prose.

| Skill | When to use it | What it does |
|---|---|---|
| [`proofreading-pass`](plugins/math-writing/skills/proofreading-pass/SKILL.md) | When copyediting a LaTeX paper before sharing it with coauthors or submitting it | Applies unambiguous language and LaTeX fixes; produces a corrected source, change log, and `latexdiff` |
| [`simple-english`](plugins/math-writing/skills/simple-english/SKILL.md) | When simplifying English prose | Rewrites it in direct language while preserving meaning and authorial voice |
| [`occam-no-slop`](plugins/math-writing/skills/occam-no-slop/SKILL.md) | When tightening mathematical prose and removing filler | Cuts unnecessary rhetoric, repetition, and case splits while preserving the claims |
| [`project-scaffold`](plugins/math-writing/skills/project-scaffold/SKILL.md) | When starting a new paper or refreshing an existing preamble | Selects a LaTeX scaffold, packages, notation, and environments; compares existing files before changing them |
| [`russian-translation`](plugins/math-writing/skills/russian-translation/SKILL.md) | When translating, drafting, or revising mathematical prose in Russian | Applies Russian mathematical terminology and the plugin author's style while preserving meaning and LaTeX |
| [`speech-style-adaptation`](plugins/math-writing/skills/speech-style-adaptation/SKILL.md) | When drafting or revising English prose in the plugin author's style | Applies corpus-based voice rules for word choice, rhythm, and logical transitions |

Bundled mechanisms: a LaTeX scaffold, environments, notation,
`latexmk`/`latexdiff` workflow, terminology, and two authorial corpora.
`project-scaffold` contains contact placeholders; both voice skills are
calibrated to the plugin author's style. The Typst scaffold in this
plugin is reserved but not yet a usable template.

### `biblio`

Bibliography verification and record synchronisation.

| Skill | When to use it | What it does |
|---|---|---|
| [`bibliography-check`](plugins/biblio/skills/bibliography-check/SKILL.md) | When checking a bibliography or an individual citation | Verifies authors, title, year, pages, and DOI against Semantic Scholar and MathNet |
| [`zotero-library`](plugins/biblio/skills/zotero-library/SKILL.md) | When finding, adding, or updating Zotero records | Verifies metadata, checks for duplicates, preserves citation keys, and synchronises local records |
| [`mathscinet`](plugins/biblio/skills/mathscinet/SKILL.md) | When you need a paper's MR number | Looks for a matching MathSciNet record through the specified proxy and reports unsuccessful lookups |
| [`personal-bibliography`](plugins/biblio/skills/personal-bibliography/SKILL.md) | When preparing the plugin author's publication list or using their bibliography | Selects or maintains entries in the bundled TeX corpora while preserving citation keys |

Bundled mechanisms: a local `\bibitem` parser, web requests to Semantic Scholar
and MathNet, citation-key rules, and personal TeX corpora. `zotero-library`
requires an available Zotero connector. `mathscinet` requires private access
configuration and your institution's network or VPN; credentials are not bundled.

### `typst`

Native Typst authoring and LaTeX migration.

| Skill | When to use it | What it does |
|---|---|---|
| [`typst`](plugins/typst/skills/typst/SKILL.md) | When writing a paper or slides in Typst, migrating LaTeX, or reviewing a `.typ` file | Applies native Typst syntax, uses bundled templates, and checks for leftover LaTeX constructs |

Bundled mechanisms: a LaTeX-to-Typst map, Russian note and slide templates, and
the local `check_typst_migration.py` checker. Typst is required for compilation;
the templates contain author, date, institution, and logo placeholders to replace.

### `knowledge`

Finding and maintaining research notes and related stores.
[Detailed plugin documentation](plugins/knowledge/README.md).

| Skill | When to use it | What it does |
|---|---|---|
| [`find`](plugins/knowledge/skills/find/SKILL.md) | When looking for a recorded idea, decision, or conversation without remembering its location | Searches the map of linked stores and returns the matching sources |
| [`knowledge-rule`](plugins/knowledge/skills/knowledge-rule/SKILL.md) | When capturing a message, fact, or note and deciding where it belongs | Selects a canonical home under local rules and preserves the material's provenance |
| [`move`](plugins/knowledge/skills/move/SKILL.md) | When relocating notes or other objects to a new canonical home | Transfers objects and attachments, verifies the result, removes the originals, and updates known links |
| [`cross-boundary`](plugins/knowledge/skills/cross-boundary/SKILL.md) | When sharing material across private and shared stores or different services | Establishes the audience and transfer mode—link, copy, or move—and checks access and delivery |
| [`process-inbox`](plugins/knowledge/skills/process-inbox/SKILL.md) | When processing an accumulated inbox or a series of materials | Classifies the material and processes it under the store's own lifecycle |
| [`audit-knowledge`](plugins/knowledge/skills/audit-knowledge/SKILL.md) | When carrying out a periodic review of a knowledge store | Finds duplicates, orphans, broken links, and stale information; proposes corrections |
| [`agent-charter`](plugins/knowledge/skills/agent-charter/SKILL.md) | When defining or changing an attached agent's purpose, rules, or personality | Maintains `docs/charter`, compares it with runtime instructions, and reports the agent's exact self-changes |

Bundled mechanisms: storage maps, local lifecycles, and boundary rules. The
plugin does not hard-code personal paths; it uses the current store's
instructions and available connectors.

### `dev`

Software development, including mathematical software.

| Skill | When to use it | What it does |
|---|---|---|
| [`flow`](plugins/dev/skills/flow/SKILL.md) | When assigning an agent a code change or asking it to finish one | Routes the task through requirements, implementation, verification, and the agreed Git workflow |
| [`grill-docs`](plugins/dev/skills/grill-docs/SKILL.md) | Before implementing a feature, when its requirements need clarification | Asks material questions and defines scope, behaviour, and acceptance criteria |
| [`debug`](plugins/dev/skills/debug/SKILL.md) | When a program misbehaves or a test fails | Reproduces the failure, traces its cause, and, when a fix is requested, changes the code and verifies the result |
| [`tdd`](plugins/dev/skills/tdd/SKILL.md) | When adding behaviour, fixing a known bug, or refactoring | Chooses meaningful tests, writes them before implementation where practical, and checks the change |
| [`verify`](plugins/dev/skills/verify/SKILL.md) | Before declaring a change complete | Runs relevant checks and records their results and any missing evidence |
| [`review`](plugins/dev/skills/review/SKILL.md) | When reviewing a specific diff or a prepared commit | Checks correctness and/or complexity and reports concrete issues with their locations |
| [`audit`](plugins/dev/skills/audit/SKILL.md) | When simplifying an entire repository | Ranks dependencies, abstractions, and code that can be removed or replaced with standard facilities |

Bundled mechanisms: instructions and a shared Occam reference. The plugin uses
Git, tests, and tools from the target project; it has no separate service or
background process.

### `meta`

Developing this marketplace and other skill collections. Ordinary users of the
mathematics plugins do not need it.

| Skill | When to use it | What it does |
|---|---|---|
| [`doc-map`](plugins/meta/skills/doc-map/SKILL.md) | When creating or reorganising agent-facing documentation | Checks the tree rooted at `AGENTS.md`, document placement, and links |
| [`skill-quality`](plugins/meta/skills/skill-quality/SKILL.md) | When creating or changing a skill or evaluating its triggers | Checks the instruction against a baseline problem and tests tasks that should and should not load it |
| [`maintenance`](plugins/meta/skills/maintenance/SKILL.md) | When running routine repository maintenance | Processes the inbox, reconciles the roadmap, and runs the documented checks |
| [`editing-this-marketplace`](plugins/meta/skills/editing-this-marketplace/SKILL.md) | When changing this marketplace's plugins or testing their installation | Synchronises manifests and versions, validates the structure, and reinstalls the plugin from the local source |
| [`trusting-foreign-skills`](plugins/meta/skills/trusting-foreign-skills/SKILL.md) | Before installing or updating a third-party skill or plugin | Reviews the package's provenance and payload, including scripts, hooks, and external connections |
| [`evolving-plugins`](plugins/meta/skills/evolving-plugins/SKILL.md) | When marketplace work produces a validated improvement to its skills | Records the session lesson and drafts the smallest skill change for review |

Bundled mechanisms: two Python session-start hooks, evaluation files, and
review guards in `.gitattributes`. One hook enables guarded evolution only
inside this marketplace; the other adds a bounded index of documentation in
the current repository.

The `obsidian` package is reserved and currently unavailable for installation.

## Свой стиль / Your own writing style

В своей копии плагина замените образцы статей и заново выведите из них правила
стиля. Одной замены корпуса недостаточно: при каждой задаче агент читает
`voice.md`, а к статьям обращается только при необходимости.

In your copy of the plugin, replace the sample papers and derive new voice
rules from them. Replacing the corpus alone is not enough: the agent reads
`voice.md` for every task and consults the papers only when needed.

| Навык / Skill | Образец / Sample paper | Правила / Voice rules |
|---|---|---|
| `speech-style-adaptation` | [jems4.tex](plugins/math-writing/skills/speech-style-adaptation/references/corpus/jems4.tex) | [voice.md](plugins/math-writing/skills/speech-style-adaptation/references/voice.md) |
| `russian-translation` | [P18_ru.tex](plugins/math-writing/skills/russian-translation/references/corpus/P18_ru.tex) | [voice.md](plugins/math-writing/skills/russian-translation/references/voice.md) |

Также пересмотрите правила [введений](plugins/math-writing/skills/speech-style-adaptation/references/introductions.md),
[терминологию](plugins/math-writing/skills/russian-translation/references/terminology.md),
LaTeX-соглашения ([EN](plugins/math-writing/skills/speech-style-adaptation/references/latex.md),
[RU](plugins/math-writing/skills/russian-translation/references/latex.md)) и
[сведения об авторе](plugins/math-writing/skills/russian-translation/references/metadata.md).
В обоих `SKILL.md` обновите имя автора и ссылки на заменённые корпуса.

Also review the [introduction rules](plugins/math-writing/skills/speech-style-adaptation/references/introductions.md),
[terminology](plugins/math-writing/skills/russian-translation/references/terminology.md),
LaTeX conventions ([EN](plugins/math-writing/skills/speech-style-adaptation/references/latex.md),
[RU](plugins/math-writing/skills/russian-translation/references/latex.md)), and
[author metadata](plugins/math-writing/skills/russian-translation/references/metadata.md).
Update the author's name and corpus links in both `SKILL.md` files.

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
