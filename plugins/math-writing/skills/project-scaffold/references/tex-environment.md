---
reviewed: d9f00dd
---

# TeX environment

The academic-workshop prototype used TinyTeX with these TeX Live packages:

```text
cmap cm-super cyrillic babel-russian babel-english thmtools lh extarrows
grfext jknapltx enumitem pgf tikz-cd pgfplots xypic wrapfig cite tocbibind
caption titlesec rsfs
```

Ghostscript was used for EPS-to-PDF conversion.

Treat this as an inventory, not an install script. First check the document's
actual dependencies and the available TeX distribution. Installing TinyTeX,
running a downloaded shell script, or invoking `apt-get` changes the user's
machine and requires explicit authorization. Prefer project-local instructions
and report missing packages before proposing installation.
