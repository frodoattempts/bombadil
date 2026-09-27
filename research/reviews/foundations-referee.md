# Referee report: Section 7, "Rendering on demand, observers, and quantum foundations"

Referee expertise: quantum foundations and quantum-optics experiments (delayed choice, quantum erasers, complementarity and duality relations, decoherence, Bell tests, superdeterminism, collapse models).

Material reviewed:
- `paper/sections/07-rendering-qm.tex`
- `research/ledgers/07-rendering-qm.md`
- `research/notes/07-rendering-qm-report.md`
- the H-lazy row of `09-methodology.tex`
- the summaries of this section in `00-abstract.tex`, `00-introduction.tex` and `10-discussion.tex`

Primary sources I read myself:
- Campbell et al.: arXiv v2 and the published IJQF PDF.
- Kim et al.: quant-ph/9903047.
- Also Jacques 2007, Ma 2012, Ma 2013, the Ma–Kofler–Zeilinger RMP, Hackermüller 2004, Hornberger 2003, Luo 2024, Kastner 2019, Hossenfelder & Palmer 2020, 't Hooft (CAI §5.8), Irwin 2020, Tremblay 2019, Yampolskiy 2023, the Bell-test abstracts, Walborn et al. 2002, and Schlosshauer et al. 2013.

---

## 1. Summary judgement and recommendation

The section is careful, well sourced and mostly accurate. Its central original point holds up under an independent calculation: what Campbell et al. count as "success" is excluded by standard quantum mechanics, and their Eq. (2) differs from the QM value of 1/2 by exactly the amounts stated.

The section nevertheless has three problems that an expert referee would pick on.

1. **Framing.** The section says the schemes "predict deviations from QM" and that the paper "does not compare its success criteria with QM". Neither statement is quite fair to Campbell et al.
   - They state success conditions, not predictions.
   - For schemes 1–2 they explicitly set up the detection-determined account as the null.
   - For scheme 3 they acknowledge that R "is supposed to be random (or … independent from X)".
   - The mismatch in schemes 3–4 is most plausibly a misreading of Kim et al.: their Remark 1 lists both D1 and D2 as "Interference pattern" and drops the π phase shift. It is not intended new physics.
2. **The strongest argument is missing.** Eq. (2)'s premise is refuted by the published data of the very experiment it modifies (Kim et al., Figs. 3–4). Taken together, Campbell et al.'s conditionals imply a D0 marginal whose visibility depends on a later beam-splitter setting. That is a violation of no-signalling, and it cannot be produced by any unitary optics acting on the idler. These arguments do not depend on interpretation, and they are much harder to dismiss than "this contradicts QM", to which a proponent will answer "of course, that is the point".
3. **Collateral inaccuracies.**
   - Ma 2013 numbers are attributed to the wrong configuration.
   - Table 09 wrongly lists GRW/CSL as a degenerate explanation of H-lazy.
   - The nonlocal-versus-superdeterministic dichotomy is logically incomplete.
   - Directly relevant "unread which-path marker" experiments, collapse-model bounds and Wigner's-friend / Local Friendliness work are missing.

**Recommendation: major revision.** None of the problems is fatal. Every fix is a rewording or an addition, and the core result survives, in a stronger form.

---

## 2. VERDICT on the Campbell-deviation claim: **CORRECT WITH CAVEATS**

### 2.1 What the section claims (07-rendering-qm.tex:71–106)

- (a) Scheme 1: removing the coincidence counter, or unplugging the which-path recorder, cannot produce fringes in QM.
- (b) Scheme 3: in QM, P(R=1|X) = 1/2, whereas Eq. (2) gives [1+2cos²(πx/a)]⁻¹. That is a deviation of 1/2 at dark fringes (Eq. 2 gives 1) and 1/6 at bright fringes (Eq. 2 gives 1/3).
- (c) Scheme 4: the "interference at D0" that configurations (a)–(c) assume is not a QM prediction, and the QM outcome is labelled a "discontinuity".

### 2.2 Independent calculation (Kim et al. geometry)

Script: scratchpad `kim_qm.py`, not in the repo. Its results are reproduced below.

**Set-up** (Kim et al., quant-ph/9903047):
- A double slit in the pump creates pairs in region A or region B (width 0.3 mm, centre separation 0.7 mm, λ = 702.2 nm).
- The signal photon goes to D0 in the Fourier plane of lens L_S.
- The idler from A meets BS_A and the idler from B meets BS_B. Kim et al. state that both are "50-50".
  - One output goes to a which-path detector (D3 or D4).
  - The other goes via mirrors to a 50-50 BS whose outputs are D1 and D2.
- Kim et al.'s Fig. 1 text routes *transmission* at BS_A/BS_B to D3/D4. Campbell et al. say *reflection* gives R=1. The labels are immaterial; define R=1 as {D3, D4} and R=0 as {D1, D2}, as in Campbell's Fig. 7.

**State and amplitudes.**
- Signal amplitudes at D0: ψ_A(x), ψ_B(x) ∝ sinc(πax/λf)·e^{±iπdx/λf}.
- Joint state: |Ψ⟩ ∝ ∫dx [ψ_A(x)|x⟩|a⟩ + ψ_B(x)|x⟩|b⟩], with ⟨a|b⟩ = 0.

**Idler network parameters:**
- r_A, r_B: reflectances of BS_A and BS_B towards the which-path detectors;
- t: transmittance of the erasing BS;
- η1…η4: efficiencies of D1…D4;
- φ: interferometer phase.

Joint detection probabilities:

- P(x, D1) = η1 (1−r)·|√t ψ_A + √(1−t) e^{iφ} ψ_B|²  (for r_A = r_B = r)
- P(x, D2) = η2 (1−r)·|√(1−t) ψ_A − √t e^{iφ} ψ_B|²
- P(x, D3) = η3 r_A |ψ_A|², and P(x, D4) = η4 r_B |ψ_B|²

**General statement (POVM form).**
- The event R=1 corresponds, on the idler path space, to the POVM element E₁ = η_w (r_A|a⟩⟨a| + r_B|b⟩⟨b|).
- For r_A = r_B = r and equal which-path efficiencies η_w, this is E₁ = η_w r·𝟙. It has no off-diagonal elements.
- Therefore P(R=1|x) cannot contain an interference term. The pooled erasure event R=0 is the sum of the two output ports of a unitary BS. Unitarity fixes that sum to |ψ_A|² + |ψ_B|², which is fringe-free for any t.
- With finite detector efficiencies:

  P(R=1|x) = η_w r / [ η_w r + (1−r)( η̄ + Δη·√(t(1−t))·cos(2πx/a + φ) ) ],

  where η̄ = (η1+η2)/2 and Δη = η1 − η2.

**Numerical results** over the central fringe period, with the sinc² envelope divided out where noted:

| Case | P(R=1\|x) range | Visibility of pooled R01+R02 |
|---|---|---|
| Ideal Kim: all 50:50, η = 1 | 0.5000 – 0.5000 | 0.0000 |
| Erasing BS at 70:30 (t = 0.7) | 0.5000 – 0.5000 | 0.0000 |
| r_A = 0.5, r_B = 0.4 | 0.4500 – 0.4500 (in the central period) | 0.0000 |
| Interferometer phase φ = π/3 | 0.5000 – 0.5000 | 0.0000 |
| η1 = 0.9, η2 = 0.6 | 0.526 – 0.625 | 0.200 = (η1−η2)/(η1+η2) |
| η1 = 0.9, η2 = 0.6, t = 0.7 | 0.530 – 0.620 | 0.183 |
| D2 removed (only D1 counted) | 0.500 – 1.000, i.e. 1/(1+cos²) | 1.000 |

**Campbell et al. Eq. (2):**
- It gives 1/3 at bright fringes and 1 at dark fringes.
- max |Eq.(2) − 1/2| = 0.5, and |1/3 − 1/2| = 1/6. **The section's arithmetic is correct.**
- The plain average of Eq. (2) over a period is 1/√3. Weighted by the marginal Campbell et al. themselves imply, it averages to exactly 1/2, so Eq. (2) is internally consistent with P[R=0] = 1/2.

**Marginal implied by Campbell et al.'s conditionals.** They take P(x|R=1) ≈ 2I₀ and P(x|R=0) ≈ 4I₀cos². With BS_A/BS_B reflectance r, the unconditioned D0 distribution is then P(x) ∝ r + (1−r)(1+cos 2πx/a), whose visibility is V = 1 − r:

| r | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|
| Implied V (D0 marginal) | 1.00 | 0.75 | 0.50 | 0.25 | 0.00 |
| QM | 0 | 0 | 0 | 0 | 0 |

### 2.3 Conclusions from the calculation

1. **Claim (b) is correct** for the Kim geometry with its 50:50 BS_A/BS_B. The ratio of the *erasing* BS is irrelevant (unitarity). The interferometer phase is irrelevant. Unequal r_A, r_B shift P(R=1|X) to a constant that is still fringe-free.
   - Only **unequal D1/D2 efficiencies** make X and R correlated in QM. The correlation then has fringe visibility (η1−η2)/(η1+η2)·2√(t(1−t)).
   - This matters for any real attempt at scheme 3: a 20% efficiency imbalance mimics a weak "Campbell signal". The section should say that "P(R=1|X) = 1/2" assumes equal reflectances and balanced erasure detection.
2. **Eq. (2) matches no QM configuration.**
   - It is exactly what one obtains if *both* erasure detectors showed the same in-phase fringe, which is how Campbell et al.'s Remark 1 describes them (IJQF pp. 85–86: "D1: Interference pattern … D2: Interference pattern").
   - Kim et al. report the opposite: "there is a π phase shift between the two interference fringes" (Figs. 3–4).
   - So **the premise of Eq. (2) is contradicted by the published data of the experiment it modifies**, independently of any QM calculation. Even discarding D2 gives 1/(1+cos²), not Eq. (2).
3. **Taken together, Campbell et al.'s conditionals violate no-signalling.** The unconditioned D0 pattern would have visibility 1 − r, set by a beam-splitter configuration that can be chosen up to ∆t later (∆t ≈ 60 s in their scheme 4(b)–(c)). QM forbids this (Ghirardi–Rimini–Weber 1980), and so does Campbell et al.'s own total-variation argument (Eq. 4), which is a special case of no-signalling applied to an X-dependent switch. This is the cleanest statement of what goes wrong.
4. **Claim (a) is correct.**
   - The D0 marginal is the partial trace over the idler, which is fringe-free because ⟨a|b⟩ = 0, whatever is done to the idler or its records.
   - For scheme 1 with a physical which-path detector, V ≤ |⟨m_A|m_B⟩| for pure marker states (Englert 1996). The marker states are fixed by the detector's physical coupling, not by whether a cable to a recorder is connected.
   - Walborn et al. (2002) say this explicitly: "The which-path marker's presence alone is sufficient … Therefore, it is enough that the which-path information is available to destroy interference." They show it experimentally in their Fig. 3.
   - Caveat: for *photons*, "turned-on detectors at the slits" (Campbell p. 86) absorb the photon, so scheme 1 is only well posed with non-demolition markers. That is the regime of Buks et al. (1998) and of the polarisation-marker experiments.
5. **Claim (c) is correct.**
   - In every configuration, (a)–(d), QM predicts the fringe-free marginal, i.e. Campbell's "particle pattern".
   - Campbell et al. themselves write: "This experiment is likely to be successful in the sense that the only possible outcomes are: the exposure of discontinuities in the rendering of reality, or paradoxes" (IJQF p. 93).
   - The section's conclusion that the protocol has "no outcome that counts against the hypothesis" should quote this sentence rather than infer it.

### 2.4 Caveats (why not simply "CORRECT")

- **Intent.** Campbell et al. never say that their success criteria deviate from QM, and they do not present them as new physics. The evidence points to a misreading of the eraser data (Remark 1; the "standard approximations" of p. 89; "whether the which-way data is or is not erased determines the screen result", Sec. 4.1).
  - For schemes 1–2 they *do* frame the test against the view that the pattern is "entirely determined by the experimental/detection set-up" (p. 81) and against Copenhagen, where "any detection causes a quantum collapse" (p. 79). A positive result there is intended to overturn the detection-determined account, which amounts to standard QM plus decoherence.
- **Wording.** "Contradict standard QM" is logically true of the criteria. Read as a statement about the paper, though, it suggests the authors *predicted* a violation. The accurate phrasing is: "the outcomes that the schemes count as success are excluded by standard QM (and, for scheme 3, by the published Kim et al. data and by no-signalling)". Avoid "predict": Campbell et al. say they "cannot predict the outcome".
- **Numbers.** "Up to 1/2 in probability" applies only to scheme 3 under ideal balance. For schemes 1, 2 and 4 the discrepancy is in visibility (V ≈ 1, or unspecified, against V = 0).
- **Originality.** Once the π phase shift is noticed, the calculation is elementary. It should be presented as "we point out", not as one of four headline original analyses. I found no published critique of Campbell et al. making this point (web search; INSPIRE lists only 2 citing records). The authors should state their search, as they do elsewhere.

---

## 3. Numbered issues

### Issue 1: MAJOR. Mischaracterisation of Campbell et al.'s stance ("predict deviations"; "does not compare with QM")

- **Location:** 07-rendering-qm.tex:71–73. Also 07:57–60, where Eq. (2) is presented as what "X predicts".
- **Evidence.** The paper says "if the proposed experiment is successful", and "we cannot predict the outcome" (p. 83).
  - It frames alternative (I), that the outcome is "entirely determined by the experimental/detection set-up" (p. 81), against (II), a role for the observer.
  - It notes that R "is supposed to be random (or, for a general value of X, independent from X)" (p. 90).
  - Remark 1 (pp. 85–86) omits the π shift.
- **Fix.** Replace lines 71–73 with:
  > "**Are the success criteria compatible with QM?** They are not. Campbell et al. frame their null hypothesis as outcomes 'entirely determined by the experimental/detection set-up'~\cite[p.~81]{Campbell2017on}, but they do not derive the QM predictions for their schemes. For schemes~1–2 a success would contradict that null, which is standard QM with decoherence. For schemes~3–4 the success criteria appear to rest on reading both erasure detectors of Kim et al.\ as showing the same fringe: their Remark~1 lists D1 and D2 each as an 'interference pattern'~\cite[pp.~85--86]{Campbell2017on}. Kim et al.\ report a $\pi$ phase shift between them~\cite{Kim2000delayed}. The comparison below is ours."
- **Also** change 07:57–58 to "success would mean that the signal position $X$ predicts the later … outcome $R$, with …".

### Issue 2: MAJOR. The headline summaries overstate the result

- **Location:** 00-abstract.tex:1 ("we show that the success criteria … contradict standard quantum mechanics"); 00-introduction.tex:19 ("contradict standard quantum mechanics by up to $1/2$ in probability").
- **Evidence.** See §2.4. The 1/2 figure is specific to scheme 3 in the ideal limit. The analysis is elementary. "Contradict" invites the proponent's reply that deviating from QM is the whole point.
- **Fix.**
  - Abstract: "Third, we point out that the outcomes counted as success by the proposed render-on-demand experiments are excluded by standard quantum mechanics; in one case the proposal's premise is also contradicted by the published data of the experiment it modifies."
  - Introduction: "An analysis showing that the outcomes counted as success by the proposed render-on-demand experiments~\cite{Campbell2017on} are excluded by standard quantum mechanics and, for the delayed-erasure scheme, by no-signalling and by the published data of Kim et al.\ (Sec.~\ref{sec:rendering-qm-campbell})."
  - 10-discussion.tex:11 already uses good wording ("count as 'success' an outcome that standard quantum mechanics excludes"). Keep it.

### Issue 3: MAJOR. The argument omits its strongest, interpretation-independent form

- **Location:** 07-rendering-qm.tex:85–95.
- **Evidence.** §2.2–2.3 above.
  - (i) Kim et al.'s Figs. 3–4 show complementary R01 and R02 fringes, so the premise P(x|R=0) ∝ cos² is refuted by existing data.
  - (ii) Campbell's conditionals imply an unconditioned D0 visibility of 1 − r, controlled by a later BS setting, which is signalling.
  - (iii) The erasure subensemble is the sum of the two ports of a unitary BS and so cannot be fringed, for any splitting ratio.
- **Fix.** After "…$P(R{=}1|X)=1/2$." insert:
  > "Eq.~(2) follows from assuming that the pooled erasure events show the fringe of a single detector. This premise is contradicted by Kim et al.'s own data, in which the D1 and D2 fringes are shifted by $\pi$ and sum to a fringe-free distribution~\cite{Kim2000delayed}. It also conflicts with no-signalling. Combined with $P(x|R{=}1)\propto$ const, it implies that the \emph{unconditioned} D0 pattern has visibility $1-r$, where $r$ is the which-path reflectance of BS$_A$/BS$_B$, a setting that can be changed after the signal photon is registered. Quantum mechanics forbids such signalling~\cite{Ghirardi1980general}. So does Campbell et al.'s own total-variation argument (their Eq.~(4)), which is a special case of it."
- Put the detailed derivation in an appendix or the ledger, including the POVM statement E₁ ∝ 𝟙.

### Issue 4: MAJOR. Internal inconsistency on "numerical prediction"

- **Location:** 07-rendering-qm.tex:67 ("No scheme carries a numerical prediction") against 07:57–60 and 07:92–95 and the introduction's "by up to 1/2".
- **Evidence.** Eq. (2) is a quantitative functional form, and the paper's own headline number comes from it.
- **Fix.** "Apart from the functional form of Eq.~(2), which describes the $X$–$R$ correlation expected if scheme~3 succeeds, no scheme states an expected visibility or effect size. The only tolerance given is …"

### Issue 5: MAJOR. Ma et al. 2013 numbers attributed to the wrong configuration; the "few-per-cent" bound is overstated

- **Location:** 07-rendering-qm.tex:154–156 (table) and 07:181–183.
- **Evidence** (Ma 2013, arXiv 1206.6578):
  - I = 0.955(7), V = 0.951(18) and I = 0.077(22) are **Vienna** (55 m fibre) values (Table I, scenario II).
  - The **Canary Islands** (144 km) runs, including the one in which the choice happens ≈450 µs after the interference events, give I ≈ 0.928–0.932 and V ≈ 0.751–0.776 (Table II). These are "after subtraction of the background".
  - The table row puts "55 m, 144 km, or ≈450 µs" next to the Vienna numbers.
- **Fix.**
  - Split the row. Vienna: "choice space-like separated (55 m fibre): I=0.955(7); V=0.951(18), I=0.077(22)". Canaries: "144 km; choice up to ≈450 µs after detection: I≈0.93, V≈0.75–0.78 (background-subtracted)". Add both to the ledger with locators (Tables I–II).
  - Change 07:181–183 to "…is bounded at the few-per-cent level for delays up to $\sim$100\,ns–$\mu$s (Vienna), and more weakly, at the $\sim$20\% level of the background-subtracted visibility, for the $\approx450\,\mu$s delay".
  - State what is bounded: deviations from the QM prediction computed with the measured imperfections (Ma 2013, Fig. 4), not from V = 1.

### Issue 6: MAJOR. The H-lazy row of Table `tab:subhyp` lists the wrong degenerate model and a poorly posed signature

- **Location:** 09-methodology.tex:151.
- **Evidence.**
  - GRW/CSL collapse is observer-independent and depends on mass and particle number. It does not predict that interference depends on the availability of which-path information to an observer, and it does not predict that unplugging or destroying a record restores fringes. So it is not degenerate with the stated signature.
  - Standard QM with decoherence already predicts dependence on the *physical* availability of which-path information (Walborn 2002; Ma–Kofler–Zeilinger RMP §II.E). As phrased, the signature does not discriminate.
- **Fix.**
  - Signature: "Interference that depends on whether a which-path record is read, or is destroyed after the fact, at fixed physical coupling to the marker \cite{Campbell2017on}".
  - Degenerate explanation: "Consciousness-triggered collapse (von~Neumann--Wigner, as noted by the proposers; Chalmers--McQueen \cite{Chalmers2022consciousness}). Objective-collapse models (GRW/CSL) \cite{Bassi2013models} are degenerate only with a resource-limited variant in which detail is lost for large systems, not with the observer-dependence signature."
  - Status: "Success criteria are outcomes that standard QM excludes (and, for delayed erasure, that no-signalling excludes); none performed; related experiments agree with QM."

### Issue 7: MAJOR. Missing experiments that test "unread / unrecorded which-path information" and missing collapse-model bounds

- **Location:** 07-rendering-qm.tex:137–184 (table and discussion); 10-discussion.tex:23.
- **Evidence.** The section says no experiment varied whether a record was read (07:173–175). Several classic experiments with markers that are never read, or photons that are never detected, are the closest existing tests and are absent:
  - Zou, Wang & Mandel 1991: coherence is lost when idler paths are made distinguishable, without the idler being detected.
  - Eichmann et al. 1993: which-ion information in the ion's internal state.
  - Buks et al. 1998: a switched-on which-path QPC detector whose output is not used to sort events.
  - Bertet et al. 2001: which-path information stored in a cavity field that is never read.
  - Walborn et al. 2002: the explicit "availability" statement quoted in §2.3.
  - Lemos et al. 2014: imaging with undetected photons.
- Collapse models are the ready-made quantitative framework for any "renderer that economises on large systems". Current bounds exist (Bassi 2013 RMP; Vinante 2016; Fein 2019, 25 kDa superpositions; Donadi 2021; Carlesso 2022 review) and are not discussed. Open problem 3 in 10-discussion.tex:23 should point to them.
- **Fix.**
  - Add two or three of these to the table: Zou–Wang–Mandel, Buks, Bertet, after reading them to FULLTEXT standard.
  - Add a short paragraph: "The most natural quantitative formalisation of a renderer that saves resources on large or unobserved systems is a spontaneous-collapse model with a size-dependent rate; such models are already bounded by matter-wave interferometry and non-interferometric tests~\cite{Bassi2013models,Fein2019quantum,Carlesso2022present}."

### Issue 8: MAJOR. The nonlocal-or-superdeterministic dichotomy is incomplete, and superdeterminism is presented without its critics

- **Location:** 07-rendering-qm.tex:225–231 and 241–251.
- **Evidence.**
  - "Must therefore act nonlocally … or correlate its hidden state with the settings" omits options that a foundations referee will name:
    - no single outcomes (Everett). A simulator that evolves the universal state vector needs neither; Campbell et al. reject this option only on cost grounds (p. 79).
    - retrocausal or "locally mediated" models (Wharton & Argaman 2020 RMP). Hossenfelder & Palmer fold "Future Input Dependence" into violation of Statistical Independence (their §3.1), but note that others distinguish the two (§3.2).
    - operational or QBist readings that deny the realism premise. Campbell et al. themselves invoke QBism (p. 79).
  - Hossenfelder & Palmer are reported fairly, but alone. The standard objections are absent:
    - fine-tuning or "conspiracy" (Wood & Spekkens 2015; H&P's own §4.2 responds to it);
    - Chen's analysis of superdeterminism and quantum probabilities (arXiv:2006.08609);
    - the measurement-dependence literature quantifying how little setting correlation suffices (Hall 2010; Barrett & Gisin 2011). This last point bears directly on how "cheap" a setting-correlating simulator would be.
- **Fix.**
  - 07:225–228: "A simulator that assigns single, definite outcomes and matches these results must act nonlocally with respect to simulated spacetime, as Campbell et al.\ posit, or correlate its hidden state with the settings (a violation of Statistical Independence~\cite{Hossenfelder2020rethinking}; see \cite{Hall2010local,Barrett2011how} for how small a correlation suffices). A simulator that evolves the full quantum state without selecting single outcomes needs neither, and retrocausal models~\cite{Wharton2020colloquium} offer a further option."
  - After the H&P sentence add: "Critics argue that such correlations require fine-tuning~\cite{Wood2015lesson}; see \cite{Chen2021bell} for a philosophical assessment."

### Issue 9: MINOR. "Availability means recording on objective media" is stronger than the source

- **Location:** 07-rendering-qm.tex:40–41.
- **Evidence.** Campbell et al. p. 87: availability "is implied by the which-way data being recorded on objective media (but does not imply a simple 'observation…')". This is a sufficient condition, not a definition. They add that knowledge held only in an experimenter's memory does not count.
- **Fix.** "Campbell et al.\ state that availability `is implied by' recording `on objective media', and that knowledge held only in an experimenter's memory does not suffice~\cite[p.~87]{Campbell2017on}."

### Issue 10: MINOR. Scheme 1's second variant partly agrees with QM (fairness)

- **Location:** 07-rendering-qm.tex:48–52.
- **Evidence.** In the second variant (p. 86), D3/D4 are switched off. Success requires fringes in the unsorted D0 data *and* in the D1- and D2-sorted data. The sorted part is the standard QM result; only the unsorted part is excluded.
- **Fix.** Add: "(A second variant switches off D3/D4; its criterion that D1- and D2-sorted data show fringes agrees with QM, but its criterion of fringes in the unsorted D0 data does not.)"

### Issue 11: MINOR. Wrong locator for Kim et al.; unsourced "unsorted D0 data are fringe-free"

- **Location:** 07-rendering-qm.tex:85–89.
- **Evidence.**
  - In the arXiv text read, Eq. (10) is the finite-slit R01 ∝ sinc²·cos² and R02 ∝ sinc²·sin². The which-path statement is in the text after Eqs. (4)–(5) and in Fig. 5.
  - The bib entry uses PRL 84, 1 but the arXiv title ("A delayed choice…"; the PRL title is 'Delayed "Choice" Quantum Eraser'). Equation numbers may differ in the PRL version.
  - Kim et al. do **not** report D0 singles. "The unsorted D0 data are thus fringe-free" is an inference.
- **Fix.**
  - Cite "\cite[Eqs.~(4)--(5), (10), Figs.~3--5]{Kim2000delayed}" and check the numbering against PRL 84, 1.
  - Write "The D0 data summed over all idler outcomes are therefore fringe-free; this is the pattern obtained when the marker is ignored, shown experimentally by Walborn et al.~\cite{Walborn2002double}".
  - Correct the bib title.

### Issue 12: MINOR. "Both fringe-free, so X and R independent" is a non sequitur as written

- **Location:** 07-rendering-qm.tex:90–92; ledger C-07-011.
- **Evidence.** Independence requires P(x|R=0) = P(x|R=1), i.e. identical envelopes, not merely the absence of fringes. It holds when r_A = r_B and erasure detection is balanced. With η1 ≠ η2, QM predicts an X–R correlation with fringe visibility (η1−η2)/(η1+η2)·2√(t(1−t)) (§2.2). This is a systematic that could fake a positive result in any real attempt.
- **Fix.** "…so in QM, for equal which-path reflectances and balanced erasure detectors, $P(x|R{=}0)=P(x|R{=}1)$ and $P(R{=}1|X)=1/2$ (the BS$_A$/BS$_B$ reflectance in Kim et al.). Unequal D1/D2 efficiencies produce a small fringe-modulated $X$–$R$ correlation, which a real test would have to calibrate out." Add the derivation to the ledger as "(our analysis)".

### Issue 13: MINOR. The duality relation is misstated

- **Location:** 07-rendering-qm.tex:79–80.
- **Evidence.**
  - Englert's (1996) relation is D² + V² ≤ 1, where D is the *distinguishability*: the optimum over marker measurements. Ma 2013 uses a measured parameter I ≤ D.
  - For unread records (schemes 1–2) nothing is measured. The relevant bound is V ≤ √(1−D²), with V = |⟨m₁|m₂⟩| for pure marker states.
  - Englert 1996 is only METADATA-verified in the ledger, yet it is used for a characterisation. Conventions §2 require FULLTEXT.
- **Fix.** "…where QM bounds $V$ by the distinguishability $D$ of the marker states, $D^2+V^2\le1$~\cite{Englert1996fringe} (for pure marker states $V=|\langle m_1|m_2\rangle|$); Ma et al.\ verified the bipartite form with a measured which-path parameter $I\le D$~\cite{Ma2013quantum}." Read Englert 1996. Consider citing Greenberger & Yasin 1988 and Jaeger, Shimony & Vaidman 1995 for the predictability version.

### Issue 14: MINOR. The opening paragraph propagates the misconception the section later corrects

- **Location:** 07-rendering-qm.tex:18–19 ("a pattern that depends on a later choice of measurement").
- **Evidence.** In QM no pattern depends on the later choice. Only which *conditional* subensembles can be formed depends on it (Kastner 2019; Ma et al. RMP §VI).
- **Fix.** "…such as the fact that which conditional interference pattern can be extracted depends on a later choice of measurement, are QM predictions, not anomalies."

### Issue 15: MINOR. "No outcome counts against the hypothesis" should quote the source and be scoped to scheme 4

- **Location:** 07-rendering-qm.tex:100–106.
- **Fix.** Replace the last sentence with: "The authors themselves note that the experiment `is likely to be successful in the sense that the only possible outcomes are: the exposure of discontinuities in the rendering of reality, or paradoxes'~\cite[p.~93]{Campbell2017on}. Scheme~4 therefore has no outcome that counts against the hypothesis." Optionally add: "Their Eq.~(4) argument, that the D0 distribution cannot follow a later, $X$-dependent switch, is correct, and QM satisfies it by predicting the fringe-free pattern in every configuration."

### Issue 16: MINOR. Reading the "VR engine reacting to intention" as superdeterminism is a stretch

- **Location:** 07-rendering-qm.tex:229–231.
- **Evidence.** Campbell et al. treat experimenters' decisions as "external to the simulation" and say the engine "would not necessarily be able to predict" them (p. 93). That is Statistical Independence *holding*. Outcome (ii), a particle pattern regardless of the switch, requires no reaction to intention at all.
- **Fix.** "Campbell et al.'s suggestion of a `VR engine reacting to the intention of the experimentalist'~\cite[p.~94]{Campbell2017on} would, if the engine anticipated choices, amount to such a correlation; the authors, however, treat experimenters' decisions as external to the simulation."

### Issue 17: MINOR. Dürr et al. row: wording and a primary source not read

- **Location:** 07-rendering-qm.tex:160–162 and 176–179.
- **Evidence.**
  - The RMP says "disturbance of the path … four orders of magnitude smaller than the fringe period". The table says "momentum kick". That is only the *classical* kick. The Storey et al. (1994) / Englert–Scully–Walther / Wiseman debate and Dürr & Rempe (2000) show that a non-classical momentum transfer accompanies which-way marking.
  - Dürr et al. (Nature 395, 33) is METADATA-only, yet it is quoted.
- **Fix.** Read the original, or cite the quote explicitly as "quoted in~\cite{Ma2016delayed}". Change the cell to "classical momentum kick shifts the pattern by $\sim10^{-4}$ of a fringe period", and cite Dürr & Rempe 2000 (doi:10.1119/1.1285869) for the nuance.

### Issue 18: MINOR. The Yampolskiy characterisation needs a qualifier

- **Location:** 07-rendering-qm.tex:201–203.
- **Evidence.** He states that he does "not evaluate evidence" (abstract). His §3.6 (p. 15) nonetheless asserts that the "simulation hypothesis, arguably, represents the best fitting interpretations of experimental results produced by QM researchers [4, 17]". It also cites the Wigner's-friend experiments of Proietti 2019 and Bong 2020, whose "observers" are photons, as evidence of "interaction of quantum systems with conscious agents [163–165]".
- **Fix.** "…does not set out to evaluate evidence, though it asserts in passing that the hypothesis `arguably, represents the best fitting interpretations of experimental results produced by QM researchers'~\cite[Sec.~3.6]{Yampolskiy2023how}."

### Issue 19: MINOR. The rebuttal of Irwin et al.'s "more widely agreed" claim can be made empirical

- **Location:** 07-rendering-qm.tex:192–196.
- **Evidence.** In a 33-participant poll at a foundations conference, 6% chose "the observer plays a distinguished physical role (e.g., wave-function collapse by consciousness)" (Schlosshauer, Kofler & Zeilinger 2013, Question 10; read, arXiv:1301.1069). Campbell et al. cite this poll themselves (their ref. [39]).
- **Fix.** Add: "In a poll of participants at a foundations conference, 6\% chose a distinguished physical role for the observer, such as consciousness-induced collapse~\cite{Schlosshauer2013snapshot}."

### Issue 20: MINOR. Wigner's-friend / Local Friendliness work is absent from a section on "observers"

- **Location:** 07-rendering-qm.tex:186–215.
- **Evidence.** Observer-dependent rendering is precisely what the Local Friendliness no-go theorems constrain:
  - Frauchiger & Renner 2018;
  - Proietti et al. 2019;
  - Bong et al. 2020;
  - Wiseman, Cavalcanti & Rieffel 2023, which proposes a test with a human-level AI "friend" on a quantum computer, the closest concrete proposal to testing whether a "conscious observer" changes quantum predictions.
- **Fix.** One or two sentences with these citations. They are the observer-dependent tests that actually exist.

### Issue 21: MINOR. 't Hooft's prediction: add the concrete example and the caveat

- **Location:** 07-rendering-qm.tex:255–260.
- **Evidence.** CAI §5.8 gives a concrete example: "factoring a number with millions of digits into its prime factors will not be possible – unless fundamentally improved classical algorithms turn out to exist". The resource is quantified; the threshold is not computed.
- **Fix.** Add the factoring example and the caveat. Replace "a quantified, resource-based prediction" with "a resource-based falsification criterion".

### Issue 22: MINOR. Wheeler: consider verifying a stronger primary quote

- **Location:** 07-rendering-qm.tex:126–128.
- **Evidence.** The present claim is sourced via the RMP and is fine. My recollection is that "Law without law" contains an explicit statement that "consciousness" has nothing to do with the quantum process. **I have not verified this.** If confirmed, it would settle the point against render-on-demand readings of Wheeler.
- **Fix.** Check Wheeler & Zurek (1983), "Law without law", before adding. Otherwise leave as is.

### Issue 23: MINOR. Missing modern delayed-choice variants

- **Location:** 07-rendering-qm.tex, the table.
- **Evidence.** The table covers photonic delayed choice only up to 2013, plus Jacques 2007. It lacks:
  - Jacques et al. 2008, a continuous complementarity test;
  - the quantum-controlled delayed-choice experiments (Peruzzo et al. 2012; Kaiser et al. 2012);
  - Manning et al. 2015, with a single atom;
  - Vedovato et al. 2017, over a satellite link. This is the closest realisation of Wheeler's "cosmological" version mentioned at 07:125–126.
- **Fix.** Add at least Vedovato 2017 and Manning 2015 to the table.

### Issue 24: NIT. Labels for R

- 07:57–60. Kim et al.'s Fig. 1 text routes transmission to D3/D4, whereas Campbell et al. say reflection gives R=1. Define R by detector sets ({D3, D4} against {D1, D2}), not by reflection.

### Issue 25: NIT. Fringe period

- 07:60. Campbell's a = λL/d is the slit-screen geometry. In Kim et al., D0 sits in the Fourier plane, so the period is λf/d. Say so, or write "$a$ the fringe period".

### Issue 26: NIT. "The following argument is ours"

- 07:14. The empirical-equivalence point is standard; every interpretation of QM faces it. Drop the claim of originality, or cite a standard source.

### Issue 27: NIT. Hackermüller row

- 07:163–165. Specify "heating-laser power, C$_{70}$ at 190\,m/s, Talbot–Lau interferometer" (Fig. 2 caption).

### Issue 28: NIT. Luo et al. description

- 07:112–116. The polarisers are at ±45°, and the paper comes from E. J. Galvez's group at Colgate. Say "a paper from Galvez's group, co-authored by Khoshnoud", to avoid a guilt-by-association reading.

### Issue 29: NIT. Hensen et al. second run

- 07:221–222. Optionally cite the second run (Hensen et al., Sci. Rep. 6, 30289, 2016; doi:10.1038/srep30289) for completeness.

---

## 4. Missing literature (existence verified via Crossref or arXiv, 2026-09-27)

Items marked (R) are ones I read in part. All others have metadata only: authors must read them before citing, per CONVENTIONS §2.

**Duality, erasers and markers**
- Englert, PRL 77, 2154 (1996), doi:10.1103/PhysRevLett.77.2154. Currently METADATA only: read it.
- Greenberger & Yasin, Phys. Lett. A 128, 391 (1988), doi:10.1016/0375-9601(88)90114-4.
- Jaeger, Shimony & Vaidman, PRA 51, 54 (1995), doi:10.1103/PhysRevA.51.54.
- Scully, Englert & Walther, Nature 351, 111 (1991), doi:10.1038/351111a0.
- Zou, Wang & Mandel, PRL 67, 318 (1991), doi:10.1103/PhysRevLett.67.318.
- Kwiat, Steinberg & Chiao, PRA 45, 7729 (1992), doi:10.1103/PhysRevA.45.7729.
- Eichmann et al., PRL 70, 2359 (1993), doi:10.1103/PhysRevLett.70.2359.
- Herzog et al., PRL 75, 3034 (1995), doi:10.1103/PhysRevLett.75.3034.
- Buks et al., Nature 391, 871 (1998), doi:10.1038/36057. Theory: Aleiner, Wingreen & Meir, PRL 79, 3740 (1997), doi:10.1103/PhysRevLett.79.3740.
- Bertet et al., Nature 411, 166 (2001), doi:10.1038/35075517.
- (R) Walborn et al., PRA 65, 033818 (2002), doi:10.1103/PhysRevA.65.033818, arXiv:quant-ph/0106078.
- Lemos et al., Nature 512, 409 (2014), doi:10.1038/nature13586.
- Aharonov & Zubairy, Science 307, 875 (2005), doi:10.1126/science.1107787.
- Storey et al., Nature 367, 626 (1994), doi:10.1038/367626a0.
- Dürr & Rempe, Am. J. Phys. 68, 1021 (2000), doi:10.1119/1.1285869.
- Dürr, Nonn & Rempe, Nature 395, 33 (1998), doi:10.1038/25653. Read the original.

**Delayed choice**
- Jacques et al., PRL 100, 220402 (2008), doi:10.1103/PhysRevLett.100.220402.
- Peruzzo et al., Science 338, 634 (2012), doi:10.1126/science.1226719.
- Kaiser et al., Science 338, 637 (2012), doi:10.1126/science.1226755.
- Manning et al., Nat. Phys. 11, 539 (2015), doi:10.1038/nphys3343.
- Vedovato et al., Sci. Adv. 3, e1701180 (2017), doi:10.1126/sciadv.1701180.

**No-signalling**
- Ghirardi, Rimini & Weber, Lett. Nuovo Cim. 27, 293 (1980), doi:10.1007/BF02817189.

**Collapse-model bounds**
- Bassi et al., RMP 85, 471 (2013), doi:10.1103/RevModPhys.85.471. Already in the 09 bib.
- Vinante et al., PRL 116, 090402 (2016), doi:10.1103/PhysRevLett.116.090402.
- Fein et al., Nat. Phys. 15, 1242 (2019), doi:10.1038/s41567-019-0663-9.
- Donadi et al., Nat. Phys. 17, 74 (2021), doi:10.1038/s41567-020-1008-4.
- Carlesso et al., Nat. Phys. (2022), doi:10.1038/s41567-021-01489-5, arXiv:2203.04231.

**Bell, superdeterminism and measurement dependence**
- Wood & Spekkens, NJP 17, 033002 (2015), doi:10.1088/1367-2630/17/3/033002, arXiv:1208.4119.
- Hall, PRL 105, 250404 (2010), doi:10.1103/PhysRevLett.105.250404.
- Barrett & Gisin, PRL 106, 100406 (2011), doi:10.1103/PhysRevLett.106.100406.
- Wharton & Argaman, RMP 92, 021002 (2020), doi:10.1103/RevModPhys.92.021002, arXiv:1906.04313.
- Chen, "Bell's Theorem, Quantum Probabilities, and Superdeterminism", arXiv:2006.08609.
- Hensen et al., Sci. Rep. 6, 30289 (2016), doi:10.1038/srep30289.

**Observers and Wigner's friend**
- Frauchiger & Renner, Nat. Commun. 9, 3711 (2018), doi:10.1038/s41467-018-05739-8.
- Proietti et al., Sci. Adv. 5, eaaw9832 (2019), doi:10.1126/sciadv.aaw9832, arXiv:1902.05080.
- Bong et al., Nat. Phys. 16, 1199 (2020), doi:10.1038/s41567-020-0990-x, arXiv:1907.05607.
- Wiseman, Cavalcanti & Rieffel, Quantum 7, 1112 (2023), doi:10.22331/q-2023-09-14-1112, arXiv:2209.08491.
- (R) Schlosshauer, Kofler & Zeilinger, SHPMP 44, 222 (2013), doi:10.1016/j.shpsb.2013.04.004, arXiv:1301.1069.

---

## 5. Spot checks performed

| Item | Source checked | Result |
|---|---|---|
| Campbell Eq. (1)–(2), P[R=0]=1/2, "standard approximations" | arXiv v2 + IJQF PDF, p. 89 | Matches section |
| Campbell Remark 1: D1 and D2 both "Interference pattern", no π shift | IJQF pp. 85–86 | Confirmed; basis of Issues 1 and 3 |
| "supposed to be random (or … independent from X)" | IJQF p. 90 | Present; section omits it |
| "likely to be successful … only possible outcomes are … discontinuities … or paradoxes" | IJQF p. 93 | Present; section should quote it |
| All 12 Campbell page locators in the section (pp. 80, 81, 82, 83, 86, 87, 87–88, 91, 92, 94) | IJQF running headers | All correct |
| Figure 7 definition of R (erased → R=0) | Rendered page 11, arXiv | Confirmed |
| Kim: BS_A, BS_B, BS "50-50"; π shift; ≥ 8 ns; R03 no interference; no singles reported | quant-ph/9903047 | Confirmed; Eq. (10) locator imprecise (Issue 11) |
| Eq. (2) deviation of 1/2 (dark) and 1/6 (bright) | Own calculation | Correct |
| QM P(R=1\|X) = 1/2, and its robustness to t, φ, r_A ≠ r_B, η1 ≠ η2 | Own calculation (§2.2) | Correct under stated conditions (Issue 12) |
| Jacques 2007: 48 m, V = 94%, 0.50 ± 0.01, I > 0.99, QRNG space-like | quant-ph/0610241 | Correct (I measured in preliminary test; checked unchanged under delayed choice) |
| Ma 2013: 0.955(7), 0.951(18), 0.077(22), 55 m, 144 km, 450 µs | arXiv 1206.6578, Tables I–II | Numbers correct, but configuration conflated (Issue 5) |
| Ma 2012: 14–313 ns; F = 0.681 ± 0.034 vs 0.421 ± 0.029 | arXiv 1203.4834 | Correct |
| Hackermüller 2004: V = 47/29/7/0% at 0/3/6/10.5 W | quant-ph/0402146, Fig. 2 | Correct (add conditions, Issue 27) |
| Hornberger 2003: pressure-dependent loss of V, quantitative agreement | quant-ph/0303093 | Correct |
| Dürr 1998 quote and "10⁻⁴" | RMP arXiv 1407.2930 §IV.B | Matches RMP; original not read (Issue 17) |
| RMP §II.E "still present in the universe…" | 1407.2930 | Correct |
| Kastner "just noise" | arXiv 1905.03137 | Correct |
| Luo 2024: \|V\| = 0.65 ± 0.22; "did not need to measure"; acknowledgements | arXiv 2401.02351 | Correct |
| Hensen: S = 2.42 ± 0.20, 245 trials, p = 0.039 | 1508.05949 | Correct |
| Giustina 3.74×10⁻³¹; Shalm 5.9×10⁻⁹ / 2.3×10⁻⁷ | 1511.03190, 1511.03189 | Correct |
| BIG Bell: 97,347,490 choices, ~100,000 participants | 1805.04431 | Correct |
| Handsteiner: ≳ 7.31σ, ≳ 11.93σ, ~600 yr; Rauch: 9.3σ, ~7.8 Gyr, 96% | 1611.06985, 1808.05966 | Correct |
| H&P §4.3 quotes, §6 test, §3.1–3.2 on retrocausality | 1912.06462 | Quotes correct; see Issue 8 for balance |
| 't Hooft CAI §5.8 prediction and falsification sentence | 1405.1548 pp. 78–79 | Correct; factoring example omitted (Issue 21) |
| Irwin et al. "more widely agreed" and Tremblay summary; refs 76–79 | Entropy 2020 text | Correct; Radin 2016 is ref. 77 |
| Tremblay abstract (p > 0.05; no evidence) | PLoS ONE 2019 | Correct |
| Yampolskiy quotes; "best fitting interpretations" passage | Seeds of Science 2023 §3.6 | Quotes correct; qualifier needed (Issue 18) |
| Schlosshauer poll Q10 (6%) | arXiv 1301.1069 | Verified |
| Prior published critique of Campbell et al. on these grounds | Web search; ledger's INSPIRE/S2 searches | None found |

---

## 6. Issue counts

FATAL 0 · MAJOR 8 (Issues 1–8) · MINOR 15 (Issues 9–23) · NIT 6 (Issues 24–29).
