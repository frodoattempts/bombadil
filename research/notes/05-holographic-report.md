# Report: 05-holographic (finite information density and interferometric probes)

Files:
- `research/ledgers/05-holographic.md`: 62 claims, all FULLTEXT for the claim as
  used. Two claims also carry secondary sources at a lower level:
  - C-05-001: Bekenstein 1981 is METADATA only; the bound is taken from Bousso's account.
  - C-05-043: Verlinde & Zurek 2020 JHEP is ABSTRACT only.
- `research/bib/05-holographic.bib`: 38 entries, all from INSPIRE BibTeX with keys
  rewritten to our convention. The four Holometer-collaboration papers use the prefix
  `Holometer` (INSPIRE lists `collaboration = "Holometer"`). The Richardson 2021 PRL
  has no collaboration field, so it is keyed `Richardson2021interferometric`.
- `paper/sections/05-holographic.tex`: about 2.7 two-column pages of text plus one
  full-width table (`table*`). A test compile (article class) produced no errors and
  one minor overfull hbox; every `\cite` key resolves.

## Coverage

- **Holographic bounds.** Covered: Bekenstein (via Bousso), 't Hooft 1993,
  Susskind 1995, Bousso 2002. Lloyd 2002 is used for scale only. Vazza 2025 (Front.
  Phys.) is used for the holographic-bound estimate of simulation cost.
- **Hogan holographic noise and GEO600.** Covered: Hogan PRD 77 (2008), PRD 78
  (2008), the 2009 arXiv-only revision, PRD 85 (2012), and the 2013 essay. The
  critique is Smolyaninov PRD 79 (2009). The GEO600 side is Hild et al. CQG 26 (2009)
  and Lück et al. JPCS 228 (2010). The retrospective is Amelino-Camelia, Living Rev.
  Relativ. 16 (2013).
- **Holometer.** Covered: the PRL 117 (2016) first result, the CQG 34 065005
  instrument paper, the CQG 34 165005 final shear result, the PRD 95 063002 MHz GW
  paper, and the PRL 126 241301 bent-arm rotational result. The theory inputs are Kwon
  & Hogan CQG 33 (2016) and Hogan, Kwon & Richardson CQG 34 135006 (2017). Kwon, Found.
  Phys. 55 (2025) gives a retrospective by a Holometer collaborator.
- **Verlinde-Zurek line.** Covered: PLB 822 (2021), JHEP 2020, Zurek PLB 826 (2022),
  modular/shockwave PRD 106 (2022), Li et al. PRD 107 (2023) (the pixellon recasts),
  and Bub et al. PRD 108 (2023).
- **New experiments.** Covered: GQuEST, PRX 15, 011034 (2025). Note that the task brief
  guessed a CQG venue; the published venue is PRX. QUEST design is CQG 38 085008
  (2021). QUEST first results are Patra et al., PRL 135, 101402 (2025). The INRIM
  twin-beam demo is Commun. Phys. 3 (2020).
- **Counterpoints.** Covered: Carney, Karydas & Sivaramakrishnan PRD 113, 106002
  (2026), which gives the EFT prediction of Planck-suppressed noise, and Freidel &
  Oberfrank 2026 (a preprint). Reviews: Carlip, Rep. Prog. Phys. 86 (2023) and
  Sharmila et al., Nat. Commun. 17 (2026).
- **Simulation link.** Neukart et al. (arXiv:2212.04921, not refereed) is the only
  paper found that explicitly ties the Holometer to the simulation hypothesis.

## Corrections to the task brief (verified)

- The Holometer PRL title is "First Measurements of High Frequency Cross-Spectra from a
  Pair of Large Michelson Interferometers", PRL 117, 111102 (2016).
- The instrument paper is CQG 34 (2017) 065005. The brief's guess was correct.
- The rotational paper is Richardson et al., PRL 126, 241301 (2021).
- GQuEST is arXiv:2404.07524, published in PRX (not CQG).
- The Cardiff paper is titled "An experiment for observing quantum gravity phenomena
  using twin table-top 3D interferometers", CQG 38 (2021) 085008. It is not an
  "optical gravitational wave" paper. The Cardiff experiment is called QUEST.
- The **2.1e-20 m/√Hz** figure is the *cross-spectrum* sensitivity. The
  single-interferometer shot noise is **2.1e-18 m/√Hz**. Do not conflate them.
- The 4.6σ figure is the exclusion after the 10% calibration uncertainty; the
  statistical-only figure is 5.1σ. The equivalent 95% CL bound is a normalization below
  44% of the model prediction.

## Controversies and possible embarrassments

1. **What the Holometer excluded.** The first result excluded one spectral shape (the
   Kwon-Hogan model), and the authors say the exclusion applies "only to the spectral
   shape of the particular model". The final shear analysis excludes a two-parameter
   family. The rotational model was tested separately, with η < 0.25 t_P at 95% CL.
   Planar layouts cannot test 3D-entangled models. Any sentence of the form "the
   Holometer showed space is not pixelated" or "ruled out holographic noise" would be
   wrong. Later theorists (Li et al.) recast Holometer data for Verlinde-Zurek
   fluctuations; those numbers are **not** collaboration results.
2. **Inconsistent recast numbers.** For geontropic fluctuations, Li et al. give Holometer
   bounds of α ≲ 0.7 (with an IR cutoff) and α ≲ 0.6 (without). GQuEST quotes
   α ≲ 3 / 0.7 (with cutoff) and 0.1 / 0.6 (without) for LIGO / Holometer, citing Li et
   al., but then states that "α < 0.6 ... is the current experimental constraint set by
   the Holometer for geontropic fluctuations with IR cutoff". That is a small internal
   inconsistency in GQuEST (0.6 vs 0.7). We quote Li et al. in the table.
3. **Two different "inverse light crossing times".** The Holometer PRL says 3.8 MHz
   (c/2L, the free spectral range). The CQG instrument and shear papers say 7.6 MHz
   (c/L). Both appear in the literature, so state which one is meant.
4. **Arm length.** The PRL gives 39.06 m and the CQG papers give "40-m"; the bent-arm
   PRL gives 38.9 m.
5. **Hogan's model was critiqued, and changed over time.**
   - The prediction changed by a factor √π in 2009, and an earlier spectral-slope claim
     was withdrawn.
   - The GEO600 frequency range cited as "unexplained" differs between papers
     (100-600 Hz in PRD 77, 300-1400 Hz in PRD 78).
   - Smolyaninov (PRD 79) argued the noise should be orders of magnitude smaller.
   - Amelino-Camelia called it "a young proposal still looking for some maturity".
   - Kwon (2025) says the first-generation design faced "(justified) criticism" for
     not being Lorentz invariant. We could not find that criticism in the refereed
     literature (see gaps).
6. **The GEO600 "mystery noise".**
   - GEO600 papers do not mention Hogan.
   - Lück et al. (2010) say the 100-500 Hz noise was "yet unknown" in detuned RF
     readout, and that all noise was explained by known sources in tuned DC readout.
   - Amelino-Camelia (2013) declares the episode over.
   - Hogan (2012) argues that GEO600's folded arms suppress holographic noise by 2, so
     GEO600 never ruled it out.

   Present this carefully. No GEO600 paper we read claims to have tested or excluded
   holographic noise.
7. **"Holographic noise" names two unrelated proposals.** One is the Ng-van Dam /
   Amelino-Camelia foam type; the other is Hogan's. Amelino-Camelia stresses there is
   "no relation". Coordinate terminology with the spacetime-foam/discreteness section.
8. **EFT versus holographic enhancement.** This is a live dispute. Carney et al.
   (PRD 2026) say the minimal EFT "unambiguously" predicts ΔL ~ 10^-35 m, while
   Verlinde-Zurek and follow-ups claim an IR-enhanced ΔL² ~ l_p L. Also, Li et al.
   argue that geontropic noise *does* accumulate in Fabry-Perot cavities, which is the
   opposite of Hogan's assumption for his model. The two are different models, so this
   is not a direct contradiction.
9. **The simulation framing.**
   - The popular "pixelated space" framing does not appear in the Holometer papers.
   - The term "pixel" comes from Susskind (1995) and reappears in Verlinde-Zurek
     ("Planck size pixels") and in Li et al.'s "pixellon".
   - Hogan's 2013 essay uses computing metaphors ("cosmic Internet Service Provider",
     "operating system") but proposes no simulation hypothesis.
   - Do not cite press coverage (e.g. 2009 New Scientist "hologram" stories) as
     evidence. We did not read or use any press article.

## Gaps and unverifiable items (kept out of the .tex)

- **Bekenstein 1981 (PRD 23, 287).** The APS PDF was paywalled (HTTP 403), so the bound
  is stated via Bousso's review. If a referee insists, obtain the PDF and upgrade
  C-05-001.
- **Leong et al., CQG 29 (2012) 065001** ("A new method for the absolute amplitude
  calibration of GEO 600"). It cites Hogan 2009, but only the IOP abstract was
  reachable, and the abstract does not mention holographic noise. Whether the
  calibration work was motivated by Hogan's claim is **UNVERIFIED**.
- **Prijatelj et al., CQG 29 (2012) 055009, and the AEI GEO600 web page.** Amelino-
  Camelia cites both as showing that no unexplained GEO600 noise remains. Neither was
  read.
- **LIGO/Virgo Nature 460, 990 (2009).** The limit Ω_GW < 5.6e-6 is taken as quoted by
  Kwon & Hogan (C-05-061), not from the primary paper.
- **Kwon's claim that the Holometer ran "through 2019".** This is the only source for
  the operating period; it is FULLTEXT but self-reported.
- **Published Lorentz-invariance critique of Hogan's 2008-2012 model.** Not found. We
  searched INSPIRE `refersto` lists for recids 771200, 787277, 821662 and 847012, and
  read the candidate critiques (Smolyaninov, Amelino-Camelia). The only explicit
  critique found is Smolyaninov's diffraction/self-focusing argument.
- **Direct statements by Hogan or the Holometer team linking their work to a simulated
  universe** (e.g. in interviews). Not searched in press sources, by policy.
- **Holometer scalar-dark-matter result** ("Constraints on Scalar Field Dark Matter from
  Colocated Michelson Interferometers", PRL 128 (2022), arXiv:2108.04746; authors and
  article number not checked). Not included; it is out of scope.
- **Dated-proposal status.** GQuEST results are not yet published. QUEST has
  stochastic-background limits only. Recheck both before submission, because
  new results in 2026-27 could make the table stale.

## Search log (supports the "we are not aware" statements)

- **INSPIRE `refersto`.**
  - Checked: Holometer PRL (recid 1407948, 52 citing records), Verlinde-Zurek PLB
    (recid 1721400, 108 citing records), and Hogan 2008/2009/2012 (recids 771200,
    821662, 847012).
  - All citing titles were scanned. Candidate critiques and follow-ups were downloaded
    and read.
- **INSPIRE full text (2026-09-27).**
  - These queries returned 0 records:
    - `fulltext:"simulation hypothesis" and fulltext:Holometer`
    - `... and fulltext:"holographic noise"`
    - `fulltext:"simulated universe" and fulltext:Holometer`
    - `fulltext:"simulation hypothesis" and fulltext:GQuEST`
    - `fulltext:"simulation argument" and fulltext:interferometer and fulltext:Planck`
  - `fulltext:"simulation hypothesis"` returned 36 records.
    - The only one citing the Holometer is Neukart et al. 2022.
    - Vazza 2025 uses the holographic bound.
  - `fulltext:"holographic noise" and fulltext:GEO600` returned 16 records, none by the
    GEO600 team.
- **Local text search.** A case-insensitive grep for "simulat" over the pdftotext
  output of all 21 core papers listed in C-05-056 finds only FINESSE/optical-modelling
  or test-signal usages.

## Suggested cross-links

- **Section 02 (computational resources / Lloyd).** Share the Lloyd and Vazza numbers,
  and avoid duplicating Vazza's energy argument.
- **Lattice/discreteness section (Beane et al. 2014).** The holographic resolution
  argument is area-law, whereas Beane et al. assume a cubic *volume* lattice. Point out
  Bousso's n^V vs e^{A/4} contrast (C-05-004).
- **Spacetime-foam / Lorentz-violation section.**
  - Kwon & Hogan's LIGO bounds on random-walk and white-noise foam models (C-05-027).
  - The distinct "holography-inspired" Ng-van Dam noise (C-05-023).
  - Carlip's foam review.
- **Digital physics / cellular automata section.** 't Hooft's 2+1 cellular-automaton
  remark (C-05-007) is explicitly flagged by him as speculation.
- **Proposed-tests section.** If Neukart et al. is discussed there, align the critique:
  the Holometer result they cite is a null result for one spectrum and does not test
  "the holographic universe".
- **LaTeX.**
  - `\label{sec:holographic}` and `\label{tab:holographic-experiments}` are defined.
  - The .tex has a `% cross-link: Section 02` comment where a `\ref` should be
    inserted at merge.
  - The table uses `table*` with `p{}` columns (no `array` package needed). At merge,
    consider `\raggedright` cells if the main preamble loads `array`.
