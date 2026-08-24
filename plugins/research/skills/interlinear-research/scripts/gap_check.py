#!/usr/bin/env python3
"""Report proof or claim rows that lack a worked concrete example."""
from __future__ import annotations

import argparse
from pathlib import Path

from interlinear_io import load_csv, tag_set


def is_proof_step(tags: str) -> bool:
    return bool({"proof", "claim"} & tag_set(tags))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("sentences.csv"))
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    _, rows = load_csv(args.data)
    steps = [row for row in rows if is_proof_step(row.get("tags", ""))]
    gaps = [row for row in steps if not row.get("example_step", "").strip()]
    for row in steps:
        complete = bool(row.get("example_step", "").strip())
        if args.all or not complete:
            marker = "OK" if complete else "GAP"
            print(f"{marker:3} {row.get('label', ''):20} {row.get('tags', '')}")
    print(f"steps={len(steps)} worked={len(steps) - len(gaps)} gaps={len(gaps)}")
    return 1 if gaps else 0


if __name__ == "__main__":
    raise SystemExit(main())
