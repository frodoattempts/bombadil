# Claim ledger: 05-holographic

Topic: finite information density of space (holographic bounds) and interferometric
searches for Planckian "holographic noise".

All FULLTEXT entries were checked against the arXiv PDF (text extracted with
`pdftotext`, PDFs in `/tmp/claude-0/papers/`). Where `pdftotext` dropped a
mathematical symbol (usually a square root), the restored symbol is shown in
square brackets inside the quote and the restoration was checked against the
equation it comes from. Version checked is noted where it matters.

---

## A. Information bounds (context for "resolution" of any substrate)

### C-05-001
- Claim: Bekenstein argued, from the generalized second law (GSL), that a weakly gravitating system of energy E and size R in asymptotically flat space obeys S_matter <= 2 pi E R (Planck units, k = hbar = c = 1).
- Source: Bousso2002holographic (secondary account of Bekenstein1981universal)
- Locator: Sec. II.B, Eq. (2.20)
- Evidence: "For any weakly gravitating matter system in asymptotically flat space, Bekenstein (1981) has argued that the GSL implies the following bound: Smatter ≤ 2πER."
- Verified: FULLTEXT (Bousso); METADATA (Bekenstein1981universal, PRD 23, 287; publisher PDF paywalled, APS returned 403)
- Notes: The primary source was not read. The .tex attributes the bound to Bekenstein and cites Bousso for its statement.

### C-05-002
- Claim: Whether the GSL actually implies the Bekenstein bound is described by Bousso as controversial.
- Source: Bousso2002holographic
- Locator: Sec. II.B (after Eq. 2.21)
- Evidence: "The question of whether the GSL implies the Bekenstein bound remains controversial (see, e.g., Bekenstein, 1999, 2001; Pelath and Wald, 1999; Wald, 2001; Marolf and Sorkin, 2002)."
- Verified: FULLTEXT
- Notes:

### C-05-003
- Claim: Bousso's review summarizes the holographic entropy bound as a limit on the information content of the spacetime regions adjacent to a surface, at 1.4 x 10^69 bits per square metre, and the holographic principle as the claim that this bound must originate in the fundamental degrees of freedom of a quantum theory of gravity.
- Source: Bousso2002holographic
- Locator: Abstract; Sec. I.A
- Evidence: "There is strong evidence that the area of any surface limits the information content of adjacent spacetime regions, at 1.4 × 10^69 bits per square meter." / "The holographic principle asserts that this bound is not a coincidence, but that its origin must be found in a new theory."
- Verified: FULLTEXT
- Notes: The general form is the covariant (light-sheet) entropy bound, a conjecture supported by examples and by partial proofs under stated assumptions.

### C-05-004
- Claim: A local field theory on a Planck-scale grid (one oscillator of n states per Planck volume) would give about n^V states, i.e. a number of degrees of freedom that scales with volume, whereas the spherical entropy bound gives e^{A/4} states; Bousso stresses the conflict between the two counts.
- Source: Bousso2002holographic
- Locator: Sec. III.C, Eqs. (3.2), (3.7)
- Evidence: "So let us discretize space into a Planck grid and assume that there is one oscillator per Planck volume. ... Hence, the total number of independent quantum states in the specified region is N ∼ n^V." / "The result obtained from the spherical entropy bound is thus at odds with the much larger number of degrees of freedom estimated from local field theory."
- Verified: FULLTEXT
- Notes: This is the precise sense in which a "voxel" (volume-pixel) simulation overcounts relative to holography.

### C-05-005
- Claim: 't Hooft argued that reconciling gravitational collapse with quantum mechanics implies that the observable degrees of freedom are best described as Boolean variables on a two-dimensional lattice, with about one Boolean variable per Planckian surface element.
- Source: tHooft1993dimensional
- Locator: Abstract; p. 6 (text around Eq. 3)
- Evidence: "the observable degrees of freedom can best be described as if they were Boolean variables defined on a two-dimensional lattice, evolving with time." / "One Boolean variable per Planckian surface element should suffice."
- Verified: FULLTEXT
- Notes: arXiv v2 (2009 replacement of the 1993 essay).

### C-05-006
- Claim: 't Hooft compared the situation to a hologram and stated that the resulting "blurring" of the three-dimensional image is small compared with ordinary quantum-mechanical uncertainties.
- Source: tHooft1993dimensional
- Locator: p. 6
- Evidence: "The situation can be compared with a hologram of a three dimensional image on a two-dimensional surface. The image is somewhat blurred because of limitations of the hologram technique, but the blurring is small compared to the uncertainties produced by the usual quantum mechanical fluctuations."
- Verified: FULLTEXT
- Notes: Relevant contrast with Hogan's later proposal that holographic blurring could be macroscopically large (C-05-012 ff.). We do not claim 't Hooft commented on Hogan.

### C-05-007
- Claim: 't Hooft noted that the discreteness of surface degrees of freedom "strongly reminds" one of a 2+1-dimensional cellular automaton, while flagging this as speculation.
- Source: tHooft1993dimensional
- Locator: p. 7
- Evidence: "The discreteness of our degrees of freedom on the two-surface strongly remind us of a 2+1 dimensional cellular automaton. But this would constitute a speculation on"
- Verified: FULLTEXT
- Notes: Cross-link: digital-physics/cellular-automaton section.

### C-05-008
- Claim: Susskind recast 't Hooft's proposal as a two-dimensional "screen" of "pixels", each storing one bit, with one discrete degree of freedom per Planck area sufficing to describe three-dimensional phenomena.
- Source: Susskind1995world
- Locator: Abstract; Sec. 1
- Evidence: "The two dimensional description only requires one discrete degree of freedom per Planck area and yet it is rich enough to describe all three dimensional phenomena." / "I will refer to such a two dimensional surface as a “screen” and its discrete lattice sites as “pixels”. A pixel can only store one bit of information"
- Verified: FULLTEXT
- Notes: The "pixel" vocabulary in the holography literature originates here as a heuristic, not as a claim about computation.

### C-05-009
- Claim: Lloyd estimated that the universe can have performed no more than about 10^120 elementary operations on about 10^90 bits (about 10^120 bits if gravitational degrees of freedom are included).
- Source: Lloyd2002computational
- Locator: Abstract; p. 3
- Evidence: "The universe can have performed no more than 10^120 ops on 10^90 bits." / "total number of bits (≈ 10^90 in matter, ≈ 10^120 if gravitation is taken into account)"
- Verified: FULLTEXT
- Notes: Included only for scale; Section 02 treats Lloyd in depth.

### C-05-010
- Claim: Vazza used the holographic bound to estimate a maximum information content of about 3.5 x 10^124 bits for the observable Universe and concluded that simulating the entire visible Universe down to the Planck scale is physically impossible with the energy available within it.
- Source: Vazza2025astrophysical
- Locator: Sec. 3.1, Eqs. (8)-(11)
- Evidence: "IU ∼ 3.5 · 10^124 bits" / "This leads to the FIRST CONCLUSION: simulating the entirety of our visible Universe at full resolution (i.e. down to the Planck scale) is physically impossible."
- Verified: FULLTEXT
- Notes: Conclusion depends on assumptions (simulator shares our physics; Landauer cost at T_CMB; Planck-scale resolution). Cross-link to Section 02 (computational resources).

### C-05-011
- Claim: Vazza notes that the holographic principle already gives a low information budget compared with volume-scaling estimates, and that a coarse-grained description of the cosmic web requires vastly fewer bits, so the conclusion hinges on the assumed resolution.
- Source: Vazza2025astrophysical
- Locator: Sec. 4.4
- Evidence: "the HP prescribes the maximum information content to scale with the surface, and not the volume, of a system: hence it generally already provides a very low information budget estimate" / "the statistical evolution of the cosmic web within the observable Universe can be encoded by using (only) ∼ 4 · 3 · 10^16 bits of information."
- Verified: FULLTEXT
- Notes:

## B. Hogan's holographic-noise proposal and the GEO600 episode

### C-05-012
- Claim: Hogan (2008) proposed "holographic noise": a quantum indeterminacy of transverse position, derived from the limits of measurement with Planck-wavelength radiation, with a transverse shear signature and a flat power spectral density equal to the Planck time, predicted with no free parameters.
- Source: Hogan2008measurement
- Locator: Abstract; Sec. II
- Evidence: "The indeterminacy predicts fluctuations from a classically defined geometry in the form of “holographic noise” whose spatial character, absolute normalization, and spectrum are predicted with no parameters. The noise has a distinctive transverse spatial shear signature, and a flat power spectral density given by the Planck time."
- Verified: FULLTEXT
- Notes: arXiv v5 (24 Mar 2008). Hogan states the noise "is not derived here from a fundamental theory".

### C-05-013
- Claim: Hogan normalized the noise as a lower bound tied to covariant entropy bounds, using Nyquist-Shannon sampling with one degree of freedom per 2 l_P in each transverse direction, so that an experimental upper bound on the noise would imply a lower bound on the density of independent position states.
- Source: Hogan2008measurement
- Locator: Sec. III ("Lower Bound on Holographic Noise from Upper Bound on Gravitational Entropy")
- Evidence: "For a theory with a minimum cutoff wavelength λmin, the Nyquist-Shannon sampling criterion implies that any state is specified by its value at two points in position space per λmin." / "An experimental upper bound on holographic noise gives a lower bound on the number density of independent position eigenstates on a null surface, therefore on the number of degrees of freedom."
- Verified: FULLTEXT
- Notes: This is the explicit "information-capacity => noise" logic that makes the proposal the closest physics analogue of a finite-resolution argument.

### C-05-014
- Claim: Hogan remarked that the argument also applies to "rays or paths in a virtual 3D world encoded in a 2D hologram".
- Source: Hogan2008measurement
- Locator: Sec. II
- Evidence: "It also applies to rays or paths in a virtual 3D world encoded in a 2D hologram."
- Verified: FULLTEXT
- Notes: "Virtual" here refers to the holographic encoding, not to a computer simulation; no simulation hypothesis is invoked.

### C-05-015
- Claim: Hogan compared the Planck threshold sqrt(t_P) = 2.3 x 10^-22 Hz^-1/2 with LIGO's measured strain noise (below 10^-22 Hz^-1/2 from about 70 to 300 Hz) but argued that LIGO suppresses holographic noise relative to GEO600, which sends its full power through the beamsplitter.
- Source: Hogan2008measurement
- Locator: Sec. I; Sec. IV.C
- Evidence: "the measured spectral density of noise in the recent science runs of LIGO[20, 21] is less than h = 10^−22 Hz^−1/2 over a broad band, from about 70 Hz to about 300 Hz." / "metric strain noise below h ≈ [√]tP = 2.3 × 10^−22 Hz^−1/2" / "the most promising currently operating experiment for detecting the effect is not LIGO, but GEO600"
- Verified: FULLTEXT
- Notes: Later disputed for other models by Li2023interferometer (C-05-042), who find that geontropic fluctuations do accumulate in Fabry-Perot arms.

### C-05-016
- Claim: Hogan (2008) estimated holographic noise comparable in magnitude and spectrum to the measured GEO600 noise between about 100 and 600 Hz, and wrote that the approximate agreement with otherwise unexplained GEO600 noise "motivates further study".
- Source: Hogan2008measurement
- Locator: Sec. IV.B
- Evidence: "Since it predicts noise comparable in magnitude and spectrum to the level of noise measured in the current GEO600 system from about 100 to 600 Hz[30] ... The approximate agreement of predicted holographic noise with otherwise unexplained noise in GEO600 motivates further study."
- Verified: FULLTEXT
- Notes: Hogan notes the estimate "omits numerical factors of the order unity".

### C-05-017
- Claim: In a companion paper Hogan stated that the estimated GEO600 holographic-noise spectrum approximately accounts for then-unexplained noise between about 300 and 1400 Hz.
- Source: Hogan2008indeterminacy
- Locator: Abstract
- Evidence: "The spectrum of holographic noise is estimated for the GEO600 interferometric gravitational-wave detector, and is shown to approximately account for currently unexplained noise between about 300 and 1400Hz."
- Verified: FULLTEXT
- Notes: Frequency range differs from C-05-016 (100-600 Hz); both are as stated in the respective papers.

### C-05-018
- Claim: In a 2009 revision Hogan derived an equivalent strain amplitude a factor sqrt(pi) smaller than his earlier estimate, predicted h = sqrt(t_P/2pi) = 0.92 x 10^-22 Hz^-1/2 for GEO600, withdrew an earlier claim about a low-frequency change of slope, and predicted that signals in two nearly co-located interferometers would be highly correlated.
- Source: Hogan2009holographic
- Locator: Abstract; Sec. on GEO600 (text after Eq. 38)
- Evidence: "The spectral amplitude of equivalent strain derived here is a factor of [√]π smaller than previously published estimates. Signals in two nearly-collocated interferometers are predicted to be highly correlated" / "In GEO600, with N = 2, the estimate in Eq.(38) predicts a new noise source, h = [√](tP/2π) = 0.92 × 10^−22 /[√]Hz" / "In that paper however it was erroneously claimed that in the GEO600 power-recycling cavity the predicted slope changes at very low frequencies"
- Verified: FULLTEXT
- Notes: arXiv-only (v8, Jan 2010); not published in a journal per INSPIRE. Square roots restored from Eq. (38) and the stated ratio sqrt(t_P/2) vs sqrt(t_P/2pi); numerically sqrt(5.39e-44/2pi) = 0.93e-22, consistent.

### C-05-019
- Claim: Smolyaninov argued that Hogan's derivation rests on assumed linear diffraction of Planck-wavelength radiation; if vacuum self-focusing (nonlinear optics) operates, the ray-orientation uncertainty would be of order lambda_p/L rather than (lambda_p/L)^{1/2}, i.e. 19 orders of magnitude smaller, so the expected holographic noise "must be reduced by many orders of magnitude".
- Source: Smolyaninov2009level
- Locator: Abstract; main text
- Evidence: "It is demonstrated that earlier estimates are based on assumed linear diffractive behavior of Planck radiation. Since nonlinear effects, such as self-focusing, are expected to appear at much lower energies, the expected level of holographic noise must be reduced by many orders of magnitude." / "the ray orientation uncertainty must be of the order of ∆θ ∼ (λp /L), which is 19 orders of magnitude smaller."
- Verified: FULLTEXT
- Notes: A published critique (PRD 79, 087503). We found no published reply by Hogan in INSPIRE citation lists.

### C-05-020
- Claim: GEO600 papers of the period describe noise between roughly 100 Hz and 1 kHz that was not yet explained in the detuned heterodyne (RF) readout configuration.
- Source: Hild2009dcreadout; Luck2010upgrade
- Locator: Hild2009dcreadout Sec. 7; Luck2010upgrade Sec. 1
- Evidence: Hild: "The noise sources limiting the peak sensitivity with both, heterodyne and DC-readout, in the frequency band between 300 Hz and 1 kHz, are so far unexplained and subject of intense investigation." Lück: "Between roughly 100 Hz and 500 Hz a yet unknown noise source limits the sensitivity in ’detuned RF readout’"
- Verified: FULLTEXT
- Notes: Neither paper mentions Hogan or holographic noise.

### C-05-021
- Claim: The GEO600 team reported that in subsequent "tuned DC readout" experiments all observed noise could be explained by contributions from known sources.
- Source: Luck2010upgrade
- Locator: Sec. 1 (below Fig. 1)
- Evidence: "In recent ’tuned DC readout’ experiments all of the observed noise could be explained by simulated (e.g. thermal noise, quantum noise) and measured (e.g. alignment feedback noise) contributions from known sources."
- Verified: FULLTEXT
- Notes: This is in a different detector configuration from the one Hogan compared with; the paper does not frame it as a test of holographic noise. Hogan's own later paper (C-05-024) argues GEO600's folded arms suppress holographic noise by a factor of 2.

### C-05-022
- Claim: Amelino-Camelia's review described Hogan's proposal as "a young proposal still looking for some maturity", distinct from earlier "holography-inspired" noise estimates, and reported that the "GEO600 anomaly" episode was over because GEO600 experimenters had reached a better understanding of their noise sources.
- Source: AmelinoCamelia2013quantum
- Locator: Sec. 4.2.3 (interferometric noise), pp. ~84-85 of arXiv v2
- Evidence: "it is probably fair to describe the alternative version of holographic noise more recently proposed in Ref. [391, 392, 393] as a young proposal still looking for some maturity" / "It appears however that experimenters at GEO600 have achieved recently a better understanding of their noise sources, and no unexplained contribution is at this point reported ... The brief season of the “GEO600 anomaly” (at some point known among specialists as the “mystery noise”) is over."
- Verified: FULLTEXT
- Notes: Amelino-Camelia also cites a GEO600 web page and Prijatelj et al. CQG 29 (2012) 055009, which we did not read.

### C-05-023
- Claim: Amelino-Camelia stated that there is no relation between Hogan's holographic noise and the earlier "holography-inspired" noise models (of the Ng-van Dam type) in the quantum-gravity phenomenology literature.
- Source: AmelinoCamelia2013quantum
- Locator: Sec. 4.2.3
- Evidence: "More recently a different mechanism for quantum-spacetime-induced noise, also labeled as “holography inspired”, was proposed in a series of papers by Hogan [391, 392, 393]. There is no relation between the two “holography-inspired” proposals for quantum-spacetime-induced interferometric noise."
- Verified: FULLTEXT
- Notes: Terminology hazard for the paper; "holographic noise" names two unrelated proposals.

### C-05-024
- Claim: Hogan's 2012 paper recast the effect as noncommuting transverse position operators (not fluctuations of a quantized metric), with amplitude fixed by equating position degrees of freedom on a 2D surface with black-hole entropy density, argued that folded arms (GEO600) and Fabry-Perot arms (LIGO) do not amplify it, so it was "not currently ruled out by either LIGO or GEO600", and proposed cross-correlating two nearly co-located interferometers at frequencies near c/2L.
- Source: Hogan2012interferometers
- Locator: Abstract; Sec. on experimental comparison (Figs. 5-6)
- Evidence: "The amplitude of the effect in physical units is predicted with no parameters, by equating the number of degrees of freedom of position wavefunctions on a 2D spacelike surface with the entropy density of a black hole event horizon of the same area." / "This quantum-geometrical “holographic noise” in position is not describable as fluctuations of a quantized metric" / "When this factor is included, holographic noise is not currently ruled out by either LIGO or GEO600." / "One way to isolate the holographic component of noise as a distinctive signal is to cross-correlate two nearly co-located interferometers at high frequencies."
- Verified: FULLTEXT
- Notes: arXiv v27 (Feb 2012); the preprint was revised many times between 2010 and 2012.

### C-05-025
- Claim: In a 2013 essay Hogan framed the hypothesis in explicitly informational terms: if reality has finite information content, space has finite fidelity, with information in spatial position limited by a "Planck broadcast" bandwidth of about 2 x 10^43 bits per second, and he used computing metaphors ("cosmic Internet Service Provider", "operating system").
- Source: Hogan2013now
- Locator: Abstract; pp. 2-3
- Evidence: "If reality has finite information content, space has finite fidelity. The quantum wave function that encodes spatial relationships may be limited to information that can be transmitted in a “Planck broadcast”, with a bandwidth given by the inverse of the Planck time, about 2 × 10^43 bits per second." / "If this is the best that the cosmic Internet Service Provider can give us, we do not get a perfect picture." / "how its instructions are encoded, and what operating system it runs on."
- Verified: FULLTEXT
- Notes: Essay (arXiv v2, Dec 2014), not peer reviewed. Metaphor only: Hogan does not propose that the universe is a simulation.

### C-05-026
- Claim: In the same essay Hogan rejected the naive picture of Planck-size pixels and instead derived a transverse blurring scale much larger than the Planck length, <x_perp^2> = L c t_P / sqrt(4 pi) = (2.135 x 10^-18 m)^2 (L/1 m), with total information growing like (L/c t_P)^2.
- Source: Hogan2013now
- Locator: pp. 3-4, Eqs. (1)-(3)
- Evidence: "Of course, nature is not really pixelated in little squares" / "The total amount of information is the number of directions times the duration, so it grows holographically, like (L/ctP)^2." / "⟨x̂⊥^2⟩ = LctP /[√]4π = (2.135 × 10^−18 m)^2 (L/1m)"
- Verified: FULLTEXT
- Notes: Numerical check: 1.616e-35 m / sqrt(4 pi) = 4.56e-36 m, sqrt = 2.135e-18 m. Consistent.

### C-05-027
- Claim: Kwon and Hogan found that Planck-scale effects on interferometers are negligible in standard field theory with canonically quantized gravity, and that LIGO/Virgo stochastic-background limits rule out a "random walk" metric-fluctuation model and constrain a "white spacetime noise" model to a normalization a0 < 0.06 (95% CL), whereas their non-metric holographic model predicts noise close to then-current and projected bounds.
- Source: Kwon2016interferometric
- Locator: Abstract; Sec. "Comparison with Experimental Data"
- Evidence: "It is shown that effects are negligible in standard field theory with canonically quantized gravity." / "it is clear that the “random walk” model is now safely ruled out." / "We calculate the limit on this coefficient as a0 < 0.06, with the same 95% confidence level." / "Predictions in this case are shown to be close to current and projected experimental bounds."
- Verified: FULLTEXT
- Notes: The metric-fluctuation models are spacetime-foam models (Amelino-Camelia, Ng-van Dam type); cross-link to the spacetime-foam/discreteness section. This paper supplies the model tested in Holometer2016first.

## C. Fermilab Holometer

### C-05-028
- Claim: The Holometer comprised two co-located, co-aligned 39.06 m power-recycled Michelson interferometers (1064 nm, about 2 kW on each beamsplitter, beamsplitters 0.91 m apart) with no arm cavities, giving a flat broadband response up to and beyond the 3.8 MHz free spectral range, digitized at 50 MHz; each had shot-noise-limited sensitivity of about 2.1 x 10^-18 m/sqrt(Hz).
- Source: Holometer2016first
- Locator: pp. 1-2, Fig. 1
- Evidence: "a pair of co-located and co-aligned 39.06 m long power-recycled Michelson interferometers, each operating at 2 kW power with mean shot-noise-limited differential position noise sensitivity of 2.1 × 10^−18 m/[√]Hz." / "They thus maintain their full Michelson differential bandwidth at frequencies up to the 3.8 MHz inverse light-crossing time of the apparatus" / "the small separation d = 0.91 m between the two beam splitters"
- Verified: FULLTEXT
- Notes: arXiv v2 (Jan 2017). The instrument paper (C-05-032) gives "40-m" arms and calls 7.6 MHz the inverse light crossing time; 3.8 MHz is c/2L, 7.6 MHz is c/L.

### C-05-029
- Claim: Cross-correlating 145 hours of data (July-August 2015) with 381 Hz resolution averaged down uncorrelated shot noise over 2 x 10^8 spectral measurements to a sensitivity of 2.1 x 10^-20 m/sqrt(Hz) to stationary correlated signals; for bandwidths above 11 kHz the strain/shear PSD sensitivity surpassed the Planck time t_p = 5.39 x 10^-44 /Hz.
- Source: Holometer2016first
- Locator: Abstract; "Measured spectra"
- Evidence: "The dominant but uncorrelated shot noise is averaged down over 2 × 10^8 independent spectral measurements with 381 Hz frequency resolution to obtain 2.1 × 10^−20 m/[√]Hz sensitivity to stationary signals. For signal bandwidths ∆f > 11 kHz, the sensitivity to strain h or shear power spectral density of classical or exotic origin surpasses a milestone PSDδh < tp where tp = 5.39 × 10^−44 /Hz is the Planck time." / "averaged over 145 hours of data taken in July-August, 2015"
- Verified: FULLTEXT
- Notes: 2.1e-18 is the single-interferometer shot noise; 2.1e-20 is the cross-spectrum sensitivity. Do not conflate.

### C-05-030
- Claim: The Holometer tested a "speculative model of Planckian diffraction" (from Kwon and Hogan) predicting a sinc-shaped cross-spectrum normalized to 4.64 x 10^-41 m^2/Hz for L of about 39 m; the data were consistent with zero at 1.1 sigma and excluded the model at 5.1 sigma statistical significance (4.6 sigma including 10% calibration uncertainty), equivalently limiting its normalization to less than 44% of the prediction at 95% CL.
- Source: Holometer2016first
- Locator: "Model testing", Eq. (1), Fig. 3
- Evidence: "we consider a speculative model in which irreducible space-time noise arising from a putative fundamental Nyquist frequency fp = 1/tp grows via diffraction over macroscopic distances" / "which is a sinc response function normalized to 4.64×10^−41 m^2/Hz" / "Using all data up to 25 MHz, the weighted integral curve remains statistically consistent at 1.1σ with zero broadband correlation. The model of Eq. 1 is thus excluded with 5.1σ statistical significance, reduced by the 10% calibration uncertainty to 4.6σ. Alternatively, the result may be viewed as a constraint on the normalization of this model to be less than 44% of the predicted value at 95% confidence level."
- Verified: FULLTEXT
- Notes: Numerical check: (t_p/sqrt(pi)) L^2 = 3.04e-44 x 39.06^2 = 4.64e-41 m^2/Hz. Reference [18] of the PRL is Kwon2016interferometric.

### C-05-031
- Claim: The Holometer authors stressed that the exclusion applies only to the spectral shape of that model, and that the straight-arm layout does not respond to correlated noise in rotational observables.
- Source: Holometer2016first
- Locator: "Model testing"; "Conclusions"
- Evidence: "It should be emphasized that these results apply only to the spectral shape of the particular model used here." / "it would not respond to correlated exotic noise power in rotational observables; these could be studied with a similar instrument reconfigured with bent arms"
- Verified: FULLTEXT
- Notes: Key for avoiding overstatement ("the Holometer ruled out holographic noise").

### C-05-032
- Claim: The Holometer instrument paper describes two co-located but independent and isolated 40 m power-recycled Michelson interferometers cross-correlated to 25 MHz, with sensitivity up to and beyond the inverse light crossing time of 7.6 MHz.
- Source: Holometer2017holometer
- Locator: Abstract
- Evidence: "The apparatus consists of two co-located, but independent and isolated, 40-m power-recycled Michelson interferometers, whose outputs are cross-correlated to 25 MHz. The data are sensitive to correlations of differential position across the apparatus over a broad band of frequencies up to and exceeding the inverse light crossing time, 7.6 MHz."
- Verified: FULLTEXT
- Notes: See note in C-05-028 on 3.8 vs 7.6 MHz.

### C-05-033
- Claim: The final first-generation (straight-arm) Holometer analysis used 704 hours of data (July 2015 to February 2016) and found no correlation; at 2 sigma it limited the two amplitudes of a two-parameter shear-noise model to |beta_L| < 0.10 t_P and |beta_2L| < 0.25 t_P, well below the order-unity values predicted, and the authors describe the class of shear-correlation models as "conclusively excluded".
- Source: Holometer2017interferometric
- Locator: Sec. 3 (data), Fig. 3, Sec. 5
- Evidence: "704 hours. These data were taken between July 2015 and February 2016." / "At 2σ significance, the data limit the amplitudes of the spectral correlation terms to |βL| < 0.10 tP and |β2L| < 0.25 tP, well below the predicted scale of quantum geometrical position noise." / "The first-generation Holometer has tested and conclusively excluded a general class of models of quantum geometrical shear noise correlations."
- Verified: FULLTEXT
- Notes: arXiv v2 (Aug 2017).

### C-05-034
- Claim: The same paper states that the straight-arm Holometer had no sensitivity to a newer Lorentz-invariant model in which exotic correlations are purely rotational, so that model was not constrained.
- Source: Holometer2017interferometric
- Locator: Sec. 5
- Evidence: "The first-generation Holometer, by the design of its optical geometry, has no sensitivity to such rotational effects, so the result reported here does not constrain this model."
- Verified: FULLTEXT
- Notes:

### C-05-035
- Claim: From a 130-hour dataset the Holometer achieved strain sensitivity better than 10^-21 Hz^-1/2 between 1 and 13 MHz and set 3 sigma upper limits on the stochastic gravitational-wave energy density from Omega_GW < 5.6 x 10^12 at 1 MHz to 8.4 x 10^15 at 13 MHz, far above closure density and above indirect CMB/BBN limits of about 10^-5.
- Source: Holometer2017mhz
- Locator: Abstract; "Result 1"
- Evidence: "Strain sensitivity achieved is better than 10^−21 /[√]Hz between 1 to 13 MHz from a 130-hr dataset." / "The 3σ upper limit on ΩGW ... ranges from 5.6 × 10^12 at 1 MHz to 8.4 × 10^15 at 13 MHz." / "it is higher than indirect measurements at these frequencies from integrated limits placed by the Cosmic Microwave Background [20] and Big Bang Nucleosynthesis[21] that have limits of ∼ 10^−5 in these units."
- Verified: FULLTEXT
- Notes: Additional 15% calibration systematic stated. Tangential to the simulation question; included for completeness of the experiment table.

### C-05-036
- Claim: A reconfigured Holometer with one arm of each interferometer bent by 90 degrees (L = 38.9 m, 1.3 kW, 2.7 x 10^-18 m/sqrt(Hz) shot-noise-limited) measured rotationally induced differential displacements over 1098 hours of data, reaching cross-spectral strain sensitivity below t_P/2 from 1.1 to 20 MHz for bandwidths above 10 kHz.
- Source: Richardson2021interferometric
- Locator: Abstract; Fig. 2 caption; Conclusions
- Evidence: "One arm of each interferometer is bent 90° near its midpoint to obtain sensitivity to rotations about an axis normal to the plane of the instrument." / "consists of two colocated and coaligned L = 38.9 m long power-recycled Michelson interferometers, each operating at 1.3 kW power with a mean shot-noise-limited sensitivity of 2.7 × 10^−18 m/[√]Hz." / "The spectra are averaged over 1098 hours of dual interferometer time series data" / "the sensitivity to rotation-induced strain surpasses CSDδh < tP /2 across a broad band from 1.1 MHz to 20 MHz."
- Verified: FULLTEXT
- Notes: arXiv v2 (May 2021).

### C-05-037
- Claim: The rotational analysis constrained the normalization of the tested model (Hogan, Kwon and Richardson) to eta < 0.25 t_P at 95% confidence for rotations about one axis; the authors state that values much below t_P would violate the holographic entropy bound.
- Source: Richardson2021interferometric
- Locator: Introduction; results section
- Evidence: "We constrain this parameter to η < 0.25 tP for models with one rotational axis; values much less than tP correspond to an information excess in violation of the holographic entropy bound." / "At 95% confidence we constrain the normalization to η < 0.25 tP for rotations around one axis"
- Verified: FULLTEXT
- Notes: Tested model = Hogan2017statistical (Ref. [7]).

### C-05-038
- Claim: Richardson et al. state that their data are consistent with a classical spacetime, that local quantum-field-theoretic models of quantum gravity predict no detectable effect in such a measurement, and that the planar layout cannot test models with Planck-scale uncertainty entangling all three spatial directions.
- Source: Richardson2021interferometric
- Locator: Conclusions
- Evidence: "The data presented here are consistent with a classical spacetime." / "Models of quantum gravity based on locally quantized fields on classical backgrounds predict no detectable effect in this type of measurement." / "Even though our measurement exceeds Planck sensitivity, it does not exclude all theories with large, nonlocally coherent holographic correlations. All light paths in our interferometers lie in a single plane."
- Verified: FULLTEXT
- Notes:

### C-05-039
- Claim: The model tested in the rotational Holometer run is a Lorentz-invariant statistical model of rotational fluctuations of the local inertial frame, assuming classical causal structure and a Planck information density in invariant proper time along an observer's world line.
- Source: Hogan2017statistical
- Locator: Abstract
- Evidence: "A Lorentz invariant statistical model is presented for rotational fluctuations in the local inertial frame that arise from new quantum degrees of freedom of space-time. The model assumes invariant classical causal structure, and a Planck information density in invariant proper time determined by the world line of an observer."
- Verified: FULLTEXT
- Notes:

### C-05-040
- Claim: A Holometer collaborator (Kwon) later wrote that the Holometer, proposed in 2009 and operated through 2019, was originally designed on a "naive premise" based on a toy model; that the proposal faced "(justified) criticism" that the targeted effect was not Lorentz invariant; and that the first-generation null result should be read as verifying an exact symmetry.
- Source: Kwon2025phenomenology
- Locator: Introduction; Sec. on design principles (p. 8 of arXiv v6)
- Evidence: "The Fermilab Holometer [1–4], proposed in 2009 and in operation through 2019" / "This line of research, initially based on Hogan’s conceptual insights in 2007 ... was met with controversy." / "That instrument was designed on the naive premise that we might be able to measure some noncommutativity of space-time in a simple Michelson setup ... the proposal faced much (justified) criticism that the targeted effect was not Lorentz invariant" / "the null result from this early experiment should be thought of as a verification of an exact symmetry"
- Verified: FULLTEXT
- Notes: The criticism is reported without citation to specific critics; we could not identify a published Lorentz-invariance critique (see report).

## D. Verlinde-Zurek "geontropic" fluctuations and new experiments

### C-05-041
- Claim: Verlinde and Zurek, motivated by the holographic principle and covariant entropy bound, built a model of "Planck size pixels" on the surface bounding a causally connected region whose energy fluctuations produce arm-length fluctuations <delta L^2> ~ l_p L with strong transverse correlations, which they argue could be observable in interferometers.
- Source: Verlinde2021observational
- Locator: Introduction; Sec. 8
- Evidence: "one is tempted to postulate that the microscopic spacetime degrees of freedom, also in flat spacetime, can be identified with Planck size pixels on the surface bounding a causally connected part of space." / "we have derived length fluctuations of size δL^2 ∼ lp L. The strong transverse correlation implies that in interferometer experiments the length fluctuations are sufficiently coherent across the light beam, so that they are in principle observable."
- Verified: FULLTEXT
- Notes: arXiv v2 (Oct 2021); published PLB 822 (2021) 136663.

### C-05-042
- Claim: Verlinde and Zurek state that a null result in an appropriately sensitive interferometer would falsify at least one of their postulates, and that a concrete comparison with Holometer or LIGO data required further modeling.
- Source: Verlinde2021observational
- Locator: Sec. 8
- Evidence: "Conversely, if no signal is observed in an appropriately sensitive interferometer, it would tell us that one our proposed postulates does not hold." / "The closest experimental set-up to our toy is the “Holometer” [19], but to make a concrete comparison to experimental results requires at minimum a computation extending Eq. 29"
- Verified: FULLTEXT
- Notes:

### C-05-043
- Claim: Follow-up papers grounded the proposal in modular-Hamiltonian fluctuations obeying an area law <Delta K^2> = <K> = A/4G_N (computed in AdS/CFT) and modeled them in flat space by a high-occupation-number bosonic degree of freedom, later reproduced from shockwave geometries.
- Source: Zurek2022vacuum; Verlinde2020spacetime; Verlinde2022modular
- Locator: Abstracts
- Evidence: Zurek: "both obey an area law identical to the Bekenstein-Hawking area law of black hole mechanics: ⟨K⟩ = ⟨∆K^2⟩ = A/4GN" / "the model consists of a high occupation number bosonic degree of freedom." Verlinde & Zurek 2022: "Here we demonstrate the physical origin of these fluctuations, showing that the modular area law, in d−dimensional Minkowski space, can be reproduced from shockwaves arising from vacuum fluctuations."
- Verified: FULLTEXT (Zurek2022vacuum abstract and intro read; Verlinde2022modular abstract read); ABSTRACT (Verlinde2020spacetime)
- Notes: Zurek writes "it is not known how to precisely extend such ideas about holographic quantum gravity to ordinary flat space."

### C-05-044
- Claim: Li, Lee, Chen and Zurek modeled these "geontropic" fluctuations with a scalar "pixellon" field and recast existing data: at 3 sigma, LIGO and the Holometer constrain the normalization to roughly alpha <~ 3 and alpha <~ 0.7 (with an IR cutoff) and alpha <~ 0.1 and alpha <~ 0.6 (without), with alpha ~ 1 the natural benchmark; GEO600 and LISA are out of reach.
- Source: Li2023interferometer
- Locator: Sec. V (experimental constraints), Fig. 6
- Evidence: "As expected, the tightest experimental limit comes from LIGO and Holometer measurements, which at 3σ significance, are roughly α ≲ 3 and α ≲ 0.7 (with IR cutoff), and α ≲ 0.1 and α ≲ 0.6 (w/o IR cutoff), respectively. On the other hand, our model is out of reach for GEO600 and LISA." / "α ∼ 1 gives the amplitude of the effect computed in [1, 2], and should be considered the natural benchmark"
- Verified: FULLTEXT
- Notes: These are theorists' recasts of published noise/cross-spectra, not collaboration analyses. Numbers are "roughly". The without-IR-cutoff LIGO number already excludes alpha = 1 for that variant.

### C-05-045
- Claim: Li et al. argue that, unlike the assumption made in earlier holographic-noise work, fluctuations in their model accumulate over Fabry-Perot arm cavities, justifying direct comparison with LIGO strain data.
- Source: Li2023interferometer
- Locator: Sec. V
- Evidence: "Some previous works on quantifying spacetime fluctuations (motivated by theories other than the VZ effect) argued that the predicted strain should not be directly compared against experimental constraints such as GEO600 and LIGO [32] ... Here we show that spacetime fluctuations based on Eq. (2) do accumulate over a Fabry-Perot cavity"
- Verified: FULLTEXT
- Notes: Contrast with C-05-015/C-05-024 (Hogan). Different models, so not a direct contradiction.

### C-05-046
- Claim: Bub et al. argue that if the Verlinde-Zurek effect appears in GQuEST, it would be a large background for astrophysical searches in Cosmic Explorer and the Einstein Telescope.
- Source: Bub2023quantum
- Locator: Abstract
- Evidence: "If the VZ effect proposed in Ref. [1], as modeled in Refs. [2, 3], appears in the upcoming GQuEST experiment, we show that it will be a large background for astrophysical gravitational wave searches in observatories like Cosmic Explorer and the Einstein Telescope."
- Verified: FULLTEXT
- Notes:

### C-05-047
- Claim: The GQuEST design paper proposes tabletop (5 m arm) Michelson interferometers with a photon-counting readout that is not subject to the interferometric standard quantum limit; for L = 5 m the predicted signal peaks near 15.6 MHz, and at design sensitivity GQuEST would probe alpha < 0.6 at 3 sigma in 60 h and alpha < 0.1 at 3 sigma in 2160 h, reaching the nominal signal level within several hours of integration.
- Source: Vermeulen2025photon
- Locator: Abstract; Eq. (4); Sec. IV (text after Eq. 19); Sec. VII
- Evidence: "We present a practicable interferometer design featuring a novel photon-counting readout method that provides unprecedented sensitivity, as it is not subject to the interferometric standard quantum limit." / "f pk ≈ 15.6 MHz (5 m / L)" / "GQuEST will be able to probe values of α < 0.6 at 3σ significance in 60 h of measurement time, which is the current experimental constraint set by the Holometer for geontropic fluctuations with IR cutoff. GQuEST can reach α < 0.1 at 3σ in 2160 h" / "The experiment is projected to reach the nominal predicted geontropic signal PSD peak of S̄ϕL = (3 × 10^−22 m/[√]Hz)^2 within several hours of integrated measurement time."
- Verified: FULLTEXT
- Notes: Projections, not results. Published PRX 15, 011034 (2025). Note the Holometer figure quoted here (alpha < 0.6 with IR cutoff) differs from Li2023interferometer (alpha < 0.7 with, 0.6 without); record both.

### C-05-048
- Claim: The GQuEST paper also states that the photon-counting readout enables detection of the predicted signal in measurement times at least 100 times shorter than equivalent conventional interferometers.
- Source: Vermeulen2025photon
- Locator: Abstract
- Evidence: "The accelerated accrual of Fisher information offered by the photon-counting readout enables GQuEST to detect the predicted quantum gravity phenomena within measurement times at least 100 times shorter than equivalent conventional interferometers."
- Verified: FULLTEXT
- Notes:

### C-05-049
- Claim: The Cardiff QUEST design paper proposed co-located twin tabletop "3D" interferometers with estimated displacement sensitivity of about 10^-19 m/sqrt(Hz) between 1 and 250 MHz, motivated by holographic theories predicting accumulating, correlated distance fluctuations.
- Source: Vermeulen2021experiment
- Locator: Abstract
- Evidence: "Theories of quantum gravity based on the holographic principle predict the existence of quantum fluctuations of distance measurements that accumulate and exhibit correlations over macroscopic distances." / "The experiment is estimated to be sensitive to displacements ∼ 10^−19 m/[√]Hz in a frequency band between 1 and 250 MHz"
- Verified: FULLTEXT
- Notes: Design estimate.

### C-05-050
- Claim: QUEST's first results (two co-located power-recycled Michelsons with 1.83 m arms, 10^4 s coincident run) reached a cross-correlated strain sensitivity of 3 x 10^-20 Hz^-1/2 and set upper limits on correlated length fluctuations from 13 to 80 MHz, presented as the first broadband stochastic-GW constraints there; the paper does not quote a constraint on a specific quantum-gravity model.
- Source: Patra2025broadband
- Locator: Abstract; "Experimental setup"; Conclusions
- Evidence: "set new upper limits on correlated length fluctuations from 13 to 80 MHz, constituting the first broadband constraints for a stochastic gravitational wave background at these frequencies. In a coincident observing run of 10^4 s the averaging of the cross-correlation spectra between the two interferometer signals resulted in a strain sensitivity of 3 × 10^−20 1/[√]Hz" / "The interferometers in QUEST have an arm length of 1.83 m and an inter-arm separation of 0.45 m."
- Verified: FULLTEXT
- Notes: arXiv v4 (Jun 2025); published PRL 135, 101402 (2025). Design goal 2 x 10^-19 m/sqrt(Hz), 1-200 MHz. The "does not quote" part was checked by reading the full text.

### C-05-051
- Claim: Carney, Karydas and Sivaramakrishnan show that the effective field theory of gravitons predicts an unobservably small length variation Delta L ~ l_pl ~ 10^-35 m, free of low-energy divergences, so that detecting a large gravitationally induced length variation would signal a severe breakdown of low-energy effective quantum field theory.
- Source: Carney2026response
- Locator: Abstract; Introduction
- Evidence: "show that it unambiguously predicts an unobservably small variation in the measured interferometer length ∆L ∼ ℓpl ∼ 10^−35 m. In particular, there are no divergences signaling a breakdown of this calculation in the low energy regime. Thus, detection of a large, gravitationally-induced length variation would signal a severe breakdown of effective quantum field theory in low energy quantum gravity."
- Verified: FULLTEXT
- Notes: arXiv v2 (Apr 2026); published PRD 113, 106002 (2026).

### C-05-052
- Claim: Freidel and Oberfrank find that time-delay noise spectra from graviton vacuum, thermal and squeezed states, and from a scalar vacuum stress-energy, are ultraviolet finite but remain suppressed by the Planck scale.
- Source: Freidel2026geometric
- Locator: Abstract
- Evidence: "We find that the resulting spectra are free of ultraviolet divergences and that, while thermal and squeezed states provide a natural amplification mechanism, the spectra remain suppressed by the Planck scale."
- Verified: FULLTEXT
- Notes: Preprint (arXiv:2601.17849v1), not yet refereed.

### C-05-053
- Claim: Sharmila, Vermeulen and Datta map classes of spacetime-fluctuation correlation functions to interferometer signatures and conclude that laboratory instruments such as QUEST and GQuEST could reveal more about the nature of the fluctuations, while LIGO is better suited to detecting their bare presence or absence.
- Source: Sharmila2026signatures
- Locator: Abstract
- Evidence: "such observations could provide more information on the nature of the SFs than those from LIGO. On the other hand, we find that LIGO is better suited for detecting the bare presence or absence of SFs."
- Verified: FULLTEXT
- Notes: arXiv v1; published Nature Commun. 17, 701 (2026).

### C-05-054
- Claim: A tabletop demonstration injected a common stochastic signal (standing in for holographic noise) into two interferometers and showed that quantum-correlated (twin-beam) light outperforms classical light for detecting correlated signals in the MHz band.
- Source: Pradyumna2020twin
- Locator: Abstract; Results
- Evidence: "Here we present and realize a correlation interferometry scheme exploiting bipartite quantum correlated states injected in two independent interferometers. The scheme outperforms classical ones in detecting a faint signal that may be correlated/uncorrelated between the two devices." / "The same stochastic signal (simulating the presence of the holographic noise) was injected by two electrooptical modulators"
- Verified: FULLTEXT
- Notes: Proof of principle, no constraint on physics models.

### C-05-055
- Claim: Carlip's review of spacetime foam lists interferometer noise among observational probes and notes that some holographic models with macroscopic correlations have allowed experimental searches that placed limits on particular phenomenological models.
- Source: Carlip2023spacetime
- Locator: Sec. on observational tests ("Interferometer noise")
- Evidence: "In some “holographic” models of spacetime foam, the relevant quantum fluctuations have macroscopic correlations (see, for instance, [273]). These have allowed experimental searches and placed limits on particular phenomenological models [274–276]."
- Verified: FULLTEXT
- Notes: Refs [274-276] are the Holometer instrument and shear papers and QUEST.

## E. Connection (or not) to the simulation hypothesis

### C-05-056
- Claim: None of the theoretical or experimental papers on holographic noise and geontropic fluctuations read for this section invokes the simulation hypothesis; the word "simulation" appears in them only for numerical/optical modelling (e.g. FINESSE) or injected test signals.
- Source: Hogan2008measurement; Hogan2008indeterminacy; Hogan2009holographic; Hogan2012interferometers; Hogan2013now; Kwon2016interferometric; Holometer2016first; Holometer2017holometer; Holometer2017interferometric; Holometer2017mhz; Richardson2021interferometric; Hogan2017statistical; Verlinde2021observational; Zurek2022vacuum; Li2023interferometer; Bub2023quantum; Vermeulen2021experiment; Vermeulen2025photon; Patra2025broadband; Kwon2025phenomenology; Carney2026response
- Locator: whole texts (case-insensitive search for "simulat" in pdftotext output)
- Evidence: Hits only of the form "FINESSE Monte Carlo simulations" (Holometer2017holometer), "Computer simulations using FINESSE" (Vermeulen2021experiment), "simulated realizations based on the standard QFT-based model" (Kwon2025phenomenology); no hit refers to a simulated universe.
- Verified: FULLTEXT
- Notes: Negative result; search method documented in the report. INSPIRE full-text queries combining "simulation hypothesis" with "Holometer", "holographic noise" or "GQuEST" returned 0 records (2026-09-27).

### C-05-057
- Claim: Neukart et al. (a non-refereed preprint) explicitly link the Holometer to the simulation hypothesis, suggesting that if experiments such as the Holometer showed the "holographic universe" to be true, this "may be interpreted as an indication of us participating in a simulation chain".
- Source: Neukart2022do
- Locator: Section on computability constraints (holographic universe paragraph), ref. [85] = Holometer2016first
- Evidence: "An external programmer could potentially use this fact and encode a more complex, higher-dimensional universe as physical theories operating on its lower-dimensional boundary surface" / "If experiments [85] show that the holographic universe is true, it may be interpreted as an indication of us participating in a simulation chain."
- Verified: FULLTEXT
- Notes: The cited experiment reported a null result for one specific noise model; it did not test "the holographic universe" in general. Preprint (arXiv:2212.04921), no journal version found in INSPIRE.

### C-05-058
- Claim: The Holometer PRL itself frames the tested spectrum in information-theoretic terms, as noise from "a putative fundamental Nyquist frequency f_p = 1/t_p" growing by diffraction over macroscopic distances.
- Source: Holometer2016first
- Locator: "Model testing"
- Evidence: "a speculative model in which irreducible space-time noise arising from a putative fundamental Nyquist frequency fp = 1/tp grows via diffraction over macroscopic distances to give a white noise shear power spectral density quantitatively equal to tp."
- Verified: FULLTEXT
- Notes: Sampling-theorem language, but no reference to computation or simulation.

## F. Additional numerical claims used in the experiment table

### C-05-059
- Claim: Around 2010 GEO600 reached a peak strain sensitivity of 2.2 x 10^-22 Hz^-1/2 at its 530 Hz signal-recycling tuning frequency.
- Source: Luck2010upgrade
- Locator: Sec. 1
- Evidence: "The peak sensitivity of GEO 600, 2.2 · 10^−22 [1/[√]Hz], is reached at the tuning frequency of 530 Hz (see figure 2)."
- Verified: FULLTEXT
- Notes: Detuned RF-readout configuration.

### C-05-060
- Claim: In the bent-arm Holometer run the cross-correlation reached 6.1 x 10^-21 m/sqrt(Hz) at 9.92 kHz resolution (3.9 x 10^10 spectral averages per bin), giving an average limit of 3.72 x 10^-41 m^2/Hz (about 0.46 t_P L^2) on stationary sources with bandwidth above 9.92 kHz between 1.1 and 20 MHz.
- Source: Richardson2021interferometric
- Locator: p. 1; results section
- Evidence: "averaging down below shot noise to a sensitivity of 6.1 × 10^−21 m/[√]Hz at 9.92 kHz resolution to stationary signals common to both interferometers." / "we place an average limit of 3.72 × 10^−41 m^2/Hz ≈ 0.46 tP L^2 on the magnitude of stationary sources with bandwidth ∆f > 9.92 kHz."
- Verified: FULLTEXT
- Notes: Numerical check: 0.46 x 5.39e-44 x 38.9^2 = 3.75e-41, consistent.

### C-05-061
- Claim: Kwon and Hogan used the LIGO/Virgo stochastic-background limit Omega_GW < 5.6 x 10^-6 (95% CL, flat spectrum over 41.5-169.25 Hz) to constrain metric-fluctuation models.
- Source: Kwon2016interferometric
- Locator: Sec. "Comparison with Experimental Data"
- Evidence: "By assuming a frequency-independent spectrum over the frequency band 41.5 − 169.25Hz, LIGO and Virgo obtained a result of ΩGW < 5.6 × 10^−6 at 95% confidence[49]."
- Verified: FULLTEXT
- Notes: The primary LIGO/Virgo paper (their ref. [49], Nature 460, 990 (2009)) was not read by us; number taken as quoted.

### C-05-062
- Claim: GEO600 has folded arms (light traverses each arm twice, N = 2) of physical length about 600 m, and Hogan (2012) computed a predicted displacement noise of 2.2 x 10^-19 m/sqrt(Hz) for L = 600 m before applying the arm-folding suppression factor.
- Source: Hogan2012interferometers; Hogan2009holographic
- Locator: Hogan2012 experimental-comparison section; Hogan2009 text after Eq. (38)
- Evidence: Hogan 2012: "For L = 600m, the predicted amplitude spectral density is [√]Ξ̃(f) = 2.2 × 10^−19 m/[√]Hz, slightly higher than the observed minimum noise in GEO600." Hogan 2009: "In GEO600, with N = 2, the estimate in Eq.(38) predicts a new noise source"
- Verified: FULLTEXT
- Notes: Numerical check: sqrt(8 t_P L^2 / pi) with L = 600 m = 2.2e-19 m/sqrt(Hz). Arm length taken from Hogan's use of L = 600 m; not independently checked against a GEO600 instrument paper.
