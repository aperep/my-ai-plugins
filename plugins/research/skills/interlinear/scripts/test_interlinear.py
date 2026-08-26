#!/usr/bin/env python3
"""Focused regression tests for the bundled interlinear helpers."""
from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from gap_check import is_proof_step
from interlinear_io import load_csv, parse_sentences, save_csv, tag_set
from validate_interlinear import validate


class InterlinearTests(unittest.TestCase):
    def test_nested_typst_brackets(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.typ"
            path.write_text('#sent("s1")[Ring $k[x]$ and [nested] text.]\n', encoding="utf-8")
            self.assertEqual(parse_sentences(path), [("s1", "Ring $k[x]$ and [nested] text.")])

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


if __name__ == "__main__":
    unittest.main()
