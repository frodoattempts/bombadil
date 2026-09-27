# Report: 04-uhecr (UHECRs as a probe of a spacetime lattice; novelty check)

Date of work: 2026-09-27. Files:
- `research/ledgers/04-uhecr.md` (56 claims)
- `research/bib/04-uhecr.bib` (33 entries: 31 from INSPIRE, 2 Zenodo datasets via DataCite)
- `paper/sections/04-uhecr.tex` (about 2,500 words plus one table). It test-compiles cleanly with the bib, with no undefined references except the `sec:lattice-liv` label, which section 03 provides.

PDFs and text extractions are in `/tmp/claude-0/papers/`.

## 1. Coverage and verification

| Level | Count | Claims |
|---|---|---|
| FULLTEXT | 51 | all numerical claims |
| ABSTRACT | 3 | C-04-046 (Auger top-100 catalog), C-04-048 (IceCube sidereal LV), C-04-049 (Auger LIV uses isotropic dispersion) |
| METADATA (mixed) | 2 | C-04-007 (Greisen and Zatsepin-Kuzmin originals are paywalled; the characterization rests on HiRes's full-text description), C-04-052 (citation lists; each candidate then checked by full text or abstract) |
| UNVERIFIED | 0 | none in the `.tex` |

Every number in the `.tex` has a FULLTEXT ledger entry with its confidence level or significance as stated in the source. Section 5 below lists the numbers that are our own computations (labelled "we" in the text).

Topics covered: the Beane et al. premises and prediction; the spectrum (HiRes 2008, Auger 2008 and 2020); composition (Auger DNN-Xmax 2025, Auger combined fit 2023, TA Xmax 2018); the dipole (Auger 2017 and 2024); intermediate scales (Auger 2018 and 2022, TA hotspot 2014, Auger+TA 2025); the Amaterasu event; multipoles and power spectra up to ℓ = 20 and ℓ = 64 (Auger 2017 and 2024, Auger+TA 2014 and 2025, Ahlers 2018); Galactic magnetic field models (JF12, UF23); public data (EPJC 2025 open-data paper, the 30% expansion proceedings, portal and Zenodo records inspected live, the full 2,635-event >32 EeV Zenodo set); the novelty check.

## 2. Key findings for the paper

1. **ℓ = 4 and ℓ = 6 have been measured, but never combined in an O_h-invariant way.** Auger's C_ℓ goes to ℓ = 64 (2017) and ℓ = 20 (2024). The Auger+TA full-sky a_ℓm and C_ℓ go to ℓ = 20 (2014, 2025). All are consistent with isotropy beyond the dipole; in the 2025 joint analysis the quadrupole is the most significant multipole, at 2.1σ post-trial.
2. **No numerical C_4 or C_6 upper limits are tabulated anywhere.** Auger 2024 shows 99% CL upper limits only graphically (Fig. 4). Auger+TA 2014 tabulates only ℓ ≤ 3. To quote numbers we would have to digitize the figures (not done) or ask the collaborations.
3. **A cubic pattern has no ℓ = 1 or ℓ = 2 content** (OWN numerical check: O_h invariants exist only at ℓ = 0, 4, 6, 8, 10, 12, ...). The observed dipole is therefore a nuisance, not a signal. Beane et al.'s Eq. (18) is exactly the ℓ = 4 cubic harmonic, a nice hook for the ℓ = 4/6 statistic.
4. **The GZK premise of the Beane bound is contested.** Auger's composition becomes heavier and purer, the suppression "cannot be entirely ascribed to effects of extragalactic propagation" (PRL 134, 021001), and E_{1/2} disfavors the proton-only paradigm. TA's Xmax is proton-compatible, with poor discrimination at the highest energies.
5. **Better public data than the "10%/30%" framing suggests.** The complete Auger Phase 1 list of 2,635 events above 32 EeV (100% of that energy range, with exposure per event) is on Zenodo under CC BY 4.0. It has 1,387 events at ≥ 40 EeV (OWN tally). The 10% open-data release has only 86 events at ≥ 40 EeV (OWN tally). As of 2026-09-27, the 30% release announced for "late 2025" is **not** on the portal or Zenodo; release 3 of March 2024 (10%) is current. The README's statement ("expanding to 30% ...") should be phrased as planned, not done.
6. **Magnetic smearing is not negligible.** For iron at E_34 ≈ 46 EeV (R ≈ 1.8 EV), UF23 implies deflections well above the ~20° benchmark over most of the sky (the 20° half-sky condition needs R ≥ 20 EV, or 11 EV with GMF correction). The ℓ = 4 and ℓ = 6 scales are about 45° and 30°. A lattice search is only clean if the highest-energy primaries are light, or if the analysis forward-models the field.

## 3. Things that could embarrass us (please propagate)

- **Beane et al. print the GZK scale as "∼6×10^20 eV"** (arXiv v2, Sec. IV.4). The standard threshold is ~6×10^19 eV (HiRes), and the measured suppression is at 4-5×10^19 eV. Do not repeat the arXiv number. Section 03 already flags this consistently. We could not check the published EPJ A version (paywall).
- Beane et al. write "GKZ" throughout. Quote it as-is with a note, or say "GZK".
- **Vazza (2025) states the Beane bound as "∼10^-11 GeV^-1"**, which inverts the units (Beane: b^{-1} ≳ 10^{11} GeV). Vazza also dates the Amaterasu event to 2022; TA gives 27 May 2021. Other sections citing Vazza should not copy these.
- The Auger 2025 open-data proceedings describe the top-100 catalog as "2004 and 2022", "76-166 EeV". The ApJS abstract says 1 Jan 2004 to 31 Dec 2020, "78-166 EeV". We follow the ApJS.
- Two different ≥ 32 EeV Auger event counts exist: 2,635 (ApJ 935, to end-2020, looser cuts) and 2,738 (ApJ 976, 19-year large-scale selection). They are different selections, not a discrepancy, but a referee may ask.
- The joint Auger-TA 2025 results are ICRC proceedings, not refereed journal papers. The `.tex` cites them for numbers, and we label them as the "2025 joint update".
- Pseudo-C_ℓ reconstruction from partial sky assumes a statistically isotropic random sky (Auger's own caveat). A single fixed lattice pattern is not such a sky. The `.tex` makes this point; a referee from Auger will expect it.
- Do not call the Auger Science 2017 significance "5.6σ": that is pre-trial. The post-trial abstract value is ">5.2σ".

## 4. Novelty check: full log

Question: has anyone searched UHECR (or other astroparticle) arrival directions for a lattice-aligned / cubic / O_h-symmetric anisotropy, or explicitly tested the "numerical simulation" hypothesis with such data?

### 4.1 Citation graph of Beane et al. (arXiv:1210.1847; EPJ A 50, 148; INSPIRE recid 1189720)

**INSPIRE `refersto:recid:1189720`** returns 13 records. (Note that `refersto:arxiv:1210.1847` is mis-parsed by the API and returns 25,074 unrelated hits, so recid must be used.)

| # | Record | Class | Note |
|---|---|---|---|
| 1 | Andersen, "Lorentz Covariant Lattice Gauge Theory" (1210.8348) | theory | lattice graph method; no data |
| 2 | Leckey, "Quantum Measurement, Complexity and Discrete Physics" (quant-ph/0310033) | theory | collapse model |
| 3 | Kakushadze, "Does the Universe have a Hard Drive?" (1701.07161) | theory/popular essay | no data |
| 4 | Qin, "Machine learning and serving of discrete field theories" (Sci. Rep. 2020) | theory/methods | no UHECR |
| 5 | Irwin, Amaral, Chester, "Self-Simulation Hypothesis Interpretation of QM" (Entropy 2020) | philosophy/theory | no data |
| 6 | Bleu et al., "Quantum Geometric Tensor ..." (PRB 97, 195422) | irrelevant | condensed matter |
| 7 | Leckey & Flitney, "Spontaneous Collapse ... Discrete Physics" (2303.03096) | theory | no UHECR |
| 8 | Vazza, "Astrophysical constraints on the simulation hypothesis" (2504.08461; Front. Phys. 2025) | theory (energy argument) | full text read: UHECR energy used only as a resolution scale; no direction analysis |
| 9 | Feng, McGuigan, White, "Superconformal QM on a Quantum Computer" (2201.00805) | irrelevant | quantum computing |
| 10 | Chandra, Feng, McGuigan, "A Matrix Big Bang on a Quantum Computer" (2212.00260) | irrelevant | quantum computing |
| 11 | Stryker, "Shearing approach to gauge-invariant Trotterization" (PRD 112, 2025) | irrelevant | quantum simulation |
| 12 | Perović & Ćirković, *The Cosmic Microwave Background* (CUP 2024) | history/philosophy | book |
| 13 | Miguel-Tomé et al., "Fundamental Physics and Computation" (Universe 2022) | review/philosophy | no data |

**Semantic Scholar** `paper/arXiv:1210.1847/citations` returns 61 records, retrieved after retries. Classification:
- Philosophy, theology, ethics or popular: about 40. Examples: "A Neo-Platonic Perspective on the Simulation Hypothesis" (Sophia 2026); "Islamic Theological Reflections ..." (2024); "Business models for the simulation hypothesis" (2404.08991); "How to Escape From the Simulation" (Seeds of Science 2023); Erkenntnis papers on simulation probes and termination risks; "Freak Observers and the Simulation Argument" (Ratio 2013); "A Bayesian Approach to the Simulation Argument" (Universe 2020); Olshin, *Deciphering Reality* (Brill 2017, essay book); "A Fortunate Universe" (book 2016); "Is the Universe a Vast, Consciousness-Created Virtual Reality Simulation?"; film and literature studies.
- Theory without data: Vazza 2025; Wolpert, "What computer science has to say about the simulation hypothesis" (J. Phys. Complexity 2025); Andersen 2012; Kakushadze 2017; Qin 2019; "A lattice Maxwell system with discrete space-time symmetry" (1709.09593); Leckey & Flitney 2023; the quantum-computing papers above.
- Proposals for experiments, but not UHECR: Campbell, Owhadi, Sauvageau, Watkinson, "On testing the simulation theory" (1703.00058). Full text checked: it proposes quantum-optics experiments and cites Beane only in the reference list.
- Humor: Rachen & Gahlings, "Conspiratorial cosmology - the case against the Universe" (1303.7476). Full text checked: an April-1 parody.
- Irrelevant: PRB 97 195422 and others.
- **Observational analyses of arrival directions: 0.**

**OpenAlex** reports 54 citing works for the EPJ A DOI (W2021145183). The listing could not be retrieved because the shared daily API budget was exhausted (HTTP 429 "Insufficient budget"). **NASA ADS**: the API returned 401 without a token, and the web UI served a "Human Verification" page. **Google Scholar**: HTTP 429. These three gaps bound the absence claim.

### 4.2 Full-text and keyword searches

INSPIRE full-text (`fulltext:`):
- `fulltext:"cubic symmetry" and fulltext:"arrival directions"`: 1 hit (SAIP2015 proceedings volume, an aggregate of unrelated contributions; not inspected in detail).
- `fulltext:"cubic symmetry" and fulltext:"cosmic rays" and fulltext:"anisotropy"`: 16 hits, none an arrival-direction analysis. They are materials, lattice QCD (1706.07104, 2607.12508), dust emission, SAIP volumes, the Moriond 2006 volume, and "50 Years of QCD".
- `fulltext:"Beane" and fulltext:"numerical simulation" and fulltext:"arrival directions"`: 0.
- `fulltext:"Constraints on the Universe as a Numerical Simulation"`: 8. These are 1210.1847 itself, 1701.07161, 1210.8348, 1303.7476, 1703.00058, 2504.08461, 2105.11548 and the Entropy paper; all classified above.
- `fulltext:"simulation hypothesis" and fulltext:"cosmic ray"`: 5. These are Vazza 2025, Beane, a LArTPC paper (2010.08370), a dark-matter review (2310.20472) and "The Autodidactic Universe" (2104.03902); none is an analysis.
- `fulltext:"octahedral" and fulltext:"arrival directions"`: 3 (CMB topology thesis; SAIP volumes).
- `fulltext:"cubic harmonics" and fulltext:"cosmic ray"`: 0.
- `fulltext:"lattice" and "arrival directions" and "cubic" and "ultra-high-energy"`: 60 hits. The first 40 were reviewed by title: propagation codes, neutrino detectors, reviews and white papers; no lattice-anisotropy search.

arXiv search (all fields; titles, abstracts, comments):
- `"simulation hypothesis"`: 19 results, all listed. None analyzes cosmic-ray data. Checked in full: 2212.04921 (Neukart et al., philosophy; no cosmic-ray analysis) and 2404.16050 (Wolpert, CS theory).
- `"simulation argument"`: 12, none relevant.
- `"numerical simulation" universe lattice constraints`: 9, only 1210.1847 relevant.
- `cosmic rays "cubic symmetry"`: 0. `cosmic ray "cubic lattice"`: 1 (irrelevant, 1002.3408). `cosmic rays anisotropy "lattice spacing"`: 0. `octahedral anisotropy cosmic`: 3 (all CMB topology or simulation-box artefacts). `cosmic rays "simulated universe"`: 3 (irrelevant). `cosmic ray "discrete spacetime" anisotropy`: 0. `cosmic rays "rotational symmetry breaking"`: 1 (1210.1847 itself).

Semantic Scholar keyword search (mostly HTTP 429):
- "spacetime lattice anisotropy cosmic ray arrival directions search": 194 hits. The top 20 are standard anisotropy papers (Auger, TA, Fermi), none lattice-related.
- Four other queries were rate-limited ("cubic symmetry anisotropy ultra-high-energy cosmic rays arrival directions", "simulation hypothesis cosmic rays test", "octahedral symmetry cosmic ray anisotropy", "numerical simulation universe lattice cosmic ray anisotropy data").

General web searches (search engine), eight queries, including:
- "cosmic ray arrival directions 'cubic symmetry' lattice simulation hypothesis search Auger data"
- "'octahedral' OR 'cubic harmonics' anisotropy 'ultra-high-energy cosmic rays' arrival directions"
- "'Beane' 'Davoudi' 'Savage' cosmic ray anisotropy lattice test data analysis"
- "testing 'simulation hypothesis' with cosmic ray data arXiv lattice spacing anisotropy search"
- "'simulation hypothesis' 'Pierre Auger' anisotropy lattice test"
- "search for lattice-aligned anisotropy cosmic rays spherical harmonics ℓ=4 ℓ=6 cubic invariant preferred axes Lorentz violation"
- "Auger open data analysis ... github OR kaggle"
- "'Constraints on the universe as a numerical simulation' cited by cosmic ray anisotropy observational test"
- "'preferred directions' spacetime lattice UHECR ... 2024-2026"

Results: press coverage from 2012 (phys.org, MIT Technology Review, ScienceDaily, SciTechDaily; not usable as evidence), Vazza 2025, standard anisotropy papers, one GitHub repo on Auger direction reconstruction (abdul-samad021/auger_direction_reconstruction; not a lattice search), and Mlodinow & Brun 2025 (2506.20136). Full text of the last was checked: it bounds a cubic-lattice QCA using GRB timing and lab anisotropy limits, not UHECR directions.

### 4.3 Nearest analogues found (direction-dependent Lorentz violation, not O_h flux anisotropy)
- Klinkhamer & Risse, PRD 77, 016002 (2008). They bound nine nonbirefringent (partly anisotropic) modified-Maxwell parameters at the 10^-18 level from the absence of vacuum Cherenkov radiation. The note added in proof uses the directions of 29 real events.
- IceCube, PRD 82, 112003 (2010): a sidereal-modulation search for direction-dependent LV neutrino oscillations; none found.
- Auger, JCAP 01 (2022) 023: LIV with isotropic dispersion relations.

### 4.4 Conclusion
We found **no published analysis** that tests UHECR (or other astroparticle) arrival directions for a cubic/O_h-symmetric, lattice-aligned anisotropy, and none that confronts the Beane et al. anisotropy prediction with data. The generic multipole analyses (ℓ ≤ 20 or 64) contain the ℓ = 4 and 6 information implicitly, but form no O_h invariant and scan no orientations. The statement "to our knowledge, no such search has been published" is supported, with the explicit caveat that ADS full text, Google Scholar and the OpenAlex citation listing could not be queried from this environment. **Recommended before submission:** one manual ADS full-text query by a human, e.g. `full:"cubic symmetry" full:"arrival directions"` and `citations(bibcode:2014EPJA...50..148B)`, plus a Google Scholar "cited by" pass. Section 03 reached the same conclusion independently.

## 5. Our own computations (labelled as "we" in the `.tex`)
- The O_h-invariant harmonic degrees for ℓ ≤ 12 (0, 4, 6, 8, 10, 12×2), and invariance of K_4 = Y40 + sqrt(5/14)(Y44 + Y4−4) and K_6 = Y60 − sqrt(7/2)(Y64 + Y6−4). These were checked numerically on all 48 O_h elements, with error < 5e-15 (`/tmp/claude-0/papers/cubic.py`). The ℓ = 6 combination is not taken from a cited source. If a referee wants a citation, use the classic cubic-harmonics literature (Von der Lage & Bethe 1947, Phys. Rev. 71, 612), which we did not read (APS paywall).
- Noise of a single unit-normalized harmonic amplitude: sqrt(4π/N). For N = 1,387 this is 0.095, confirmed by a 2,000-trial Monte Carlo (0.0949) (`mc.py`).
- Event tallies from the public files: open-data SD summary CSVs (≥ 32 EeV: 155; ≥ 40: 86; ≥ 57: 24) and the Zenodo 2022 >32 EeV file (≥ 40: 1,387; ≥ 57: 411; ≥ 80: 95; ≥ 100: 35). These are raw counts without re-applying analysis-specific cuts.
- Iron rigidity at 46 EeV ≈ 1.8 EV; ℓ = 4 and 6 angular scales ≈ 45° and 30° (using Auger's 180°/ℓ convention).
- The remark that a heavy nucleus carries E/A per nucleon, weakening the E_max ~ 1/b matching (Beane et al. do not discuss nuclear primaries).

## 6. Gaps
1. Numerical C_4 and C_6 upper limits above the suppression energy are not published in text or tables. Options: digitize Auger 2024 Fig. 4(d), which gives approximate values only, or contact the collaboration.
2. There is no theory of the anisotropy amplitude ε(b, rigidity). Without it, a null result cannot become a bound on b. Section 03 argues that LIV bounds already suppress the threshold anisotropy for unimproved Wilson fermions.
3. We did not read an Auger-TA joint Xmax compatibility study, so the `.tex` makes no claim that the two experiments agree or disagree within systematics.
4. The JF12 random-field deflection numbers were not extracted, and UF23 excludes random fields.
5. TA has not released a full event list beyond the 72 events above 57 EeV (2008-2013) in ApJL 790 L21. We did not search exhaustively for later TA public lists.
6. The Greisen and Zatsepin-Kuzmin originals were not read (paywalls).
7. The published EPJ A version of Beane et al. was not compared with arXiv v2.

## 7. Suggested cross-links
- Section 03 (sec:lattice-liv) uses the same keys (Beane2014constraints, PierreAuger2020features, PierreAuger2022testing, Vazza2025astrophysical). Its threshold-anisotropy mapping (the "strongest robust constraint" discussion) should be referenced where 04 discusses interpretation; the `.tex` already does this.
- Section 09 (methodology): the proposed O_h search is a concrete example of a pre-registered, look-elsewhere-corrected test with mock-sky validation.
- The README's R1 description should state: (i) the full >32 EeV Auger list (2,635 events) is already public, so the proposal need not wait for the 30% release; (ii) the 30% release is planned, not yet out, as of 2026-09-27.
