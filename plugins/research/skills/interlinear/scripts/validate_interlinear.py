#!/usr/bin/env python3
"""Validate label and CSV invariants for an interlinear Typst or LaTeX document."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

from interlinear_io import load_csv, parse_sentences, tag_set

STACKS_TAG = re.compile(r"[0-9A-Z]{4}")
LEAN_STATUS = {"", "planned", "generated", "checked", "failed"}


def validate(document: Path, data: Path) -> list[str]:
    errors: list[str] = []
    sentences = parse_sentences(document)
    source_labels = [label for label, _ in sentences]
    fields, rows = load_csv(data)
    row_labels = [row.get("label", "") for row in rows]

    if "label" not in fields:
        return ["CSV has no label column"]
    if not source_labels:
        errors.append("document contains no sent(\"label\")[...] entries")

    for label, count in Counter(source_labels).items():
        if count > 1:
            errors.append(f"duplicate source label: {label}")
    for label, count in Counter(row_labels).items():
        if not label:
            errors.append("CSV contains an empty label")
        elif count > 1:
            errors.append(f"duplicate CSV label: {label}")

    source_set = set(source_labels)
    row_set = set(row_labels)
    for label in source_labels:
        if label not in row_set:
            errors.append(f"source label missing from CSV: {label}")
    for label in row_labels:
        if label and label not in source_set:
            errors.append(f"CSV label missing from source: {label}")

    order = {label: index for index, label in enumerate(source_labels)}
    for row in rows:
        label = row.get("label", "")
        active_until = row.get("active_until", "")
        if active_until:
            if active_until not in order:
                errors.append(f"{label}: unknown active_until label {active_until}")
            elif label in order and order[active_until] < order[label]:
                errors.append(f"{label}: active_until precedes the row")
        stacks_ref = row.get("stacks_ref", "")
        if stacks_ref and not STACKS_TAG.fullmatch(stacks_ref):
            errors.append(f"{label}: invalid Stacks tag {stacks_ref!r}")
        stacks_candidate = row.get("stacks_candidate", "")
        if stacks_candidate and not STACKS_TAG.fullmatch(stacks_candidate):
            errors.append(
                f"{label}: invalid candidate Stacks tag {stacks_candidate!r}"
            )
        lean_status = row.get("lean_status", "")
        if lean_status not in LEAN_STATUS:
            errors.append(f"{label}: invalid Lean status {lean_status!r}")
        if lean_status == "checked":
            if not row.get("lean_ref", "").strip():
                errors.append(f"{label}: checked Lean status needs lean_ref")
            if not row.get("lean_toolchain", "").strip():
                errors.append(f"{label}: checked Lean status needs lean_toolchain")
        if "" in tag_set(row.get("tags", "")):
            errors.append(f"{label}: empty tag")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document", type=Path, default=Path("document.typ"))
    parser.add_argument("--data", type=Path, default=Path("sentences.csv"))
    args = parser.parse_args()
    errors = validate(args.document, args.data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    count = len(parse_sentences(args.document))
    print(f"OK: {count} labelled sentences; source and CSV agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
