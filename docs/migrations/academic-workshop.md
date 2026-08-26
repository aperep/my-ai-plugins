# Academic workshop migration

Source: `/home/sage/texlab/academic-workshop` at commit `b0ac1eb`.

The useful authored material was distributed by responsibility:

- interlinear research mechanics and the Noetherian fixture: `research`;
- Typst note/slide templates and HSE logo: `typst`;
- LaTeX project scaffold and TeX package inventory: `math-writing`;
- the original TinyTeX installer became a reviewed package inventory rather than an executable remote-installer pipeline;
- personal bibliography corpora: `biblio`;
- the useful three-skill research plan: `docs/ROADMAP.md`.

The migration intentionally excludes generated PDFs, TeX build output, Python
caches, duplicate root copies of the Typst templates, and project-local Claude
configuration. The latter referred to the former `latex` plugin name and an
older marketplace repository; current consumer configuration lives in
`docs/consumer-snippets.md`.

The speculative omnibus roadmap was later removed. It mixed implemented
features, possible external dependencies, and abandoned names without marking
their status.
