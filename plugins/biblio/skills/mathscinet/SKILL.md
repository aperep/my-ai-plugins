---
name: mathscinet
description: Fetch MathSciNet (MR) numbers for mathematical papers. Use when creating biblio notes and the msnumber field needs to be filled. Requires institutional MathSciNet access.
---

# MathSciNet Skill

Retrieve the MathSciNet review number (MR number) for a paper using the user's institutional library proxy.

## Prerequisites

Provide these environment variables to the active client or shell without
committing their values:

- `MATHSCINET_PROXY` — your institution's proxy URL, for example `http://proxy.example.org:3128`
- `MATHSCINET_PROXY_USER` — proxy username
- `MATHSCINET_PROXY_PASS` — proxy password

**Network requirement:** use the network or VPN required by your institution.
Obtain the real proxy URL and credentials from your library; the example URL
is a placeholder. If access is not configured or a lookup times out, report
the reason and leave `msnumber: ""`.

---

## Workflow

### Step 1 — Build the search URL

Use the MathSciNet HTML search endpoint, filtering by title and year:

```
https://mathscinet.ams.org/mathscinet/search/publications.html
  ?pg1=TI&s1=<url-encoded-title>
  &dr=pubyear&yearRangeFirst=<year>&yearRangeSecond=<year>&yrop=eq
```

### Step 2 — Run the search via proxy

```bash
TITLE="Exact paper title here"
YEAR="2024"
TITLE_ENC=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$TITLE")

curl -s --max-time 30 \
  -x "$MATHSCINET_PROXY" \
  -U "${MATHSCINET_PROXY_USER}:${MATHSCINET_PROXY_PASS}" \
  "https://mathscinet.ams.org/mathscinet/search/publications.html?pg1=TI&s1=${TITLE_ENC}&dr=pubyear&yearRangeFirst=${YEAR}&yearRangeSecond=${YEAR}&yrop=eq" \
  -o /tmp/msn_result.html
```

### Step 3 — Extract MR numbers

```bash
python3 - <<'EOF'
import re

with open("/tmp/msn_result.html") as f:
    html = f.read()

# MR numbers appear as MR followed by 6-10 digits
mrs = re.findall(r'MR(\d{4,10})', html)
unique = list(dict.fromkeys(mrs))  # deduplicate, preserve order
for mr in unique[:5]:
    print(f"MR{mr}")
EOF
```

### Step 4 — Verify and select

If multiple MR numbers are found, also extract the titles of matching results and compare against the target title:

```bash
python3 - <<'EOF'
import re

with open("/tmp/msn_result.html") as f:
    html = f.read()

# Extract (title_text, mr_number) pairs from result rows
# MathSciNet search results have structure:
#   <div class="headline"> ... MRxxxx ... title text ...
items = re.findall(
    r'MR(\d{4,10}).*?<span[^>]*class="title"[^>]*>(.*?)</span>',
    html, re.DOTALL
)
for mr, title in items[:5]:
    print(f"MR{mr}  |  {re.sub('<[^>]+>', '', title).strip()}")
EOF
```

Pick the MR number whose title matches the target paper exactly (case-insensitive, ignoring punctuation differences). If no match, set `msnumber: ""`.

### Step 5 — Fallback: broader search

If the year-filtered search returns nothing (paper year may differ from publication year, e.g. preprint vs. journal), retry without the year filter:

```bash
curl -s --max-time 30 \
  -x "$MATHSCINET_PROXY" \
  -U "${MATHSCINET_PROXY_USER}:${MATHSCINET_PROXY_PASS}" \
  "https://mathscinet.ams.org/mathscinet/search/publications.html?pg1=TI&s1=${TITLE_ENC}" \
  -o /tmp/msn_result.html
```

Then re-run Step 3–4.

---

## Output

The `msnumber` frontmatter field takes the form `MR` followed by digits, no spaces:

```yaml
msnumber: "MR4234567"
```

If the paper is not in MathSciNet (preprints often aren't), or if the proxy is unreachable, leave:

```yaml
msnumber: ""
```

and note the reason in the report.

---

## MR Number Format

MathSciNet assigns a unique MR number to each reviewed item:
- Format: `MR` + 7 digits (older items may have fewer), e.g. `MR1234567`, `MR4750823`
- Preprints / arXiv-only papers typically have no MR number until published and reviewed
- The MR number links to: `https://mathscinet.ams.org/mathscinet-getitem?mr=<digits>`
