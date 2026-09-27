# Claim ledger: 07-rendering-qm

Topic: "render-on-demand" / observer-dependent computation proposals and quantum foundations.
Researcher notes: all PDFs read are in `/tmp/claude-0/papers/` (file names given in Notes where
useful). Page numbers for Campbell et al. refer to the published IJQF pagination (pp. 78-99);
the arXiv v2 text (1703.00058v2, 6 Jun 2017) is identical in substance to the published version
(checked side by side; the published version fixes the typo "would would" on p. 92).

Claims marked "(our analysis)" in the Notes are inferences we draw by combining quoted source
statements. They are flagged so that the section text presents them as the authors' (i.e. our)
reasoning, not as claims of the cited paper.

---

## A. Campbell, Owhadi, Sauvageau & Watkinson (2017)

### C-07-001
- Claim: Campbell et al. assume that the system performing the simulation is finite and seeks low computational complexity.
- Source: Campbell2017on
- Locator: Sec. 3 "Theory description", p. 80
- Evidence: "Our core assumption is that this system is finite and, as a consequence, the content of the simulation is limited by (and only by) its finite processing resources and the system seeks to achieve low computational complexity."
- Verified: FULLTEXT
- Notes: Published IJQF PDF (IJQF2017v3n3p2.pdf) and arXiv v2 both read.

### C-07-002
- Claim: From this assumption and an analogy with video games (procedural generation in No Man's Sky, Boundless), they posit that reality is rendered only when information becomes available to a conscious observer ("player"), at a resolution matched to the observer's perception.
- Source: Campbell2017on
- Locator: Sec. 3, "On rendering reality", p. 80
- Evidence: "the system performing the simulation would render reality only at the moment the corresponding information becomes available for observation by a conscious observer (a player), and the resolution/granularity of the rendering would be adjusted to the level of perception of the observer."
- Verified: FULLTEXT
- Notes: The step from "low complexity" to "render on observation" is an analogy, not a derivation; the video-game support cites a CNN article (their ref. [21]).

### C-07-003
- Claim: Campbell et al. account for Bell-inequality violations by positing that locality within the simulation does not constrain the simulating system.
- Source: Campbell2017on
- Locator: Sec. 3, "On the compatibility of the simulation theory with Bell's no go theorem", p. 81
- Evidence: "notions of locality and distance defined within the simulation do not constrain the action space of the system performing the simulation"
- Verified: FULLTEXT
- Notes: i.e. the proposed simulator is explicitly nonlocal with respect to simulated spacetime.

### C-07-004
- Claim: They postulate that a good virtual reality must both preserve consistency and avoid detection, and that unresolvable conflicts between these would produce "VR indicators and discontinuities".
- Source: Campbell2017on
- Locator: Sec. 3, p. 82
- Evidence: "a good/effective VR would operate based on two, possibly conflicting, requirements: (1) preserving the consistency of the VR (2) avoiding detection"; "conflicts that were unresolvable would lead to VR indicators and discontinuities (such as the wave/particle duality)."
- Verified: FULLTEXT
- Notes: none

### C-07-005
- Claim: Their central testable conjecture is that wave or particle patterns are fixed not at detection but by the existence and availability of which-way data when the pattern is observed.
- Source: Campbell2017on
- Locator: Sec. 4 "Hypothesis test", p. 82
- Evidence: "our hypothesis is that wave or particle duality patterns are not determined at the moment of detection but by the existence and availability of the which-way data when the pattern is observed."
- Verified: FULLTEXT
- Notes: "Availability" is further glossed on p. 87 as recording "on objective media" (C-07-008).

### C-07-006
- Claim: Proposed experiment 1 (Sec. 4.2): which-way detectors at the slits remain on while the recording device is switched off or unplugged; success is an interference pattern.
- Source: Campbell2017on
- Locator: Sec. 4.2, Fig. 5, p. 86
- Evidence: "place (turned on) detectors at the slits and turn off any device recording the information sent from these detectors (or this could be simply done by unplugging cables"
- Verified: FULLTEXT
- Notes: Success criterion stated as interference ("wave pattern") in this configuration.

### C-07-007
- Claim: In the entangled-photon (Kim et al.) implementation of experiment 1, they state that removing the coincidence counter and recording only D0 should, if the experiment is successful, display the wave (interference) pattern at D0.
- Source: Campbell2017on
- Locator: Sec. 4.2, p. 86
- Evidence: "Simply removing the coincidence counter from the experimental setup and recording (only) the output of D0 (result screen). D0 should display the wave pattern if the experiment is successful."
- Verified: FULLTEXT
- Notes: Standard QM predicts no fringes in the unsorted D0 distribution (C-07-019, C-07-020). This "success" is therefore a deviation from QM.

### C-07-008
- Claim: Campbell et al. define "availability" of which-way data as its recording on objective media, as distinct from its being known to a conscious experimenter.
- Source: Campbell2017on
- Locator: Sec. 4.2, "On the availability of the which-way data", pp. 86-87
- Evidence: "Note that 'availability of the which-way data' is implied by the which-way data being recorded on objective media (but does not imply a simple 'observation of the which-way data')."
- Verified: FULLTEXT
- Notes: The paper does not give an operational criterion for when a physical record (e.g. an atomic internal state or an emitted photon) counts as "objective media". This makes the hypothesis flexible.

### C-07-009
- Claim: Proposed experiment 2 (Sec. 4.3) records which-way data and screen data on separate USB drives, irreversibly destroys the which-way drive with probability 1/2, and counts as success an interference pattern only in the screen data whose which-way drive was destroyed.
- Source: Campbell2017on
- Locator: Sec. 4.3, Fig. 6, pp. 87-88
- Evidence: "For each pair, the which-way USB flash drive is destroyed with probability pd = 1/2."; "The test is successful if the USB flash drives storing impact patterns show an interference pattern only when the corresponding which-way data USB flash drive has been destroyed."
- Verified: FULLTEXT
- Notes: none

### C-07-010
- Claim: For experiment 3 (Sec. 4.4) Campbell et al. derive P[R=1 | x <= X <= x+dx] ~ 1/(1 + 2 cos^2(pi x / a)), with a = lambda L / d, predicting that the signal-photon position X would statistically predict the later random which-way/erasure outcome R.
- Source: Campbell2017on
- Locator: Sec. 4.4, Eqs. (1)-(2), p. 89
- Evidence: "Therefore if the proposed experiment is successful, then the distribution of the random variable R would be biased by that of X and this bias could be used by a microprocessor whose output would predict the value of the random variable R (prior to its realization)"
- Verified: FULLTEXT
- Notes: The derivation uses P[x|R=0] ~ 4 I0 cos^2(pi x/a) dx and P[x|R=1] ~ 2 I0 dx, with P[R=0]=1/2. The assumed R=0 distribution is the fringe pattern of a single erasure detector (D1 in Kim et al.), not the sum over both erasure detectors.

### C-07-011
- Claim: Under standard QM, the D0 events conditioned only on "erasure" (either erasure detector) are the sum of the D1 fringe and D2 antifringe patterns and show no fringes, so X and R are independent and P(R=1|X) = 1/2; Campbell et al.'s Eq. (2) thus departs from QM by up to 1/2 in probability (at dark fringes, where Eq. (2) gives ~1) and by 1/6 at bright fringes (where it gives 1/3).
- Source: Kim2000delayed; Kastner2019delayed; Campbell2017on
- Locator: Kim et al. Eq. (10) and text (p. 3 arXiv); Kastner Sec. after Eq. (9) (arXiv p. 13); Campbell Eq. (2)
- Evidence: Kim: "R01 ∝ cos2 (xπd/λf ), and R02 ∝ sin2 (xπd/λf )"; Kastner: "the distribution exhibited, which is just noise, cannot be interpreted preferentially as a sum of the slit A and slit B patterns, since exactly the same noise distribution is yielded as a sum of the fringe and antifringe patterns."
- Verified: FULLTEXT
- Notes: (our analysis) The deviation magnitudes are our arithmetic from Eq. (2) vs. 1/2. The claim that R and X are independent in QM follows because R03, R04 (which-path) and R01+R02 (erasure) both lack fringes (Kim Fig. 5 and Eq. 10).

### C-07-012
- Claim: In the thought experiment of Sec. 4.5 (Fig. 8), configurations (a)-(c), in which the which-way data are eventually erased and X is examined later, are stated to produce an interference pattern at D0 in the aggregate of X_1..X_n.
- Source: Campbell2017on
- Locator: Sec. 4.5 steps (a)-(c), p. 91; Fig. 8, p. 90; "Clarification of the notion of pattern", p. 92
- Evidence: "One should get an interference pattern at D0 , as illustrated in Figure 8-(a)."; "these samples are observed after the erasure of the which-way data and the resulting aggregated pattern (formed by X1 , . . . , Xn for large n) must be that of an interference pattern."
- Verified: FULLTEXT
- Notes: Standard QM predicts no fringes in the unconditioned D0 pattern of an entangled-pair eraser in any of (a)-(d) (C-07-019, C-07-020). Fig. 8 inspected as rendered image.

### C-07-013
- Claim: Campbell et al. prove, from a total-variation argument (Eq. 4), that X cannot be sampled from the wave distribution when the switch is inactive and from the particle distribution when active; they classify the possible outcomes as a "discontinuity in the rendering reality", evidence for rendering at observation, or a paradox.
- Source: Campbell2017on
- Locator: Sec. 4.5, outcomes (I)-(III) p. 91; Eqs. (3)-(4), pp. 91-92
- Evidence: "(I) Steps (1) or (2) in Figure 8 do not hold true (which would be a discontinuity in the rendering reality). (II) Reality is rendered at the moment the corresponding information becomes available for observation by an experimenter (which would be an indication that the simulation (VR) theory is true). (III) Which-way data can be recorded with a wave pattern (which would be a paradox)."
- Verified: FULLTEXT
- Notes: (our analysis) Since QM predicts that step (1) (interference at D0 in Fig. 8(a)) already fails, the standard-QM outcome would be classified by the paper's scheme as outcome (I), a "discontinuity". The scheme therefore does not have an outcome that corresponds to "standard QM holds and the hypothesis is disfavoured".

### C-07-014
- Claim: Campbell et al. state that outcome (ii) of Fig. 8(d) (a particle pattern at D0 regardless of the switch position) "would be a strong indicator that this reality is simulated".
- Source: Campbell2017on
- Locator: Sec. 4.5 (d), p. 92
- Evidence: "Outcome (ii) would be a strong indicator that this reality is simulated."
- Verified: FULLTEXT
- Notes: (our analysis) Standard QM predicts a no-fringe D0 marginal independent of the switch position (no-signalling; C-07-019), i.e. the outcome that the paper reads as an indicator of simulation is also the textbook prediction for the unconditioned D0 data. The paper's intended contrast is with configuration (c), which it expects to show fringes; QM predicts no fringes there either.

### C-07-015
- Claim: The paper states that the Sec. 4.5 experiment had not been performed, and that the authors "cannot predict" its outcome but can prove it will be "new".
- Source: Campbell2017on
- Locator: Sec. 4 p. 83; Sec. 4.5 end, p. 95
- Evidence: "Although we cannot predict the outcome of the experiments proposed in Subsection 4.5 we can rigorously prove that their outcome will be new in comparison to classical wave-duality experiments."; "although the experiment has not been performed yet we can already predict that its outcome will be new."
- Verified: FULLTEXT
- Notes: The paper provides no numerical prediction (e.g. an expected fringe visibility) for any experiment; its predictions are qualitative ("wave pattern" vs "particle pattern") with a noise allowance delta(I) < 0.9 in Sec. 4.5 (p. 94: "We use δ(I) < 0.9 to account for experimental noise").

### C-07-016
- Claim: Campbell et al. cite Ma et al. (2013) as suggesting that the delay Delta-t between the signal detection and the erasure choice can be made arbitrarily large without changing the outcome, and adopt this as an assumption.
- Source: Campbell2017on
- Locator: Sec. 4.5, p. 91
- Evidence: "The experiments of X. Ma, J. Kofler, A. Qarry et al. [27] suggest that the set-up could be such that ∆t could be arbitrarily large without changing the outcome of the delayed erasure (we will make that assumption)."
- Verified: FULLTEXT
- Notes: Ma et al. achieved a choice ~450 microseconds after the interference events (C-07-026). Campbell et al. propose Delta-t ~ 60 s.

### C-07-017
- Claim: Campbell et al. treat the Copenhagen, many-worlds and von Neumann-Wigner views as the three main perspectives on collapse, and describe their proposal as supporting the von Neumann-Wigner postulate while agreeing with Copenhagen that waves and collapse need not exist.
- Source: Campbell2017on
- Locator: Sec. 2 "Review", p. 79; Sec. 3, p. 83
- Evidence: "Although this perspective supports the Von Neumann-Wigner postulate that [48, 53] human consciousness is necessary for the completion of quantum theory, the simulation theory also agrees with Copenhagen in the sense that it does not require the actual existence of quantum waves or their collapse"
- Verified: FULLTEXT
- Notes: The review omits decoherence theory, Bohmian mechanics and objective-collapse models, which bear directly on which-path experiments.

## B. Status of the proposed experiments

### C-07-018
- Claim: The CUSAC website run by Campbell's organisation lists five experiments "that CUSAC intends to perform" and names team leads in California (F. Khoshnoud) and Canada (D. Chartrand); it posts no results or data.
- Source: CUSAC2024experiments
- Locator: pages /experiments, /team, /faq, /copy-of-paper ("Updates"), accessed 2026-09-27
- Evidence: "Here you will find video summaries of each of the wave-particle duality experiments that CUSAC intends to perform."; "California Experiment Team Leader Dr. Farbod Khoshnoud"; "Canada Experiment Team Leader David Chartrand"
- Verified: FULLTEXT
- Notes: Website, not a scientific source; cited only for the status of the programme. The "Updates" page links only to videos. No preprint or paper with results found (searches in report).

### C-07-018a
- Claim: Luo et al. (2024), an American Journal of Physics paper co-authored by F. Khoshnoud and acknowledging T. Campbell and D. Chartrand, demonstrated single-photon double-slit interference and a polarization quantum eraser.
- Source: Luo2024young
- Locator: Abstract; Acknowledgments (arXiv p. 17)
- Evidence: "We include experimental data obtained using this setup demonstrating double-slit and single-slit interference as well as quantum erasing through the use of sheet polarizers."; "We thank T. Campbell, D. Chartrand, J. Freericks, and J. Küchenmeister for suggestions and encouragement."
- Verified: FULLTEXT
- Notes: The paper does not mention the simulation hypothesis and is not presented as a test of it.

### C-07-018b
- Claim: In Luo et al., orthogonal polarizers on the two slits removed interference without any measurement of the path information; a vertical polarizer after the slits restored it. The fitted double-slit visibility was |V| = 0.65 +/- 0.22.
- Source: Luo2024young
- Locator: Sec. IV.C, Fig. 5; Sec. V.D (visibility)
- Evidence: "Notably, we did not need to measure the path information. Interference is not present whenever the path information is available, regardless of whether it is collected or not."; "the visibility comes out to be |V | = 0.65 ± 0.22"
- Verified: FULLTEXT
- Notes: A polarization marker is not the "detector + unplugged recorder" set-up of Campbell et al. Sec. 4.2. A proponent could call the polarization an "objective" record (C-07-008). Error bars are large; this is a teaching-lab demonstration.

## C. Standard QM predictions and delayed-choice / eraser experiments

### C-07-019
- Claim: In the standard QM account of which-path marking by an entangled partner, ignoring (not measuring) the partner leaves the interfering system in a mixed state that cannot show interference, "independent of whether an observer takes note of it or not".
- Source: Ma2016delayed
- Locator: Sec. II.E (arXiv v3 pp. 8-9), discussion of Scully et al. (1991) proposal, Eqs. (6)-(7)
- Evidence: "The lack of interference in both cases is because the which-path information is still present in the universe, independent of whether an observer takes note of it or not. Ignoring the photon state, which carries which-path information about the atom, leads to a mixed state of the atom of the from 1/2(|g⟩1⟨g| + |g⟩2⟨g|) which cannot show an interference pattern."
- Verified: FULLTEXT
- Notes: Direct contradiction of Campbell et al.'s Sec. 4.2 success criterion.

### C-07-020
- Claim: Kim et al. (2000) realized the Scully-Drühl delayed-choice quantum eraser with SPDC photon pairs: coincidences with the erasing detectors D1 and D2 show fringes with a pi phase shift (R01 ∝ cos^2, R02 ∝ sin^2), coincidences with the which-path detectors D3, D4 show none, and the idler was registered at least 8 ns after the signal.
- Source: Kim2000delayed
- Locator: arXiv pp. 2-3, Eq. (10), Figs. 3-5
- Evidence: "It is clear we have observed the standard Young's double-slit interference pattern. However, there is a π phase shift between the two interference fringes."; "any information one can learn from photon 2 must be at least 8ns later than what one has learned from the registration of photon 1."
- Verified: FULLTEXT
- Notes: arXiv version (submitted to PRL). The RMP review (Ma2016delayed Sec. IV.C) gives the delay as about 2.3 m (7.7 ns); Kim et al. text says "≃ 2.5m" and "at least 8ns". We quote Kim et al.

### C-07-021
- Claim: Kastner (2019) argues that the quantum eraser neither erases information nor delays anything beyond standard EPR correlations: the unsorted signal distribution is "just noise", and the fringes appear only as conditional Born-rule distributions after coincidence sorting.
- Source: Kastner2019delayed
- Locator: Abstract; Sec. after Eq. (9); concluding section (arXiv pp. 13-16)
- Evidence: "It is demonstrated that 'quantum eraser' (QE) experiments do not erase any information. Nor do they demonstrate 'temporal nonlocality' in their 'delayed choice' form, beyond standard EPR correlations."; "The patterns seen only after coincidence count comparisons are nothing more than conditional Born probability distributions"
- Verified: FULLTEXT
- Notes: Interpretive paper (Found. Phys.). The no-fringe marginal is uncontroversial; the terminological critique is Kastner's position.

### C-07-022
- Claim: Wheeler proposed the delayed-choice gedanken experiment in 1978 and developed it, including a cosmological (gravitational-lens) version, in "Law without law" (1983).
- Source: Wheeler1978past; Wheeler1983law; Ma2016delayed
- Locator: Ma et al. RMP Sec. II.D, Figs. 4-5
- Evidence: "The paradigm of delayed-choice experiments was revived by Wheeler in Ref. (Wheeler, 1978) and a series of works between 1979 and 1981 which were merged in Ref. (Wheeler, 1984)."; "Wheeler proposed a most dramatic 'delayed-choice gedanken experiment at the cosmological scale'"
- Verified: FULLTEXT
- Notes: Wheeler originals: METADATA only (not accessible). Characterization taken from the RMP review, which quotes them. The RMP dates the collection "1984"; the Princeton volume carries 1983 (Crossref DOI 10.1515/9781400854554). Page range 182-213 from Ma2013quantum ref. [13].

### C-07-023
- Claim: Wheeler wrote that "No elementary phenomenon is a phenomenon until it is a registered (observed) phenomenon", while also warning that it is "wrong to talk of the 'route' of the photon".
- Source: Ma2016delayed (quoting Wheeler1983law)
- Locator: RMP Sec. II.D, p. 7 (arXiv)
- Evidence: "In actuality it is wrong to talk of the 'route' of the photon. [...] 'No elementary phenomenon is a phenomenon until it is a registered (observed) phenomenon.'"
- Verified: FULLTEXT
- Notes: Quote via the review; the original not read. Render-on-demand proposals often cite Wheeler; Wheeler's criterion is registration by "an irreversible act of amplification", not conscious observation (same passage).

### C-07-024
- Claim: Jacques et al. (2007) realized Wheeler's delayed choice with single photons from an NV centre in a 48 m interferometer, with the choice made by a quantum random number generator space-like separated from the photon's entry; they measured 94% visibility in the closed configuration and, in the open configuration, equal detection probabilities (0.50 +/- 0.01) with which-way parameter I > 0.99.
- Source: Jacques2007experimental
- Locator: Abstract; main text; Fig. 3 caption
- Evidence: "Measurements in the closed configuration show interference with a visibility of 94%, while measurements in the open configuration allow us to determine the followed path with an error probability lower than 1%."; "no interference is observed and equal detection probabilities (0.50 ± 0.01) on the two output ports are measured"
- Verified: FULLTEXT
- Notes: arXiv quant-ph/0610241. Also measured alpha = 0.12 +/- 0.01 (single-photon anticorrelation parameter).

### C-07-025
- Claim: Jacques et al. conclude that the photon's behaviour depends on the observable measured even when the choice is space-like separated from its entry, in agreement with QM.
- Source: Jacques2007experimental
- Locator: final paragraph of main text
- Evidence: "Our realization of Wheeler's delayed-choice GedankenExperiment demonstrates beyond any doubt that the behavior of the photon in the interferometer depends on the choice of the observable which is measured"; "we find that Nature behaves in agreement with the predictions of Quantum Mechanics"
- Verified: FULLTEXT
- Notes: none

### C-07-026
- Claim: Ma et al. (2013) performed a quantum eraser with the erasure choice space-like separated from the interference (Vienna, 55 m fibre; Canary Islands, 144 km free space), obtaining which-path parameter I = 0.955(7) with no interference in the which-path setting and visibility V = 0.951(18) with I = 0.077(22) in the erasure setting; in one Canary arrangement the choice happened about 450 microseconds after the interference events.
- Source: Ma2013quantum
- Locator: Abstract; Fig. 3 caption; main text pp. 5-7 (arXiv)
- Evidence: "The value 0.955(7) of the parameter I(i) reveals almost full welcher-weg information"; "interference shows up with the visibility of V(ii) = 0.951(18)"; "the choice event Ce happens approximately 450 µs after the events Is in the reference frame of the source"
- Verified: FULLTEXT
- Notes: Uncertainties are +/- 1 standard deviation (Poissonian). Canary data are background-subtracted ("after subtraction of the background").

### C-07-027
- Claim: Ma et al. (2013) found their data to agree with the complementarity inequality I^2 + V^2 <= 1 over a continuous transition between which-path and erasure measurements, with the curve computed from independently measured imperfections.
- Source: Ma2013quantum; Englert1996fringe
- Locator: Ma et al. Eq. (3), Fig. 4
- Evidence: "I^2 + V^2 ≤ 1"; "The solid line is computed using actual non-ideal experimental parameters, which are measured independently. The agreement between the calculation and the experimental data is excellent."
- Verified: FULLTEXT
- Notes: Englert (1996) is cited only as the origin of the inequality (METADATA; title "Fringe Visibility and Which-Way Information: An Inequality"). Ma et al. call Ineq. (3) the bipartite extension.

### C-07-028
- Claim: Ma et al. (2013) state that in the erasure setting the system photon shows one of two complementary interference patterns depending on the environment photon's outcome, i.e. fringes exist only conditional on that outcome.
- Source: Ma2013quantum
- Locator: arXiv p. 3 (description of scheme) and Eq. (2)
- Evidence: "In the latter case, it depends on the specific outcome of the environment photon which one out of two different interference patterns the system photon is showing."
- Verified: FULLTEXT
- Notes: Supports C-07-011 and C-07-012 analysis.

### C-07-029
- Claim: Ma et al. (2012) realized Peres's delayed-choice entanglement swapping: the choice was made 14 ns to 313 ns after Alice's and Bob's photons were registered; with the Bell-state measurement the 1-4 state fidelity was 0.681 +/- 0.034 (witness -0.181 +/- 0.034), and with the separable-state measurement it was 0.421 +/- 0.029 (witness 0.078 +/- 0.029).
- Source: Ma2012experimental
- Locator: arXiv main text pp. 4-5; Table 1
- Evidence: "Victor's choice happens in an interval of 14 ns to 313 ns later than Alice and Bob's measurement events"; "The state fidelity F(ρ_exp, |Φ−⟩14) is 0.681 ± 0.034 and the entanglement witness value ... is –0.181 ± 0.034"; "The state fidelity ... is 0.421 ± 0.029 and the entanglement witness value ... is 0.078 ± 0.029"
- Verified: FULLTEXT
- Notes: Published Nature Physics 8, 479-484 (Crossref); the task brief gives p. 480.

### C-07-030
- Claim: Ma et al. (2012) and the RMP review state that no physical influence into the past is needed to explain delayed-choice results if the quantum state is viewed as a catalogue of knowledge, and that the temporal order of the measurements is irrelevant.
- Source: Ma2012experimental; Ma2016delayed
- Locator: Ma 2012 final paragraph; RMP Sec. VI
- Evidence: RMP: "the relative temporal order of measurement events is not relevant, and no physical interactions or signals, let alone into the past, are necessary to explain the experimental results."
- Verified: FULLTEXT
- Notes: Interpretive statement by the experimenters.

### C-07-031
- Claim: The RMP review summarizes Dürr, Nonn & Rempe (1998): which-path information stored in internal atomic states destroyed interference although the momentum disturbance was four orders of magnitude smaller than the fringe period; in Dürr et al.'s words, "the mere fact that which-path information is stored in the detector and could be read out already destroys the interference pattern".
- Source: Ma2016delayed (reporting Durr1998origin)
- Locator: RMP Sec. IV.B, Fig. 20
- Evidence: "the disturbance of the path, which was induced by using microwave pulses, was four orders of magnitude smaller than the fringe period and hence was not able to explain the disappearance of the interference patterns. Instead, 'the mere fact that which-path information is stored in the detector and could be read out already destroys the interference pattern' (Dürr et al., 1998)."
- Verified: FULLTEXT
- Notes: Dürr et al. original: METADATA only (Nature 395, 33-37). Also from RMP: visibilities without marking (75 +/- 1)% and (44 +/- 1)% for t_sep = 105 and 255 microseconds.

### C-07-032
- Claim: Hackermüller et al. (2004) observed C70 interference fringe visibility fall from 47% (no heating) to 29%, 7% and 0% at laser heating powers of 3, 6 and 10.5 W, due to thermal emission of photons carrying which-path information into the environment, in good quantitative agreement with decoherence theory.
- Source: Hackermuller2004decoherence
- Locator: Abstract; Fig. 2 caption; text
- Evidence: "P =0 W (V =47%), P = 3 W (V = 29%), P = 6 W (V = 7%), P = 10.5 W (V=0%)"; "We find good quantitative agreement between our experimental observations and microscopic decoherence theory."
- Verified: FULLTEXT
- Notes: The emitted photons are not detected or recorded by anyone; the which-path information is carried off by the environment.

### C-07-033
- Claim: Hornberger et al. (2003) observed the gradual suppression of C70 interference with increasing background-gas pressure, where colliding gas molecules are left in states distinguishing the path, in quantitative agreement with decoherence theory.
- Source: Hornberger2003collisional
- Locator: Abstract; introduction (arXiv p. 1)
- Evidence: "From the gradual suppression of quantum interference with increasing gas pressure we are able to support quantitatively both the predictions of decoherence theory and our picture of the interaction process."; "the gas particle is left in a state distinguishing the path taken."
- Verified: FULLTEXT
- Notes: none

## D. Other render-on-demand / observer-dependent proposals

### C-07-034
- Claim: Whitworth (2008, arXiv; originally a 2007 CDMTCS research report) argued that if reality is a virtual reality it "would likewise be expected to be calculated only on demand", which could solve the measurement problem, and that non-local collapse could reflect a processor equidistant from all points.
- Source: Whitworth2008physical
- Locator: arXiv 0801.0337, p. 14 (on-demand passage) and p. 9 (item 4, "Non-local effects")
- Evidence: "If what we call reality is a multi-dimensional space-time interface, it would likewise be expected to be calculated only on demand."; "so the non-local collapse of the quantum wave function could be such an effect."
- Verified: FULLTEXT
- Notes: Not peer-reviewed as far as we could determine (Campbell et al. cite it as "CDMTCS Research Report Series, (316), 2007"). No quantitative prediction.

### C-07-035
- Claim: Irwin, Amaral & Chester (2020, Entropy) propose a "self-simulation hypothesis" interpretation of QM, and assert that it became widely agreed that conscious knowledge, rather than physical interaction with a detector, generates the change in the double-slit interference pattern.
- Source: Irwin2020self
- Locator: Abstract; Sec. 2.2, pp. 12-13
- Evidence: "However, as experimental physics and discussion advanced, it became more widely agreed that it is consciousness, i.e., knowledge or thought about the measurement that generates the physical change and not a physical interaction between an artificial or biological detector and system being observed."
- Verified: FULLTEXT
- Notes: This characterization conflicts with the account in the delayed-choice review literature (C-07-019, C-07-031). They also state that Campbell et al.'s tests "could be applied to the SSH" (Sec. 2.3, p. 14). No quantitative prediction.

### C-07-036
- Claim: Irwin et al. cite Radin et al.'s double-slit "mind-matter" experiments as evidence (a "4.4 sigma deviation") and note Tremblay's independent reanalysis.
- Source: Irwin2020self
- Locator: Sec. 2.2, p. 12
- Evidence: "Radin et al. reported evidence of this, showing a 4.4 sigma deviation above the null effect. [76–78]. Tremblay independently analyzed the results to confirm the statistical significance but also identified lesser magnitude statistical anomalies in the control data [79]."
- Verified: FULLTEXT
- Notes: Irwin et al.'s summary of Tremblay conflicts with Tremblay's own abstract (C-07-037), which concludes no evidence of mind-matter interaction for the dataset he reanalysed (Radin, Michel & Delorme 2016). We report Tremblay's stated conclusion.

### C-07-037
- Claim: Tremblay (2019) reanalysed the two-year dataset of Radin, Michel & Delorme (2016), in which participants shifted attention towards or away from a double-slit apparatus; he found the original test's trimming procedure produced uncontrolled false positives, observed visibility shifts in the direction predicted by the mind-matter hypothesis but not significant (p > 0.05), and concluded that the dataset does not contain evidence of mind-matter interaction.
- Source: Tremblay2019independent (on Radin2016psychophysical)
- Locator: Abstract; ref. [1]
- Evidence: "We observe, as in [1], shifts in fringe visibility in the direction expected by the mind-matter interaction hypothesis. However, these shifts are not deemed significant (p > 0.05). Our re-analysis concludes that this particular dataset does not contain evidence of mind-matter interaction."
- Verified: FULLTEXT
- Notes: Radin et al. (2016) original: METADATA only (Physics Essays 29, 14-22). Tremblay's paper was edited by L. K. Shalm (PLoS ONE). Tremblay reanalysed one dataset only.

### C-07-038
- Claim: Arvan (2014) proposed a "peer-to-peer simulation hypothesis" as a unified explanation of quantum phenomena.
- Source: Arvan2014unified
- Locator: title/bibliographic record
- Evidence: Title: "A Unified Explanation of Quantum Phenomena? The Case for the Peer-to-Peer Simulation Hypothesis as an Interdisciplinary Research Program"
- Verified: METADATA
- Notes: Full text not accessible (Wiley and SSRN returned 403). Only existence may be stated.

### C-07-039
- Claim: Yampolskiy's "How to hack the simulation?" preprint (2022) appeared as "How to Escape From the Simulation" in Seeds of Science (March 2023), a journal with public reviewer ("gardener") comments; it does not evaluate evidence for the simulation hypothesis but asks whether agents could escape it.
- Source: Yampolskiy2023how
- Locator: Abstract (p. 1); "Gardener Comments" (pp. 32-35)
- Evidence: "In this paper, we do not evaluate evidence for or against such a claim, but instead ask a computer science question, namely: Can we hack the simulation?"
- Verified: FULLTEXT
- Notes: Venue verified via Crossref DOI 10.53975/wg1s-9j16. The ResearchGate/Twitter title "How to Hack the Simulation?" is the Oct 2022 preprint (not read; we cite the published version).

### C-07-040
- Claim: Yampolskiy's "actionable plan" is to study quantum mechanics for exploitable effects; he suggests quantum phenomena may be interpreted as "computational artifacts or glitches" and that "every novel QM experiment can be seen as an attempt at hacking the simulation"; he also surveys proposals to overload the simulator with computationally intense activity.
- Source: Yampolskiy2023how
- Locator: Sec. 3.6 "Actionable Plan", p. 15; Sec. 3.5, p. 12
- Evidence: "Essentially, every novel QM experiment can be seen as an attempt at hacking the simulation."; "'Spooky', 'Quantum Weirdness' [161] makes a lot of sense if interpreted as computational artifacts or glitches/exploits of the simulators' hardware/software"; "engaging in computationally intense activities in the hopes of overloading the simulator's hardware causing the simulation to crash"
- Verified: FULLTEXT
- Notes: No quantitative prediction or proposed measurement with a stated expected signal. Cites Kim et al. (2000) as an example of "modifying the past" (ref. [168]); the experimenters themselves reject retrocausal readings (C-07-030).

### C-07-041
- Claim: A Seeds of Science reviewer comment printed with Yampolskiy's paper argues that if the simulators cannot see through layers of abstraction, a full-universe simulation is more likely, making attempts to thwart it by computation or by "expanding the human-observed-in-detail cone" fruitless.
- Source: Yampolskiy2023how
- Locator: Gardener Comments ("Evinceo"), p. 35
- Evidence: "if we're in a simulation it's probably the full representation of the whole universe-type, which makes attempts to thwart the simulation by doing computationally intensive tasks or expanding the human-observed-in-detail cone to be larger fruitless."
- Verified: FULLTEXT
- Notes: Reviewer comment, pseudonymous; cite as part of the published article, attribute to "a published reviewer comment".

### C-07-042
- Claim: Chalmers & McQueen (2022) combine integrated information theory with continuous spontaneous localization to build consciousness-collapse models; they state that simple versions are falsified by the quantum Zeno effect while more complex versions remain compatible with evidence and could in principle be tested with quantum computers.
- Source: Chalmers2022consciousness
- Locator: Abstract; Sec. 3 "Superselection and the Zeno problem"; Sec. 7 "Experimental tests"
- Evidence: "Simple versions of the theory are falsified by the quantum Zeno effect, but more complex versions remain compatible with empirical evidence. In principle, versions of the theory can be tested by experiments with quantum computers."
- Verified: FULLTEXT
- Notes: arXiv 2105.02314 (the version read); published in S. Gao (ed.), Consciousness and Quantum Mechanics (OUP 2022), pp. 11-63. This is not a simulation proposal; cited as an example of an observer-dependent collapse hypothesis that makes quantitative, partly falsified predictions.

## E. Superdeterminism, Bell tests and freedom of choice

### C-07-043
- Claim: Hossenfelder & Palmer define a superdeterministic theory as one violating Statistical Independence (hidden-variable distributions independent of measurement settings) and argue that Bell-type tests cannot determine whether Statistical Independence is violated.
- Source: Hossenfelder2020rethinking
- Locator: Abstract; Sec. 3; Sec. 4.3
- Evidence: "A superdeterministic theory is one which violates the assumption of Statistical Independence (that distributions of hidden variables are independent of measurement settings)."; "Violations of Bell's inequality can only tell us that at least one of the assumptions of the theorem was violated."
- Verified: FULLTEXT
- Notes: arXiv v2 read; published Front. Phys. 8:139 (2020).

### C-07-044
- Claim: Hossenfelder & Palmer argue that cosmic Bell tests "do not – cannot – rule out Superdeterminism", only local causation of the correlations by events in the distant past, and that the BIG Bell test cannot prove freedom of choice by assuming it.
- Source: Hossenfelder2020rethinking
- Locator: Sec. 4.3 "The Cosmic Bell Test and the BIG Bell Test"
- Evidence: "this (and similar) experiments do not – cannot – rule out Superdeterminism; they merely rule out that the observed correlations in Bell-type tests were locally caused by events in the distant past."; "one cannot prove freedom of choice by assuming freedom of choice."
- Verified: FULLTEXT
- Notes: Their position; the experimental collaborations frame their results differently (C-07-049, C-07-050).

### C-07-045
- Claim: Hossenfelder & Palmer propose that superdeterminism could be tested by looking for time-correlations (deviations from the Born rule) in sequences of measurements on nearly identically prepared states with small, cold detectors and short time increments; they note the required similarity cannot be specified without a concrete theory.
- Source: Hossenfelder2020rethinking
- Locator: Sec. 6 "Experimental Test"
- Evidence: "rather than fulfilling the Born-rule, such an experiment would reveal time-correlations in the measurement outcomes."; "one should make measurements on states prepared as identically as possible with devices as small and cool as possible in time-increments as small as possible."; "this is not a question which can be answered in generality; for this one would need a theory to make the corresponding calculation."
- Verified: FULLTEXT
- Notes: Proposal; we are not aware of a completed test (not searched exhaustively; outside core scope).

### C-07-046
- Claim: 't Hooft frames his deterministic "theory of everything" through the metaphor of a God who must run a universe on a computer, argues that efficiency favours unambiguous (deterministic) rules and hence a classical rather than quantum computer, and states he sees no objection to superdeterminism.
- Source: tHooft2019free
- Locator: Sec. 2 "God's assignment"; Sec. 3, Demand #1
- Evidence: "Imagine that you were God. Your assignment is: run a universe."; "his computer will have to be a classical computer, not a quantum computer"; "Yet I see no objections against super-determinism, while 'conspiracy' is an ill-defined concept"
- Verified: FULLTEXT
- Notes: 't Hooft marks the God image as metaphorical (footnote 2: "This is only meant metaphorically"). arXiv 1709.02874 read.

### C-07-047
- Claim: 't Hooft's cellular automaton interpretation predicts that quantum computers will not outperform a classical computer with one memory site per Planck volume (or area) operating at one step per Planck time, and he states that a quantum computer beating this bound would falsify the theory.
- Source: tHooft2016cellular
- Locator: Sec. 5.8 "The quantum computer" (arXiv 1405.1548 pp. 78-79)
- Evidence: "these will not be able to function better than a classical computer would do, if its memory sites would be scaled down to one per Planckian volume element"; "If engineers ever succeed in making such quantum computers, it seems to me that the CAT is falsified; no classical theory can explain quantum mechanics."
- Verified: FULLTEXT
- Notes: arXiv version read; the Springer book (2016) is the published edition. Cross-link to the computational-complexity section.

### C-07-048
- Claim: Hensen et al. (2015) reported a loophole-free CHSH violation with electron spins 1.3 km apart: 245 trials, S = 2.42 +/- 0.20, p = 0.039 for a local-realist model.
- Source: Hensen2015loophole
- Locator: Abstract
- Evidence: "We perform 245 trials testing the CHSH-Bell inequality18 S ≤ 2 and find S = 2.42 ± 0.20. A null hypothesis test yields a probability of p = 0.039"
- Verified: FULLTEXT
- Notes: arXiv title differs ("Experimental loophole-free violation..."); published title "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres".

### C-07-049
- Claim: Giustina et al. (2015) reported a significant-loophole-free photonic Bell test with probability under local realism not exceeding 3.74 x 10^-31 (11.5 standard deviations); Shalm et al. (2015) reported p-values as small as 5.9 x 10^-9, and 2.3 x 10^-7 after accounting for setting predictability.
- Source: Giustina2015significant; Shalm2015strong
- Locator: Abstracts
- Evidence: Giustina: "does not exceed 3.74 × 10−31 , corresponding to an 11.5 standard deviation effect."; Shalm: "we compute p-values as small as 5.9×10−9 for our Bell violation"; "our smallest adjusted p-value is 2.3 × 10−7"
- Verified: FULLTEXT
- Notes: INSPIRE lists the Shalm paper under "Stevens" as first author; corrected from Crossref (Shalm first).

### C-07-050
- Claim: The BIG Bell Test (2018) used about 100,000 human participants who generated 97,347,490 binary choices, sent to 13 experiments in 12 laboratories on 30 November 2016, to set measurement bases; the collaboration reports strong contradiction of local realism and frames the result as a conditional: if human will is free, the outcomes are intrinsically random.
- Source: BIGBellTest2018challenging
- Locator: Abstract and first page (arXiv)
- Evidence: "We recruited about 100,000 human participants"; "The participants generated 97,347,490 binary choices, which were directed via a scalable web platform to 12 laboratories on five continents, where 13 experiments tested local realism"; "such experiments can prove the conditional relation: if human will is free, there are physical events (the measurement outcomes in the Bell tests) that are intrinsically random"
- Verified: FULLTEXT
- Notes: The collaboration also lists "closing the 'freedom-of-choice loophole'" among project outcomes; H&P dispute this framing (C-07-044).

### C-07-051
- Claim: Handsteiner et al. (2017) chose Bell-test settings from real-time observations of Milky Way stars, observing violations of >~7.31 sigma and >~11.93 sigma and pushing back by ~600 years the latest time at which local-realist influences could have engineered the violation, assuming fair sampling and that each stellar photon's colour was set at emission.
- Source: Handsteiner2017cosmic
- Locator: Abstract
- Evidence: "we observe statistically significant & 7.31σ and & 11.93σ violations of Bell's inequality with estimated p-values of . 1.8 × 10−13 and . 4.0 × 10−33 , respectively, thereby pushing back by ∼600 years the most recent time by which any local-realist influences could have engineered the observed Bell violation."
- Verified: FULLTEXT
- Notes: "&" and "." in pdftotext output are the ≳ and ≲ symbols.

### C-07-052
- Claim: Rauch et al. (2018) used high-redshift quasars to set measurement bases, observed a Bell violation of 9.3 standard deviations (p <~ 7.4 x 10^-21), and pushed back to at least ~7.8 Gyr ago the most recent time at which local-realist influences could have exploited the freedom-of-choice loophole, excluding such mechanisms from 96% of the space-time volume of the past light cone.
- Source: Rauch2018cosmic
- Locator: Abstract
- Evidence: "we observe statistically significant violation of Bell's inequality by 9.3 standard deviations, corresponding to an estimated p value of . 7.4 × 10−21 . This experiment pushes back to at least ∼7.8 Gyr ago the most recent time by which any local-realist influences could have exploited the 'freedom-of-choice' loophole to engineer the observed Bell violation, excluding any such mechanism from 96% of the space-time volume of the past light cone of our experiment"
- Verified: FULLTEXT
- Notes: Assumes fair sampling and that quasar photon wavelengths were not altered or previewed in transit.

### C-07-053
- Claim: The RMP review notes that space-like separation of the choice in Wheeler's experiment resembles closing the freedom-of-choice loophole in Bell tests, since it excludes causal influence from the emission to the choice.
- Source: Ma2016delayed
- Locator: Sec. II.D (arXiv p. 7)
- Evidence: "it rules out any causal influence from the emission to the choice which might instruct the photon to behave as a particle or as a wave. Note that this resembles the freedom-of-choice loophole"
- Verified: FULLTEXT
- Notes: Relevant to a "simulator that reads the setting in advance" (our analysis in the section).

---

## Items NOT admitted to the .tex (UNVERIFIED or unsuitable)

### C-07-U01
- Claim: Tests at Polytechnique Montréal over three years and seven quantum-erasure experiments falsified one version of Campbell's hypothesis.
- Source: Psi Encyclopedia article on T. W. Campbell (Duggan 2026), citing "Personal communication from David Chartrand (2026)"
- Locator: section "Quantum Experiments", endnote 13
- Evidence: "A personal communication from David Chartrand to the author of this article in 2026 reported that tests at Polytechnique Montréal over three years and seven quantum-erasure experiments had falsified one version of Campbell's simulation hypothesis."
- Verified: UNVERIFIED
- Notes: Secondary source reporting a personal communication; the article itself flags it as provisional. No preprint found. Excluded from .tex; listed in report.

### C-07-U02
- Claim: Turchin & Yampolskiy (2019), "Glitch in the Matrix: Urban Legend or Evidence of the Simulation?", discusses glitch reports as evidence.
- Source: cited as ref. [162] in Yampolskiy2023how (PhilPapers .docx)
- Locator: n/a
- Evidence: n/a
- Verified: UNVERIFIED
- Notes: PhilPapers blocks automated access; not read. Excluded.
