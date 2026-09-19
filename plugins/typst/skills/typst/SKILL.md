---
name: typst
description: >
  Write, migrate, and review academic or technical documents in idiomatic Typst. Use for new Typst documents, LaTeX-to-Typst migration, syntax review, slide creation, or cleanup of LaTeX habits.
---

# Typst вместо LaTeX

Reusable Russian note and slide starters are in `assets/templates/`; copy and
customize them instead of treating their personal titles, dates, or affiliation
as defaults.


Используй этот скилл, когда пользователь:
- пишет новый академический/технический текст в Typst;
- переносит текст из LaTeX в Typst;
- просит «проверить typst-файл», «почистить от latex-привычек», «сделать typst-версию».

В начале работы сообщи:
> «Использую скилл `typst`, чтобы перевести/написать материал в стиле Typst и прогнать проверки.»

## Быстрый workflow

1. **Определи режим**
   - `new`: пишем сразу нативно в Typst;
   - `migrate`: переносим LaTeX → Typst.

2. **Сделай базовые замены**
   - Прогони таблицу из `references/latex-to-typst-mapping.md`.
   - Для доклада/слайдов бери за образец `references/slides.typ` — рабочая
     презентация на `touying` (тема `university`) с `ctheorems`, `cetz`,
     `fletcher` и готовым набором математических сокращений в преамбуле.

3. **Убери LaTeX-паттерны**
   - Удали `\\command{}` там, где в Typst есть нативный синтаксис.
   - Заменяй math-блоки, ссылки, списки, таблицы и рисунки на idiomatic Typst.

4. **Проверь файл**
   - Запусти `python <каталог этого скилла>/scripts/check_typst_migration.py <file.typ>`
     (скрипт лежит рядом с `SKILL.md`; плагин может ставиться в кэш, поэтому
     не используй фиксированный путь из исходного репозитория).
   - Исправь все `ERROR` и максимально сократи `WARN`.

5. **Финальный quality-check**
   - Проверка структуры: заголовки, секции, подписи, единый стиль.
   - Проверка математики: inline/display, индексы/дроби/операторы.
   - Проверка ссылок: библиография, cross-ref, labels.

## Мини-чеклист перед завершением

- [ ] В тексте нет LaTeX-команд вида `\\...` (кроме сознательно оставленных raw-фрагментов).
- [ ] Формулы читаются в типст-стиле и не зависят от latex-пакетов.
- [ ] Ссылки и библиография собираются через Typst-механизмы.
- [ ] Таблицы/рисунки используют нативные конструкции Typst.
- [ ] Скрипт проверки не выдаёт `ERROR`.

## Когда звать пользователя

Задай 1 уточняющий вопрос, если не хватает контекста:
- целевой шаблон/издательство;
- язык документа;
- сохранить «визуально близко к LaTeX» или «максимально idiomatic Typst».
