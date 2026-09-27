# Research conventions for the bombadil review paper

The target is a review paper for arXiv and OpenReview. Expert referees in
philosophy of physics, quantum gravity phenomenology, astroparticle physics,
and computational complexity will read it. **Every factual statement must be
traceable to a source that we actually read.** Tone: sober, precise,
non-sensational. We do not advocate the simulation hypothesis. We map claims,
tests, constraints and critiques.

## 1. Deliverables per topic (NN = topic number, slug = short name)

| File | Content |
|---|---|
| `research/ledgers/NN-slug.md` | **Claim ledger** (format below). The ground truth. |
| `research/bib/NN-slug.bib` | BibTeX for every cited work, generated from DOI/INSPIRE/arXiv metadata, never typed from memory. |
| `paper/sections/NN-slug.tex` | Draft LaTeX section built only from ledger claims, citing with `\cite{key}`. |
| `research/notes/NN-slug-report.md` | A short report: coverage, gaps, controversies, anything that could embarrass us, suggested cross-links to other sections. |

Do **not** git commit. Only write inside your own topic's files. Never
edit another topic's files.

## 2. Claim ledger format

One entry per atomic claim that the section makes about the literature:

```
### C-NN-001
- Claim: <one sentence, as it will appear (paraphrased) in the paper>
- Source: <bibkey>
- Locator: <section / equation / page / figure / table in the source>
- Evidence: "<short verbatim quote from the source supporting the claim>"
- Verified: FULLTEXT | ABSTRACT | METADATA | UNVERIFIED
- Notes: <caveats, e.g. "number is a 95% CL lower limit", "claim disputed by X">
```

- `FULLTEXT`: you read the relevant passage in the paper itself (arXiv PDF,
  open-access publisher HTML/PDF). Required for **every numerical value**
  and every characterization of what a paper argues or concludes.
- `ABSTRACT`: supported by the official abstract only. Acceptable for
  high-level "X proposed Y" statements.
- `METADATA`: the existence and bibliographic data only.
- `UNVERIFIED`: you could not check it. Such claims **must not** appear in the
  `.tex` draft. List them in the report instead.

## 3. Bibliography rules

- BibTeX keys: `LastnameYYYYfirstword`, lowercase first word of the title,
  skipping articles (e.g. `Bostrom2003are`, `Beane2014constraints`,
  `PierreAuger2017observation` for collaborations). Keeping keys consistent
  lets us merge bib files across topics without collisions.
- Sources for BibTeX, in order of preference:
  1. INSPIRE-HEP: `https://inspirehep.net/api/literature?q=arxiv:XXXX.XXXXX&format=bibtex` or `q=doi:...`
  2. DOI content negotiation: `curl -sL -H "Accept: application/x-bibtex" https://doi.org/<DOI>`
  3. Crossref: `https://api.crossref.org/works/<DOI>`
  4. arXiv listing page for preprints.
  Afterwards, rewrite the key to our convention. Keep `doi` and `eprint`
  fields where available.
- Include the arXiv ID (`eprint`, `archivePrefix = {arXiv}`) whenever one
  exists, and the DOI whenever one exists.
- Books: cite the edition you are describing. Blog posts and videos are allowed
  only where the argument itself is the object of study (e.g. a
  widely discussed critique); mark them `@misc` with a URL and access date.
- **Never cite press releases or news articles as evidence for a scientific
  claim.** They may be cited only where the paper discusses *how a result was
  reported*.

## 4. Reading the sources

- arXiv PDFs: `curl -sL -o /tmp/claude-0/papers/<id>.pdf https://arxiv.org/pdf/<id>`
  then `pdftotext -layout file.pdf -` (poppler is installed; `pypdf` and
  `pdfminer.six` are available in Python). The arXiv API host
  (`export.arxiv.org`) rejects requests, so use the abs/pdf pages on `arxiv.org`.
- Where the published version differs from the arXiv version and matters (e.g.
  a number changed), note it in the ledger.
- Semantic Scholar API rate-limits (429). PhilPapers blocks automated access
  (403); for philosophy papers use the publisher (OUP, Springer, JSTOR landing
  pages), author-hosted PDFs, or PhilArchive mirrors if reachable.
- Follow citation trails: check the papers that cite the key works (INSPIRE
  `refersto:` queries are ideal for physics). Surveys that miss important
  follow-ups are what reviewers mock.

## 5. Writing rules for the `.tex` drafts

- LaTeX only, no preamble; start with `\section{...}`. Use `\label{sec:slug}`.
- State what each paper *assumes*, what it *derives*, and its *limitations*.
  Distinguish proposals from performed experiments, and bounds from detections.
- Give numbers with their confidence level and units, exactly as in the source.
- Attribute critiques precisely. "It has been argued" is not allowed without a
  citation.
- Where literature is thin or absent, say so carefully ("we are not aware of…"),
  and record in the report the search you performed to back that up (databases
  and queries).
- Avoid rhetorical flourish, avoid "prove/disprove the simulation hypothesis"
  language unless quoting.
