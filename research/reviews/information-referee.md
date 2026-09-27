# Referee report: Section 8, "Information-theoretic proposals: the mass of information and 'infodynamics'"

Scope: `paper/sections/08-information.tex` (cited below as `08:LINE`), with the ledger
`research/ledgers/08-information.md` (`L:LINE`), the report `research/notes/08-information-report.md`
(`R:LINE`) and the scripts `research/notes/08-scripts/`. I also checked how the section is summarized in
`00-abstract.tex`, `00-introduction.tex:20`, `09-methodology.tex:153` (row H-info) and
`10-discussion.tex:11,24`.

Referee expertise: statistical mechanics, the thermodynamics of information (Landauer's principle and
its experimental tests, stochastic thermodynamics, entropy estimation), with working knowledge of
molecular evolution and mutation spectra.

---

## 1. Summary judgement and recommendation

This is a careful and mostly fair section. Every number I recomputed is right. The ten SARS-CoV-2
entropies reproduce to the last printed digit. The per-substitution algebra and the null-model value
are right, and I give a closed form for the null value below. The copper arithmetic is right, and the
section uses Vopson's own premises (1.509 bits per particle; 219.5 electrons plus quarks per Cu atom;
Δm_inf linear in T at a fixed number of bits). The symmetric-memory argument is the standard textbook
position and is correctly supported by Kish & Granqvist and by Lairez. The section quotes Vopson's own
caveats, and it keeps peer-reviewed and informal critiques apart better than most papers on this topic.

An expert referee would still find five weaknesses.

1. **The genomic argument shows a mechanism but does not yet discriminate between hypotheses.** The
   statistic "41 of 49 substitutions move a site toward a more common base" is exactly what Vopson's
   "law" also predicts. A sympathetic reader will answer that mutational bias is the *mechanism* of
   the law, not a refutation of it. The section has to state the predictions on which "biased
   substitution process" and "second law of infodynamics" differ. They do differ: saturation at the
   mutational-equilibrium composition, reversal of sign, and a slope fixed by the spectrum. The
   abstract's verb "show" is too strong for ten genomes and an in-sample spectrum.
2. **One sentence of the symmetric-memory paragraph conflates three different processes.** These are
   resetting an unknown bit, resetting a known bit, and spontaneous thermalization. As written, the
   sentence contradicts the section's own Landauer bullet (`08:27-29`). A thermodynamics referee will
   notice this first. The fix is one sentence, based on the two-state partition function.
3. **The calorimetry argument will be called a straw man unless it rests on Vopson's own
   energy-conservation equations.** Protocol Eqs. (9)–(10) conserve the "information energy" in
   annihilation. Present the argument as a trilemma, show that it is robust to Vopson's alternative
   inputs (at least 28× in every variant), and optionally add the third-law point, which is decisive.
4. **Summaries elsewhere in the paper contradict the section.** Row H-info in Sec. 9 says the
   conjecture is "untested". Sec. 10 calls calorimetry a "target". Sec. 8 says the conjecture
   "conflicts with calorimetry".
5. **The characterizations of Hong 2016, Bérut 2012, Jun 2014, Ostrowski 2024 and Todd 2026 need
   small corrections.** There is also an error in the ledger and report: the claimed one-SNP
   discrepancy with the published counts does not exist.

**Recommendation: major revision, in framing only.** No new data are needed. I estimate one to two days
of work. None of the issues is fatal. All three original claims survive, with caveats.

| Original claim | Verdict |
|---|---|
| (a) SARS-CoV-2 reproduction and the C→U argument | **CORRECT WITH CAVEATS** |
| (b) Stored-bit rest mass in a symmetric memory | **CORRECT WITH CAVEATS** |
| (c) Copper heat-capacity conflict | **CORRECT WITH CAVEATS** |

Issue counts: FATAL 0, MAJOR 5, MINOR 14, NIT 7.

---

## 2. Verdicts on the three original claims, with independent calculations

### (a) SARS-CoV-2 entropies and C→U bias: CORRECT WITH CAVEATS

**Reproduction.** I ran `fetch_seqs.sh` in a scratch directory. It sends no email and no API key, and
the result is byte-identical to `/tmp/claude-0/papers/sars/seqs.fasta`. I then wrote my own analysis
script, independent of `analyze*.py`.

- All ten records have 29,903 nt and contain only A/C/G/T.
- The plug-in entropies agree with Vopson & Lepadatu's Table I to within 4×10⁻⁸ bits in every case,
  i.e. to rounding in the seventh decimal.
- Reference composition (MN908947.3): A 8954, C 5492, G 5863, U 9594, i.e. p = (0.29943, 0.18366,
  0.19607, 0.32084).

**Per-substitution change (analytic).** Write H = −Σ (n_i/N) log₂(n_i/N). Moving one site from base a
to base b gives

  ΔH = N⁻¹ log₂(p_a/p_b) + O(N⁻²),

where the second-order term is −(1/(2N² ln2))(1/p_a + 1/p_b) ≈ −7×10⁻⁹ bits, which is negligible. The
table compares the exact finite difference with the first-order formula.

| Substitution | Exact ΔH (bits) | First-order ΔH (bits) |
|---|---|---|
| C→U | −2.6921e-5 | −2.6914e-5 |
| G→U | −2.3767e-5 | −2.3760e-5 |
| C→A | −2.3590e-5 | −2.3583e-5 |
| G→A | −2.0436e-5 | −2.0429e-5 |
| A→U | −3.336e-6 | −3.331e-6 |
| C→G | −3.162e-6 | −3.154e-6 |

The reverse substitutions have the opposite sign. The section's value of −2.7×10⁻⁵ for C→U (`08:231`)
is correct.

**Null model.** Take the site uniformly at random and the target uniformly among the other three bases
(a Jukes–Cantor-type null). The expected change per substitution then has a closed form that the paper
should state:

  E[ΔH] = (1/3N) Σ_a p_a Σ_{b≠a} log₂(p_a/p_b) = (4/3N)·[D(u‖p) + D(p‖u)] ≥ 0,

where u is the uniform distribution. The bracket is the Jeffreys (symmetrized Kullback–Leibler)
divergence between the composition and uniform. For SARS-CoV-2 it equals 0.08679 bits, so
E[ΔH] = +3.870×10⁻⁶ bits (first order) and +3.863×10⁻⁶ bits (exact). The section's +3.9×10⁻⁶
(`08:237`) is correct.

Two further points strengthen the argument:

- The identity shows that *any* unbiased substitution process raises H, for *any* non-uniform genome.
  This is the quantitative form of Crecraft's remark.
- A transitions-only null (sites uniform, each base going to its transition partner) also gives a
  positive value, +5.8×10⁻⁶ bits. So the sign of the null does not depend on the choice between
  Jukes–Cantor and Kimura-type models.

**Observed changes.** Total ΔH (OL351371.1 minus reference) is −7.6286×10⁻⁴ bits. Divided by 49
differences this is −1.557×10⁻⁵ bits per SNP, matching the section's −1.6×10⁻⁵. The observed
differences in OL351371.1 are:

| Change | Count |
|---|---|
| C>U | 22 |
| G>U | 9 |
| G>A | 5 |
| A>G | 4 |
| U>C | 3 |
| A>U | 2 |
| C>G | 2 |
| U>G | 1 |
| C>A | 1 |

This gives 22 of 49 C→U, and 41 of 49 toward a commoner base (22+9+5+2+2+1). Both numbers are
confirmed. U rises by 29 and C falls by 22, also confirmed. Summing the first-order terms over the
observed differences gives −7.584×10⁻⁴ bits, versus −7.629×10⁻⁴ exact.

Note that this agreement is an algebraic identity, not evidence (see M1).

**New number the section should add: the null expectation of the "41 of 49" statistic.** Under the
uniform null, the probability that a substitution moves a site toward a commoner base is

  p_C·1 + p_G·(2/3) + p_A·(1/3) = 0.414.

The observed 41/49 = 0.84 has a binomial tail probability of 1.5×10⁻⁹. Pooling the distinct differences
across all nine genomes gives 119/148 = 0.80, with a spectrum dominated by C→U (75) and G→U (24). The
spectrum-weighted expectation from that pool is −1.54×10⁻⁵ bits per substitution. This is the same
order as Ostrowski et al.'s independent large-sample slope, −0.97×10⁻⁵ (least squares) and −1.15×10⁻⁵
(robust).

**SNP counts: the ledger and report are wrong, and the reality is better.** Both
`research/notes/08-scripts/analyze.py` and my own script give 9 differences for MW466798.1 and 40 for
OK104651.1. These match the published SNP counts exactly. The claims of "10 (published: 9)" and
"41 (published: 40)" at `R:124,129` and `L:479` ("differ by one") are erroneous. The report's own
toward/away columns sum to 9 and 40.

**Miller–Madow.** The remark is correct. The correction is (m̂−1)/(2N) nats. With m̂ = 4 for every genome
and N = 29,903 fixed, it is a constant 3/(2N ln2) = 7.237×10⁻⁵ bits, so it cannot change a trend. It is
the Paninski citation that supplies the formula; the constancy is our own inference, and the text
should say so (N7).

The more telling point is missing. Suppose one adopts the i.i.d. sampling model under which "estimator
bias" is meaningful. The plug-in standard error is then √(Var[−log₂ p]/N) = √(0.1205/29903) =
2.0×10⁻³ bits. That is 2.6 times the *entire* 22-month decline of 7.6×10⁻⁴ bits. The trend is visible
only because the genomes are nearly identical, so each ΔH is a deterministic function of the handful of
substitutions. Estimation theory is simply the wrong frame here, which reinforces the section's
conclusion that the estimator is not the issue.

**Caveats that make this "with caveats":** see M1 (discrimination between hypotheses, and the abstract),
m6 (substitution spectrum versus mutation spectrum; sources for the 2021 spectrum), m7 (reference
backfilling), m10 (Todd) and m13 (ledger).

### (b) Symmetric memory carries no stored rest mass: CORRECT WITH CAVEATS

**Physics.** Consider N non-interacting bits whose logical states are degenerate, with high barriers
and local equilibrium within each well. The mean energy in either well is the same, because the wells
are identical under the symmetry. Hence:

- A bit localized in one well (a known, written bit) has the same U as the thermalized bit.
- Its entropy is lower by k ln2 and its free energy higher by kT ln2.
- By Esposito & Van den Broeck, F − F_eq = kT·D[ρ‖ρ_eq], and D = ln2 exactly for ρ = 2ρ_eq restricted
  to one well.

The rest mass of a composite body is its rest-frame energy divided by c² (Okun). Free energy is not an
energy content, so no mass difference follows. This is correct and standard.

The crispest form is the partition function of one degenerate bit: Z = 2, F = −kT ln2, S = k ln2,
U = 0. The quantity kT ln2 is TS. It is not U.

M/E/I assigns a mass of TS/c², i.e. N·kT ln2/c² for a memory whose data are unknown to the observer.
In the same bookkeeping, a memory erased to all zeros has S = 0. This reproduces Vopson's sign ("full
heavier than erased"). It also shows that the conjecture identifies TS, not U, with rest energy, which
is Lairez's diagnosis. Two consequences follow:

- Had one identified F with rest energy, the sign would reverse: the erased memory would be heavier.
- A memory full of *known* data and an erased memory both have S = 0 relative to their writer. So the
  predicted mass difference would be observer-relative, which is untenable for a rest mass.

**Do the cited supports say this?**

- **Kish & Granqvist 2013** (Proc. IEEE, a "Point of View" column; I read arXiv 1309.7889 §II). Yes.
  "Though this energy is dissipated by the writing operation during changing the state, the energy and
  the mass of the system after the operation remain the same as their original values." More directly:
  "the increase of entropy is relevant for the energy dissipation (which is then released to the
  environment) rather than for the change of the energy and mass of the system." For the asymmetric
  (flash) case they obtain m ≈ (kT/c²)·ln(N t_m/τ) ≈ 3.4×10⁻³⁶ kg, whose sign depends on convention.
  The section's statement at `08:145-146` is accurate.
- **Lairez 2024** (Entropy 26, 337; I read arXiv 2401.15104 §I.B). Yes. At constant T the internal
  energy of independent entities is constant, and "any monothermal variation of entropy interpreted in
  terms of potential energy stored under the form of rest mass cannot be localized in such a system,
  but only in its surroundings." However, see M5: the same paper asserts that thermal energy
  ("temperature") is not stored as rest mass. That is wrong, and it conflicts with the section's own
  use of ΔH/c² at `08:156`.

**Caveats:**

- The erasure sentence at `08:143-145` (M2).
- Vopson's phrase "stored at equilibrium" (`08:72`) deserves a one-line rebuttal. A written bit is a
  metastable, ergodicity-broken, non-equilibrium state. Only the thermalized bit is at equilibrium.
- Energy equality of the two wells is exact for mirror-symmetric wells. For wells with equal minima
  but different curvature it holds in the harmonic approximation (U = E_min + kT/2 per quadratic
  degree of freedom).

### (c) Copper heat capacity: CORRECT WITH CAVEATS

**Premises checked against the protocol** (Vopson 2022, AIP Adv. 12, 035311; full text read):

- **The particle count.** Eq. (1) gives N_b = I·(mN_A/A)·(N_e + 3(N_p + N_n)), with "the factor of 3
  [accounting] for the fact that each proton and each neutron are made up of three quarks". For Cu,
  N_e = N_p = 29 and N_n = 34.5, so 29 + 3·63.5 = **219.5 electrons plus quarks per atom**. Confirmed.
- **The bits per particle.** The protocol states: "If each subatomic elementary particle contains
  I = 1.509 bits". This is Vopson's figure (2021: H(0.483, 0.29, 0.225) = 1.5093 bits; I recomputed it).
  Confirmed.
- **Linearity in T.** Eq. (2) gives Δm_inf = I·(mN_A/A)·k_B·ΔT·ln2·(…)/c² at fixed N_b, and the text
  says "the mass of information is temperature dependent". So m_inf = N_b·k_B·T·ln2/c² is linear in T
  at a fixed number of bits. Confirmed.
- **Energy conservation.** Is identifying Δm·c² with heat from the heater legitimate? **Yes, on
  Vopson's own terms**, but the section must say so explicitly. The protocol conserves the
  information energy in annihilation. Its Eq. (9) is
  E_tot = m_e c² + m_e+ c² + I_e− k_BT ln2 + I_e+ k_BT ln2, and Eq. (10) says "the information
  content must also be conserved by producing two information energy photons". The weighing test also
  requires Δm_inf to be real inertial/gravitating mass. A body whose rest energy rises by Δm·c² when it
  is heated must receive that energy from somewhere, and in a calorimeter the only source is the
  heater. The argument is therefore a trilemma for the proponent:
  1. give up energy conservation, which the annihilation prediction relies on;
  2. give up E = mc², which the M/E/I syllogism relies on; or
  3. accept a heat capacity 78 times the tabulated one.

  This is not a straw man.

**Recomputation.**

- Shomate/JANAF: C_p(298.15 K) = 24.4705 J mol⁻¹ K⁻¹; ΔH(300→400 K) = 2489.2 J mol⁻¹ =
  3.917×10⁴ J kg⁻¹.
- C_inf = 1.509 × 219.5 × R ln2 = **1908.9 J mol⁻¹ K⁻¹**. The ratio to C_p is **78.0**.
- N_b(1 kg) = 3.139×10²⁷, against the protocol's printed 29.8×10²⁶, as the report notes.
  Δm_inf = 3.342×10⁻¹¹ kg and Δm·c² = 3.004 MJ, which is 76.7 times the enthalpy increment.
- The ordinary thermal mass is ΔH/c² = 4.36×10⁻¹³ kg, so the ratio is 76.7.

All of the section's numbers are confirmed (`08:151-157`).

**Robustness (the paper should add this).** The conflict survives every variant Vopson has used:

| Variant | C_inf (J mol⁻¹ K⁻¹) | Ratio to C_p |
|---|---|---|
| I = 1.288 bits, counting {p, n, e} (92.5 per atom) | 687 | 28 |
| I = 1 bit, counting electrons + quarks | 1265 | 52 |
| I = 1.509 bits, counting {p, n, e} | 804 | 33 |

Only a drastic change, such as one bit per *atom* (5.8 J mol⁻¹ K⁻¹, 24% of C_p), would bring it
within range.

**Stronger, optional third-law argument.** C_inf is independent of T. It would therefore dominate at
low temperature, where the specific heat of Cu follows γT + βT³, with γ ≈ 0.69 mJ mol⁻¹ K⁻² and
θ_D ≈ 343 K. From those values I estimate C_Cu(1 K) ≈ 0.74 mJ mol⁻¹ K⁻¹, so C_inf would exceed it by
~2.6×10⁶. A T-independent heat capacity also makes S = ∫C/T dT diverge logarithmically as T → 0, which
violates the third law. Copper is a standard reference material for low-temperature calorimetry
(Martin 1973, verified below). The γ and θ_D values above are my textbook values. The authors must read
Martin 1973 and take the numbers from it before using this argument.

**Caveats:**

- Use ΔU rather than ΔH for the rest-energy comparison. The difference, pΔV, is ~10⁻² J and
  negligible, but a referee will ask.
- Report one consistent ratio: ~78 for the heat capacity at 298 K, ~77 for the 300–400 K example. At
  present the text says "78" in one place and "about 80" in another (`08:152,156`).
- Frame the argument as the trilemma above (M3).

---

## 3. Numbered issues

### MAJOR

**M1. The genomic argument must state what distinguishes "mutational bias" from the "law"; the
abstract overclaims.**

- *Location:* `08:226-243`, `08:266-268`, `08:302`, `00-abstract.tex:1` ("show that the reported
  decrease follows from the known mutational bias"), `00-introduction.tex:20`.
- *Evidence:* "41 of 49 move a site toward a more common base" is precisely what "genomes mutate so as
  to reduce their information entropy" (Vopson 2022, *Appl. Sci.*) predicts. Summing the observed
  per-substitution ΔH reproduces the total ΔH only as an algebraic identity. The report itself notes
  that the discriminating null models (N1/N2 with an independently estimated spectrum) have not been
  run (`R:276-287`).
- *What discriminates the hypotheses:*
  1. Under a Markov substitution process the composition relaxes toward the stationary composition π
     of that process, so H tends to H(π). A genome more skewed than π should show *increasing* H.
  2. The trend must saturate. It cannot continue as a law with ∂H/∂t ≤ 0 indefinitely.
  3. The slope must follow Σ_ab f_ab log₂(p_a/p_b)/N across viruses and hosts, with f taken from an
     independently estimated spectrum.
  4. The substitutions must show APOBEC and ROS sequence context.

  None of this appears in the text.
- *Fix:*
  - Add after `08:237`: "The expected change under unbiased substitutions is
    (4/3N)[D(u‖p)+D(p‖u)] > 0 for any non-uniform composition, so a decrease requires a biased
    spectrum. Under such a spectrum the composition relaxes toward the stationary composition of the
    substitution process. H therefore decreases only while the genome is less skewed than that
    stationary composition. It must level off, and it would increase for a genome more skewed than its
    mutational equilibrium. The entropic 'law' predicts neither saturation nor reversal. Under a
    uniform null, 41% of substitutions would move toward a commoner base, against 41 of 49 observed
    (binomial p ≈ 10⁻⁹)."
  - In the abstract, replace "and show that the reported decrease follows from the known mutational
    bias of the virus" with "and show that its sign and size are accounted for by the virus's
    C→U-dominated substitution spectrum, whereas unbiased substitutions would raise the entropy".
  - In `08:227-228`, replace "The decrease is then a direct consequence of" with "The decrease is
    accounted for by".

**M2. The erasure-energy sentence conflates reset of an unknown bit, reset of a known bit, and
thermalization.**

- *Location:* `08:143-145`, "The k_BT ln 2 that appears on erasure is supplied as work by the eraser
  and leaves as heat. It is not released from the bit's rest energy."
- *Evidence:* The section's own bullet `08:27-29` (Landauer) says that resetting a *known* bit costs
  no heat. Bérut et al. (J. Stat. Mech. 2015, footnote 1) note that writing into an unknown memory is
  the same operation as reset. Spontaneous thermalization of a written bit (Vopson's "self-erasure")
  involves W = Q = 0 on average; the kT ln2 of free energy is lost as entropy production. Recovering
  it as work requires drawing kT ln2 of heat *from* the bath (Szilard engine; Koski 2014; Toyabe 2010).
- *Fix:* Replace the two sentences with: "In a symmetric memory the mean energy is the same at every
  stage (writing, storage, spontaneous thermalization, reset). For one degenerate bit Z = 2,
  F = −k_BT ln2, S = k_B ln2 and U = 0, so k_BT ln2 is TS, not energy. The Landauer cost appears only
  in exchanges with the environment: as work converted to heat when a bit of unknown value is reset,
  as heat drawn from the bath when a known bit is used to extract work, or as entropy production when
  a written bit thermalizes. At no stage is it released from the memory's rest energy. M/E/I in effect
  identifies TS with rest energy."

**M3. The calorimetry argument must be anchored in the protocol's own energy conservation and shown to
be robust.**

- *Location:* `08:147-157`; `L:498-503`.
- *Evidence:* Protocol Eqs. (9)–(10), quoted in §2(c) above; the robustness table in §2(c). The report
  itself anticipates the reply that information energy is not supplied by the heater (`R:174-175`).
  The text answers it only with "taken literally".
- *Fix:* Replace `08:147-150` ("Take the conjecture literally … when the body is heated.") with: "The
  protocol treats the information energy I k_BT ln2 as conserved energy, which annihilation converts
  into photons (its Eqs. (9)–(10)), and treats Δm_inf as weighable mass. If energy is also conserved
  when the body is heated, Δm_inf c² must be supplied by the heater. For copper …". After the ratio,
  add: "The conflict does not depend on the particular inputs: with 1.288 bits over {p, n, e}, or 1 bit
  over electrons and quarks, the ratio is 28 or 52. A proponent must therefore give up energy
  conservation, which the annihilation prediction uses, or E = mc², which the M/E/I rationale uses."
  Optionally add the third-law sentence from §2(c), with Martin 1973 read and ledgered first.

**M4. The summaries in Secs. 9 and 10 contradict Sec. 8.**

- *Location:* `09-methodology.tex:153` (H-info: "Mass–information conjecture untested");
  `10-discussion.tex:24` ("the calorimetric consistency argument … give[s] definite targets");
  `10-discussion.tex:11` (no mention of the calorimetry conflict). Compare with `08:264-265` and
  `08:294` ("In conflict with calorimetry (our calculation)").
- *Fix:*
  - H-info status: "Weighing and annihilation tests not performed; temperature-dependent version
    conflicts with calorimetry if the information energy is conserved (this work); genomic entropy
    trend accounted for by the substitution spectrum; see Sec. 8."
  - Discussion item 4: "The annihilation experiment has not been attempted. The temperature-dependent
    version is already constrained by calorimetry unless energy conservation is abandoned (Sec. 8)."
  - Discussion line 11: add "and the temperature-dependent version conflicts with calorimetry under
    its own energy bookkeeping".

**M5. The section relies on Lairez without disowning his claim that thermal energy is not rest mass,
while using ΔH/c² itself.**

- *Location:* `08:124-133` (Lairez cited in support; "Our assessment agrees with Lairez"), against
  `08:155-157` (ΔH/c² ≈ 4×10⁻¹³ kg).
- *Evidence:* Lairez's abstract: "Potential energy of a body is actually stored under the form of rest
  mass, interaction energy too, temperature is not." In standard relativity the invariant mass of a
  composite body includes its internal thermal kinetic energy (Okun). The report flags this
  (`R:231-236`), but the tex does not.
- *Fix:* After `08:130` add: "(Lairez also states that thermal energy is not stored as rest mass. That
  is not correct for the invariant mass of a composite body, and nothing here depends on it. Below we
  use the standard result that heating raises a body's mass by ΔU/c².)"

### MINOR

**m1. Bérut 2012 is characterized from the abstract only, which breaks CONVENTIONS §2.**

- *Location:* `08:41-42`, table row `08:286`; `L:82-87` (ABSTRACT).
- *Evidence:* A characterization of what a paper concludes requires FULLTEXT. The open follow-up
  Bérut, Petrosyan & Ciliberto, J. Stat. Mech. (2015) P06015 (doi:10.1088/1742-5468/2015/06/P06015;
  text at `/tmp/claude-0/papers/berut2015.txt`) reports three things:
  - with a free two-parameter fit, ⟨Q⟩→0 = A + B/τ gives A = 0.72 k_BT;
  - the averages are conditioned on trajectories that end in the target state, with success rates of
    95–99%;
  - individual trajectories can dissipate less than the bound.
- *Fix:* "Bérut et al. found that the mean heat, conditioned on successful erasure (success rate
  95–99%), approaches k_BT ln2 as 1/τ; a free fit gives an asymptote of 0.72 k_BT." Cite both
  papers.

**m2. The Jun et al. quote is background, not a measurement.**

- *Location:* `08:45-46`.
- *Evidence:* "This work is dissipated into a surrounding heat bath" is in their introductory statement
  of Landauer's principle (arXiv 1408.5089, p. 1). The experiment measures work from the trajectory.
- *Fix:* "…compared with ln2 ≈ 0.693 and 0.05 kT in a control protocol that does not erase (the
  measured quantity is the work; in Landauer's statement, which they adopt, it is dissipated into the
  bath)."

**m3. Hong et al. 2016 is presented without its caveats.**

- *Location:* `08:47-49`; table `08:286` ("Confirmed within errors").
- *Evidence (PMC4795654):*
  - The five-trial room-temperature mean is (6.09 ± 1.43) zJ = (1.45 ± 0.35) k_BT, which is 2.2σ above
    k_BT ln2.
  - The authors say their results "depart by only 50 to 100% of the Landauer value".
  - The initial state was not randomized; they argue the protocol makes randomization unnecessary.
  - The measurement is an ensemble MOKE hysteresis-loop area over ~10⁴ nanomagnets.
- *Fix:* Add "(the authors attribute an excess of 50–100% over k_BT ln2 to misalignment; the initial
  state was not randomized)". In the table, write "Consistent with the bound as a lower limit; approach
  to within ~5% (colloids) and 50–100% (nanomagnets)".

**m4. Ostrowski et al. are misattributed and their statistics are reported uncritically.**

- *Location:* `08:200-206`.
- *Evidence:*
  - The authors write "Those results simply confirmed the Vopson's hypothesis" and "The presented
    analysis fully confirmed the results of Vopson". So "rather than a new law" (`08:205`)
    misrepresents them.
  - The 1.4σ statement is correct: HIV 0.433/0.338 = 1.28σ, influenza 1.725/1.245 = 1.39σ, SARS-CoV-2
    2.7σ.
  - Taking the degrees of freedom as roughly the number of records, χ²/dof ≈ 9 (SARS-CoV-2),
    ≈ 1.5×10³ (HIV) and ≈ 4×10⁴ (influenza). The CLS uncertainties are therefore not credible for HIV
    and influenza. Inflating by √(χ²/dof) makes both CLS slopes consistent with zero.
  - They do not define the per-record uncertainty σ₀ᵢ, nor how the "mutation number" M was obtained.
    NCBI influenza records are single segments.
  - The journal (Acta Phys. Pol. A) is peer-reviewed.
- *Fix:* "…The authors describe this as confirming Vopson's hypothesis and interpret it through
  Prigogine–Onsager nonequilibrium thermodynamics. Their least-squares fits have χ² per record of
  ~10–10⁴, and their robust slopes for HIV and influenza are within 1.4σ of zero. They do not define
  the mutation count and do not test a mutation-bias null model."

**m5. Todd's reinterpretation does not cover the genomic case; its sign is opposite.**

- *Location:* `08:211-212`, `08:249-250`, table `08:300`.
- *Evidence:* Todd defines I_struct = D(p‖p_iso) and shows it *decreases* as systems relax (his §on
  H(p) increasing, `ipil_308`). For a four-letter composition, D(p‖u) = 2 − H. The observed decrease
  of H in SARS-CoV-2 is therefore an *increase* of Todd's structure-information, i.e. a departure from
  isotropy. Todd's mapping applies to the digital example only.
- *Fix:* In the Reformulations item add: "This reading fits the digital example. In the genomic example
  H decreases, so D(p‖u) = 2 − H increases, which is the opposite of relaxation toward isotropy." Also
  state the venue: "(IPI Letters, whose editor-in-chief is Vopson)", paralleling `08:219-221`.

**m6. Describe the process as a "substitution spectrum" and cite a spectrum that covers 2021.**

- *Location:* `08:227-243`.
- *Evidence:*
  - Position-wise differences from Wuhan-Hu-1 are observed substitutions, i.e. mutation filtered by
    selection. They include lineage-defining, positively selected changes such as A23403G (D614G),
    T22917G (L452R) and C23604G (P681R).
  - MN908947.3 is not the root (the lineage A/B question), so the direction of some changes is
    unpolarized.
  - Simmonds (2020) analyzed early-2020 data, whereas OL351371.1 is a 2021 Delta genome.
- *Fix:* Use "substitution spectrum (mutation filtered by selection)". Add: "C→U has remained the
  dominant SARS-CoV-2 mutation class through 2021–22 [Bloom, Beichman, Neher & Harris, MBE 40, msad085
  (2023)]". Read that paper first and add it to the ledger.

**m7. Vopson & Lepadatu's equal-length criterion selects reference-backfilled records (new
observation).**

- *Location:* `08:180-181`, `08:226-227`; `L:466`.
- *Evidence (my check):*
  - OK104651.1 and OL351371.1 carry Delta markers (C22995A T478K, T22917G L452R, C23604G P681R).
  - Yet at the lineage-defining deletion sites S:E156–F157 (nt 22029–22034, AGTTCA) and ORF8
    D119–F120 (nt 28248–28253, GATTTC) they carry the reference bases.
  - Their first and last 60 nt, including the 33-nt poly(A), are identical to the reference, in
    regions that amplicon protocols do not cover.
  - They contain no ambiguous bases.

  These records appear to be reference-filled consensus sequences. Requiring "the same number of
  nucleotides as the reference" selects such records and excludes correct Delta assemblies (~29,891
  nt). The effect is to *understate* divergence. It does not change the sign.
- *Fix:* Add one sentence after the "no ambiguity codes" remark: "The two Delta-lineage genomes carry
  reference bases at the lineage's deletion sites and reference-identical termini, so the equal-length
  criterion appears to select reference-backfilled assemblies. This understates divergence but does
  not affect the sign." Also qualify the ledger claim "contain no ambiguous bases" (`L:466`).

**m8. The estimator paragraph misses its strongest point.**

- *Location:* `08:239-241`.
- *Fix:* After "constant offset" add: "Under an i.i.d. sampling model the plug-in standard error would
  be 2×10⁻³ bits, larger than the whole 22-month decline (7.6×10⁻⁴ bits). The decline is resolved only
  because the genomes are nearly identical, so each ΔH is fixed by a few substitutions and estimation
  theory is not the relevant frame."

**m9. The "pure hydrogen gives 1 bit" statement depends on the particle counting; strengthen it with
copper.**

- *Location:* `08:158-161`.
- *Evidence:*
  - Hydrogen gives 1 bit over {p, e} and 1.5 bits over {u, d, e}.
  - Applying Vopson's own procedure to copper gives 1.43 bits over {u, d, e} and 1.58 bits over
    {p, e, n}. Yet the protocol applies the cosmic 1.509 bits to copper.
- *Fix:* "A pure-hydrogen population gives 1 bit per particle over {p, e} (1.5 bits over {u, d, e}).
  Applied to copper's own composition, the same procedure gives 1.43 or 1.58 bits rather than the
  cosmic 1.509 that the protocol uses for copper."

**m10. Fairness: include Vopson's own hedges.**

- *Location:* `08:4-8`, `08:193-196`.
- *Evidence:*
  - The gravity paper concludes: "Whether the universe is indeed a computational construct remains an
    open question" (`L:363`).
  - Sec. 9 reports his statement that the law "is valid regardless of whether the universe is a
    simulation or not" (`09-methodology.tex:284,299-301`).

  The tex quotes only the strong framing.
- *Fix:* Append to `08:196`: "; the paper's conclusion adds that whether the universe is computational
  'remains an open question'". Cross-reference the Sec. 9 statement at `08:8`.

**m11. The "degenerate explanation" in row H-info cites the wrong work.**

- *Location:* `09-methodology.tex:153`, which cites Lloyd 2002 (computational capacity of the
  universe).
- *Evidence:* The standard-physics explanations of the H-info signatures are the Landauer bound with
  heat to the environment, relaxation under the second law, and biased substitution spectra.
- *Fix:* "Landauer/stochastic thermodynamics \cite{Landauer1961irreversibility,Esposito2011second};
  biased viral substitution spectra \cite{Simmonds2020rampant}".

**m12. Kish & Granqvist: state the genre and quote the sentence that bears on the point.**

- *Location:* `08:136-138`.
- *Evidence:* Proc. IEEE "Point of View" column (bib title). The sentence on entropy versus energy
  and mass quoted in §2(b) is the one that bears directly on the claim.
- *Fix:* Quote that sentence alongside the "remain the same" quote.

**m13. Errors and stale paths in the ledger and report.**

- *Location:* `L:479` and `R:124,129,243-246` (the one-SNP discrepancies do not exist; see §2(a));
  `L:468`, `R:116-117` (the scripts are now in `research/notes/08-scripts/`, not only in `/tmp`).
- *Fix:*
  - Correct the counts to 9 and 40 and delete the "differ by one" notes.
  - Update the locators to `research/notes/08-scripts/`.
  - Add a regression check that `analyze.py` reproduces both H and the SNP counts.

**m14. The Hossenfelder quotation comes only from the criticized party's transcript.**

- *Location:* `08:215-218`.
- *Evidence:* `L:373` confirms the text was not checked against the video.
- *Fix:* Check the quoted sentences against the video (captions) before submission. Otherwise write
  "according to the transcript reproduced in Ref. [Vopson2025response]", which the text nearly does
  already.

### NIT

- **N1.** `08:69,118-119`: Vopson writes "1 Tb", but 2.5×10⁻²⁵ kg corresponds to 8×10¹² bits (one
  terabyte); 10¹² bits would give 3.2×10⁻²⁶ kg. Write "for 1 Tb (numerically 8×10¹² bits, i.e. one
  terabyte)".
- **N2.** `08:152-156`: use one ratio (≈78 for heat capacity, ≈77 for the 100 K example) instead of
  "78" and "about 80".
- **N3.** `08:155-156`: the rest-energy change is ΔU; say "ΔU ≈ ΔH (pΔV is negligible)".
- **N4.** `08:152-153`: "measured C_p … which we obtain from the NIST-JANAF parameters" should read
  "tabulated C_p (NIST-JANAF Shomate fit)".
- **N5.** Bib `Crecraft2024second`: volume 27 is the 2025 issue (online 30 Dec 2024). Check that the
  year field matches the house style.
- **N6.** An optional internal point on the protocol that the authors may note: Eq. (5) defines
  m_e = m_e,phys + I k_BT ln2/c², but Eq. (9) adds I k_BT ln2 on top of m_e c². Either Eq. (9) uses
  m_e,phys, or the information energy is counted twice.
- **N7.** `08:239-240`: the constancy of the Miller–Madow offset is our inference from Paninski's
  formula, not a statement in Paninski. Write "(Paninski gives the correction as (m̂−1)/2N nats, which
  is constant here)".

---

## 4. Missing literature (existence verified via Crossref metadata; the authors must read each before citing)

**Landauer experiments and information-to-work conversion** (for §8.1 and for M2):

- Bérut, Petrosyan & Ciliberto, J. Stat. Mech. (2015) P06015, doi:10.1088/1742-5468/2015/06/P06015.
  Open on HAL (ensl-01134137); text already downloaded. **Read.**
- Gavrilov & Bechhoefer, "Erasure without work in an asymmetric double-well potential", PRL 117,
  200601 (2016), doi:10.1103/PhysRevLett.117.200601. This is directly relevant to the asymmetric-memory
  sentence at `08:145-146`: the average work to erase can fall below kT ln2.
- Gavrilov & Bechhoefer, "Arbitrarily slow, non-quasistatic, isothermal transformations", EPL 114,
  50002 (2016), doi:10.1209/0295-5075/114/50002, arXiv:1603.07814. Relevant to logical versus
  thermodynamic reversibility, and so to Lairez's argument.
- Toyabe, Sagawa, Ueda, Muneyuki & Sano, Nat. Phys. 6, 988 (2010), doi:10.1038/nphys1821. Information
  converted to free energy.
- Koski, Maisi, Pekola & Averin, PNAS 111, 13786 (2014), doi:10.1073/pnas.1406966111. A Szilard engine
  with a single electron, extracting ≈kT ln2 per bit from the bath.
- Yan et al., PRL 120, 210601 (2018), doi:10.1103/PhysRevLett.120.210601. Single-ion quantum Landauer
  test.
- Gaudenzi et al., Nat. Phys. 14, 565 (2018), doi:10.1038/s41567-018-0070-7. Quantum Landauer erasure
  with a molecular nanomagnet.
- Dago et al., PRL 126, 170601 (2021), doi:10.1103/PhysRevLett.126.170601. Fast, precise approach to
  the bound in an underdamped oscillator.
- Scandi et al., PRL 129, 270601 (2022), doi:10.1103/PhysRevLett.129.270601. Minimally dissipative
  erasure in a quantum dot.

**Theory and reviews:**

- Sagawa, "Thermodynamic and logical reversibilities revisited", J. Stat. Mech. (2014) P03025,
  doi:10.1088/1742-5468/2014/03/P03025, arXiv:1311.1886. This is the standard reference for the
  logical/thermodynamic distinction that Lairez invokes, and it balances Norton.
- Lutz & Ciliberto, "Information: From Maxwell's demon to Landauer's eraser", Phys. Today 68(9), 30
  (2015), doi:10.1063/PT.3.2912.

**Genomics:**

- Bloom, Beichman, Neher & Harris, "Evolution of the SARS-CoV-2 mutational spectrum", Mol. Biol.
  Evol. 40, msad085 (2023), doi:10.1093/molbev/msad085. Needed for m6, and for an independent-spectrum
  prediction of the slope for comparison with Ostrowski et al.'s −0.97×10⁻⁵ per mutation.

**Calorimetry (optional third-law argument):**

- Martin, "Specific heat of copper, silver, and gold below 30 K", Phys. Rev. B 8, 5357 (1973),
  doi:10.1103/PhysRevB.8.5357.

**Optional (electron-mass idea in `R:70-77`):**

- Sturm et al., Nature 506, 467 (2014), doi:10.1038/nature13026. M/E/I implies a fractional electron
  mass shift of 5.3×10⁻⁸ at 300 K (I = 1.509) and 7×10⁻¹⁰ at 4 K. Turning this into a bound needs a
  well-defined "temperature" of a single trapped electron, so I would not add it without care.

I found no further peer-reviewed critique of the second law of infodynamics beyond those cited
(web search, 2026-09-27). The bioRxiv preprint doi:10.1101/2022.06.13.495895 is by Vopson himself.

---

## 5. Spot checks performed

1. **NCBI fetch and entropies.** I fetched the sequences with `fetch_seqs.sh` (no email; output
   identical to the stored FASTA). An independent script (`scratchpad/seq/ref.py`) reproduced all ten
   H values to within 4×10⁻⁸ bits, and the SNP counts 0/4/7/9/19/25/26/32/40/49 match Table I exactly.
2. **Per-substitution ΔH.** I checked the exact values against the first-order formula for all twelve
   substitution types. I derived the Jeffreys form of the null, E[ΔH] = +3.87×10⁻⁶ bits, and computed
   the transitions-only null (+5.8×10⁻⁶ bits), the toward-commoner null probability (0.414, binomial
   tail 1.5×10⁻⁹), the pooled spectrum (148 distinct differences), the Miller–Madow offset
   (7.237×10⁻⁵ bits) and the i.i.d. standard error (2.0×10⁻³ bits).
3. **Delta genomes.** I checked the lineage markers, the deletion sites (22029–22034 and 28248–28253)
   and the termini of OK104651.1, OL351371.1 and OK546282.1 (m7).
4. **Vopson 2022 protocol (full text).** I checked Eqs. (1), (2), (4), (5), (9), (10) and (11); the
   particle count 219.5; I = 1.509; the printed N_b of 29.8×10²⁶ against the computed 3.14×10²⁷;
   Δm_inf = 3.34×10⁻¹¹ kg; λ = 45.85 µm (0.0270 eV) at 300 K; the electron mass ratio of 2.2×10⁷; and
   m_bit = 3.194×10⁻³⁸ kg.
5. **Copper thermochemistry.** From the NIST-JANAF Shomate parameters: C_p(298.15 K) = 24.47 J mol⁻¹ K⁻¹
   and ΔH(300→400 K) = 2489 J mol⁻¹. I computed C_inf and the variant ratios (§2(c)) and the thermal
   mass, 4.36×10⁻¹³ kg.
6. **Vopson 2021 entropies.** I recomputed H(0.483, 0.29, 0.225) = 1.5093 and
   H(0.466, 0.466, 0.067) = 1.2878.
7. **Vopson & Lepadatu 2022 (full text), digital example.** Eq. (4); N counts the "information states";
   the thermalized initial state is treated as N = 0, although Eq. (4) applied to a random pattern
   would give H ≈ 1. This supports the section's reading and could be added as one sentence: the
   decrease is set by the definition of N.
8. **Esposito & Van den Broeck.** I checked Eq. (12), W_irr = TΔ_iS + TΔI. With W = ΔF_eq = 0 it gives
   ΔI = −Δ_iS ≤ 0, as the section states.
9. **Kish & Granqvist, §II, and Lairez, §I.B.** I checked the quotations and the context; see §2(b)
   and M5.
10. **Jun et al.** I checked Table I (0.71 ± 0.03, 0.05) and the source of the "dissipated into a heat
    bath" phrase (m2).
11. **Hong et al.** I checked the two dissipation values, the 2σ statement, the 50–100% excess and the
    non-randomized initial state (m3).
12. **Bérut 2015.** I checked the free fit A = 0.72 k_BT, the conditioning on success, and the
    writing-equals-reset footnote.
13. **Ostrowski et al. (full text).** I checked Table I, the σ ratios, the χ² values, the "confirmed
    Vopson" wording and the peer-reviewed venue (m4).
14. **Todd 2026.** I checked the definition of I_struct, the direction of change, and the statement that
    it is "not a new fundamental principle" (m5).
15. **Classification of critiques.**
    - Peer-reviewed: Burgin & Mikkilineni (MDPI *Information*), Lairez (*Entropy*), Crecraft
      (*Entropy*), Bormashenko (*Entropy*), Ostrowski (*Acta Phys. Pol. A*), Kubiński (*Entropy*).
    - Editor-screened, not peer-reviewed: the IPI Letters "News and Views" items.
    - A regular IPI Letters article, with review process unverified and edited by the author under
      discussion: Todd.
    - Informal: Hossenfelder (video).
    - An editorial "Point of View" column: Kish & Granqvist.

    The tex is correct except that Todd's venue is not flagged (m5) and the genre of Kish & Granqvist
    is not stated (m12).
16. **Missing-literature DOIs.** All DOIs in §4 were resolved through the Crossref API: titles,
    journals, years and first authors match. For the EPL paper, arXiv:1603.07814 was checked through
    its arXiv abstract page. This is METADATA-level verification only.
