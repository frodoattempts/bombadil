# Report: 07-rendering-qm (render-on-demand / observer-dependent computation and QM foundations)

## Files

- Ledger: `research/ledgers/07-rendering-qm.md`, with 56 admitted claims (55 FULLTEXT, 1 METADATA) and 2 excluded UNVERIFIED items.
- BibTeX: `research/bib/07-rendering-qm.bib`, 32 entries.
- Section: `paper/sections/07-rendering-qm.tex`
  - Compiles cleanly with amsmath and url, no amssymb needed.
  - About 2,000 words plus one table: roughly 3.5 pages at 11pt with 1in margins.
  - Labels: `sec:rendering-qm`, `sec:rendering-qm-logic`, `sec:rendering-qm-campbell`, `sec:rendering-qm-constraints`, `sec:rendering-qm-others`, `sec:rendering-qm-bell`, `tab:rendering-qm-exps`.

## Main findings

1. **Campbell et al. (2017) do predict deviations from standard QM.** The paper never says so and never quantifies them. Each "success" criterion contradicts a standard QM prediction:
   - Scheme 1 (detectors on, recorder unplugged; or the coincidence counter removed) predicts interference. QM predicts none: an unread which-path record still suppresses interference (Ma, Kofler & Zeilinger, RMP Sec. II.E), and the unsorted D0 data of an eraser never show fringes (Kim et al. Eq. 10; Kastner 2019).
   - Scheme 2 (destroy the USB drive) predicts that interference returns. In QM, destroying a classical copy does not restore coherence.
   - Scheme 3 (Eq. 2: P[R=1|X] = 1/(1+2cos^2(pi x/a))) predicts that X and R are correlated. QM gives P = 1/2, because both the erasure and the which-path subensembles are fringe-free. The deviation is up to 1/2 at dark fringes and 1/6 at bright fringes. This is our arithmetic, flagged as such.
   - Scheme 4 assumes interference in the unconditioned D0 data for configurations (a)-(c), which is not a QM prediction. Under the paper's own outcome classification, the QM result would count as a "discontinuity in the rendering reality". In configuration (d) it matches the outcome the authors call "a strong indicator that this reality is simulated". The protocol as written has no outcome that disconfirms the hypothesis. This is the most important point for referees, and the section states it carefully with page cites.
   - The paper gives no numerical predictions, only qualitative "wave/particle pattern" outcomes plus a noise allowance delta(I) < 0.9.
2. **None of the proposed experiments has been reported in citable form** as of 2026-09-27 (searches below).
   - CUSAC's site lists the experiments as intended. It names leads F. Khoshnoud (Cal Poly Pomona) and D. Chartrand (Canada), and its "Updates" page only links videos.
   - The only related peer-reviewed output we found is Luo, ..., Galvez & Khoshnoud (Am. J. Phys. 92, 308, 2024). It is a teaching-lab single-photon double slit plus a polarisation eraser. It acknowledges Campbell and Chartrand, does not mention the simulation hypothesis, and states that interference vanishes "regardless of whether [path information] is collected or not."
3. **Existing experiments** (table in the .tex) agree with QM:
   - delayed choice at space-like separation (Jacques 2007: V = 94%, open-port probabilities 0.50 ± 0.01);
   - eraser with Einstein locality (Ma 2013: V = 0.951(18), I = 0.955(7), choice up to about 450 µs later);
   - delayed-choice entanglement swapping (Ma 2012);
   - unread which-path records: Dürr 1998 (via RMP), Hackermüller 2004 (V = 47 → 0%), Hornberger 2003.

   They bound timing-dependent deviations at the few-per-cent level. They do **not** directly test the "destroy the classical record" or "unplugged recorder" variants. Because Campbell et al. never define "availability on objective media" operationally, a proponent can reinterpret the decoherence results.
4. **Bell / superdeterminism.** A rendering simulator must be nonlocal (as Campbell et al. posit) or violate Statistical Independence. Cosmic and human-choice Bell tests constrain only local in-universe mechanisms. We present Hossenfelder & Palmer's critique of the cosmic and BIG Bell framing as their position. 't Hooft's CAI gives an explicit, falsifiable computational prediction (quantum computers vs. a Planck-scale classical computer), which we use as a contrast.

## Gaps

- **Unperformed experiments (no citable results found):**
  - Campbell et al. schemes 1-4: detector without recorder; USB destruction; the X-R correlation of Eq. 2; the manual-switch 60 s delay;
  - the "further questions" of Sec. 4.6: objective vs subjective recording, anonymous which-way data;
  - Hossenfelder-Palmer time-correlation test of superdeterminism. We did not search exhaustively for this; it is outside the core scope.
- **No quantitative render-on-demand model exists** in the literature we found. This means a model with a resource budget, a rendering rule, and a predicted deviation from QM as a function of the budget. The survey's R4 opportunity stands.
- **No direct test of the "classical record destroyed later" variant.**
  - Existing unread-record experiments (Dürr, Hackermüller, Hornberger, Luo, Eichmann 1993) involve quantum or environmental records, not a macroscopic classical memory that is later destroyed.
  - QM's prediction is unambiguous, but no experiment has been framed to answer the render-on-demand claim in its own terms.
  - Such a test would be cheap. Referees in quantum optics may say it is unnecessary, because standard decoherence theory already fixes the answer.
- **Wheeler 1978, "Law without law" (1983), Scully & Drühl 1982, Dürr et al. 1998, Englert 1996 and Radin et al. 2016 were not read in the original.**
  - Characterisations come from the RMP review (Ma, Kofler & Zeilinger 2016), Ma et al. 2013 or Tremblay 2019, all read in full. These are marked METADATA-original in the ledger notes.
  - Someone with library access should check the Dürr quote against Nature 395, 33.
- **Arvan 2014 (Philosophical Forum): METADATA only.** Wiley and SSRN returned 403. The .tex states only the title-level claim.
- **Wheeler "Law without law" date.** The Princeton volume is 1983 (Crossref DOI 10.1515/9781400854554). The RMP review and Jacques et al. cite it as 1984. We used 1983 with a bib note. Other sections should use the same key, `Wheeler1983law`.

## Unverifiable items (kept out of the .tex)

- **C-07-U01.** The Psi Encyclopedia entry on T. W. Campbell (M. Duggan, created 1 June 2026, updated 4 Sept 2026) reports a "personal communication from David Chartrand ... that tests at Polytechnique Montréal over three years and seven quantum-erasure experiments had falsified one version of Campbell's simulation hypothesis". The article itself calls this provisional. We found no preprint. If a paper appears before submission, it should be added: it would be the first performed test.
- **C-07-U02.** Turchin & Yampolskiy (2019), "Glitch in the Matrix: Urban Legend or Evidence of the Simulation?" (PhilPapers .docx). Not accessible, because PhilPapers blocks automated access.
- **Press claims.** Earth.com, Futurism, IFLScience and Lifeboat (2024) say experiments were "underway" at Cal Poly Pomona with "early results" to be presented at a symposium. These are press or PR items and are not cited. No results were found in citable form.

## Searches performed (for the "we found no citable report" statements)

- **arXiv** (arxiv.org/search, 2026-09-27):
  - author "Khoshnoud" (6 hits; only 2401.02351 relevant);
  - author "Chartrand David" (none relevant);
  - all-fields queries "simulation theory Campbell", "simulation hypothesis test quantum", "virtual reality wave function collapse", "simulated universe quantum eraser", "observer render simulation quantum".
- **INSPIRE:** `refersto:recid:3036557`, i.e. citations of Campbell et al. (2 hits: Ydri 2020 essay; Irwin et al. 2020).
- **Semantic Scholar:** citations of arXiv:1703.00058 (20 items). We checked:
  - Wolpert 2025 (J. Phys. Complexity 6, 045010), which only cites Campbell et al.;
  - Sisini 2023, not relevant;
  - Yampolskiy 2023 and Irwin 2020, both used.
- **Web search** (Sept 2026): "Tom Campbell simulation theory double slit experiment results Cal Poly Pomona"; "Khoshnoud Campbell double-slit quantum eraser experiment simulation hypothesis paper 2024 OR 2025 results"; "Polytechnique Montréal quantum eraser experiment Campbell"; "testingthehypothesis.com Campbell experiment 1 results published"; "Yampolskiy How to Hack the Simulation journal"; "quantum measurement lazy evaluation simulation hypothesis paper"; "wave function collapse level of detail rendering simulated universe paper".
- **Crossref** bibliographic queries: Yampolskiy (found the Seeds of Science DOI), Arvan, Whitworth, Irwin, Kastner, Chalmers & McQueen.
- **Sites checked directly:**
  - testingthehypothesis.com: /experiments, /team, /faq, /press, /copy-of-paper (Updates);
  - the IJQF article pages (archives 3888 and 4105). Their comment feeds were empty or not visible.

## Peer-reviewed "lazy evaluation / level-of-detail" work

We found **no peer-reviewed paper that models QM measurement as lazy evaluation or level-of-detail rendering in a quantitative way.** The closest items:

- **Campbell et al. 2017 (IJQF):** conceptual only.
- **Whitworth 2007/2008:** a CDMTCS technical report on arXiv, not peer-reviewed as far as we can tell. It says "calculated only on demand".
- **Irwin, Amaral & Chester 2020 (Entropy, peer-reviewed):**
  - uses a VR-headset/GPU rendering analogy (p. 12);
  - asserts a consciousness consensus that conflicts with the review literature;
  - makes no quantitative prediction.
- **Arvan 2014 (Philosophical Forum):** METADATA only.

"Lazy evaluation" as a phrase appears in forum discussions (Hacker News, Quora), not in the peer-reviewed literature we could find.

## Things that could embarrass us

- **"Campbell et al. predict deviations" is our inference.** The paper never uses the word "deviation", so the .tex phrases the comparison as "ours". The inference rests on standard, uncontroversial QM:
  - no-signalling: the D0 marginal is independent of the idler measurement;
  - the Englert/Ma complementarity relation.

  A quantum-optics referee will agree; Campbell's supporters may object that "availability" rescues the hypothesis. The section acknowledges that loophole explicitly.
- **Kim et al. delay.** Kim et al. write "≃ 2.5 m" and "at least 8 ns". The RMP review says 2.3 m (7.7 ns). We quote Kim.
- **INSPIRE metadata errors corrected in the bib:**
  - the Shalm et al. first author appears as "Stevens";
  - Jacques et al. pages appear as "1136303";
  - 't Hooft's CAI book year appears as 2006;
  - the free-will chapter lists the editors as authors.

  If other sections pulled these entries straight from INSPIRE, they will carry the same errors.
- **Hackermüller.** The visibility numbers are from the Fig. 2 caption, for C70 at 190 m/s.
- **Irwin et al. vs Tremblay.** Irwin et al. describe Tremblay as having confirmed "the statistical significance". Tremblay's own abstract concludes that the dataset shows no evidence (p > 0.05 after correcting the trimming procedure). We report Tremblay's own conclusion and do not repeat Irwin's summary as fact.
- **Yampolskiy venue.** Seeds of Science is a real DOI-bearing venue with public "gardener" review, but it is not a conventional peer-reviewed journal. The .tex names the venue without calling it peer-reviewed.
- **Cosmic Bell test caveats.** Their σ values are lower bounds ("≳" in the abstracts). The .tex says "quoted as lower bounds".

## Suggested cross-links

- **09-methodology:** shares the key `Campbell2017on`, with identical fields. It should also use the "a test needs a predicted deviation Δ" framing from `sec:rendering-qm-logic`, and could cite `tab:rendering-qm-exps`.
- **Computational-complexity / bounded-compute section (H-budget):** 't Hooft's CAI quantum-computer prediction (`tHooft2016cellular`, Sec. 5.8) belongs there as well. Keep the key identical.
- **Philosophy section (01):** consciousness-collapse (Chalmers & McQueen 2022) and the von Neumann-Wigner lineage that Campbell et al. adopt.
- **Survey R4 ("Quantifying H-lazy"):** this section confirms the gap. No existing model gives a budget-dependent deviation. Any R4 model must reproduce the Table 1 data within their uncertainties and the Bell results (nonlocal or superdeterministic).
