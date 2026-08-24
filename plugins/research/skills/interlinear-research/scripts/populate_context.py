#!/usr/bin/env python3
"""Propose or write heuristic active_until values for labelled statements."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

from interlinear_io import load_csv, parse_sentences, save_csv

STOP = {
    "если", "тогда", "значит", "также", "снова", "обоих", "каждый", "каждое",
    "каждого", "всех", "любая", "любой", "этом", "этих", "которо", "через",
    "будет", "имеем", "поэтому", "получа", "только", "более", "менее", "можно",
    "пусть", "возьмём", "покажем", "обозначим", "доказательство", "утверждение",
}
MATH_TOKEN = re.compile(r"[A-Za-z]_[A-Za-z0-9]+|[A-Za-z]\^?\([^)]*\)")
WORD = re.compile(r"[А-Яа-яЁёA-Za-z]{4,}")


def stem(word: str) -> str:
    lowered = word.lower()
    return lowered[:5] if len(lowered) >= 5 else lowered


def tokens(body: str) -> set[str]:
    result = {
        match.replace(" ", "") for match in MATH_TOKEN.findall(body) if len(match) >= 3
    }
    result.update(
        value for value in (stem(word) for word in WORD.findall(body))
        if value not in STOP and len(value) >= 4
    )
    return result


def compute(sentences: list[tuple[str, str]], common_ratio: float) -> dict[str, str]:
    labels = [label for label, _ in sentences]
    token_sets = [tokens(body) for _, body in sentences]
    frequency: Counter[str] = Counter()
    for token_set in token_sets:
        frequency.update(token_set)
    threshold = max(2, int(common_ratio * len(sentences)))
    distinctive = [
        {token for token in token_set if frequency[token] <= threshold}
        for token_set in token_sets
    ]
    result: dict[str, str] = {}
    for index, label in enumerate(labels):
        last = index
        for later in range(index + 1, len(labels)):
            if distinctive[index] & token_sets[later]:
                last = later
        result[label] = labels[last]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document", type=Path, default=Path("document.typ"))
    parser.add_argument("--data", type=Path, default=Path("sentences.csv"))
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--common", type=float, default=0.25)
    args = parser.parse_args()

    sentences = parse_sentences(args.document)
    computed = compute(sentences, args.common)
    fields, rows = load_csv(args.data)
    if "active_until" not in fields:
        print("ERROR: CSV has no active_until column")
        return 1
    by_label = {row.get("label", ""): row for row in rows}
    order = {label: index for index, (label, _) in enumerate(sentences)}
    changed = 0
    print(f"{'label':20} {'active_until':20} span")
    for label, _ in sentences:
        active_until = computed[label]
        span = order[active_until] - order[label] + 1
        print(f"{label:20} {active_until:20} {span}")
        row = by_label.get(label)
        if args.write and row is not None and (args.force or not row.get("active_until", "")):
            if row.get("active_until", "") != active_until:
                row["active_until"] = active_until
                changed += 1
    if args.write:
        save_csv(args.data, fields, rows)
        print(f"Updated {changed} rows in {args.data}")
    else:
        print("Preview only; pass --write to fill empty values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
