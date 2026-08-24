#!/usr/bin/env python3
"""Search a local Stacks-style index or fill candidate stacks_ref values."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from interlinear_io import load_csv, save_csv

BASE_URL = "https://stacks.math.columbia.edu/tag/"
STOP = {
    "that", "this", "with", "from", "have", "every", "into", "then", "than",
    "over", "under", "such", "some", "lies", "case", "both", "also", "where",
    "which", "there", "being", "show", "take", "each", "step", "form", "same",
    "definition", "proof", "claim", "corollary", "theorem", "proposition",
    "example", "examples", "lemma", "indeed", "equivalently", "conversely",
}


def tokens(text: str) -> set[str]:
    return {
        word[:6] for word in re.findall(r"[A-Za-z]{4,}", text.lower())
        if word not in STOP
    }


def load_index(path: Path) -> list[dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data["entries"]
    for entry in entries:
        haystack = " ".join(
            str(entry.get(field, "")) for field in ("title", "statement", "keywords")
        )
        entry["_tokens"] = tokens(haystack)
    return entries


def score(query_tokens: set[str], entry: dict[str, object]) -> float:
    shared = query_tokens & set(entry["_tokens"])
    bonus_terms = {"hilber", "leadin", "coeffi", "ascend", "minima", "spectr", "presen"}
    return float(len(shared) + len(shared & bonus_terms))


def rank(query: str, entries: list[dict[str, object]], limit: int = 3):
    query_tokens = tokens(query)
    scored = sorted(
        ((score(query_tokens, entry), entry) for entry in entries),
        key=lambda item: item[0], reverse=True,
    )
    return [(value, entry) for value, entry in scored[:limit] if value > 0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?")
    parser.add_argument("--index", type=Path, default=Path("stacks-index.json"))
    parser.add_argument("--data", type=Path, default=Path("sentences.csv"))
    parser.add_argument("--fill", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--min-score", type=float, default=2.0)
    parser.add_argument("--query-field", default="translation_en")
    args = parser.parse_args()
    entries = load_index(args.index)

    if args.query:
        for value, entry in rank(args.query, entries):
            print(f"[{entry['tag']}] score={value:.1f} {entry['title']}")
            print(f"  {BASE_URL}{entry['tag']}")
        return 0
    if not args.fill:
        parser.error("provide a query or --fill")

    fields, rows = load_csv(args.data)
    if "stacks_ref" not in fields or args.query_field not in fields:
        print(f"ERROR: CSV needs stacks_ref and {args.query_field} columns")
        return 1
    changed = 0
    for row in rows:
        if row.get("stacks_ref", "") and not args.force:
            continue
        hits = rank(row.get(args.query_field, ""), entries, limit=1)
        if hits and hits[0][0] >= args.min_score:
            value, entry = hits[0]
            row["stacks_ref"] = str(entry["tag"])
            changed += 1
            print(f"{row.get('label', '')}: candidate {entry['tag']} score={value:.1f}")
    save_csv(args.data, fields, rows)
    print(f"Updated {changed} candidate references in {args.data}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
