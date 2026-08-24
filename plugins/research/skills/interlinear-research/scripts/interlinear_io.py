"""Shared parsing and CSV utilities for interlinear research documents."""
from __future__ import annotations

import csv
import os
import re
import tempfile
from pathlib import Path

SENT_START = re.compile(r'#sent\(\s*"([^"]+)"\s*\)\s*\[')


def parse_sentences(path: str | Path) -> list[tuple[str, str]]:
    """Return labelled Typst bodies in source order."""
    source = Path(path).read_text(encoding="utf-8")
    result: list[tuple[str, str]] = []
    for match in SENT_START.finditer(source):
        index = match.end()
        depth = 1
        while index < len(source) and depth:
            char = source[index]
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            index += 1
        if depth:
            raise ValueError(f"unclosed sent body for {match.group(1)!r} in {path}")
        result.append((match.group(1), source[match.end() : index - 1].strip()))
    return result


def load_csv(path: str | Path) -> tuple[list[str], list[dict[str, str]]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def save_csv(path: str | Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    """Atomically replace a CSV while preserving its declared column order."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent, text=True
    )
    try:
        with os.fdopen(descriptor, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows({key: row.get(key, "") for key in fields} for row in rows)
        os.replace(temporary, destination)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def tag_set(value: str) -> set[str]:
    return {tag.strip() for tag in value.split(";") if tag.strip()}
