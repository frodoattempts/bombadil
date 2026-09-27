# Report for 03-lattice-liv: discretized spacetime as a simulation signature

Files:
- `research/ledgers/03-lattice-liv.md`: 68 claims (C-03-001 to C-03-068; 8 are THIS WORK derivations: C-03-018, C-03-020 to C-03-026)
- `research/bib/03-lattice-liv.bib`: 38 entries, all from INSPIRE BibTeX with keys rewritten. The Abdo2009limit author field was corrected against Crossref.
- `paper/sections/03-lattice-liv.tex`: section draft. Test-compiled standalone (11pt, 1in margins): about 6 pages of text plus 2 of references, so roughly 4 pages in two-column format
- PDFs and text: `/tmp/claude-0/papers/` (retrieved 2026-09-27)

## A. Coverage and main findings

1. **Beane, Davoudi & Savage** (arXiv v2) was read in full, and every number is ledgered with its equation locator:
   - Muon g−2 gives b^{-1} = (3.6 ± 1.1)×10^7 GeV (eq. 10). This is a *value* obtained by attributing the 2012 ~3.6σ anomaly to the lattice spacing, not a null bound.
   - The α comparison gives b^{-1} ≳ 4×10^8 GeV at 1σ (eq. 13).
   - The cosmic-ray argument gives E_max ~ 1/b and hence b^{-1} ~ 10^11 GeV (p. 11-12), with no confidence level.
   - The anisotropy is quantified only through the direction-dependent GZK threshold, eq. (18). The paper gives no arrival-direction amplitude.
2. **The quoted GZK value is nonstandard.** Beane et al. write "GKZ-cut off scale [...] of ∼ 6×10^20 eV". The conventional threshold is ≃ 5×10^19 eV (Liberati 2013), and Auger measures the suppression at E_34 = (46±3±6)×10^18 eV. The order-of-magnitude bound survives, since the observed spectrum reaches ~10^20 eV (section 04), but the text should not repeat 6×10^20 eV as "the GZK cutoff".
3. **Main result of this work (section D).** The unimproved-Wilson dispersion relations that Beane et al. write down imply (n = 4, i.e. dimension-6) subluminal modified dispersion for every species. Mapped onto the existing LIV literature, they give much stronger constraints than the GZK/E_max estimate:
   - Photon time of flight (LHAASO GRB 221009A, 95% CL): b^{-1} ≳ 2×10^11 GeV
   - Photon decay kinematics plus LHAASO PeV photons: b^{-1} ≳ 4×10^14 GeV
   - Crab synchrotron, via Liberati-Maccione-Sotiriou (95% CL): b^{-1} ≳ 1×10^16 GeV
   - Auger GZK photons, conditional on a proton component: b^{-1} ≳ 3×10^19 GeV

   For the scenario as Beane et al. specified it, the cubic threshold anisotropy at 5×10^10 GeV is therefore bounded to a fraction ≲ 10^{-11}. A tree-level O(b)-improved (clover) action has the same free dispersion and is equally constrained. Only an action whose dispersion is improved to all orders (nonperturbatively) at O(b^2) falls back to b^{-1} ≳ 10^11 GeV. **These are our derivations, not published results.** They should be reviewed by a lattice theorist before submission (see E.1).
4. **Kinematic disagreement with Beane et al.** They state that γ → e+e− proceeds only for photon energies comparable to 1/b near the Brillouin-zone edge. With their own eqs. (16)-(17), the Wilson-fermion O(b^2) coefficient is 4× the boson one at equal momentum. Asymmetric pair production is then allowed above k_th ≈ 2.5 (m_e/b)^{1/2}, and we checked this numerically with the exact lattice relations (D.3). The symmetric split x = 1/2 is exactly degenerate at O(b^2), which may be why the channel was missed.
5. **Naturalness.** Beane et al. dismiss the Collins et al. fine-tuning problem by invoking Euclidean hypercubic symmetry (fn. 3). Polchinski (2012, commenting on Gambini et al.) argues that this protection does not carry over to a Lorentzian lattice and that continuing from the Euclidean lattice conflicts with unitarity. The Hadron Spectrum Collaboration's anisotropic lattices show the tuning concretely: the gauge and fermion anisotropies must be tuned separately to restore the "speed of light". The `.tex` presents these three positions side by side without adjudicating.
6. **Lorentz-invariant discreteness.** The causal-set arguments are covered: the Bombelli-Henson-Sorkin theorem, infinite valency and non-locality, swerve bounds (Kaloper-Mattingly k < 10^{-61} GeV^3; c < 10^{-118} for γ = 3), and the fact that quantum field theory on causal sets exists only for the free scalar.

## B. Papers citing Beane et al. and our assessment

The query `refersto:arxiv:1210.1847` returned a malformed result on INSPIRE (25,074 unrelated hits). We used `refersto:recid:1189720` instead, which returned 13 records on 2026-09-27. Semantic Scholar returned 61 citing records. OpenAlex's daily budget was exhausted and gave no result.

INSPIRE (13):

| arXiv / DOI | Paper | Substantive physics follow-up? |
|---|---|---|
| 1210.8348 | Andersen, "Lorentz Covariant Lattice Gauge Theory" (2012, unrefereed, 0 cites) | **Yes (direct response).** Claims a lattice-graph formulation with exact Lorentz covariance and concludes that a "digital universe" need not break Lorentz symmetry. Technical validity not assessed. Ledger C-03-034. |
| 2504.08461 | Vazza, Front. Phys. 13 (2025) | **Partly.** Energy-cost argument against simulating the universe or Earth. Uses the 10^20 eV UHECR and 10^17 eV neutrino scales as resolution requirements. Misquotes Beane's bound units ("inverse lattice spacing ~10^-11 GeV^-1"). Ledger C-03-067. |
| 1701.07161 | Kakushadze, "Does the Universe have a Hard Drive?" | No. Information-paradox essay that cites Beane in passing. |
| 1910.10147 | Qin, Sci. Rep. 10 (2020), discrete field theories and machine learning | No. Uses the simulation hypothesis as motivation for discrete field theory and ML. No test. |
| 2303.03096 | Leckey & Flitney, spontaneous collapse motivated by discrete physics | No. Mentions Beane as considering consequences of discrete spacetime. |
| quant-ph/0310033 | Leckey, "Quantum Measurement, Complexity and Discrete Physics" | No (a 2003 preprint whose later version cites Beane). |
| — | Irwin et al., Entropy 22 (2020), self-simulation hypothesis | No. Interpretational. |
| 1712.08731 | Bleu et al., PRB 97 (2018), quantum geometric tensor in photonic systems | No (probably a mis-linked citation). |
| 2201.00805; 2212.00260 | Feng et al.; Chandra et al. (quantum-computer simulations of SCQM / matrix big bang) | No. Cite Beane as motivation for simulating physics on quantum computers. |
| 2105.11548 | Stryker, PRD 112 (2025), gauge-invariant Trotterization | No. Motivation only. |
| 10.1017/9781108951968 | Perovic, "The Cosmic Microwave Background" (book, 2024) | No (philosophy of cosmology). |
| 10.3390/universe8010040 | Miguel-Tomé et al., Universe 8 (2022), computer-theoretic framework | No. Conceptual. |

Additional physics-relevant records from Semantic Scholar only (not on INSPIRE):
- 1703.00058, Campbell, Owhadi, Sauvageau, Watkinson (2017): proposes quantum-measurement ("render on observation") tests and cites Beane. Not lattice. Belongs to another section.
- 1709.09593, Xiao, Qin et al. (PLA 2019): lattice Maxwell system with discrete space-time symmetry. Cites Beane as consistent with the simulation hypothesis. No observational test.
- 2008.12254, Kipping, Universe 6 (2020): Bayesian treatment of the simulation argument. Not lattice.
- 10.1088/2632-072X/ae1e50 (2025), "What computer science has to say about the simulation hypothesis", J. Phys. Complexity: computational and complexity arguments. Not lattice. Belongs to another section.
- The remaining ~50 are philosophy, theology, AI-alignment and popular items.

**Conclusion:** in all three databases we found no paper that re-derives, extends, or tests Beane et al.'s lattice bounds or cubic-anisotropy prediction against data. The only technical responses are Andersen (2012, unrefereed) and passing uses (Vazza 2025).

## C. Searches performed (for "we are not aware of" statements)

- INSPIRE: `refersto:recid:1189720`; `fulltext:"simulation hypothesis"` (36 hits, screened); `abstracts.value:"simulation hypothesis"` (7); `t "simulated universe"` (7, all astrophysical N-body); `fulltext:"1210.1847"` (5); `fulltext:"Beane" and fulltext:"lattice spacing" and fulltext:"GZK"` (4); `fulltext:"numerical simulation" and fulltext:"Beane" and fulltext:"arrival directions"` (0); `fulltext:"lattice spacing" and fulltext:"simulation" and fulltext:"Pierre Auger" and fulltext:"cubic"` (23, none relevant); `abstracts.value:"space-time lattice" and abstracts.value:"Lorentz"` (4, historical: Wilson 1976, Thacker 1998, 't Hooft 2012, Lorente 1976).
- arXiv full-text search (arxiv.org/search): "simulation hypothesis lattice", "universe numerical simulation lattice spacing", "simulated universe Lorentz violation", "simulation hypothesis cosmic rays", "simulation hypothesis test". The only new relevant item was Gantumur 2512.22072 (rotation-covariant Euclidean lattice regulator, JHEP 2026).
- Semantic Scholar citation API for arXiv:1210.1847 (61 records).
- No search for "cubic anisotropy" in UHECR arrival directions returned a dedicated analysis. We are not aware of any published search. Section 04 should confirm this with an observational-literature search.

## D. Derivations (this work)

Units: hbar = c = 1, lattice spacing b, and lattice rest frame taken as the CMB frame, as in Beane et al. Numerical checks are in the scratchpad scripts `decay.py`, `checks.py` and `crab.py`. Their outputs are reproduced below.

### D.1 Small-momentum expansion of Beane et al.'s dispersion relations

Boson, eq. (16) with m_b = 0: sinh^2(bE/2) = Σ_j sin^2(bk_j/2). Using sinh^2(x/2) = x^2/4 + x^4/48 + … and sin^2(y/2) = y^2/4 − y^4/48 + …:

  E^2 + b^2E^4/12 = k^2 − (b^2/12) Σ_j k_j^4  ⇒  **E^2 = k^2 − (b^2/12)(k^4 + Σ_j k_j^4) + O(b^4)**.

Wilson fermion, eq. (17): sinh^2(bE) = Σ sin^2(bk_j) + [bm + 2r(Σ sin^2(bk_j/2) − sinh^2(bE/2))]^2. The bracket is bm + (rb^2/2)(k^2 − E^2) + O(b^4k^4), with k^2 − E^2 = −m^2 + O(b^2k^4). Its square is therefore b^2m^2 − rb^3m^3 + (terms suppressed by m). With sinh^2 x = x^2 + x^4/3 and sin^2 y = y^2 − y^4/3:

  **E^2 = k^2 + m^2 − rbm^3 − (b^2/3)(k^4 + Σ_j k_j^4) + …**

This reproduces the O(b) term of eq. (17). Define n = k/|k| and f(n) = 1 + Σ_j n_j^4 ∈ [4/3 (111), 2 (100)].

Numerical check at |k| = 0.01/b, comparing (E^2 − k^2)/k^4 from the exact relations with the prediction:

| direction | boson (exact / predicted) | fermion, m = 0 (exact / predicted) | boson, continuous time (exact / predicted) |
|---|---|---|---|
| (100) | −0.16666 / −1/6 | −0.66662 / −2/3 | −0.08333 / −1/12 |
| (111) | −0.11111 / −1/9 | −0.44442 / −4/9 | −0.02778 / −1/36 |
| (110) | −0.12500 / −1/8 | −0.49997 / −1/2 | −0.04167 / −1/24 |

With continuous time (a Hamiltonian lattice), the E^4 term is absent and f → Σ_j n_j^4 ∈ [1/3, 1].

Eq. (16) has one physical branch, so the lattice photon is not birefringent. For the Wilson plaquette action, both transverse modes satisfy the same relation. The dispersion is even in k, so no n = 3 (dimension-5, CPT-odd) terms arise, and birefringence limits (Götz 2014; Kostelecký-Mewes 2013) do not constrain the scenario at leading order.

Scope of the fermion coefficient b^2/3: it is the naive-derivative sin(bk_j)/b coefficient. It is the same for naive, staggered, and clover (O(b)-improved) Wilson fermions, because the clover term vanishes for free fields. We have not derived the domain-wall or overlap light-mode dispersion.

### D.2 The anisotropy in eq. (18)

Using Y_4^0 = (3/(16√π))(35cos^4θ − 30cos^2θ + 3) and Y_4^{±4} = (3/16)sqrt(35/(2π)) sin^4θ e^{±4iφ}, the combination in eq. (18) satisfies

  K(θ,φ) ≡ Y_4^0 + sqrt(5/14)(Y_4^4 + Y_4^{−4}) = (15/(4√π)) (Σ_j n_j^4 − 3/5).

This was checked at random directions: for example, K = 0.48469 vs 0.48469 and K = −0.30459 vs −0.30459 after fixing the coefficient. At the axis it gives 3/(2√π) = Y_4^0(0), as it should.

The fractional threshold shift in eq. (18) is therefore

  δω/ω = (√π/9) K (b|p|)^2 = (5/12)(Σ_j n_j^4 − 3/5)(b|p|)^2,

which is +(b|p|)^2/6 along an axis and −(b|p|)^2/9 along a body diagonal, with an angular average of zero. The spread is (5/18)(b|p|)^2:
- |p| = 5×10^10 GeV, b^{-1} = 10^11 GeV: spread ≈ 0.069
- b^{-1} = 1.3×10^16 GeV: spread ≈ 4×10^{-12}

This is a threshold shift. Converting it into an arrival-direction anisotropy requires propagation modelling, which neither Beane et al. nor we have done.

### D.3 Photon decay γ → e+e−

For E ≫ m, E_γ(k) ≈ k − c_γk^3 with c_γ = fb^2/24, and E_e(p) ≈ p + m^2/(2p) − c_ep^3 with c_e = fb^2/6 = 4c_γ (same direction, collinear final state). Following the EFT result that threshold configurations have parallel outgoing momenta and allow unequal splits (Liberati 2013, Sec. 6.2.3), split k into xk and (1−x)k and set y = x(1−x) ∈ (0, 1/4]. Then

  E_pair − E_γ = m^2/(2ky) − c_γk^3[4(1 − 3y) − 1] = m^2/(2ky) − 3c_γk^3(1 − 4y).

At y = 1/4 (the symmetric split) the O(b^2) terms cancel exactly. For y < 1/4 the decay is allowed once k^4 ≥ m^2/[6c_γ y(1 − 4y)]. Maximizing y(1 − 4y) = 1/16 at y = 1/8:

  **k_th^4 = 8m^2/(3c_γ) = 64 m^2/(f b^2), so k_th = (64/f)^{1/4}(m/b)^{1/2} ≈ 2.4–2.6 (m/b)^{1/2}.**

Numerical check with the exact eqs. (16)-(17): b = 1, m = 10^{-4}, r = 1, grid over the collinear fraction plus a 3D Nelder-Mead minimization of E_e(q) + E_e(k−q). The table gives E_γ − min E_pair:

| k | (100) | (111) | (110) |
|---|---|---|---|
| 0.005 | −4.0e-6 | −4.0e-6 | −4.0e-6 |
| 0.01 | −2.0e-6 | −2.0e-6 | −2.0e-6 |
| 0.02 | −8.3e-7 | −9.8e-7 | −9.5e-7 |
| 0.03 | **+2.5e-6** | **+1.0e-6** | **+1.4e-6** |
| 0.05 | +2.4e-5 | +1.5e-5 | +1.7e-5 |

The predicted k_th is 0.0238 (100) and 0.0263 (111), consistent with the sign change between 0.02 and 0.03. The kinematic statement is therefore robust for the relations as written.

Bound: requiring no decay below k_obs gives b^{-1} > k_obs^2 f^{1/2}/(8 m_e). We take k_obs = 1140 TeV (LHAASO 95% CL lower limit on any spectral cutoff of LHAASO J2032+4102) and m_e = 0.511 MeV:
- f = 4/3: 3.7×10^14 GeV
- f = 2: 4.5×10^14 GeV
- continuous time (f → Σn^4 ∈ [1/3, 1]): 1.8–3.2×10^14 GeV

This assumes that, once allowed, decay is fast on Galactic (kpc) scales. JLM 2006 and Liberati 2013 argue this for EFT modified dispersion relations: lifetime ≪ 1 s, and (10^{-6} ns)^{-1} for n = 4. We did not compute the lattice matrix element or check the rate close to threshold.

### D.4 Time of flight

LHAASO uses E^2 ≃ p^2[1 − s(E/E_QG,2)^2]. Matching to D.1 gives s = +1 (subluminal) and E_QG,2 = b^{-1}(12/f)^{1/2}. With E_QG,2 > 6.9×10^11 GeV (Table I, ML/MINOS, subluminal, 95% CL):
- b^{-1} > 2.3×10^11 GeV (f = 4/3)
- b^{-1} > 2.8×10^11 GeV (f = 2)
- continuous time: 1.2–2.0×10^11 GeV

Caveat: LHAASO assumes an isotropic dispersion, so only the coefficient along the GRB direction is constrained. We quote the weakest orientation. The transverse group velocity is O(b^2k^2) and affects the path length only at second order.

### D.5 Crab synchrotron

The lattice electron has E^2 = p^2 + m^2 − (fb^2/3)p^4, which in Liberati-Maccione-Sotiriou (LMS) form is η = −1 and M_LV = b^{-1}(3/f)^{1/2}. With M_LV ≳ 2×10^16 GeV (LMS, 95% CL):
- b^{-1} ≳ 1.3×10^16 GeV (f = 4/3)
- b^{-1} ≳ 1.6×10^16 GeV (f = 2)
- continuous time: 0.7–1.2×10^16 GeV

Independent check of the LMS maximum-frequency formula (their eq. 7):

  ω_c^max = (3eB/2m)(1 − 4/(3n))^{3/2}[4(M/m)^{n−2}/(−η(n−1)(3n−4))]^{2/n},

with eB/m = 3.47×10^{-21} GeV for B = 300 μG. Requiring ω_c^max ≥ 0.1 GeV gives:
- n = 4: η ≳ −10^{4.88} at M_Pl, i.e. M_LV > 4.4×10^16 GeV for η = −1. This matches LMS's "η ≳ −10^5 ... M_LV > 3×10^16 GeV".
- n = 6: M_LV > 4.0×10^11 GeV. We use this in D.7.

Our own cross-estimate: the maximum electron Lorentz factor for the lattice relation is γ_max = [m b f^{1/2} · 3/√2]^{-1/2} at E_* = [m/(b(2f)^{1/2})]^{1/2}. Requiring γ^3/E to reach the Lorentz-invariant value for 1500 TeV electrons gives b^{-1} ≳ 2.6 f^{1/2} m_e γ_LI^2 ≈ 1.3–1.6×10^16 GeV. This is consistent.

### D.6 Auger GZK photons (conditional)

In Auger's convention, E^2 − p^2 = δ_γ,2 E^4. The lattice photon gives δ_γ,2 = −fb^2/12, so δ_γ,2 > −10^{-58} eV^{-2} = −10^{-40} GeV^{-2} implies b^{-1} > (f/12)^{1/2} × 10^20 GeV:
- f = 4/3: 3.3×10^19 GeV
- f = 2: 4.1×10^19 GeV

This holds only if protons are a subdominant component up to 10^20 eV (Auger's condition). With the proton-poor compositions favoured by Auger, the photon constraint disappears.

### D.7 How the bounds change for improved actions (answer to the brief's question)

| Discretization (free dispersion) | g−2 / α (Beane) | E_max ≈ 1/b (Beane "GZK") | TOF (n = 2) | γ decay | Crab synchrotron |
|---|---|---|---|---|---|
| Unimproved Wilson (Beane) | 3.6×10^7 value; 4×10^8 at 1σ | ~10^11 | ≳2×10^11 | ≳4×10^14 | ≳1×10^16 |
| O(b)-improved Wilson (clover), naive, staggered | removed at tree level (C_p + C_sw = O(α)), weakened by ~α | ~10^11 | same as Wilson | same | same |
| Tree-level O(b^2)-improved (e.g. Naik and Lüscher-Weisz), with residual O(αb^2) | removed | ~10^11 | weakened | model-dependent | ~10^15 if the residual coefficient ~α/π (scales as sqrt of the coefficient) |
| Nonperturbatively O(b^2)-improved, leading O(b^4k^6) | removed | ~10^11 (O(1) factor) | not applicable | ~10^11 if coefficients mismatch with the right sign | ≳4×10^11 × c^{1/4} (n = 6), i.e. ~10^11 |
| Chirally symmetric (domain wall, overlap) | C_p → 0 (Beane) | ~10^11 | dispersion not derived here | not derived | not derived |
| Anisotropic lattice (a_t ≠ a_s) | as its spatial action | ~10^11 | as above | as above | as above, plus a separate dimension-4 speed-of-light tuning per species (Lin et al.; Collins et al.) |
| Causal set (Poisson sprinkling) | none | no Brillouin zone | no modified dispersion (BHS theorem) | none | none. The observable is swerves (k < 10^{-61} GeV^3) |

Notes on the table:
- (i) The E_max argument depends only on the Brillouin zone |k_j| ≤ π/b. For the unimproved boson, E_max = (2/b)asinh(1) = 1.76/b along an axis and (2/b)asinh(√3) = 2.63/b at the corner. Improved operators change this only by O(1).
- (ii) Naik: (9/8)sin x − (1/24)sin 3x = x − (3/40)x^5 + …, so the per-component residual is −(3/40)b^4k_j^5 and the spatial dispersion error is −(3/20)b^4Σk_j^6.
- (iii) Fodor & Hoelbling note that tree-level improvement leaves O(g^2a^2). For QED this means O(α b^2) dimension-6 coefficients, which keep the Crab bound at b^{-1} ≳ 2×10^16 × (α/π)^{1/2} ≈ 10^15 GeV.
- All entries are order-of-magnitude. O(1) coefficients depend on the action.

**Bottom line for the brief.** For an O(b^2)-improved action, Beane et al.'s headline number (b^{-1} ~ 10^11 GeV from E_max) is essentially unchanged, because it comes from the Brillouin zone. The g−2/α bounds disappear. The cubic signature moves from O(b^2p^2) to O(b^4p^4). For unimproved and O(b)-improved actions, the dimension-6 LIV bounds, not the GZK argument, are now the strongest, by five or more orders of magnitude.

## E. Gaps, controversies, and embarrassment risks

1. **Our derivations contradict a statement of Beane et al.** (the γ → e+e− threshold) and supersede their headline bound for their own scenario. Both are "this work" and must be labelled as such. A lattice field theorist should check D.1 and D.3 before submission, in particular whether any lattice subtlety (e.g., the Wilson-term contribution at O(b^2), or the Minkowski continuation of eq. 17) changes the factor of 4 between the fermion and boson coefficients. We are fairly confident: the numerical check uses their exact equations.
2. **Anisotropic vs isotropic mapping.** All published n = 2 and n = 4 limits assume rotational invariance. Our mapping uses the weakest direction, which is conservative to O(1). A rigorous treatment would use direction-dependent SME coefficients. Vasileiou et al. (Table VI) and the Kostelecký-Russell tables contain such limits for d = 6 nonbirefringent photon coefficients. We did not attempt the SME normalisation mapping.
3. **The "GKZ ~6×10^20 eV" value** in Beane et al. is nonstandard (see A.2). If we paraphrase it, we must say what they wrote.
4. **The muon g−2 "bound" is a central value** from attributing a 2012 anomaly to the lattice. Calling it a "bound" would misrepresent the paper. It is also outdated because the g−2 theory situation has changed. We did not recompute it.
5. **LHAASO abstract vs Table I.** "E_QG,1 > 10 E_Pl" in the abstract corresponds to 1.0×10^20 GeV = 8.2 E_Pl in Table I (ML/MINOS, subluminal). The brief's wording copies the abstract. We quote the table value in GeV and note the abstract's rounding.
6. **Composition dependence.** UHECR-based n = 4 constraints (Maccione et al. 2009; Auger 2022 photons) assume protons. Liberati 2013 flags this. The Auger mapping (D.6) is kept conditional.
7. **The cubic-anisotropy search (README R1)** is strongly disfavoured for Beane's scenario as specified (spread ≲ 10^{-11}). It stays meaningful only for simulators with all-orders O(b^2)-improved dispersion and b^{-1} near 10^11 GeV, where the leading anisotropy is O((bp)^4) ~ 6% at most. This should inform how the paper frames R1. Section 04 should know.
8. **The Andersen (2012) claim** of exact Lorentz covariance on a lattice graph is unrefereed. The Bombelli-Henson-Sorkin theorem forbids a Lorentz-invariant finite-valency graph associated with a sprinkling, so Andersen's construction must evade it somehow (e.g., by not being a sprinkling). We have not checked this. The `.tex` reports it as a claim only.
9. **Non-locality as simulation cost.** It is our interpretation that the infinite valency of causal sets makes them expensive to simulate. The `.tex` flags this as interpretation.

## F. Unverifiable or partly verified items (kept out of the `.tex` or cited only at METADATA or ABSTRACT level)

- Beane et al.'s published EPJA version: the Springer page was blocked, so differences from arXiv v2 are unchecked.
- Bombelli, Lee, Meyer, Sorkin PRL 59 (1987) 521 is paywalled and cited at METADATA level. Content claims rely on Dowker et al., BHS 2009 and Surya 2019.
- Christ, Friedberg & Lee (1982) random lattice is cited only through Surya (secondary). Not added to the bib.
- Greisen (1966) and Zatsepin & Kuzmin (1966) are not cited. We use Liberati 2013 and Auger 2020 for the GZK scale.
- Symanzik (1983), Sheikholeslami-Wohlert (1985) and Lüscher-Weisz (1985) are not read. Improvement statements are sourced to Fodor & Hoelbling (RMP 2012).
- The LHAASO PRL 133 (2024) published text was not compared with arXiv v3 (Feb 2026). The abstract wording in the brief matches v3.
- Kostelecký & Mewes 2009 (nonminimal photon sector) was not read and is not cited.
- OpenAlex citation list: rate-limited.

## G. Suggested cross-links

- **Section 04 (UHECR observations):** GZK/suppression energies (Auger E_34), composition, the absence of a cubic-anisotropy search, magnetic deflections, and D.2's threshold-shift formula as input for any anisotropy estimator.
- **Holographic noise / Planck-scale interferometry section:** the Collins/Polchinski naturalness argument applies to any preferred-frame proposal.
- **Computational-cost section:** the E_max ~ 1/b scaling, the Vazza 2025 energy arguments, and causal-set non-locality (infinite valency) as a cost for a Lorentz-invariant simulator.
- **Philosophy / critiques section:** the dependence of every bound on simulator design (the D.7 table), and the underdetermination point that the same signatures arise in non-simulation discrete physics (Coleman-Glashow, SME).
