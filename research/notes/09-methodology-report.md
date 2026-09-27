# Report: 09-methodology

## Files

- `research/ledgers/09-methodology.md`: 60 claims (C-09-001 to C-09-060). 54 FULLTEXT, 5 ABSTRACT, 1 METADATA, 0 UNVERIFIED.
- `research/bib/09-methodology.bib`: 43 entries. Every `\cite` key in the `.tex` is present and every entry is cited.
- `paper/sections/09-methodology.tex`: about 6 pages in `article` 10pt one-column, which should be about 3.5 pages in a two-column layout. It contains two tables:
  - `tab:subhyp`: sub-hypothesis, signature, degenerate explanation, status.
  - `tab:reception`: what four papers claim versus how they were reported.
- Test compile: pdflatex plus bibtex against a minimal wrapper. No errors. Undefined refs remain only for other sections' labels (see below). The file needs `amssymb` (`\gtrsim`) and `url`.

## Coverage

- **Frameworks.**
  - Popper and Lakatos via SEP (Thornton, rev. 2026).
  - Underdetermination via SEP (Stanford, rev. 2023): holist vs contrastive, empirical equivalence, the evil demon.
  - Bayesian relevance confirmation and the likelihood-ratio measure via SEP (Crupi, rev. 2025).
  - Carroll's five levels of falsifiability.
  - Dawid's three non-empirical arguments (arXiv version of his 2019 chapter), Dawid 2013 (ABSTRACT), Ellis & Silk (standfirst only) and Rovelli.
- **Application to the SH.**
  - The unrestricted hypothesis falls in Carroll's category 1 (our application, flagged as such).
  - Asymmetry: confirmable by disclosure (Chalmers; Hsu & Zee), never refutable.
  - Bostrom's own statement that the chief empirical importance lies in the trilemma.
  - Wolpert's FHE indistinguishability.
- **Classification scheme.** Six rows: H-grid, H-noise, H-lazy, H-budget, H-info, plus **H-patch** (adaptive simulator, Barrow 2007). Each row has a cited non-simulation rival:
  - LIV in quantum gravity (Mattingly); minimal length (Hossenfelder LRR); causal sets (Dowker-Henson-Sorkin); Collins et al. fine-tuning.
  - Hogan's holographic noise model; Holometer null results.
  - Collapse models (Bassi et al. RMP 85, 471); the von Neumann-Wigner postulate as acknowledged by Campbell et al.
  - Aaronson's NP-hardness assumption; Lloyd's bounds.
  - Varying-constant theories (Uzan LRR).
- **Adaptive simulator.**
  - Bostrom 2003, Sec. III: edit brain states, rerun. Verified verbatim. Journal page not verified; the locator uses p. 5 of the author's preprint.
  - Barrow 2007 (patches, drifting constants); Campbell et al. 2017 (consistency vs detection avoidance); Hossenfelder 2017 (how would the programmer know).
  - Formalized as a holist auxiliary: the likelihood ratio of a null result is about 1.
- **Assessments.** Hossenfelder 2017 and 2021 blogs (verbatim); Aaronson 2017 blog; Vazza 2025 (testable only for simulators obeying our physics); Wolpert 2025; Chalmers 2022 (authorized Nautilus excerpt of *Reality+*) and 2024 (PPR); Beane et al. (in-principle discoverability under finite resources); the AMNH 2016 debate as an event only.
- **Reception.** Four cases, each paired with what the paper says:
  1. Beane et al. 2012: the UW release, via ScienceDaily.
  2. Ringel & Kovrizhin 2017: PBS NOVA Next headline "Physicists Confirm...". A full-text search of the paper finds no mention of "universe" at all.
  3. Vopson 2023: Vice headline, with Vopson quoted conceding that the law holds "regardless of whether the universe is a simulation or not".
  4. Faizal et al. 2025: here the paper itself claims "logically impossible". The UBCO release says "mathematically proven"; ScienceDaily's headline says "prove". The Redden arXiv comment is the rebuttal.

## Suggested defensible phrasing of the paper's thesis

> The unrestricted simulation hypothesis is not an empirical hypothesis: no
> observation can refute it, and strong evidence for it would most plausibly
> require disclosure by the simulator. What can be tested are conjunctions of
> the hypothesis with explicit assumptions about simulator architecture,
> resources and non-adaptivity. For every such sub-hypothesis we examine, the
> signature is also predicted by non-simulation physics, so a detection would
> establish new physics (discreteness, holographic noise, collapse) and not
> simulation as such, while a null result bounds the space of non-adaptive,
> resource-limited simulator designs sharing the assumed architecture.

Wording to avoid:
- "The SH is unfalsifiable, therefore meaningless." Carroll and Chalmers would object. Say instead that it is not refutable by observation.
- "Every conceivable signature has a non-simulation rival." We showed this only for the six classes in the table. General contrastive underdetermination makes it plausible but not demonstrated.
- "Faizal et al. is refuted." Section 06 must assess this. We cite only that the argument is disputed.

## Gaps and weak points (could embarrass us)

1. **Ellis & Silk (Nature 2014) is paywalled.** Only the standfirst was verified (ABSTRACT). The `.tex` attributes to them only the standfirst sentence. Anyone with Nature access should read the full piece before adding more.
2. **Dawid 2013 book not read.** We used his 2017 arXiv paper (the 2019 CUP chapter) for the three arguments. The book is cited only at the level of the publisher's description.
3. **Popper is cited only through SEP.** A philosopher referee may want *The Logic of Scientific Discovery* or *Conjectures and Refutations*. Also, the SH is an existential claim ("there exists a simulator"), and Popper treats purely existential statements as unfalsifiable. That would be a neat point, but we did not verify a quotable source, so it is not in the text.
4. **Hossenfelder, *Existential Physics* (2022), was not read.** We cite only her two blog posts, verbatim. If her book has a chapter on the simulation hypothesis, someone with the book should add it with a page number.
5. **Chalmers *Reality+* page numbers are unknown.** We read the authorized Nautilus excerpt (`Chalmers2022can`) and cite the book alongside it. Section 01 may cite the book with pages. Reconcile.
6. **Greene (2020), "The Termination Risks of Simulation Science", Erkenntnis 85, 489-509, doi:10.1007/s10670-018-0037-1.** This is highly relevant: it argues about the risks of experimental probes of the SH and ties into the adaptive or interventionist simulator. It is METADATA only: the full text and abstract were blocked (Springer, PhilArchive, NTU repository and OpenAlex had no abstract). It is not in the `.tex` or the `.bib`. **It should be added if anyone can read it.**
7. **Vopson 2023: full text not read** (AIP and Portsmouth repository behind a bot check). We used the abstract only. Section 08 must provide the full-text claims.
8. **The Ringel quote to New Scientist is second-hand** (via Futurism). The New Scientist article (2149627) could not be fetched. The `.tex` attributes it only as "one outlet reported". The Aaronson post also mentions a headline, "Researchers claim to have found proof we are NOT living in a simulation", but we did not trace which outlet.
9. **Beane et al. coverage.** The widely cited US News blog "Proof Of The Simulation Argument" (17 Dec 2012) was blocked, so it is not verified or used. The case we use (the UW release) is fairly faithful. The overstatement examples are RK, Vopson and Faizal.
10. **AMNH debate.** amnh.org returned a CAPTCHA. The event metadata comes from AMNH's official YouTube description. We did not watch the debate, so **no statement may be attributed to any panelist**.
11. **Peer-reviewed philosophy-of-science literature on SH testability appears thin.** The `.tex` says "we are not aware of" a peer-reviewed phil-sci article devoted specifically to SH falsifiability. Searches performed:
    - web search: "simulation hypothesis" + falsifiability/testability/"scientific status"/pseudoscience; also restricted to Synthese/Erkenntnis/Found. Sci./EJPS;
    - Crossref bibliographic queries: "simulation hypothesis falsifiability", "...testability", "testing the simulation hypothesis", "...scientific status", "simulation argument empirical test", "simulation hypothesis pseudoscience";
    - INSPIRE: titles containing "simulation hypothesis"/"simulated universe"/"simulation argument", and citations of Beane et al. (recid 1189720; INSPIRE lists only 13 citing records).

    PhilPapers returned 403 and the OpenAlex search was rate-limited, **so this negative claim is the weakest statement in the section**. Before submission, someone should search PhilPapers' "Simulation Hypothesis" category by hand. Candidates seen but not checked:
    - Birch 2013 and Summers & Arvan: about the argument, not testability; section 01.
    - Dainton 2012, J. Consciousness Studies.
    - Hanson 2001.
    - Neukart et al. arXiv:2212.04921: not peer-reviewed as far as we know.
    - The PhilArchive paper "The Logical and Physical Impossibility of the Simulation Hypothesis" (JAMTLA-4): unknown status.
12. **Redden 2025 (arXiv:2512.11807)** is an unrefereed comment by a single author. We cite it only as evidence that the argument is disputed. Section 06 should give the substantive critique, ideally with a stronger source if one exists.
13. **The H-info row is thin.** Its "degenerate explanation" cites Lloyd 2002 ("information is physical" within standard physics). Section 08 should supply the specific rival (standard Landauer thermodynamics, estimator artifacts) with its own citations.
14. **Holometer: a 4.6σ exclusion of *one* model** (5.1σ statistical only). The table says "incl. calibration uncertainty". Section 05 should check consistency.

## Unverifiable or excluded items (not in `.tex`)

- Greene 2020 content (METADATA only).
- New Scientist 2017 (Ringel's exact words).
- US News 2012 "Proof of the Simulation Argument" blog.
- Hossenfelder, *Existential Physics* (2022).
- Anything said at the AMNH 2016 debate.
- Popper's treatment of existential statements (no primary source read).

## Cross-section notes and label assumptions

The `.tex` uses these **assumed** labels. The integrator must match them to the labels the other sections actually define:

| Label in 09 | Intended section |
|---|---|
| `sec:argument` | 01, Bostrom and critics |
| `sec:lattice` | 03, lattice |
| `sec:cosmicrays` | 04, cosmic rays |
| `sec:holographic` | 05, holographic noise |
| `sec:complexity` | 06, complexity (Faizal, Ringel-Kovrizhin, Vazza, Wolpert details) |
| `sec:render` | 07, render on demand |
| `sec:infophysics` | 08, Vopson |

Section 09 defines `sec:methodology`, `sec:methodology:{standards,unrestricted,subhyp,adaptive,assessments,reception,thesis}`, `tab:subhyp` and `tab:reception`.

The "Status" column of `tab:subhyp` is deliberately minimal ("see Sec. X"). Sections 03-08 should confirm or replace each cell:
- whether any dedicated cubic-anisotropy search exists (03/04);
- whether any H-lazy experiment has been performed (07);
- the status of Vopson's IR-photon prediction (08).

Keys shared with `research/bib/01-philosophy.bib`, all referring to the same works: `Barrow2007living`, `Bostrom2003are`, `Chalmers2022reality`, `Chalmers2024taking`. Field contents may differ slightly, so merge carefully. Section 01's bib also contains `Greene2020termination`. **If section 01 has verified Greene's content, this section should cite it in Sec. 9.4 (adaptive simulators and the risks of probing).** Check 01's ledger.

Possible BibTeX key collisions or duplicates across topics:
- `Chou2016first` and `Chou2017interferometric` (the Holometer papers): section 05 might key these as `Holometer2016first` etc.
- `Wolpert2025what`: section 06 might use the arXiv title and year, e.g. `Wolpert2024implications`.
- `Chalmers2022reality`: check with 01.
- `Beane2014constraints`: matches the convention example.
- `Bostrom2003are`: matches the convention example.

## Downloaded sources

Everything is under `/tmp/claude-0/papers/`:
- arXiv PDFs and their `.txt` extractions;
- SEP HTML and text (`sep-*.txt`);
- Europe PMC full text of Ringel & Kovrizhin (`rk.xml`, `rk.txt`);
- the Bostrom and Barrow preprints;
- the Chalmers PPR PDF (`simserious.pdf`);
- blog and news HTML/text (`hoss20*.txt`, `news/`).
