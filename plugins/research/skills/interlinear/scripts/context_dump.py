#!/usr/bin/env python3
"""Export active earlier statements as JSON context for each source label."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from interlinear_io import load_csv, parse_sentences, tag_set


def build(
    document: Path, data: Path, requested_tags: set[str] | None = None
) -> dict[str, object]:
    sentences = parse_sentences(document)
    order = {label: index for index, (label, _) in enumerate(sentences)}
    bodies = dict(sentences)
    _, rows = load_csv(data)
    metadata = {row.get("label", ""): row for row in rows}

    def final_index(label: str) -> int:
        final = metadata.get(label, {}).get("active_until", "") or label
        return order.get(final, order[label])

    result: dict[str, object] = {}
    for label, _ in sentences:
        index = order[label]
        context = []
        for earlier, earlier_index in order.items():
            if earlier_index >= index or final_index(earlier) < index:
                continue
            row = metadata.get(earlier, {})
            row_tags = tag_set(row.get("tags", ""))
            if requested_tags and not requested_tags & row_tags:
                continue
            context.append({
                "label": earlier,
                "text": bodies[earlier],
                "tags": sorted(row_tags),
                "active_until": row.get("active_until", ""),
            })
        result[label] = {
            "index": index,
            "text": bodies[label],
            "tags": metadata.get(label, {}).get("tags", ""),
            "active_until": metadata.get(label, {}).get("active_until", ""),
            "context": context,
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document", type=Path, default=Path("document.typ"))
    parser.add_argument("--data", type=Path, default=Path("sentences.csv"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--label")
    parser.add_argument(
        "--tags",
        help="comma-separated tags; keep active rows matching at least one",
    )
    args = parser.parse_args()
    requested_tags = {
        tag.strip() for tag in (args.tags or "").split(",") if tag.strip()
    }
    result = build(args.document, args.data, requested_tags)
    selected = result.get(args.label) if args.label else result
    if args.label and selected is None:
        print(f"ERROR: unknown label {args.label}")
        return 1
    rendered = json.dumps(selected, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
        print(f"Wrote {len(result)} labels to {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
