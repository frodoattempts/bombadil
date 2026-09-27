# Claim ledger: 03-lattice-liv

Topic: a discretized spacetime as a simulation signature. Covers the theory, lattice-artifact predictions, and
Lorentz-invariance-violation (LIV) bounds. Cosmic-ray observations are reviewed in section 04.

Conventions for this ledger:
- Quotes come from `pdftotext -layout` of the arXiv PDFs saved under `/tmp/claude-0/papers/`. Superscripts and
  subscripts that the PDF-to-text conversion flattened (e.g. "107 GeV" for 10^7 GeV) are restored in `^{}`/`_{}`
  notation, and nothing else is changed.
- Entries marked **THIS WORK** are derivations made for this review. Their inputs are FULLTEXT-verified, and each
  derivation is written out in `research/notes/03-lattice-liv-report.md` (section D). The `.tex` draft labels them
  "this work".
- Units are natural (hbar = c = 1). b is the lattice spacing, so b^{-1} is an energy.
- Retrieval date for all sources: 2026-09-27.

---

## A. Beane, Davoudi & Savage (2012 preprint; EPJA 2014): assumptions, bounds and prediction

### C-03-001
- Claim: Beane et al. study observable consequences of the hypothesis that the universe is a numerical simulation on a cubic space-time lattice. Their motivation is an extrapolation of the computational-resource trends of lattice QCD, and they assume an early simulation with unimproved Wilson fermions.
- Source: Beane2014constraints
- Locator: Abstract; Sec. I (p. 4-6)
- Evidence: "Observable consequences of the hypothesis that the observed universe is a numerical simulation performed on a cubic space-time lattice or grid are explored. The simulation scenario is first motivated by extrapolating current trends in computational resource requirements for lattice QCD into the future. [...] we assume that our universe is an early numerical simulation with unimproved Wilson fermion discretization"
- Verified: FULLTEXT
- Notes: arXiv:1210.1847v2 (9 Nov 2012) was read. The published EPJA version (paywalled; the Springer page could not be fetched) was not compared.

### C-03-002
- Claim: The extrapolation uses the computational resource requirement (CRR) of lattice-QCD ensemble generation, which scales roughly as λ_QCD L^5/b^6. It is fitted to the MILC asqtad (staggered) and SPECTRUM anisotropic clover-Wilson programs, and the authors list caveats: continuation of an effective Moore's law, a technological singularity, and human extinction.
- Source: Beane2014constraints
- Locator: Sec. I, p. 3-4, Fig. 1
- Evidence: "At fixed quark masses, the CRR of a lattice ensemble generation (in units of petaFLOP-years) scales roughly as the dimensionless number λ_QCD L^5/b^6 [...] There are, of course, many caveats to this extrapolation. Foremost among them is the assumption that an effective Moore's Law will continue into the future"
- Verified: FULLTEXT
- Notes: Fig. 1 marks the years at which lattices of 1 micron and 1 metre at b = 0.1 fm would be reached. The paper states these as extrapolations, not predictions.

### C-03-003
- Claim: Beane et al. assume a classical computer and restrict attention to one ingredient of present-day simulations: an underlying cubic lattice.
- Source: Beane2014constraints
- Locator: Sec. I, p. 2-3
- Evidence: "we take a pedestrian approach [...] by assuming that a classical computer (i.e. the classical limit of a quantum computer) is used to simulate the quantum universe [...] we focus on one aspect only: the possibility that the simulations of the future employ an underlying cubic lattice structure."
- Verified: FULLTEXT
- Notes: none

### C-03-004
- Claim: Beane et al. argue that the fine-tuning problem of Lorentz-violating dimension-four operators does not arise in the simulation scenario, because the space-time symmetries of the lattice action are preserved at the quantum level. Their footnote attributes this protection to the hypercubic symmetry of Euclidean lattices and notes that Hamiltonian lattice formulations are also possible.
- Source: Beane2014constraints
- Locator: Sec. I, p. 4 and footnote 3
- Evidence: "This is not an issue if one assumes the simulation scenario for the same reason that it is not an issue when one performs a lattice QCD calculation. The underlying space-time symmetries respected by the lattice action will necessarily be preserved at the quantum level." Footnote 3: "Current lattice QCD simulations are performed in Euclidean space, where the underlying hyper-cubic symmetry protects Lorentz invariance breaking in dimension four operators. However, Hamiltonian lattice formulations, which are currently too costly to be practical, are also possible."
- Verified: FULLTEXT
- Notes: Polchinski (C-03-049) disputes that Euclidean hypercubic protection carries over to a Lorentzian world. See also C-03-052 (anisotropic lattices require tuning).

### C-03-005
- Claim: Expanding the unimproved Wilson action in b produces an O(b) Pauli term (the Sheikholeslami-Wohlert operator) with tree-level coefficient C_p = 1 + O(α). Adding the Sheikholeslami-Wohlert term with C_sw = −C_p + O(α) removes it (O(b) improvement).
- Source: Beane2014constraints
- Locator: Sec. II, eqs. (1)-(3)
- Evidence: "L^(W) = ψ̄D̸ψ + m̃ψ̄ψ + C_p (gb/4) ψ̄σ_μν G^μν ψ + O(b^2) [...] The coefficient of the Pauli term ψ̄σ_μν G^μν ψ is fixed at tree level, C_p = 1 + O(α) [...] the lattice action can be O(b) improved by adding a term [...] with C_sw = −C_p + O(α). This is the so-called Sheikholeslami-Wohlert term."
- Verified: FULLTEXT
- Notes: none

### C-03-006
- Claim: The O(b) term shifts the fermion magnetic moment to g + 2mbC_p. The lattice-spacing contribution is therefore enhanced by one power of the particle mass.
- Source: Beane2014constraints
- Locator: Sec. III.1, eq. (5)
- Evidence: "μ = (Q̂e/2m)(g + 2mb C_p + ...) S = g(b) (Q̂e/2m) S [...] the lattice spacing contribution to the magnetic moment is enhanced relative to the Dirac contribution by one power of the particle mass."
- Verified: FULLTEXT
- Notes: none

### C-03-007
- Claim: From the muon g−2, Beane et al. obtain b^{-1} = (3.6 ± 1.1) × 10^7 GeV. This is not a null bound: it comes from attributing the then ~3.6σ experiment-theory difference entirely to a finite lattice spacing, and the authors call it an approximate upper bound on the lattice spacing.
- Source: Beane2014constraints
- Locator: Sec. III.1, eq. (10)
- Evidence: "Given that the standard model calculation of g^(µ)(0) is consistent with the experimental value, with a ∼ 3.6σ deviation [...] Attributing this difference to a finite lattice spacing, these values give rise to b^{-1} = (3.6 ± 1.1) × 10^7 GeV , which provides an approximate upper bound on the lattice spacing."
- Verified: FULLTEXT
- Notes: The inputs are 2012 CODATA-era values (their ref. [39]). The muon g−2 theory situation has changed since 2012, so the numerical "value" is of historical interest only. We have not recomputed it.

### C-03-008
- Claim: From the difference between the fine-structure constant extracted from the electron g−2 and from atomic recoil (^87Rb), Beane et al. find |δα| = (1.86 ± 5.51) × 10^{-12}, which gives b = |(−0.6 ± 1.7) × 10^{-9}| GeV^{-1} and, from the 1σ values, b^{-1} ≳ 4 × 10^8 GeV.
- Source: Beane2014constraints
- Locator: Sec. III.2, eqs. (11)-(13)
- Evidence: "This gives rise to a difference of |δα| = (1.86 ± 5.51) × 10^{-12} between two extractions, which translates into b = | (−0.6 ± 1.7) × 10^{-9} | GeV^{-1} . As this result is consistent with zero, the 1σ values of the lattice spacing give rise to a limit of b^{-1} ≳ 4 × 10^8 GeV"
- Verified: FULLTEXT
- Notes: This is a 1σ limit, not a 95% CL limit. It depends on an unknown O(1) coefficient C̃_p (naive dimensional analysis).

### C-03-009
- Claim: For chirally symmetric discretizations, C_p vanishes or is exponentially small, so the g−2 and α bounds become significantly weaker. The analysis covers QED only and is presented as an estimate.
- Source: Beane2014constraints
- Locator: Sec. III.2, last paragraph
- Evidence: "For more sophisticated simulations in which chiral symmetry is preserved by the lattice discretization, the coefficient C_p will vanish or will be exponentially small. As a result, the bound on the lattice spacing derived from the muon g − 2 and from the differences between determinations of α will be significantly weaker. [...] these constraints are to be considered estimates only"
- Verified: FULLTEXT
- Notes: none

### C-03-010
- Claim: At O(b^2), the Wilson action contains a hypercubic, rotation-breaking operator (tree-level coefficient C^RV = 1). Its hydrogen energy shifts are δE ~ C^RV α^4 m_e^3 b^2, about 10^{-26} eV for b^{-1} = 10^8 GeV, which is unobservable.
- Source: Beane2014constraints
- Locator: Sec. IV.3, eqs. (14)-(15)
- Evidence: "a lattice spacing of b^{-1} = 10^8 GeV gives an energy shift of order δE ∼ 10^{-26} eV [...] This magnitude of energy shifts and splittings is presently unobservable."
- Verified: FULLTEXT
- Notes: none

### C-03-011
- Claim: Beane et al. give the free lattice dispersion relations for bosons (eq. 16) and Wilson fermions (eq. 17) in Minkowski space, with the time direction also discretized. These relations have only cubic, not full rotational, symmetry, and rotational invariance is recovered only for momenta small compared with 1/b.
- Source: Beane2014constraints
- Locator: Sec. IV.4, eqs. (16)-(17), Fig. 2
- Evidence: "sinh^2(bE_b/2) − Σ_{j} sin^2(bk_j/2) − (bm_b/2)^2 = 0 [...] sinh^2(bE_f) − Σ_{j} sin^2(bk_j) − [bm_f + 2r(Σ_{j} sin^2(bk_j/2) − sinh^2(bE_f/2))]^2 = 0 [...] The violation of Lorentz invariance resulting from these dispersion relations is due to the fact that they have only cubic symmetry and not full rotational symmetry"
- Verified: FULLTEXT
- Notes: Eq. (17) also gives E_f = sqrt(k^2+m^2) − r b m^3/(2 sqrt(k^2+m^2)) + O(b^2). That O(b) term vanishes as m → 0 and is negligible at high energy.

### C-03-012
- Claim: Beane et al. assume that all particles, including composite ones such as the proton and pion, obey dispersion relations of the form of eqs. (16)-(17).
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 10-11
- Evidence: "for composite particles, such as the proton or pion, the dispersion relations will be dynamically generated. In the present analysis we assume that the dispersion relations for all particles take the form of those in eq. (16) and eq. (17)."
- Verified: FULLTEXT
- Notes: none

### C-03-013
- Claim: Beane et al. argue that the Coleman-Glashow bounds on differences in maximal attainable velocity do not apply directly, because on the lattice each particle's speed depends on its momentum.
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 10
- Evidence: "As the speed of light for each particle in the discretized space-time depends on its three-momentum, the constraints obtained by Coleman and Glashow [25] do not directly apply to processes occurring in a lattice simulation."
- Verified: FULLTEXT
- Notes: Correct for the dimension-4 (momentum-independent) Coleman-Glashow framework. The momentum-dependent (n = 4, dimension-6) LIV framework does apply; see C-03-020 to C-03-024 (this work).

### C-03-014
- Claim: Beane et al. report numerically that vacuum p → p + γ is kinematically forbidden for all proton momenta with their dispersion relations. They state that γ → e+e− can proceed only for photons with energies comparable to 1/b near the Brillouin-zone edge, and that high-energy π0 are stable against π0 → γγ.
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 11
- Evidence: "Numerically, we find that there are no final states that satisfy this condition, and therefore this process is forbidden for all proton momentum. In contrast, the process γ → e+e−, which provides tight constraints on differences between MAV's [25], can proceed for very high energy photons (those with energies comparable to the inverse lattice spacing) near the edges of the Brillouin zone. Further, very high energy π0's are stable against π0 → γγ"
- Verified: FULLTEXT
- Notes: Our kinematic check of their own eqs. (16)-(17) disagrees on γ → e+e− (C-03-021, THIS WORK).

### C-03-015
- Claim: If the lattice rest frame coincides with the CMB frame, the Δ-resonance threshold for photopion production acquires a direction-dependent correction proportional to (√π b^2|p|^2/9)[Y_4^0 + sqrt(5/14)(Y_4^4 + Y_4^{-4})](θ, φ), valid for |p| ≪ 1/b.
- Source: Beane2014constraints
- Locator: Sec. IV.4, eq. (18)
- Evidence: "When the lattice rest frame coincides with the CMB rest frame, head-on interactions between a high energy proton with momentum |p| and a photon of (very-low) energy ω can proceed through the ∆ resonance when ω = ((m_∆^2 − m_N^2)/(4|p|)) [1 + (√π b^2|p|^2/9)(Y_4^0(θ,φ) + sqrt(5/14)(Y_4^{+4}(θ,φ) + Y_4^{−4}(θ,φ)))] − ((m_∆^3 − m_N^3)/(4|p|)) b r + ... , for |p| ≪ 1/b"
- Verified: FULLTEXT
- Notes: Eq. (18) is the only quantitative, direction-dependent formula for cosmic rays in the paper. C-03-018 recasts it (THIS WORK).

### C-03-016
- Claim: The lattice imposes a maximum energy E_max ~ 1/b. Equating this to the "GKZ" cut-off, which the paper quotes as ~6 × 10^{20} eV, gives b ~ 10^{-12} fm, i.e. b^{-1} ~ 10^{11} GeV. The paper presents this as the most stringent bound it finds.
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 11-12; Abstract; Sec. V
- Evidence: "Processes such as γ_CMB + N → ∆ give rise to the predicted GKZ-cut off scale [50, 51] of ∼ 6×10^{20} eV [...] For both the fermions and the bosons, the cut off from the dispersion relation is E_max ∼ 1/b. Equating this to the GKZ cut off corresponds to a lattice spacing of b ∼ 10^{-12} fm, or a mass scale of b^{-1} ∼ 10^{11} GeV."
- Verified: FULLTEXT
- Notes: The paper spells it "GKZ". Its value of ~6 × 10^{20} eV is an order of magnitude above the conventional threshold (Liberati2013tests quotes E_th ≃ 5 × 10^{19} eV, C-03-042) and above the Auger suppression energy (C-03-043). The bound is an order-of-magnitude statement ("∼") with no confidence level.

### C-03-017
- Claim: Beane et al.'s signature is that, if the lattice supplies the cut-off, the angular distribution of the highest-energy cosmic rays would show cubic symmetry in the lattice rest frame. For smaller lattice spacings the effect would be less significant and hidden by the GZK mechanism, and a non-cubic lattice would imprint its own symmetry.
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 11-12; Abstract
- Evidence: "The most striking feature of the scenario in which the lattice provides the cut off to the cosmic ray spectrum is that the angular distribution of the highest energy components would exhibit cubic symmetry in the rest frame of the lattice, deviating significantly from isotropy. For smaller lattice spacings, the cubic distribution would be less significant, and the GKZ mechanism would increasingly dominate the high energy structure."
- Verified: FULLTEXT
- Notes: Having read the whole paper, we find no amplitude for the arrival-direction anisotropy apart from eq. (18). The paper does not treat magnetic deflection, source distribution or the motion of Earth relative to the lattice frame.

### C-03-018
- Claim: **THIS WORK.** Eq. (18) of Beane et al. can be rewritten as a fractional threshold shift of (5/12)(Σ_j n_j^4 − 3/5)(b|p|)^2, where n is the unit momentum direction in the lattice frame. This equals +(b|p|)^2/6 along a lattice axis and −(b|p|)^2/9 along a body diagonal, a total spread of (5/18)(b|p|)^2.
- Source: Beane2014constraints
- Locator: eq. (18); derivation in report §D.2
- Evidence: (see C-03-015 for the input formula)
- Verified: FULLTEXT
- Notes: Uses the identity Y_4^0 + sqrt(5/14)(Y_4^4 + Y_4^{-4}) = (15/(4√π))(Σ_j n_j^4 − 3/5), checked numerically at random directions (report §D.2). At |p| = 5 × 10^{10} GeV the spread is ~7% for b^{-1} = 10^{11} GeV and ~7 × 10^{-12} for b^{-1} = 10^{16} GeV.

### C-03-019
- Claim: Beane et al. conclude that improvement "masks" much of the ability to test the scenario. Apart from the modified dispersion relation and the associated maximum energy and momentum, even O(b^2) Symanzik operators avoid obvious probes. They also judge it unlikely that any but the earliest simulations would be unimproved.
- Source: Beane2014constraints
- Locator: Sec. V
- Evidence: "Given the ease with which current lattice QCD simulations incorporate improvement or employ discretizations that preserve chiral symmetry, it seems unlikely that any but the very earliest universe simulations would be unimproved with respect to the lattice spacing. Of course, improvement in this context masks much of our ability to probe the possibility that our universe is a simulation, and we have seen that, with the exception of the modifications to the dispersion relation and the associated maximum values of energy and momentum, even O(b^2) operators in the Symanzik action easily avoid obvious experimental probes."
- Verified: FULLTEXT
- Notes: none

## B. Mapping the lattice dispersion onto LIV constraints (THIS WORK)

### C-03-020
- Claim: **THIS WORK.** Expanding eqs. (16)-(17) of Beane et al. for |k| ≪ 1/b gives, for massless bosons, E^2 = k^2 − (b^2/12)(k^4 + Σ_j k_j^4), and for Wilson fermions, E^2 = k^2 + m^2 − (b^2/3)(k^4 + Σ_j k_j^4), up to mass-suppressed terms. Both are subluminal, even in k, and have a direction factor f = 1 + Σ_j n_j^4 between 4/3 (body diagonal) and 2 (axis). Beane's eq. (16) has one boson branch, so the photon is not birefringent.
- Source: Beane2014constraints
- Locator: eqs. (16)-(17); derivation in report §D.1
- Evidence: (see C-03-011)
- Verified: FULLTEXT
- Notes: The coefficients were checked numerically against the exact eqs. (16)-(17) along the (100), (110) and (111) directions (report §D.1). With continuous time (a Hamiltonian lattice), f is replaced by Σ_j n_j^4 ∈ [1/3, 1]. The same b^2/3 fermion coefficient holds for naive, staggered and O(b)-(clover-)improved Wilson fermions, since the clover term does not change the free dispersion. That point is our inference and is not stated by Beane et al.

### C-03-021
- Claim: **THIS WORK.** With the same two dispersion relations, the electron is four times more subluminal than the photon at equal momentum. Photon decay γ → e+e− is therefore kinematically allowed above k_th ≈ (64/f)^{1/4} (m_e/b)^{1/2} ≈ 2.4-2.6 (m_e/b)^{1/2}, far below 1/b. This disagrees with Beane et al.'s statement (C-03-014).
- Source: Beane2014constraints
- Locator: eqs. (16)-(17); derivation and numerical check in report §D.3
- Evidence: (see C-03-011, C-03-014)
- Verified: FULLTEXT
- Notes: A numerical minimization over two-body final states with the exact lattice relations (b = 1, m = 10^{-4}) confirms that the threshold lies between k = 0.02 and 0.03, compared with an analytic 0.024-0.026. The check is kinematic only. We did not compute the decay rate on the lattice. See C-03-037 for rates in the EFT literature.

### C-03-022
- Claim: **THIS WORK.** Matching the lattice photon dispersion to the LHAASO quadratic parametrization gives E_QG,2 = b^{-1}(12/f)^{1/2} ∈ [2.45, 3.0] b^{-1}. LHAASO's subluminal 95% CL limit E_QG,2 > 6.9 × 10^{11} GeV then implies b^{-1} ≳ 2.3 × 10^{11} GeV for any orientation, or ≳ 1.2 × 10^{11} GeV for a continuous-time lattice.
- Source: LHAASO2024stringent; Beane2014constraints
- Locator: LHAASO eqs. (1)-(2), Table I; derivation in report §D.4
- Evidence: (see C-03-032)
- Verified: FULLTEXT
- Notes: Photons from a single GRB probe one direction. The weakest-direction value is quoted. This is comparable to Beane et al.'s GZK estimate but comes from an independent observable with a stated CL.

### C-03-023
- Claim: **THIS WORK.** The lattice electron has an n = 4 (dimension-6) subluminal dispersion, η p^4/M_LV^2 with η = −1 and M_LV = b^{-1}(3/f)^{1/2}. The Crab-synchrotron constraint M_LV ≳ 2 × 10^{16} GeV (95% CL) then implies b^{-1} ≳ 1.3 × 10^{16} GeV for Beane et al.'s scenario (≳ 7 × 10^{15} GeV for continuous time).
- Source: Liberati2012scale; Beane2014constraints
- Locator: Liberati2012scale eqs. (3)-(7) and conclusions; derivation in report §D.5
- Evidence: (see C-03-040)
- Verified: FULLTEXT
- Notes: Liberati et al. assume a rotationally invariant electron dispersion. The lattice coefficient varies by at most a factor of 1.5 with direction, and the weakest direction is used. Liberati et al. neglect photon LIV at 0.1 GeV, and the same holds for the lattice photon. We also reproduced their simple maximum-frequency estimate (eq. 7) and got M_LV > 4.4 × 10^{16} GeV for η = −1 and B = 300 μG, consistent with their "η ≳ −10^5 ... M_LV > 3 × 10^{16} GeV" (report §D.5).

### C-03-024
- Claim: **THIS WORK.** Requiring photons up to the LHAASO 95% CL lower limit on the cutoff energy (E_cut > 1140 TeV for LHAASO J2032+4102) not to decay gives b^{-1} ≳ k^2 f^{1/2}/(8 m_e) ≈ 4 × 10^{14} GeV (≈ 2 × 10^{14} GeV for continuous time). This assumes that decay above threshold is fast, as argued in the EFT literature (C-03-037).
- Source: LHAASO2022exploring; Jacobson2006lorentz; Beane2014constraints
- Locator: LHAASO2022 Sec. IV; JLM 2006 Sec. 2 and 4.3.1; derivation in report §D.3
- Evidence: (see C-03-033, C-03-037)
- Verified: FULLTEXT
- Notes: LHAASO derived E_cut for a superluminal-photon model. We use E_cut only as the empirical statement that the spectrum shows no hard cutoff below 1140 TeV at 95% CL, which is model-independent.

### C-03-025
- Claim: **THIS WORK.** Auger's GZK-photon limit δ_γ,2 > −10^{-58} eV^{-2}, valid only if protons are a subdominant component up to 10^{20} eV, maps onto the lattice photon (δ_γ,2 = −f b^2/12) as b^{-1} ≳ 3 × 10^{19} GeV. The result is conditional on UHECR composition.
- Source: PierreAuger2022testing; Beane2014constraints
- Locator: Auger abstract, eq. (2.2); derivation in report §D.6
- Evidence: (see C-03-041)
- Verified: FULLTEXT
- Notes: The strongest mapping, but also the most model-dependent (it needs a proton fraction). Report it with that caveat.

### C-03-026
- Claim: **THIS WORK.** For an action that is O(b^2)-improved at tree level in both the fermion and gauge sectors: (i) the E_max ~ 1/b (GZK) argument changes only by O(1) factors, because the Brillouin zone is still |k_j| ≤ π/b; (ii) the g−2 and α bounds disappear once the Pauli term is removed; (iii) the leading dispersion anisotropy becomes O(b^4 k^4), so the LHAASO n = 2 time-of-flight bound no longer applies; (iv) the synchrotron maximum-frequency argument for an n = 6 electron dispersion gives only M_LV ≳ 4 × 10^{11} GeV, i.e. b^{-1} ≳ 10^{11} GeV up to O(1) coefficients.
- Source: Beane2014constraints; Liberati2012scale; Fodor2012light
- Locator: derivation in report §D.7
- Evidence: Liberati2012scale eq. (7) gives ω_c^max for arbitrary n > 2. Fodor2012light (Sec. II.E) describes tree-level Lüscher-Weisz and Naik improvement.
- Verified: FULLTEXT
- Notes: If improvement is only at tree level, O(g^2 b^2) terms survive (C-03-030). Residual dimension-6 coefficients of order α/π ≈ 2 × 10^{-3} would still give b^{-1} ≳ 10^{15} GeV from the Crab bound, which scales as (coefficient)^{1/2}. Evading the n = 4 bounds therefore requires improvement to all orders or nonperturbatively. This is an order-of-magnitude estimate.

## C. Lattice discretizations and their artifacts

### C-03-027
- Claim: By the Nielsen-Ninomiya theorem, no lattice fermion discretization simultaneously has no doublers, continuum chiral symmetry in the massless case, locality, and the correct continuum limit.
- Source: Fodor2012light
- Locator: Sec. II.E.1 (p. 9-10)
- Evidence: "It was later shown by (Nielsen and Ninomiya, 1981a,b,c), that no lattice fermion regularization exists that fulfills all of the following conditions at the same time i Absence of doubler fermions ii Continuum chiral symmetry in the massless case iii Locality [...] iv Correct continuum limit"
- Verified: FULLTEXT
- Notes: none

### C-03-028
- Claim: Wilson fermions start with O(a) discretization effects. Staggered, twisted-mass fermions at maximal twist, and exactly chiral (Ginsparg-Wilson) fermions show O(a^2) scaling, and improved staggered fermions such as asqtad scale as O(g^2 a^2).
- Source: Fodor2012light
- Locator: Sec. III.B (continuum extrapolation), p. 29 of arXiv version
- Evidence: "Formally, staggered fermions and twisted mass fermions at maximal twist as well as exactly chiral fermions show O(a^2) continuum scaling while Wilson type fermions generically start with O(a) scaling. Only improved staggered fermions such as asqtad have a leading scaling behavior of O(g^2 a^2)."
- Verified: FULLTEXT
- Notes: none

### C-03-029
- Claim: The O(a^2) effects of staggered fermions can be removed classically by replacing the one-hop derivative with a combination of one-hop and three-hop terms (Naik).
- Source: Fodor2012light
- Locator: Sec. II.E, fermion improvement
- Evidence: "In contrast to Wilson fermions the staggered action has leading discretization effects of O(a^2). These can be eliminated on a classical level by replacing the one-hop derivative of the staggered action (57) with a suitable combination of one-hop and three-hop derivative operators such that O(a^2) terms cancel (Naik, 1989)."
- Verified: FULLTEXT
- Notes: none

### C-03-030
- Claim: The Wilson plaquette gauge action has O(a^2) errors. Tree-level Lüscher-Weisz improvement (c_0 = 5/3, c_1 = −1/12) removes them classically, but radiative corrections reintroduce O(g^2 a^2) terms.
- Source: Fodor2012light
- Locator: Sec. II.E.1 (gauge field improvement)
- Evidence: "The simple Wilson gauge action (20) only contains the elementary plaquette and has discretization errors of O(a^2). [...] which leads to a choice of coefficients c_0 = 5/3 and c_1 = −1/12. The resulting action is known as tree level Lüscher-Weisz action. [...] Generically, these corrections are proportional to g^2 such that the tree level Lüscher-Weisz action is correct up to O(g^2 a^2) terms as opposed to O(a^4) in the classical theory."
- Verified: FULLTEXT
- Notes: none

### C-03-031
- Claim: On a hypercubic lattice the action is constrained by hypercubic symmetry. Davoudi and Savage show that, with suitably smeared operators, rotation-violating contributions enter at tree level with coefficients suppressed by O(a^2), and quantum loops do not change this in λφ^4, nor in QCD if the gauge fields are smeared over a comparable region.
- Source: Davoudi2012restoration
- Locator: Abstract; Sec. I
- Evidence: "Contributions from these operators that violate rotational invariance occur at tree-level, with coefficients that are suppressed by O(a^2) in the continuum limit. Quantum loops do not modify this behavior in λφ^4, nor in QCD if the gauge-fields are smeared over a comparable spatial region." Sec. I: "While the action lacks Lorentz invariance and rotational symmetry, it is constrained by hyper-cubic symmetry."
- Verified: FULLTEXT
- Notes: This is a Euclidean lattice-QCD result about operators (matrix elements), not about a real-time Lorentzian universe.

### C-03-032
- Claim: On anisotropic lattices (a_s/a_t = 3.5 in the Hadron Spectrum Collaboration's N_f = 2+1 program), the gauge and fermion anisotropy parameters must be tuned (γ*_g = 4.3, γ*_f = 3.4) to restore Lorentz symmetry in low-energy observables. The "speed of light" is measured from the dispersion of boosted hadrons.
- Source: Lin2009first
- Locator: Sec. I-II, eq. (4); Sec. III (meson dispersion, Fig. 9)
- Evidence: "Simulations were performed on anisotropic lattices with the ratio of spatial and temporal scales fixed non-perturbatively to a_s/a_t = 3.5." (Sec. VI) "In a previous study, we tuned a three-flavor lattice action to ensure Lorentz symmetry is restored in appropriately chosen low-energy observables." "Tuning the anisotropy for all quark masses (even below the chiral limit) gives the desired γ_{g,f}^*: γ_g^* = 4.3, γ_f^* = 3.4." "The speed of light c is measured from the energy of the boosted hadron"
- Verified: FULLTEXT
- Notes: This is the lattice analogue of the dimension-4 speed-of-light tuning discussed by Collins et al. (C-03-047). The SPECTRUM ensembles are among those Beane et al. extrapolate from (C-03-002).

### C-03-033
- Claim: Gantumur (2025; JHEP 2026) proposes a Euclidean lattice regulator on a hypercubic graph whose embedding is dynamical. The partition function is exactly covariant under the global Euclidean group SE(d) at any lattice spacing, and d = 2 simulations show reduced axis-versus-diagonal artefacts.
- Source: Gantumur2026rotationally
- Locator: Abstract
- Evidence: "the partition function is exactly covariant under the global special Euclidean group SE(d) at any lattice spacing [...] evidence for reduced axis-vs-diagonal cutoff artefacts relative to a fixed lattice at matched bare parameters."
- Verified: ABSTRACT
- Notes: The result is Euclidean and conditioned on a "short-range geometry hypothesis". It is not a Lorentzian construction.

### C-03-034
- Claim: Andersen (2012, unrefereed preprint) responds to Beane et al. with a lattice-graph construction that, he claims, keeps exact Lorentz covariance in lattice gauge simulations. He concludes that a "digital universe" need not violate Lorentz symmetry.
- Source: Andersen2012lorentz
- Locator: Abstract; p. 1-2
- Evidence: "I demonstrate a technique for accomplishing lattice gauge theory simulations while maintaining exact Lorentz covariance by replacing the lattice with a lattice graph [...] This technique eliminates the symmetry violation of standard lattice gauge theory and suggests that, even in a digital universe, Lorentz covariance can still hold."
- Verified: FULLTEXT
- Notes: arXiv only (math-ph), INSPIRE citation count 0. We have not assessed its technical validity, so the `.tex` presents it as a claim.

## D. The LIV framework

### C-03-035
- Claim: Colladay and Kostelecký built a framework for low-energy effects of spontaneous CPT and Lorentz violation (1997) and then a general Lorentz-violating extension of the SU(3)×SU(2)×U(1) Standard Model (1998). The extension includes CPT-even and CPT-odd terms, keeps observer covariance and breaks particle Lorentz covariance.
- Source: Colladay1997cpt; Colladay1998lorentz
- Locator: Abstracts
- Evidence: 1998: "we present a general Lorentz-violating extension of the minimal SU(3) × SU(2)× U(1) standard model including CPT-even and CPT-odd terms [...] The extension has gauge invariance, energy-momentum conservation, and covariance under observer rotations and boosts, while covariance under particle rotations and boosts is broken."
- Verified: ABSTRACT
- Notes: none

### C-03-036
- Claim: The Kostelecký-Russell Data Tables for Lorentz and CPT Violation are updated annually. The January 2026 edition (arXiv v19) compiles 52 data tables of measured and derived SME coefficients, with literature up to December 31, 2025.
- Source: Kostelecky2011data
- Locator: title page; Sec. I
- Evidence: "January 2026 update of Reviews of Modern Physics 83, 11 (2011) [arXiv:0801.0287] [...] We compile 52 data tables for these SME coefficients [...] The tables include results available from the literature up to December 31, 2025."
- Verified: FULLTEXT
- Notes: Cite the version (v19) explicitly, because the living document changes.

### C-03-037
- Claim: In the EFT framework, once photon decay is kinematically allowed, the photon lifetime is extremely short (≪ 1 s), far shorter than the ~10^{11} s travel time of Crab photons. Threshold constraints are therefore insensitive to the details of the matrix element.
- Source: Jacobson2006lorentz
- Locator: Sec. 2 (p. 8-9); Sec. 4.3.1
- Evidence: "Once the reaction is kinematically allowed, the photon lifetime is extremely short (≪ 1 sec) when calculated with standard QED plus modified dispersion, much shorter for example than the required lifetime of 10^{11} seconds for high energy photons that reach us from the Crab nebula. Thus we could tolerate huge modifications to the matrix element (the dynamics) and still have a photon decay rate incompatible with observation."
- Verified: FULLTEXT
- Notes: Liberati2013tests (Sec. 6.2.4) gives decay times of order (10 ns)^{-1} for n = 3 and (10^{-6} ns)^{-1} for n = 4 above threshold.

### C-03-038
- Claim: The dimension-5 LV operators of QED in the EFT framework (which give n = 3 photon dispersion and vacuum birefringence) all violate CPT, so a CPT-preserving theory forbids them. If LV at dimension n > 4 is suppressed by 1/M^{n−2}, it feeds down to lower-dimension operators unless a symmetry protects them.
- Source: Jacobson2006lorentz
- Locator: Sec. 3.1 and 3.4
- Evidence: "All of the terms (6) violate CPT symmetry as well as Lorentz invariance. Thus if CPT were preserved, these LV operators would be forbidden." "if LV operators of dimension n > 4 are suppressed as we have imagined by 1/M^{n−2}, LV would feed down to the lower dimension operators and be strong at low energies [...] unless there is a symmetry or some other mechanism that protects the lower dimension operators from strong LV."
- Verified: FULLTEXT
- Notes: Our inference, not stated in the source: the lattice dispersion (C-03-020) is even in k, and eq. (16) has one photon branch. The Beane lattice therefore gives no n = 3 birefringence, so birefringence limits (C-03-039) do not constrain it at leading order.

### C-03-039
- Claim: A commonly used modified dispersion relation is E^2 = p^2 + m^2 + f^{(n)} p^n/E_Pl^{n−2}. For n > 2 and f^{(n)} < 0 there is a stability problem near the Planck energy, which is usually assumed to be cured by a UV completion.
- Source: Mattingly2005modern
- Locator: Sec. 2-3 (p. 13)
- Evidence: "For the models in section 3.1 with higher order dispersion relations (E^2 = p^2 + m^2 + f^{(n)} p^n/E_Pl^{n−2} with n > 2) there is a stability problem for particles with momentum near the Planck energy if f^{(n)} < 0 [...] it is usually assumed that these modified dispersion relations are only effective"
- Verified: FULLTEXT
- Notes: The lattice relations are periodic (bounded) in k and supply their own UV completion.

## E. Observational constraints (numbers)

### C-03-040
- Claim: Liberati, Maccione and Sotiriou recompute the Crab Nebula broadband spectrum with n = 4 matter dispersion E^2 = m^2 + p^2 + η p^4/M_LV^2 and exclude M_LV ≲ 2 × 10^{16} GeV at 95% CL. A simpler maximum-synchrotron-frequency argument gives η ≳ −10^5 for M_LV = M_Pl and B ~ 300 μG, equivalent to M_LV > 3 × 10^{16} GeV.
- Source: Liberati2012scale
- Locator: eqs. (3)-(7); "Constraints" paragraph; Fig. 2
- Evidence: "We can run the same argument here for n = 4 and straightforwardly derive a constraint η ≳ −10^5 (assuming B ∼ 300 µG and M_LV = M_Pl), which would correspond to M_LV > 3 × 10^{16} GeV. [...] Mass scales M_LV ≲ 2 × 10^{16} GeV are excluded at 95% CL."
- Verified: FULLTEXT
- Notes: Assumes CPT and P invariance in the matter sector and equal electron and positron dispersion. Both assumptions hold for a hypercubic lattice, since it is P- and C-symmetric (our inference).

### C-03-041
- Claim: Using Auger data, Auger obtains δ_γ,0 > −10^{-21}, δ_γ,1 > −10^{-40} eV^{-1} and δ_γ,2 > −10^{-58} eV^{-2} for subluminal photons, only if there is a subdominant proton component up to 10^{20} eV. For the hadronic sector (positive coefficients only), it obtains δ_had,0 < 10^{-19}, δ_had,1 < 10^{-38} eV^{-1} and δ_had,2 < 10^{-57} eV^{-2} at 5σ CL. The convention is E_i^2 − p_i^2 = m_i^2 + Σ_n δ_{i,n} E_i^{2+n}.
- Source: PierreAuger2022testing
- Locator: Abstract; eq. (2.2); Sec. 5-6
- Evidence: "For the electromagnetic sector, while no constraints can be obtained in the absence of protons beyond 10^{19} eV, we obtain δ_γ,0 > −10^{-21}, δ_γ,1 > −10^{-40} eV^{-1} and δ_γ,2 > −10^{-58} eV^{-2} in the case of a subdominant proton component up to 10^{20} eV. For the hadronic sector [...] δ_had,0 < 10^{-19}, δ_had,1 < 10^{-38} eV^{-1} and δ_had,2 < 10^{-57} eV^{-2} at 5σ CL."
- Verified: FULLTEXT
- Notes: The hadronic bounds cover only δ_had > 0 ("We consider only positive LIV coefficients"), whereas the lattice gives negative (subluminal) coefficients, so they do not apply. The CL of the photon limits is not stated as a sigma level in the abstract.

### C-03-042
- Claim: With Lorentz invariance, photopion production on the CMB has threshold E_th ≃ 5 × 10^{19} (ω_0/1.3 meV)^{-1} eV. Liberati notes that UHECR-based n = 4 constraints depend on the proton-dominance assumption, which the composition data had made uncertain.
- Source: Liberati2013tests
- Locator: Sec. 7.3.1, 7.5
- Evidence: "When Lorentz invariance holds, this process has a threshold energy E_th ≃ 5 × 10^{19} (ω_0/1.3 meV)^{-1} eV" "It is hence quite unfortunate that these constraints are still suffering from experimental uncertainties about the composition of the UHECR and hence the nature of the steep fall-off in the spectrum observed above 10^{19} eV."
- Verified: FULLTEXT
- Notes: none

### C-03-043
- Claim: Auger measures a flux suppression above E_34 = (46 ± 3 ± 6) × 10^{18} eV, with spectral index γ_4 = 5.1 ± 0.3 ± 0.1 above it.
- Source: PierreAuger2020features
- Locator: p. 6 (spectral fit)
- Evidence: "Finally, the spectrum softens further above a suppression energy of E_34 = (46 ± 3 ± 6)×10^{18} eV with γ_4 = 5.1 ± 0.3 ± 0.1"
- Verified: FULLTEXT
- Notes: Errors are statistical and systematic. Section 04 discusses observations in detail. Cite here only to fix the energy scale.

### C-03-044
- Claim: Fermi observed GRB 090510 and obtained lower limits on the linear LIV scale M_QG,1/M_Pl from > 1.19 (most conservative, time-of-flight with limit (a)) to > 102 (least conservative, spike association). A dispersion analysis gives |Δt/ΔE| < 30 ms/GeV at 99% confidence, i.e. M_QG,1/M_Pl > 1.22. Models with n > 1 are not significantly constrained.
- Source: Abdo2009limit
- Locator: Table 2; text p. 12-16
- Evidence: Table 2: "(a) [...] > 1.19 [...] (e) [...] > 102 [...] (g) |Δt/ΔE| < 30 ms/GeV lag analysis of > 1 GeV spikes ±1 > 1.22" and "we find an upper limit for a linear dispersion of photons above 100 MeV of |Δt/ΔE| < 30 ms/GeV (at 99% confidence" "(models with n > 1 are not significantly constrained by our results)"
- Verified: FULLTEXT
- Notes: The arXiv title ("Testing Einstein's special relativity with Fermi's short hard γ-ray burst GRB090510") differs from the published Nature title. The limits use the 1σ lower limits on redshift (z = 0.900) and photon energy (28.0 GeV).

### C-03-045
- Claim: Vasileiou et al. analyse four Fermi-LAT GRBs and obtain, from GRB 090510 at 95% CL, E_QG,1 > 7.6 E_Pl and E_QG,2 > 1.3 × 10^{11} GeV (subluminal, without source-intrinsic dispersion). With maximally conservative treatment of intrinsic effects the limits are 1.8 E_Pl and 4.0 × 10^{10} GeV. They also give direction-dependent limits on SME d = 6 coefficients.
- Source: Vasileiou2013constraints
- Locator: Abstract; Tables V-VI
- Evidence: "our most stringent limits (at 95% CL) are obtained from GRB 090510 and are E_QG,1 > 7.6 times the Planck energy (E_Pl) and E_QG,2 > 1.3×10^{11} GeV for linear and quadratic leading order LIV-induced vacuum dispersion" Table V (090510, s± = +1): "1.8" (n = 1, E_Pl) and "4.0" (n = 2, 10^{10} GeV).
- Verified: FULLTEXT
- Notes: Table VI gives, for example, −0.31 to 0.16 (×10^{-20} GeV^{-2}) for Σ_jm Y_jm(117°, 334°) c^(6)_(I)jm from GRB 090510. These are direction-dependent limits, the kind of limit a lattice-anisotropy search would need.

### C-03-046
- Claim: From the TeV afterglow of GRB 221009A, LHAASO obtains 95% CL lower limits on the photon LIV scale of E_QG,1 > 1.0 × 10^{20} GeV (subluminal) and E_QG,2 > 6.9 × 10^{11} GeV (subluminal). The abstract summarizes these as E_QG,1 > 10 E_Pl and E_QG,2 > 6 × 10^{-8} E_Pl, with E_Pl = 1.22 × 10^{19} GeV. The parametrization is E^2 ≃ p^2[1 − Σ_n s(E/E_QG,n)^n], with group velocity v ≈ 1 − s((n+1)/2)(E/E_QG,n)^n.
- Source: LHAASO2024stringent
- Locator: Abstract; eqs. (1)-(2); Table I; Sec. IV
- Evidence: "the 95% confidence level lower limits on the QG energy scales are E_QG,1 > 10 times of the Planck energy E_Pl for the linear, and E_QG,2 > 6 × 10^{-8} E_Pl for the quadratic LIV effects" "Our limit on the linear modification of the photon dispersion relation is E_QG,1 > 1.0 × 10^{20} GeV (E_QG,1 > 1.1 × 10^{20} GeV), considering a subluminal (superluminal) LIV effect. [...] In the quadratic case, our result on the energy scale E_QG,2 > 6.9 × 10^{11} GeV (E_QG,2 > 7.0 × 10^{11} GeV) for a subluminal (su[perluminal])"
- Verified: FULLTEXT
- Notes: arXiv v3 (13 Feb 2026) was read. 1.0 × 10^{20} GeV is 8.2 E_Pl, so the abstract's "10 times" is a rounding. The calibrated-ML column of Table I gives 1.1 × 10^{20} GeV (9.0 E_Pl) subluminal. In the text we quote Table I values in GeV. The PRL abstract has the same wording (prompt and INSPIRE).

### C-03-047
- Claim: LHAASO finds no cutoff in the spectra of its two highest-energy sources and sets 95% CL lower limits on a LIV-induced cutoff of 750 TeV (Crab, LHAASO J0534+2202) and 1140 TeV (LHAASO J2032+4102). In a superluminal-photon model these correspond to a first-order LIV scale of about 1.42 × 10^{33} eV and a second-order scale above 10^{-3} M_Pl.
- Source: LHAASO2022exploring
- Locator: Abstract; Sec. IV
- Evidence: "The 95% CL lower limits for the cutoff energy are 750 TeV and 1140 TeV for LHAASO J0534+2202 and LHAASO J2032+4102, respectively. [...] The combined limit on the first-order LIV energy scale is about 1.42×10^{33} eV [...] The second-order LIV energy scale reaches 10^{-3} times of the Planck scale"
- Verified: FULLTEXT
- Notes: The highest-energy photon-like event is about 1.4 PeV (abstract). LHAASO states that photon decay "occurs rapidly and leads to a sharp cutoff in the γ-ray spectrum".

### C-03-048
- Claim: Götz et al. combine the INTEGRAL/IBIS polarization of GRB 140206A (> 28% at 90% c.l. in the second peak) with its redshift z = 2.739 and obtain a vacuum-birefringence limit ξ < 1 × 10^{-16}. Here ξ is the coefficient of the helicity-dependent cubic term, ω^2 = k^2 ± 2ξk^3/M_Pl.
- Source: Gotz2014grb
- Locator: Abstract; Sec. 4, eqs. (2)-(5)
- Evidence: "constrain the linear polarization level of the second peak of this GRB as being larger than 28% at 90% c.l. [...] z=2.739. This distance value together with the polarization measure obtained with IBIS, allowed us to derive the deepest and most reliable limit to date (ξ <1×10^{-16})"
- Verified: FULLTEXT
- Notes: The limit follows from requiring the differential rotation to be ≤ 90° across the band. No CL is attached to ξ. It constrains CPT-odd n = 3 physics, which the Beane lattice does not generate at leading order (C-03-038).

### C-03-049
- Claim: Kostelecký and Mewes report that evidence for linear polarization in GRBs improves sensitivities to photon-sector Lorentz and CPT violation by factors of ten to a million.
- Source: Kostelecky2013constraints
- Locator: Abstract
- Evidence: "Recent evidence for linear polarization in gamma-ray bursts improves existing sensitivities to Lorentz and CPT violation involving photons by factors ranging from ten to a million."
- Verified: ABSTRACT
- Notes: Birefringent SME coefficients. For context only.

### C-03-050
- Claim: Jacobson, Liberati and Mattingly use the ~100 MeV synchrotron emission of the Crab Nebula to constrain a type of Lorentz violation that gives electrons a maximum speed below c, improving previous limits by a factor of 40 million. In the Lorentz-invariant case, 100 MeV synchrotron photons require electrons of about 1500 TeV.
- Source: Jacobson2003strong
- Locator: Abstract; p. 10 (eqs. 9-11)
- Evidence: "We use the observation of 100 MeV synchrotron radiation from the Crab nebula to improve the previous limits by a factor of 40 million" "The energy of the electrons that produce the synchrotron radiation of frequency 100 MeV is 1500 TeV in the Lorentz invariant case."
- Verified: FULLTEXT
- Notes: The original constraint is n = 3. The n = 4 extension is C-03-040.

### C-03-051
- Claim: Maccione et al. set constraints of order 10^{-5} at 95% CL on O(E/M) (n = 3) lepton LV parameters, using a full calculation of the Crab Nebula broadband spectrum.
- Source: Maccione2007new
- Locator: Abstract
- Evidence: "We cast constraints of order 10^{-5} at 95% confidence level on the lepton Lorentz Violation parameters."
- Verified: FULLTEXT
- Notes: For context in the table (n = 3).

### C-03-052
- Claim: Maccione et al. (2009) use the Auger UHECR spectrum to obtain two-sided bounds on dimension-5 and dimension-6 CPT-even operators for protons and pions: dimension-5 operators at the 10^{-3} M_Pl^{-1} level and the dimension-6 proton coefficient at the 10^{-6} M_Pl^{-2} level. Liberati 2013 quotes −10^{-3} ≲ η_p^{(4)} ≲ 10^{-6} at 99% CL.
- Source: Maccione2009planck; Liberati2013tests
- Locator: Maccione2009 abstract; Liberati2013 Sec. 7.4, eq. (76)
- Evidence: Maccione2009: "the dimension five operators are constrained at the level of 10^{-3} M_Planck^{-1}. The magnitude of the dimension six proton coefficient is bounded at the level of 10^{-6} M_Planck^{-2}". Liberati: "the final constraints implied by UHECR physics are (at 99% CL) [183] − 10^{-3} ≲ η_p^{(4)} ≲ 10^{-6}"
- Verified: FULLTEXT
- Notes: Assumes pure proton composition (Liberati Sec. 7.4-7.5). Mapping to a lattice proton requires Beane et al.'s assumption (C-03-012) that composite particles obey eq. (17), so it appears only in the report.

## F. Naturalness and the preferred-frame problem

### C-03-053
- Claim: Collins et al. argue that combining known particle interactions with a Planck-scale preferred frame produces Lorentz violation at the percent level, about 20 orders of magnitude above earlier estimates, unless the bare parameters are unnaturally fine-tuned. The effect appears as different "speeds of light" for different fields, suppressed only by two powers of Standard Model couplings.
- Source: Collins2004lorentz
- Locator: Abstract; p. 2-3; Appendix
- Evidence: "combining known elementary particle interactions with a Planck-scale preferred frame gives rise to Lorentz violation at the percent level, some 20 orders of magnitude higher than earlier estimates, unless the bare parameters of the theory are unnaturally strongly fine-tuned." "different fields have different values of c, with fractional differences around 0.1% to 10%."
- Verified: FULLTEXT
- Notes: Their argument explicitly assumes real time and a Minkowski-space cutoff: "We assume here that the treatment involves real time, not an analytic continuation to imaginary time".

### C-03-054
- Claim: Collins et al. note that discreteness need not conflict with the absence of a preferred frame, citing the random causal set of Dowker et al. They identify the key theoretical task as finding a mechanism, such as a custodial symmetry, that gives automatic low-energy Lorentz invariance.
- Source: Collins2004lorentz
- Locator: p. 3
- Evidence: "There is not necessarily a conflict between discreteness and the absence of a preferred frame. In [28] Dowker et al. show how, by the use of a random causal set of points, space-time can be made discrete while Lorentz invariance is preserved in a suitable sense." "One mechanism is to have a custodial symmetry that is sufficient to prohibit Lorentz-violating dimension 4 terms, without itself being the full Lorentz group. But such a symmetry does not appear to be known."
- Verified: FULLTEXT
- Notes: none

### C-03-055
- Claim: Gambini, Rastgoo and Pullin argue that non-perturbative treatments such as loop quantum gravity may produce Lorentz-invariance deviations that do not necessarily have low-energy consequences.
- Source: Gambini2011small
- Locator: Abstract
- Evidence: "We show that non-perturbative treatments like those of loop quantum gravity may generate deviations of Lorentz invariance of a different type than those considered by Collins et al. that do not necessarily imply observational consequences at low energy."
- Verified: FULLTEXT
- Notes: none

### C-03-056
- Claim: Polchinski replies that a Euclidean lattice with equal steps has discrete rotational symmetry forbidding Lorentz-violating dimension-4 terms, but a Lorentzian lattice has no such enhanced symmetry, and continuing from the Euclidean lattice conflicts with unitarity. He concludes that almost all models of observable high-energy Lorentz violation are ruled out by low-energy tests, and that the only known exceptions rely on supersymmetry.
- Source: Polchinski2012comment
- Locator: Abstract; p. 2
- Evidence: "A Euclidean lattice with equal steps along different axes has discrete rotational symmetries, which forbids the dimension 4 terms that would violate the Euclidean Lorentz (i.e. rotational) invariance [...] However, we are interested in a Lorentzian world, and a Lorentzian lattice with equal time and space steps has no such enhanced symmetry. [...] However, a lattice propagator has an analytic structure not consistent with unitarity." Abstract: "almost all models of observable high energy Lorentz violation, and proposed Lorentz-violating theories of quantum gravity, are ruled out by low energy tests; the only known exceptions are based on supersymmetry."
- Verified: FULLTEXT
- Notes: This bears directly on Beane et al.'s footnote 3 (C-03-004). Polchinski does not discuss Beane et al.

### C-03-057
- Claim: Belenchia, Gambassi and Liberati revisit LIV naturalness in a Yukawa toy model. They show that separating the EFT validity scale from the LIV scale can hinder low-energy percolation, and that dissipation does not generically percolate to lower-dimension operators although dispersion does.
- Source: Belenchia2016lorentz
- Locator: Abstract
- Evidence: "We then show how a separation between the scale of validity of the effective field theory and that one of Lorentz invariance violations can hinder this low-energy percolation. [...] the dissipative behaviour does not percolate generically to lower mass dimension operators albeit dispersion does."
- Verified: ABSTRACT
- Notes: none

## G. Lorentz-invariant discreteness

### C-03-058
- Claim: Bombelli, Lee, Meyer and Sorkin (1987) proposed that spacetime is a causal set.
- Source: Bombelli1987space
- Locator: title (PRL 59, 521)
- Evidence: Crossref title "Space-time as a causal set"; authors Bombelli, Lee, Meyer, Sorkin; Phys. Rev. Lett. 59, 521-524.
- Verified: METADATA
- Notes: Paywalled. The content claims below use Surya 2019 and Dowker et al. 2004.

### C-03-059
- Claim: Dowker, Henson and Sorkin argue that fundamental discreteness need not contradict Lorentz invariance, and that causal-set discreteness is locally Lorentz invariant. They introduce a phenomenological model in which particles undergo Lorentz-invariant diffusion in phase space ("swerves").
- Source: Dowker2004quantum
- Locator: Abstract
- Evidence: "Contrary to what is often stated, a fundamental spacetime discreteness need not contradict Lorentz invariance. A causal set's discreteness is in fact locally Lorentz invariant [...] The particles undergo a Lorentz invariant diffusion in phase space"
- Verified: FULLTEXT
- Notes: none

### C-03-060
- Claim: Bombelli, Henson and Sorkin prove that no equivariant measurable map exists from Poisson sprinklings of Minkowski space to spacetime directions. A sprinkled causal set therefore picks out no preferred frame and gives no modified dispersion relations, and no finite-valency graph can be associated with a sprinkling consistently with Lorentz invariance.
- Source: Bombelli2009discreteness
- Locator: Abstract
- Evidence: "It proves that there exists no equivariant measurable map from sprinklings to spacetime directions (even locally). [...] This implies that the discreteness of a sprinkled causal set will not give rise to "Lorentz breaking" effects like modified dispersion relations. Another consequence is that there is no way to associate a finite-valency graph to a sprinkling consistently with Lorentz invariance."
- Verified: FULLTEXT
- Notes: none

### C-03-061
- Claim: In a manifold-like causal set the number of nearest neighbours (links) of an element is almost surely infinite, which makes the theory characteristically non-local. Lorentz invariance holds in every realization, not just on average, whereas a random Euclidean lattice (Christ et al. 1982) preserves symmetry only on average.
- Source: Surya2019causal
- Locator: Sec. 3.1 (p. 17-18), Sec. 3.2
- Evidence: "the number of future links to e is (almost surely) infinite. [...] this means the valency of the graph C is infinite. It is this feature of manifold-like causal sets which gives rise to a characteristic "non-locality"" "In Bombelli et al (2009), it was shown that a causal set in C(M^d, ρ_c) not only preserves Lorentz invariance on average, but in every realisation, with respect to the Poisson distribution."
- Verified: FULLTEXT
- Notes: The non-locality is relevant to simulation cost. That point is our interpretation and is attributed as such in the `.tex`.

### C-03-062
- Claim: Surya lists extending the swerve (momentum-space diffusion) calculation from Minkowski space to an FRW universe as an open question. Addazi et al. note that quantum fields on causal sets have so far been described only for the free scalar field.
- Source: Surya2019causal; Addazi2022quantum
- Locator: Surya Sec. 7 (p. 67-68); Addazi Sec. 2 (causal sets paragraph)
- Evidence: Surya: "This spacetime Brownian motion was calculated in M^d and can be constrained by observations (Kaloper and Mattingly 2006), but an open question is how to extend the calculation to our FRW universe." Addazi: "one needs to be able to describe quantum fields of spin 0, 1/2 and 1 and 2 on a causal set to describe SM matter as well as GWs/gravitons. So far, this has only been achieved for the free scalar field"
- Verified: FULLTEXT
- Notes: none

### C-03-063
- Claim: Philpott, Dowker and Sorkin show that, at large scales, swerves give Lorentz-invariant energy-momentum diffusion governed by one parameter for massive particles and two (diffusion and drift) for massless ones. They bound the photon parameters using the blackbody spectrum of the CMB.
- Source: Philpott2009energy
- Locator: Abstract
- Evidence: "the microscopic swerves induced by the underlying atomicity manifest themselves as a Lorentz invariant diffusion in energy-momentum governed by a single phenomenological parameter [...] the most general Lorentz invariant diffusion equation for a massless particle [...] contain[s] two phenomenological parameters describing, respectively, diffusion and drift [...] we deduce bounds on the drift and diffusion constants for photons from the blackbody nature of the spectrum of the cosmic microwave background radiation."
- Verified: FULLTEXT
- Notes: none

### C-03-064
- Claim: Kaloper and Mattingly bound the swerve momentum-diffusion constant with the relic-neutrino background, k < 10^{-61} GeV^3 for m_ν > 0.01 eV. With the EFT-motivated scaling k = c ε^{3−γ} E_C^γ, γ = 3 and E_C at the Planck scale, this requires c < 10^{-118}.
- Source: Kaloper2006low
- Locator: Abstract; Sec. IV.D, eqs. (22)-(24); Sec. V
- Evidence: "we estimate to constrain the momentum space diffusion constant by k < 10^{-61} GeV^3 for neutrinos with masses m_ν > 0.01 eV" "If we fix γ = 3, as suggested by EFT lore, then the corresponding constraint on c is c < 10^{-118} which is an extremely small value begging for a first-principles explanation."
- Verified: FULLTEXT
- Notes: The paper states this as an estimate, not a formal CL.

### C-03-065
- Claim: Hossenfelder's review finds discreteness neither necessary nor sufficient for a minimal length scale, and notes that causal sets can preserve Lorentz invariance by using a random (Poisson) rather than regular sprinkling, so there is no lattice parameter in the ordinary sense.
- Source: Hossenfelder2013minimal
- Locator: Sec. 3.7; Sec. 5
- Evidence: "discreteness seems neither necessary nor sufficient for the existence of a minimal length scale." "the causal sets approach to a discrete spacetime can preserve Lorentz invariance. This can be achieved by using not a regular but a random sprinkling of points; there is thus no meaningful lattice parameter in the ordinary sense."
- Verified: FULLTEXT
- Notes: none

## H. Follow-up literature citing Beane et al.

### C-03-066
- Claim: On 2026-09-27, INSPIRE listed 13 records citing Beane et al., most of them not physics follow-ups. Semantic Scholar listed 61 citing records, dominated by philosophy and popular works.
- Source: Beane2014constraints
- Locator: INSPIRE query refersto:recid:1189720; Semantic Scholar API citations endpoint
- Evidence: INSPIRE "citation_count": 13; Semantic Scholar list length 61 (report §B)
- Verified: METADATA
- Notes: The INSPIRE query `refersto:arxiv:1210.1847` returned a malformed result (25,074 hits), so we used the record-ID query. OpenAlex was rate-limited and not used.

### C-03-067
- Claim: Vazza (2025) cites Beane et al. as a rare quantitative treatment and uses the ~10^{20} eV energies of UHECRs (length scale ~10^{-24} cm) and ~10^{17} eV neutrinos as resolution requirements in an energy-cost argument against the simulation hypothesis.
- Source: Vazza2025astrophysical
- Locator: Sec. 1; Sec. 3 (low-resolution Earth)
- Evidence: "A remarkable exception is the work by Beane et al. (2014), who investigated the potentially observable consequences of the SH, by exploring the particular case of a cubic space-time lattice." "we can use E_UHECR = 10^{20} eV = 1.6·10^8 erg as a conservative limit: this yields a length scale λ_UHECR ∼ 1.2·10^{-24} cm."
- Verified: FULLTEXT
- Notes: Vazza writes Beane et al.'s bound as "inverse lattice spacing [...] ∼ 10^{-11} GeV^{-1}". The units are garbled: Beane et al. have b^{-1} ≳ 10^{11} GeV. Do not repeat this.

## I. Additional framework entry

### C-03-068
- Claim: Coleman and Glashow build a perturbative framework of renormalizable (dimension ≤ 4), gauge-invariant Lorentz-violating terms that are rotationally invariant in a preferred frame (46 CPT-even perturbations). These define species-dependent maximal attainable velocities and, among other effects, can undo the GZK cutoff.
- Source: Coleman1999high
- Locator: Abstract
- Evidence: "Tiny non-invariant terms introduced into the standard model Lagrangian are assumed to be renormalizable (dimension ≤ 4), invariant under SU(3) ⊗ SU(2) ⊗ U(1) gauge transformations, and rotationally and translationally invariant in a preferred frame. There are a total of 46 independent CPT-even perturbations of this kind [...] They define the energy-momentum eigenstates and their maximal attainable velocities in the high-energy limit. [...] relevant both to cosmic-ray physics (e.g., by undoing the GZK cutoff)"
- Verified: ABSTRACT
- Notes: Beane et al. cite this framework and argue that it does not apply directly (C-03-013).
