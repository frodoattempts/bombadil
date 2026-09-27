#!/usr/bin/env python3
"""Consistency checks for the review paper.

  python3 tools/check_paper.py            # offline checks + merge bibliography
  python3 tools/check_paper.py --online   # also resolve every DOI / arXiv ID

Offline:
  * merges research/bib/*.bib into paper/refs.bib (dedup by key; flags
    conflicting duplicates and the same DOI/eprint under different keys)
  * every \\cite key in paper/**/*.tex exists in the bibliography
  * every cited key is backed by at least one claim in research/ledgers/
  * no UNVERIFIED claim's source is cited only via UNVERIFIED claims
  * every bib entry has a doi, eprint, url or isbn
Online:
  * DOIs resolve on Crossref and titles match; arXiv IDs resolve and titles match
"""
import difflib
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.I)
CITE_RE = re.compile(r"\\(?:cite|citep|citet|citealt|citeauthor|citeyear|nocite)\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
UA = {"User-Agent": "bombadil-paper-check/0.1"}


def split_entries(text):
    """Yield (type, key, body) for each BibTeX entry, balancing braces."""
    pos = 0
    while True:
        m = ENTRY_RE.search(text, pos)
        if not m:
            return
        depth, i = 0, text.index("{", m.start())
        for j in range(i, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
        yield m.group(1).lower(), m.group(2), text[m.start():j + 1]
        pos = j + 1


def field(body, name):
    m = re.search(r"\b" + name + r"\s*=\s*[{\"](.+?)[}\"]\s*,?\s*\n", body, re.I | re.S)
    return re.sub(r"[{}\s]+", " ", m.group(1)).strip() if m else None


def norm(s):
    s = re.sub(r"<[^>]+>", " ", s or "")                       # MathML / HTML tags
    s = re.sub(r"\\(texttimes|times|,|;|!|mathrm|rm|text)", " ", s)  # LaTeX spacing/markup
    s = s.replace("\u2019", "'").replace("\u00d7", " ")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def load_bib():
    entries, problems = {}, []
    for path in sorted(glob.glob(os.path.join(ROOT, "research/bib/*.bib"))):
        for typ, key, body in split_entries(open(path, encoding="utf-8").read()):
            if typ in ("comment", "string", "preamble"):
                continue
            src = os.path.basename(path)
            if key in entries:
                old = entries[key]
                if norm(field(old["body"], "title")) != norm(field(body, "title")):
                    problems.append(f"key {key}: conflicting titles in {old['src']} and {src}")
                continue
            entries[key] = {"type": typ, "body": body, "src": src}
    by_id = {}
    for key, e in entries.items():
        for f in ("doi", "eprint"):
            v = field(e["body"], f)
            if v:
                by_id.setdefault((f, v.lower()), []).append(key)
        if not (any(field(e["body"], f) for f in ("doi", "eprint", "url", "isbn"))
                or re.search(r"\\url\{|\bdoi:?\s*10\.", e["body"], re.I)
                # pre-DOI works: a complete journal or proceedings citation suffices
                or (all(field(e["body"], f) for f in ("volume", "pages")) and field(e["body"], "journal"))
                or all(field(e["body"], f) for f in ("booktitle", "publisher", "pages"))):
            problems.append(f"key {key} ({e['src']}): no doi/eprint/url/isbn")
    for (f, v), keys in by_id.items():
        if len(keys) > 1:
            problems.append(f"same {f} {v} under keys {keys}")
    return entries, problems


def load_ledgers():
    claims = []
    for path in sorted(glob.glob(os.path.join(ROOT, "research/ledgers/*.md"))):
        for block in re.split(r"\n(?=### C-)", open(path, encoding="utf-8").read()):
            m = re.match(r"### (C-[\w-]+)", block)
            if not m:
                continue
            src = re.search(r"-\s*Source:\s*(.+)", block)
            ver = re.search(r"-\s*Verified:\s*([A-Z]+)", block)
            keys = re.findall(r"[A-Za-z][\w:.-]*\d{4}[\w-]*", src.group(1)) if src else []
            claims.append({"id": m.group(1), "keys": keys,
                           "verified": ver.group(1) if ver else "MISSING",
                           "file": os.path.basename(path)})
    return claims


def cited_keys():
    cites = {}
    for path in glob.glob(os.path.join(ROOT, "paper/**/*.tex"), recursive=True):
        for m in CITE_RE.finditer(open(path, encoding="utf-8").read()):
            for k in m.group(1).split(","):
                if k.strip():
                    cites.setdefault(k.strip(), set()).add(os.path.relpath(path, ROOT))
    return cites


def fetch_json(url, tries=5):
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == tries - 1:
                raise
        except urllib.error.URLError:
            if attempt == tries - 1:
                raise
        time.sleep(2 ** attempt)


def online_check(entries):
    bad = []
    for key, e in sorted(entries.items()):
        if field(e["body"], "titlecheck"):   # documented, legitimate title difference
            continue
        title = field(e["body"], "title")
        doi, eprint = field(e["body"], "doi"), field(e["body"], "eprint")
        try:
            if doi:
                try:
                    msg = fetch_json("https://api.crossref.org/works/" + urllib.request.quote(doi))["message"]
                    remote = (msg.get("title") or [""])[0]
                except urllib.error.HTTPError as exc:
                    if exc.code != 404:
                        raise
                    # not a Crossref DOI (e.g. DataCite/Zenodo): check it is registered, skip title match
                    h = fetch_json("https://doi.org/api/handles/" + doi)
                    if h.get("responseCode") != 1:
                        raise RuntimeError("DOI not registered")
                    continue
            elif eprint and re.match(r"^(\d{4}\.\d{4,5}|[a-z-]+(\.[A-Z]{2})?/\d{7})", eprint):
                html = urllib.request.urlopen(urllib.request.Request(
                    "https://arxiv.org/abs/" + eprint, headers=UA), timeout=30).read().decode("utf-8", "replace")
                m = re.search(r'<meta name="citation_title" content="([^"]+)"', html)
                remote = m.group(1) if m else ""
            else:
                continue
        except Exception as exc:  # noqa: BLE001 - report and move on
            bad.append(f"{key}: lookup failed ({exc})")
            continue
        ratio = difflib.SequenceMatcher(None, norm(title), norm(remote)).ratio()
        if ratio < 0.8:
            bad.append(f"{key}: title mismatch ({ratio:.2f})\n    bib:    {title}\n    remote: {remote}")
    return bad


def main():
    entries, problems = load_bib()
    claims = load_ledgers()
    cites = cited_keys()

    with open(os.path.join(ROOT, "paper/refs.bib"), "w", encoding="utf-8") as out:
        out.write("% AUTO-GENERATED by tools/check_paper.py from research/bib/*.bib -- do not edit\n\n")
        for key in sorted(entries):
            out.write(entries[key]["body"].strip() + "\n\n")

    verified_keys, levels = set(), {}
    for c in claims:
        levels[c["verified"]] = levels.get(c["verified"], 0) + 1
        if c["verified"] in ("FULLTEXT", "ABSTRACT", "METADATA"):
            verified_keys.update(c["keys"])

    for key, files in sorted(cites.items()):
        if key not in entries:
            problems.append(f"cited but not in bibliography: {key} ({', '.join(sorted(files))})")
        elif key not in verified_keys:
            problems.append(f"cited but no verified ledger claim: {key} ({', '.join(sorted(files))})")

    print(f"bibliography: {len(entries)} entries -> paper/refs.bib")
    print(f"ledger claims: {len(claims)}  " + "  ".join(f"{k}={v}" for k, v in sorted(levels.items())))
    print(f"cited keys: {len(cites)}   uncited bib entries: {len(set(entries) - set(cites))}")

    if "--online" in sys.argv:
        problems += online_check(entries)

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print("\nall checks passed")


if __name__ == "__main__":
    main()
