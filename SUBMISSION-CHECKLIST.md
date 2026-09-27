# Pre-submission checklist

Status of the review paper `paper/main.tex`. Items marked **[human]** need a
person, or database access that automated agents here did not have.

## Automated checks (re-run before every submission)
- [x] `python3 tools/check_paper.py`: every `\cite` is in the bibliography and
      backed by a verified ledger claim.
- [x] `python3 tools/check_paper.py --online`: every DOI and arXiv ID resolves
      and its title matches.
- [x] `cd paper && latexmk -pdf main.tex`: builds with no undefined references
      or citations.
- [ ] Adversarial referee pass (reports in `research/reviews/`), with all
      FATAL and MAJOR issues resolved.

## Literature searches that could not be automated **[human]**
Every "we are not aware of" statement in the paper depends on these.
- [ ] **NASA ADS full-text search** for any search for cubic, octahedral or
      lattice-aligned anisotropy in cosmic-ray arrival directions (Sec. 4, novelty
      claim). Suggested queries: `full:"cubic symmetry" AND full:"cosmic ray"`,
      `full:"lattice spacing" AND full:"anisotropy" AND full:"simulation"`,
      and the citations of Beane et al. 2014 (EPJA 50, 148).
- [ ] **Google Scholar "cited by"** pass on Beane, Davoudi & Savage (2012/2014).
- [ ] **PhilPapers** search for peer-reviewed philosophy-of-science articles
      on the falsifiability or testability of the simulation hypothesis
      (Sec. 9 negative claim).
- [ ] Check whether any preprint reports a performed Campbell et al.
      experiment (the unconfirmed Polytechnique Montréal report, Sec. 7 notes).
- [ ] Check whether the Auger 30% open-data release has appeared (Sec. 4).

## Sources read only as abstracts or metadata (upgrade if access is available) **[human]**
See the per-section "gaps" lists in `research/notes/*-report.md`. The most
important:
- Bekenstein 1981 (PRD 23, 287); Bombelli et al. 1987 (PRL 59, 521).
- Greisen 1966; Zatsepin & Kuzmin 1966.
- Zuse 1967/1969; Fredkin 1990, 2003.
- Vopson 2019 (AIP Adv. 9, 095206) and 2023 (AIP Adv. 13, 105308) full text.
- The published EPJA version of Beane et al. (compared only with arXiv v2).

## Expert checks of original results **[human]**
- [ ] A lattice field theorist checks Sec. 3 "this work": the dispersion
      expansion, the photon-decay threshold, and the improved-action discussion.
- [ ] A cosmic-ray analyst checks the Sec. 4 analysis proposal.
- [ ] A statistical physicist checks the Sec. 8 copper / stored-bit arguments.

## Submission logistics **[human]**
- [ ] Author list, affiliations, ORCID, acknowledgements (including disclosure
      of AI assistance in research and drafting, per venue policy).
- [ ] arXiv primary category (suggested: physics.hist-ph or gr-qc, cross-list
      hep-ph, astro-ph.HE, quant-ph).
- [ ] OpenReview venue and its template/page limits (the draft is about 23k
      words / 69 pages in 11pt single column).
- [ ] Licence for the paper and for the repository (ledgers, scripts).
- [ ] Archive the repository (e.g. a Zenodo DOI) and cite it in the data
      availability statement.
