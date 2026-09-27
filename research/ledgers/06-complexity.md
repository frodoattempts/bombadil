# Claim ledger: 06-complexity

Topic: arguments from computational complexity and computability for or against
the simulability of our universe.

Page locators refer to the PDF that was read. For arXiv sources the page is the
arXiv PDF page; for journal scans (Feynman, Lloyd 1996, Moore, Wolfram) the
printed journal page is given. All PDFs are saved under `/tmp/claude-0/papers/`.

---

## A. Feynman, Lloyd, and the extended Church-Turing thesis

### C-06-001
- Claim: Feynman restricted his question to *exact* simulation, in which the computer "will do exactly the same as nature", and set aside approximate numerical integration of differential equations.
- Source: Feynman1982simulating
- Locator: Sec. 1, p. 468
- Evidence: "There is, of course, a kind of approximate simulation in which you design numerical algorithms for differential equations ... That's an interesting subject, but is not what I want to talk about. I want to talk about the possibility that there is to be an exact simulation, that the computer will do exactly the same as nature."
- Verified: FULLTEXT
- Notes: Read from a scan of the IJTP article (mirror at s2.smu.edu). The printed journal pages are 467–488.

### C-06-002
- Claim: Feynman's efficiency requirement, that the number of computer elements scale only in proportion to the simulated space-time volume, was a rule he chose himself and not something he derived.
- Source: Feynman1982simulating
- Locator: Sec. 1, p. 469
- Evidence: "The rule of simulation that I would like to have is that the number of computer elements required to simulate a large physical system is only to be proportional to the space-time volume of the physical system. ... If doubling the volume of space and time means I'll need an exponentially larger computer, I consider that against the rules (I make up the rules, I'm allowed to do that)."
- Verified: FULLTEXT
- Notes: This matters for the paper. "Exponential cost" is a failure only relative to this chosen rule.

### C-06-003
- Claim: Feynman argued that a computer that stores or computes the general probability function of N variables would have to grow exponentially when N doubles, so by his rules it cannot simulate by calculating the probabilities.
- Source: Feynman1982simulating
- Locator: Sec. 3, p. 472
- Evidence: "if a description of an isolated part of nature with N variables requires a general function of N variables and if a computer stimulates this by actually computing or storing this function then doubling the size of nature (N → 2N) would require an exponentially explosive growth in the size of the simulating computer. It is therefore impossible, according to the rules stated, to simulate by calculating the probability."
- Verified: FULLTEXT
- Notes: "stimulates" is a typo in the original.

### C-06-004
- Claim: Feynman's negative answer to the question of whether a classical computer can simulate quantum systems probabilistically concerns *local* classical probabilistic machines. It rests on a Bell-type inequality.
- Source: Feynman1982simulating
- Locator: Sec. 5, p. 476 and p. 485
- Evidence: p. 476: "If you take the computer to be the classical kind I've described so far ... the answer is certainly, No! This is called the hidden-variable problem"; p. 485: "That's why quantum mechanics can't seem to be imitable by a local classical computer."
- Verified: FULLTEXT
- Notes: This is not a complexity-theoretic statement. A nonlocal classical computer can store the wave function at exponential cost.

### C-06-005
- Claim: Feynman conjectured that a locally coupled lattice of quantum spins could imitate any discrete quantum system with finitely many degrees of freedom. He was confident about bosons but left fermions open.
- Source: Feynman1982simulating
- Locator: Sec. 4, p. 476
- Evidence: "could we imitate every quantum mechanical system which is discrete and has a finite number of degrees of freedom? I know, almost certainly, that we could do that for any quantum mechanical system which involves Bose particles. I'm not sure whether Fermi particles could be described by such a system. So I leave that open."
- Verified: FULLTEXT
- Notes:

### C-06-006
- Claim: Lloyd (1996) showed that a quantum computer can efficiently simulate closed quantum systems with local Hamiltonians. The required memory and time are proportional to the simulated system's size and to the simulated time.
- Source: Lloyd1996universal
- Locator: Abstract, p. 1073; summary, p. 1076
- Evidence: p. 1073: "Feynman's 1982 conjecture, that quantum computers can be programmed to simulate any local quantum system, is shown to be correct."; p. 1076: "the quantum simulation takes resources of quantum computer time and memory space directly proportional to the time and space taken up by the system to be simulated."
- Verified: FULLTEXT
- Notes: Read from a scan hosted on an MIT course page. The result uses Trotter/Campbell-Baker-Hausdorff splitting to accuracy ε.

### C-06-007
- Claim: In Lloyd's scheme, continuous variables such as field values in a lattice gauge theory are discretized, with N qubits per local variable giving N bits of accuracy.
- Source: Lloyd1996universal
- Locator: p. 1076
- Evidence: "Although continuous variables complicate the computation, they can still be approximated discretely: N quantum bits are required to simulate a continuous local variable such as the position of a particle or the value of a field in a lattice gauge theory to N bits of accuracy."
- Verified: FULLTEXT
- Notes: The simulation of continuum physics is therefore approximate, with controllable accuracy.

### C-06-008
- Claim: Bravyi and Kitaev showed that local fermionic modes and qubits can simulate each other with at most logarithmic overhead per gate, and with constant overhead for nearest-neighbour fermionic gates on bounded-degree graphs. This settles the fermion question Feynman left open, at the level of polynomial equivalence.
- Source: Bravyi2002fermionic
- Locator: Abstract
- Evidence: "simulation of one fermionic gate takes O(m) qubit gates and vice versa. We show that using different encodings, the simulation cost can be reduced to O(log m) and a constant, respectively. Nearest-neighbors fermionic gates on a graph of bounded degree can be simulated at a constant cost."
- Verified: ABSTRACT
- Notes: "Settles Feynman's question" is our framing. Say "addresses" in the paper.

### C-06-009
- Claim: Jordan, Lee and Preskill gave a quantum algorithm for relativistic scattering probabilities in massive φ⁴ theory in four or fewer spacetime dimensions. Its run time is polynomial in the number of particles, their energy and the precision.
- Source: Jordan2012quantum
- Locator: Abstract
- Evidence: "We develop a quantum algorithm to compute relativistic scattering probabilities in a massive quantum field theory with quartic self-interactions (phi-fourth theory) in spacetime of four and fewer dimensions. Its run time is polynomial in the number of particles, their energy, and the desired precision, and applies at both weak and strong coupling."
- Verified: ABSTRACT
- Notes: This covers φ⁴ theory only, not gauge theories or gravity.

### C-06-010
- Claim: Bernstein and Vazirani gave the first formal evidence that quantum Turing machines violate the complexity-theoretic ("modern" or "extended") Church-Turing thesis: an oracle problem that a QTM solves in polynomial time but that needs superpolynomial time on a bounded-error probabilistic TM.
- Source: Bernstein1997quantum
- Locator: Abstract
- Evidence: "We give the first formal evidence that quantum Turing machines violate the modern (complexity theoretic) formulation of the Church--Turing thesis. We show the existence of a problem, relative to an oracle, that can be solved in polynomial time on a quantum Turing machine, but requires superpolynomial time on a bounded-error probabilistic Turing machine"
- Verified: ABSTRACT
- Notes: The separation is relative to an oracle.

### C-06-011
- Claim: Bernstein and Vazirani showed that BPP ⊆ BQP ⊆ P^#P. An unrelativized proof that quantum computers outperform classical probabilistic ones would therefore require a major breakthrough in complexity theory.
- Source: Bernstein1997quantum
- Locator: Abstract
- Evidence: "BPP ⊆ BQP ⊆ P^{#P}. Therefore, there is no possibility of giving a mathematical proof that quantum Turing machines are more powerful than classical probabilistic Turing machines (in the unrelativized setting) unless there is a major breakthrough in complexity theory."
- Verified: ABSTRACT
- Notes:

### C-06-012
- Claim: The extended Church-Turing thesis, in the form "any reasonable computational model can be simulated efficiently by a probabilistic Turing machine", is an empirical hypothesis whose truth depends on the laws of physics. Whether quantum computers falsify it is still debated.
- Source: Copeland2023churchturing
- Locator: Sec. 6.2
- Evidence: "[T]he extended Church-Turing thesis … asserts that any reasonable computational model can be simulated efficiently by the standard model of classical computation, namely, a probabilistic Turing machine." ... "both extended theses are empirical hypotheses. Moreover, there is ongoing debate as to whether quantum computers in fact falsify these theses."
- Verified: FULLTEXT
- Notes: Stanford Encyclopedia of Philosophy entry, substantive revision 18 Dec 2023, accessed 2026-09-27.

### C-06-013
- Claim: Arute et al. (2019) reported sampling from a 53-qubit random circuit in about 200 s. They estimated that a state-of-the-art classical supercomputer would take about 10,000 years for the equivalent task.
- Source: Arute2019quantum
- Locator: Abstract (Nature)
- Evidence: "Our Sycamore processor takes about 200 seconds to sample one instance of a quantum circuit a million times—our benchmarks currently indicate that the equivalent task for a state-of-the-art classical supercomputer would take approximately 10,000 years."
- Verified: ABSTRACT
- Notes: The 10,000-year figure is an estimate, not a measurement.

### C-06-014
- Claim: Pan, Chen and Zhang later produced one million samples for the 53-qubit, 20-cycle Sycamore circuit, at fidelity about 0.0037, in about 15 hours on 512 GPUs. This shows that the classical-hardness estimates behind specific advantage claims are provisional.
- Source: Pan2022solving
- Locator: Abstract
- Evidence: "For the Sycamore quantum supremacy circuit with 53 qubits and 20 cycles, we have generated one million uncorrelated bitstrings ... where the approximate state ψ̂ has fidelity F≈0.0037. The whole computation has cost about 15 hours on a computational cluster with 512 GPUs."
- Verified: ABSTRACT
- Notes: "Provisional" is our inference. This does not bear on the asymptotic question BPP vs BQP.

## B. The sign problem

### C-06-015
- Claim: Troyer and Wiese define a "solution of the sign problem" as a polynomial-complexity algorithm for a thermal average, applicable where the related bosonic problem (absolute-value weights) is itself polynomial. Changing representation to non-negative weights does not count as a solution if the cost stays exponential.
- Source: Troyer2005computational
- Locator: arXiv p. 3 (definitions after Eq. 7)
- Evidence: "we define a solution of the sign problem as an algorithm of polynomial complexity to evaluate the thermal average ⟨A⟩." ... "changing the representation so that the sum in Eq. (5) contains only positive terms p(c) ≥ 0 is not sufficient to solve the sign problem if the scaling remains exponential"
- Verified: FULLTEXT
- Notes: Published as PRL 94, 170201 (2005). The arXiv v1 was read.

### C-06-016
- Claim: Troyer and Wiese prove NP-hardness by mapping the NP-complete ground-state decision problem for a 3D ±J Ising spin glass to a quantum model with a sign problem, H = −Σ J_jk σ^x_j σ^x_k. Its related bosonic model, the ferromagnet, is efficiently simulable by cluster algorithms.
- Source: Troyer2005computational
- Locator: arXiv pp. 3–4, Eqs. (10)–(11)
- Evidence: "The specific NP-complete problem we consider [7] is to determine whether a state with energy less than or equal to a bound E0 exists for a classical three-dimensional Ising spin glass" ... "The related bosonic model is the ferromagnet with all couplings Jjk ≥ 0 and efficient cluster algorithms with polynomial time complexity are known for this model"
- Verified: FULLTEXT
- Notes: The reduction needs inverse temperature βJ ≥ N ln 2 + ln(12N), which scales with system size.

### C-06-017
- Claim: What Troyer and Wiese exclude, assuming standard conjectures, is a *generic* polynomial-time solution of the sign problem. Specific solutions for restricted classes of models, such as meron-cluster algorithms, are not excluded. Strictly, the relevant containment is NP ⊆ BPP rather than P = NP.
- Source: Troyer2005computational
- Locator: arXiv p. 4 (Conclusions; footnote [9])
- Evidence: "This does not exclude that a specific sign problem can be solved for a restricted subclass of quantum systems. This was indeed possible using the meron-cluster algorithm [11] for some particular lattice models." Footnote 9: "Strictly speaking a polynomial time Monte Carlo solution is thus not in the class P but in the complexity class BPP"
- Verified: FULLTEXT
- Notes: The result is worst-case hardness.

### C-06-018
- Claim: Troyer and Wiese note that classical Monte Carlo for the hard spin-glass instance has exponentially large autocorrelation times. They also judge that quantum simulators are most likely not a generic solution to the sign problem either.
- Source: Troyer2005computational
- Locator: arXiv pp. 3–4
- Evidence: "The autocorrelation times and hence the time complexity of this Monte Carlo approach are exponentially large τ ∝ exp(aN), as expected for this NP-complete problem." ... "even these quantum simulators are most likely not a generic solution to the sign problem since there exist quantum systems with exponentially diverging time scales"
- Verified: FULLTEXT
- Notes: This supports our point that the hard instances are hard equilibrium tasks, not dynamics that nature carries out quickly.

### C-06-019
- Claim: Aaronson reports that physical relaxation processes proposed as NP-solvers, such as soap-film Steiner trees, spin glasses and protein folding, are subject to local optima and long relaxation times. In his own soap-bubble experiments the optimal Steiner tree was often not found.
- Source: Aaronson2005np
- Locator: arXiv pp. 3–4 (Sec. 2)
- Evidence: "with 3 or 4 pegs, the optimum tree usually is found. However, by no means is it always found, especially with more pegs." ... "There are other proposed methods for solving NP-complete problems that involve relaxation to a minimum-energy state, such as spin glasses and protein folding. All of these methods are subject to the same pitfalls of local optima and potentially long relaxation times."
- Verified: FULLTEXT
- Notes: The experiment was informal ("'experimental' results" in his abstract). Cite it only for the qualitative point.

### C-06-020
- Claim: Ringel and Kovrizhin show that, for bosonic systems, a nonvanishing quantized thermal Hall conductance with a gapped bulk (as in most fractional quantum Hall phases) obstructs *local* sign-free QMC. Here "local" means that the weights involve degrees of freedom obtained from the physical ones by finite-depth local quantum circuits.
- Source: Ringel2017quantized
- Locator: Introduction; Results (first paragraph)
- Evidence: "we show that no local sign-free QMC formulation is possible for phases that have a nonvanishing quantized thermal Hall conductance and a gapped bulk." ... "the degrees of freedom σ, that enter the Boltzmann weights must be expressed as local combinations of the physical ones or, more precisely, that σ are given by finite depth local quantum circuits acting on the physical degrees of freedom."
- Verified: FULLTEXT
- Notes: Read from the published Science Advances full text (Europe PMC XML, open access CC BY-NC).

### C-06-021
- Claim: Ringel and Kovrizhin explicitly do not address nonlocal QMC approaches such as determinant QMC or cluster algorithms.
- Source: Ringel2017quantized
- Locator: Introduction
- Evidence: "For the sake of clarity in this work, we do not address the possibility of nonlocal approaches to QMC, such as determinant QMC or cluster algorithms (8–10)."
- Verified: FULLTEXT
- Notes: This is a central caveat that the press omitted.

### C-06-022
- Claim: Ringel and Kovrizhin state that establishing an obstruction to classical simulation in general is "a rather ill-defined task". They therefore target QMC specifically. For the chiral Kagome antiferromagnet their argument needs additional microscopic assumptions.
- Source: Ringel2017quantized
- Locator: Introduction; Discussion
- Evidence: "Establishing an obstruction to a classical simulation is a rather ill-defined task. A related, yet more concrete, goal is to find an obstruction to an efficient quantum Monte Carlo (QMC)" ... "The same argument extends to frustrated quantum magnets that support a chiral spin liquid phase, although here, some additional microscopic assumptions are currently required."
- Verified: FULLTEXT
- Notes:

### C-06-023
- Claim: For non-symmetric transfer matrices, Ringel and Kovrizhin concede that they cannot rule out that a needed similarity transformation is nonlocal, which would void the argument.
- Source: Ringel2017quantized
- Locator: Materials and Methods (last paragraph)
- Evidence: "However, we cannot refute the possibility that ν̂ is some nonlocal transformation that can, in principle, transform a Schrodinger cat state into a physical state, rendering the previous arguments void."
- Verified: FULLTEXT
- Notes:

### C-06-024
- Claim: Ringel and Kovrizhin's paper does not mention the simulation hypothesis or the universe being a simulation.
- Source: Ringel2017quantized
- Locator: whole text
- Evidence: A search of the published full text (Europe PMC XML) for "universe", "simulation hypothesis" and "Matrix" (other than "transfer matrix", "S-matrix") returned no such mentions. Aaronson likewise states that the original paper does not make this claim: "as the popular articles claim (and as the original paper does not)".
- Verified: FULLTEXT
- Notes: A negative claim, backed by a text search of the whole paper and by Aaronson2017because.

### C-06-025
- Claim: Hastings (2016) established an intrinsic sign problem, one not removable by quantum circuits, for commuting Hamiltonians in the double-semion phase, under a technical assumption (TQO-2).
- Source: Hastings2016how
- Locator: Abstract
- Evidence: "We show a weaker version of this, showing that the sign problem is intrinsic for commuting Hamiltonians in the same phase as the double semion model under the technical assumption that TQO-2 holds"
- Verified: ABSTRACT
- Notes: Ringel and Kovrizhin call this the first rigorous establishment of a sign problem.

### C-06-026
- Claim: Follow-up work gave a criterion for intrinsic sign problems in bosonic (2+1)D topological phases based on anyon statistics. It also established an intrinsic sign problem in a broad class of chiral topological phases, excluding stoquastic Hamiltonians for bosons and sign-free determinantal QMC for fermions within that class.
- Source: Smith2020intrinsic; Golan2020intrinsic
- Locator: Abstracts
- Evidence: Smith et al.: "if the exchange statistics of the anyonic excitations do not form complete sets of roots of unity, then the model has an intrinsic sign problem". Golan et al.: "we establish the existence of an intrinsic sign problem in a broad class of gapped, chiral, topological phases of matter. Within this class, we exclude the possibility of stoquastic Hamiltonians for bosons (or 'qudits'), and of sign-problem-free determinantal Monte Carlo algorithms for fermions."
- Verified: ABSTRACT
- Notes: Still specific to QMC-type (stoquastic / determinantal) methods.

### C-06-027
- Claim: Marvian, Lidar and Hen proved that finding a transformation that cures a non-stoquastic Hamiltonian is NP-complete when the transformations are restricted to single-qubit Clifford elements or single-qubit orthogonal matrices.
- Source: Marvian2019on
- Locator: Abstract
- Evidence: "We prove that if such transformations are limited to single-qubit Clifford group elements or general single-qubit orthogonal matrices, finding the curing transformation is NP-complete."
- Verified: ABSTRACT
- Notes: Published title: "On the computational complexity of curing non-stoquastic Hamiltonians".

### C-06-028
- Claim: PBS NOVA Next reported the Ringel-Kovrizhin result under the headline "Physicists Confirm That We're Not Living In a Computer Simulation", stating that it is "impossible to model the physics of our universe on even the biggest computer".
- Source: Eck2017physicists
- Locator: web article, 3 Oct 2017
- Evidence: "Scientists have discovered that it's impossible to model the physics of our universe on even the biggest computer. What that means is that we're probably not living in a computer simulation." ... "Therefore, according to Ringel and Kovrizhin, classical computers most certainly aren't controlling our universe."
- Verified: FULLTEXT
- Notes: Cited ONLY as evidence of how the result was reported. The byline (Allison Eck) and date come from the page metadata.

### C-06-029
- Claim: UPI reported "We're not living in a simulation, scientists confirm". It quoted sentences as written "in a paper" that do not appear in the published article.
- Source: UPI2017were
- Locator: web article, 4 Oct 2017
- Evidence: UPI: "'Even just to store the information about a few hundred electrons on a computer one would require a memory built from more atoms than there are in the universe,' researchers wrote in a paper on their efforts, published this week in the journal Science Advances." A search of the Science Advances full text and of arXiv:1704.03880 for "few hundred electrons", "atoms than there are" and "double the number of processors" returned no matches.
- Verified: FULLTEXT
- Notes: The quotation probably comes from a university press release (phys.org, "Gravitational twists help theoretical physicists shed light on quantum complexity"), which we could not access because the domain is blocked. Use this only for how the result was reported.

### C-06-030
- Claim: Aaronson argued that getting from Ringel-Kovrizhin to "the universe is not a simulation" faces four independent obstacles. (i) Only local transformations within QMC are considered, not all polynomial-time algorithms. (ii) BPP ≠ BQP is unproven. (iii) A simulator could use a quantum computer. (iv) Exponential classical slowdown is invisible to the simulated beings.
- Source: Aaronson2017because
- Locator: blog post, 3 Oct 2017
- Evidence: "within that framework, only 'local' transformations of the physical degrees of freedom are considered, not nonlocal ones that could still be accessible to polynomial-time algorithms." ... "until someone proves P≠PSPACE, there's no hope for an unconditional proof that quantum computers can't be efficiently simulated by classical ones." ... "why not just imagine that the universe is being simulated on a quantum computer?" ... "why couldn't God, using Her classical computer, spend a trillion years to simulate one second as subjectively perceived by us?"
- Verified: FULLTEXT
- Notes: A blog post, cited as a critique by a quantum-complexity theorist (the argument itself is the object of study).

### C-06-031
- Claim: Bostrom's FAQ answers the media reading of Ringel-Kovrizhin by noting that "the most obvious flaw in that interpretation is that simulators could use quantum computers", and that a simulator need not compute all the physics faithfully.
- Source: Bostrom2025simulation
- Locator: FAQ Q12
- Evidence: "Some media reported this as 'scientists have found proof that we are not living in a simulation!'. The most obvious flaw in that interpretation is that simulators could use quantum computers. More generally ... another way would be to run a simulation that 'cheats' and that produces the appearances in a more intelligently creative or klugey manner"
- Verified: FULLTEXT
- Notes: The FAQ is labelled "(2025) Nick Bostrom version 2.0" (accessed 2026-09-27). Edge2026commentary cites an FAQ dated 2008 for a sentence that appears in this 2025 version.

## C. Undecidability in physics

### C-06-032
- Claim: Cubitt, Perez-Garcia and Wolf construct translationally invariant, nearest-neighbour Hamiltonians on a 2D square lattice of d-level systems, with interaction strength at most 1. Such a Hamiltonian is gapped with gap ≥ 1 if a universal Turing machine halts on input n, and gapless otherwise. Deciding the gap is therefore undecidable.
- Source: Cubitt2022undecidability
- Locator: Theorem 3, arXiv v5 p. 6
- Evidence: "(ii). If UTM halts on input n, then the associated family of Hamiltonians {H^Λ(L)(n)} is gapped in the strong sense of Definition 1 and, moreover, the gap γ ≥ 1. (iii). If UTM does not halt on input n, then the associated family ... is gapless in the strong sense of Definition 2."
- Verified: FULLTEXT
- Notes: Full version Forum Math. Pi 10, e14 (2022), arXiv:1502.04573. Short version Nature 528, 207 (2015), arXiv:1502.04135.

### C-06-033
- Claim: As a corollary, for any consistent formal system with a recursive set of axioms, there is a Hamiltonian of this kind for which neither the presence nor the absence of a gap is provable.
- Source: Cubitt2022undecidability
- Locator: Corollary 4, arXiv v5 p. 7
- Evidence: "For any consistent formal system with a recursive set of axioms, there exists a translationally invariant nearest-neighbour Hamiltonian on a 2D lattice with local dimension d and algebraic entries for which neither the presence nor the absence of a spectral gap is provable from the axioms."
- Verified: FULLTEXT
- Notes:

### C-06-034
- Claim: The undecidability concerns the thermodynamic limit. Cubitt et al. state that algorithmic undecidability always concerns infinite families of systems, and that their models can switch from gapless-looking to gapped at an uncomputable threshold lattice size.
- Source: Cubitt2015undecidability
- Locator: Discussion, arXiv:1502.04135v3 p. 5
- Evidence: "Whilst algorithmic undecidability always concerns infinite families of systems, the axiomatic interpretation of the result also allows us to talk about individual systems" ... "Not only can the lattice size at which the system switches from gapless to gapped be arbitrarily large, the threshold at which this transition occurs is uncomputable."
- Verified: FULLTEXT
- Notes:

### C-06-035
- Claim: Perales-Eceiza et al. stress that undecidability is a feature of the mathematical model and not of the physical system. Any finite problem is decidable, so an undecidable problem must "conceal an infinite somewhere".
- Source: PeralesEceiza2025undecidability
- Locator: Sec. 1, arXiv v2 pp. 5–6
- Evidence: "undecidability is not a feature of the physical system; it is a feature of the mathematical model we use to describe that physical system." ... "Since any finite problem is decidable simply by enumerating the solutions, an undecidable problem must necessarily conceal an infinite somewhere: infinitely many instances, infinitely many particles, infinite precision."
- Verified: FULLTEXT
- Notes: Published in Phys. Rep. 1138, 1–29 (2025). The co-authors include Cubitt, Pérez-García and Wolf.

### C-06-036
- Claim: The review also notes that undecidability in the infinite limit can show up at finite sizes: as completeness of the finite problem for some complexity class, or as abrupt size-dependent changes at uncomputably large sizes.
- Source: PeralesEceiza2025undecidability
- Locator: Sec. 6.2, arXiv v2 pp. 52–53
- Evidence: "1. The associated problem for finite size or finite precision becomes complete for some computational complexity class." ... "2. ... there may be a finite but uncomputably large size at which the properties of the system change abruptly and dramatically."
- Verified: FULLTEXT
- Notes:

### C-06-037
- Claim: Moore showed that a particle with three degrees of freedom (for example, a particle in a 3D potential or billiard) can be equivalent to a Turing machine. For such a system, virtually any question about long-term dynamics is undecidable even when the initial conditions are known exactly.
- Source: Moore1990unpredictability
- Locator: Abstract, p. 2354
- Evidence: "We show that motion with as few as three degrees of freedom (for instance, a particle moving in a three-dimensional potential) can be equivalent to a Turing machine ... Even if the initial conditions are known exactly, virtually any question about their long-term dynamics is undecidable."
- Verified: FULLTEXT
- Notes: Read from a scan of the PRL.

### C-06-038
- Claim: In the same systems, Moore notes that finite-time quantities remain computable and that the best one can do is simulate. Undecidability of long-time properties coexists with step-by-step simulability.
- Source: Moore1990unpredictability
- Locator: p. 2357
- Evidence: "The best one can do is to simulate the system and see what happens." ... "we can calculate the average amount of shifting S_t for any finite t, but its long-time behavior is uncomputable."
- Verified: FULLTEXT
- Notes: This is key support for the "property vs dynamics" distinction.

### C-06-039
- Claim: Wolfram (1985) argued that the behaviour of a physical system can always be calculated by explicitly simulating each step. Computational irreducibility means no shortcut exists, and questions about infinite-time limits can be formally undecidable. For a finite cellular automaton the fate of a pattern is decidable, but PSPACE-complete if the automaton is universal.
- Source: Wolfram1985undecidability
- Locator: pp. 735–736
- Evidence: "The behavior of a physical system may always be calculated by simulating explicitly each step in its evolution." ... "The infinite-time limiting behavior is formally undecidable" ... "The fate of a pattern in a CA with a finite total number of sites N can always be determined in at most k^N steps. However, if the CA is a universal computer, then the problem is PSPACE-complete"
- Verified: FULLTEXT
- Notes: Read from the PDF hosted by Wolfram.

### C-06-040
- Claim: Pour-El and Richards found non-computable (weak) solutions of a 3D wave equation with computable initial data.
- Source: PeralesEceiza2025undecidability (secondary); PourEl1981wave
- Locator: review Sec. 4, arXiv v2 p. 26
- Evidence: "Pour-El and Richards (1981) [104] found non-computable weak solutions for a particular three-dimensional wave equation with computable initial conditions."
- Verified: FULLTEXT
- Notes: FULLTEXT of the review only. The original paper was not accessible (Elsevier and CORE both refused), so PourEl1981wave is METADATA-level. Attribute the characterization to the review.

### C-06-041
- Claim: Weihrauch and Zhong proved, in type-2 computability, that the wave propagator is computable on continuously differentiable waves (losing one derivative) and on Sobolev spaces. They argue that the Pour-El-Richards result probably does not help to build a wave computer that beats the Turing machine.
- Source: Weihrauch2002is
- Locator: Abstract
- Evidence: "we prove that the wave propagator is computable on continuously differentiable waves, where one derivative is lost, and on waves from Sobolev spaces. Finally, we explain why the Pour-El-Richards result probably does not help to design a wave computer which beats the Turing machine."
- Verified: ABSTRACT
- Notes: Computability depends on the chosen norm/topology.

### C-06-042
- Claim: Wolpert proves that any "inference device" (observation, prediction or recollection apparatus) inside a universe fails to infer some binary function. He states that this holds even for super-Turing computers and independently of chaos, light-speed or quantum limits. He also proves that no two distinguishable devices can weakly infer each other.
- Source: Wolpert2008physical
- Locator: Prop. 1(ii) and discussion, arXiv p. 12; Theorem 1, p. 13
- Evidence: "ii) For any device C, there is a binary-valued function that C does not infer." ... "This is all true even if the computer has super-Turing capability, and does not derive from chaotic dynamics, physical limitations like the speed of light, or quantum mechanical limitations." ... "Theorem 1: No two distinguishable devices can weakly infer each other."
- Verified: FULLTEXT
- Notes: Physica D 237, 1257 (2008). These are limits on devices embedded in the universe they infer. They are not limits on the executability of dynamics by an external machine (our reading; state it as such).

## D. Faizal, Krauss, Shabir and Marino (2025) and responses

### C-06-043
- Claim: Faizal et al. model a candidate quantum-gravity theory as a computational formal system F_QG with a recursively enumerable axiom set, and require it to be effectively axiomatizable, arithmetically expressive, consistent and "empirically complete".
- Source: Faizal2025consequences
- Locator: arXiv v1 p. 3
- Evidence: "it is assumed a candidate theory of quantum gravity is encoded as a computational formal system F_QG = {L_QG, Σ_QG, R_alg}. ... Σ_QG = {A1, A2, ...} is a finite (or at least recursively-enumerable) set" ... "Any viable F_QG must meet four intertwined criteria: Effective axiomatizability; ... Arithmetic expressiveness; ... Internal consistency; ... Empirical completeness"
- Verified: FULLTEXT
- Notes: On the same page the axiom set is described both as "finite (or at least recursively-enumerable)" and as "The number of axioms in Σ_QG are finite". Published version: JHAP 5(2), 10–21 (2025). Only arXiv v1 was read; we did not compare it with the JHAP version (the site was unreachable).

### C-06-044
- Claim: They define truth as satisfaction in the standard model of arithmetic, invoke Gödel's first theorem to get Th(F_QG) ⊊ True(F_QG), and then assert, without derivation, that the resulting Gödel sentences correspond to empirically meaningful facts such as specific black-hole microstates.
- Source: Faizal2025consequences
- Locator: arXiv v1 p. 4
- Evidence: "the semantically true sentences are True(F_QG) = {φ ∈ L_QG | N ⊨ φ}. Thus, Gödel's first incompleteness theorem asserts the strict containment Th(F_QG) ⊊ True(F_QG) ... Physically these Gödel sentences correspond to empirically meaningful facts—e.g., specific black-hole microstates—that elude any finite, rule-based derivation."
- Verified: FULLTEXT
- Notes: "Without derivation" is our assessment. The text gives no argument for the physical correspondence.

### C-06-045
- Claim: They adjoin an external, non-recursively-enumerable truth predicate T(x) (the "Meta-Theory of Everything", M_ToE), which they claim is "actualized in nature". They cite the appearance of undecidable phenomena in physics as empirical backing, and the Lucas-Penrose argument as showing that non-algorithmic understanding can access truths beyond formal proof.
- Source: Faizal2025consequences
- Locator: arXiv v1 pp. 4–6
- Evidence: "Σ_T is an external, non-recursively-enumerable set of axioms about T" ... "the appearance of undecidable phenomena in physics already offers empirical backing for M_ToE" ... "this truth predicate T(x) would also be actualized in nature" ... "the Lucas–Penrose argument shows that non-algorithmic understanding can access truths beyond formal proofs"
- Verified: FULLTEXT
- Notes: The examples cited as backing include the spectral gap (Cubitt et al.), thermalization (Shiraishi & Matsumoto) and RG flows (Watson et al.).

### C-06-046
- Claim: From this they conclude that any finite algorithm can at best emulate F_QG, that no simulation could reproduce the full structure of physics, and that the simulation hypothesis is "logically impossible rather than merely implausible". They also frame the target as reality that "cannot be instantiated on a Turing-equivalent device".
- Source: Faizal2025consequences
- Locator: Abstract p. 1; arXiv v1 p. 8
- Evidence: Abstract: "Because any putative simulation of the universe would itself be algorithmic, this framework also implies that the universe cannot be a simulation." p. 8: "any finite algorithm can at best emulate F_QG while systematically omitting the meta-theoretic truths enforced by T(x). ... genuine physical reality embeds non-computational content that cannot be instantiated on a Turing-equivalent device. Since it is impossible to simulate a complete and consistent universe, our universe is definitely not a simulation. As the universe is produced by M_ToE, the simulation hypothesis is logically impossible rather than merely implausible."
- Verified: FULLTEXT
- Notes: The argument excludes at most Turing-equivalent simulators. A hypercomputational host is not addressed.

### C-06-047
- Claim: Faizal et al. attribute to the simulation proposals of Bostrom, Chalmers and Deutsch the assumption "that every physical truth is reducible to the output of a finite algorithm".
- Source: Faizal2025consequences
- Locator: arXiv v1 p. 8
- Evidence: "These proposals assume that every physical truth is reducible to the output of a finite algorithm executed on a sufficiently powerful substrate. Yet this assumption tacitly identifies the full physical theory with its computable slice F_QG."
- Verified: FULLTEXT
- Notes: Bostrom (2003) does not require simulating all physics (see C-06-056). The attribution is contestable.

### C-06-048
- Claim: Redden's comment argues that Faizal et al. conflate provability within a formal theory with execution by an algorithm. Using Conway's Game of Life, which is Turing-complete and has undecidable long-term questions yet evolves by a finite rule, he argues that undecidability constrains provability, not execution.
- Source: Redden2025provability
- Locator: Abstract; Sec. 2, arXiv p. 2
- Evidence: "this reasoning conflates what can be proven within a formal theory with what can be executed by an algorithmic process." ... "These undecidable truths do not prevent the system from evolving; they merely restrict what an observer can predict or prove about its evolution."
- Verified: FULLTEXT
- Notes: arXiv:2512.11807 (submitted 14 Nov 2025). A single-author preprint by a non-specialist. The acknowledgements disclose LLM assistance with formatting and wording. Not peer reviewed as far as we know.

### C-06-049
- Claim: Redden argues that inferring non-simulability would require showing that physical dynamics must resolve undecidable problems to advance, i.e. hypercomputation in nature. No such mechanism has been shown to be physically realizable.
- Source: Redden2025provability
- Locator: Sec. 3, arXiv p. 2
- Evidence: "the dynamics of the universe must depend on the resolution of an undecidable problem in order to advance from one state to another. This would entail the existence of hypercomputation in nature" ... "Although several theoretical constructs have been proposed as candidates for hypercomputational systems, none have been shown to be physically realizable"
- Verified: FULLTEXT
- Notes: The comment also says hypercomputers are unrealizable "due to the Church-Turing thesis". That wording conflates the mathematical thesis with a physical one (cf. C-06-052), so do not reproduce it.

### C-06-050
- Claim: A "Discussion" paper on the Faizal et al. argument and a reply by Faizal, Krauss, Shabir and Marino appeared in JHAP in 2026. In the reply the authors say that nature itself "instantiates" non-algorithmic truths. They argue that objections based on the possible inconsistency of human reasoning (as against Lucas-Penrose) do not apply.
- Source: Faizal2026reply
- Locator: Abstract (INSPIRE record 3145749)
- Evidence: "we argue that Gödelian non-algorithmic truths are likewise objectively actualized in physical reality. Although the Lucas-Penrose argument is superficially similar, it concerns the nature of human consciousness, whereas our claim is fundamentally different in scope. ... objections based on the possible inconsistency of human reasoning are not applicable here"
- Verified: ABSTRACT
- Notes: The Discussion paper itself (jhap.du.ac.ir article_2003) could not be reached, and its author is unverified. The DOI metadata registered for 10.22128/jhap.2026.3205.1181 carries the title of the Discussion paper, while INSPIRE gives "Reply to 'Discussion ...'", JHAP 6(2) 119–124. We use INSPIRE's title.

### C-06-051
- Claim: The UBC Okanagan press release was reposted by ScienceDaily under the headline "Physicists prove the Universe isn't a simulation after all". It described the result as showing the idea "is mathematically impossible" and as possibly "the final, definitive answer".
- Source: UBCO2025physicists
- Locator: ScienceDaily, 10 Nov 2025 (source: University of British Columbia Okanagan campus)
- Evidence: "new research from UBC Okanagan suggests that not only is this concept implausible -- it is mathematically impossible." ... "delivering what may be the final, definitive answer to one of science's most intriguing questions." Faizal: "Any simulation is inherently algorithmic -- it must follow programmed rules. But since the fundamental level of reality is based on non-algorithmic understanding, the universe cannot be, and could never be, a simulation."
- Verified: FULLTEXT
- Notes: Cite only as evidence of how the result was reported.

## E. Physical Church-Turing thesis and hypercomputation

### C-06-052
- Claim: Copeland distinguishes the Church-Turing thesis, which concerns what a human computer can do by rote, from "Thesis M" and physical versions (Deutsch 1985; Wolfram 1985). He regards the physical versions as distinct, empirical claims that depend on the laws of physics.
- Source: Copeland2023churchturing
- Locator: Secs. 5.1, 6.3, 6.4.1
- Evidence: "the Church-Turing thesis is a thesis about the extent of effective methods ... the thesis concerns what a human being can achieve when calculating by rote" ... "the Simulation thesis is, like the Extended Church-Turing thesis, an empirical thesis ... The truth of the 'actual physical systems' version of the Simulation thesis depends on the laws of physics." ... "these physical theses are very distant from Turing's thesis and Church's thesis."
- Verified: FULLTEXT
- Notes:

### C-06-053
- Claim: Copeland reports Gandy's observation that Thesis M fails for some Newtonian machines (unbounded speeds, rigid rods), and Deutsch's argument that a universal Turing machine cannot perfectly simulate continuous classical dynamics.
- Source: Copeland2023churchturing
- Locator: Secs. 5.1, 6.4.1
- Evidence: "He pointed out that Thesis M is in fact false in the case of some 'machines obeying Newtonian mechanics', where 'there may be rigid rods of arbitrary lengths and messengers travelling with arbitrary large velocities'" ... "Deutsch argued that a universal Turing machine 'cannot perfectly simulate any classical dynamical system', since '[o]wing to the continuity of classical dynamics, the possible states of a classical system necessarily form a continuum'"
- Verified: FULLTEXT
- Notes: Gandy 1980 and Deutsch 1985 are reported through the SEP. We did not read them directly.

### C-06-054
- Claim: Aaronson argues that Planck-scale physics and the holographic entropy bound appear to rule out Zeno-type and Malament-Hogarth hypercomputers and unlimited-precision analog computation. He proposes that the "NP Hardness Assumption" might be considered a physical principle.
- Source: Aaronson2005np
- Locator: arXiv pp. 12, 18 (Secs. 6, 10)
- Evidence: "our current understanding seems to rule out, not only the Malament-Hogarth proposal, but all similar proposals for solving the halting problem in finite time." ... "if the nth step of a hypercomputation took 2^−n seconds, then it would take fewer than 150 steps to reach the Planck time." ... "The problem, of course, is that unlimited-precision real numbers would violate the holographic entropy bound." ... "should the 'NP Hardness Assumption'—loosely speaking, that NP-complete problems are intractable in the physical world—eventually be seen as a principle of physics?"
- Verified: FULLTEXT
- Notes: Published as the SIGACT News Complexity Theory Column 36(1), 30–52 (2005).

## F. Resource arguments and the host's physics

### C-06-055
- Claim: Bostrom estimated about 10^33–10^36 operations for a realistic simulation of human mental history, and about 10^42 operations per second for a planetary-mass computer using known nanotechnological designs.
- Source: Bostrom2003are
- Locator: Sec. III, p. 5 of the author's PDF
- Evidence: "we can use ~10^33 - 10^36 operations as a rough estimate" ... "a rough approximation of the computational power of a planetary-mass computer is 10^42 operations per second, and that assumes only already known nanotechnological designs"
- Verified: FULLTEXT
- Notes: Cross-reference to Section 01. The author's PDF (simulation-argument.com) was read. The estimates assume the physics of our universe.

### C-06-056
- Claim: Bostrom states that simulating the entire universe down to the quantum level "is obviously infeasible, unless radically new physics is discovered". He holds that a simulation need only include what is needed for simulated humans not to notice irregularities.
- Source: Bostrom2003are
- Locator: Sec. III, p. 5 of the author's PDF
- Evidence: "Simulating the entire universe down to the quantum level is obviously infeasible, unless radically new physics is discovered. But in order to get a realistic simulation of human experience, much less is needed – only whatever is required to ensure that the simulated humans ... don't notice any irregularities."
- Verified: FULLTEXT
- Notes:

### C-06-057
- Claim: Lloyd computes that the observable universe can have performed at most ~10^120 elementary operations on ~10^90 bits (~10^120 bits if gravitational degrees of freedom are included). He reads these as upper bounds on computation by matter in the universe and as lower bounds on the resources of a quantum computer that directly simulates the universe.
- Source: Lloyd2002computational
- Locator: Abstract p. 1; p. 2
- Evidence: "The universe can have performed no more than 10^120 ops on 10^90 bits." ... "the total number of bits (≈ 10^90 in matter, ≈ 10^120 if gravitation is taken into account)" ... "2. They give lower bounds to the number of ops and bits required to simulate the entire universe on a quantum computer."
- Verified: FULLTEXT
- Notes: Cross-reference to Section 02. Published as PRL 88, 237901 (2002). arXiv v1 was read.

### C-06-058
- Claim: Lloyd considered quantum computers' efficient simulation of local, finite theories to be "a strong indication" that quantum gravity, whatever its final form, is efficiently simulable on a quantum computer.
- Source: Lloyd2002computational
- Locator: arXiv p. 14
- Evidence: "the fact that quantum computers can efficiently simulate any theory that is locally finite and that can be described by local strictly positive transformations is a strong indication that whatever the eventual theory of quantum gravity, it is efficiently simulatable on a quantum computer."
- Verified: FULLTEXT
- Notes: This is an expectation, not a theorem. It is directly opposed to Faizal et al.'s premise.

### C-06-059
- Claim: Vazza concludes that the energy and power needed to simulate our Universe, or even a low-resolution Earth, are incompatible with physics for a simulator in a universe sharing our properties. He adds that only universes with very different physical properties could produce ours as a simulation.
- Source: Vazza2025astrophysical
- Locator: Abstract, arXiv p. 1; Conclusions, p. 15
- Evidence: "Only universes with very different physical properties can produce some version of this Universe as a simulation. On the other hand, our results show that it is just impossible that this Universe is simulated by a universe sharing the same properties" ... "the question whether universes with entirely different sets of physical laws or dimensionalities could produce our Universe as a simulation, seems to be be entirely outside of what is scientifically testable, even in theory."
- Verified: FULLTEXT
- Notes: Cross-reference to Section 02. Front. Phys. 13:1561873 (2025).

### C-06-060
- Claim: Edge and Brown's commentary states that Vazza's conclusions hold "if the simulator's universe is governed by physics like our own". It argues that such critiques target a fully comprehensive simulation that Bostrom's hypothesis does not require.
- Source: Edge2026commentary
- Locator: Secs. 1 and 3
- Evidence: "Vazza [1] mathematically demonstrates that such calculations are not achievable given the computational power required if the simulator's universe is governed by physics like our own." ... "Vazza's strongest conclusions follow for a shared-world, planet-level (and experiment-consistent) simulation under physics like our own"
- Verified: FULLTEXT
- Notes: Front. Phys. 14:1808725 (2026). Open-access HTML was read.

### C-06-061
- Claim: Bostrom's FAQ states that a fully comprehensive simulation is "not inconceivable, since the physics in the basement universe might allow for vastly more powerful computers than does the physics in our observed universe".
- Source: Bostrom2025simulation
- Locator: FAQ Q6
- Evidence: "even if fully comprehensive detailed simulations are possible—which is not inconceivable, since the physics in the basement universe might allow for vastly more powerful computers than does the physics in our observed universe—it would still be unlikely that we are in a fully comprehensive simulation"
- Verified: FULLTEXT
- Notes: A web FAQ (version 2.0, 2025), cited as the author's own statement of the argument.

### C-06-062
- Claim: Neukart et al. argue that a computer governed by the same physical laws as the universe it simulates would need at least as many particles as that universe. They acknowledge that an external programmer not limited by the simulation's physical laws escapes this constraint.
- Source: Neukart2022do
- Locator: Abstract p. 1; p. 14
- Evidence: Abstract: "in a simulation in which the computer simulating a universe is governed by the same physical laws as the simulation and is smaller than the universe it simulates, the exhaustion of computational resources will halt all simulations down the simulation chain unless an external programmer intervenes or isn't limited by the simulation's physical laws". p. 14: "the computer, if it is governed by the same physical laws as the simulation, would at least have to consist of the same number of particles and be the size of the universe."
- Verified: FULLTEXT
- Notes: arXiv preprint (v2, Dec 2022, Terra Quantum AG). We did not find a peer-reviewed version.

### C-06-063
- Claim: Wolpert formalizes simulation with the physical Church-Turing thesis. His framework allows the simulating and simulated universes to obey different laws of physics. Using Kleene's second recursion theorem, he proves that a universe obeying both the PCT and its "reverse" can simulate itself.
- Source: Wolpert2025what
- Locator: Abstract p. 1; Secs. 1.2 and 2, arXiv v5 pp. 5, 10
- Evidence: "I use Kleene's second recursion theorem to prove that it is mathematically possible for us to be a simulation that is being run on a computer — by us." ... "In general, the theorems derived below allow V and V′ to be (portions of) different cosmological universes, obeying different laws of physics." ... "I do not assume that the PCT applies to our actual physical universe."
- Verified: FULLTEXT
- Notes: Published as "What computer science has to say about the simulation hypothesis", J. Phys. Complexity 6, 045010 (2025). arXiv v5 (19 Mar 2026) was read; its title is "Implications of computer science theory for the simulation hypothesis".

### C-06-064
- Claim: Wolpert uses Rice's theorem to show that many mathematical questions about simulation and self-simulation are undecidable.
- Source: Wolpert2025what
- Locator: Sec. 1 overview, arXiv v5 p. 8
- Evidence: "Specifically, I use Rice's theorem to establish that many of the mathematical questions one might ask concerning simulation and self-simulation are undecidable."
- Verified: FULLTEXT
- Notes:

### C-06-065
- Claim: Faizal et al. themselves cite the spectral-gap, thermalization and RG-flow results. These undecidability proofs work by embedding a universal Turing machine in a computable local model, so a known undecidable property of the machine becomes a property of the physical model.
- Source: PeralesEceiza2025undecidability
- Locator: Sec. 1, arXiv v2 p. 6
- Evidence: "in order to prove the undecidability of properties of a physical system, one embeds a universal computer in it. Once embedded, a known undecidable property of the universal computer (e.g. the halting problem) is mapped to a property of the physical system, which therefore has to be undecidable as well."
- Verified: FULLTEXT
- Notes: This supports our observation that these results show computable local rules generating undecidable global properties. They are not evidence for non-algorithmic dynamics.
