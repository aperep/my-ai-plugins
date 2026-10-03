#!/usr/bin/env python3
"""Focused regression tests for the bundled interlinear helpers."""
from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from gap_check import is_proof_step
from context_dump import build
from interlinear_io import load_csv, parse_sentences, save_csv, tag_set
from validate_interlinear import validate

SCRIPT_DIR = Path(__file__).resolve().parent


class InterlinearTests(unittest.TestCase):
    def test_nested_typst_brackets(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.typ"
            path.write_text('#sent("s1")[Ring $k[x]$ and [nested] text.]\n', encoding="utf-8")
            self.assertEqual(parse_sentences(path), [("s1", "Ring $k[x]$ and [nested] text.")])

    def test_typst_ignores_strings_and_comments(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.typ"
            path.write_text(
                '// #sent("bad")[Comment.]\n'
                '#sent("s1")[Text with "a ] string" and \\] escaped.]\n'
                '/* #sent("bad2")[Block.] */\n',
                encoding="utf-8",
            )
            self.assertEqual(
                parse_sentences(path),
                [("s1", 'Text with "a ] string" and \\] escaped.')],
            )

    def test_latex_line_tags_and_comments(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.tex"
            path.write_text(
                '% Comment.\\itag{nope}\n'
                'Text with \\emph{nested braces} and '
                '\\{literal\\}.\\itag{dJ2z}\n',
                encoding="utf-8",
            )
            self.assertEqual(
                parse_sentences(path),
                [("dJ2z", "Text with \\emph{nested braces} and \\{literal\\}.")],
            )

    def test_latex_tag_must_end_the_line(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.tex"
            path.write_text('First.\\itag{dJ2z} Second.\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "end of its line"):
                parse_sentences(path)

    def test_latex_tag_requires_short_id(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.tex"
            path.write_text('Claim.\\itag{semantic-label}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "four alphanumeric"):
                parse_sentences(path)

    def test_latex_tags_are_unique(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.tex"
            path.write_text(
                'First.\\itag{dJ2z}\nSecond.\\itag{dJ2z}\n',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate interlinear tag"):
                parse_sentences(path)

    def test_atomic_csv_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sentences.csv"
            save_csv(path, ["label", "tags"], [{"label": "s1", "tags": "proof"}])
            self.assertEqual(load_csv(path)[1][0]["label"], "s1")

    def test_exact_proof_tags(self):
        self.assertTrue(is_proof_step("definition;proof"))
        self.assertFalse(is_proof_step("proof-outline"))
        self.assertEqual(tag_set("proof; claim ;"), {"proof", "claim"})

    def test_validation_rejects_backward_span(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "document.typ"
            data = root / "sentences.csv"
            document.write_text('#sent("s1")[One.]\n#sent("s2")[Two.]\n', encoding="utf-8")
            with data.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["label", "active_until"])
                writer.writeheader()
                writer.writerows([
                    {"label": "s1", "active_until": "s2"},
                    {"label": "s2", "active_until": "s1"},
                ])
            self.assertIn("s2: active_until precedes the row", validate(document, data))

    def test_context_filter_uses_span_and_tags(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "document.tex"
            data = root / "sentences.csv"
            document.write_text(
                "Definition one.\\itag{D1a2}\n"
                "Unrelated note.\\itag{A3b4}\n"
                "Proof step.\\itag{P5c6}\n",
                encoding="utf-8",
            )
            with data.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle, fieldnames=["label", "active_until", "tags"]
                )
                writer.writeheader()
                writer.writerows([
                    {
                        "label": "D1a2",
                        "active_until": "P5c6",
                        "tags": "definition;topic:ring",
                    },
                    {
                        "label": "A3b4",
                        "active_until": "P5c6",
                        "tags": "translation",
                    },
                    {"label": "P5c6", "active_until": "", "tags": "proof;topic:ring"},
                ])
            result = build(document, data, {"definition"})
            self.assertEqual(
                [item["label"] for item in result["P5c6"]["context"]],
                ["D1a2"],
            )

    def test_lookup_writes_candidate_not_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "sentences.csv"
            index = root / "index.json"
            with data.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=[
                        "label", "translation_en", "stacks_candidate", "stacks_ref"
                    ],
                )
                writer.writeheader()
                writer.writerow({
                    "label": "s1",
                    "translation_en": "Noetherian polynomial ring Hilbert basis",
                    "stacks_candidate": "",
                    "stacks_ref": "",
                })
            index.write_text(json.dumps({"entries": [{
                "tag": "00FN",
                "title": "Hilbert basis theorem",
                "statement": "A polynomial ring over a Noetherian ring is Noetherian",
                "keywords": "Hilbert basis polynomial Noetherian",
            }]}), encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_DIR / "stack_lookup.py"),
                    "--fill",
                    "--index", str(index),
                    "--data", str(data),
                    "--min-score", "1",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            row = load_csv(data)[1][0]
            self.assertEqual(row["stacks_candidate"], "00FN")
            self.assertEqual(row["stacks_ref"], "")

    def test_checked_lean_requires_evidence_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "document.tex"
            data = root / "sentences.csv"
            document.write_text("Claim.\\itag{C1a2}\n", encoding="utf-8")
            data.write_text("label,lean_status,lean_ref,lean_toolchain\nC1a2,checked,,\n")
            errors = validate(document, data)
            self.assertIn("C1a2: checked Lean status needs lean_ref", errors)
            self.assertIn("C1a2: checked Lean status needs lean_toolchain", errors)


if __name__ == "__main__":
    unittest.main()
