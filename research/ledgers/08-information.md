# Claim ledger: 08-information

Topic: information-theoretic proposals linked to the simulation hypothesis, mainly the work of
M. M. Vopson: the mass-energy-information (M/E/I) equivalence principle and the "second law of
infodynamics". These are set against the established thermodynamics of information (Landauer,
Bennett, and the experimental tests).

Read with care:
- AIP Advances pages (pubs.aip.org) sit behind a Cloudflare challenge in this environment. The
  published PDFs we read were obtained from these places:
  - Vopson2022experimental: the Newswise-hosted copy of the published PDF.
  - Vopson2022second: the University of Central Lancashire repository copy of the published PDF.
  - Vopson2025is: the INSPIRE-hosted copy of the published PDF.
  - Vopson2021estimation and Vopson2020information: the arXiv versions.
  - Vopson2019mass and Vopson2023second: we could not reach the full text, so those claims are at
    ABSTRACT level or are taken from Vopson's own later restatements, which we read in full (see
    Notes).
- Claims labelled "this work" are our own calculations or analysis. The report gives the reasoning
  and the reproducibility details (`research/notes/08-information-report.md`, Sec. 4).

---

## A. Established background: Landauer's principle and its tests

### C-08-001
- Claim: Landauer (1961) argued that logically irreversible operations, which lack a single-valued inverse, are associated with physical irreversibility and require a minimal heat generation, typically of order kT, per irreversible function.
- Source: Landauer1961irreversibility
- Locator: Abstract (reprint IBM J. Res. Dev. 44, 261 (2000), p. 261)
- Evidence: "This logical irreversibility is associated with physical irreversibility and requires a minimal heat generation, per machine cycle, typically of the order of kT for each irreversible function."
- Verified: FULLTEXT
- Notes: Read as page images of the 2000 reprint, because the PDF is a scan with no text layer. Original pagination is 183-191.

### C-08-002
- Claim: In Landauer's analysis, resetting a thermal ensemble of bits reduces their entropy by k ln 2 per bit, so at least kT ln 2 of heat per reset bit must appear in the surroundings.
- Source: Landauer1961irreversibility
- Locator: Sec. 4 "Logical irreversibility and entropy generation", reprint p. 265
- Evidence: "The entropy therefore has been reduced by k loge 2 = 0.6931 k per bit. The entropy of a closed system, e.g., a computer with its own batteries, cannot decrease; hence this entropy must appear elsewhere as a heating effect, supplying 0.6931 kT per restored bit to the surroundings."
- Verified: FULLTEXT
- Notes: The heat goes to the surroundings. It is not stored in the memory.

### C-08-003
- Claim: Landauer also noted that when stored information thermalizes, the entropy of the information-bearing degrees of freedom increases by up to kN ln 2 for N bits.
- Source: Landauer1961irreversibility
- Locator: Sec. 4, reprint p. 265 (left column, bottom)
- Evidence: "The degrees of freedom associated with the information can, through thermal relaxation, go to any one of 2^N states (for N bits in the assembly) and therefore the entropy can increase by kN loge 2 as the initial information becomes thermalized."
- Verified: FULLTEXT
- Notes: This is directly relevant to the digital example of the "second law of infodynamics" (C-08-035, C-08-T09).

### C-08-004
- Claim: In Landauer's accounting the erasure cost depends on the statistics of the data. Resetting bits that are already known to be in the target state involves no entropy change and no heat dissipation.
- Source: Landauer1961irreversibility
- Locator: Sec. 4, reprint p. 265 (right column, bottom)
- Evidence: "Consider the extreme case, where the inputs are all ONE, and there is no need to carry out any operation. Clearly then no entropy changes occur and no heat dissipation is involved."
- Verified: FULLTEXT
- Notes: none

### C-08-005
- Claim: Landauer identified a class of devices, such as a particle in a symmetric bistable well, that can hold information without dissipating energy.
- Source: Landauer1961irreversibility
- Locator: Sec. 2 "Classification", reprint p. 262, Fig. 1
- Evidence: "The simplest class and the one to which all the arguments of subsequent sections will be addressed consists of devices which can hold information without dissipating energy. The system illustrated in Fig. 1 is in this class."
- Verified: FULLTEXT
- Notes: Fig. 1 is a symmetric double well. Storing a bit therefore requires no ongoing energy input and no energy difference between the logical states.

### C-08-006
- Claim: In Bennett's statement, Landauer's principle requires that an entropy decrease in the information-bearing degrees of freedom be compensated by an equal or greater entropy increase in the non-information-bearing degrees of freedom or the environment. Typically this happens by importing energy and dissipating it as heat into the environment.
- Source: Bennett2003notes
- Locator: Section "Landauer's Principle", p. 1 (arXiv physics/0210005v2)
- Evidence: "the entropy decrease of the IBDF during a logically irreversible operation must be compensated by an equal or greater entropy increase in the NIBDF and environment. This is Landauer's principle. Typically the entropy increase takes the form of energy imported into the computer, converted to heat, and dissipated into the environment"
- Verified: FULLTEXT
- Notes: none

### C-08-007
- Claim: Bennett distinguishes two cases. Erasing random data can be thermodynamically reversible. Erasing known data is thermodynamically irreversible, because the environmental entropy increase is not compensated by any decrease in the entropy of the data.
- Source: Bennett2003notes
- Locator: Section "Landauer's Principle", p. 1, right column
- Evidence: "If a logically irreversible operation like erasure is applied to random data, the operation still may be thermodynamically reversible ... But if ... the logically irreversible operation is applied to known data, the operation is thermodynamically irreversible, because the environmental entropy increase not compensated by any decrease of entropy of the data."
- Verified: FULLTEXT
- Notes: Bennett also calls the Earman-Norton objection "the one of greatest merit" (same page).

### C-08-008
- Claim: Bérut et al. (2012) erased a one-bit memory made of a colloidal particle in a modulated double-well potential. They found that the mean dissipated heat saturates at the Landauer bound in the limit of long erasure cycles.
- Source: Berut2012experimental
- Locator: Abstract (nature.com landing page)
- Evidence: "Using a system of a single colloidal particle trapped in a modulated double-well potential, we establish that the mean dissipated heat saturates at the Landauer bound in the limit of long erasure cycles."
- Verified: ABSTRACT
- Notes: We could not access the full text of the Nature paper. The authors' longer J. Stat. Mech. (2015) account is open on HAL (ensl-01134137) but is not cited here.

### C-08-009
- Claim: Jun, Gavrilov and Bechhoefer (2014) used a feedback trap and found an asymptotic mean erasure work of 0.71 ± 0.03 kT for full erasure, compatible with ln 2 ≈ 0.693, against 0.05 kT for a control protocol that does not erase. The work is dissipated into the surrounding bath.
- Source: Jun2014high
- Locator: Abstract; p. 1 col. 1; Table I (arXiv 1408.5089v1)
- Evidence: "reducing the number of possible macroscopic states in a system by a factor of two requires work of at least kT ln 2"; "This work is dissipated into a surrounding heat bath."; Table I: "full erasure (p = 1) 0.71 ... no erasure (p = 0.5) 0.05", "The full-erasure value is compatible with ln 2 ≈ 0.693."
- Verified: FULLTEXT
- Notes: The ±0.03 is the stated uncertainty on the asymptotic work column of Table I.

### C-08-010
- Claim: Hong et al. (2016) measured the energy dissipated in erasing single nanomagnetic bits as (4.2 ± 0.9) zJ, or (1.0 ± 0.22) kBT at 300 K, which is within 2 standard deviations of kBT ln 2.
- Source: Hong2016experimental
- Locator: Abstract; Results (Europe PMC full text PMC4795654)
- Evidence: "the energy dissipation was measured to be (4.2 ± 0.9) zJ, which corresponds to a value of (1.0 ± 0.22) k B T (for T = 300 K)"; "Our result is within 2 SDs of the value of k B T ln(2) predicted by Landauer."
- Verified: FULLTEXT
- Notes: The same paper reports a mean simulated dissipation of 0.6842 kBT, with a 95% CI of 0.6740-0.6943 kBT.

### C-08-011
- Claim: Parrondo, Horowitz and Sagawa (2015) review a framework for the thermodynamics of information based on stochastic thermodynamics and fluctuation theorems, together with recent experiments.
- Source: Parrondo2015thermodynamics
- Locator: Abstract
- Evidence: "Here we give an introduction to a novel theoretical framework for the thermodynamics of information based on stochastic thermodynamics and fluctuation theorems, review some recent experimental results, and present an overview of the state of the art in the field."
- Verified: ABSTRACT
- Notes: We could not access the full text.

### C-08-012
- Claim: In the nonequilibrium formulation of Esposito and Van den Broeck, the free energy of a nonequilibrium state, F = E - TS with S the Shannon/von Neumann entropy, exceeds the equilibrium value by T times the relative entropy I = D[ρ||ρ_eq]. The irreversible work is W_irr = T Δ_iS + T ΔI.
- Source: Esposito2011second
- Locator: Eqs. (4)-(7), (11), (12) (arXiv 1104.5165v2)
- Evidence: "the corresponding nonequilibrium system free energy: F(t) = E(t) - T S(t)"; "The free energy of a nonequilibrium state is higher than that of the corresponding equilibrium state by an amount equal to the temperature times the information I needed to specify the nonequilibrium state: F(t) - F_eq(t) = T I(t) ≡ T D[ρ(t)||ρ_eq(t)] ≥ 0."; "W_irr(t) ≡ W(t) - ΔF_eq(t) = T Δ_iS(t) + T ΔI(t)"; "ΔE(t) = W(t) + Q(t)"
- Verified: FULLTEXT
- Notes: Used in C-08-T06 and C-08-T09. Here k_B = 1.

### C-08-013
- Claim: Norton argues that Landauer's principle is usually derived from incorrect assumptions, and that the standard repertoire of processes in the thermodynamics of computation neglects thermal fluctuations and is inconsistent.
- Source: Norton2011waiting
- Locator: Abstract, p. 184
- Evidence: "It is usually derived from incorrect assumptions, most notably, that erasure must compress the phase space of a memory device or that thermodynamic entropy arises from the probabilistic uncertainty of random data." ... "the standard repertoire of processes selectively neglects thermal fluctuations."
- Verified: FULLTEXT
- Notes: Norton's author-hosted PDF of the published version. Norton2005eaters is METADATA only.

## B. Mass-energy-information (M/E/I) conjecture and its tests

### C-08-014
- Claim: Vopson (2019) proposed that a bit of information has a finite mass while it stores information, m_bit = k_B T ln 2 / c^2. This gives 3.19 × 10^-38 kg at 300 K. The paper proposed testing the idea by weighing a data storage device when full and when erased, predicting a change of 2.5 × 10^-25 kg for a 1 Tb device.
- Source: Vopson2019mass
- Locator: Abstract
- Evidence: "it has a finite and quantifiable mass while it stores information. In this framework, it is shown that the mass of a bit of information at room temperature (300K) is 3.19 × 10-38 Kg. ... predicting that the mass of a data storage device would increase by a small amount when is full of digital information relative to its mass in erased state. For 1Tb device the estimated mass change is 2.5 × 10-25 Kg."
- Verified: ABSTRACT
- Notes: The formula m_bit = k_b T ln(2)/c^2 is verified FULLTEXT as Eq. (4) of Vopson2022experimental, citing Vopson2019mass. We checked the arithmetic: k_B(300 K) ln2/c^2 = 3.194e-38 kg and 8e12 × m_bit = 2.56e-25 kg.

### C-08-015
- Claim: The rationale given for M/E/I is that information is equivalent to energy (Landauer) and energy to mass (special relativity), so all three are equivalent. On this view the Landauer energy of a bit "condenses" into mass-energy when the information is stored at equilibrium.
- Source: Vopson2022second
- Locator: Sec. I, p. 075310-1
- Evidence: "if information is equivalent to energy, according to Landauer, and if energy is equivalent to mass, according to Einstein's special relativity, then the triad of mass, energy, and information must all be equivalent, too (i.e., if M = E and E = I, then M = E = I)."; "The M-E-I equivalence principle proposes that the Landauer energy of an information bit condenses into its equivalent mass-energy when the information is stored at equilibrium."
- Verified: FULLTEXT
- Notes: Vopson2020information (arXiv v1, Sec. 4) says M/E/I "explains the mechanism by which a classical digital bit of information at equilibrium stores data without energy dissipation, requiring the bit to acquire a mass".

### C-08-016
- Claim: Earlier, Herrera (2014) used Brillouin's principle to associate a mass of about 3 × 10^-35 g (3 × 10^-38 kg) with one bit at room temperature. Herrera interprets this as the decrease of the system's mass that accompanies the minimal energy dissipated when one bit changes.
- Source: Herrera2014mass
- Locator: Sec. I, Eqs. (2)-(4) (arXiv 1403.4511v1)
- Evidence: "Since the above quantity determines the decreasing of the mass of the system, associated to the change of one bit of information, it is fair to say that such a mass is associated to this information."; "△M ≈ 3 × 10−35 grams."
- Verified: FULLTEXT
- Notes: The numbers match Vopson's m_bit, but the physical reading differs: Herrera's mass leaves the system with the dissipated energy, whereas Vopson's is stored in the bit.

### C-08-017
- Claim: Kish and Granqvist (2013) argue that for a memory based on a symmetric double well, the system's energy and mass after writing are the same as before. For an asymmetric memory (flash), the mass change is of order (kT/c^2) ln(N t_m/τ), about 3.4 × 10^-36 kg at room temperature, and its sign depends on which state is defined as "erased".
- Source: Kish2013does
- Locator: Sec. II "Mass of stored information", Eqs. (12)-(15) (arXiv 1309.7889)
- Evidence: "Though this energy is dissipated by the writing operation during changing the state, the energy and the mass of the system after the operation remain the same as their original values."; "This yields m f ≈ 3.4 x 10−36 kg at room temperature ... However, the mass in Eq. (15) is negative if one defines the erased memory element to be a MOSFET with charged gate!"
- Verified: FULLTEXT
- Notes: Also: "A calculation of the thermodynamic entropy does not give any clue to the correct answer, however, because the increase of entropy is relevant for the energy dissipation (which is then released to the environment) rather than for the change of the energy and mass of the system."

### C-08-018
- Claim: The only direct weighings of storage media we found were made to about 10^-8 kg accuracy. They showed unexplained transient weight changes of order 1 mg after writing or erasing gigabytes of data. The authors do not attribute these to a mass of information, and they are about 17 orders of magnitude above the M/E/I prediction for a terabyte.
- Source: Kish2013does
- Locator: Section "Experiments: negative weight transients of memories"
- Evidence: "Experiments devised to compare the weight of information storage media before and after recording/erasure have been carried out to 10−8 kg accuracy by use of a precision balance, and significant differences—the order of 10−6 kg —have been found"; "negative weight transients ... of the order of 10−5 N (corresponding to a weight of about 1 mg)"; "weight transients observed after writing or secure-erasing information into a memory have not been satisfactorily explained."
- Verified: FULLTEXT
- Notes: The original report is Kish2007gravitational (METADATA only). The phrase "About 17 orders of magnitude" is this work: 1e-6 kg against 2.5e-25 kg per Tb is about 19 orders, and the stated balance accuracy of 1e-8 kg against 2.5e-25 kg is about 17 orders. The tex uses the accuracy comparison.

### C-08-019
- Claim: Vopson (2021) estimated the "information content per particle" as the Shannon entropy of the relative abundances of particle species in baryonic matter. With protons, electrons and neutrons (probabilities 0.466, 0.466, 0.067) this gives 1.288 bits. With up quarks, down quarks and electrons (0.483, 0.29, 0.225) it gives 1.509 bits. The total is ~6 × 10^80 bits in the observable universe.
- Source: Vopson2021estimation
- Locator: Sec. 2, Eqs. (6)-(7); Sec. 3; Abstract (arXiv 2112.04473)
- Evidence: "with the occurrence probabilities Pp+, Pe-, Pn0 = 0.466, 0.466, 0.067"; "we obtain 1.288 bits of information encoded per elementary particle"; "Puq, Pdq, Pe- = 0.483, 0.29, 0.225"; "we obtain 1.509 bits of information encoded per elementary particle"; "there are ~6 × 10^80 bits of information stored in all the matter particles of the observable universe."
- Verified: FULLTEXT
- Notes: The quantity is the entropy of a species label drawn at random from the cosmic mixture. It depends on the composition of the population, not on any property of a single particle (this work, C-08-T07).

### C-08-020
- Claim: Vopson (2021) postulates that information about a particle's mass, charge and spin is stored in the particle itself, like a "particle DNA", and that only stable particles with non-zero rest mass store information.
- Source: Vopson2021estimation
- Locator: Sec. 1-2 (arXiv 2112.04473)
- Evidence: "particles and elementary particles store information about themselves"; "we postulate that information can only be stored in particles that are stable and have a non-zero rest mass"; "these degrees of freedom are embedded within each elementary particle, like an intrinsic label, or 'particle DNA'."
- Verified: FULLTEXT
- Notes: none

### C-08-021
- Claim: The M/E/I programme has been linked to dark matter. Vopson earlier estimated that ~52 × 10^93 bits at 2.735 K would account for the missing dark matter, and in 2021 described this estimate as "most likely overestimated".
- Source: Vopson2021estimation
- Locator: Sec. 1 (arXiv 2112.04473)
- Evidence: "Vopson estimated that around 52 × 10^93 bits would be enough to account for all the missing Dark Matter in the observable universe [22,24]. However, this is most likely overestimated, as he assumed that all the information bits are stored at T = 2.735 K."
- Verified: FULLTEXT
- Notes: Džaferović-Mašić (2021, J. Phys. Conf. Ser., ABSTRACT) reviews "missing information" as a dark matter candidate and mentions proposed ultra-accurate balance and interferometer tests.

### C-08-022
- Claim: Vopson (2022) derives a temperature-dependent "information mass" for a body. For 1 kg of copper heated or cooled by 100 K, with I = 1.509 bits per elementary particle, it gives Δm_inf = 3.33 × 10^-11 kg. The paper asserts that the body's physical mass does not change with temperature.
- Source: Vopson2022experimental
- Locator: Sec. I, Eqs. (1)-(2), p. 035311-2
- Evidence: "For a temperature change ΔT = 100 K of the Cu sample (cooling or heating), using (2) we obtain an absolute value of information mass change of Δminf = 3.33 × 10−11 kg."; "Since the physical mass of the material under test does not change with the temperature (assuming solid materials are thermally and chemically stable), the detected mass change can only be related to the information mass change"
- Verified: FULLTEXT
- Notes: The paper quotes N_b = 29.8 × 10^26 bits for 1 kg Cu. Eq. (1) with the stated inputs gives 3.14 × 10^27. Δm_inf = 3.33e-11 kg is consistent with the latter (this work computes 3.34e-11 kg). Minor internal inconsistency; see report.

### C-08-023
- Claim: Vopson's experimental protocol predicts that electron-positron annihilation emits, besides the two 511 keV photons, two photons carrying the erased information energy, with λ = hc/(I k_B T ln 2). For I = 1.509 bits this is ~50 µm at room temperature, and 25-75 µm for 1-3 bits per particle.
- Source: Vopson2022experimental
- Locator: Abstract; Eqs. (9)-(11); Sec. III, Fig. 2
- Evidence: "At room temperature, a positron–electron annihilation should produce two ∼50 μm wavelength infrared photons due to the information erasure."; "λ = hc / (I kb T ln(2))"; "from 1 to 3 bits per elementary particle, the wavelength at room temperature ranges broadly from 25 to 75 μm."
- Verified: FULLTEXT
- Notes: This work: at T = 300 K and I = 1.509, λ = 45.9 µm and the photon energy is 0.027 eV. For I = 1 and 3, λ = 69 and 23 µm.

### C-08-024
- Claim: The protocol proposes a ^22Na positron source, a thin W(100) moderator, a nm-thin Al target and temperature control. The linear shift of the IR wavelength with sample temperature serves as the main control.
- Source: Vopson2022experimental
- Locator: Sec. IV, Fig. 4; Sec. V
- Evidence: "For our experiment, we propose to use positrons generated by a 22 Na radioactive source."; "We propose to cover the 22 Na source with a thin (1–2 μm) single-crystal tungsten foil in (100) orientation"; "we propose to use a metallic Al thin film as the target material. The thickness of the Al thin film must be in the range of a few nm"; "The main control tool is the fact that the wavelength of the information energy IR photons must shift with the temperature of the sample."
- Verified: FULLTEXT
- Notes: none

### C-08-025
- Claim: The protocol states two assumptions explicitly. The annihilating particles take the temperature of the metal target, and the information energy is released as IR photons rather than by another route (for example, carried by the gamma photons). The author therefore says the experiment could fail even if the conjectures are correct.
- Source: Vopson2022experimental
- Locator: Text after Eq. (9); Sec. V
- Evidence: "Te− = Te+ = T because the positrons will reach thermal equilibrium with the metallic sheet"; "we make a strong assumption that the transfer of the information mass content of the annihilating particles takes place via conversion into IR photons. However, other mechanisms of conversion are possible, including the gamma photons becoming carriers of this excess information energy. Hence, even if the information conjectures are correct, the proposed experiment is, therefore, not totally guaranteed to succeed."
- Verified: FULLTEXT
- Notes: A null result would therefore not falsify M/E/I as formulated.

### C-08-026
- Claim: Vopson (2022) estimates the electron's rest mass to be ~22 × 10^6 times its putative information mass, and concludes that direct mass measurement cannot test the idea.
- Source: Vopson2022experimental
- Locator: Sec. II, after Eq. (5)
- Evidence: "Taking Ie− = 1.288 bits, it results that the rest mass of the electron is ∼22 × 10^6 times larger than its information mass ... this makes the experimental testing impossible via direct mass change measurements."
- Verified: FULLTEXT
- Notes: This work: 9.109e-31/(1.288 × 3.194e-38) = 2.21e7. Consistent.

### C-08-027
- Claim: The proponent acknowledges that M/E/I has not been confirmed empirically.
- Source: Vopson2022second; Vopson2025response
- Locator: Vopson2022second Sec. I; Vopson2025response Sec. 5
- Evidence: "The M-E-I equivalence principle ... still awaits an experimental confirmation." (Vopson2022second); "the Mass-Energy-Information equivalence principle [7], which has no empirical validation yet." (Vopson2025response)
- Verified: FULLTEXT
- Notes: Our search found no reported execution of the annihilation experiment and no weighing at the required sensitivity (report, Sec. 3).

### C-08-028
- Claim: Vopson (2020) extrapolated M/E/I to predict that, at 20% annual growth of data production, digital content would exceed half of Earth's mass after ~500 years.
- Source: Vopson2020information
- Locator: Abstract (published version)
- Evidence: "after ∼500 years from now, the digital content will account for more than half Earth's mass, according to the mass-energy–information equivalence principle."
- Verified: ABSTRACT
- Notes: The arXiv v1 abstract gives different year estimates from the published abstract. We quote the published one.

### C-08-029
- Claim: Burgin and Mikkilineni (2022) argue, within the "general theory of information", that information is not physical in itself. Its physical representations have mass, and different representations of the same information can have different masses, so M/E/I is not valid as stated.
- Source: Burgin2022is
- Locator: Abstract; Sec. 3 (discussion of Vopson's Formula (6))
- Evidence: "a bit of information does not have mass, but the physical structure that represents the bit indeed has mass."; "the mass-energy–information equivalence conjectured by Vopson in [11] is not valid because the same portion of information can have different physical representations."
- Verified: FULLTEXT
- Notes: Peer-reviewed (MDPI Information). The argument is conceptual, not thermodynamic. The authors state they do not argue against Landauer's principle.

### C-08-030
- Claim: Lairez (2024) argues that for a system of non-interacting entities at constant temperature the internal energy is constant. The energy TΔS associated with a change of entropy is therefore exchanged with the surroundings as work and heat and cannot correspond to a change in the system's rest mass.
- Source: Lairez2024on
- Locator: Abstract; Sec. I.B "Entropic forces" (arXiv 2401.15104v1)
- Evidence: "for a thermodynamic system made of non interacting entities at constant temperature, the internal energy is also constant. So that, the energy involved in a variation of entropy (T ΔS) differs from a change in potential energy stored or released and cannot be associated to a corresponding variation of mass of the system"; "any monothermal variation of entropy interpreted in terms of potential energy stored under the form of rest mass cannot be localized in such a system, but only in its surroundings."
- Verified: FULLTEXT
- Notes: Peer-reviewed (Entropy 26, 337). The same abstract also says thermal energy ("temperature") is not stored as rest mass. That is not the standard relativistic treatment of a composite body's invariant mass, and our section does not rely on it.

### C-08-031
- Claim: Lairez further argues that under M/E/I, erasing the same bit twice should produce a mass change only the first time, and that making an independent copy before erasing would not change the physical outcome of the erasure. He concludes that any mass change would have nothing to do with the logical loss of information.
- Source: Lairez2024on
- Locator: Sec. III (hard-drive and double-erase thought experiments)
- Evidence: "According to the mass-energy-information equivalence principle, a mass defect should be observed in the first stage, while it should not be observed in the second."; "If there is a mass defect, it has nothing to do with logical irreversibility nor with information that would be lost or not."
- Verified: FULLTEXT
- Notes: Lairez also rejects Landauer's principle as a general principle (Sec. II), a minority position. We report his mass argument separately from that position.

### C-08-032
- Claim: A 2024 review of the Landauer bound by Bormashenko records that M/E/I "was criticized recently" and summarizes Lairez's three objections.
- Source: Bormashenko2024landauer
- Locator: Sec. 2.7 and the section on criticism (Europe PMC PMC11119825)
- Evidence: "The mass–energy–information equivalence principle, summarized by Equations (19) and (20), was criticized recently [116]. In particular, Lairez argued that (i) isothermal variation in the entropy-rooted part of the free energy of a body (namely, T Δ S) is not accompanied by any variation in its mass, (ii) the Landauer–Bennet idea is not a general principle and is only true in a particular case, and (iii) the link between information and energy is valid only for fresh information about a dynamic system."
- Verified: FULLTEXT
- Notes: Bormashenko is otherwise sympathetic to "it from bit" readings of Landauer.

### C-08-033
- Claim: Einstein's 1905 conclusion, as summarized by Okun, is that the mass of a body is a measure of its energy content (rest energy E_0 = mc^2).
- Source: Okun2008einstein
- Locator: Sec. on Einstein's 1905 papers (arXiv 0808.0437, p. 4)
- Evidence: "this immediately implies that the mass of the body decreased by the amount L/V^2. From this Einstein concluded that 'The mass of a body is a measure of its energy content'"
- Verified: FULLTEXT
- Notes: Used for C-08-T05 and C-08-T06. We could not reach the original 1905 paper (publisher 403).

### C-08-034
- Claim: The NIST Chemistry WebBook gives Shomate heat-capacity parameters for solid copper (298-1358 K, from the NIST-JANAF tables). They imply C_p(298 K) ≈ 24.5 J mol^-1 K^-1 and an enthalpy increment of 2.49 kJ/mol between 300 and 400 K.
- Source: NIST2026copper
- Locator: "Solid Phase Heat Capacity (Shomate Equation)" table
- Evidence: "A 17.72891 B 28.09870 C -31.25289 D 13.97243 E 0.068611 F -6.056591 G 47.89592 H 0.000000 Reference Chase, 1998"
- Verified: FULLTEXT
- Notes: C_p and ΔH are computed by this work from the listed parameters using the WebBook's Shomate formulas. ΔH(300→400 K) = 2489 J/mol = 3.92 × 10^4 J/kg.

## C. The "second law of infodynamics"

### C-08-035
- Claim: Vopson and Lepadatu define the "entropy of information-bearing states" as S_inf = N k_B ln 2 H(X), where N is the number of information-bearing states and H(X) is the Shannon entropy of the symbol frequencies. For the 88-bit ASCII encoding of "INFORMATION" they obtain H = 0.991.
- Source: Vopson2022second
- Locator: Sec. II, Eqs. (2)-(5)
- Evidence: "Sinf = kb ⋅ ln Ω = N ⋅ kb ⋅ ln 2 ⋅ ∑ pj ⋅ log2 (1/pj)"; "Counting the occurrences of 0 and 1 s, we get 49 and 39, respectively."; "the Shannon entropy function is just under 1 bit ... = 0.991."
- Verified: FULLTEXT
- Notes: H is computed from the frequencies in a single string, i.e. a zeroth-order (plug-in) estimate. It is not an entropy of a physical ensemble.

### C-08-036
- Claim: In the digital example, a micromagnetic Monte Carlo simulation of a granular film shows the written bits self-erasing by thermal relaxation. The authors conclude that because N falls, S_inf decreases, and they state the law ∂S_inf/∂t ≤ 0. They say this decrease must be compensated by an increase in physical entropy.
- Source: Vopson2022second
- Locator: Sec. III, Eqs. (6)-(7), Fig. 2
- Evidence: "after a sufficiently long time, we expect magnetic grains to lose their magnetization state, leading to magnetic bit states undergoing self-erasure, and, therefore, reducing the information states N."; "when the entropy of the information bearing states is examined independently, we conclude that the second law manifests in reverse so that the information entropy stays constant or decreases."; "the entropy reduction in the information states must be compensated by an entropy increase in the physical states, via a dissipation mechanism."
- Verified: FULLTEXT
- Notes: The printed anisotropy constant, 8.75 × 10^8 J/m^3, is inconsistent with the stated K_aV/k_BT and τ = 1.5 s, which imply 8.75 × 10^7 J/m^3 (this work; see report).

### C-08-037
- Claim: In the genetic example, the authors compute the Shannon entropy of nucleotide composition for ten SARS-CoV-2 genomes of identical length (29,903 nt), selected from NCBI with increasing numbers of SNPs (0-49) over 22 months. H falls from 1.9570243 to 1.9562614 bits, "rather linearly" in time (coefficient of determination 97%).
- Source: Vopson2022second
- Locator: Sec. IV, Table I, Fig. 3
- Evidence: "By searching for complete genome sequences, containing the same number of nucleotides as the reference sequence, we carefully selected variants that displayed an incremental number of SNP mutations with time"; Table I values "1.957 024 3 ... 1.956 261 4"; "decreases rather linearly over time (Fig. 3, top graph, COD = 97%)."
- Verified: FULLTEXT
- Notes: The ten accessions are listed in Table I (MN908947 ... OL351371.1).

### C-08-038
- Claim: Vopson and Lepadatu interpret the genomic trend as pointing to a possibly deterministic, entropy-driven process for genetic mutations. They also list open questions, including the relation to relaxation and observation times and fluctuations.
- Source: Vopson2022second
- Locator: Sec. IV end; Sec. V
- Evidence: "it also points to a possible deterministic approach to genetic mutations, currently believed to be just random events."; "We also do not explain how the second law of infodynamics relates to the relaxation times of the information states and the observation time, nor do we address the question of the possible existence of fluctuations of information states"
- Verified: FULLTEXT
- Notes: A companion paper (Vopson2022possible, ABSTRACT) proposes a "governing law of genetic mutations ... driven by a tendency to reduce their overall information entropy".

### C-08-039
- Claim: Vopson (2023) extends the second law of infodynamics to digital and genetic information, atomic physics, mathematical symmetries and cosmology, and says it provides evidence that "appears to underpin" the simulated-universe hypothesis.
- Source: Vopson2023second
- Locator: Abstract
- Evidence: "we re-examine the second law of infodynamics and its applicability to digital information, genetic information, atomic physics, mathematical symmetries, and cosmology, and we provide scientific evidence that appears to underpin the simulated universe hypothesis."
- Verified: ABSTRACT
- Notes: The specific applications (Hund's rules; symmetry as low information entropy) are restated in full text in Vopson2025is, Sec. I: "explaining ... the rules followed by the electrons in populating atomic orbitals"; "high symmetry corresponds to a low information entropy content".

### C-08-040
- Claim: The cosmological derivation of the law assumed that an adiabatically expanding universe has dQ = T dS = 0 and hence constant total entropy, so that growth in physical entropy must be balanced by a fall in information entropy. After private criticism that dQ = T dS holds only for reversible processes, Vopson (2025) proposed a modified argument with added "loss" terms.
- Source: Vopson2025on
- Locator: Secs. 1-3, Eqs. (2)-(13)
- Evidence: "The main criticism of this approach was the fact that we used the relation dQ = TdS = 0, which in reality is only valid for reversible processes."; "Considering that the entropy budget of the universe contains an unaccounted entropy term ... It was proposed that the missing entropy term is the entropy associated with the information content of the universe"
- Verified: FULLTEXT
- Notes: Published as a "News and Views" item in IPI Letters (see C-08-046 on review status). The modified argument assumes, among other things, that the "loss" term decreases over time and that T is approximately constant.

### C-08-041
- Claim: In "Is gravity evidence of a computational universe?", Vopson models space as Planck-area cells storing 0 (empty) or 1 (occupied), and computes H from the occupied fraction. Four particles in 100 cells give H = 0.242 bits; merged into one cell they give 0.081 bits. From these he derives an entropic force, and obtains F = GMm/R^2 by setting ΔS_inf = k_B ln2 H per step Δr = ħ/(mc), M = N H k_B T ln 2/c^2 and N ≈ R^2/L_p^2.
- Source: Vopson2025is
- Locator: Sec. II (Fig. 1); Secs. III-IV, Eqs. (2), (6)-(15)
- Evidence: "the probability distribution is P = {4/100, 96/100}, and using (1), we calculate the information entropy of the system as H(X) = 0.242 bits"; "the final system will contain N0 = 99 and N1 = 1, giving a Shannon information entropy of H(X) = 0.081 bits"; "Δr ≈ λ = ħ/mc"; "M = NH(X) kb T ln(2)/c^2"; "N ≈ R^2/Lp^2 ... FS = G Mm/R^2."
- Verified: FULLTEXT
- Notes: This work checked H(0.04) = 0.2423 and H(0.01) = 0.0808.

### C-08-042
- Claim: Vopson (2025) presents gravity as "data compression and computational optimization", which "supports the possibility of a simulated or computational universe".
- Source: Vopson2025is
- Locator: Abstract; Sec. II
- Evidence: "This is another example of data compression and computational optimization in our universe, which supports the possibility of a simulated or computational universe."
- Verified: FULLTEXT
- Notes: The conclusion adds: "Whether the universe is indeed a computational construct remains an open question".

## D. Critiques, replies, independent re-analyses

### C-08-043
- Claim: In a YouTube commentary, Hossenfelder argued that the Shannon entropy of a binary distribution is unchanged when 0s and 1s are swapped and is maximal for equal numbers. She said the paper's reasoning "makes no sense at all" and that it "shouldn't have been published".
- Source: Hossenfelder2025gravity; Vopson2025response
- Locator: Vopson2025response, Appendix (transcript)
- Evidence: "you should get the same entropy or information if you swap out the ones and zeros so you could take that to also argue that matter wants to spread out."; "The entropy is maximal if there are approximately the same numbers of zero and ones"; "This paper has multiple mathematical problems and I think it shouldn't have been published."
- Verified: FULLTEXT
- Notes: FULLTEXT refers to the transcript as reproduced by Vopson in IPI Letters. We checked the video's title and channel through YouTube oEmbed, but did not transcribe the video ourselves. This is an informal (non-peer-reviewed) critique.

### C-08-044
- Claim: Vopson's reply says the video gives no explicit mathematical rebuttal. It argues that bit values acquire meaning once an encoding is fixed, and that clustering reduces the number of "1" cells, which is analogous to data compression.
- Source: Vopson2025response
- Locator: Secs. 1-2, 5
- Evidence: "Hossenfelder's video provides no explicit mathematical rebuttal, specific citations, or reproducible counter-examples"; "once a data encoding scheme and semantics are fixed, bit values acquire physical meaning."; "Clustering matter reduces the number of '1' states and therefore reduces entropy under his definition. This is analogous to data compression."
- Verified: FULLTEXT
- Notes: none

### C-08-045
- Claim: IPI Letters, where the reply and the cosmological-derivation note appeared, is the journal of the Information Physics Institute, and Vopson is its Editor-in-Chief. The journal states that its "News and Views" and communication items are screened at editorial level rather than going through the usual peer review.
- Source: Vopson2025response; Vopson2025on
- Locator: IPI Letters "About" and "Editorial Team" pages (ipipublishing.org, accessed 2026-09-27); article headers ("News and Views")
- Evidence: "Editor-in-Chief Dr Melvin M. Vopson"; "we also offer the opportunity to publish less developed research studies, bold ideas, opinions, news and views that do not undergo the usual peer-review process and are just screened at the editorial level."
- Verified: FULLTEXT
- Notes: The response was "Received: 2025-05-28 Accepted: 2025-05-29 Published: 2025-05-30" (article header).

### C-08-046
- Claim: Crecraft (Entropy, 2025) attributes the decline in the magnetic-storage example to the ordinary second law of thermodynamics. He argues that the statistical "information entropy" used is observer-dependent and ill-suited to define a physical law, notes that unbiased random mutations would be expected to increase it, and proposes a "thermocontextual" reformulation.
- Source: Crecraft2024second
- Locator: Sec. 1 (Introduction); Sec. 5 discussion of Corollary 5-4 (PMC11765112)
- Evidence: "It is clear that statistical entropy is subjectively based on an observer's prior knowledge or on arbitrary assumptions. It is ill defined, and it is not suitable to define a physical law."; "Unbiased random mutations by themselves would be expected to increase a system's information entropy."; "The magnetic storage device's entropy decline in their first example is instead a consequence of Corollary 4-1 (Second Law of thermodynamics)."
- Verified: FULLTEXT
- Notes: Crossref year 2024 (online 30 Dec 2024), volume 27 (2025). The reformulated law ("an external agent seeks to increase its access to exergy by narrowing its information gap") differs substantially from the original.

### C-08-047
- Claim: Ostrowski, Ozimek and Fornalski (2024) fitted linear trends of nucleotide-composition entropy against mutation number for NCBI data comprising 8.8 million SARS-CoV-2, 1.1 million HIV and 1 million influenza entries. All slopes were negative. For SARS-CoV-2 they found A = (-0.972 ± 0.018) × 10^-5 (least squares, χ^2 = 7.6 × 10^7) and (-1.146 ± 0.421) × 10^-5 (robust Bayesian regression). They describe this as confirming Vopson's hypothesis.
- Source: Ostrowski2024entropy
- Locator: Sec. 2; Table I; Sec. 5
- Evidence: "The database contains 8.8 million entries for SARS-CoV-2, 1.1 million for HIV and 1 million for influenza."; Table I "SARS-CoV-2 A = (−0.972 ± 0.018) × 10−5 χ2 = 7.6 × 107 A = (−1.146 ± 0.421) × 10−5"; "The presented analysis fully confirmed the results of Vopson and his colleagues"
- Verified: FULLTEXT
- Notes: Robust-regression slopes for HIV, (-0.433 ± 0.338) × 10^-5, and influenza, (-1.725 ± 1.245) × 10^-5, lie within 1.3σ and 1.4σ of zero (this work, from Table I; uncertainties are 1σ per the caption). The authors interpret the decrease through Prigogine-Onsager nonequilibrium thermodynamics and do not test a mutation-bias null model.

### C-08-048
- Claim: Todd (2026) reinterprets Vopson's information entropy as "structure-information", the relative entropy of a distribution to isotropic equilibrium. Its decrease then follows from thermodynamic relaxation, with the second law of thermodynamics intact.
- Source: Todd2026thermodynamic
- Locator: Abstract; Sec. "Relation to Vopson's Framework"
- Evidence: "We interpret this information entropy as structure-information: the relative entropy Istruct = DKL(p∥piso) measuring a distribution's departure from isotropic equilibrium."; "This does not contradict the second law of thermodynamics—thermodynamic entropy increases in the bath precisely because structure-information is being dissipated."
- Verified: FULLTEXT
- Notes: Published as an "Article" in IPI Letters.

### C-08-049
- Claim: Kubiński, Ostrowski and Fornalski (2024) found a U-shaped evolution of Shannon entropy of the neutron-source distribution in simulated deep-burnup fuel: an initial decrease, a minimum at ~45 years, then an increase. They compare the quasi-linear decrease to the viral results.
- Source: Kubinski2024shannon
- Locator: Abstract; Sec. 4.2 (PMC11675148)
- Evidence: "The results show a 'U-shaped' entropy evolution: an initial decrease due to self-organization, followed by stabilization and eventual increase due to degradation. A minimum entropy state is reached after approximately 45 years"; "regularly multiplying systems exhibit a linear decrease in entropy ... This was previously observed for viruses [17,18,19]."
- Verified: FULLTEXT
- Notes: The late-time increase is not the monotonic ∂S_inf/∂t ≤ 0 behaviour.

### C-08-050
- Claim: Simmonds (2020) found that almost half of early SARS-CoV-2 sequence changes (38-42% across data sets) were C→U transitions, with an 8-fold base-frequency-normalized C→U/U→C asymmetry attributed to an APOBEC-like host editing process. The genome contains about twice as many U as C (32.1% vs 18.4%). Long-term C→U hypermutation has been proposed as the cause of the U ≫ A > G ≫ C base asymmetry of other human coronaviruses.
- Source: Simmonds2020rampant
- Locator: Abstract; Results (transition frequencies); Discussion (PMC7316492)
- Evidence: "Almost one-half of sequence changes were C→U transitions, with an 8-fold base frequency normalized directional asymmetry between C→U and U→C substitutions."; "These accounted for 38% to 42% of all changes in the four SARS-CoV-2 data sets."; "there was an almost 2-fold greater number of U bases in the SARS-CoV-2 genome than Cs (32.1% compared to 18.4%, respectively)"; "Marked base asymmetries observed in nonpandemic human coronaviruses (U ≫ A > G ≫ C) and low G+C contents may represent long-term effects of prolonged C→U hypermutation in their hosts."
- Verified: FULLTEXT
- Notes: This is the known mutational process behind C-08-T02 and C-08-T03.

### C-08-051
- Claim: The standard plug-in (maximum-likelihood) entropy estimator is biased downward. The Miller-Madow correction adds (m̂ - 1)/(2N) nats, and bias-corrected estimators can still fail in undersampled regimes.
- Source: Paninski2003estimation; Nemenman2002entropy
- Locator: Paninski2003estimation Sec. 2 (list of estimators), Abstract; Nemenman2002entropy Eq. (10)
- Evidence: "The MLE with the so-called Miller-Madow bias correction (Miller, 1955), Ĥ_MM(p_N) ≡ Ĥ_MLE(p_N) + (m̂ − 1)/2N" (Paninski); "information estimates in a certain data regime are likely contaminated by bias, even if 'bias-corrected' estimators are used" (Paninski, Abstract); "it is well known that S_ML always underestimates the actual value of the entropy" (Nemenman et al.)
- Verified: FULLTEXT
- Notes: The NSB estimator is introduced in Nemenman2002entropy.

## E. This work (independent technical assessment)

### C-08-T01
- Claim: We downloaded the ten accessions of Vopson and Lepadatu's Table I from NCBI and reproduced all ten published entropies to seven decimals, using the plug-in Shannon entropy of A/C/G/T counts. All ten sequences have length 29,903 and contain no ambiguous bases.
- Source: this work (data: Vopson2022second, Table I; NCBI nuccore)
- Locator: report Sec. 4.1; scripts in /tmp/claude-0/papers/sars/analyze.py, analyze2.py
- Evidence: e.g. MN908947.3 counts A 8954, C 5492, G 5863, T 9594 → H = 1.9570243; OL351371.1 counts A 8954, C 5470, G 5856, T 9623 → H = 1.9562614 (published: 1.957 024 3 and 1.956 261 4)
- Verified: FULLTEXT
- Notes: FULLTEXT here means the computation reproduces the published values exactly.

### C-08-T02
- Claim: Relative to the reference, the most mutated genome (OL351371.1) has 22 of its 49 position-wise differences as C→U. 41 of the 49 move a site from a rarer to a more common nucleotide. U content rises by 29 and C content falls by 22.
- Source: this work (data: NCBI; frequencies consistent with Simmonds2020rampant)
- Locator: report Sec. 4.1
- Evidence: substitution counts OL351371.1 vs MN908947.3: C>T 22, G>T 9, G>A 5, A>G 4, T>C 3, A>T 2, C>G 2, T>G 1, C>A 1
- Verified: FULLTEXT
- Notes: A position-wise comparison is valid here because all sequences have identical length. For two sequences our difference counts (10, 41) differ by one from the published SNP counts (9, 40).

### C-08-T03
- Claim: To first order, moving one site of a length-N sequence from base a to base b changes the composition entropy by ΔH ≈ N^-1 log2(p_a/p_b). With the reference composition this is -2.69 × 10^-5 bits for C→U and +2.69 × 10^-5 bits for U→C. Under a null model with sites chosen uniformly and targets uniform among the other three bases, the expected change is +3.9 × 10^-6 bits per substitution, i.e. an increase. The published decrease (-1.56 × 10^-5 bits per SNP on average) therefore follows from the known C→U-dominated mutational spectrum and does not require a new law.
- Source: this work (definition of H from Vopson2022second Eq. (2); spectrum from Simmonds2020rampant)
- Locator: report Sec. 4.1
- Evidence: computed values; (1.9562614 - 1.9570243)/49 = -1.56e-5
- Verified: FULLTEXT
- Notes: This agrees with Crecraft's qualitative remark that unbiased mutations would raise the entropy (C-08-046).

### C-08-T04
- Claim: For fixed N = 29,903 and four symbols, the Miller-Madow correction adds a constant 7.2 × 10^-5 bits and cannot change the trend. The block (conditional) entropies of order 2 and 3 also decline overall (not strictly monotonically) from the reference to the most mutated genome. General-purpose compressors (lzma, bz2, zlib) have a resolution of about 2.7 × 10^-4 bits per base at this length and show no monotonic trend.
- Source: this work (estimators per Paninski2003estimation)
- Locator: report Sec. 4.1
- Evidence: H_cond2 1.925237 → 1.924579; H_cond3 1.918212 → 1.917682 (MN908947.3 → OL351371.1); lzma bits/base fluctuate 2.258-2.262 non-monotonically
- Verified: FULLTEXT
- Notes: Exploratory only. The estimator is not the main issue for this dataset; the interpretation and the null model are.

### C-08-T05
- Claim: Vopson's Eq. (2) for copper implies an information contribution to the heat capacity of I(N_e + 3(N_p + N_n)) k_B ln 2 per atom, which is 1.9 kJ mol^-1 K^-1, about 78 times the measured C_p of 24.5 J mol^-1 K^-1. Equivalently, the predicted Δm_inf c^2 = 3.0 MJ for 1 kg and ΔT = 100 K, against a measured enthalpy increment of 39 kJ. If the information mass carries energy E = mc^2 and energy is conserved, standard calorimetry already rules out the prediction by nearly two orders of magnitude.
- Source: this work (inputs: Vopson2022experimental Eqs. (1)-(2); NIST2026copper; Okun2008einstein)
- Locator: report Sec. 4.2
- Evidence: 1.509 × 219.5 × k_B ln2 × N_A = 1909 J mol^-1 K^-1; Δm_inf c^2 = 3.33e-11 kg × c^2 = 2.99e6 J; ΔH(300→400 K) = 3.92e4 J/kg
- Verified: FULLTEXT
- Notes: The standard mass-energy increase of the heated block, ΔH/c^2 = 4.4 × 10^-13 kg, is ~80 times smaller than the predicted Δm_inf. This contradicts the protocol's premise that the physical mass does not change with temperature, although the correction is small in absolute terms. A proponent could respond that information energy is not supplied by the heater, but the papers do not specify any other energy source.

### C-08-T06
- Claim: For a memory whose two logical states have equal energy (Landauer's symmetric well), a bit known to be in one well and the thermalized bit have the same mean energy. The first differs from the second only by an excess nonequilibrium free energy T·I = k_B T ln 2, which is entropic. With m = E/c^2 the stored bit then carries no extra rest mass. The k_B T ln 2 dissipated on erasure is supplied as work by the eraser and leaves as heat.
- Source: this work (from Landauer1961irreversibility C-08-005; Esposito2011second C-08-012; Kish2013does C-08-017; Jun2014high C-08-009; Bennett2003notes C-08-006; Okun2008einstein C-08-033)
- Locator: report Sec. 4.3
- Evidence: For ρ localized with equal weight on one of two symmetric wells, D[ρ||ρ_eq] = ln 2 (k_B = 1). E(ρ) = E(ρ_eq) by symmetry (Kish and Granqvist: "the energy and the mass of the system after the operation remain the same").
- Verified: FULLTEXT
- Notes: This is the same conclusion Lairez reaches by other means (C-08-030). For asymmetric memories a mass difference of either sign exists, set by the device's energy asymmetry rather than by k_B T ln 2 (Kish2013does).

### C-08-T07
- Claim: The "information per particle" of 1.288 or 1.509 bits (C-08-019) is the entropy of the species mix in a population, not a property of any single particle. For example, a pure-hydrogen population (p and e in equal numbers) gives exactly 1 bit per particle under the same procedure. The IR-photon prediction of C-08-023 inherits this dependence.
- Source: this work (on Vopson2021estimation Eqs. (6)-(7))
- Locator: report Sec. 4.4
- Evidence: H(1/2, 1/2) = 1 bit
- Verified: FULLTEXT
- Notes: none

### C-08-T08
- Claim: In the gravity model, H(X) depends only on the counts (N_0, N_1), so it is invariant under any rearrangement of cell contents. Moving a particle through empty cells leaves H unchanged, and only merging changes it. The 1/R^2 dependence enters through the identifications Δr = ħ/(mc), M = N H k_B T ln2/c^2 and N ≈ R^2/L_p^2 (Eqs. (9), (12), (14)-(15)), not through a configuration-dependent entropy.
- Source: this work (on Vopson2025is)
- Locator: report Sec. 4.5
- Evidence: Eq. (1) of Vopson2025is is a function of p_0 = N_0/N only; Eq. (11) sets ΔS_inf = k_B ln(2) H(X) under the stated condition H_N = H_{N-1}
- Verified: FULLTEXT
- Notes: This sharpens, and differs from, the swap-symmetry point in C-08-043.

### C-08-T09
- Claim: In the digital example, standard accounting says thermal relaxation of N stored bits raises the entropy of the information-bearing degrees of freedom by up to N k_B ln 2 (Landauer). What falls is the relative entropy (information) that the medium retains about the written record. For undriven relaxation at fixed Hamiltonian (W = 0, ΔF_eq = 0), Esposito and Van den Broeck's Eq. (12) gives ΔI = -Δ_iS ≤ 0. The reported decrease is therefore the ordinary second law expressed as loss of information, consistent with Crecraft and Todd.
- Source: this work (from Landauer1961irreversibility C-08-003; Esposito2011second C-08-012; Crecraft2024second C-08-046; Todd2026thermodynamic C-08-048)
- Locator: report Sec. 4.3
- Evidence: see cited claims
- Verified: FULLTEXT
- Notes: none

### C-08-T10
- Claim: We are not aware of any reported execution of Vopson's annihilation protocol, or of any weighing of storage media, samples or particles with the sensitivity required to test M/E/I directly.
- Source: this work (search log in report Sec. 3)
- Locator: report Sec. 3
- Evidence: Semantic Scholar citations of Vopson2022experimental (27 citing items, none experimental); Crossref and web searches
- Verified: FULLTEXT
- Notes: "FULLTEXT" refers to our search record. The claim is phrased as "we are not aware".
