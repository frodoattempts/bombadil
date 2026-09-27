# Report: 02-digital-physics

Section: `paper/sections/02-digital-physics.tex` (`\label{sec:digital-physics}`).
Ledger: `research/ledgers/02-digital-physics.md`, 58 claims.
Bib: `research/bib/02-digital-physics.bib`, 37 entries. Every entry is cited
in the tex and every citation resolves. The section compiles cleanly with
pdflatex and bibtex, with no undefined citations. It runs to about 2,500
words plus one table, roughly 2.5–3 pages in a two-column layout.

## 1. Coverage

| Level | Claims |
|---|---|
| FULLTEXT | 48, plus 1 mixed (Tegmark 2008 FULLTEXT / Tegmark 1998 ABSTRACT) |
| ABSTRACT | 3 (Lloyd 2005 preprint; Gorard 2020 relativistic; Gorard 2020 causal sets) |
| METADATA | 6 (Zuse 1967/1969/1970; Fredkin 1990/2003; Toffoli 1984; the 1982 IJTP issue; Sdrolia & Bishop; Moravec 1988 / Tipler 1994) |
| UNVERIFIED | 0 in the ledger. See §2 for items kept out of the tex. |

Primary texts read in full, or in the relevant passages:
- Feynman 1982
- Fredkin & Toffoli 1982 (course-hosted copy)
- Deutsch 1985 (van Dam's LaTeX re-edition on Deutsch's site)
- Wheeler "it from bit" (reprint of the Tokyo proceedings)
- Lloyd 2000 and 2002 (arXiv)
- Wolfram NKS pp. 465 and 1026 (publisher's online edition)
- Wolfram 2020 §8 (arXiv)
- Gorard 2020 (abstract)
- Aaronson 2002 review (arXiv)
- Kadanoff 2002 review (publisher HTML)
- Weinberg 2002 NYRB review (publisher HTML)
- 't Hooft CAI (arXiv v3)
- Tegmark 2008 (arXiv)
- Schmidhuber 1997 and 2000 (arXiv)
- Szudzik (arXiv)
- SEP "Computation in Physical Systems" (revision of 20 Aug 2025)
- Floridi 2009 (accepted manuscript from the UHRA repository)
- Butterfield & Dowker (arXiv v1)
- Moravec 1992 (author-hosted)
- Bostrom 2003 (preprint cached in the shared papers dir)

## 2. Items we could not verify (kept out of the tex, or cited only via secondary sources)

- **Zuse 1967 / 1969 / 1970 (text).** We could not open any version:
  - The IDSIA ftp scans are gone and the http mirrors return 404.
  - The Wayback fetches failed (429 errors, and tunnels closed mid-exchange).
  - PhilPapers/PhilArchive (German & Zenil LaTeX edition), mathrix.org and Springer are blocked.

  **All characterizations of Zuse in the tex are attributed to the SEP entry
  or to Floridi.** Floridi's "Zuse Thesis" wording ("deterministically computed
  on some sort of giant but discrete computer") is attributed to Zuse (1969).
  We could not confirm it is a quotation rather than a paraphrase. Wolfram's
  NKS note says Zuse proposed a *continuous* cellular automaton. That is also
  unchecked and is left out of the tex. If someone can get the MIT translation
  (or the 2012 World Scientific reprint, doi:10.1142/9789814374309_0036), check:
  (a) whether Zuse says the universe *is* computed or only asks what a fully
  discretized physics would look like (Schmidhuber's web page says the latter
  for the 1967 paper); (b) the CA and relativity discussion.
- **Fredkin 1990 (Physica D) and Fredkin 2003 (IJTP).** Both closed access, with
  no repository copy. We use Floridi's quotations of Fredkin 2003 (pp. 190–191)
  and the SEP's reading of Fredkin 2003, p. 193 (the "simulation in another
  universe" option). Both are attributed as secondary. A 209-page Fredkin
  manuscript "Digital Mechanics" (2000) circulates online, marked "Working Draft
  – Do not Circulate". **Do not cite it.**
- **Toffoli 1984.** Title only.
- **Zuse 1982 and Wheeler 1982 (IJTP 21(6–7)).** Metadata only. The name of the
  1981 MIT conference (commonly "Physics of Computation", Endicott House) is
  *not* verified, so the tex does not name it.
- **Wheeler's "it from bit" in the Zurek volume (pp. 3–28).** We read a reprint
  (labelled chapter 19 of an unidentified edited volume) that says it reproduces
  Proc. 3rd Int. Symp. Found. QM, Tokyo 1989, pp. 354–368. The bib entry
  therefore points to the Tokyo proceedings, with the Zurek volume in `note`.
  - Publication year 1990 is from secondary sources; INSPIRE says 1989.
  - The Zurek pagination (3–28) is from web search and is consistent with
    Floridi quoting "p. 5".
  - If the lead prefers the Zurek version as the canonical citation, change the
    booktitle but keep the key.
- **Lloyd, *Programming the Universe* (2006); Moravec, *Mind Children* (1988);
  Tipler, *The Physics of Immortality* (1994).** Metadata only (OpenLibrary). The
  tex says nothing about their content beyond:
  - the SEP's classification of Lloyd 2006;
  - Bostrom's citation of Moravec;
  - Tegmark's listing of Tipler.
- **Moravec, "Pigs in Cyberspace".** The text was read on Moravec's CMU page
  (dated 1992). Its original print venue is not verified; it is cited as an
  author-hosted essay.
- **Butterfield & Dowker.** Published in *Philosophy of Physics* 2(1):5 (2024).
  We read only arXiv v1 (2021) because the publisher host is blocked. The quoted
  passage mentioning the Wolfram model should be re-checked in the published
  version.
- **Gorard 2020 (both papers).** Abstract only. We did not check the proofs or
  their assumptions. Gorard's companion "Some Quantum Mechanical Properties of
  the Wolfram Model" (Complex Systems 29(2):537–598) is not cited. Its key would
  collide with `Gorard2020some`; use `Gorard2020somea` or similar if another
  section needs it.
- **Tegmark 1998.** Abstract only.

## 3. Searches performed

- **arXiv PDFs fetched:** quant-ph/0110141, quant-ph/9908043, 2004.08210,
  2004.14810, 2011.12174, quant-ph/0206089, 1405.1548, 0704.0646, gr-qc/9704009,
  quant-ph/9904050, quant-ph/0011122, quant-ph/0501135, 1003.5831, 2106.01297.
- **INSPIRE:**
  - bibtex by arXiv ID.
  - `refersto:recid:1791702` (Wolfram 2020; 34 citing records).
  - `refersto:recid:1793601` (Gorard 2020; 27 records).
  - `refersto:recid:2976809` (Aaronson review; 2 records, both by Aaronson).
  - The combination Aaronson AND Wolfram 2020: 0 records.

  This is the basis for the tex statement that we found no published analysis
  of whether Aaronson's 2002 Bell/causal-invariance argument applies to the 2020
  multiway models. INSPIRE covers the QIC review poorly, so treat this as weak
  evidence of absence.
- **Crossref, doi.org and OpenAlex:** metadata and abstracts for all DOIs. OpenAlex
  and Unpaywall report Fredkin 2003, Fredkin 1990, Toffoli 1984 and Zuse 1982 as
  closed access with no repository copy.
- **Web searches:**
  - PDFs of Zuse's *Calculating Space*, Fredkin 2003, Fredkin & Toffoli 1982,
    Wheeler 1990, Deutsch 1985 and Floridi 2009.
  - "Szudzik computable universe hypothesis".
  - zuse.zib.de. The Konrad Zuse Internet Archive has the 1966–67 manuscripts,
    but not as text.
- **Blocked or failed hosts:** philpapers.org, philarchive.org (Cloudflare),
  link.springer.com, mathrix.org, scilit, ADS (captcha), philosophyofphysics.lse.ac.uk,
  ftp.idsia.ch, and web.archive.org (intermittent 429 errors / tunnel closures).
  Semantic Scholar returned 429.

## 4. Controversies and things that could embarrass us

1. **The "Church–Turing–Deutsch principle" label.** Deutsch's paper calls it
   "the Church–Turing principle". The tex uses Deutsch's own name for it and
   notes this. The SEP lists Deutsch 1985 under "Any physical process can be
   simulated by some TM". But Deutsch explicitly says the Turing machine *cannot*
   perfectly simulate classical continuum systems, and appeals to a universal
   *quantum* computer. Do not repeat the SEP's gloss.
2. **Floridi's "run out of memory" argument.** Floridi quotes a *news article*
   (Ball 2002) that contrasts Lloyd's 10^90 bits with "around 10^80 elementary
   particles". This conflates entropy-bounded bit counts with particle number.
   We did not use it, and the tex should not.
3. **Wheeler is not a digital-physics or simulation author in the relevant
   sense.** He explicitly rejects "universe as machine". Other sections (e.g.
   01) should not cite "it from bit" as support for a computational or
   simulated universe.
4. **Fredkin's simulation remark.** The tex has it only via the SEP's reading of
   Fredkin 2003, p. 193. It is attributed as such.
5. **Wolfram 2020 venue.** *Complex Systems* is the venue for both Wolfram 2020
   and Gorard 2020, and Crossref lists its publisher as "Wolfram Research, Inc."
   We did not put this in the tex; the lead may decide whether it is worth a
   neutral footnote. No independent peer-reviewed technical critique of the 2020
   models turned up in our INSPIRE citation trail. What we found:
   - Butterfield & Dowker list the model as "to be assessed".
   - Most citing papers are by Gorard and collaborators or are sympathetic.

   The tex says only what Wolfram's own paper says, namely that predictions are
   prospective.
6. **Schmidhuber's beta-decay prediction.** It is quoted as a prediction derived
   from his speed prior. We found no experimental test of it and made no claim
   about one.
7. **Two sentences in the tex's final subsection are our own inferences, and are
   flagged as such in the text.** They are: "Nothing in (S) as such fixes a
   lattice representation", and "their bearing on (S) depends on extra
   assumptions". A philosophy-of-physics referee should accept them.
8. **Bib quirks.** These are documented in the bib `note` fields.
   - INSPIRE's 't Hooft record has year 2006; it should be 2016. Fixed in our entry.
   - Crossref dates Floridi to 2008 (online); we use volume year 2009.
   - Sdrolia & Bishop: online 2013, volume year 2014.
   - Butterfield & Dowker author order differs: arXiv lists Dowker first; the
     journal and PDF list Butterfield first. We follow the journal.
   - Aaronson key follows the arXiv/INSPIRE title ("Book Review: …"). The
     published title differs.

## 5. Suggested cross-links

- **01 (philosophy / simulation argument):**
  - Table 1 and the (C)/(CU)/(D)/(P)/(M)/(S) taxonomy, which section 01 could reuse.
  - The SEP's three readings of computational ontology (simulation vs.
    Pythagorean vs. structuralist).
  - Tegmark's "time misconception" and Schmidhuber's "local time" point, relevant
    to rendering and cost arguments.
  - Moravec 1992 as an informal precursor of the counting argument in Bostrom 2003.
  - Bostrom's footnotes citing Lloyd 2000 and Moravec.
- **03 (lattice / Lorentz violation):**
  - Feynman 1982 p. 468: a simple lattice makes *c* direction-dependent, with
    experimentally constrained anisotropies. This is the earliest statement we
    found of the lattice-anisotropy test.
  - Wolfram 2020 §8.20: the elementary length need not equal the Planck length.
  - Gorard's discrete Lorentz covariance (abstract only).
  - Butterfield & Dowker: a Planck-discrete theory recovering GR needs causal
    sets. Link this to any causal-set / Lorentz-invariant discreteness discussion
    in 03.
- **06 (complexity / computability):**
  - Deutsch's physical Church–Turing principle.
  - Lloyd's bounds (~10^120 ops on ~10^90 bits) as lower bounds on the cost of a
    direct quantum simulation.
  - 't Hooft's CAI prediction that quantum computers will not beat a Planck-scale
    classical computer.
  - Tegmark's exact vs. approximate computability (his footnote 14) and CUH
    challenges.
  - Szudzik's formal computable universe hypothesis.
  - Feynman 1982 on complexity (not covered here).
  - Pour-El & Richards (non-computable wave-equation solutions): not covered
    here; the SEP §4 cites them.
- To wire the cross-references, replace the four `% TODO(xref)` comments in the
  tex with `\ref`s once the other sections' labels are known.
