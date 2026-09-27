# Is the Universe a Simulation? A Structured Literature Survey

*Bombadil research notes — survey v0.1, September 2026*

## 0. Purpose and epistemic stance

The goal of this survey is **not** to argue that we live in a simulation. It is
to map what has actually been claimed, what has actually been tested, and where
a small research group could add something genuinely new.

The bare statement "the universe is a simulation" is not testable: a
sufficiently capable simulator could reproduce any physics we observe, and
could patch any anomaly we find. Research becomes possible only once the
hypothesis is narrowed into **sub-hypotheses about how a simulator would be
built**, each of which predicts something measurable. Throughout, we use this
convention:

| Label | Sub-hypothesis | What it predicts |
|---|---|---|
| **H-grid** | Spacetime is computed on a fixed (e.g. cubic) lattice | Broken rotational / Lorentz symmetry; energy cut-offs; direction-dependent effects at extreme energies |
| **H-noise** | Space has finite "pixel" resolution with holographic information limits | Correlated position jitter between nearby interferometers |
| **H-lazy** | The simulator only computes detail when it is observed ("render on demand") | Deviations from standard quantum mechanics in which-path / delayed-choice experiments |
| **H-budget** | The simulator runs on finite classical resources | Physics that is exponentially hard to compute classically should be absent or approximated |
| **H-info** | Information is a physical quantity with its own dynamics, as a computational substrate might imply | Mass of information; a "second law of infodynamics" |

An important caveat applies to every row: **each of these signatures is also
predicted by some non-simulation physics** (quantum gravity, discrete spacetime
models, and so on). A positive result would therefore show "spacetime is
discrete in way X", not "we are simulated". A null result excludes only the
particular simulator design that was assumed. The honest framing is that
experiments **bound the space of cheap simulators**.

---

## 1. Philosophical foundations

### 1.1 Bostrom's simulation argument
Bostrom (2003) argues that **at least one** of the following is true:
1. almost all civilizations at our level go extinct before becoming "posthuman";
2. almost no posthuman civilizations are interested in running ancestor simulations;
3. we are almost certainly living in a simulation.

It is a trilemma, not an argument *for* proposition 3. It rests on two
assumptions: **substrate independence** (minds can run on silicon) and a
**bland indifference principle** (if most observers with your experiences are
simulated, you should believe you probably are).

### 1.2 Principal critiques
- **Weatherson (2003)** questions the indifference principle: evidence about
  our own experiences need not be treated as a random sample over all observers.
- **Birch (2013)** argues the argument asks for *selective* scepticism that is
  hard to apply consistently: it relies on empirical knowledge of computing and
  history that a simulated agent has no special reason to trust.
- **Carroll (2016, blog)** gives the "resolution/recursion" argument. Most
  simulated observers would live in low-resource, deeply nested simulations
  that cannot run simulations of their own. We are able to contemplate running
  simulations, so we are atypical of that population, and the typicality
  reasoning undermines itself.
- **Kipping (2020)** makes the argument Bayesian with model averaging over
  "simulations are possible" and "not possible". The posterior probability that
  we are simulated comes out **slightly below 50%**. It approaches 50% only in
  the limit of infinitely many simulations. This assumes equal prior weight on
  the two models, which Kipping himself notes may be generous to the
  simulation side.
- **Chalmers (2022, *Reality+*)** argues the question is metaphysically
  meaningful but that being simulated would not make the world "unreal".

**Takeaway:** the philosophical case is a probabilistic argument whose premises
are contested. It motivates the physics, but it provides no evidence.

---

## 2. Physical tests, grouped by sub-hypothesis

### 2.1 H-grid — spacetime on a lattice

**Beane, Davoudi & Savage (2012 preprint; EPJ A 2014).** This is the
foundational paper. It assumes the universe is simulated in the manner of
present-day lattice QCD: a cubic grid with spacing *b* and unimproved Wilson
fermions. It derives:
- the strongest bound, **b⁻¹ ≳ 10¹¹ GeV**, from the fact that the observed
  cosmic-ray spectrum extends to the GZK cut-off. A lattice imposes a maximum
  momentum, so the spectrum would have to end;
- weaker bounds from the muon g-2 and from differences between determinations of α;
- a **distinctive signature**: the highest-energy cosmic rays should show an
  anisotropy with the **cubic symmetry of the lattice**, meaning structure
  aligned with three preferred axes rather than a smooth dipole.

**Lorentz-invariance-violation (LIV) limits.** Any lattice with a preferred
frame modifies particle dispersion relations. The linear LIV energy scale is
now bounded well above the Planck energy:
- Fermi-LAT, GRB 090510 (Abdo et al. 2009): E_QG,1 ≳ 1.2 E_Pl;
- LHAASO, GRB 221009A (Cao et al. 2024): **E_QG,1 > 10 E_Pl** and
  E_QG,2 > 6×10⁻⁸ E_Pl (95% CL).

**Fine-tuning argument (Collins et al. 2004).** Lorentz violation at the Planck
scale does not stay at the Planck scale. Radiative corrections carry it down to
low-energy physics, where it is already excluded to high precision, unless the
theory is heavily fine-tuned. This makes naive preferred-frame lattices very
hard to sustain.

**The key loophole: Lorentz-invariant discreteness.** Causal-set theory
(Bombelli et al. 1987; Dowker, Henson & Sorkin 2004) shows that spacetime can
be fundamentally discrete **without** a preferred frame, by using a random
(Poisson) "sprinkling" of points instead of a regular grid. A simulator built
this way would show **none** of the anisotropy signatures. Its predicted
signature is instead a Lorentz-invariant momentum diffusion ("swerves").

**Status:** naive fixed-grid simulators are strongly constrained. The *cubic
anisotropy* signature proposed by Beane et al. appears **not to have been
directly searched for** in published cosmic-ray data (see §4, R1). We found no
dedicated analysis; this needs a more exhaustive check.

**Relevant data now public:**
- Pierre Auger Observatory: a dipole of ~6.5% above 8 EeV at >5.2σ (Auger
  Collaboration 2017). It is interpreted as extragalactic in origin, and it is
  the dominant large-scale structure any lattice search must model.
- **Auger Open Data**: 10% of cosmic-ray events released in 2021, expanding to
  **30% of Phase-I surface-detector events above 2.5 EeV (2004–2022)**.

### 2.2 H-noise — pixelated / holographic space

- **Hogan (2008)** proposed that holographic information bounds imply
  measurable, correlated transverse position noise ("holographic noise").
- The **Fermilab Holometer** (Chou et al. 2016, PRL 117, 111102) used two
  co-located 39 m Michelson interferometers and reached 2.1×10⁻²⁰ m/√Hz. It
  **excluded Hogan's original model** at high significance. Later papers
  constrained other geometries of the correlation.

**Status:** the specific model is excluded. Modified models (rotational or
"shear" correlations, horizon-coherence models) remain under discussion. This
is not simulation-specific, but it is the cleanest example of a "pixel" test
actually being carried out.

### 2.3 H-lazy — rendering on demand

- **Campbell, Owhadi, Sauvageau & Watkinson (2017)** proposed variants of the
  double-slit and delayed-choice quantum-eraser experiments. The idea is that a
  resource-saving simulator would compute interference only when which-path
  information *could* reach an observer.
- **Critical issue:** standard quantum mechanics already makes definite
  predictions for all of these set-ups, and those predictions have been
  confirmed repeatedly in delayed-choice / eraser experiments. A "lazy
  rendering" simulator that faithfully reproduces QM is observationally
  identical to QM. A test is informative only if the hypothesis predicts a
  **deviation** from QM, and the proposals do not quantify one.

**Status:** conceptual. We are not aware of a published result that
distinguishes H-lazy from standard QM. This needs checking.

### 2.4 H-budget — computational-complexity arguments

- **Feynman (1982):** simulating quantum systems on classical computers costs
  exponential resources. A simulator of our universe would need to be quantum,
  or to approximate.
- **Lloyd (2002):** the observable universe could have performed at most
  ~10¹²⁰ elementary operations on ~10⁹⁰ bits (~10¹²⁰ bits if
  gravitational degrees of freedom are included). This bounds the cost of an exact simulation of the
  universe *by something inside it*.
- **Ringel & Kovrizhin (2017, Sci. Adv.):** systems with quantized
  gravitational (thermal Hall) responses cannot be simulated by *local,
  sign-free quantum Monte Carlo*. The press reported this as "the universe is
  not a simulation". In fact it rules out only one class of classical algorithm.
- **Faizal, Krauss, Shabir & Marino (2025, J. Holography Appl. Phys.):**
  argue from Gödel/Tarski/Chaitin-type undecidability that a complete theory of
  physics cannot be algorithmic, and therefore that the universe cannot be
  simulated. A 2025 comment ("Provability vs. Execution", arXiv:2512.11807)
  counters that *proving* every truth within a formal system is different from
  *executing* dynamics. On this view, incompleteness limits what can be known,
  not what can be run.

**Status:** these are arguments about in-principle cost and computability. None
is an empirical test. They constrain the *simulator's* architecture (quantum,
hypercomputational, or approximate) more than they settle the question.

### 2.5 H-info — information as physics

- **Vopson (2019):** mass–energy–information equivalence. It proposes that a
  stored bit has a small mass, m = k_B T ln 2 / c².
- **Vopson (2022, AIP Adv. 12, 035311):** an experimental protocol. Electron–
  positron annihilation should emit, in addition to the two 511 keV photons,
  two **~50 µm infrared photons** from erasure of the particles' information
  content (at room temperature). **No result has been reported.**
- **Vopson & Lepadatu (2022), Vopson (2023, AIP Adv. 13, 105308):** the
  "second law of infodynamics", which claims that the information entropy of
  information-bearing systems stays constant or decreases over time. The 2023
  paper links this to symmetry and to "data compression" by a simulator.
- **Critiques:** these are contested. Public criticism (e.g. Hossenfelder's
  2025 commentary on the related "gravity as computation" paper, and Vopson's
  reply) focuses on the entropy definitions, the estimators, and whether
  "information entropy" is used consistently. Some reformulations exist, for
  example a "thermocontextual" reformulation (2025).

**Status:** there is one sharp, testable prediction (the IR photons), and it is
untested. The infodynamics claims rest on specific entropy estimators applied
to specific datasets, which makes them **reproducible and auditable** with
modest resources.

---

## 3. Cross-cutting problems

1. **Signature degeneracy.** Every proposed signature (lattice anisotropy, LIV,
   holographic noise, information mass) is also predicted by some
   *non-simulation* physics. No experiment distinguishes "simulated discrete
   physics" from "discrete physics".
2. **Adversarial / adaptive simulator.** If the simulator can detect and patch
   probes, null results mean nothing. Research has to assume a *non-adaptive,
   resource-limited* simulator, and should say so explicitly.
3. **Design-specific null results.** Beane et al. assumed *unimproved Wilson
   fermions on a cubic grid*. With improved actions, discretization errors
   shrink from O(b) to O(b²) or better, and the bounds weaken. No paper
   systematically maps bounds across simulator designs.
4. **Publication and press distortion.** Several results (Ringel & Kovrizhin;
   Faizal et al.; Vopson) were widely reported with conclusions stronger than
   the papers support. A survey should always cite the paper, not the press
   release.

---

## 4. Research opportunities (ranked by feasibility × novelty)

**R1 — Search for cubic-symmetric anisotropy in Auger open data.** *(Most
promising.)* Expand the arrival-direction distribution above ~40 EeV in
spherical harmonics. Build the **cubic-group (O_h) invariants** at ℓ = 4 and 6.
Scan over all lattice orientations in SO(3)/O_h, correct for the look-elsewhere
effect, and model the known dipole and the non-uniform detector exposure. The
outcome is either a detection or an upper limit on lattice-aligned anisotropy
as a function of orientation. The data are public and the tools are standard
(HEALPix, healpy), and to our knowledge nobody has done this analysis.
*Caveat:* Galactic magnetic-field deflections of ~degrees to tens of degrees
smear high-ℓ structure, so sensitivity has to be established on simulated
skies first.

**R2 — A "simulator design space" map of lattice bounds.** Take Beane et al.'s
approach and recompute the GZK and LIV-derived bounds on *b* for several
discretizations: Wilson, staggered, domain-wall, improved (O(b²)) actions,
anisotropic lattices, and random (causal-set-like) discretizations. Plug in
current LIV limits (LHAASO 2024). The deliverable is a single table/figure
showing which cheap-simulator architectures are already excluded.

**R3 — Reproducible audit of the second law of infodynamics.** Re-run the
published entropy analyses (digital data and genome mutation datasets) with
several entropy estimators: plug-in Shannon, Miller–Madow, NSB, and
compression-based. Check whether the reported *decrease* in entropy is robust,
or whether it is an artifact of the estimator or of finite sampling.

**R4 — Quantifying H-lazy.** Write down an explicit, resource-bounded rendering
model. Derive the size of its *deviation* from QM in a delayed-choice
experiment, as a function of the simulator's "budget". Compare with existing
experimental precision to bound the budget. This turns a conceptual proposal
into a falsifiable one.

**R5 — Bayesian nesting model.** Extend Kipping (2020) with Carroll's
resource-decay-with-depth argument. Each simulation level has a smaller budget,
so observers at depth *d* have fewer resources. Compute the posterior as a
function of the decay rate, and check whether our being able to plan
simulations counts as evidence against being deep in the stack.

**Suggested starting point:** R1 on synthetic skies. Build the O_h-invariant
estimator, inject a lattice-aligned signal plus the Auger dipole and exposure,
and measure detection power. Only then apply it to the open data. R2 is a good
parallel, pen-and-paper track.

---

## 5. Open questions to resolve before committing to R1

- Has any cosmic-ray collaboration already published an O_h / cubic-harmonic
  search? This needs an ADS full-text search for "cubic symmetry" and
  "lattice spacing" in UHECR papers.
- What exactly is the expected *magnitude* of the lattice anisotropy for a
  given *b* in Beane et al.? This needs extracting from the paper.
- Which energy threshold and event count does the 30% Auger release provide
  above 40 EeV? This sets the statistical reach.

---

## References

*Verification note:* citation details below were checked against publisher,
ADS, arXiv-listing or institutional pages via web search in September 2026.
Direct arXiv access was unavailable from the research environment, so
page-level details should be re-checked before any citation in formal writing.

**Philosophy / probability**
- Bostrom, N. (2003). Are We Living in a Computer Simulation? *Philosophical Quarterly* 53(211), 243–255.
- Weatherson, B. (2003). Are You a Sim? *Philosophical Quarterly* 53(212), 425–431.
- Birch, J. (2013). On the 'simulation argument' and selective scepticism. *Erkenntnis* 78, 95–107.
- Kipping, D. (2020). A Bayesian Approach to the Simulation Argument. *Universe* 6(8), 109. [doi:10.3390/universe6080109](https://doi.org/10.3390/universe6080109) · [arXiv:2008.12254](https://arxiv.org/abs/2008.12254)
- Chalmers, D. J. (2022). *Reality+: Virtual Worlds and the Problems of Philosophy.* W. W. Norton.
- Carroll, S. (2016). Maybe We Do Not Live in a Simulation: The Resolution Conundrum. *Preposterous Universe* (blog).

**Lattice / Lorentz invariance**
- Beane, S. R., Davoudi, Z., Savage, M. J. (2014). Constraints on the Universe as a Numerical Simulation. *Eur. Phys. J. A* 50, 148. [Springer](https://link.springer.com/article/10.1140/epja/i2014-14148-0) · [arXiv:1210.1847](https://arxiv.org/abs/1210.1847)
- Collins, J., Perez, A., Sudarsky, D., Urrutia, L., Vucetich, H. (2004). Lorentz invariance and quantum gravity: an additional fine-tuning problem? *Phys. Rev. Lett.* 93, 191301. [doi:10.1103/PhysRevLett.93.191301](https://doi.org/10.1103/PhysRevLett.93.191301)
- Bombelli, L., Lee, J., Meyer, D., Sorkin, R. D. (1987). Space-time as a causal set. *Phys. Rev. Lett.* 59, 521.
- Dowker, F., Henson, J., Sorkin, R. D. (2004). Quantum gravity phenomenology, Lorentz invariance and discreteness. *Mod. Phys. Lett. A* 19, 1829–1840. [arXiv:gr-qc/0311055](https://arxiv.org/abs/gr-qc/0311055)
- Abdo, A. A. et al. (Fermi-LAT/GBM) (2009). A limit on the variation of the speed of light arising from quantum gravity effects. *Nature* 462, 331–334.
- Cao, Z. et al. (LHAASO) (2024). Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A. *Phys. Rev. Lett.* 133, 071501. [doi:10.1103/PhysRevLett.133.071501](https://link.aps.org/doi/10.1103/PhysRevLett.133.071501)

**Cosmic-ray data**
- Pierre Auger Collaboration (2017). Observation of a large-scale anisotropy in the arrival directions of cosmic rays above 8×10¹⁸ eV. *Science* 357, 1266–1270. [doi:10.1126/science.aan4338](https://www.science.org/doi/10.1126/science.aan4338)
- Pierre Auger Collaboration (2024–25). The Pierre Auger Observatory open data. *Eur. Phys. J. C.* [Springer](https://link.springer.com/article/10.1140/epjc/s10052-024-13560-5) · [Data portal](https://opendata.auger.org/data.php) · [Expansion to 30%: arXiv:2507.08504](https://arxiv.org/abs/2507.08504)

**Holographic noise**
- Hogan, C. J. (2008). Measurement of quantum fluctuations in geometry. *Phys. Rev. D* 77, 104031.
- Chou, A. S. et al. (Holometer) (2016). First Measurements of High Frequency Cross-Spectra from a Pair of Large Michelson Interferometers. *Phys. Rev. Lett.* 117, 111102. [doi:10.1103/PhysRevLett.117.111102](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.117.111102)

**Rendering / complexity / computability**
- Campbell, T., Owhadi, H., Sauvageau, J., Watkinson, D. (2017). On Testing the Simulation Theory. *Int. J. Quantum Foundations* 3(3), 78–99. [IJQF](https://ijqf.org/archives/4105) · [arXiv:1703.00058](https://arxiv.org/abs/1703.00058)
- Feynman, R. P. (1982). Simulating physics with computers. *Int. J. Theor. Phys.* 21, 467–488.
- Lloyd, S. (2002). Computational capacity of the universe. *Phys. Rev. Lett.* 88, 237901.
- Ringel, Z., Kovrizhin, D. L. (2017). Quantized gravitational responses, the sign problem, and quantum complexity. *Sci. Adv.* 3(9), e1701758. [doi:10.1126/sciadv.1701758](https://www.science.org/doi/10.1126/sciadv.1701758)
- Faizal, M., Krauss, L. M., Shabir, A., Marino, F. (2025). Consequences of Undecidability in Physics on the Theory of Everything. *J. Holography Appl. Phys.* 5(2), 10–21. [arXiv:2507.22950](https://arxiv.org/abs/2507.22950)
- Comment: Provability vs. Execution: A Comment on "Consequences of Undecidability in Physics on the Theory of Everything" (2025). [arXiv:2512.11807](https://arxiv.org/abs/2512.11807)

**Information physics**
- Vopson, M. M. (2019). The mass-energy-information equivalence principle. *AIP Advances* 9, 095206.
- Vopson, M. M. (2022). Experimental protocol for testing the mass–energy–information equivalence principle. *AIP Advances* 12, 035311. [doi:10.1063/5.0087175](https://pubs.aip.org/aip/adv/article/12/3/035311/2819739)
- Vopson, M. M., Lepadatu, S. (2022). Second law of information dynamics. *AIP Advances* 12, 075310.
- Vopson, M. M. (2023). The second law of infodynamics and its implications for the simulated universe hypothesis. *AIP Advances* 13, 105308. [AIP](https://pubs.aip.org/aip/adv/article/13/10/105308/2915332)
- Vopson, M. M. (2025). Is gravity evidence of a computational universe? *AIP Advances* 15, 045035. [doi:10.1063/5.0264945](https://doi.org/10.1063/5.0264945)
- Response to Hossenfelder's commentary (2025). *IPI Letters.* [link](https://ipipublishing.org/index.php/ipil/article/view/212)
