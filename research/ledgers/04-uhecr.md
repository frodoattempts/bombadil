# Claim ledger: 04-uhecr (UHECRs as a probe of a spacetime lattice; novelty check)

Compiled 2026-09-27. PDFs read from arXiv (versions noted) and saved under
`/tmp/claude-0/papers/`. Quotes are verbatim from `pdftotext` output. Where
`pdftotext` split a superscript or subscript, we give the reading in square brackets.
Claims marked "OWN" in Notes are our own computations or derivations, not literature claims.
Section 5 of the report lists them separately.

## A. The lattice prediction (Beane, Davoudi & Savage)

### C-04-001
- Claim: Beane, Davoudi and Savage assume that the universe is simulated on a hyper-cubic space-time grid and, as a starting point, with an unimproved Wilson action.
- Source: Beane2014constraints
- Locator: arXiv:1210.1847v2, Sec. I (p. 5), and the abstract
- Evidence: "we will assume that the simulation of our universe is done on a hyper-cubic grid and, as a starting point, we will assume that the simulator is using an unimproved Wilson action"
- Verified: FULLTEXT
- Notes: arXiv v2 (9 Nov 2012) was read. The published EPJ A 50 (2014) 148 is paywalled and was not compared.

### C-04-002
- Claim: Their most stringent bound, b^{-1} ≳ 10^{11} GeV (b ≲ 10^{-12} fm), comes from equating the lattice momentum cutoff E_max ~ 1/b with the GZK cutoff of the cosmic-ray spectrum.
- Source: Beane2014constraints
- Locator: Sec. IV.4, text after Eq. (18) (pp. 11-12); abstract
- Evidence: "For both the fermions and the bosons, the cut off from the dispersion relation is E max ∼ 1/b. Equating this to the GKZ cut off corresponds to a lattice spacing of b ∼ 10−12 fm, or a mass scale of b−1 ∼ 1011 GeV." [10^{-12}, 10^{11}]
- Verified: FULLTEXT
- Notes: This is an order-of-magnitude matching argument, not a fit to data. Beane et al. write "GKZ" throughout.

### C-04-003
- Claim: They predict that if the lattice provides the cutoff, the highest-energy cosmic rays would have an angular distribution with the cubic symmetry of the lattice in the lattice rest frame. For much smaller b the cubic signal would weaken and the GZK mechanism would dominate.
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 12
- Evidence: "The most striking feature of the scenario in which the lattice provides the cut off to the cosmic ray spectrum is that the angular distribution of the highest energy components would exhibit cubic symmetry in the rest frame of the lattice, deviating significantly from isotropy. For smaller lattice spacings, the cubic distribution would be less significant, and the GKZ mechanism would increasingly dominate"
- Verified: FULLTEXT
- Notes: The prediction is qualitative. The paper gives no amplitude and no angular template for the flux anisotropy as a function of b.

### C-04-004
- Claim: At leading order, the lattice modification of the Δ-resonance photopion threshold for a head-on proton-photon collision is proportional to the ℓ = 4 cubic harmonic Y_4^0 + sqrt(5/14)(Y_4^4 + Y_4^{-4}), assuming the lattice rest frame coincides with the CMB rest frame.
- Source: Beane2014constraints
- Locator: Eq. (18), p. 11
- Evidence: "When the lattice rest frame coincides with the CMB rest frame, head-on interactions between a high energy proton with momentum |p| and a photon of (very-low) energy ω can proceed through the ∆ resonance when ... Y40 (θ, φ) + sqrt(5/14) (Y4+4 (θ, φ) + Y4−4 (θ, φ)) ..." [reconstructed from the layout]
- Verified: FULLTEXT
- Notes: The equation gives a direction-dependent threshold, not a flux map. OWN: we verified numerically that this combination is invariant under all 48 elements of O_h (max deviation 2e-15), and that O_h-invariant harmonics exist only at ℓ = 0, 4, 6, 8, 10, 12 (two at 12) for ℓ ≤ 12. Script: /tmp/claude-0/papers/cubic.py.

### C-04-005
- Claim: Beane et al. put the GZK cutoff scale at "∼6×10^{20} eV". This is an order of magnitude above the ~6×10^{19} eV threshold quoted by HiRes and the ~4-5×10^{19} eV suppression energies measured by HiRes and Auger.
- Source: Beane2014constraints; HiRes2008first
- Locator: Beane Sec. IV.4, p. 11; HiRes p. 1
- Evidence: Beane: "Processes such as γCMB + N → ∆ give rise to the predicted GKZ-cut off scale [50, 51] of ∼ 6×1020 eV" [6×10^{20}]. HiRes: "a “GZK” threshold of ∼ 6 × 1019 eV was calculated" [6×10^{19}]
- Verified: FULLTEXT
- Notes: Probably a typographical error in arXiv v2. The published version was not checked (paywall). The order-of-magnitude bound b^{-1} ~ 10^{11} GeV = 10^{20} eV is consistent with a cutoff near 10^{20} eV either way. We flag the number so that the review does not repeat it.

### C-04-006
- Claim: Beane et al. note that for a composite proton the relation between energy and momentum involves parton distributions. Their numerical analysis assumes that all particles obey the lattice dispersion relations of their Eqs. (16)-(17). They do not discuss primaries that are heavy nuclei.
- Source: Beane2014constraints
- Locator: Sec. IV.4, p. 10 and footnote 10
- Evidence: "for composite particles, such as the proton or pion, the dispersion relations will be dynamically generated. In the present analysis we assume that the dispersion relations for all particles take the form of those in eq. (16) and eq. (17)."
- Verified: FULLTEXT
- Notes: The absence of a discussion of nuclei as cosmic-ray primaries is an absence claim. We searched the arXiv v2 text for "nucle", "iron" and "composition"; the only hits are about nuclear physics on the lattice and "collisions of nucleons with the cosmic microwave background". OWN: a nucleus of mass number A and energy E carries about E/A per nucleon, which weakens the cutoff matching if the primaries are heavy.

## B. Spectrum: the flux suppression

### C-04-007
- Claim: Greisen (1966) and Zatsepin & Kuzmin (1966) predicted a suppression of the cosmic-ray flux above a threshold of about 6×10^{19} eV, caused by photopion production on the CMB, assuming a proton-dominated extragalactic flux.
- Source: Greisen1966end; Zatsepin1966upper; HiRes2008first
- Locator: HiRes2008first p. 1 (description of the 1966 predictions)
- Evidence: HiRes: "In 1966, Greisen [1], and Zatsepin and Kuzmin [2], proposed an upper limit to the cosmic-ray energy spectrum. Their predictions were based on the assumption of a proton dominated extra-galactic cosmic-ray flux which would interact with the photons in the cosmic microwave background (CMB) via photo-pion production."
- Verified: METADATA (Greisen, Zatsepin-Kuzmin); FULLTEXT (HiRes description)
- Notes: The 1966 originals are paywalled (APS 403; JETP Lett. archive 403). The characterization rests on the HiRes text.

### C-04-008
- Claim: HiRes reported the first observation of the GZK suppression at 5 standard deviations, with a break at log10(E/eV) = 19.75 ± 0.04.
- Source: HiRes2008first
- Locator: abstract; p. 4 (fit and significance)
- Evidence: "We found the two breaks at log E (E in eV) of 19.75 ± 0.04 and 18.65 ± 0.05, corresponding to the GZK cutoff and the ankle"; "we expect 43.2 events above 10^19.8 eV from the extrapolation, whereas 13 events were actually found in the data. The Poisson probability for the observed deficit is 7 × 10−8 , which corresponds to 5.3 standard deviations."
- Verified: FULLTEXT
- Notes: HiRes also finds E_{1/2} = 10^{19.73±0.07} eV and a slope of 5.1 ± 0.7 above the break.

### C-04-009
- Claim: Auger (2008) rejected, at 6 standard deviations, the hypothesis that the spectrum continues with a constant slope above 4×10^{19} eV. The spectral index steepens from 2.69 ± 0.02 (stat) ± 0.06 (syst) to 4.2 ± 0.4 (stat) ± 0.06 (syst).
- Source: PierreAuger2008observation
- Locator: abstract; final paragraph
- Evidence: "we reject the hypothesis that the cosmic-ray spectrum continues with a constant slope above 4 × 1019 eV, with a significance of 6 standard deviations"
- Verified: FULLTEXT
- Notes: The paper itself is cautious: "the results suggest that the GZK prediction of spectral steepening may have been verified. A full identification of the reasons for the suppression will come from knowledge of the mass spectrum".

### C-04-010
- Claim: Auger's 2020 spectrum, based on 215,030 events above 2.5×10^{18} eV, shows a suppression above E_34 = (46 ± 3 ± 6)×10^{18} eV with spectral index γ_4 = 5.1 ± 0.3 ± 0.1, and a newly observed "instep" softening at E_23 = (13 ± 1 ± 2)×10^{18} eV.
- Source: PierreAuger2020features
- Locator: abstract; p. 6
- Evidence: "the spectrum softens further above a suppression energy of E34 = (46 ± 3 ± 6)×1018 eV with γ4 = 5.1 ± 0.3 ± 0.1"; "At E23 = (13±1±2)×1018 eV, the spectrum softens"
- Verified: FULLTEXT
- Notes: The first error is statistical and the second systematic.

### C-04-011
- Claim: The companion Auger PRD analysis is based on an exposure of (60,400 ± 1,810) km² sr yr collected between 1 January 2004 and 31 August 2018.
- Source: PierreAuger2020measurement
- Locator: Sec. (exposure), line "Between 1 January 2004 and 31 August 2018"
- Evidence: "Between 1 January 2004 and 31 August 2018 an exposure (60,400 ± 1,810) km2 sr yr was achieved."
- Verified: FULLTEXT
- Notes: none.

### C-04-012
- Claim: Auger measures E_{1/2} = (2.2 ± 0.1 ± 0.3)×10^{19} eV, which disagrees with the 5.3×10^{19} eV expected for uniformly distributed proton-only sources. Auger states that this popular paradigm is thereby disfavored.
- Source: PierreAuger2020features
- Locator: p. 6-7 (interpretation)
- Evidence: "The prediction in this framework is that E1/2 = 5.3×1019 eV ... The value found here, (2.2 ± 0.1 ± 0.3)×1019 eV, is at variance with the prediction because of the new feature of the spectrum at ≈ 1019 eV, which is absent in the popular paradigm that is thus disfavored."
- Verified: FULLTEXT
- Notes: The paper also states that in the ankle region "a pure proton composition, or one of only protons and helium, is excluded at the 6.4 σ level" (citing an earlier Auger result).

### C-04-013
- Claim: In Auger's benchmark mixed-composition scenario, the steepening above ≈5×10^{19} eV results from the combination of the maximum acceleration energy of the heaviest nuclei and the GZK effect. Auger cautions that alternative scenarios remain viable.
- Source: PierreAuger2020features
- Locator: p. 7
- Evidence: "In this scenario, the steepening observed above ≈ 5×1019 eV results from the combination of the maximum energy of acceleration of the heaviest nuclei at the sources and the GZK effect."; "Some cautionary comments on the illustrative model considered here are in order. The presence of a subdominant light component at the highest energies is not excluded by our data"
- Verified: FULLTEXT
- Notes: Directly relevant to the Beane et al. premise that the observed cutoff is the GZK cutoff.

## C. Mass composition

### C-04-014
- Claim: Auger's surface-detector deep-learning Xmax analysis (10-fold statistics over FD, up to 100 EeV) finds that the composition becomes heavier and purer with energy. This is incompatible with a large fraction of light nuclei between 50 and 100 EeV.
- Source: PierreAuger2025inference
- Locator: abstract
- Evidence: "The energy evolution of the mean and standard deviation of the measured Xmax distributions indicates that the mass composition becomes increasingly heavier and purer, thus being incompatible with a large fraction of light nuclei between 50 EeV and 100 EeV."
- Verified: FULLTEXT
- Notes: The interpretation depends on hadronic interaction models, as stated in the paper.

### C-04-015
- Claim: The same analysis concludes that the observed suppression cannot be ascribed entirely to extragalactic propagation effects.
- Source: PierreAuger2025inference
- Locator: Results section (discussion of Fig. 2b)
- Evidence: "The small fluctuations disfavor a substantial fraction of light particles at the highest energies and, at the same time, indicate that the observed suppression in the energy spectrum cannot be entirely ascribed to effects of extragalactic propagation"
- Verified: FULLTEXT
- Notes: Key point against reading the suppression as a pure GZK (or pure lattice) cutoff.

### C-04-016
- Claim: The elongation rate shows three breaks, at 6.5 ± 0.6 (stat) ± 1 (sys) EeV, 11 ± 2 (stat) ± 1 (sys) EeV and 31 ± 5 (stat) ± 3 (sys) EeV. A constant elongation rate is rejected at 4.4σ once energy-dependent systematics are included.
- Source: PierreAuger2025inference
- Locator: abstract; results
- Evidence: "features three breaks at 6.5 ± 0.6 (stat) ± 1 (sys) EeV, 11 ± 2 (stat) ± 1 (sys) EeV, and 31 ± 5 (stat) ± 3 (sys) EeV"; "Considering energy-dependent systematic uncertainties, the significance level for rejecting a constant elongation rate reduces to 4.4σ"
- Verified: FULLTEXT
- Notes: none.

### C-04-017
- Claim: Auger's combined fit of spectrum and composition above 6×10^{17} eV finds that sources above the ankle emit a mixed composition with a hard spectrum and a low rigidity cutoff.
- Source: PierreAuger2023constraining
- Locator: abstract
- Evidence: "We find our data to be well reproduced if sources above the ankle emit a mixed composition with a hard spectrum and a low rigidity cutoff."
- Verified: FULLTEXT
- Notes: The fit is model-dependent (source evolution, photon backgrounds, hadronic models).

### C-04-018
- Claim: Telescope Array hybrid Xmax data (8.5 years) are compatible with QGSJet II-04 protons at 95% CL in all energy bins, after systematic Xmax shifting. At the highest energies, where statistics are sparse, three other elements are also compatible.
- Source: TelescopeArray2018depth
- Locator: abstract
- Evidence: "For all energy bins, QGSJet II-04 protons are found to be compatible with Telescope Array hybrid data at the 95% confidence level after some systematic Xmax shifting of the data. Three other QGSJet II-04 elements are found to be compatible using the same test procedure in an energy range limited to the highest energies where data statistics are sparse."
- Verified: FULLTEXT
- Notes: TA's interpretation is lighter than Auger's, but its highest-energy statistics do not discriminate strongly. We did not read a joint Auger-TA Xmax comparison, so the tex draft does not claim one.

### C-04-019
- Claim: At E ≈ 10 EeV, the best mass estimates imply a mean charge Z between 1.7 and 5. Recent Galactic-field models give typical deflections of a few tens of degrees at E/Z = 10 EeV.
- Source: PierreAuger2017observation
- Locator: main text, p. 2
- Evidence: "At E ≈ 10 EeV, the best estimates for the mass of the particles [6] lead to a mean value for Z between 1.7 and 5."; "typical values of the deflections of particles crossing the Galaxy are a few tens of degrees for E/Z = 10 EeV, depending on the direction considered"
- Verified: FULLTEXT
- Notes: none.

## D. Large-scale anisotropy

### C-04-020
- Claim: Using 3×10^4 events above 8 EeV from an exposure of 76,800 km² sr yr, Auger reported a dipolar anisotropy at more than 5.2σ. The dipole amplitude is 6.5 (+1.3/−0.9)% towards (α, δ) = (100 ± 10°, −24 (+12/−13)°).
- Source: PierreAuger2017observation
- Locator: abstract
- Evidence: "Using 3×104 cosmic rays above 8×1018 electron volts, recorded with the Pierre Auger Observatory from a total exposure of 76,800 square kilometers steradian year, we report an anisotropy in the arrival directions. The anisotropy, detected at more than the 5.2σ level of significance, can be described by a dipole with an amplitude of 6.5+1.3−0.9 % towards right ascension αd = 100 ± 10 degrees and declination δd = −24+12−13 degrees."
- Verified: FULLTEXT
- Notes: 5.2σ is post-trial. The pre-trial first-harmonic significance is 5.6σ with a chance probability of 2.6×10^{-8} (Table 1: 32,187 events ≥ 8 EeV). Auger interprets the direction, ~125° from the Galactic centre, as indicating extragalactic origin.

### C-04-021
- Claim: With 19 years of data (49,678 events ≥ 8 EeV), the right-ascension dipole modulation reaches 6.8σ, and the 8-16 EeV bin alone exceeds 5σ (5.7σ). The 3D dipole above 8 EeV has amplitude 7.4 (+1.0/−0.8)% towards (α, δ) = (97 ± 8°, −38 ± 9°).
- Source: PierreAuger2024large
- Locator: abstract; Sec. 4.1; Table 1
- Evidence: "For E ≥ 8 EeV, the significance of the dipolar modulation in R.A. is now at 6.8σ and its significance in the 8-16 EeV energy bin is 5.7σ."; Table 1 row "≥8 49,678 5.8+0.9−0.8 −4.5 ± 1.2 7.4+1.0−0.8 97 ± 8 −38+9−9 8.7 × 10−12"
- Verified: FULLTEXT
- Notes: Uncertainties are 68% CL.

### C-04-022
- Claim: No time variation of the dipole above 8 EeV is found; the upper limit on its rate of change is 0.3% per year at 95% CL.
- Source: PierreAuger2024large
- Locator: abstract
- Evidence: "No time variation of the dipole moment above 8 EeV is found, setting an upper limit to the rate of change of such variations of 0.3% per year at the 95% confidence level."
- Verified: FULLTEXT
- Notes: A lattice-fixed pattern would be time-independent in equatorial coordinates, as is the observed dipole. Stationarity does not by itself discriminate between the two.

### C-04-023
- Claim: In the joint 3D dipole-plus-quadrupole fit, the ≥ 32 EeV bin (2,738 events) has a quadrupole amplitude Q = 0.13 ± 0.06. The quadrupolar components are reported as not significant.
- Source: PierreAuger2024large
- Locator: Table 1 (N), Table 4; Sec. 4.2
- Evidence: Table 4 row "Q 0.018 ± 0.010 0.028 ± 0.015 0.05 ± 0.02 0.10 ± 0.03 0.13 ± 0.06" (columns 4-8, ≥8, 8-16, 16-32, ≥32 EeV); Sec. 4.2: "quadrupolar components are not significant"
- Verified: FULLTEXT
- Notes: ℓ = 2 is not an O_h-invariant degree (OWN, C-04-004). This constrains the nuisance model, not the lattice signal directly.

## E. Angular power spectrum and higher multipoles

### C-04-024
- Claim: Because Auger covers only part of the sky, individual a_ℓm cannot be estimated with useful resolution once ℓ_max > 2. Auger therefore reconstructs the angular power spectrum under the hypothesis that the anisotropies are a realization of a statistically isotropic stochastic process.
- Source: PierreAuger2024large; PierreAuger2017multiresolution
- Locator: PierreAuger2024large Sec. 3.3; PierreAuger2017multiresolution Sec. 2.1
- Evidence: 2024: "Due to the incomplete sky coverage of the Pierre Auger Observatory, the estimation of the individual aℓm coefficients cannot be carried out with relevant resolution as soon as ℓmax > 2 ... it is possible to reconstruct the angular power spectrum within a statistical resolution independent of the bound ℓmax ... if the observed distribution of arrival directions represents a particular realization of an underlying stochastic process in which the anisotropies cancel in the ensemble average"
- Verified: FULLTEXT
- Notes: A single fixed, lattice-aligned pattern is a deterministic, not statistically isotropic, sky. The pseudo-C_ℓ deconvolution is derived in ensemble average under that hypothesis, so its applicability to a fixed O_h pattern would need checking by simulation (OWN remark).

### C-04-025
- Claim: Auger's 2024 angular power spectrum covers ℓ = 1-20 in four energy bins above 4 EeV. Besides the dipole, only Ĉ_17 (4-8 EeV) and Ĉ_8 (16-32 EeV) exceed the 99% isotropic band, with penalized chance probabilities of 3.3% and 26.5%. All other Ĉ_ℓ, including ℓ = 4 and 6, are not significant.
- Source: PierreAuger2024large
- Locator: Sec. 4.3; Fig. 4
- Evidence: "Besides the significant dipolar pattern corresponding to Ĉ1 , the only Ĉℓ values that stand above the 99% CL of isotropic fluctuations are Ĉ17 ... and Ĉ8 ... After statistical penalization for searches over different multipoles and energy bins (four independent energy bins × 20 multipole measurements = 80), the probability of these results arising from fluctuations of isotropy are 3.3% and 26.5%, respectively. All other Ĉℓ values in different energy bins are not significant."
- Verified: FULLTEXT
- Notes: The energy bins are 4-8, 8-16, 16-32 and ≥ 32 EeV, plus a cumulative ≥ 8 EeV panel.

### C-04-026
- Claim: Auger's 2024 paper derives 99% CL upper limits on each C_ℓ from simulations, but gives them only graphically (red lines in Fig. 4). No numerical C_4 or C_6 limits are tabulated.
- Source: PierreAuger2024large
- Locator: Sec. 4.3 and Fig. 4 caption; Tables 1-5
- Evidence: "The red lines indicate the upper limits on multipole amplitudes with 99% CL."; Fig. 4 caption: "The red lines correspond to the 99% CL upper limits."
- Verified: FULLTEXT
- Notes: The absence of tabulated C_4 and C_6 values was checked by searching all tables (Tables 1-5) in the layout text. This is a gap for the review: the numbers would have to be digitized or requested from the collaboration.

### C-04-027
- Claim: Auger's 2017 multi-resolution study (angular power spectrum plus needlets, E > 4 EeV) found no deviation from isotropy at any angular scale in 4-8 EeV. Above 8 EeV it found only an indication of a dipole moment and no deviation for moments beyond the dipole.
- Source: PierreAuger2017multiresolution
- Locator: abstract
- Evidence: "No deviation from isotropy is observed on any angular scale in the energy range between 4 and 8 EeV. Above 8 EeV, an indication for a dipole moment is captured; while no other deviation from isotropy is observed for moments beyond the dipole one."
- Verified: FULLTEXT
- Notes: none.

### C-04-028
- Claim: The first joint Auger-TA full-sky analysis above 10^{19} eV (8,259 Auger and 2,130 TA events) estimated all a_ℓm up to ℓ = 20 and the power spectrum up to ℓ = 20. It found no significant deviation from isotropy.
- Source: PierreAugerTA2014searches
- Locator: abstract; Secs. 2.1-2.2 (event counts); Secs. 5.1 and 5.4; Figs. 8 and 11
- Evidence: "A significance table for the coefficients up to ℓ = 20, built simply by dividing each estimated coefficient by its corresponding uncertainty, is reported in the left panel of figure 8 ... overall, the extraction of the multipole coefficients does not provide any evidence for anisotropy."; power spectrum: "Overall, no significant deviation from isotropy is found from this study."; "the total number of events above 1019 eV is 8259"; "for a total number of events above 1019 eV amounting to 2130"
- Verified: FULLTEXT
- Notes: Only ℓ ≤ 3 coefficients are tabulated (Table 1). The ℓ = 4-20 values appear only graphically. Upper limits are given for the dipole (7-13%) and a symmetric quadrupole (7-10%), varying with direction.

### C-04-029
- Claim: The 2025 Auger-TA full-sky update (Auger 2004-2022; TA May 2008-May 2024) introduced a harmonic-space auto- and cross-correlation analysis for ℓ ≤ 20, scanning the energy threshold. In all cases the quadrupole is the most significant multipole.
- Source: PierreAugerTA2025new
- Locator: abstract; Sec. 2; Sec. 5
- Evidence: "we also introduce a new angular harmonic space analysis that allows us to measure both the auto-correlation and cross-correlation with all catalogues for all multipoles independently (ℓmax = 20 in this work)"; "From this figure we see that the quadrupole is the most statistically significant multipole in all cases."
- Verified: FULLTEXT
- Notes: Conference proceedings (ICRC 2025), not peer-reviewed in the journal sense. The Auger large-scale set has an exposure of 123,000 km² sr yr; the TA set has an effective exposure of 19,500 km² sr yr.

### C-04-030
- Claim: In that update, the UHECR auto-correlation peaks at ℓ = 2 above 41 EeV (Auger scale) with 4.2σ pre-trial and 2.1σ post-trial. The post-trial correction accounts for the energy scan and the ℓ ≤ 20 multipoles. By implication, no ℓ = 4 or ℓ = 6 auto-correlation exceeds this.
- Source: PierreAugerTA2025new
- Locator: Sec. 5; Table 2
- Evidence: Table 2: "Auto-Correlation 2 41 EeVAuger ≈ 51.8 EeVTA 4.2σ 2.1σ"; text: "by taking into account the scan in energy and the measurements of different mutipoles up to ℓ = 20"
- Verified: FULLTEXT
- Notes: The "by implication" part follows from "the quadrupole is the most statistically significant multipole in all cases". Pre-trial significances of ℓ = 4 and 6 are only in Fig. 6 (graphical).

### C-04-031
- Claim: An independent reanalysis of the 32,187 public Auger events above 8 EeV (from the 2017 release) used a likelihood method that fits the acceptance and background simultaneously. It recovered an equatorial dipole of (5.3 ± 1.3)% at α = 103 ± 15° and found no significant medium- or small-scale anisotropy, including in the pseudo power spectrum.
- Source: Ahlers2018searching
- Locator: abstract; Sec. 5; Fig. 4; Sec. 6
- Evidence: "Our best-fit dipole anisotropy in the equatorial plane has an amplitude of 5.3 ± 1.3 percent and right ascension angle of 103 ± 15 degrees, consistent with the results of the Pierre Auger Collaboration. We do not find evidence for the presence of medium- or small-scale anisotropies."
- Verified: FULLTEXT
- Notes: A precedent that an external researcher can run an all-scale analysis on public Auger event lists. The public data came from the Science 2017 release (www.auger.org/data/science2017.tar.gz, per PierreAuger2017observation acknowledgments).

## F. Intermediate-scale anisotropy and notable events

### C-04-032
- Claim: With 5,514 events above 20 EeV, Auger found that a starburst-galaxy sky model fits better than isotropy at 4.0σ.
- Source: PierreAuger2018indication
- Locator: abstract
- Evidence: "The data consist of 5514 events above 20 EeV with zenith angles up to 80 ◦ recorded before 2017 April 30."; "It is found that the starburst model fits the data better than the hypothesis of isotropy with a statistical significance of 4.0 σ"
- Verified: FULLTEXT
- Notes: none.

### C-04-033
- Claim: With the full Phase 1 set of 2,635 events above 32 EeV (1 Jan 2004 to 31 Dec 2020; exposure 122,000 km² sr yr), Auger reports evidence for intermediate-scale anisotropy at 4σ for E ≳ 40 EeV. The scale is a ~15° Gaussian spread or ~25° top-hat radius.
- Source: PierreAuger2022arrival
- Locator: abstract; Appendix A
- Evidence: "We publish this data set, the largest available at such energies from an integrated exposure of 122,000 km2 sr yr ... Evidence for a deviation in excess of isotropy at intermediate angular scale, with ∼ 15◦ Gaussian spread or ∼ 25◦ top-hat radius, is obtained at the 4 σ significance level for cosmic-ray energies above ∼ 40 EeV."; "The data set used here consists of 2,635 events above 32 EeV collected at the Pierre Auger Observatory from 1 January 2004 to 31 December 2020."
- Verified: FULLTEXT
- Notes: none.

### C-04-034
- Claim: In that data set, the blind search's most significant excess is at E ≥ 41 EeV within 24° of (α, δ) = (196.3°, −46.6°), in the Centaurus region: 5.4σ local, 3% post-trial. The starburst model gives the lowest post-trial p-value, 3.2×10^{-5}, at E_th = 38 EeV.
- Source: PierreAuger2022arrival
- Locator: Sec. 3.1; Table 2
- Evidence: "The most significant excess, with 5.4 σ local significance, is found above an energy threshold of 41 EeV within a top-hat window of 24◦ radius centered on equatorial coordinates (α, δ) = (196.3◦ , −46.6◦ ) ... resulting in a post-trial p-value of 3%."; Table 2: "Starbursts (radio) 38 15+8−4 9+6−4 25.0 3.2 × 10−5"
- Verified: FULLTEXT
- Notes: none.

### C-04-035
- Claim: The 2025 joint Auger-TA medium-scale analysis finds the starburst correlation to be the most significant, at 4.2σ post-trial.
- Source: PierreAugerTA2025new
- Locator: Sec. 6 (Conclusions)
- Evidence: "The correlation with starburst galaxies remains the most significant, at 4.2𝜎 post-trial, even after the inclusion of attenuations"
- Verified: FULLTEXT
- Notes: Conference proceedings.

### C-04-036
- Claim: Telescope Array reported a "hotspot" of events above 57 EeV in 5 years of data. The hotspot is centered at (α, δ) = (146.7°, 43.2°) with a Li-Ma significance of 5.1σ (20° oversampling), and the probability of such a cluster arising by chance in an isotropic sky is 3.7×10^{-4} (3.4σ).
- Source: TelescopeArray2014indications
- Locator: abstract; Appendix A (list of 72 events)
- Evidence: "The hotspot has a Li-Ma statistical significance of 5.1σ, and is centered at R.A. = 146.◦7, Dec. = 43.◦2. ... The probability of a cluster of events of 5.1σ significance, appearing by chance in an isotropic cosmic-ray sky, is estimated to be 3.7×10−4 (3.4σ)."
- Verified: FULLTEXT
- Notes: The appendix lists the 72 events with E > 57 EeV (May 2008 to May 2013). This is a public northern-sky event list.

### C-04-037
- Claim: TA detected an event (27 May 2021) with energy 244 ± 29 (stat.) +51/−76 (syst.) EeV arriving from (α, δ) = (255.9°, 16.1°). Its direction points back to a void in the large-scale structure. TA lists the possible explanations as a large magnetic deflection, an unidentified nearby source, or incomplete knowledge of particle physics.
- Source: TelescopeArray2023extremely
- Locator: abstract; Table 1 of the main text
- Evidence: "We calculate the particle’s energy as 244 ± 29 (stat.) +51−76 (syst.) exa-electron volts (∼ 40 joules). Its arrival direction points back to a void in the large-scale structure of the Universe. Possible explanations include a large deflection by the foreground magnetic field, an unidentified source in the local extragalactic neighborhood or an incomplete knowledge of particle physics."; table row "27 May 2021 244±29(stat.) 530±57 38.6±0.4◦ 206.8±0.6◦ 255.9±0.6◦ 16.1±0.5◦"
- Verified: FULLTEXT
- Notes: A single event cannot test an O_h pattern. We cite it for the energy reach and the GMF caveat.

## G. Magnetic deflections

### C-04-038
- Claim: In the JF12 Galactic magnetic field model, a 60 EeV proton is deflected on average by 5.2° across the sky, with a quarter of the sky below 2.2°. The deflection is highly non-uniform, and about 60% larger in the southern part of the Galaxy than in the north.
- Source: Jansson2012new
- Locator: Sec. 7.2
- Evidence: "the average UHE proton deflection in the southern part of the Galaxy is approximately 60% larger than in the north. For a 60 EeV proton, the average deflection (across the sky) is 5.2◦ , with a quarter of the sky having less than 2.2◦ deflections. The magnitude of the deflection is highly non-uniform across the sky."
- Verified: FULLTEXT
- Notes: The random-field component is described in Jansson2012galactic. We did not extract a random-field deflection number, so the tex quotes none.

### C-04-039
- Claim: Deflection angles scale with the particle's charge Z, with the integrated transverse field, and inversely with energy (that is, inversely with rigidity).
- Source: PierreAuger2017observation
- Locator: p. 2
- Evidence: "They undergo angular deflections with amplitude proportional to their atomic number Z, to the integral along the trajectory of the magnetic field (orthogonal to the direction of propagation), and to the inverse of their energy E."
- Verified: FULLTEXT
- Notes: This is the small-angle regime; at low rigidity deflections are not linear.

### C-04-040
- Claim: Unger & Farrar (UF23) provide an ensemble of eight coherent-field model variations. Requiring deflections below 20° in half the sky in all eight models needs rigidity R ≥ 20 EV without correction, or 11 EV if arrival directions are corrected for the modelled deflection. The authors call this estimate indicative, since random fields are not included.
- Source: Unger2024coherent
- Locator: Sec. 8.1; Fig. 20
- Evidence: "Requiring that the deflections in half of the sky are less than θmax = 20◦ , according to all of these models, requires the rigidity to be greater than or equal to R50nocorr = 20 EV."; "With corrections, the rigidity quantile at which half of the sky can be observed at θmax = 20◦ or better, decreases to R50corr = 11 EV giving a much greater observational reach. Note that this discussion is indicative only, since the minimal rigidity requirement may change when random fields are included in the analysis."
- Verified: FULLTEXT
- Notes: 1 EV = 10^{18} V.

### C-04-041
- Claim: UF23 find that the JF12 deflections lie close to those of the new model ensemble, and that ensemble deflection uncertainties are smaller than the deflections themselves for most of the sky at ultrahigh energies.
- Source: Unger2024coherent
- Locator: Sec. 9 (summary)
- Evidence: "We find that the deflections predicted by the widely-used JF12 model are close to the ones from the new model ensemble. An important conclusion of our work is that the UHECR deflection uncertainties derived from the model ensemble are smaller than the deflection itself for most of the sky at ultrahigh energies"
- Verified: FULLTEXT
- Notes: none.

## H. Public data

### C-04-042
- Claim: Auger's Open Data Portal opened in February 2021 with 10% of the Phase I cosmic-ray data. The cosmic-ray dataset comprises 81,121 showers, of which 25,086 are SD-1500 events: vertical (θ < 60°) above 2.5 EeV and inclined (60°-80°) above 4 EeV. Events are distributed as JSON files plus a CSV summary.
- Source: PierreAuger2025pierre
- Locator: abstract; Sec. 3 ("Cosmic-ray data")
- Evidence: "In February 2021, a portal was released containing 10% of cosmic-ray data collected by the Pierre Auger Observatory from 2004 to 2018"; "The cosmic-ray dataset comprises in total 81 121 showers 3348 of which are hybrid events"; "A total of 25 086 events measured with the SD-1500 have been selected. This set includes both vertical events, with a zenith angle less than 60◦ , and inclined events in the zenith interval 60◦ − 80◦ . Their reconstructed energies are above 2.5 EeV and 4 EeV respectively"
- Verified: FULLTEXT
- Notes: Portal page (https://opendata.auger.org/data.php, visited 2026-09-27) states the same counts. It gives the SD-1500 period as January 2004 to August 2018 and says the sample is events whose "sdid" ends in zero.

### C-04-043
- Claim: As of 27 September 2026, the current open-data release is release 3 (20 March 2024; DOI 10.5281/zenodo.10488964), still at the 10% level. The Zenodo record holds a 869 MB `data.zip` (JSON) and a 7.9 MB `summary.zip` (CSV) under CC BY-SA 4.0.
- Source: PierreAuger2024pierre
- Locator: Zenodo API record 10488964 (files and sizes); portal release list
- Evidence: Portal: "Mar 20, 2024: release 3, DOI 10.5281/zenodo.10488964"; Zenodo file list: "data.zip 869470279", "summary.zip 7852063"; license "cc-by-sa-4.0"; concept record 4487612 "latest" resolves to 10488964.
- Verified: FULLTEXT (primary web record inspected)
- Notes: OWN tally from the downloaded summary CSVs: 155 SD events ≥ 32 EeV (114 vertical + 41 inclined), 86 ≥ 40 EeV, 24 ≥ 57 EeV.

### C-04-044
- Claim: The Auger Collaboration Board approved (June 2023) raising the public fraction to 30% of the main-array events above 2.5×10^{18} eV from January 2004 to December 2022, with an exposure of about 24,000 km² sr yr, in the same format as before. The release was planned for late 2025.
- Source: PierreAuger2025expanding
- Locator: abstract; Sec. 3
- Evidence: "the Pierre Auger Collaboration will disclose 30% of the cosmic ray events above 2.5 · 1018 eV collected with the main surface detector array between 2004 and 2022, corresponding to an exposure of about 24 000 km2 sr yr"; "The new release is planned for late 2025. Data is selected by the same criteria applied for the vertical spectrum analysis"; "Data will be shared in the same format as the previous releases."
- Verified: FULLTEXT
- Notes: Our checks on 2026-09-27 of the portal pages and the Zenodo concept record 4487612 (latest version = v3, 2024) found no 30% release yet. The 30% sample is selected with vertical-spectrum criteria (θ < 60°, per the paper's Fig. 6).

### C-04-045
- Claim: The full Phase 1 list of 2,635 events above 32 EeV is public on Zenodo (DOI 10.5281/zenodo.6504276 / 6759610, CC BY 4.0) with analysis code. It gives, per event, time, local and equatorial coordinates, energy, and cumulative exposure.
- Source: PierreAuger2022arrival; PierreAuger2022material
- Locator: PierreAuger2022arrival Appendix A; Zenodo record 6759610
- Evidence: "For each event, we report the year in which the event was detected, the Julian day of the year and the time of detection in UTC seconds. The arrival directions are expressed in local coordinates, (θ, φ) ... and in equatorial coordinates (J2000), (α, δ) ... Finally, the reconstructed energy, in EeV, and the integrated exposure accumulated up to the time of detection are reported"; "The full list of 2,635 events ... is available at DOI 10.5281/zenodo.6504276 together with the code"
- Verified: FULLTEXT (paper and downloaded file inspected)
- Notes: OWN tally of `AugerApJS2022_Yr_JD_UTC_Th_Ph_RA_Dec_E_Expo.dat`: 2,635 events, E from 32.0 to 165.5 EeV, 1,387 ≥ 40 EeV, 411 ≥ 57 EeV, 95 ≥ 80 EeV, 35 ≥ 100 EeV; θ ≤ 79.9°; last cumulative exposure 121,420 km² sr yr. For a search above 32 EeV this is 100% of Phase 1, far more than the 10%/30% open-data fractions.

### C-04-046
- Claim: Auger published a catalog of the 100 highest-energy events recorded between 1 January 2004 and 31 December 2020 (78-166 EeV), plus nine calibration events. The catalog offers no interpretation.
- Source: PierreAuger2023catalog
- Locator: abstract
- Evidence: "Descriptions of the 100 showers created by the highest-energy particles recorded between 2004 January 1 and 2020 December 31 are given for cosmic rays that have energies in the range 78–166 EeV. ... No interpretations of the data are offered."
- Verified: ABSTRACT
- Notes: PierreAuger2025expanding describes the same catalog as covering "2004 and 2022" and "76 EeV and 166 EeV". We follow the ApJS abstract; the discrepancy is noted in the report.

## I. Novelty check: nearest analogues and citing literature

### C-04-047
- Claim: Klinkhamer & Risse bounded the nine nonbirefringent (including direction-dependent) Lorentz-violating photon parameters of modified Maxwell theory at the 10^{-18} level from the absence of vacuum Cherenkov radiation by UHECRs. They first used pseudo-random directions; in a note added in proof they used the actual directions of 27 Auger events above 57 EeV plus one AGASA and one Fly's Eye event.
- Source: Klinkhamer2008ultrahigh
- Locator: abstract; Note added in proof
- Evidence: "New bounds on the remaining nine nonbirefringent parameters can be obtained from the absence of vacuum Cherenkov radiation for ultrahigh-energy cosmic rays (UHECRs). Using selected UHECR events recorded at the Pierre Auger Observatory and assigning pseudo-random directions (i.e., assuming large-scale isotropy), Cherenkov bounds are found at the 10−18 level"; "The observed energies and directions of these 29 events can now be used to sharpen bound (14)"
- Verified: FULLTEXT
- Notes: This is a direction-dependent Lorentz-violation test that uses UHECR arrival directions. It tests a threshold (existence of events along given directions), not an anisotropy of the flux, and not a cubic/O_h pattern. It is the closest analogue we found.

### C-04-048
- Claim: IceCube searched atmospheric muon-neutrino data for a sidereal modulation that would indicate direction-dependent, Lorentz-violating oscillations, and found none.
- Source: IceCube2010search
- Locator: abstract
- Evidence: "A search for sidereal modulation in the flux of atmospheric muon neutrinos in IceCube was performed. ... Neutrino oscillation models ... allow for neutrino oscillations that depend on the neutrino's direction of propagation. No such direction-dependent variation was found."
- Verified: ABSTRACT
- Notes: Tests preferred-direction (SME-type) coefficients, not O_h symmetry.

### C-04-049
- Claim: Auger's Lorentz-invariance-violation study uses isotropic, direction-independent modified dispersion relations of the form E_i² = m_i² + p_i² + δ_{i,n} E^{2+n}.
- Source: PierreAuger2022testing
- Locator: abstract
- Evidence: "Lorentz invariance violation (LIV) is often described by dispersion relations of the form E i 2 = m i 2+p i 2+δ i,n E 2+n with delta different based on particle type i"
- Verified: ABSTRACT
- Notes: The characterization as "isotropic" follows from the form (no direction dependence) quoted in the abstract.

### C-04-050
- Claim: Vazza (2025), a citing work, uses the UHECR energy scale only as a spatial-resolution requirement for a simulator. It does not analyze arrival directions. It also restates the Beane bound in inverted units ("∼10^{-11} GeV^{-1}").
- Source: Vazza2025astrophysical
- Locator: Sec. 1 (p. 1-2); Sec. 3 (UHECR paragraph)
- Evidence: "They found that the most stringent bound on the inverse lattice spacing of the universe is ∼ 10−11 GeV−1"; "hence we can use EUHECR = 1020 eV = 1.6·108 erg as a conservative limit: this yields a length scale λUHECR ∼ 1.2·10−24 cm."
- Verified: FULLTEXT
- Notes: Beane et al. state b^{-1} ≳ 10^{11} GeV. The Vazza phrasing inverts the units. Vazza dates the Amaterasu event to 2022; TA gives 27 May 2021.

### C-04-051
- Claim: Mlodinow & Brun (2025) show that a quantum-cellular-automaton version of QED on a cubic lattice implies speed-of-light deviations and spatial anisotropies. They bound the lattice spacing using GRB timing and laboratory anisotropy limits, not UHECR arrival directions.
- Source: Mlodinow2025bounds
- Locator: abstract; Sec. II; conclusions ("Anisotropy: the velocity of light differs slightly along lattice axes versus oblique directions. Using arrival-time data from high-energy gamma-ray bursts ...")
- Evidence: "we analyze the QCA corresponding to QED and show that it implies both a deviation from the speed of light and spatial anisotropies. Using current experimental and astrophysical constraints, we place upper bounds on the QCA lattice spacing"
- Verified: FULLTEXT
- Notes: Theory; belongs mainly to section 03.

### C-04-052
- Claim: In the citation databases we queried, none of the works citing Beane et al. presents an observational analysis of cosmic-ray (or other astroparticle) arrival directions for a lattice-aligned/cubic/O_h anisotropy.
- Source: Beane2014constraints (citation graph)
- Locator: INSPIRE refersto:recid:1189720 (13 citing records); Semantic Scholar citations of arXiv:1210.1847 (61 records), retrieved 2026-09-27
- Evidence: see report Sec. 4 (full classification table)
- Verified: METADATA (citation lists) + FULLTEXT/ABSTRACT for each candidate that could plausibly contain data analysis
- Notes: NASA ADS (API needs a token; web UI served a bot-verification page), Google Scholar (HTTP 429) and OpenAlex (daily quota exhausted) could not be queried. The absence claim is bounded by these gaps.

## J. Additions (multipole reach and blind-search power)

### C-04-053
- Claim: Auger's 2017 multi-resolution study expanded the sky maps in spherical harmonics up to ℓ_max = 64 (∼2.8°), with the power spectrum evaluated for 4 ≤ E/EeV < 8 and E ≥ 8 EeV. The choice was motivated by an expected minimum Galactic deflection of ∼3° even for the most energetic protons.
- Source: PierreAuger2017multiresolution
- Locator: Sec. 4 (opening), Sec. 4.1
- Evidence: "the expected deflection of even the highest energetic protons is around ∼ 3o [57] through the galactic magnetic field (GMF) alone ... Thus the harmonic expansion is performed up to ℓmax = 64 (∼ 2.8o )"; "In the following we evaluate the angular power spectrum in two energy ranges: 4 ≤ E/EeV < 8 and E ≥ 8 EeV."
- Verified: FULLTEXT
- Notes: So ℓ = 4 and 6 have been measured (as C_ℓ) in all the Auger power-spectrum papers since at least 2017.

### C-04-054
- Claim: For simulated skies of 14,000 events from a 5% dipole at declination −30° (−60°), blind searches over all multipoles up to ℓ_max = 64 detect the dipole at 99% CL in only 25% (7%) of cases with the angular power spectrum and 13% (5%) with the needlet analysis.
- Source: PierreAuger2017multiresolution
- Locator: Sec. 4 (discussion of sensitivities)
- Evidence: "The detection efficiencies, at a confidence level C.L. of 99%, obtained after accounting for searches blindly performed considering all multipole moments ℓ up to ℓmax = 64 are 25% (7%) for the Angular Power Spectrum analysis and 13% (5%) for the needlet analysis"
- Verified: FULLTEXT
- Notes: This shows how much power blind all-ℓ searches lose. It motivates a targeted (template) statistic for a specific symmetry.

### C-04-055
- Claim: Beane et al. conclude that improvement masks much of the ability to probe the scenario, and that any but the very earliest universe simulations are unlikely to be unimproved.
- Source: Beane2014constraints
- Locator: Sec. V (Conclusions)
- Evidence: "Given the ease with which current lattice QCD simulations incorporate improvement or employ discretizations that preserve chiral symmetry, it seems unlikely that any but the very earliest universe simulations would be unimproved with respect to the lattice spacing. Of course, improvement in this context masks much of our ability to probe the possibility that our universe is a simulation"
- Verified: FULLTEXT
- Notes: Section 03 (sec:lattice-liv) develops the consequences for the size of the threshold anisotropy.

### C-04-056
- Claim: Auger relates multipole ℓ to an angular scale of about 180°/ℓ (for example, ℓ = 17 to ≈11° and ℓ = 8 to ≈23°).
- Source: PierreAuger2024large
- Locator: Sec. 4.3
- Evidence: "Ĉ17 , corresponding to an angular scale of ∼180◦ /ℓ ≈ 11◦ , and Ĉ8 , corresponding to an angular scale of ∼23◦"
- Verified: FULLTEXT
- Notes: Used for the ℓ = 4 (≈45°) and ℓ = 6 (≈30°) scales (OWN arithmetic). The iron rigidity at E_34 (46 EeV / 26 ≈ 1.8 EV) is also OWN arithmetic.
