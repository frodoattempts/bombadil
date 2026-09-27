# Claim ledger: 01-philosophy (simulation argument in philosophy and formal epistemology)

Conventions for this ledger:
- Quotes are verbatim from the text we read, except that typographic hyphens and
  quotation marks are normalized to ASCII and PDF line breaks are joined.
- "Preprint" locators refer to the author-hosted version we read; where it is not the
  version of record this is stated in Notes. Section numbers are given because
  preprint pagination differs from the journal's.
- Local copies are in /tmp/claude-0/papers/ (filenames in Notes where useful).

---

## A. Bostrom (2003): the original argument

### C-01-001
- Claim: Bostrom argues that at least one of three propositions is true: (1) the human species is very likely to go extinct before reaching a "posthuman" stage; (2) any posthuman civilization is extremely unlikely to run a significant number of simulations of its evolutionary history; (3) we are almost certainly living in a computer simulation.
- Source: Bostrom2003are
- Locator: Abstract; restated in §VII (Conclusion)
- Evidence: "This paper argues that at least one of the following propositions is true: (1) the human species is very likely to go extinct before reaching a "posthuman" stage; (2) any posthuman civilization is extremely unlikely to run a significant number of simulations of their evolutionary history (or variations thereof); (3) we are almost certainly living in a computer simulation."
- Verified: FULLTEXT
- Notes: Read the author's preprint from simulation-argument.com (sa_simulation.pdf), which is headed "Published in Philosophical Quarterly (2003) Vol. 53, No. 211, pp. 243-255". The preprint is titled "Are You Living in a Computer Simulation?"; the version of record (Crossref) is titled "Are We Living in a Computer Simulation?". Use the published title in the bibliography.

### C-01-002
- Claim: The argument assumes a weak "substrate-independence" thesis: that a computer running a program which replicates the computational processes of a human brain in sufficiently fine-grained detail (e.g. at the level of individual synapses) would in fact have conscious experiences; Bostrom takes this as given rather than arguing for it.
- Source: Bostrom2003are
- Locator: §II "The assumption of substrate-independence" (preprint pp. 2-3)
- Evidence: "although it is not entirely uncontroversial, we shall here take it as a given." ... "We need only the weaker assumption that it would suffice for the generation of subjective experiences that the computational processes of a human brain are structurally replicated in suitably fine-grained detail, such as on the level of individual synapses."
- Verified: FULLTEXT
- Notes: He explicitly denies needing that substrate-independence be necessarily true: "just that, in fact, a computer running a suitable program would be conscious."

### C-01-003
- Claim: Bostrom estimates the processing needed to emulate a human brain at ~10^14 operations per second (from retinal-processing extrapolation) or ~10^16-10^17 operations per second (from synapse counts and firing rates), and the maximum human sensory bandwidth at ~10^8 bits per second.
- Source: Bostrom2003are
- Locator: §III "The technological limits of computation" (preprint p. 4)
- Evidence: "yields a figure of ~10^14 operations per second for the entire human brain." ... "gives a figure of ~10^16-10^17 operations per second." ... "the maximum human sensory bandwidth is ~10^8 bits per second"
- Verified: FULLTEXT
- Notes: Superscripts lost in text extraction ("1014", "1016-1017", "108"); values confirmed by context and by the footnote-10 product below. Sources Bostrom cites: Moravec (1989) and Bostrom (1998).

### C-01-004
- Claim: Bostrom's rough estimate of the computation needed to simulate the mental history of humankind is 10^33-10^36 operations, obtained as 100 billion humans x 50 years/human x 30 million s/year x [10^14, 10^17] operations per brain per second.
- Source: Bostrom2003are
- Locator: §III and footnote 10 (preprint pp. 5-6)
- Evidence: "we can use ~10^33 - 10^36 operations as a rough estimate" ; fn 10: "100 billion humans x 50 years/human x 30 million secs/year x [10^14, 10^17] operations in each human brain per second ~ [10^33, 10^36] operations."
- Verified: FULLTEXT
- Notes: Bostrom states "even if our estimate is off by several orders of magnitude, this does not matter much for our argument."

### C-01-005
- Claim: Bostrom takes ~10^42 operations per second as a rough figure for a planetary-mass computer built from known nanotechnological designs, and infers that one such computer could simulate the entire mental history of humankind using less than one millionth of its processing power for one second.
- Source: Bostrom2003are
- Locator: §III (preprint pp. 4, 6)
- Evidence: "a rough approximation of the computational power of a planetary-mass computer is 10^42 operations per second, and that assumes only already known nanotechnological designs" ... "A single such a computer could simulate the entire mental history of humankind (call this an ancestor-simulation) by using less than one millionth of its processing power for one second."
- Verified: FULLTEXT
- Notes: The 10^42 figure is attributed to Bradbury's "Matrioshka Brains" working manuscript (2002), not to a peer-reviewed source. Bostrom also cites Lloyd's (2000) upper bound of 5x10^50 logical operations per second on ~10^31 bits for a 1 kg computer and Drexler's 10^21 instructions per second for a sugar-cube-sized device, but says the argument uses "the more conservative estimate". (Division check: 10^36 ops / 10^42 ops/s = 10^-6 s, consistent with "less than one millionth ... for one second".)

### C-01-006
- Claim: Bostrom argues that a simulation need only reproduce what simulated observers can notice: distant objects can be compressed, microscopic detail filled in on demand, and errors repaired by editing observers' brain states or re-running the simulation; he locates the main cost in simulating brains.
- Source: Bostrom2003are
- Locator: §III (preprint p. 5)
- Evidence: "it could fill in sufficient detail in the simulation in the appropriate domain on an as-needed basis. Should any error occur, the director could easily edit the states of any brains that have become aware of an anomaly before it spoils the simulation. Alternatively, the director could skip back a few seconds and rerun the simulation"
- Verified: FULLTEXT
- Notes: This "rendering on demand" assumption is what later lets Bostrom discount physics tests (C-01-052). He also notes that "Simulating the entire universe down to the quantum level is obviously infeasible, unless radically new physics is discovered."

### C-01-007
- Claim: Bostrom defines f_P (fraction of human-level technological civilizations that reach a posthuman stage), N-bar (average number of ancestor-simulations run by a posthuman civilization) and H-bar (average number of individuals who lived in a civilization before it became posthuman), and writes the fraction of observers with human-type experiences who live in simulations as f_sim = f_P N-bar H-bar / ((f_P N-bar H-bar) + H-bar); with N-bar = f_I N-bar_I this becomes f_sim = f_P f_I N-bar_I / ((f_P f_I N-bar_I) + 1).
- Source: Bostrom2003are
- Locator: §IV "The core of the simulation argument", unnumbered equation and eq. (*) (preprint pp. 6-7)
- Evidence: "The actual fraction of all observers with human-type experiences that live in simulations is then f_sim = f_P N H / ((f_P N H) + H)" ; "N = f_I N_I and thus: f_sim = f_P f_I N_I / ((f_P f_I N_I) + 1) (*)"
- Verified: FULLTEXT
- Notes: Overbars on N, H and N_I confirmed by rendering preprint p. 7 to an image (text extraction drops them). f_I is "the fraction of posthuman civilizations that are interested in running ancestor-simulations (or that contain at least some individuals who are interested in that and have sufficient resources to run a significant number of such simulations)".

### C-01-008
- Claim: Because N-bar_I is argued to be extremely large, inspection of (*) yields the trilemma f_P ≈ 0, or f_I ≈ 0, or f_sim ≈ 1.
- Source: Bostrom2003are
- Locator: §IV (preprint p. 7)
- Evidence: "Because of the immense computing power of posthuman civilizations, N_I is extremely large, as we saw in the previous section. By inspecting (*) we can then see that at least one of the following three propositions must be true: (1) f_P ≈ 0 (2) f_I ≈ 0 (3) f_sim ≈ 1"
- Verified: FULLTEXT
- Notes: The derivation of the trilemma is a separate step from the credence claim (C-01-009). Birch 2013 (C-01-021) and Bostrom 2005 (C-01-013) both emphasise this separation.

### C-01-009
- Claim: The step from (3) to credence uses a "bland indifference principle", Cr(SIM | f_sim = x) = x, which Bostrom says prescribes indifference only between hypotheses about which observer one is when one has no information about which observer one is; he motivates it with a junk-DNA analogy and a betting argument.
- Source: Bostrom2003are
- Locator: §V "A bland indifference principle", eq. (#) (preprint pp. 7-9)
- Evidence: "Cr(SIM | f_sim = x) = x (#)" ... "the bland indifference principle expressed by (#) prescribes indifference only between hypotheses about which observer you are, when you have no information about which of these observers you are." ... "if everybody were to place a bet on whether they are in a simulation or not, then if people use the bland principle of indifference ... almost everyone will win their bets."
- Verified: FULLTEXT
- Notes: Bostrom says a stronger principle is defended in Bostrom (2001, Synthese) and Anthropic Bias (2002).

### C-01-010
- Claim: Bostrom distinguishes the bland indifference principle from the premise of the Doomsday argument, which he calls "much stronger and more controversial".
- Source: Bostrom2003are
- Locator: §V (preprint p. 9)
- Evidence: "The Doomsday argument rests on a much stronger and more controversial premiss, namely that one should reason as if one were a random sample from the set of all people who will ever have lived (past, present, and future)"
- Verified: FULLTEXT
- Notes: Richmond (2008) comments on this contrast (C-01-027).

### C-01-011
- Claim: Bostrom raises nesting himself: simulated civilizations might run their own simulations, but he notes that the computational cost to basement-level simulators counts against many levels and that, if this cost is prohibitive, "we should expect our simulation to be terminated when we are about to become posthuman".
- Source: Bostrom2003are
- Locator: §VI "Interpretation" (preprint pp. 11-12)
- Evidence: "One consideration that counts against the multi-level hypothesis is that the computational cost for the basement-level simulators would be very great. Simulating even a single posthuman civilization might be prohibitively expensive. If so, then we should expect our simulation to be terminated when we are about to become posthuman."
- Verified: FULLTEXT
- Notes: Harris (2024) cites this passage as published p. 253.

### C-01-012
- Claim: Bostrom concludes that "in the dark forest of our current ignorance" it seems sensible to apportion credence roughly evenly between (1), (2) and (3), and that the truth of (3) would require only slight revisions to most beliefs, since "our best guide" to how the world is set up remains ordinary empirical study.
- Source: Bostrom2003are
- Locator: §VI and §VII (preprint pp. 13-14)
- Evidence: "In the dark forest of our current ignorance, it seems sensible to apportion one's credence roughly evenly between (1), (2), and (3)." ; "Our best guide to how our posthuman creators have chosen to set up our world is the standard empirical study of the universe we see."
- Verified: FULLTEXT
- Notes: Compare Bostrom's later statements (C-01-015, C-01-051), which avoid a number.

## B. Bostrom's later clarifications and the 2011 patch

### C-01-013
- Claim: In reply to Weatherson, Bostrom states that the simulation argument purports to establish only the disjunction (1)∨(2)∨(3), not that we are probably simulated, and that he does not accept (3) on its own.
- Source: Bostrom2005simulation
- Locator: §1 Introduction
- Evidence: "By contrast, I do not accept (3), but only the disjunction (1) ∨ (2) ∨ (3). My view is that we do not currently have strong evidence for or against any of the particular disjuncts. At any rate, the disjunction is all that the simulation argument purports to show; it does not seek to establish that we are probably living in a computer simulation."
- Verified: FULLTEXT
- Notes: Read the journal PDF hosted at simulation-argument.com (sa_weathersonreply.pdf); the embedded font dropped numerals, so the "(3)" etc. were reconstructed from context and the preprint structure.

### C-01-014
- Claim: Bostrom holds that the indifference principle is a constraint on conditional credence, which additional evidence overrides by conditionalization, and that the argument needs only that our current evidence is too weak to shift credence substantially once f_sim ≈ 1 is conditioned on.
- Source: Bostrom2005simulation
- Locator: §2 "Weatherson's four interpretations"
- Evidence: "What the principle actually asserts, however, is that the conditional credence of Φ given f_Φ = x should be x. If one has other relevant information ... then one needs to conditionalize on this extra evidence too" ; "all we need from (P*) is that our current empirical evidence is too weak to result in substantial changes to the posterior credence of (SIM) after we have already conditionalized on f_sim ≈ 1."
- Verified: FULLTEXT
- Notes: Bostrom concedes that (P*) is not strictly true, e.g. if simulators preferentially simulate "pivotal moments in history".

### C-01-015
- Claim: Bostrom writes (2009) that he does not argue that we should believe we are simulated and that he believes we are probably not simulated.
- Source: Bostrom2009simulation
- Locator: first page (author's preprint "The Simulation Argument: Some Explanations", marked "Analysis, in press")
- Evidence: "However, pace Brueckner, I do not argue that we should believe that we are in simulation. In fact, I believe that we are probably not simulated. The simulation argument purports to show only that, as well as (#), at least one of (1) - (3) is true; but it does not tell us which one."
- Verified: FULLTEXT
- Notes: Author's preprint (sa_brueckner.pdf); published version Analysis 69(3):458-461.

### C-01-016
- Claim: Brueckner argued that a simulated being cannot really build a computer and hence that "stacked" simulations cannot multiply conscious sims; Bostrom replied that virtual machines really perform the computations they emulate, so that under substrate-independence nested simulations raise no special difficulty.
- Source: Bostrom2009simulation (quoting Brueckner2008simulation)
- Locator: pp. 2-3 of preprint
- Evidence: (Brueckner, as quoted by Bostrom) "Just as a brain in a vat is incapable of really building another brain in a vat, a Sim is incapable of really building another computer which instantiates another human-like conscious Sim mind." ; (Bostrom) "each computation that any of these virtual machines implements is really being implemented"
- Verified: FULLTEXT
- Notes: Brueckner (2008) itself is paywalled; we saw only its opening paragraph via OpenAlex (ABSTRACT level), which confirms Brueckner's reading that "we should believe that we are not humans but rather conscious computer simulations of humans". Bostrom also says Brueckner misquoted "will run" for "may run". Characterize Brueckner's argument only via this quote, and say so.

### C-01-017
- Claim: Bostrom and Kulczycki identify a "mathematical non sequitur" in the original f_sim formula: if civilizations that go on to run ancestor simulations have much smaller pre-posthuman populations than those that do not, all three disjuncts can fail at once.
- Source: Bostrom2011patch
- Locator: sections "The bug" and "The vulnerability" (author's preprint pp. 1-2)
- Evidence: "What has so far passed unnoticed is a mathematical non sequitur in the original paper." ; "if those civilizations that eventually reach a posthuman phase have unusually brief pre-posthuman phases compared to other civilizations ... it could happen that most pre-posthuman observers live outside simulations even if most pre-posthuman civilizations eventually become posthuman"
- Verified: FULLTEXT
- Notes: Author's preprint (sa_patch.pdf) headed "Published in: Analysis, Vol. 71, No. 1 (2011): 54-61". Numerical values in the counter-example were lost in text extraction; do not quote them. Birch 2013's reference list gives the pages as 64-71, which disagrees with Crossref (54-61); we use Crossref.

### C-01-018
- Claim: Two independent patches restore the disjunction: (i) assume that the cumulative pre-posthuman population does not differ by an astronomically large factor (e.g. more than a million) between simulating and non-simulating civilizations; or (ii) use indexical evidence about our position in history (e.g. "computer age birth rank") to restrict the relevant observers.
- Source: Bostrom2011patch
- Locator: "The first patch", "The second patch", Appendix (preprint pp. 3-6)
- Evidence: "we need only introduce a very weak assumption to the effect that the typical duration (or more precisely, the typical cumulative population) of the pre-posthuman phase does not differ by an astronomically large factor ... by assuming that the difference is no greater than a factor of one million we can derive the key tripartite disjunction." ; "Define a person's computer age birth rank as follows"
- Verified: FULLTEXT
- Notes: The paper assumes a finite universe throughout ("in order to avoid complications that arise when assigning probabilities and using indifference principles, such as the Self-Sampling Assumption, over infinite outcome spaces", endnote v).

## C. Objections to the indifference step and to the evidential base

### C-01-019
- Claim: Weatherson distinguishes four interpretations of the general principle behind Bostrom's indifference step and argues that on two it is false, on the third it does not entail Bostrom's principle, and on the fourth it does so only given an auxiliary hypothesis (that all of one's evidence is probabilistically independent of being a Sim) that we have no reason to believe.
- Source: Weatherson2003are
- Locator: Abstract; sections "First" to "Fourth Interpretation"
- Evidence: "I set out four possible interpretations of the principle, none of which can be used to support Bostrom's argument. On the first two interpretations the principle is false, on the third it does not entail the conclusion, and on the fourth it only entails the conclusion given an auxiliary hypothesis that we have no reason to believe."
- Verified: FULLTEXT
- Notes: Read the preprint hosted at simulation-argument.com (sa_weatherson.pdf). Weatherson's auxiliary premise is "P2. All of Rat's evidence is probabilistically independent of the property of being a Sim."

### C-01-020
- Claim: Weatherson's grounds for rejecting that auxiliary premise include epistemic externalism (a human's perceptual evidence may differ from a Sim's even if their experiences match) and a Goodman-style "grue" challenge built from the gerrymandered predicate "suman".
- Source: Weatherson2003are
- Locator: "Second Interpretation" (definition of suman) and "Fourth Interpretation"
- Evidence: "Just as seeing a dagger and hallucinating a dagger provide different evidence, so does seeing a dagger and sim-seeing a sim-dagger." ; "x is a suman =df x is a human C or a Sim who is not a C"
- Verified: FULLTEXT
- Notes: Weatherson's conclusion is permissive: "If Rat is very confident that she is human, even while knowing that most human-like beings are Sims, she has not violated any norms of reasoning". Bostrom's reply to both objections: C-01-014 and his §§3, 5 (externalism; "suman").

### C-01-021
- Claim: Birch argues that the argument needs "selective scepticism": its case for the trilemma requires good scientific evidence about the physical limits of computation, while the indifference step requires that our evidence not support mundane self-locating claims such as having real hands; with a "parity of evidence" premise the three claims are jointly inconsistent.
- Source: Birch2013on
- Locator: §1 (Good Evidence, Impoverished Evidence, Parity of Evidence)
- Evidence: "Good Evidence, Impoverished Evidence and Parity of Evidence are jointly incompatible. Bostrom must reject one."
- Verified: FULLTEXT
- Notes: Read the Springer version of record (sa_birch-on-the-simulation-argument-and-selective-skepticism.pdf, DOI header present).

### C-01-022
- Claim: Birch makes explicit the credence constraint the argument yields, Cr(SIM) ≥ Cr(SIM|H3)·(1 − Cr(H1 ∨ H2)), so that unless one is nearly certain of H1 ∨ H2 one must give SIM significant credence.
- Source: Birch2013on
- Locator: §1, inequalities (ii)-(iv)
- Evidence: "(iv) Cr(SIM) ≥ Cr(SIM|H3) · (1 − Cr(H1 ∨ H2))" ; "if I assign credence 0.7 to H1 ∨ H2, I ought to assign credence greater than or approximately equal to 0.3 to SIM."
- Verified: FULLTEXT
- Notes: Operator symbols were garbled in extraction ("≥" rendered as a blank); the inequality direction is fixed by Birch's accompanying prose.

### C-01-023
- Claim: Birch argues that retreating to a weaker quadripartite disjunction (SIM ∨ H1 ∨ H2 ∨ H3) does not deliver the credence constraint, that a simulated observer could reliably infer only that at least one ancestor-simulation is possible, and that Elga-style self-locating scepticism would rescue the argument only in circumstances we are not in; he concludes there is no good reason to believe the argument's conclusion.
- Source: Birch2013on
- Locator: §§3, 4.2, 4.3, 5
- Evidence: "a simulated observer could infer with confidence only one claim about the limits of computation: namely, that these limits are such that at least one posthuman civilization could run at least one ancestor-simulation." ; "There is, at present, no good reason to endorse the curious combination of scientific realism and self-locating scepticism that Bostrom's argument requires. There is thus no good reason to believe its conclusion."
- Verified: FULLTEXT
- Notes: Bostrom's FAQ (2025) answers a version of this objection with a two-case argument (if simulated, the underlying reality permits simulations; if not, the evidence is veridical), C-01-051.

### C-01-024
- Claim: Crawford develops two objections: a structurally parallel argument that one is a "freak observer" formed in a fluctuation, and the claim that evidence that simulants or freak observers exist is not a reason to think one is one of them.
- Source: Crawford2013freak
- Locator: Abstract
- Evidence: "The first takes the form of a structurally similar argument for a conflicting conclusion, the claim that I am a so-called freak observer ... The evidence that simulants or freak observers exist is not a reason to think that I am one of them."
- Verified: ABSTRACT
- Notes: Paywalled (Wiley). Abstract from Crossref. Restrict to the abstract.

### C-01-025
- Claim: Thomas argues that Bostrom's reasoning supports only a conditional claim (high odds of being simulated given a high simulant-to-non-simulant ratio), and that confidence in a high ratio is hard to reconcile with being simulated; he replaces it with a premise that, conditional on being non-simulated, the expected ratio in one's reference class is high, and proves that under an indifference principle and an admissibility condition the odds of being simulated are at least that expected ratio.
- Source: Thomas2026simulation
- Locator: §1 (conditional sim, high ratio, high expectation); §4 "Main Result, Version 2"
- Evidence: "However, the Simulation Argument is not an argument for sim." ; "high expectation. Conditional on my being a non-simulant person, the expected ratio of simulant to non-simulant people in my reference class is high." ; "Assume that indifference is true. If R is admissible* with respect to E, F, and G, then Odds(ιF/ιG | ιE) ≥ E(Rat_R^{F/G} | ιE & ιG)."
- Verified: FULLTEXT
- Notes: FULLTEXT is the GPI Working Paper 16-2021 version (thomas_simexp.pdf). The Erkenntnis version of record could not be downloaded (Springer blocked); its Crossref abstract matches the working paper's thesis. Thomas presents this partly as a response to Birch (2013) and Crawford (2013) (his fn. 2).

### C-01-026
- Claim: Thomas argues that finding (or running) many simulations would not necessarily raise the odds that one is simulated, because such evidence may break the admissibility of one's reference class or, on an externalist reading, confirm that one is non-simulated.
- Source: Thomas2026simulation
- Locator: §6.2 "The limits of future evidence"; published abstract
- Evidence: (published abstract) "I refute the common line of thought that finding many simulations being run—or running them ourselves—must increase the odds that we are in a simulation." ; (working paper) "Bostrom (2006, p. 9) and Greene (2020) both claim that this should make me confident that I am a simulant person."
- Verified: FULLTEXT
- Notes: Contrast Bostrom 2003 §VI ("If we do go on to create our own ancestor-simulations, this would be strong evidence against (1) and (2)") and Kipping 2020 (C-01-041). This is a live disagreement.

## D. Doomsday, reference classes and self-locating belief

### C-01-027
- Claim: Richmond (2008) argues that our own lack of simulating capacity is evidence about our place in any simulation hierarchy: on Bostrom's picture ours would be an unusual successor-less level, and if simulation costs rise with the number of levels, a likelihood argument favours hypotheses with fewer levels, without needing priors or indifference principles.
- Source: Richmond2008doomsday
- Locator: §V "The Simulation Argument" (accepted-manuscript pp. 11-13)
- Evidence: "If we take Bostrom's simulation-hierarchy seriously, we have to conclude that ours is the one and only level in the hierarchy that lacks descendents." ; "Because this argument issues in a likelihood-ratio, it requires neither priors, exact numerical likelihoods nor indifference principles."
- Verified: FULLTEXT
- Notes: Read the Edinburgh Research Archive copy (richmond2008.pdf), apparently the accepted manuscript; version of record Ratio 21(2):201-217.

### C-01-028
- Claim: Richmond (2017) offers a "Doomsday lottery" argument against Bostrom's conclusion and argues that anti-simulation conclusions can be drawn with more robust reference classes and without indifference principles.
- Source: Richmond2017why
- Locator: Abstract
- Evidence: "This paper initially offers a posterior-probabilistic 'Doomsday lottery' argument against Bostrom's conclusions. ... Anti-simulation arguments herein use more (epistemically and metaphysically) robust reference classes than Bostrom's argument, require no Principles of Indifference"
- Verified: ABSTRACT
- Notes: Wiley reports it as OA, but the PDF download was blocked from our environment. Restrict to abstract.

### C-01-029
- Claim: Lewis (2013) argues that, despite structural similarities, the simulation argument succeeds where the Doomsday argument fails, because of a "relative location effect" and because, in versions with several simulations per world, self-location uncertainty is not resolved by the evidence that our world contains no simulations.
- Source: Lewis2013doomsday
- Locator: Abstract; §§3-4
- Evidence: "I argue that these disanalogies mean that the Simulation Argument succeeds and the Doomsday Argument fails." ; "the power of the Simulation Argument is that it involves self-location uncertainty that is not resolved by the evidence at hand."
- Verified: FULLTEXT
- Notes: Read the PhilSci-Archive preprint (docx). Lewis's results depend on a "location-uniform" (LU) prior, which he identifies with the thirder answer to Sleeping Beauty; under the alternative "hypothesis-uniform" (HU) prior the effect holds only for small n. One sentence in the preprint (end of §3 case n=3) appears to contain a typo ("less likely" where the surrounding numbers imply "more likely"); do not quote it. Illustrative numbers: with n = 10^6 possible simulations and 99% prior that there are none, LU gives a final credence of 99.98% that one is simulated (§4). Treat that as Lewis's illustration, not a result.

### C-01-030
- Claim: Bostrom's Self-Sampling Assumption (SSA) states that one should reason as if one were a random sample from the set of all observers in one's reference class; he later strengthens it to observer-moments (SSSA).
- Source: Bostrom2002anthropic
- Locator: ch. 4, p. 57 (SSA); ch. 10 (SSSA)
- Evidence: "(SSA) One should reason as if one were a random sample from the set of all observers in one's reference class." ; "(SSSA) One should reason as if one's present observer-moment were a random sample from the set of all observer-moments in its reference class."
- Verified: FULLTEXT
- Notes: Read the author-hosted PDF of the 2002 Routledge edition (anthropic-principle.com). The book does not discuss the simulation argument; one passing mention of beings "running as simulations".

### C-01-031
- Claim: Bostrom states the Self-Indication Assumption (SIA), that one's existence favours hypotheses with many observers, and rejects it, chiefly by the "Presumptuous Philosopher" thought experiment.
- Source: Bostrom2002anthropic
- Locator: ch. 4, p. 66 (SIA); ch. 7, pp. 124-125 (Presumptuous Philosopher)
- Evidence: "(SIA) Given the fact that you exist, you should (other things equal) favor hypotheses according to which many observers exist over hypotheses on which few observers exist." ; "SIA may seem prima facie implausible, and we shall argue in chapter 7 that it is no less implausible ultimo facie."
- Verified: FULLTEXT
- Notes: Bostrom notes that "adopting SIA annihilates the Doomsday argument". Lewis (2013, §2) argues that the presumptuous-philosopher case does not tell against his LU prior because it involves no self-location uncertainty.

### C-01-032
- Claim: Bostrom's discussion of the reference-class problem shows that which entities count as in the reference class can change the rational credence when population size depends on the hypothesis.
- Source: Bostrom2002anthropic
- Locator: ch. 4, "The reference class problem", pp. 69-71 (Incubator, version II)
- Evidence: "The reference class problem can be relevant in cases like this, where the size of the population depends on which hypothesis is true. What you should believe depends on whether the object x that would be in Room 2 would be in the reference class or not."
- Verified: FULLTEXT
- Notes: The simulation argument's reference class is "observers with human-type experiences" (Bostrom 2003). Carroll (C-01-036) and Richmond (C-01-028) target this choice.

### C-01-033
- Claim: Elga (2000) defends the "thirder" answer to the Sleeping Beauty problem, a case in which uncertainty about the world interacts with uncertainty about one's own temporal location.
- Source: Elga2000self
- Locator: §1-2
- Evidence: "I will argue that the correct answer is 1/3."
- Verified: FULLTEXT
- Notes: Read the author-hosted PDF with the Analysis citation line. Relevant because Lewis (2013) identifies his LU prior with this answer.

### C-01-034
- Claim: Elga (2004) defends an indifference principle for self-locating belief, that similar centered worlds deserve equal credence, and argues that it separates ordinary sceptical hypotheses (which one may give low credence by default) from self-locating ones (which arise only if one's subjective state is instantiated more than once, and which get no such default bias).
- Source: Elga2004defeating
- Locator: §§6-7
- Evidence: "INDIFFERENCE Similar centered worlds deserve equal credence." ; "There is a default bias against the first sort of skeptical hypothesis. ... In contrast, INDIFFERENCE entails that there is no corresponding bias against the second sort of hypothesis."
- Verified: FULLTEXT
- Notes: Read the author's penultimate draft. Elga explicitly rejects the stronger claim that centred worlds representing indistinguishable predicaments deserve equal credence (so a lone brain-in-a-vat hypothesis gets no boost). Birch (2013, §4.3) uses this to delimit when Bostrom's selective scepticism could be defensible.

### C-01-035
- Claim: Bostrom's own FAQ notes that in an infinite universe the ratio of simulated to all people is undefined and proposes a limit-density measure instead.
- Source: Bostrom2025simulation
- Locator: FAQ Q7 "What happens to the argument if the world is infinite?"
- Evidence: "In this case, the ratio of simulated people to the total number of people is not defined. To deal with these infinite cases, we need to do something like thinking in terms of densities rather than total populations."
- Verified: FULLTEXT
- Notes: Non-peer-reviewed. Thomas (working paper fn. 9) also assumes a finite number of observers and cites Arntzenius & Dorr (2017) on problems in infinite populations. Bostrom & Kulczycki (2011) assume finiteness (C-01-018).

## E. Nesting and resource decay

### C-01-036
- Claim: Carroll (2016) argues that, since each level of simulation has less computing power than the level above, the hierarchy bottoms out in simulations unable to run realistic simulations; with the typicality premise, most observers would then be in such lowest-level simulations, contradicting the premise that simulating civilizations is feasible. He calls the typicality premise "more or less completely without justification".
- Source: Carroll2016maybe
- Locator: blog post, full text (22 August 2016)
- Evidence: "We probably live in the lowest-level simulation, the one without an ability to perform effective simulations. That's where the vast majority of observers are to be found." ; "premise 5. (we should assume we are typical observers) is more or less completely without justification."
- Verified: FULLTEXT
- Notes: A blog post, cited because the argument itself is the object of study. Carroll attributes the resource-decay observation to an audience member at an FQXi event. Carroll's reconstruction of the argument (seven premises) is his own and differs from Bostrom's.

### C-01-037
- Claim: Kipping's hierarchical model agrees that, for pλ ≫ 1, most realities lie in the lowest level, and replies to Carroll that the lowest level might still build detailed but non-sentient simulations, so that its inhabitants could still arrive at Bostrom's trilemma.
- Source: Kipping2020bayesian
- Locator: §2.2 eq. (4); §2.3
- Evidence: "Thus, for all pλ ≫ 1, most realities reside in the lowest level of the hierarchy." ; "We suggest here that this contradiction can be somewhat dissolved by considering that the lowest level may indeed not be capable of generating their own reality simulations, but are plausibly capable of still making very detailed simulations that fall short of generating sentience."
- Verified: FULLTEXT
- Notes: arXiv:2008.12254v1. Published version not readable from our environment (MDPI blocked); Crossref abstract matches v1 abstract.

### C-01-038
- Claim: Bostrom's FAQ answers the exponential-cost objection by suggesting simulators could cap or end simulated civilizations that consume excessive computing, with the consequence that most civilizations would be "leaf nodes" that never run genuine simulations of their own.
- Source: Bostrom2025simulation
- Locator: FAQ Q6
- Evidence: "simulators could avoid this by stepping in to prevent simulated civilizations from using excessive amounts of computing power, or by ending them shortly after they begin to consume excessive resources ... most civilizations would be leaf nodes of the simulation tree: they are themselves simulated but they will never run genuine simulations of their own."
- Verified: FULLTEXT
- Notes: Non-peer-reviewed; compare Richmond 2008 (C-01-027), which treats our being a "leaf" as evidence against deep hierarchies.

### C-01-039
- Claim: Bibeau-Delisle and Brassard derive a Drake-style equation for the probability that our universe is a deliberate simulation, and argue that in a recursive scenario (simulated civilizations also simulate) the fraction of simulated beings is bounded above by the simulation efficiency factor, which they argue is most likely below 50%.
- Source: BibeauDelisle2021probability
- Locator: Abstract; §2, eqs. (15)-(16) (arXiv v1)
- Evidence: "it follows from equation (15) that f_Sim also is upper-bounded by f_Eff, which is most likely under 50%." ; "The recursive scenario thus gives us a reasonable situation in which there are more real than simulated consciousnesses despite the gigantic value of R_Cal."
- Verified: FULLTEXT
- Notes: Read arXiv:2008.09275v1; the version of record (Proc. R. Soc. A 477:20200658) abstract matches, but we did not check whether the equation numbering changed. The model assumes physics is efficiently simulable on quantum but not classical computers.

## F. Quantitative (Bayesian) treatments

### C-01-040
- Claim: Kipping merges Bostrom's disjuncts (1) and (2) into a "physical hypothesis" H_P and compares it with the simulation hypothesis H_S modelled as a hierarchy in which a base civilization runs λ simulations, each "parous" with probability p, to a maximum depth G, giving N_sim = Σ_{g=2}^{G} p^{g−2} λ^{g−1} simulated realities.
- Source: Kipping2020bayesian
- Locator: §1; §2.1-2.2, eq. (1)
- Evidence: "It is useful to combine these two propositions into a single hypothesis since their outcome is the same ... let us dub this the "physical hypothesis", H_P." ; "N_sim = Σ_{g=2}^{G} p^{g−2} λ^{g−1}"
- Verified: FULLTEXT
- Notes: Kipping states the model is deterministic (each parous simulation spawns exactly λ) and treats λ and p as constant across levels, arguing a variable model would add unwarranted complexity.

### C-01-041
- Claim: With equal prior odds on H_S and H_P and conditioning only on one's existence, Kipping obtains Pr(base reality) = 1/2 + 1/(2(N_sim+1)), so the probability of being simulated is below 50% and tends to 50% as N_sim → ∞; conditioning instead on our not (yet) having produced simulations gives a Bayes factor (λ−1)/λ, slightly favouring H_P; if humanity began producing such simulations, the probability of base reality would fall to λ/N_sim.
- Source: Kipping2020bayesian
- Locator: §2.5 eq. (12); §2.7 eqs. (21)-(22); §2.8 eq. (27); §2.9 eq. (32)
- Evidence: "Pr(g = 1|CES) = 1/2 + 1/(2(N_sim + 1))." ; "Pr(nulliparous|H_S)/Pr(nulliparous|H_P) = (λ − 1)/λ." ; "the probability that we live in a simulated reality radically shifts from just below one-half to just approaching zero."
- Verified: FULLTEXT
- Notes: (a) The 50% ceiling follows from the assumption Pr(H_S) = Pr(H_P); Kipping himself says this choice "could be challenged as being too generous to model H_S, on the basis that it is an intrinsically far more complex model" (§3). (b) The §2.9 sentence as printed in v1 says probability "that we live in a simulated reality" shifts "to just approaching zero", but eq. (32) is the probability of base reality; the intended meaning is that the probability of base reality approaches zero. Likewise, §3 says the probability "we live in base reality ... is still not the favored outcome, with a probability less than 50%", which contradicts eq. (22) and the abstract. The abstract and equations are consistent with each other; cite them, not the prose. (c) Kipping claims the result is robust to counting individuals rather than realities, assuming sims are evenly distributed across realities (§3).

### C-01-042
- Claim: Richmond, Lewis and Kipping all derive different verdicts from the same observation that our civilization has not (yet) produced simulated minds: Richmond takes it to favour fewer simulation levels, Lewis shows it can raise the credence that one is simulated in some models, and Kipping uses it to obtain a Bayes factor near 1.
- Source: Richmond2008doomsday; Lewis2013doomsday; Kipping2020bayesian
- Locator: Richmond §V; Lewis §3; Kipping §2.3, §2.5
- Evidence: (Richmond) "ours is the one and only level in the hierarchy that lacks descendents"; (Lewis) "conditionalizing on the fact that the world contains no simulations makes it more likely that you live in a simulation"; (Kipping) "In our case, the "data" we leverage is that we are nulliparous when it comes to simulating realities."
- Verified: FULLTEXT
- Notes: This is our synthesis of three FULLTEXT-verified positions, not a claim any single author makes. Phrase it as such in the draft.

## G. Consciousness, substrate and scepticism

### C-01-043
- Claim: Beisbart argues that the simulation argument relies on an assumption that the hardware running a brain simulation bears a close analogy to the brain, and that this fails because the way computer components interact during a simulation does not resemble the way neurons interact.
- Source: Beisbart2014are
- Locator: Abstract
- Evidence: "this does not suffice to underwrite the simulation argument because the ways in which parts of the computer hardware interact during simulations do not resemble the ways in which neurons interact in the brain."
- Verified: ABSTRACT
- Notes: Abstract from OpenAlex; OUP PDF blocked.

### C-01-044
- Claim: Summers and Arvan argue that if panpsychism or panqualityism is true, the only way to live in a simulation might be as brains-in-vats (making it unlikely that we live in a simulation), and viable simulation hypotheses become substantially sceptical scenarios, against Chalmers.
- Source: Summers2022two
- Locator: Abstract
- Evidence: "we argue that if either panpsychism or panqualityism is true, then the only way to live in a simulation might be as brains-in-vats, in which case it is unlikely that we live in a simulation. We then argue that, if panpsychism or panqualityism is true, viable simulation hypotheses are substantially sceptical scenarios."
- Verified: ABSTRACT
- Notes: Abstract from OpenAlex (T&F and PhilArchive blocked).

### C-01-045
- Claim: Chalmers (2005) argues that the "Matrix Hypothesis" is not a sceptical but a metaphysical hypothesis, equivalent to the conjunction of a Creation Hypothesis, a Computational Hypothesis (microphysical processes are computational) and a Mind-Body Hypothesis, so that if one is in a matrix most ordinary beliefs remain true.
- Source: Chalmers2005matrix
- Locator: §§2-3 (consc.net version)
- Evidence: "I will argue that the hypothesis that I am envatted is not a skeptical hypothesis, but a metaphysical hypothesis. That is, it is a hypothesis about the underlying nature of reality." ; "I think that even if I am in a matrix, I am still in Tucson; I am still sitting at my desk"
- Verified: FULLTEXT
- Notes: Read the consc.net version, which states it also appears in Grau (ed.), Philosophers Explore the Matrix (OUP 2005). Bostrom (2005, fn. 3) cites this as making "a similar point".

### C-01-046
- Claim: Chalmers (2005) allows that local, recent or partial simulation scenarios are "partial skeptical hypotheses" that undercut some empirical beliefs while leaving many intact.
- Source: Chalmers2005matrix
- Locator: §8 "Other skeptical hypotheses"
- Evidence: "one can argue that most of these are not global skeptical hypotheses: that is, their truth would not undercut all of our empirical beliefs about the physical world. At worst, most of them are partial skeptical hypotheses"
- Verified: FULLTEXT
- Notes: The later debate (C-01-049, C-01-050) turns on how probable such small or deceptive simulations are.

### C-01-047
- Claim: In Reality+ Chalmers reformulates the argument as "If there are no sim blockers, we are probably sims", where sim blockers include Bostrom's two disjuncts and further ones (intelligent sims impossible, conscious sims impossible, simulators avoid creating conscious sims, sims require too much computer power); he argues we cannot know that any sim blocker obtains and so cannot know we are not in a simulation.
- Source: Chalmers2024precis
- Locator: Précis, paragraph on Chapter 5
- Evidence: "1. If there are no sim blockers, most humanlike beings are sims. 2. If most humanlike beings are sims, we are probably sims. 3. So: If there are no sim blockers, we are probably sims." ; "I argue that we can't know that any of these sim blockers obtain. I go on to argue that we should assign a non-negligible probability to the simulation hypothesis"
- Verified: FULLTEXT
- Notes: Read the consc.net précis (fn.: "A version of this précis appears in Uriah Kriegel (ed.), Oxford Studies in Philosophy of Mind (2024)"). The book itself (Chalmers2022reality) was not read; cite the précis for content and the book for the source of the argument. Harris (2024) reports that Chalmers (2022, ch. 5) suggests a "roughly 25%" probability; we have not verified this number in the book, so do not state it.

### C-01-048
- Claim: Chalmers' central anti-sceptical thesis is that "virtual reality is genuine reality": objects in a simulation are real, and a structuralist reading of physics implies that if our physical theories are true in an unsimulated universe they are true in a simulated one with the same structure.
- Source: Chalmers2024precis
- Locator: Précis, opening and Chapter 22 paragraph
- Evidence: "The central thesis of Reality+ is virtual reality is genuine reality." ; "1. Our physical theories are structural theories 2. If we're in Nonsim Universe, our physical theories are true. 3. Sim Universe has the same structure as NonSim Universe. 4. So: If we're in Sim Universe, our physical theories are true."
- Verified: FULLTEXT
- Notes: Relevant to the physics bridge: on this view detecting simulation would reveal the realizer of physical structure rather than falsify physics.

### C-01-049
- Claim: Replying to critics, Chalmers illustrates how seriously the hypothesis should be taken: giving even 10% credence each to the falsity of the sim blockers "conscious humanlike sims are impossible" and "nonsims will not create many", and assuming independence, leaves 1% credence that most humanlike beings are sims; he distinguishes global scepticism (which he rejects) from local scepticism about small or deceptive simulations (which he leaves open).
- Source: Chalmers2024taking
- Locator: §1 item 4; §2
- Evidence: "If we give these denials even 10% credence each, then (assuming independence) this still leaves us with a 1% credence that most humanlike beings are sims." ; "in Reality+, I am mainly concerned to argue against global skepticism ... Various more local forms of skepticism ... are left on the table."
- Verified: FULLTEXT
- Notes: Read the author's early-view PDF (DOI 10.1111/phpr.13122). The 1% is an illustrative lower figure, not Chalmers' own estimate. Chalmers reports that Godfrey-Smith (2024) favours a biological basis for "felt experience" and draws a parallel with Boltzmann brains; we have not read Godfrey-Smith's paper and attribute these points only as Chalmers' summary.

### C-01-050
- Claim: Schwitzgebel argues that if we live in a simulation we should attach significant conditional credence to its being small or brief, making our existence depend on contingencies beyond our control.
- Source: Schwitzgebel2024lets
- Locator: Abstract
- Evidence: "I argue on the contrary that if we live in a simulation, we ought to attach a significant conditional credence to its being a small or brief simulation."
- Verified: ABSTRACT
- Notes: Wiley PDF blocked; abstract from Crossref. Chalmers (2024, §3) replies that small simulations are hard to sustain given memories and communications.

### C-01-051
- Claim: Bostrom's FAQ says he assigns a "substantial probability" to the simulation hypothesis but declines to give a number, and answers the objection that being simulated would undermine the argument's empirical premises with a two-case argument: if we are simulated, the underlying reality permits simulations; if not, the evidence is veridical and the original reasoning applies.
- Source: Bostrom2025simulation
- Locator: FAQ Q2 and Q4
- Evidence: "I would assign a "substantial probability" to the simulation hypothesis. I tend to refrain from providing a specific number." ; "A. If we are in a simulation, then the underlying reality is such as to permit simulations, it contains at least one such simulation, and (3) is true. B. If we are not in a simulation, then the empirical evidence noted in the simulation argument is veridical taken at face value"
- Verified: FULLTEXT
- Notes: Non-peer-reviewed. Bostrom's stated credence has varied: "roughly evenly" (2003), "probably not simulated" (2009), "substantial probability" (FAQ 2025). Harris (2024) cites Bostrom (2005b) for "on the order of 20%"; not verified by us.

## H. The bridge to empirical work

### C-01-052
- Claim: Bostrom (FAQ) holds that the simulation hypothesis is testable only in a weak, probabilistic sense (evidence bearing on disjuncts (1) and (2) indirectly bears on (3)), and that proposed physics tests such as the lattice-artefact search of Beane et al. (2014) are unlikely to be informative because simulators need not use uniform lattices and could fake results.
- Source: Bostrom2025simulation
- Locator: FAQ Q11 and Q12
- Evidence: "So the simulation hypothesis is clearly empirically testable in the sense that there are possible observations we might make that would either increase or decrease the probability that it is true." ; "there is little reason to suppose that the hypothetical superintelligent simulators would use the crude simulation technique that such a test would detect."
- Verified: FULLTEXT
- Notes: Bostrom also writes that if a clear experimental test existed, "we should probably not do it" (citing Greene 2020). Cross-link to the lattice / cosmic-ray section.

### C-01-053
- Claim: Greene argues that both ancestor-simulation technology and experimental probes for simulation carry a termination risk, and that experiments cannot establish that we are not simulated: a null result is only weak evidence, while a positive result would establish simulation and could destroy the simulation's value to its operators.
- Source: Greene2020termination
- Locator: Abstract; §1; §4 (journal pp. 504-505)
- Evidence: "no matter how sophisticated our experiments become, they could never allow us to conclude that we do not live in a simulation, since if we live in a simulation, then all our observations are part of the simulation programming." ; "Demonstrating that we do not live in a simulation does not seem to be an attainable goal of experimental observation."
- Verified: FULLTEXT
- Notes: Read the Springer version of record hosted at simulation-argument.com. Greene's expected-value conclusions depend on assumed utilities; state them as his argument, not as established.

### C-01-054
- Claim: Harris argues, building on Greene, that beings who cannot rule out being simulated have self-preservation reasons not to run conscious simulations (a nested "back-breaking simulation" could terminate their level), which supports Bostrom's disjunct (2) and so undercuts assigning high probability to (3).
- Source: Harris2024simulation
- Locator: §§4, 6 (accepted manuscript)
- Evidence: "The thrust of this argument is that any beings that are both concerned for their own survival and unsure whether they are sims have good reason not to run complex simulations. It does not follow that we are not sims, only that the assignment of a relatively high probability to our being sims is premature."
- Verified: FULLTEXT
- Notes: Read the author's accepted manuscript (sa_harris-the-simulation-argument-reconsidered.pdf), which gives doi:10.1093/analys/anad048 as the version of record.

### C-01-055
- Claim: Barrow argues that if we live in a simulated reality we might expect occasional glitches, slow drifts in the constants of nature, and error-correction events, because simulators with imperfect knowledge would need to patch their simulations.
- Source: Barrow2007living
- Locator: Abstract and concluding paragraph
- Evidence: "We explain why, if we live in a simulated reality, we might expect to see occasional glitches and small drifts in the supposed constants and laws of Nature over time."
- Verified: FULLTEXT
- Notes: Read the author's preprint hosted at simulation-argument.com. These are qualitative expectations, not predictions with magnitudes. Bostrom's FAQ Q5 is sceptical of "glitch" reports. Cross-link to the physics sections on varying constants.

## I. Ethics and theology (brief)

### C-01-056
- Claim: Dainton argues that the possibility of non-divine world-makers greatly diminishes the problem of natural evil (the "simulation solution"); Crummett argues that Dainton does not show this solution is better than Fall or diabolical theodicies and offers reasons to prefer it; Johnson argues that theists who claim to know God exists are committed to our universe most likely being a simulation; Steinhart derives theological analogues (cosmological and design arguments, resurrection, theodicy) from the argument.
- Source: Dainton2020natural; Crummett2021real; Johnson2011natural; Steinhart2010theological
- Locator: Abstracts (Dainton also opening pages of the accepted manuscript)
- Evidence: (Dainton) "Given the very real possibility of world-makers who are non-divine, the problem posed by natural evil is very much diminished." ; (Crummett) "Unfortunately, Dainton fails to give compelling reasons for preferring the simulation solution to Fall or diabolical theodicies." ; (Johnson) "our universe was not designed by God and is instead, most likely, a computer simulation." ; (Steinhart) "We show how the SA can be used to develop novel versions of the Cosmological and Design Arguments."
- Verified: ABSTRACT
- Notes: Dainton's accepted manuscript was available (FULLTEXT of opening) but only abstract-level claims are made. Bostrom (2003, §VI) already drew "loose analogies with religious conceptions" and a "naturalistic theogony".

### C-01-057
- Claim: Bostrom (2003) considered the ethical convergence route to disjunct (2) (advanced civilizations might ban ancestor simulations because of the suffering they cause) but noted it would also require convergence on a civilization-wide means of enforcing such a ban.
- Source: Bostrom2003are
- Locator: §VI (preprint p. 11)
- Evidence: "convergence on an ethical view of the immorality of running ancestor-simulations is not enough: it must be combined with convergence on a civilization-wide social structure that enables activities considered immoral to be effectively banned."
- Verified: FULLTEXT
- Notes: Harris (2024) argues for (2) from prudence rather than ethics (C-01-054).

---

## Items found but NOT used in the draft (metadata only or unverified)

- Eckhardt, W. (2012/2013) "The Simulation Argument", ch. 4 of *Paradoxes in Probability Theory* (SpringerBriefs), pp. 15-17, doi:10.1007/978-94-007-5140-8_4. METADATA only; no legitimate full text or abstract reachable. (Eckhardt 1993, Mind 102:483-488, is on Doomsday, not simulation.)
- Dainton, B. (2012) "On Singularities and Simulations", *J. Consciousness Studies* 19(1-2). Existence from PhilPapers listing via web search; no DOI; Ingenta blocked. UNVERIFIED content. Dainton's 2002 manuscript "Innocence Lost" (hosted at simulation-argument.com) argues the argument can be broadened beyond substrate-independence, but it is unpublished.
- Jenkins, P. S. (2006) "Historical Simulations: Motivational, Ethical and Legal Issues", *J. Futures Studies* 11(1):23-42. Existence confirmed via SSRN listing and citations in Bostrom & Kulczycki and Birch; abstract not read. METADATA.
- Mitchell, J. B. O. (2020) "We are probably not Sims", *Science and Christian Belief* 32:45-62. Existence confirmed (St Andrews repository handle 10023/19794); PDF blocked by a captcha. METADATA.
- Agatonović, M. (2023) "The fiction of simulation: a critique of Bostrom's simulation argument", *AI & Society* 38(4):1579-1586, doi:10.1007/s00146-021-01312-y. METADATA.
- White, J. (2016) "Simulation, self-extinction, and philosophy in the service of human civilization", *AI & Society* 31(2):171-190, doi:10.1007/s00146-015-0620-9. METADATA.
- Schwitzgebel, E. (2017) "1% Skepticism", *Noûs* 51(2):271-290, doi:10.1111/nous.12129. METADATA (in bib for completeness only).
- Hanson, R. (2001) "How to Live in a Simulation", *J. Evolution and Technology* 7. Author page returned 403; claims known only via Barrow's quotation. UNVERIFIED.
- Godfrey-Smith (2024) PPR: METADATA; content only via Chalmers' summary.

### C-01-058
- Claim: Godfrey-Smith (2024) is the work Chalmers replies to on the biological basis of experience; cited for attribution only, content taken from Chalmers2024taking.
- Source: GodfreySmith2024simulation
- Locator: Phil. Phenomenol. Res. 109(3), 1036-1041
- Evidence: Crossref record for doi:10.1111/phpr.13124: title "Simulation scenarios and philosophy", author Godfrey-Smith, pp. 1036-1041, vol. 109.
- Verified: METADATA
- Notes: Added at integration. The paper states Godfrey-Smith's view only as reported by Chalmers ("Chalmers reports that..."); upgrade to FULLTEXT if the paper is read.

### C-01-059
- Claim: Reality+ (2022) is the book whose argument the précis summarizes; cited as the original source, content taken from Chalmers2024precis.
- Source: Chalmers2022reality
- Locator: W. W. Norton, 2022, ISBN 9780393635805
- Evidence: Open Library edition record for ISBN 9780393635805: "Reality+ Virtual Worlds and the Problems of Philosophy", Norton, 2022, 528 pp.
- Verified: METADATA
- Notes: Added at integration. The section states the book's content "as summarized in his précis"; no claim rests on the book text itself.
