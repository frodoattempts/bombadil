# Claim ledger 02: digital physics and computational views of nature

Topic: intellectual antecedents and neighbouring programmes (digital physics,
computable universe, pancomputationalism, mathematical universe) and how they
differ from the simulation hypothesis proper.

Texts read are cached under `/tmp/claude-0/papers/` (arXiv IDs as filenames;
`feynman1982.pdf`, `deutsch85.pdf`, `fredkin_toffoli82.pdf`,
`wheeler_cqi.pdf`, `floridi2009.pdf`, `sep_comp_phys.html`, `kadanoff.html`,
`weinberg_nyrb.html`, `nks_*.html`, `moravec_pigs.html`).

Verification legend follows `research/CONVENTIONS.md`. Where a claim rests on a
secondary source quoting a primary one that we could not open, the Source is the
secondary source and the Notes say so.

---

## A. Zuse, Fredkin and the MIT "physics of computation" circle

### C-02-001
- Claim: Zuse's "Rechnender Raum" appeared first as a journal article in *Elektronische Datenverarbeitung* 8 (1967) 336–344, then as a book (Vieweg, Braunschweig, 1969), and in English as the MIT technical translation *Calculating Space* (AZT-70-164-GEMIT, Project MAC, 1970).
- Source: Zuse1967rechnender; Zuse1969rechnender; Zuse1970calculating
- Locator: Floridi2009against reference list (accepted MS p. 39); Crossref record for DOI 10.1007/978-3-663-02723-2; J. Schmidhuber's IDSIA page "Zuse's Thesis" (people.idsia.ch/~juergen/digitalphysics.html, accessed 2026-09-27)
- Evidence: "Zuse, K. 1967, "Rechnender Raum", Elektronische Datenverarbeitung, 8, 336-344. Zuse, K. 1969, Rechnender Raum (Braunschweig: Vieweg). Eng. tr. with the title Calculating Space, MIT Technical Translation AZT-70-164-GEMIT, Massachusetts Institute of Technology (Project MAC), Cambridge, Mass. 1970."
- Verified: METADATA
- Notes: Two independent bibliographic sources agree (Floridi's reference list; Schmidhuber's page). We could NOT open Zuse's text in any form (IDSIA ftp scans offline, PhilArchive and mathrix.org blocked, Springer blocked). No characterization of Zuse's own argument may be sourced to Zuse directly; use C-02-002/003.

### C-02-002
- Claim: The SEP entry on physical computation identifies Zuse and Fredkin as the originators of the "earliest and best known" version of ontic pancomputationalism, according to which the universe is a giant cellular automaton, and says Fredkin's (largely unpublished) ideas influenced Feynman, Toffoli and Wolfram.
- Source: Piccinini2025computation
- Locator: §3.4 "The Universe as a Computing System"
- Evidence: "The earliest and best known version of ontic pancomputationalism is due to Konrad Zuse (1970, 1982) and Edward Fredkin, whose unpublished ideas on the subject influenced a number of American physicists (e.g., Feynman 1982, Toffoli 1982, Wolfram 2002; see also Wheeler 1982, Fredkin 1990). According to some of these physicists, the universe is a giant cellular automaton."
- Verified: FULLTEXT
- Notes: SEP version with substantive revision dated 20 Aug 2025, accessed 2026-09-27.

### C-02-003
- Claim: Floridi takes the core thesis of digital ontology to be that the physical universe (time, space and every entity and process in spacetime) is ultimately discrete, and summarizes the position shared by most digital ontologists as the "Zuse Thesis" that the universe is deterministically computed on a giant discrete computer, notes that the computer was taken to be a cellular automaton by Zuse (1967, following von Neumann), Fredkin and Wolfram, a universal Turing machine by Schmidhuber, and a quantum computer by Lloyd.
- Source: Floridi2009against
- Locator: §2 "What is Digital Ontology? It from Bit" (accepted MS pp. 4–5)
- Evidence: "1) the nature of the physical universe (time, space and every entity and process in space-time) is ultimately discrete." ... "ZT) "the universe is being deterministically computed on some sort of giant but discrete computer" (Zuse [1969]). The computer referred to in ZT could be a cellular automaton. This is argued by Zuse [1967], also on the basis of Von Neumann [1966], by Fredkin [2003b] and, more recently, by Wolfram [2002]. [...] Alternatively, the computer in ZT could be a universal Turing machine, as suggested by Schmidhuber [1997] [...] or a quantum computer, as proposed more recently by Lloyd [2006]."
- Verified: FULLTEXT
- Notes: Read in the author's accepted manuscript (UHRA eprint 2203), not the Springer version of record. The ZT wording is Floridi's rendering attributed to Zuse (1969); we could not check it against Zuse's text, so the paper should attribute the formulation to Floridi.

### C-02-004
- Claim: Feynman's 1981 keynote "Simulating physics with computers" states that his interest in the topic was inspired by Edward Fredkin.
- Source: Feynman1982simulating
- Locator: §1, p. 467
- Evidence: "The reason for doing this is something that I learned about from Ed Fredkin, and my entire interest in the subject has been inspired by him."
- Verified: FULLTEXT
- Notes: Text read from a course-hosted scan of the IJTP article (s2.smu.edu).

### C-02-005
- Claim: Feynman distinguished approximate numerical simulation from "exact simulation", and observed that exact simulation would require everything in a finite spacetime volume to be analysable with a finite number of logical operations, which present physics (with its continuum) does not satisfy.
- Source: Feynman1982simulating
- Locator: §1, p. 468
- Evidence: "I want to talk about the possibility that there is to be an exact simulation, that the computer will do exactly the same as nature. [...] it's going to be necessary that everything that happens in a finite volume of space and time would have to be exactly analyzable with a finite number of logical operations. The present theory of physics is not that way, apparently. [...] and therefore, if this proposition is right, physical law is wrong."
- Verified: FULLTEXT
- Notes: Complexity aspects of the same paper (exponential cost of classical simulation of QM) belong to section 06.

### C-02-006
- Claim: Feynman noted that replacing continuous space by a simple lattice with discrete time would generically make the speed of light slightly direction-dependent, producing anisotropies that experiment constrains.
- Source: Feynman1982simulating
- Locator: §1, p. 468
- Evidence: "we might change the idea that space is continuous to the idea that space perhaps is a simple lattice and everything is discrete [...] the first difficulty that would come out is that the speed of light would depend slightly on the direction, and there might be other anisotropies in the physics that we could detect experimentally."
- Verified: FULLTEXT
- Notes: Qualitative remark, no numbers. Cross-link to section 03 (lattice/Lorentz violation).

### C-02-007
- Claim: Feynman called Fredkin's programme of finding a computer simulation of physics "an excellent program", while insisting that such a simulation must be quantum mechanical.
- Source: Feynman1982simulating
- Locator: §9 (closing remarks), p. 486
- Evidence: "The program that Fredkin is always pushing, about trying to find a computer simulation of physics, seem to me to be an excellent program to follow out. [...] because nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical"
- Verified: FULLTEXT
- Notes: —

### C-02-008
- Claim: Fredkin and Toffoli's conservative logic is a model of computation built to respect reversibility and additive conservation laws; its billiard-ball realization shows that a perfect gas in a suitably shaped container can reproduce the functional behaviour of a general-purpose digital computer.
- Source: Fredkin1982conservative
- Locator: Abstract; §1
- Evidence: "Conservative logic is a comprehensive model of computation which explicitly reflects a number of fundamental principles of physics, such as the reversibility of the dynamical laws and the conservation of certain additive quantities [...] Quite literally, the functional behavior of a general-purpose digital computer can be reproduced by a perfect gas placed in a suitably shaped container and given appropriate initial conditions."
- Verified: FULLTEXT
- Notes: Read in a course-hosted copy (cs.princeton.edu); pagination differs from IJTP 21:219–253. This paper runs "computation → physics" (physical realizability of computing), not "physics is computation"; the tex should present it that way.

### C-02-009
- Claim: Fredkin set out "digital mechanics" in Physica D (1990) and "digital philosophy" in IJTP (2003).
- Source: Fredkin1990informational; Fredkin2003introduction
- Locator: bibliographic records (Crossref)
- Evidence: Crossref: "An informational process based on reversible universal cellular automata", Physica D 45 (1990) 254–270; "An Introduction to Digital Philosophy", Int. J. Theor. Phys. 42(2) (2003) 189–247.
- Verified: METADATA
- Notes: Both paywalled; no open copy found (OpenAlex/Unpaywall: closed). SEP lists the 1990 title as "Digital Mechanics: An Information Process Based on Reversible Universal Cellular Automata"; Crossref omits the "Digital Mechanics:" prefix. A 209-page Fredkin manuscript "Digital Mechanics" (2000, marked "Working Draft – Do not Circulate") is online but must not be cited.

### C-02-010
- Claim: As quoted by Floridi, Fredkin's 2003 digital philosophy takes space and time to be discrete, takes the bit as the unit of state, and requires that its models eventually re-derive the equations of current science.
- Source: Floridi2009against (quoting Fredkin2003introduction pp. 190–191)
- Locator: Floridi §2.1 (accepted MS p. 8)
- Evidence: "In physics, DP assumes that space and time are discrete. [...] What we must demand of DP is the eventual ability to derive, from our DP models of fundamental processes, the same mathematical equations that constitute the basis of science today. [...] Thus the unit of state is the bit, which is considerably simpler than a real number. (Fredkin [2003b], 190-191)."
- Verified: FULLTEXT
- Notes: Secondary quotation; Fredkin's article itself not read.

### C-02-011
- Claim: Piccinini cites Fredkin (2003, p. 193) for the option that the computation making up our universe is a simulation run on a computer in another universe whose physics is inaccessible to us.
- Source: Piccinini2025computation
- Locator: §3.4
- Evidence: "One is that we live in a computational simulation: the appearance of our physical universe is the result of a simulation run on a computer that exists in its own universe, whose physics we have no access to (Fredkin 2003, 193)."
- Verified: FULLTEXT
- Notes: Secondary characterization of Fredkin 2003 (not read). In the tex, attribute the reading to the SEP entry.

### C-02-012
- Claim: Toffoli (1984) published a paper whose title presents cellular automata as an alternative to, rather than an approximation of, differential equations in modelling physics.
- Source: Toffoli1984cellular
- Locator: bibliographic record (Crossref)
- Evidence: Title: "Cellular automata as an alternative to (rather than an approximation of) differential equations in modeling physics", Physica D 10 (1984) 117–127.
- Verified: METADATA
- Notes: Paywalled; abstract not obtained. The tex may cite only the title.

### C-02-013
- Claim: Zuse, Wheeler and Feynman papers all appeared in the same 1982 issue of the International Journal of Theoretical Physics (vol. 21, no. 6–7), and Feynman's text refers to Fredkin and Toffoli's work as appearing in "these Proceedings".
- Source: Feynman1982simulating; Zuse1982computing; Wheeler1982computer
- Locator: Crossref records; Feynman p. 469
- Evidence: Crossref: IJTP 21(6–7): Feynman 467–488, Wheeler 557–572, Zuse 589–600. Feynman: "(Editors' note: see papers by Bennett, Fredkin, and Toffoli, these Proceedings)."
- Verified: METADATA
- Notes: Fredkin & Toffoli's paper is in IJTP 21(3–4). We did not verify the conference name or dates. Zuse 1982 and Wheeler 1982 not read.

## B. Wheeler: "it from bit"

### C-02-014
- Claim: Wheeler's "it from bit" holds that every physical quantity derives its ultimate significance from binary yes/no registrations, i.e. elementary acts of observer-participancy.
- Source: Wheeler1990information
- Locator: Abstract; §19.1
- Evidence: "No element in the description of physics shows itself as closer to primordial than the elementary quantum phenomenon, that is, the elementary device-intermediated act of posing a yes-no physical question and eliciting an answer or, in brief, the elementary act of observer-participancy. Otherwise stated, every physical quantity, every it, derives its ultimate significance from bits, binary yes-or-no indications, a conclusion which we epitomize in the phrase, it from bit."
- Verified: FULLTEXT
- Notes: Read in a reprint (chapter 19 of an unidentified edited volume) that states it reproduces Proc. 3rd Int. Symp. Foundations of Quantum Mechanics, Tokyo 1989, pp. 354–368. Floridi quotes the same passage from the Zurek (1990) volume, p. 5, with identical wording.

### C-02-015
- Claim: Wheeler denied the existence of a continuum and of space and time at the microscopic level, summarizing: "continuum-based physics, no; information-based physics, yes."
- Source: Wheeler1990information
- Locator: Abstract (conclusions 2–3); §19.3 "Four no's" (third and fourth "no")
- Evidence: "(2) There is no such thing at the microscopic level as space or time or spacetime continuum." ... "In brief, continuum-based physics, no; information-based physics, yes."
- Verified: FULLTEXT
- Notes: —

### C-02-016
- Claim: Wheeler explicitly rejected the conception of the universe as a machine, partly because it requires postulating a "supermachine" that produces universes.
- Source: Wheeler1990information
- Locator: Abstract (conclusion 1); §19.3 ("Universe as machine?")
- Evidence: "(1) The world cannot be a giant machine, ruled by any preestablished continuum physical law." ... "We reject here the concept of universe as machine not least because it "has to postulate explicitly or implicitly, a supermachine, a scheme, a device, a miracle, which will turn out universes in infinite variety and infinite number""
- Verified: FULLTEXT
- Notes: Important for the distinction: "it from bit" is not a "universe run by a computer" thesis.

### C-02-017
- Claim: Floridi argues that digital ontology and pancomputationalism are independent positions, citing Wheeler as someone who held the former but not (explicitly) the latter.
- Source: Floridi2009against
- Locator: §2 (accepted MS p. 6)
- Evidence: "However, digital ontology and pancomputationalism are independent positions. Famously, Wheeler supported the former but not (or at least not explicitly) the latter." ... "Physical processes in Wheeler's participatory universe might, but need not, be reducible to computational state transitions."
- Verified: FULLTEXT
- Notes: —

## C. Deutsch and the physical Church–Turing principle

### C-02-018
- Claim: Deutsch (1985) recast the Church–Turing hypothesis as a physical principle: every finitely realizable physical system can be perfectly simulated by a universal model computing machine operating by finite means.
- Source: Deutsch1985quantum
- Locator: §1, principle (1.2)
- Evidence: "'Every finitely realizable physical system can be perfectly simulated by a universal model computing machine operating by finite means'."
- Verified: FULLTEXT
- Notes: Read in the 1999 LaTeX re-edition by W. van Dam hosted on Deutsch's site; principle numbering (1.2) as in original. Deutsch calls it "the Church-Turing principle"; the eponym "Church–Turing–Deutsch principle" is later usage and does not appear in the paper.

### C-02-019
- Claim: Deutsch argued that classical physics with its continuum does not obey the strong form of the principle with respect to the Turing machine, whereas quantum theory is compatible with it via a universal quantum computer.
- Source: Deutsch1985quantum
- Locator: Abstract; §1 (discussion after (1.2))
- Evidence: "Classical physics and the universal Turing machine, because the former is continuous and the latter discrete, do not obey the principle, at least in the strong form above." ... "Thus quantum theory is compatible with the strong form (1.2) of the Church-Turing principle."
- Verified: FULLTEXT
- Notes: Deutsch notes that the compatibility result relies on the third law of thermodynamics (section "Connections between the Church-Turing principle and other parts of physics").

### C-02-020
- Claim: Deutsch held that the principle is an empirical principle with the same epistemological status as other physical principles, falsifiable only indirectly (compared with the third law of thermodynamics).
- Source: Deutsch1985quantum
- Locator: §1
- Evidence: "I shall show that it has the same epistemological status as other physical principles." ... "The third law of thermodynamics [...] bears a certain resemblance to that of the Church-Turing principle, is likewise not directly refutable"
- Verified: FULLTEXT
- Notes: —

## D. Lloyd: physical limits and the "universe as quantum computer"

### C-02-021
- Claim: Lloyd (2000) derived that a system of average energy E can perform at most 2E/(πħ) elementary operations per second, so that a 1 kg "ultimate laptop" is limited to about 5.4 × 10^50 operations per second.
- Source: Lloyd2000ultimate
- Locator: §1 (arXiv v3 p. 2)
- Evidence: "a system with average energy E can perform a maximum of 2E/πh̄ logical operations per second. A one kilogram computer has average energy E = mc2 = 8.9874 × 10^16 joules. Accordingly, the ultimate laptop can perform a maximimum of 5.4258 × 10^50 operations per second."
- Verified: FULLTEXT
- Notes: Based on the Margolus–Levitin theorem. Upper bound, not an achievable figure. Spelling "maximimum" is in the source.

### C-02-022
- Claim: Lloyd (2002) estimated that the observable universe can have performed no more than about 10^120 elementary operations on about 10^90 bits (about 10^120 bits if gravitational degrees of freedom are included), with the operation count scaling as (t/t_P)^2.
- Source: Lloyd2002computational
- Locator: Abstract; p. 2; Eq. (2) p. 5
- Evidence: "The universe can have performed no more than 10^120 ops on 10^90 bits." ... "the total number of bits (≈ 10^90 in matter, ≈ 10^120 if gravitation is taken into account) and ops (≈ 10^120 ) turn out to be simple polynomials in the fundamental constants" ... "#ops ≈ ρc c5 t4 /h̄ ≈ t2 c5 /Gh̄ = (t/tP )2 ."
- Verified: FULLTEXT
- Notes: Order-of-magnitude estimates; Lloyd drops factors of 2, π ("X ≈ Y is equivalent to log X = log Y + O(1)"). arXiv v1 (2001) read; published PRL 88, 237901 (2002).

### C-02-023
- Claim: Lloyd offered three readings of these numbers: upper bounds on computation performed by matter; lower bounds on the resources needed by a quantum computer to simulate the universe directly; and, "more controversial", the actual memory and operations of the universe regarded as a computation.
- Source: Lloyd2002computational
- Locator: p. 2 (numbered list); §6 "Discussion" pp. 13–15
- Evidence: "1. They give upper bounds to the amount of computation that can have been performed by all the matter in the universe since the universe began. 2. They give lower bounds to the number of ops and bits required to simulate the entire universe on a quantum computer. 3. If one chooses to regard the universe as performing a computation, these numbers give the numbers of ops and bits in that computation." ... "The third interpretation [...] is more controversial."
- Verified: FULLTEXT
- Notes: Reading 2 is the one relevant to the simulation hypothesis; cross-link section 06.

### C-02-024
- Claim: Lloyd answered "Is the universe a computer?" by saying it depends on the meaning of "computer" and "is": the universe is not a conventional digital computer, but since almost any interaction supports universal quantum logic, it "can still compute".
- Source: Lloyd2002computational
- Locator: §6, p. 15
- Evidence: "Is the universe a computer? The answer to this question depends both on the meaning of 'computer' and on the meaning of 'is.' On the one hand, the universe is certainly not a digital computer running Linux or Windows. [...] Even if the universe is not a conventional computer, it can still compute."
- Verified: FULLTEXT
- Notes: —

### C-02-025
- Claim: In a preprint, Lloyd proposed a theory of quantum gravity in which spacetime geometry is derived from an underlying quantum computation.
- Source: Lloyd2005theory
- Locator: Abstract (arXiv v9, 2018)
- Evidence: "This paper proposes a method of unifying quantum mechanics and gravity based on quantum computation. [...] The geometry of space-time is a construct, derived from the underlying quantum information processing."
- Verified: ABSTRACT
- Notes: Unrefereed preprint as far as we could find (no journal ref on arXiv or INSPIRE). v1 title (INSPIRE) was "The Computational universe: Quantum gravity from quantum computation".

### C-02-026
- Claim: The SEP entry classifies Lloyd's (2006) view as the quantum version of ontic pancomputationalism, which it describes as less radical than the classical version and possibly a reformulation of quantum mechanics without change in empirical content.
- Source: Piccinini2025computation
- Locator: §3.4
- Evidence: "According to the quantum version of ontic pancomputationalism, the universe is not a classical computer but a quantum computer [...] (Lloyd 2006)" ... "quantum ontic pancomputationalism may be seen as a reformulation of quantum mechanics in the language of quantum computation and quantum information theory (qubits), without changes in the empirical content of the theory"
- Verified: FULLTEXT
- Notes: Lloyd2006programming (book) is METADATA only for us.

## E. Wolfram: NKS (2002), its reception, and the 2020 Physics Project

### C-02-027
- Claim: In *A New Kind of Science* Wolfram raised the possibility that a simple program, run long enough, could reproduce the universe in every detail, and would then be a complete and precise representation rather than an approximation.
- Source: Wolfram2002new
- Locator: Ch. 9, §5 "Ultimate Models for the Universe", p. 465 (online edition, wolframscience.com)
- Evidence: "could it even be that underneath all the complex phenomena we see in physics there lies some simple program which, if run for long enough, would reproduce our universe in every detail? [...] with such a program one would finally have a model of nature that was not in any sense an approximation or idealization."
- Verified: FULLTEXT
- Notes: Read in the publisher's free online edition.

### C-02-028
- Claim: In a note, Wolfram mentioned Zuse and Fredkin's cellular-automaton universes and science-fiction ideas of a simulated world, but wrote that no literal mechanistic model "can ever in the end realistically be expected to work".
- Source: Wolfram2002new
- Locator: Notes to Ch. 9 §5, "Mechanistic models [in physics]", p. 1026
- Evidence: "Since the 1950s science fiction has sometimes featured the idea that the universe or some part of it—such as the Earth—could be an intentionally created computer, or that our perception of the universe could be based on a computer simulation. Starting in the 1950s a few computer scientists considered the idea that the universe might have components like a computer. Konrad Zuse suggested that it could be a continuous cellular automaton; Edward Fredkin an ordinary cellular automaton [...] no such literal mechanistic model can ever in the end realistically be expected to work."
- Verified: FULLTEXT
- Notes: Wolfram's characterization of Zuse ("continuous cellular automaton") not checked against Zuse. Floridi (fn. 7) cites this note in reading Wolfram as rejecting classical CA models.

### C-02-029
- Claim: Aaronson's review argued that the discrete causal-network ideas of NKS Chapter 9 had been discussed earlier in quantum gravity, and that the main difference he could discern was that Wolfram's model is explicitly classical.
- Source: Aaronson2002book
- Locator: §3 "Fundamental Physics"
- Evidence: "The above ideas have all been discussed previously by researchers in quantum gravity: in particular, that spacetime is a causal network arising from graph updating rules [13]; that particles could arise as 'topological defects' in such a network [16]; and that dimension and other geometric properties can be defined solely in terms of the network's connectivity pattern [17]. The main difference we can discern between Wolfram's model and earlier ones is that Wolfram's is explicitly classical."
- Verified: FULLTEXT
- Notes: arXiv v2; published QIC 2(5):410–423 (2002).

### C-02-030
- Claim: Aaronson showed that Wolfram's deterministic "long-range thread" proposal for entanglement cannot simultaneously satisfy causal invariance, the relativity postulate, and Bell-inequality violation when rules act on definite graphs.
- Source: Aaronson2002book
- Locator: §3, §3.2 "Bell's theorem and causal invariance" (assertions (1)–(4))
- Evidence: "We show that this proposal cannot be made compatible with both special relativity and Bell inequality violations." ... "Our goal is to show that, for any R, at least one of these assertions is false."
- Verified: FULLTEXT
- Notes: The argument targets the NKS (2002) framework, where Wolfram disallows multiway evolution. Whether it applies to the 2020 multiway models was not addressed in any source we reviewed (see report).

### C-02-031
- Claim: Kadanoff's Physics Today review called the NKS physics chapter "a partially formed idea—exciting, but not yet science", attributed the automaton-universe view to Fredkin, and found "no new kinds of calculations, no new analytic theory, and no comparison with experiment".
- Source: Kadanoff2002new
- Locator: Physics Today 55(7), pp. 55–56
- Evidence: "The view that the universe is an automaton is due to Fredkin. But, the specific elements in Wolfram's speculation emulate previous two-dimensional quantum gravity theories and earlier work on integrable systems. This chapter describes a partially formed idea—exciting, but not yet science." ... "I see no new kinds of calculations, no new analytic theory, and no comparison with experiment."
- Verified: FULLTEXT
- Notes: Read on the publisher's HTML page (pubs.aip.org via doi.org).

### C-02-032
- Claim: Weinberg's review found no motivation for Wolfram's discrete-universe speculation beyond familiarity with computers ("So might a carpenter, looking at the moon, suppose that it is made of wood"), and noted that computational equivalence of automata to continuous systems holds only if nothing in nature is truly continuous.
- Source: Weinberg2002is
- Locator: New York Review of Books, 24 Oct 2002 (web text)
- Evidence: "Following an idea of Edward Fredkin, he concludes that the universe itself would then be an automaton, like a giant computer. It's possible, but I can't see any motivation for these speculations, except that this is the sort of system that Wolfram and others have become used to in their work on computers. So might a carpenter, looking at the moon, suppose that it is made of wood." ... "Only if Wolfram were right that neither space nor time nor anything else is truly continuous (which is a separate issue) would the Turing machine or the rule 110 cellular automaton be computationally equivalent to an analog computer or a quantum computer or a brain or the universe."
- Verified: FULLTEXT
- Notes: Essay review, not peer-reviewed; cited as a critique that is itself the object of discussion (CONVENTIONS §3).

### C-02-033
- Claim: Wolfram's 2020 models represent the universe as an evolving hypergraph with no intrinsic space, time or matter, and propose that "causal invariance" of the rewriting rules yields Lorentz invariance, general covariance, gauge invariance and objective reality in quantum mechanics; Wolfram describes the correspondence as sometimes speculative.
- Source: Wolfram2020class
- Locator: §8.1–8.2 (arXiv v1 pp. 353–354)
- Evidence: "the complete structure and content of the universe is represented by an evolving hypergraph. There is no intrinsic notion of space [...] There is also no intrinsic notion of matter [...] There is also no intrinsic notion of time." ... "this equivalence seems to yield several core known features of physics, notably Lorentz invariance in special relativity, general covariance in general relativity, as well as local gauge invariance, and the perception of objective reality in quantum mechanics." ... "what will be said here is merely an indication—and sometimes a speculative one—of how this might turn out." ... "There are, however, many choices for the sequences in which the events can occur, and the idea is that all possible branches in some sense do occur."
- Verified: FULLTEXT
- Notes: Published Complex Systems 29(2):107–536 (2020). The branching ("multiway") evolution contrasts with NKS, where, per Aaronson (C-02-030), Wolfram disallowed multiway systems: "Wolfram requires the network evolution to be deterministic, by disallowing 'multiway systems'".

### C-02-034
- Claim: In the 2020 paper Wolfram presents experimentally testable predictions as a prospect rather than a result, and suggests that the model's elementary length need not equal the Planck length.
- Source: Wolfram2020class
- Locator: §8.2 (p. 355); §8.20 "Units and Scales" (pp. 413–414)
- Evidence: "even absent the determination of a specific rule, it seems increasingly likely that experimentally accessible predictions will be possible just from general features of our models." ... "if this were the case, then our various elementary quantities would be equal to their corresponding Planck units [...] But the setup of our models suggests something different"
- Verified: FULLTEXT
- Notes: Relevant to section 03 (scale of discreteness).

### C-02-035
- Claim: Gorard (2020) claims proofs that causal invariance of Wolfram-model rewriting is equivalent to a discrete general covariance, from which a discrete Lorentz covariance follows, and, under a dimension-preservation assumption, a discrete form of the Einstein field equations.
- Source: Gorard2020some
- Locator: Abstract
- Evidence: "we prove that causal invariance [...] is equivalent to a discrete version of general covariance [...] This fact then allows one to deduce a discrete analog of Lorentz covariance [...] (along with the assumption that the updating rules preserve the dimensionality of the causal graph in limiting cases) to prove that the most general set of constraints on the discrete spacetime Ricci tensor corresponds to a discrete form of the Einstein field equations."
- Verified: ABSTRACT
- Notes: Body not checked. Published Complex Systems 29(2):599–654.

### C-02-036
- Claim: Gorard has also argued that Wolfram-model hypergraph rewriting can be read as an algorithmic dynamics for causal-set evolution.
- Source: Gorard2020algorithmic
- Locator: Abstract
- Evidence: "it is demonstrated that the hypergraph rewriting approach of the Wolfram model can effectively be interpreted as providing an underlying algorithmic dynamics for causal set evolution."
- Verified: ABSTRACT
- Notes: arXiv preprint (no journal ref found).

### C-02-037
- Claim: Butterfield and Dowker argue that if a quantum gravity theory is physically discrete at the Planck scale and recovers general relativity, causal sets must arise within it; they list the Wolfram model among discretely flavoured approaches whose status under their argument remains to be assessed.
- Source: Butterfield2024recovering
- Locator: Abstract; §2 (arXiv v1 p. 10, ref. [37] = Gorard 2020)
- Evidence: "An argument is presented that if a theory of quantum gravity is physically discrete at the Planck scale and the theory recovers General Relativity as an approximation, then, at the current stage of our knowledge, causal sets must arise within the theory, even if they are not its basis." ... "and the Wolfram model [37], among others. It would be a good project to assess these discretely flavoured quantum gravity approaches"
- Verified: FULLTEXT
- Notes: Read arXiv:2106.01297v1 (2021). Published Philosophy of Physics 2(1):5 (2024); published text not checked (publisher host blocked). Author order differs: arXiv metadata Dowker–Butterfield, PDF and journal Butterfield–Dowker.

## F. 't Hooft: the Cellular Automaton Interpretation

### C-02-038
- Claim: 't Hooft's Cellular Automaton Interpretation treats quantum mechanics as a tool for analysing a system that may be classical and deterministic at its core, and argues that the usual objections to "superdeterminism" can be overcome in principle.
- Source: tHooft2016cellular
- Locator: Abstract (arXiv v3); §1.3
- Evidence: "Quantum mechanics is looked upon as a tool, not as a theory. [...] we argue that even the Standard Model, together with gravitational interactions, might be viewed as a quantum mechanical approach to analyse a system that could be classical at its core. We explain how such thoughts can conceivably be reconciled with Bell's theorem, and how the usual objections voiced against the notion of 'superdeterminism' can be overcome, at least in principle."
- Verified: FULLTEXT
- Notes: arXiv:1405.1548v3 (Dec 2015); Springer book (2016). Page numbers of the book not checked.

### C-02-039
- Claim: 't Hooft states as a "firm prediction" of the CAI that quantum computers will not outperform a classical computer with one memory site per Planck volume (or Planck area, holographically) operating at one step per Planck time.
- Source: tHooft2016cellular
- Locator: §5.8 "The quantum computer" (arXiv v3 p. 79)
- Evidence: "Our theory comes with a firm prediction: Yes, by making good use of quantum features, it will be possible in principle, to build a computer vastly superior to conventional computers, but no, these will not be able to function better than a classical computer would do, if its memory sites would be scaled down to one per Planckian volume element (or, in view of the holographic principle, one memory site per Planckian surface element), and if its processing speed would increase accordingly, typically one operation per Planckian time unit of 10−43 seconds."
- Verified: FULLTEXT
- Notes: Cross-link section 06 (complexity).

## G. Schmidhuber and Tegmark: ensembles, algorithmic priors, mathematical universe

### C-02-040
- Claim: Schmidhuber (1997) framed his analysis around a "Great Programmer" who runs all computable universes on a "Big Computer", "computable" meaning discrete time and finitely describable states, and argued that computing all universes (e.g. by dovetailing) requires far less information than computing one arbitrary universe.
- Source: Schmidhuber1997computer
- Locator: "Preliminaries"; "All Universes are Cheaper Than Just One" (arXiv pp. 1–4)
- Evidence: "A long time ago, the Great Programmer wrote a program that runs all possible universes on His Big Computer. "Possible" means "computable": (1) Each universe evolves on a discrete time scale. (2) Any universe's state at a given time is describable by a finite number of bits." ... "In general, computing all evolutions of all universes is much cheaper in terms of information requirements than computing just one particular, arbitrarily chosen evolution."
- Verified: FULLTEXT
- Notes: Published LNCS 1337:201–208.

### C-02-041
- Claim: Schmidhuber noted that inhabitants of a computed universe run on local time and cannot tell how many steps the underlying computer spends per time step.
- Source: Schmidhuber1997computer
- Locator: "Preliminaries", paragraph "Time" (arXiv p. 2)
- Evidence: "Creatures which evolve in any of the universes don't have to worry either. They run on local time and have no idea of how many instructions it takes the Big Computer to compute one of their time steps"
- Verified: FULLTEXT
- Notes: —

### C-02-042
- Claim: Schmidhuber (2000) proposed a resource-based "speed prior" over computable universe histories and derived from it the prediction that apparently random events such as individual beta decays are generated by a fast pseudorandom algorithm.
- Source: Schmidhuber2000algorithmic
- Locator: §7.4–7.5.1 (arXiv v2 pp. 37–38)
- Evidence: "This immediately leads to the speed prior S." ... "Based on prior S, we predict: anything that appears random or noisy in our own particular world is due to hitherto unknown regularities" ... "given S, a very simple and fast but maybe not quite trivial PRG should be responsible for the decay pattern of possibly widely separated neutrons."
- Verified: FULLTEXT
- Notes: arXiv technical report; Sections 1–5 published in IJFCS 13(4):587–612 (2002), Section 6 in COLT 2002 (per arXiv journal-ref). The motivation there uses a "Great Programmer" with finite resources (p. 37).

### C-02-043
- Claim: Tegmark's Mathematical Universe Hypothesis (MUH) holds that our external physical reality is a mathematical structure; the 1998 precursor postulated that all mathematically existing structures exist physically.
- Source: Tegmark2008mathematical; Tegmark1998is
- Locator: Tegmark 2008 abstract and §VIII; Tegmark 1998 abstract
- Evidence: 2008: "the Mathematical Universe Hypothesis (MUH) that our physical world is an abstract mathematical structure." 1998: "The only postulate in this theory is that all structures that exist mathematically exist also physically"
- Verified: FULLTEXT (2008); ABSTRACT (1998)
- Notes: —

### C-02-044
- Claim: Tegmark's Computable Universe Hypothesis (CUH) adds that the relations defining that structure are computable by halting computations; he stresses that the CUH requires the description, not the time evolution, to be computable, so that "the universe is a mathematical structure according to the MUH, as opposed to a computation according to the simulation hypothesis."
- Source: Tegmark2008mathematical
- Locator: §VII (definition), §VII A "Relation to other hypotheses"
- Evidence: "Computable Universe Hypothesis (CUH): The mathematical structure that is our external physical reality is defined by computable functions." ... "By this we mean that the relations (functions) that define the mathematical structure as in Appendix A 1 can all be implemented as computations that are guaranteed to halt after a finite number of steps." ... "Note that the CUH is a different hypothesis: it requires the description (the relations) rather than the time evolution to be computable. In other words, in terms of the three vertices of Figure 5, the universe is a mathematical structure according to the MUH, as opposed to a computation according to the simulation hypothesis."
- Verified: FULLTEXT
- Notes: Tegmark's footnote 14 distinguishes "exactly computable" from "approximately computable" functions; functions of a real variable are never exactly computable in his sense.

### C-02-045
- Claim: Tegmark argued that a simulating computer need not evolve the universe step by step but only specify it (e.g. store 4-dimensional data), calling the identification of physical time with computational steps "a common misconception in the universe simulation literature".
- Source: Tegmark2008mathematical
- Locator: §VI B "The time misconception"
- Evidence: "A common misconception in the universe simulation literature is that our physical notion of a one-dimensional time must then necessarily be equated with the step-by-step one-dimensional flow of the computation." ... "In conclusion, the role of the simulating computer is not to compute the history of our universe, but to specify it."
- Verified: FULLTEXT
- Notes: —

### C-02-046
- Claim: Tegmark concedes that virtually all historically successful physical theories violate the CUH because they use the continuum.
- Source: Tegmark2008mathematical
- Locator: §VII G "Challenges for the CUH"
- Evidence: "A more immediate challenge is that virtually all historically successful theories of physics violate the CUH, and that it is far from obvious whether a viable computable alternative exists. The main source of CUH violation comes from incorporating the continuum"
- Verified: FULLTEXT
- Notes: —

### C-02-047
- Claim: Tegmark lists Tipler, Bostrom and Schmidhuber as having discussed the probability that we are simulated, and describes Lloyd's view as an "intermediate possibility" of an analog quantum simulation "not designed by anybody".
- Source: Tegmark2008mathematical
- Locator: §VI A "Are we simulated?"
- Evidence: "Tipler [116], Bostrom [117] and Schmidhuber [13, 17] have gone as far as discussing the probability that we are simulated" ... "Lloyd has advanced the intermediate possibility that we live in an analog simulation performed by a quantum computer, albeit not a computer designed by anybody"
- Verified: FULLTEXT
- Notes: Ref [116] = Tipler, The Physics of Immortality (Doubleday, 1994).

## H. Philosophical analyses of pancomputationalism and digital ontology

### C-02-048
- Claim: The SEP entry distinguishes unlimited pancomputationalism (every sufficiently complex system implements every or very many computations; Putnam, Searle) from limited pancomputationalism (every system performs some computation), and both from ontic pancomputationalism, which originates in physics and combines an empirical and a metaphysical claim.
- Source: Piccinini2025computation
- Locator: §3.1; §3.4
- Evidence: "The strongest version of pancomputationalism is that every physical system performs every computation — or at least, every sufficiently complex system implements a large number of non-equivalent computations (Putnam 1988, Searle 1992). This may be called unlimited pancomputationalism." ... "Unlike the previous versions of pancomputationalism, which originate in philosophy, this ontic pancomputationalism originates in physics. It includes both an empirical claim and a metaphysical one."
- Verified: FULLTEXT
- Notes: —

### C-02-049
- Claim: According to the SEP entry, the empirical claim of ontic pancomputationalism is that fundamental magnitudes and state transitions are exactly (not approximately) described by a computational formalism, and for a classical cellular-automaton universe this requires that all fundamental magnitudes, and space and time, be discrete.
- Source: Piccinini2025computation
- Locator: §3.4
- Evidence: "The empirical claim is that all fundamental physical magnitudes and their state transitions are such as to be exactly described by an appropriate computational formalism — without resorting to the approximations that are a staple of standard computational modeling." ... "For the universe to be a cellular automaton, all fundamental physical magnitudes must be discrete [...] In addition, time and space must be fundamentally discrete or must emerge from the discrete processing of the cellular automaton."
- Verified: FULLTEXT
- Notes: —

### C-02-050
- Claim: The SEP entry notes that the metaphysical claim (computation is what the universe is made of) needs an account of what the computation is, and lists three options: a simulation run on a computer in another universe, computations as abstract mathematical entities (a computational Pythagoreanism), or computational structural realism.
- Source: Piccinini2025computation
- Locator: §3.4
- Evidence: "Such a metaphysical claim requires an account of what computation, or software, or physical information, is. [...] One is that we live in a computational simulation [...] A second alternative is that computations are abstract, mathematical entities, like numbers and sets. [...] A third alternative is a computational version of ontic structural realism."
- Verified: FULLTEXT
- Notes: Key support for our statement that "the universe is a computation" does not by itself entail "the universe is run on someone else's computer".

### C-02-051
- Claim: The SEP entry judges that there is little positive evidence for ontic pancomputationalism, that supporters seem motivated by a desire for exact computational models, and that purely computational ontologies face the objection that they lack the causal and qualitative properties we observe; it adds that the classical version is in principle testable.
- Source: Piccinini2025computation
- Locator: §3.4 (final paragraphs)
- Evidence: "On the empirical front, there is little positive evidence to support ontic pancomputationalism. Supporters appear to be motivated by the desire for exact computational models of the world rather than empirical evidence that the models are correct." ... "purely computational ontologies face the objection that the computations they put at the fundamental physical level lack the causal and qualitative properties that we observe in the physical world" ... "Although there is no direct evidence for classical ontic pancomputationalism, in principle it is a testable hypothesis (Fredkin 1990)."
- Verified: FULLTEXT
- Notes: —

### C-02-052
- Claim: Floridi separates two questions: whether the universe can be adequately modelled digitally and computationally, and whether it is digital and computational in itself; he calls the first an open empirico-mathematical question and argues the second is ill-posed.
- Source: Floridi2009against
- Locator: §2.1 (accepted MS pp. 7–8)
- Evidence: "a) whether the physical universe might be adequately modelled digitally and computationally, independently of whether it is actually digital and computational in itself; and b) whether the ultimate nature of the physical universe might be actually digital and computational in itself [...] The first is an empirico-mathematical question that, so far, remains unsettled. [...] The second is a metaphysical question that, in the rest of the paper, I hope to show to be ill-posed"
- Verified: FULLTEXT
- Notes: Floridi also distinguishes "predicative" from "attributive" uses of "digital physics" (MS p. 12).

### C-02-053
- Claim: Floridi's overall thesis is that digital ontology should be abandoned in favour of informational structural realism, because digital and analogue are "modes of presentation" relative to a level of abstraction rather than features of reality in itself.
- Source: Floridi2009against
- Locator: Abstract
- Evidence: "The paper argues that digital ontology (the ultimate nature of reality is digital, and the universe is a computational system equivalent to a Turing Machine) should be carefully distinguished from informational ontology (the ultimate nature of reality is structural), in order to abandon the former and retain only the latter as a promising line of research. Digital vs. analogue is a Boolean dichotomy typical of our computational paradigm, but digital and analogue are only "modes of presentation" of Being"
- Verified: FULLTEXT
- Notes: Crossref lists online year 2008; volume 168 is dated 2009.

### C-02-054
- Claim: Floridi's argument has drawn a published reply by Sdrolia and Bishop in *Minds and Machines*.
- Source: Sdrolia2014rethinking
- Locator: bibliographic record (Crossref)
- Evidence: Title: "Rethinking Construction: On Luciano Floridi's 'Against Digital Ontology'", Minds and Machines 24(1):89–99.
- Verified: METADATA
- Notes: Content not read; cite only as evidence that the debate continued.

### C-02-055
- Claim: Szudzik gives a formal definition of a computable physical model (a recursive set of states with a total recursive function for each observable) and formulates the computable universe hypothesis in these terms; his examples include a model with non-discrete continuous motion.
- Source: Szudzik2012computable
- Locator: Abstract; §2 (Definition 2.1 and "Computable Universe Hypothesis")
- Evidence: "Definition 2.1. A computable physical model of a system is a recursive set S of states with a total recursive function φ for each observable quantity of the system." ... "Computable Universe Hypothesis. The universe has a recursive set of states U . For each observable quantity, there is a total recursive function φ." ... "several examples of computable physical models are given, including models which feature discrete motion, a model which features non-discrete continuous motion, and probabilistic models such as radioactive decay."
- Verified: FULLTEXT
- Notes: arXiv v6 read; published in Zenil (ed.), *A Computable Universe* (World Scientific, 2012), pp. 479–523. Szudzik: models of Zuse, Fredkin and Wolfram "are necessarily special sorts of computable physical models".

## I. Early "simulated world" proposals

### C-02-056
- Claim: In a 1992 essay Moravec argued that a future cyberspace would replay human history many times, so that "the very moment we are now experiencing may actually be (almost certainly is)" such a simulated mental event.
- Source: Moravec1992pigs
- Locator: final paragraph (author-hosted HTML at frc.ri.cmu.edu)
- Evidence: "If these minds spend only an infinitesimal fraction of their energy contemplating the human past, their sheer power should ensure that eventually our entire history is replayed many times in many places, and in many variations. The very moment we are now experiencing may actually be (almost certainly is) such a distributed mental event, and most likely is a complete fabrication that never happened physically."
- Verified: FULLTEXT
- Notes: Author-hosted text dated 1992; the original print venue was not verified, so cite as the author-hosted essay.

### C-02-057
- Claim: Bostrom's 2003 simulation-argument paper cites Moravec's *Mind Children* (in its discussion of the computational cost of simulating a human mind) and Lloyd's 2000 limits paper.
- Source: Bostrom2003are
- Locator: footnotes 5–6 (author preprint)
- Evidence: "5 S. Lloyd, "Ultimate physical limits to computation." Nature 406 (31 August): 1047‐1054 (2000). 6 H. Moravec, Mind Children, Harvard University Press (1989)."
- Verified: FULLTEXT
- Notes: Bostrom gives 1989 for *Mind Children*; the first edition is 1988 (Harvard University Press; OpenLibrary). Main treatment of Bostrom is in section 01.

### C-02-058
- Claim: Moravec's *Mind Children* (1988) and Tipler's *The Physics of Immortality* (1994) are earlier book-length discussions associated with simulated minds and worlds.
- Source: Moravec1988mind; Tipler1994physics
- Locator: bibliographic records (OpenLibrary); Tipler listed by Tegmark2008mathematical §VI A (see C-02-047)
- Evidence: OpenLibrary: "Mind children", Hans Moravec, Harvard University Press, 1988; "The Physics of Immortality", Frank J. Tipler, Doubleday, 1994.
- Verified: METADATA
- Notes: Neither book was read. The tex must not describe their content beyond Tegmark's listing of Tipler (C-02-047) and Bostrom's citation of Moravec (C-02-057).

### C-02-059
- Claim: Lloyd's popular book "Programming the Universe" (2006) presents the computational-universe view; cited for attribution only.
- Source: Lloyd2006programming
- Locator: Alfred A. Knopf, New York, 2006, ISBN 1400040922
- Evidence: Open Library record for ISBN 1400040922: "Programming the universe: from the big bang to quantum computers", 2006.
- Verified: METADATA
- Notes: Added at integration. No content claim rests on the book.
