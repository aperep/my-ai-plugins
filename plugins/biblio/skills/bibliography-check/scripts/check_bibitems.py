#!/usr/bin/env python3
"""Cross-check LaTeX \\bibitem entries against Semantic Scholar and MathNet.

Usage:
    python3 check_bibitems.py <path-to-tex>
    python3 check_bibitems.py <path-to-tex> --keys Sh66,Is78
    python3 check_bibitems.py - --offline   # read stdin, parse only
    cat tex/bibliography_resume.tex | python3 check_bibitems.py -
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser


SS_BASE = "https://api.semanticscholar.org/graph/v1/paper"
MATHNET_SEARCH = "https://www.mathnet.ru/php/search.phtml"
USER_AGENT = "thesis-bibcheck/1.0 (claude-code skill)"
SLEEP_BETWEEN_QUERIES = 1.5  # be polite


# ---------- parsing ----------

BIBITEM_RE = re.compile(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", re.M)


def split_bibitems(text):
    """Split a tex file into [(key, body), ...] tuples."""
    items = []
    matches = list(BIBITEM_RE.finditer(text))
    for i, m in enumerate(matches):
        key = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        items.append((key, body))
    return items


def strip_tex(s):
    """Remove common TeX commands so the result is searchable."""
    s = re.sub(r"\\emph\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\textit\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\newblock\s*", " ", s)
    s = re.sub(r"\\href\s*\{[^}]*\}\s*\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\path\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\url\{([^}]*)\}", r"\1", s)
    s = s.replace("~", " ").replace("--", "-")
    s = re.sub(r"\\[A-Za-z]+", " ", s)
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_fields(body):
    """Heuristically extract fields from a bibitem body."""
    out = {"raw": body, "stripped": strip_tex(body)}
    # title — first \emph or \textit or {\em ...} or \newblock {\em ...}
    m = (
        re.search(r"\\emph\{([^{}]+)\}", body)
        or re.search(r"\\textit\{([^{}]+)\}", body)
        or re.search(r"\{\\em\s+([^{}]+)\}", body)
    )
    out["title"] = m.group(1).strip() if m else ""
    # volume — first \textbf{NUMBER}
    m = re.search(r"\\textbf\{(\d+)\}", body)
    out["volume"] = m.group(1) if m else ""
    # year — first 4-digit year in parens
    m = re.search(r"\((\d{4})\)", body)
    out["year"] = m.group(1) if m else ""
    # issue — after no.~ or вып.~
    m = re.search(r"(?:no\.|вып\.)\s*~?\s*([0-9-]+)", body)
    out["issue"] = m.group(1) if m else ""
    # pages — prefer A--B (en-dash); fall back to A-B but skip
    # short ranges like "no.~1-2" (issue) by requiring 2+ digits.
    m = re.search(r"(\d+)\s*--\s*(\d+)", body)
    if not m:
        m = re.search(r"(\d{2,})\s*-\s*(\d{2,})", body)
    out["pages"] = f"{m.group(1)}-{m.group(2)}" if m else ""
    # doi
    m = re.search(r"(?:doi[:\s]+|doi\.org/)([\w./()\-]+)", body, re.I)
    out["doi"] = m.group(1).rstrip(".") if m else ""
    # arxiv
    m = re.search(r"arXiv:\s*([0-9]{4}\.[0-9]{4,5})", body)
    out["arxiv"] = m.group(1) if m else ""
    # mathnet hint
    m = re.search(r"mathnet\.ru/[a-z]+/([\w-]+)", body)
    out["mathnet_id"] = m.group(1) if m else ""
    return out


CYRILLIC_RE = re.compile(r"[Ѐ-ӿ]")
RU_VENUE_HINTS = (
    "Изв. АН СССР", "Известия АН", "Матем. сб", "Мат. сб",
    "Мат. зам", "Матем. заметки", "УМН", "Усп. мат",
    "Функц. анал", "Сиб. мат", "Алгебра и анализ",
    "Изв. РАН", "ТМФ", "Math. USSR",  # Math. USSR-* are translations of Russian originals
)


def is_russian_origin(parsed):
    """Heuristic: should this be checked against MathNet first?"""
    raw = parsed["raw"]
    if CYRILLIC_RE.search(raw):
        return True
    return any(h in raw for h in RU_VENUE_HINTS)


# ---------- Semantic Scholar ----------

def http_get(url, accept_json=True):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return None, str(e)
    if accept_json:
        try:
            return json.loads(data), None
        except Exception as e:
            return None, f"json decode: {e}"
    return data, None


def ss_lookup(parsed):
    """Try Semantic Scholar by DOI, arXiv, or title."""
    fields = "title,authors,year,venue,externalIds"
    if parsed["doi"]:
        url = f"{SS_BASE}/DOI:{urllib.parse.quote(parsed['doi'], safe='')}?fields={fields}"
        data, err = http_get(url)
        if data and "title" in data:
            return [data], "doi"
    if parsed["arxiv"]:
        url = f"{SS_BASE}/arXiv:{parsed['arxiv']}?fields={fields}"
        data, err = http_get(url)
        if data and "title" in data:
            return [data], "arxiv"
    if parsed["title"]:
        q = urllib.parse.quote(strip_tex(parsed["title"])[:120])
        url = f"{SS_BASE}/search?query={q}&limit=3&fields={fields}"
        data, err = http_get(url)
        if data and isinstance(data.get("data"), list) and data["data"]:
            return data["data"], "title"
    return [], "miss"


# ---------- MathNet ----------

class MathNetResultParser(HTMLParser):
    """Pull '/rus/<slug>' result links from a search page."""
    def __init__(self):
        super().__init__()
        self.hits = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for k, v in attrs:
            if k == "href" and v and re.match(r"^/rus/[a-z]+\d+$", v):
                if v not in self.hits:
                    self.hits.append(v)


def mathnet_search(query):
    """Submit a title to MathNet and return up to 3 result paths."""
    body = urllib.parse.urlencode({
        "wshow": "search",
        "option_lang": "rus",
        "query": query,
    }).encode()
    req = urllib.request.Request(
        MATHNET_SEARCH,
        data=body,
        headers={"User-Agent": USER_AGENT,
                 "Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return [], str(e)
    p = MathNetResultParser()
    p.feed(html)
    return p.hits[:3], None


def mathnet_fetch(slug):
    """Fetch a record page; return raw HTML for caller to inspect."""
    url = f"https://www.mathnet.ru{slug}" if slug.startswith("/") else slug
    html, err = http_get(url, accept_json=False)
    return url, html, err


# ---------- compare ----------

SKIP_KEYS = ("Sage20",)  # software/preprint hints; expand as needed


def compare(parsed, ss_hits, ss_kind, mn_hits):
    """Build a compact status report."""
    notes = []
    status = "OK"

    if not ss_hits and not mn_hits:
        return "MISS", ["no source matched; verify manually"]

    if ss_hits:
        cand = ss_hits[0]
        ss_year = cand.get("year")
        if parsed["year"] and ss_year and str(ss_year) != parsed["year"]:
            status = "MAJOR"
            notes.append(f"year: bib={parsed['year']} ss={ss_year}")
        ss_title = (cand.get("title") or "").lower()
        if parsed["title"] and ss_title:
            shared = set(re.findall(r"[a-z]{4,}", strip_tex(parsed["title"]).lower()))
            ss_words = set(re.findall(r"[a-z]{4,}", ss_title))
            if shared and ss_words and len(shared & ss_words) < min(2, len(shared)):
                status = "MAJOR" if status == "OK" else status
                notes.append(f"title: bib≈\"{parsed['title'][:60]}\" ss≈\"{cand.get('title','')[:60]}\"")
        ss_doi = (cand.get("externalIds") or {}).get("DOI")
        if ss_doi and not parsed["doi"]:
            notes.append(f"missing DOI: {ss_doi}")
            status = "MINOR" if status == "OK" else status

    if mn_hits:
        notes.append(f"mathnet hit(s): {', '.join(mn_hits)}")

    return status, notes


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="path to .tex file or '-' for stdin")
    ap.add_argument("--keys", help="comma-separated subset of bibkeys")
    ap.add_argument("--offline", action="store_true", help="parse only")
    ap.add_argument("--limit", type=int, default=0,
                    help="max bibitems to query (0 = no limit)")
    args = ap.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
    else:
        text = open(args.path, encoding="utf-8").read()

    items = split_bibitems(text)
    if args.keys:
        wanted = {k.strip() for k in args.keys.split(",")}
        items = [(k, b) for k, b in items if k in wanted]

    queried = 0
    for key, body in items:
        parsed = parse_fields(body)
        head = f"[{key}]"
        if key in SKIP_KEYS:
            print(f"{head} skipped (software/special)")
            continue
        meta = (
            f"{parsed.get('title','?')[:80] or '?'} | "
            f"vol={parsed.get('volume') or '-'} "
            f"year={parsed.get('year') or '-'} "
            f"no={parsed.get('issue') or '-'} "
            f"pp={parsed.get('pages') or '-'} "
            f"doi={parsed.get('doi') or '-'}"
        )
        if args.offline:
            print(f"{head} parsed-only\n  {meta}")
            continue

        ru_first = is_russian_origin(parsed)
        ss_hits, ss_kind = [], "skip"
        mn_hits, mn_err = [], None
        if ru_first:
            slugs, mn_err = mathnet_search(strip_tex(parsed["title"])[:120])
            mn_hits = slugs or []
            time.sleep(SLEEP_BETWEEN_QUERIES)
        ss_hits, ss_kind = ss_lookup(parsed)
        time.sleep(SLEEP_BETWEEN_QUERIES)
        if not ru_first and not mn_hits:
            slugs, mn_err = mathnet_search(strip_tex(parsed["title"])[:120])
            mn_hits = slugs or []
            time.sleep(SLEEP_BETWEEN_QUERIES)

        status, notes = compare(parsed, ss_hits, ss_kind, mn_hits)
        print(f"{head} {status}")
        print(f"  parsed: {meta}")
        if ss_hits:
            top = ss_hits[0]
            ext = top.get("externalIds") or {}
            print(f"  ss[{ss_kind}]: \"{(top.get('title') or '')[:80]}\""
                  f" venue=\"{(top.get('venue') or '')[:60]}\""
                  f" year={top.get('year','-')}"
                  f" doi={ext.get('DOI','-')}"
                  f" id={top.get('paperId','-')}")
        else:
            print(f"  ss: miss")
        if mn_hits:
            print(f"  mathnet: {', '.join('https://www.mathnet.ru'+s for s in mn_hits)}")
        elif mn_err:
            print(f"  mathnet: error ({mn_err})")
        else:
            print(f"  mathnet: miss")
        for n in notes:
            print(f"    - {n}")
        queried += 1
        if args.limit and queried >= args.limit:
            break


if __name__ == "__main__":
    main()
