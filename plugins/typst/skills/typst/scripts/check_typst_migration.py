#!/usr/bin/env python3
import re
import sys
from pathlib import Path

LATEX_PATTERNS = {
    r"\\\\usepackage": "LaTeX package import is not valid in Typst",
    r"\\\\documentclass": "LaTeX documentclass is not valid in Typst",
    r"\\\\begin\{": "LaTeX environments should be migrated to Typst constructs",
    r"\\\\end\{": "LaTeX environments should be migrated to Typst constructs",
    r"\\\\cite\{": "Use Typst citations (e.g., @key)",
    r"\\\\ref\{": "Use Typst references (e.g., @label)",
    r"\\\\label\{": "Use Typst labels (<label>)",
    r"\\\\section\{": "Use Typst headings (=, ==, ===)",
}

WARN_PATTERNS = {
    r"\\\\frac\{": "Consider Typst-native math forms (a / b or frac(a,b))",
    r"\\\\textbf\{": "Consider Typst emphasis syntax (*text*)",
    r"\\\\emph\{": "Consider Typst emphasis syntax (_text_)",
}


def scan(text: str):
    errors = []
    warns = []
    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        for pattern, message in LATEX_PATTERNS.items():
            if re.search(pattern, line):
                errors.append((i, message, line.strip()))
        for pattern, message in WARN_PATTERNS.items():
            if re.search(pattern, line):
                warns.append((i, message, line.strip()))
    return errors, warns


def main():
    if len(sys.argv) != 2:
        print("Usage: check_typst_migration.py <file.typ>")
        sys.exit(2)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        sys.exit(2)

    text = path.read_text(encoding="utf-8")
    errors, warns = scan(text)

    for ln, msg, snippet in errors:
        print(f"ERROR L{ln}: {msg}\n  -> {snippet}")

    for ln, msg, snippet in warns:
        print(f"WARN  L{ln}: {msg}\n  -> {snippet}")

    if errors:
        print(f"\nFound {len(errors)} error(s), {len(warns)} warning(s).")
        sys.exit(1)

    print(f"No blocking LaTeX patterns found. Warnings: {len(warns)}")


if __name__ == "__main__":
    main()
