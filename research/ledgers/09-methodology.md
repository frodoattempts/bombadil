# Claim ledger: 09-methodology

Scientific status of the simulation hypothesis: testability, falsifiability,
underdetermination, the adaptive-simulator problem, and reception.

Texts were read in the files saved under `/tmp/claude-0/papers/` (arXiv PDFs
through `pdftotext`, SEP HTML, Europe PMC full-text XML, blog and news HTML).
Access dates for web pages: 2026-09-27.

News articles and press releases (C-09-050 to C-09-058) are cited **only** as
evidence of how results were reported. They are not evidence for any scientific
claim.

---

## A. Testability frameworks

### C-09-001
- Claim: On Popper's demarcation criterion, a theory that is compatible with all possible observations, either by construction or because it has been modified to accommodate them, is unscientific.
- Source: Thornton2026karl
- Locator: SEP "Karl Popper", Sec. 2 (end), paragraph beginning "These factors combined"
- Evidence: "a theory which is compatible with all such observations, either because, as in the case of Marxism, it has been modified solely to accommodate such observations, or because, as in the case of psychoanalytic theories, it is consistent with all possible observations, is unscientific."
- Verified: FULLTEXT
- Notes: Secondary source (SEP) for Popper. We did not read *Logik der Forschung* / *Conjectures and Refutations* directly. SEP entry substantively revised 31 Jul 2026.

### C-09-002
- Claim: For Popper, corroboration counts only when it results from a "risky" prediction that might have turned out false.
- Source: Thornton2026karl
- Locator: SEP "Karl Popper", Sec. 3 "The Problem of Demarcation", paragraph 2
- Evidence: "such “corroboration”, as he terms it, should count scientifically only if it is the positive result of a genuinely “risky” prediction, which might conceivably have been false."
- Verified: FULLTEXT
- Notes: —

### C-09-003
- Claim: Popper held that a theory rescued from failed predictions by ad hoc hypotheses degenerates from science into pseudo-science ("reinforced dogmatism").
- Source: Thornton2026karl
- Locator: SEP "Karl Popper", Sec. 2, paragraph on Marxism
- Evidence: "the theory was saved from falsification by the addition of ad hoc hypotheses which made it compatible with the facts. By this means, Popper asserts, a theory which was initially genuinely scientific degenerated into pseudo-scientific dogma."
- Verified: FULLTEXT
- Notes: Used as the model for the "patching simulator" auxiliary hypothesis.

### C-09-004
- Claim: A standard criticism of Popper (Lakatos) is that high-level theories are protected from refutation by a "protective belt" of auxiliary hypotheses, and are abandoned when their research programme stalls rather than by single critical tests.
- Source: Thornton2026karl
- Locator: SEP "Karl Popper", Sec. 5 (Critical Evaluation), second point
- Evidence: "they are “tenaciously protected from refutation by a vast ‘protective belt’ of auxiliary hypotheses” (Lakatos 1978: 4) and so are falsified, if at all, not by Popperian critical tests, but rather within the elaborate context of the research programmes associated with them gradually grinding to a halt."
- Verified: FULLTEXT
- Notes: Lakatos quoted via SEP.

### C-09-005
- Claim: The SEP distinguishes holist underdetermination (a failed prediction can be blamed on auxiliary hypotheses rather than the hypothesis under test) from contrastive underdetermination (other theories may be equally well confirmed by the same evidence).
- Source: Stanford2023underdetermination
- Locator: SEP "Underdetermination of Scientific Theory", Sec. 1, final two paragraphs
- Evidence: "a failed prediction or falsified empirical consequence typically leaves open to us the possibility of blaming and abandoning one of these background beliefs and/or ‘auxiliary’ hypotheses rather than the hypothesis we set out to test in the first place. But contrastive underdetermination (Section 3 below) involves the quite different possibility that for any body of evidence confirming a theory, there might well be other theories that are also well confirmed by that very same body of evidence."
- Verified: FULLTEXT
- Notes: Entry by P. Kyle Stanford; substantive revision 4 Apr 2023.

### C-09-006
- Claim: Descartes' evil-demon scenario is a form of underdetermination: all sensory experience would be the same whether caused by a deceiver or by an external world.
- Source: Stanford2023underdetermination
- Locator: SEP "Underdetermination of Scientific Theory", Sec. 1, first paragraph
- Evidence: "Descartes’ challenge appeals to a form of underdetermination: he notes that all our sensory experiences would be just the same if they were caused by this Evil Demon rather than an external world of rocks and trees."
- Verified: FULLTEXT
- Notes: The SEP adds that scientific underdetermination arises in ways "that do not simply recreate such radically skeptical possibilities". The unrestricted simulation hypothesis belongs to the sceptical kind.

### C-09-007
- Claim: Empirically equivalent theories (van Fraassen) make the same empirical predictions and so cannot be better or worse supported by any possible evidence.
- Source: Stanford2023underdetermination
- Locator: SEP "Underdetermination of Scientific Theory", Sec. 3.2
- Evidence: "alternative theories making the very same empirical predictions, and which therefore cannot be better or worse supported by any possible body of evidence."
- Verified: FULLTEXT
- Notes: —

### C-09-008
- Claim: In Bayesian confirmation theory, evidence e confirms hypothesis h (relative to background k) if and only if it raises h's probability, P(h|e∧k) > P(h|k), and it is neutral if the probability is unchanged.
- Source: Crupi2025confirmation
- Locator: SEP "Confirmation", Sec. 3.3 "Probabilistic relevance confirmation", definition box
- Evidence: "e relevance-confirms h relative to k if and only if P(h∣e∧k)>P(h∣k); ... e is relevance-neutral for h relative to k if and only if P(h∣e∧k)=P(h∣k)."
- Verified: FULLTEXT
- Notes: Entry by Vincenzo Crupi; substantive revision 4 Aug 2025.

### C-09-009
- Claim: One of the classic families of Bayesian confirmation measures is the likelihood ratio P(e|h∧k)/P(e|¬h∧k).
- Source: Crupi2025confirmation
- Locator: SEP "Confirmation", Sec. 3.3, Theorem 2 (P6)
- Evidence: "(P6) holds if and only if C_P(h,e∣k) is a likelihood ratio measure, that is, if there exists a strictly increasing function f such that ... C_P(h,e∣k)=f[P(e∣h∧k)/P(e∣¬h∧k)]."
- Verified: FULLTEXT
- Notes: The paper uses the likelihood ratio to state when a signature discriminates between a simulation sub-hypothesis and its non-simulation rival (our application, not Crupi's).

### C-09-010
- Claim: Carroll argues that falsifiability tracks two features of good theories: definiteness (not every conceivable set of facts is compatible with the theory) and empiricism.
- Source: Carroll2019beyond
- Locator: arXiv:1801.05016, Sec. 2, p. 4
- Evidence: "Definiteness. A good scientific theory says something specific and inflexible about how nature works. It shouldn’t be possible to take any conceivable set of facts and claim that they are compatible with the theory."
- Verified: FULLTEXT
- Notes: Published as ch. in *Why Trust a Theory?* (CUP 2019), pp. 300-314. We read the arXiv version.

### C-09-011
- Claim: Carroll distinguishes five levels of falsifiability, from (1) no conceivable empirical test that could return a result incompatible with the theory, through tests that are impossible or impractical to perform or cover only part of parameter space, to (5) doable, definitive tests.
- Source: Carroll2019beyond
- Locator: arXiv:1801.05016, Sec. 2, numbered list, p. 5
- Evidence: "1. There is no conceivable empirical test, in principle or in practice or in our imaginations, that could return a result that is incompatible with the theory. ... 4. There exist tests that can be performed, but which will only ever cover a certain subset of parameter space for the theory. ... 5. There exist doable, definitive tests that could falsify a theory."
- Verified: FULLTEXT
- Notes: —

### C-09-012
- Claim: Carroll holds that the important divide is between category 1 and categories 2 to 5; theories in category 1 "don't really even have a chance of being true" and are "not helpful to the scientific enterprise".
- Source: Carroll2019beyond
- Locator: arXiv:1801.05016, Sec. 2, pp. 5-6
- Evidence: "Theories in category 1., by contrast, don’t really even have a chance of being true; they don’t successfully distinguish true things from not-true things, regardless of their testability by empirical means. Such theories are unambiguously not helpful to the scientific enterprise."
- Verified: FULLTEXT
- Notes: Carroll discusses the multiverse, not the simulation hypothesis. Placing the unrestricted SH in category 1 and sub-hypotheses in category 4 is our application.

### C-09-013
- Claim: Carroll notes that some ideas are falsifiable only for certain parameter values; in practice they are tested where possible and interest declines as they are squeezed into smaller regions of parameter space.
- Source: Carroll2019beyond
- Locator: arXiv:1801.05016, Sec. 2, pp. 6-7
- Evidence: "Instead, we test the theory where we can, and our interest in the idea gradually declines as it is squeezed into ever-small regions of parameter space."
- Verified: FULLTEXT
- Notes: Analogy to lattice-spacing bounds: a simulator with finer spacing always survives.

### C-09-014
- Claim: Dawid's *String Theory and the Scientific Method* (2013) argues that string theory is the most conspicuous of several high-energy theories in which non-empirical theory assessment plays an important part.
- Source: Dawid2013string
- Locator: Publisher's book description (Crossref abstract)
- Evidence: "He argues that string theory is just the most conspicuous example of a number of theories in high-energy physics where non-empirical theory assessment has an important part to play."
- Verified: ABSTRACT
- Notes: Book not read in full. Detailed claims are taken from Dawid2019significance.

### C-09-015
- Claim: Dawid names three arguments for non-empirical confirmation: the No Alternatives Argument, the Meta-Inductive Argument from success in the research field, and the Argument of Unexpected Explanatory Interconnections; he frames them in Bayesian terms (confirmation as P(H|E) > P(H)).
- Source: Dawid2019significance
- Locator: arXiv:1702.01133, Sec. 6, p. 17; Eq. (1), p. 7
- Evidence: "NAA: The No Alternatives Argument: Scientists have looked intensely and for a considerable time for alternatives to a known theory H that can solve a given scientific problem but haven’t found any. ... MIA: The Meta-Inductive Argument from success in the research field ... UEA: The Argument of Unexpected Explanatory Interconnections"
- Verified: FULLTEXT
- Notes: Published in *Why Trust a Theory?* (CUP 2019), pp. 99-119. None of the three arguments has been applied to the SH in the literature we found; NAA plainly fails for it because non-simulation alternatives exist for every signature (Sec. C of this ledger).

### C-09-016
- Claim: Ellis and Silk argued that attempts to exempt speculative theories of the Universe from experimental verification undermine science.
- Source: Ellis2014scientific
- Locator: Nature 516, 321 (2014), standfirst
- Evidence: "Attempts to exempt speculative theories of the Universe from experimental verification undermine science, argue George Ellis and Joe Silk."
- Verified: ABSTRACT
- Notes: Paywalled; only the standfirst was readable. Dawid2019significance (p. 7) cites Ellis & Silk as critics of the term "non-empirical confirmation", and Carroll2019beyond (refs [4]) counts them among objectors to the multiverse. Do not attribute specific arguments beyond the standfirst.

### C-09-017
- Claim: Rovelli argues that non-empirical evidence cannot move a theory from "maybe" to "reliable", and that any "no alternatives" argument holds only under assumptions that may be false.
- Source: Rovelli2019dangers
- Locator: arXiv:1609.01966, pp. 1-2
- Evidence: "non-empirical evidence is emphatically insufficient to increase the confidence of a theory to the point where we can consider it established; that is, to move it from “maybe” to “reliable”." / "any “no alternative” argument holds only under a number of assumptions, and these might turn out to be false."
- Verified: FULLTEXT
- Notes: Published in *Why Trust a Theory?* (CUP 2019), pp. 120-124.

### C-09-018
- Claim: Rovelli notes that a theory flexible enough to escape failed predictions is not falsified in Popper's sense, but on a Bayesian view each failure lowers its credibility because a success would have raised it.
- Source: Rovelli2019dangers
- Locator: arXiv:1609.01966, p. 2, right column
- Evidence: "From a Popperian point of view, these failures do not falsify the theory, because the theory is so flexible that it can be adjusted to escape failed predictions. But from a Bayesian point of view, each of these failures decreases the credibility in the theory, because a positive result would have increased it."
- Verified: FULLTEXT
- Notes: Applies to a sub-hypothesis only if a positive result would have raised its probability. For a fully adaptive simulator, a positive result is not expected either (see Sec. D).

## B. The unrestricted hypothesis and published assessments

### C-09-019
- Claim: Bostrom suggests that a simulator tracking observers' belief states could fill in microscopic detail on demand, edit the brain states of observers who notice an anomaly, or rewind and rerun the simulation to avoid the problem.
- Source: Bostrom2003are
- Locator: Sec. III "The technological limits of computation" (p. 5 of the author's preprint at simulation-argument.com; journal pp. 243-255)
- Evidence: "when it saw that a human was about to make an observation of the microscopic world, it could fill in sufficient detail in the simulation in the appropriate domain on an as‐needed basis. Should any error occur, the director could easily edit the states of any brains that have become aware of an anomaly before it spoils the simulation. Alternatively, the director could skip back a few seconds and rerun the simulation in a way that avoids the problem."
- Verified: FULLTEXT
- Notes: Journal page number not verified (we read the preprint). The same passage says only "whatever is required to ensure that the simulated humans ... don’t notice any irregularities" needs simulating.

### C-09-020
- Claim: Bostrom writes that if we are simulated, our best guide to how the simulators set up our world is still ordinary empirical science, and that the chief empirical importance of the simulation proposition lies in its role in the trilemma.
- Source: Bostrom2003are
- Locator: Sec. VI "Interpretation" (p. 13 of the author's preprint)
- Evidence: "Our best guide to how our posthuman creators have chosen to set up our world is the standard empirical study of the universe we see. ... The chief empirical importance of (3) at the current time seems to lie in its role in the tripartite conclusion established above."
- Verified: FULLTEXT
- Notes: Bostrom adds that learning about posthuman motivations and resource constraints could give the hypothesis "a much richer set of empirical implications". Cross-link section 01.

### C-09-021
- Claim: Chalmers argues that no evidence can prove we are not in a simulation, because any such evidence could itself be simulated.
- Source: Chalmers2022can
- Locator: Publisher-authorized excerpt of *Reality+* (Chalmers2022reality), Nautilus, 26 Jan 2022, section "Can you prove you're not in a simulation?"
- Evidence: "Can you prove you’re not in a simulation? You might think you have definitive evidence that you’re not. I think that’s impossible, because any such evidence could be simulated."
- Verified: FULLTEXT
- Notes: The excerpt credits W. W. Norton, 2022. The book was not read in full; page numbers are unknown. Cross-link section 01.

### C-09-022
- Claim: Chalmers holds that we could nevertheless get very strong (though not absolutely conclusive) evidence that we are in a simulation, for example if the simulators showed us the source code or manipulated the world on request.
- Source: Chalmers2022can
- Locator: Nautilus excerpt of *Reality+*, final paragraphs
- Evidence: "Still, we certainly could get very strong evidence that we’re in a simulation. The simulators could lift the Sydney Harbor Bridge into the air and turn it upside down. They could show us the source code of the simulation. ... Even this evidence would fall short of absolute proof that we’re in a simulation."
- Verified: FULLTEXT
- Notes: This asymmetry (confirmable in principle by simulator disclosure, not refutable) is central to our Sec. 9.2.

### C-09-023
- Claim: Chalmers argues that we should take the simulation hypothesis seriously and that we cannot rule it out.
- Source: Chalmers2024taking
- Locator: Philos. Phenomenol. Res. 109(3), 1058-1067 (2024), opening paragraph (p. 1)
- Evidence: "I argue that we should take the simulation hypothesis seriously, and that we cannot rule it out."
- Verified: FULLTEXT
- Notes: Symposium reply to Godfrey-Smith, Schneider and Schwitzgebel. Author-hosted PDF (consc.net) of the published version.

### C-09-024
- Claim: Hossenfelder calls the simulation hypothesis unscientific and "not a serious scientific argument", something one would have to believe on faith rather than logic, while stating that this does not mean it is wrong.
- Source: Hossenfelder2021simulation
- Locator: Blog post "The Simulation Hypothesis is Pseudoscience", Backreaction, 13 Feb 2021 (video transcript), final paragraph
- Evidence: "The simulation hypothesis, therefore, just isn’t a serious scientific argument. This doesn’t mean it’s wrong, but it means you’d have to believe it because you have faith, not because you have logic on your side."
- Verified: FULLTEXT
- Notes: Blog/video, cited as the object of study (a widely discussed critique). Her book *Existential Physics* (2022) was NOT read, so it is not cited.

### C-09-025
- Claim: Hossenfelder's central objection is that the hypothesis assumes, without explanation, that all observations can be reproduced by an algorithm other than the confirmed laws; she notes that algorithmic reproductions of natural laws are usually incompatible with the symmetries of special and general relativity and that searches for such effects have found nothing.
- Source: Hossenfelder2021simulation
- Locator: Same post, paragraphs "The problematic part of Boström’s argument..." and "But nobody presently knows how..."
- Evidence: "he assumes it is possible to reproduce all our observations using not the natural laws that physicists have confirmed to extremely high precision, but using a different, underlying algorithm" / "physicists have looked for signs that natural laws really proceed step by step, like in a computer code, but their search has come up empty handed. It’s possible to tell the difference because attempts to algorithmically reproduce natural laws are usually incompatible with the symmetries of Einstein’s theories of special and general relativity."
- Verified: FULLTEXT
- Notes: She also argues that "fill in on demand" rendering is unexplained, citing sub-grid parametrization in climate models.

### C-09-026
- Claim: Hossenfelder questions the adaptive-simulator move: how would the programmer notice that a simulated mind is about to notice a contradiction and fix it in time, and where would consistent data come from?
- Source: Hossenfelder2017no
- Locator: Blog post "No, we probably don't live in a computer simulation", Backreaction, 15 Mar 2017, paragraphs 10-11
- Evidence: "But how does the programmer notice a simulated mind is about to notice contradictions and how does he or she manage to quickly fix the problem? If the programmer could predict in advance what the brain will investigate next, it would be pointless to run the simulation to begin with."
- Verified: FULLTEXT
- Notes: The same post says the trivial reading ("the universe computes the laws of nature") is "tautologically true" and "meaningless".

### C-09-027
- Claim: Aaronson argued that the Ringel-Kovrizhin paper did not claim, and could not show, that the universe is not a simulation: it concerns one algorithmic framework (local, sign-free QMC); there is no unconditional proof that quantum systems cannot be efficiently simulated classically; a simulator could be a quantum computer; and a classical simulator could simply take exponentially long.
- Source: Aaronson2017because
- Locator: Blog post "Because you asked: the Simulation Hypothesis has not been falsified; remains unfalsifiable", Shtetl-Optimized, 3 Oct 2017
- Evidence: "OK, but does any of this prove that the universe isn’t a computer simulation, as the popular articles claim (and as the original paper does not)?" / "why not just imagine that the universe is being simulated on a quantum computer?" / "why couldn’t God, using Her classical computer, spend a trillion years to simulate one second as subjectively perceived by us?"
- Verified: FULLTEXT
- Notes: Blog, cited as a published assessment by a complexity theorist.

### C-09-028
- Claim: Vazza concludes that the simulation hypothesis can be "reasonably well tested" only for simulating universes that obey the same physics as ours; whether universes with entirely different laws could simulate ours appears to lie outside what is scientifically testable.
- Source: Vazza2025astrophysical
- Locator: arXiv:2504.08461, Sec. 4.6 and Sec. 5 (Conclusions)
- Evidence: "our modelling shows that the SH can be reasonably well tested only with respect to universes which are at least playing according to the Physics play book - while everything else appears beyond the bounds of falsifiability and even theoretical speculation." / "the question whether universes with entirely different sets of physical laws or dimensionalities could produce our Universe as a simulation, seems to be be entirely outside of what is scientifically testable, even in theory."
- Verified: FULLTEXT
- Notes: Peer-reviewed (Front. Phys. 13, 1561873). Vazza also notes (Sec. 1) that the topic "at first sight ... might seem to be entirely out of the boundaries of falsifiability".

### C-09-029
- Claim: Vazza finds that the energy or power required by every simulation scenario he models (whole visible Universe, Earth only, low-resolution Earth) is incompatible with physics or astronomically large for a simulator in a universe like ours.
- Source: Vazza2025astrophysical
- Locator: arXiv:2504.08461, Abstract; Sec. 5
- Evidence: "In all cases, the amounts of energy or power required by any version of the simulation hypothesis are entirely incompatible with physics, or (literally) astronomically large, even in the lowest resolution case."
- Verified: FULLTEXT
- Notes: The conclusion is conditional on the simulator sharing our physics; details belong in section 06.

### C-09-030
- Claim: Wolpert argues that experimental approaches can give only partial answers, because they rest on assumptions such as a digital simulating computer or observable "bugs".
- Source: Wolpert2025what
- Locator: arXiv:2404.16050v5, Sec. 1 (Introduction), p. 3
- Evidence: "some physicists have focused on whether there might be ways of experimentally determining whether our universe is a program in a simulation [13, 11, 9]. Work in this vein can only provide partial answers to the question of whether we are a simulation, at best. For example, some of this work first make the assumption that the simulating computer is digital"
- Verified: FULLTEXT
- Notes: The arXiv v5 title is "Implications of computer science theory for the simulation hypothesis". The published title is "What computer science has to say about the simulation hypothesis", J. Phys. Complexity 6, 045010 (2025). We read arXiv v5.

### C-09-031
- Claim: Wolpert notes that beings simulated through fully homomorphic encryption could not tell this apart from a direct simulation of their laws of physics.
- Source: Wolpert2025what
- Locator: arXiv:2404.16050v5, section "Running (self-)simulation using fully homomorphic encryption", p. 34-35
- Evidence: "there is no way that they would be able to distinguish between being produced in a simulation being made via an FHE algorithm, or instead in some simulation that is easier to understand."
- Verified: FULLTEXT
- Notes: An example of implementation-level underdetermination.

### C-09-032
- Claim: Beane, Davoudi and Savage assume a classical computer simulating the universe on a hyper-cubic lattice with an unimproved Wilson action, and derive the bound b^-1 ≳ 10^11 GeV from the high-energy cut-off of the cosmic-ray spectrum; they propose that the highest-energy cosmic rays could show rotational-symmetry breaking reflecting the lattice.
- Source: Beane2014constraints
- Locator: arXiv:1210.1847v2, Abstract; Sec. I, p. 5
- Evidence: "we assume that our universe is an early numerical simulation with unimproved Wilson fermion discretization ... the most stringent bound on the inverse lattice spacing of the universe, b^-1 >~ 10^11 GeV, is derived from the high-energy cut off of the cosmic ray spectrum. The numerical simulation scenario could reveal itself in the distributions of the highest energy cosmic rays exhibiting a degree of rotational symmetry breaking"
- Verified: FULLTEXT
- Notes: This is a bound, not a detection. Physics details are in sections 03/04.

### C-09-033
- Claim: Beane et al. note that lattice improvement "masks much of our ability to probe" the simulation possibility (O(b^2) operators easily avoid obvious probes, apart from dispersion-relation effects), but argue that finite simulator resources imply a non-zero lattice spacing, so that discovery always remains possible in principle.
- Source: Beane2014constraints
- Locator: arXiv:1210.1847v2, Sec. V (Conclusions), p. 12
- Evidence: "Of course, improvement in this context masks much of our ability to probe the possibility that our universe is a simulation, and we have seen that, with the exception of the modifications to the dispersion relation and the associated maximum values of energy and momentum, even O(b^2) operators in the Symanzik action easily avoid obvious experimental probes. Nevertheless, assuming that the universe is finite and therefore the resources of potential simulators are finite, then a volume containing a simulation will be finite and a lattice spacing must be non-zero, and therefore in principle there always remains the possibility for the simulated to discover the simulators."
- Verified: FULLTEXT
- Notes: The in-principle discoverability depends on the finite-resource premise.

### C-09-034
- Claim: Beane et al. note that in the simulation scenario the lattice energy scale could lie orders of magnitude below the Planck scale.
- Source: Beane2014constraints
- Locator: arXiv:1210.1847v2, Sec. V, p. 12
- Evidence: "It is interesting to note that in the simulation scenario, the fundamental energy scale defined by the lattice spacing can be orders of magnitude smaller than the Planck scale, in which case the conflict between quantum mechanics and gravity should be absent."
- Verified: FULLTEXT
- Notes: A sub-Planckian discreteness scale is a feature that would separate H-grid from Planck-scale quantum-gravity discreteness, if it were observed.

### C-09-035
- Claim: Barrow argues that simulators with incomplete knowledge of the laws of nature would have to patch their simulations, so that simulated scientists could observe occasional glitches and slow drifts in the constants of nature.
- Source: Barrow2007living
- Locator: *Universe or Multiverse?* ch. 27, pp. 481-486; author's text at simulation-argument.com/barrowsim.pdf, pp. 3-4
- Evidence: "The only escape is if their creators intervene to patch up the problems one by one as they arise." / "So we conclude that if we live in a simulated reality we should expect occasional sudden glitches, small drifts in the supposed constants and laws of Nature over time"
- Verified: FULLTEXT
- Notes: Barrow cites the Webb et al. (2001) fine-structure-constant claim (his ref. 7) as the kind of drift that simulated astronomers might observe. The author PDF may differ in pagination from the CUP chapter.

### C-09-036
- Claim: Campbell et al. assume a simulator with limited resources that renders content only when information becomes available to an observer, and that must balance consistency against avoiding detection; they propose wave-particle-duality (delayed-choice) experiments to test this.
- Source: Campbell2017on
- Locator: arXiv:1703.00058v2, Abstract; Sec. 3-4, pp. 4-5
- Evidence: "a good/effective VR would operate based on two, possibly conflicting, requirements: (1) preserving the consistency of the VR (2) avoiding detection (from the players that they are in a VR). However, the resolution of such a conflict would be limited by computational resources"
- Verified: FULLTEXT
- Notes: Proposal; no performed experiment is reported in this paper. Published in Int. J. Quantum Found. 3, 78-99 (2017). Cross-link section 07.

### C-09-037
- Claim: Campbell et al. acknowledge that their rendering perspective supports the von Neumann-Wigner postulate that consciousness is needed to complete quantum theory, a non-simulation interpretation that makes the same qualitative prediction.
- Source: Campbell2017on
- Locator: arXiv:1703.00058v2, Sec. 3, p. 5
- Evidence: "Although this perspective supports the Von Neumann-Wigner postulate that [48, 53] human consciousness is necessary for the completion of quantum theory, the simulation theory also agrees with Copenhagen in the sense that it does not require the actual existence of quantum waves or their collapse"
- Verified: FULLTEXT
- Notes: Evidence of degeneracy for H-lazy, stated by the proponents themselves.

### C-09-038
- Claim: Hsu and Zee argue that a creator of the universe, if one exists, could have left a message in the cosmic microwave background by adjusting the fundamental Lagrangian, without later intervention.
- Source: Hsu2006message
- Locator: arXiv:physics/0510102, Abstract
- Evidence: "We argue that the cosmic microwave background (CMB) provides a stupendous opportunity for the Creator of universe our (assuming one exists) to have sent a message to its occupants, using known physics. ... it requires only careful adjustment of the fundamental Lagrangian, but no direct intervention in the subsequent evolution of the universe."
- Verified: FULLTEXT
- Notes: Beane et al. (footnote 5) link Hsu-Zee to the simulation scenario. This is an example of the "disclosure" kind of evidence (cf. C-09-022). Typo "universe our" is in the original.

## C. Non-simulation alternatives for each signature

### C-09-039
- Claim: Tests of Lorentz invariance are motivated by quantum-gravity ideas; Lorentz violation has been studied in several quantum-gravity models, though none predicts it conclusively.
- Source: Mattingly2005modern
- Locator: arXiv:gr-qc/0502097, Abstract and Sec. 1
- Evidence: "The possibility of four dimensional Lorentz violation has been investigated in different quantum gravity models (including string theory [185, 107], warped brane worlds [70], and loop quantum gravity [120]), although no quantum gravity model predicts Lorentz violation conclusively."
- Verified: FULLTEXT
- Notes: Non-simulation alternative for H-grid dispersion signatures.

### C-09-040
- Claim: Dowker, Henson and Sorkin argue that fundamental spacetime discreteness need not violate Lorentz invariance: causal-set discreteness (a Poisson sprinkling) is locally Lorentz invariant, and its phenomenology includes a Lorentz-invariant momentum diffusion ("swerves").
- Source: Dowker2004quantum
- Locator: arXiv:gr-qc/0311055, Abstract; pp. 3-6
- Evidence: "Contrary to what is often stated, a fundamental spacetime discreteness need not contradict Lorentz invariance. A causal set’s discreteness is in fact locally Lorentz invariant ... The particles undergo a Lorentz invariant diffusion in phase space"
- Verified: FULLTEXT
- Notes: Alternative for H-grid. It is also a discretization a simulator could use, which removes the anisotropy signature.

### C-09-041
- Claim: Collins et al. show that a Planck-scale preferred frame combined with known particle interactions generically yields percent-level Lorentz violation at low energies unless bare parameters are strongly fine-tuned.
- Source: Collins2004lorentz
- Locator: arXiv:gr-qc/0403053, Abstract
- Evidence: "combining known elementary particle interactions with a Planck-scale preferred frame gives rise to Lorentz violation at the percent level, some 20 orders of magnitude higher than earlier estimates, unless the bare parameters of the theory are unnaturally strongly fine-tuned."
- Verified: FULLTEXT
- Notes: Applies to naive preferred-frame discreteness whether or not it is simulated.

### C-09-042
- Claim: Minimal-length scenarios (generalized uncertainty principle, modified dispersion relations) arise in several approaches to quantum gravity.
- Source: Hossenfelder2013minimal
- Locator: arXiv:1203.6191, Abstract
- Evidence: "we examine what insights can be gained from thought experiments for probes of shortest distances, and summarize what can be learned from different approaches to a theory of quantum gravity. Then we discuss some models that have been developed to implement a minimal length scale ... the generalized uncertainty principle or the modified dispersion relation"
- Verified: ABSTRACT
- Notes: Read the abstract page of the arXiv PDF only.

### C-09-043
- Claim: Hogan proposed a model of Planckian quantum geometry (motivated by black-hole entropy and holography, not by any simulator) that predicts directionally coherent transverse position noise, testable with co-located interferometers.
- Source: Hogan2012interferometers
- Locator: arXiv:1002.4880v27, Abstract
- Evidence: "The amplitude of the effect in physical units is predicted with no parameters, by equating the number of degrees of freedom of position wavefunctions on a 2D spacelike surface with the entropy density of a black hole event horizon of the same area. ... It is proposed that nearly co-located Michelson interferometers of laboratory scale, cross-correlated at high frequency, can test the Planckian noise prediction with current technology."
- Verified: FULLTEXT
- Notes: Non-simulation alternative for H-noise. Section 05 covers details.

### C-09-044
- Claim: The Fermilab Holometer excluded the specific holographic-noise model it tested at 5.1σ statistical significance (4.6σ including 10% calibration uncertainty), equivalently constraining its normalization to below 44% of the predicted value at 95% CL; the authors stress that this applies only to that model's spectral shape.
- Source: Chou2016first
- Locator: arXiv:1512.01216v2, final results paragraph before "Conclusions"
- Evidence: "The model of Eq. 1 is thus excluded with 5.1σ statistical significance, reduced by the 10% calibration uncertainty to 4.6σ. Alternatively, the result may be viewed as a constraint on the normalization of this model to be less than 44% of the predicted value at 95% confidence level. It should be emphasized that these results apply only to the spectral shape of the particular model used here."
- Verified: FULLTEXT
- Notes: A null result for one specific model. It is not a test of the simulation hypothesis.

### C-09-045
- Claim: The final first-generation Holometer analysis placed constraints on shear-noise correlation models with sensitivity exceeding the Planck-scale holographic information bound on position states by a large factor.
- Source: Chou2017interferometric
- Locator: arXiv:1703.08503v2, Abstract
- Evidence: "General experimental constraints are placed on parameters of a set of models of spatial shear noise correlations, with a sensitivity that exceeds the Planck-scale holographic information bound on position states by a large factor."
- Verified: ABSTRACT
- Notes: —

### C-09-046
- Claim: Collapse models (continuous spontaneous localization) modify the Schrödinger equation non-linearly and stochastically; their predictions agree with quantum theory for microscopic systems but differ appreciably near the macroscopic scale, and are being confronted by molecular interferometry and optomechanics experiments.
- Source: Bassi2013models
- Locator: arXiv:1204.4325, Abstract
- Evidence: "we review an experimentally falsifiable phenomenological proposal, known as Continuous Spontaneous Collapse: a stochastic non-linear modification of the Schrödinger equation ... As one approaches the macroscopic scale, predictions of this proposal begin to differ appreciably from those of quantum theory, and are being confronted by ongoing laboratory experiments that include molecular interferometry and optomechanics."
- Verified: FULLTEXT
- Notes: Non-simulation alternative for any H-lazy "deviation from QM" signature.

### C-09-047
- Claim: Lloyd estimates, from known physics and with no simulator assumed, that the universe can have performed at most about 10^120 elementary operations on about 10^90 bits.
- Source: Lloyd2002computational
- Locator: arXiv:quant-ph/0110141, Abstract
- Evidence: "The universe can have performed no more than 10^120 ops on 10^90 bits."
- Verified: FULLTEXT
- Notes: Supports the point that "information is physical" constraints are standard physics (Lloyd opens with Landauer's "Information is physical"). Lloyd gives ~10^120 bits when gravitational degrees of freedom are included (body text; not needed here).

### C-09-048
- Claim: Aaronson asks whether the "NP Hardness Assumption", that NP-complete problems are intractable in the physical world, should be regarded as a principle of physics, and lists constraints it would impose (e.g. no non-linear corrections to the Schrödinger equation, no closed timelike curves).
- Source: Aaronson2005np
- Locator: arXiv:quant-ph/0502072v2, Sec. 10 "Discussion", p. 17-18
- Evidence: "So, should the “NP Hardness Assumption”—loosely speaking, that NP-complete problems are intractable in the physical world—eventually be seen as a principle of physics?"
- Verified: FULLTEXT
- Notes: A non-simulation route to "bounded computation" signatures (H-budget).

### C-09-049
- Claim: A fundamental constant that varies in space or time would reflect an almost massless field coupled to matter, which would induce violations of the universality of free fall.
- Source: Uzan2011varying
- Locator: arXiv:1009.5514, Abstract
- Evidence: "Any constant varying in space and/or time would reflect the existence of an almost massless field that couples to matter. This will induce a violation of the universality of free fall."
- Verified: FULLTEXT
- Notes: Non-simulation alternative for Barrow's "drifting constants" signature (H-patch).

## D. Reception: what was reported versus what was claimed

### C-09-050
- Claim: [Reporting] The University of Washington release on Beane et al., reproduced by ScienceDaily (10 Dec 2012), was headlined "Researchers say idea can be tested" and quoted Savage: "This is the first testable signature of such an idea."
- Source: UW2012do
- Locator: ScienceDaily, 10 Dec 2012, headline and paragraph 9
- Evidence: "Do we live in a computer simulation run by our descendants? Researchers say idea can be tested" / "“This is the first testable signature of such an idea,” Savage said."
- Verified: FULLTEXT
- Notes: News or press release. Cite only as reporting. Compare with C-09-032/033: what was testable was one specific lattice design, and the paper states that improvement masks the signal. This release is relatively measured compared with the cases below.

### C-09-051
- Claim: Ringel and Kovrizhin show that quantized gravitational responses (e.g. thermal Hall conductance in fractional quantum Hall states) obstruct local sign-free quantum Monte Carlo for bosonic systems; the paper does not mention the universe or the simulation hypothesis.
- Source: Ringel2017quantized
- Locator: Sci. Adv. 3, e1701758 (2017), Abstract and Discussion (Europe PMC full text PMC5617380)
- Evidence: "we show that quantized gravitational responses appear as obstructions to local sign-free QMC." Discussion: "we suggested that nontrivial gravitational/geometrical responses can be identified with obstructions to sign-free local QMC simulations."
- Verified: FULLTEXT
- Notes: A full-text search of the Europe PMC XML finds zero occurrences of "universe", "Bostrom", "simulation hypothesis" or "reality". The paper also states: "Establishing an obstruction to a classical simulation is a rather ill-defined task."

### C-09-052
- Claim: [Reporting] PBS NOVA Next (3 Oct 2017) reported the Ringel-Kovrizhin paper under the headline "Physicists Confirm That We're Not Living In a Computer Simulation" and wrote that "classical computers most certainly aren't controlling our universe".
- Source: Eck2017physicists
- Locator: PBS NOVA Next, A. Eck, 3 Oct 2017, headline, standfirst and paragraph 3
- Evidence: "Scientists have discovered that it’s impossible to model the physics of our universe on even the biggest computer. What that means is that we’re probably not living in a computer simulation." / "Therefore, according to Ringel and Kovrizhin, classical computers most certainly aren’t controlling our universe."
- Verified: FULLTEXT
- Notes: News. The same article was reposted by American Friends of the Hebrew University (afhu.org, 4 Oct 2017). Aaronson (C-09-027) quotes another headline, "Researchers claim to have found proof we are NOT living in a simulation".

### C-09-053
- Claim: [Reporting] Futurism (6 Oct 2017) reported that both authors had said they were surprised by the headlines, and that Ringel told New Scientist that whether we live in a simulation is not a scientific question.
- Source: Galeon2017fact
- Locator: Futurism, D. Galeon, 6 Oct 2017, paragraph 2
- Evidence: "Both Ringel and Kovrizhin have since come out to say they were surprised by the headlines generated by their study on simulation theory because, as Ringel told New Scientist, whether or not we live in a computer simulation is not even a scientific question."
- Verified: FULLTEXT
- Notes: Second-hand report. The primary New Scientist article (newscientist.com/article/2149627) could not be fetched (blocked), so Ringel's actual wording is UNVERIFIED. If used in the paper, it must be attributed to Futurism's report.

### C-09-054
- Claim: Vopson's 2023 AIP Advances paper states in its abstract that it provides "scientific evidence that appears to underpin the simulated universe hypothesis", while also describing the hypothesis as lacking evidence.
- Source: Vopson2023second
- Locator: AIP Adv. 13, 105308 (2023), Abstract (via Crossref)
- Evidence: "Despite the lack of evidence, this idea is gaining traction in scientific circles as well as in the entertainment industry. ... we re-examine the second law of infodynamics and its applicability to digital information, genetic information, atomic physics, mathematical symmetries, and cosmology, and we provide scientific evidence that appears to underpin the simulated universe hypothesis."
- Verified: ABSTRACT
- Notes: The full text could not be fetched (publisher and repository behind a bot check). Section 08 must supply full-text details.

### C-09-055
- Claim: [Reporting] Vice/Motherboard (11 Oct 2023) headlined the paper "Mind-Blowing New Law of Physics Could Mean We Really Live in a Simulation"; in the same article Vopson is quoted as saying that the study alone is not sufficient to state that we live in a simulation, and that the second law of infodynamics "is valid regardless of whether the universe is a simulation or not".
- Source: Ferreira2023mind
- Locator: Vice, B. Ferreira, 11 Oct 2023, headline and paragraphs quoting Vopson
- Evidence: "“However, to categorically state that we live in a simulation, based only on this study, is not sufficient.”" / "“It is important to remember that the second law of infodynamics is valid regardless of whether the universe is a simulation or not,” he said."
- Verified: FULLTEXT
- Notes: News. The author's quoted statement concedes that the proposed law does not discriminate between the hypotheses (degeneracy).

### C-09-056
- Claim: Faizal, Krauss, Shabir and Marino argue from Gödel, Tarski and Chaitin incompleteness that a wholly algorithmic theory of everything is impossible, and conclude that, since any simulation would be algorithmic, "the universe cannot be a simulation" and that the simulation hypothesis is "logically impossible rather than merely implausible".
- Source: Faizal2025consequences
- Locator: arXiv:2507.22950v1, Abstract; penultimate section (p. 8)
- Evidence: "Because any putative simulation of the universe would itself be algorithmic, this framework also implies that the universe cannot be a simulation." / "Since it is impossible to simulate a complete and consistent universe, our universe is definitely not a simulation. As the universe is produced by MToE, the simulation hypothesis is logically impossible rather than merely implausible."
- Verified: FULLTEXT
- Notes: Unlike the Ringel-Kovrizhin case, the strong claim is in the paper itself. The argument models quantum gravity as an axiomatic structure from which spacetime is generated algorithmically (Abstract: "Quantum gravity is therefore envisaged as an axiomatic structure, and algorithmic calculations acting on these axioms are expected to generate spacetime") and posits a non-algorithmic "Meta-Theory of Everything". Journal: J. Holography Appl. Phys. 5(2), 10-21 (2025). Section 06 covers the logic.

### C-09-057
- Claim: [Reporting] UBC Okanagan's release (30 Oct 2025) stated that the research "mathematically proven" a simulated universe to be "impossible" and "provides a definitive answer".
- Source: UBCO2025ubco
- Locator: UBC Okanagan News, 30 Oct 2025, paragraphs 2 and final
- Evidence: "But new research from UBC Okanagan has mathematically proven this isn’t just unlikely—it’s impossible." / "This research brings it firmly into the domain of mathematics and physics, and provides a definitive answer."
- Verified: FULLTEXT
- Notes: Press release (institutional). Cite only as reporting.

### C-09-058
- Claim: [Reporting] ScienceDaily republished the release (10 Nov 2025) under the headline "Physicists prove the Universe isn't a simulation after all".
- Source: ScienceDaily2025physicists
- Locator: ScienceDaily, 10 Nov 2025, headline; "Source: University of British Columbia Okanagan campus"
- Evidence: "Physicists prove the Universe isn’t a simulation after all" / "Researchers have mathematically proven that our universe cannot be a simulation."
- Verified: FULLTEXT
- Notes: Republished press release.

### C-09-059
- Claim: A comment posted to arXiv argues that Gödelian undecidability limits what can be proven within a formal system, not what can be computed or executed, so Faizal et al.'s conclusion does not follow without evidence of hypercomputation in nature.
- Source: Redden2025provability
- Locator: arXiv:2512.11807v1, Abstract
- Evidence: "undecidability constrains provability but not computability or execution. Unless physical phenomena require the resolution of undecidable propositions, incompleteness alone does not imply a guaranteed failure in execution. Thus, the claim that the universe cannot be simulated lacks empirical and logical justification without evidence of hypercomputation in nature."
- Verified: FULLTEXT
- Notes: arXiv preprint (physics.hist-ph); no journal publication found. Section 06 owns the substantive assessment.

### C-09-060
- Claim: The 17th Isaac Asimov Memorial Debate, "Is the Universe a Simulation?", was held at the American Museum of Natural History on 5 April 2016, hosted and moderated by Neil deGrasse Tyson with panelists David Chalmers, Zohreh Davoudi, James Gates, Lisa Randall and Max Tegmark.
- Source: AMNH2016is
- Locator: Official AMNH video description, YouTube id wgSZA3NPpBs (event page amnh.org/explore/videos/isaac-asimov-memorial-debate/2016)
- Evidence: "The 17th annual Isaac Asimov Memorial Debate took place at The American Museum of Natural History on April 5, 2016. ... 2016 Asimov Panelists: David Chalmers ... Zohreh Davoudi ... James Gates ... Lisa Randall ... Max Tegmark" / "Neil deGrasse Tyson, Frederick P. Rose Director of the Hayden Planetarium, hosts and moderates"
- Verified: METADATA
- Notes: Event only. We did not watch or transcribe it, so the paper must not attribute any statement from the debate to any panelist. The amnh.org page returned a CAPTCHA; details are from AMNH's own YouTube channel description. Vazza2025astrophysical (footnote 1) also mentions the debate.
