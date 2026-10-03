"""Shared parsing and CSV utilities for interlinear Typst and LaTeX documents."""
from __future__ import annotations

import csv
import os
import re
import tempfile
from pathlib import Path

TYPST_SENT = re.compile(r'#sent\(\s*"([^"]+)"\s*\)\s*\[')
LATEX_TAG = re.compile(r"\\itag\s*\{([^{}]+)\}")
LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9:._-]*")
SHORT_ID = re.compile(r"[A-Za-z0-9]{4}")


def _mask_typst(source: str, hide_strings: bool) -> str:
    """Mask comments, and optionally strings, without changing offsets."""
    chars = list(source)
    index = 0
    block_depth = 0
    in_string = False
    while index < len(source):
        if block_depth:
            if source.startswith("/*", index):
                chars[index : index + 2] = "  "
                block_depth += 1
                index += 2
            elif source.startswith("*/", index):
                chars[index : index + 2] = "  "
                block_depth -= 1
                index += 2
            else:
                if source[index] != "\n":
                    chars[index] = " "
                index += 1
        elif in_string:
            if hide_strings and source[index] != "\n":
                chars[index] = " "
            if source[index] == "\\" and index + 1 < len(source):
                if hide_strings:
                    chars[index + 1] = " "
                index += 2
            elif source[index] == '"':
                in_string = False
                index += 1
            else:
                index += 1
        elif source.startswith("//", index):
            end = source.find("\n", index)
            end = len(source) if end < 0 else end
            chars[index:end] = " " * (end - index)
            index = end
        elif source.startswith("/*", index):
            chars[index : index + 2] = "  "
            block_depth = 1
            index += 2
        elif source[index] == '"':
            if hide_strings:
                chars[index] = " "
            in_string = True
            index += 1
        else:
            index += 1
    return "".join(chars)


def _mask_latex_comments(source: str) -> str:
    chars = list(source)
    index = 0
    while index < len(source):
        if source[index] == "%":
            slashes = 0
            before = index - 1
            while before >= 0 and source[before] == "\\":
                slashes += 1
                before -= 1
            if slashes % 2 == 0:
                end = source.find("\n", index)
                end = len(source) if end < 0 else end
                chars[index:end] = " " * (end - index)
                index = end
                continue
        index += 1
    return "".join(chars)


def _escaped(source: str, index: int) -> bool:
    slashes = 0
    index -= 1
    while index >= 0 and source[index] == "\\":
        slashes += 1
        index -= 1
    return slashes % 2 == 1


def _balanced_body(
    source: str, structural: str, start: int, opening: str, closing: str, label: str
) -> tuple[str, int]:
    depth = 1
    index = start
    while index < len(structural) and depth:
        char = structural[index]
        if char == opening and not _escaped(structural, index):
            depth += 1
        elif char == closing and not _escaped(structural, index):
            depth -= 1
        index += 1
    if depth:
        raise ValueError(f"unclosed sent body for {label!r}")
    return source[start : index - 1].strip(), index


def parse_sentences(path: str | Path) -> list[tuple[str, str]]:
    """Return labelled Typst or LaTeX bodies in source order."""
    source_path = Path(path)
    source = source_path.read_text(encoding="utf-8")
    result: list[tuple[str, str]] = []
    if source_path.suffix.lower() in {".typ", ".typst"}:
        searchable = _mask_typst(source, hide_strings=False)
        structural = _mask_typst(source, hide_strings=True)
        matches = TYPST_SENT.finditer(searchable)
        opening, closing = "[", "]"
    elif source_path.suffix.lower() == ".tex":
        masked = _mask_latex_comments(source)
        labels: set[str] = set()
        for line_number, (line, masked_line) in enumerate(
            zip(source.splitlines(), masked.splitlines(), strict=True), start=1
        ):
            if "\\itag" not in masked_line:
                continue
            markers = list(LATEX_TAG.finditer(masked_line))
            if len(markers) != 1:
                raise ValueError(f"line {line_number}: expected one itag")
            marker = markers[0]
            if masked_line[marker.end():].strip():
                raise ValueError(
                    f"line {line_number}: itag must be at the end of its line"
                )
            label = marker.group(1).strip()
            if not SHORT_ID.fullmatch(label):
                raise ValueError(
                    f"line {line_number}: interlinear tag must be four alphanumeric characters"
                )
            if label in labels:
                raise ValueError(f"line {line_number}: duplicate interlinear tag {label!r}")
            body = line[:marker.start()].strip()
            if not body:
                raise ValueError(
                    f"line {line_number}: itag needs a sentence or clause"
                )
            labels.add(label)
            result.append((label, body))
        return result
    else:
        raise ValueError(f"unsupported source format: {source_path.suffix or '(none)'}")
    for match in matches:
        label = match.group(1).strip()
        if not LABEL.fullmatch(label):
            raise ValueError(f"invalid sent label {label!r}")
        body, _ = _balanced_body(
            source, structural, match.end(), opening, closing, label
        )
        result.append((label, body))
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
