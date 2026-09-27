# Report: 08-information (mass of information, "infodynamics", and the thermodynamics of information)

Files:
- `research/ledgers/08-information.md`: 64 claims.
  - 54 literature claims, C-08-001 to 054.
  - 10 "this work" claims, C-08-T01 to T10.
- `research/bib/08-information.bib`: 38 entries.
- `paper/sections/08-information.tex`: about 2,600 words plus one status table.
  - Compiled in a test build with no undefined citations or BibTeX warnings. The only warning is one
    overfull box of 1 pt.
  - Single-column 11 pt gives about 4.5 pages plus the table; two-column gives about 3 pages.

## 1. Coverage and verification levels

| Level | Count | Items |
|---|---|---|
| FULLTEXT | 56 | All numbers and characterizations used in the tex, including the 10 "this work" items |
| ABSTRACT | 7 | Bérut 2012; Parrondo 2015; Vopson 2019 (M/E/I); Vopson 2020 (information catastrophe); Vopson 2023 (infodynamics and simulation); Džaferović-Mašić 2021; Vopson 2022 (Applied Sciences) |
| METADATA | 1 | Kish 2007 (the original weighing report, known only through Kish & Granqvist 2013) |
| UNVERIFIED | 0 | |

How the full texts were reached. pubs.aip.org and aip.scitation.org sit behind a bot challenge, and
web.archive.org and ResearchGate are blocked by the egress proxy. We therefore used:
- Vopson 2022 protocol: published PDF on Newswise.
- Vopson & Lepadatu 2022: published PDF in the UCLan repository.
- Vopson 2025 gravity paper: published PDF hosted by INSPIRE.
- Vopson 2020 and 2021: arXiv.
- IPI Letters items: ipipublishing.org.
- MDPI (Entropy) papers, Hong 2016 and Simmonds 2020: Europe PMC (ebi.ac.uk) or PMC.
- Landauer 1961: Norton's copy of the IBM J. Res. Dev. 44 (2000) reprint, read as page images
  because the PDF is a scan with no text layer.

Not read in full:
- Vopson 2019 (M/E/I). Claims are at ABSTRACT level. The formula m_bit = k_B T ln2/c^2 is verified
  in the 2022 protocol paper, and the rationale in Vopson & Lepadatu 2022.
- Vopson 2023 (AIP Adv. 13, 105308). ABSTRACT only. Its content is taken from Vopson's own
  restatements in the 2025 gravity paper and in IPI Letters (2025).

## 2. Gaps and unverifiable items

1. Vopson 2019 and 2023 were not read in full. If an institutional route exists, read both, in
   particular:
   - the 2019 derivation, including whether it states a mechanism for how the Landauer energy is
     "stored";
   - the 2023 Hund's-rule and symmetry arguments.

   The section describes the 2023 content only as Vopson summarizes it in 2025.
2. Bérut et al. (Nature 2012) and Parrondo, Horowitz & Sagawa (Nat. Phys. 2015) are at ABSTRACT
   level. For numbers from Bérut, cite the open J. Stat. Mech. 2015 paper by Bérut, Petrosyan and
   Ciliberto (HAL ensl-01134137, downloaded), and add it to the ledger first.
3. Einstein 1905 could not be reached (Wiley and Augsburg return 403, fourmilab returns empty).
   We cite Okun (2008), which we read in full, for "the mass of a body is a measure of its energy
   content".
4. Hossenfelder's video. We verified its title and channel through YouTube oEmbed. Its content is
   quoted only from the transcript that Vopson reproduces in IPI Letters (2025). We did not watch
   the video. If exact quotation matters, someone should check the transcript against the video.
5. Not read at all:
   - Vopson's 2024–2026 extensions: blockchain, language diversity (J. Quant. Linguist. 2026),
     Euclidean polygons (Entropy 2026), biology (Entropy 2026).
   - Russev, "Conservation relationship bridging entropy and information" (Physics Open 2025;
     Elsevier is blocked).
   - Jaffe's Qeios commentaries (informal, openly reviewed).
   - Lairez 2025 (arXiv 2509.06957).
   - Norton 2005 (METADATA only; not cited in the tex).

   None is needed for the section's claims.
6. Review status of Todd (2026). IPI Letters labels it an "Article". We did not verify how it was
   reviewed. IPI Letters says it peer-reviews its regular articles, but its editor-in-chief is the
   author whose work is being discussed.
7. Temperature dependence of the electron mass (possible extra constraint). The protocol's Eq. (5)
   implies that the electron's rest mass depends on temperature. The fractional change is
   I k_B T ln2 /(m_e c^2) ≈ 4.5 × 10^-8 at 300 K and ≈ 6 × 10^-10 at 4 K. Penning-trap electron-mass
   determinations are, to our recollection, cryogenic and reach about 10^-11 relative precision.
   This is unverified. A comparison with
   room-temperature determinations might therefore constrain the conjecture. We have **not**
   verified any of the measurement literature, so nothing about this is in the tex. It may be worth
   a short follow-up (for example CODATA, and Sturm et al., Nature 2014).

## 3. Search log for "we are not aware" statements

The tex states that no execution of the annihilation protocol is reported and that no weighing
reaches the required sensitivity (C-08-T10). The searches behind this were:
- Semantic Scholar API: all 27 items citing doi:10.1063/5.0087175 (the protocol), and the citers of
  the 2019, 2022, 2023 and 2025 papers. None reports an experiment.
- INSPIRE: `refersto:recid:2074086` (protocol) and `refersto:recid:1975314` (2021). The citers
  found were Burgin & Mikkilineni, Vopson 2025, Denis 2024 (IPI Letters), Xu 2022 and others. None
  is experimental.
- Crossref bibliographic queries:
  - "Comment on second law of information dynamics"
  - "Comment on mass-energy-information equivalence principle"
  - "critique second law of infodynamics"
  - "mass of information erasure bound experiment"

  These found no formal comment in AIP Advances.
- Web searches: "experimental search infrared photons positron annihilation information erasure
  Vopson test result", and variants.

We found no peer-reviewed comment published in AIP Advances itself. The peer-reviewed critiques are:
- Lairez 2024, Entropy
- Burgin & Mikkilineni 2022, Information
- Crecraft 2024/2025, Entropy (a critical reformulation)

The informal critiques are Hossenfelder's video (2025) and Jaffe's Qeios commentaries. Vopson's
replies appeared as editor-screened "News and Views" items in IPI Letters.

## 4. Independent technical assessment ("this work")

### 4.1 SARS-CoV-2 re-analysis (C-08-T01 to T04)

Data. We fetched the ten accessions of Vopson & Lepadatu's Table I with NCBI E-utilities efetch
(db=nuccore, FASTA):
MN908947, LC542809, MT956915, MW466798, MW294011, MW679505, MW735975, OK546282.1, OK104651.1,
OL351371.1.

All ten have length 29,903 and contain no IUPAC ambiguity codes. The scripts are
`/tmp/claude-0/papers/sars/analyze.py` and `analyze2.py`; they are not in the repo and should be
moved there if the audit becomes part of the paper.

| Accession | A | C | G | U | H (plug-in, bits) | Published | Differences from reference | toward commoner base / toward rarer base |
|---|---|---|---|---|---|---|---|---|
| MN908947.3 | 8954 | 5492 | 5863 | 9594 | 1.9570243 | 1.9570243 | 0 | 0/0 |
| LC542809.1 | 8954 | 5489 | 5862 | 9598 | 1.9569197 | 1.9569197 | 4 | 4/0 |
| MT956915.1 | 8955 | 5489 | 5862 | 9597 | 1.9569230 | 1.9569230 | 7 | 5/2 |
| MW466798.1 | 8956 | 5491 | 5860 | 9596 | 1.9569327 | 1.9569327 | 10 (published: 9) | 6/3 |
| MW294011.1 | 8957 | 5486 | 5856 | 9604 | 1.9567058 | 1.9567058 | 19 | 15/4 |
| MW679505.1 | 8951 | 5479 | 5863 | 9610 | 1.9566630 | 1.9566630 | 25 | 19/6 |
| MW735975.1 | 8955 | 5476 | 5862 | 9610 | 1.9565714 | 1.9565714 | 26 | 21/5 |
| OK546282.1 | 8951 | 5479 | 5859 | 9614 | 1.9565675 | 1.9565675 | 32 | 25/7 |
| OK104651.1 | 8952 | 5474 | 5860 | 9617 | 1.9564591 | 1.9564591 | 41 (published: 40) | 32/8 |
| OL351371.1 | 8954 | 5470 | 5856 | 9623 | 1.9562614 | 1.9562614 | 49 | 41/8 |

Key algebra. Let H = −Σ p_i log2 p_i. Moving one site from base a to base b (δ = 1/N) gives, to first
order, ΔH = δ log2(p_a/p_b). At the reference composition (A 0.2994, C 0.1837, G 0.1961, U 0.3208)
the per-substitution changes, in bits, are:

| Substitution | ΔH | Reverse | ΔH |
|---|---|---|---|
| C→U | −2.69e-5 | U→C | +2.69e-5 |
| G→U | −2.38e-5 | U→G | +2.38e-5 |
| C→A | −2.36e-5 | A→C | +2.36e-5 |
| G→A | −2.04e-5 | A→G | +2.04e-5 |
| A→U | −3.3e-6 | U→A | +3.3e-6 |
| C→G | −3.2e-6 | G→C | +3.2e-6 |

Under a uniform null (site uniform, target uniform among the other three bases), E[ΔH] is
+3.9 × 10^-6 bits per substitution. The observed mean is −1.56 × 10^-5 per SNP. The published sign
therefore follows from the dominance of C→U and G→U changes (Simmonds 2020).

Estimators. With N fixed and m = 4:
- Miller–Madow adds 3/(2N ln2) = 7.2 × 10^-5 bits, the same for all ten genomes.
- Block (conditional) entropies:
  - order 2: 1.925237 → 1.924579
  - order 3: 1.918212 → 1.917682

  Both fall overall, but not monotonically.
- Compression estimates (lzma extreme, bz2 -9, zlib -9) are 2.18–2.39 bits/base, i.e. worse than
  2 bits. Their granularity is 8 bits/29,903 = 2.7 × 10^-4 bits/base, and they show no trend.

Conclusion: for this dataset the estimator is not what matters. The null model and the sequence
selection are.

### 4.2 Calorimetry versus the temperature-dependent information mass (C-08-T05)

The protocol's Eq. (2) gives Δm_inf = I (m N_A/A)(N_e + 3(N_p + N_n)) k_B ΔT ln2 / c^2.
- Per mole of Cu, the implied information heat capacity is 1.509 × 219.5 × k_B ln2 × N_A =
  1909 J mol^-1 K^-1.
- Measured C_p(298 K) = 24.47 J mol^-1 K^-1, from the NIST WebBook Shomate parameters (Chase 1998).
  The ratio is ≈ 78.
- Δm_inf c^2 for 1 kg and ΔT = 100 K is 2.99 MJ. The measured ΔH(300→400 K) is 2489 J/mol, or
  3.92 × 10^4 J/kg.

The premises are E = mc^2, which the M/E/I rationale itself invokes, and energy conservation.

Caveat: a proponent could say that information energy is not supplied by the heater. The tex
therefore says "taken literally". The papers do not specify any other energy source.

Side note: the ordinary relativistic mass increase of the heated block is ΔH/c^2 ≈ 4.4 × 10^-13 kg.
This contradicts the protocol's sentence that the physical mass "does not change with the
temperature", but the correction is small (≈ 1/80 of the claimed effect).

Minor internal inconsistency: the protocol's N_b = 29.8 × 10^26 bits for 1 kg Cu should be
3.14 × 10^27 from its own Eq. (1). The quoted Δm_inf = 3.33 × 10^-11 kg matches the latter (we get
3.34 × 10^-11).

### 4.3 Symmetric memory and the digital "infodynamics" example (C-08-T06, T09)

These rest only on cited standard results:
- Landauer's symmetric well (C-08-005).
- Esposito & Van den Broeck: F = E − TS and F − F_eq = T D (C-08-012).
- Kish & Granqvist: equal energy of the two states (C-08-017).
- Okun: m = E_0/c^2 (C-08-033).
- Jun et al. and Bennett: the erasure work is dissipated as heat (C-08-009, 006).

For the digital example:
- Landauer says the entropy of the information-bearing degrees of freedom rises by up to Nk ln2 as
  stored information thermalizes (C-08-003).
- With W = 0 and ΔF_eq = 0, Eq. (12) of Esposito & Van den Broeck gives ΔI = −Δ_iS ≤ 0.
- Crecraft and Todd reach the same conclusion by different routes.

Minor internal inconsistency: Vopson & Lepadatu print K_a = 8.75 × 10^8 J/m^3 (confirmed from the
page image). Their stated K_aV/k_BT ≈ 40 at V ≈ 1.9 × 10^-27 m^3, and τ = 1.5 s at V = 10^-27 m^3,
both require 8.75 × 10^7 J/m^3. This is not in the tex.

### 4.4 "Information per particle" (C-08-T07)

This is the entropy of the species label for a particle drawn at random from the cosmic mixture. It
changes if the mixture changes: a pure-H population gives 1 bit, and a proton-only population gives
0 bits. So it cannot be an intrinsic property that each particle "stores about itself".

### 4.5 Gravity toy model (C-08-T08)

H depends only on N_1/N, so it is invariant under all permutations of the cells. The derivation
obtains a distance dependence by construction:
- a step Δr = ħ/(mc);
- ΔS = k_B ln2 H per step, stated under the assumption H_N = H_{N−1};
- M = N H k_B T ln2/c^2;
- N ≈ R^2/L_P^2.

Also, the "temperature" T is eliminated between Eqs. (8) and (12) without being specified
physically.

## 5. Controversies and embarrassment risks

1. **Tone and fairness.** The tex quotes Vopson's own caveats: the protocol's "strong assumption";
   the admission that M/E/I "has no empirical validation yet"; the question mark in the gravity
   title. Keep these in any edit. Do not use words like "pseudoscience". Hossenfelder's phrase
   "shouldn't have been published" appears only as her quoted opinion.
2. **IPI Letters facts.** The tex says Vopson edits IPI Letters and that "News and Views" items are
   editor-screened. Both facts are verbatim from the journal's pages. Keep the wording neutral, as
   information about review status, not as an insinuation.
3. **Lairez.** He is used only for the constant-internal-energy point. His abstract also says that
   thermal energy ("temperature") is not stored as rest mass. That is non-standard for the
   invariant mass of a composite body, and the tex deliberately does not use it. He also rejects
   Landauer's principle as a general principle, which is a minority view (see Bennett 2003 and the
   experiments). The tex separates the two. A thermodynamics referee may still object if Lairez is
   presented as mainstream.
4. **Ostrowski et al.** They call all slopes "statistically significant". Their own robust-regression
   slopes for HIV and influenza are 1.3σ and 1.4σ from zero, and their χ^2 values are 10^7–10^10.
   The tex reports the numbers without adjectives.
5. **Our calorimetry argument** (C-08-T05) is new, as far as we know; we found no one making it.
   It is phrased conditionally ("taken literally, including E = mc^2 and energy conservation"). An
   internal reviewer should re-derive it before submission.
6. **"This work" reproduction.** The table reproduction is exact. The difference counts use a
   position-wise comparison, valid because all lengths are equal, but no alignment was done. Two
   counts differ by one from the published SNP counts. This is harmless for the argument, and it is
   noted in the ledger.
7. **Docs mismatch.** `docs/literature-survey.md` says the public criticism "focuses on the entropy
   definitions, the estimators, and whether 'information entropy' is used consistently". It does
   not. Hossenfelder's critique of the gravity paper is about the symmetry and maximum of binary
   entropy; she does not discuss estimators. The survey also cites the IPI response as a critique
   venue. Suggest correcting the survey text; we did not edit it because it is another file.
8. **Press releases.** We did not cite any: phys.org, ScienceAlert, The Conversation pieces by
   Vopson, and Portsmouth news releases were all found and ignored. If the paper later discusses
   media reception, those items belong in that section, not here.

## 6. Concrete reproducible-audit plan (survey item R3)

**A. Genomic "infodynamics" (priority; low cost).**
1. Data:
   - (i) The 10 Table I accessions (done; exact reproduction).
   - (ii) NCBI Virus SARS-CoV-2 complete genomes with collection dates. Use the NCBI Datasets CLI.
     Avoid GISAID because of its terms of use.
   - (iii) Control viruses:
     - HIV-1 and influenza A (the Ostrowski et al. datasets);
     - Ebola virus, which Simmonds reports shows no C→U/U→C asymmetry. It is therefore a natural
       negative control: we predict no systematic decrease.
2. Preprocessing: align to MN908947.3 with nextclade or minimap2, and mask ambiguous bases and
   indels. Report results both with and without masking. Record the date and the lineage.
3. Estimators, per genome and per time bin:
   - plug-in H1;
   - Miller–Madow;
   - NSB (Nemenman et al. 2002);
   - block and conditional entropies for k = 1..6;
   - DNA-specialized compression (e.g. GeCo3 or XM) as well as xz and zstd. Report compressed-size
     differences, not absolute bits per base.
4. Null models, each simulated forward from the reference with the observed number of
   substitutions:
   - (N0) uniform substitutions;
   - (N1) the empirical 12-type SARS-CoV-2 spectrum, estimated from a phylogeny (e.g. an UShER
     mutation-annotated tree, or Bloom et al. 2023, MBE, whose full text still needs reading);
   - (N2) N1 plus the 5′/3′ APOBEC context dependence (Simmonds 2020).

   Test: compare the observed slope dH/dM with the null distributions. Prediction: N1 and N2
   reproduce the slope, and N0 gives a positive slope.
5. Cross-virus test: the sign and magnitude of dH/dM should track Σ f_{a→b} log2(p_a/p_b), computed
   from each virus's spectrum and composition. This gives a quantitative, falsifiable version of the
   "mutational bias" explanation.
6. Selection check: repeat the analysis on random samples of sequences, not only on hand-picked
   ones with "incremental" SNP counts.

**B. Digital example.** Re-run a granular-film relaxation. Lepadatu's BORIS code is the one cited;
any kinetic Monte Carlo of Néel–Arrhenius flips will do. Track two quantities:
- (i) the Shannon/Gibbs entropy of the ensemble of bit states;
- (ii) the mutual information between the current state and the written record.

Show that (i) rises by up to N ln2 while (ii) falls to zero, and compare both with Vopson &
Lepadatu's S_inf.

**C. Gravity toy model.** Publish a 20-line script showing that H(N_0, N_1) is invariant under
permutations. The only changes come from merging, which is independent of distance.

**D. M/E/I.**
- (i) Put the calorimetry bound (Sec. 4.2) into a short appendix with its inputs.
- (ii) Search the positron-annihilation spectroscopy literature for any far-IR coincidence
  measurements, so that a "not performed" statement can be made more firmly.
- (iii) Optionally, turn the electron-mass temperature dependence (Sec. 2, item 7) into a
  literature-based bound.

## 7. Suggested cross-links

- **"It from bit" and digital-physics background** (Wheeler; Lloyd): Vopson's rationale invokes
  Wheeler (Vopson & Lepadatu 2022, Sec. I).
- **Entropic and emergent gravity, holography** (Verlinde 2011; Bekenstein): link from our gravity
  paragraph. Vopson 2025 frames his model as an extension of Verlinde.
- **Methodology / falsifiability section:** the protocol's explicit escape clause is a clean example
  of a prediction that does not risk refutation.
- **Complexity and compression section:** Vopson equates low Shannon entropy with "data
  compression" by a simulator. Distinguish zeroth-order Shannon entropy from algorithmic (Kolmogorov)
  complexity. Vopson's own example "0101010101" has maximal H1 but is highly compressible.
- **Reception and media section:** press coverage of the "fifth state of matter" and the "new law of
  physics" (not cited here).
