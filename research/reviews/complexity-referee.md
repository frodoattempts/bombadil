# Referee report: complexity and computability (Section 6 and related statements)

Paper: "Testing the Simulation Hypothesis: A Critical Review of Arguments, Proposed Signatures, and Empirical Constraints"
Referee expertise: quantum complexity theory, computability, and the mathematical physics of undecidability
Material reviewed: `paper/sections/06-complexity.tex` (all of it); `research/ledgers/06-complexity.md`; `research/notes/06-complexity-report.md`; the complexity-related passages in `00-abstract.tex`, `00-introduction.tex`, `02-digital-physics.tex` (Deutsch, Lloyd, Wolfram, 't Hooft), `09-methodology.tex` (H-budget row, reception table) and `10-discussion.tex`. I read these primary texts myself: Faizal et al. arXiv:2507.22950v1, Redden arXiv:2512.11807, Troyer–Wiese cond-mat/0408370, Ringel–Kovrizhin (Sci. Adv. full text), Wolpert 2025 (J. Phys. Complex. text), Deutsch 1985, Aaronson arXiv:1108.1791, Jordan–Lee–Preskill arXiv:1112.4833, and Cubitt et al. arXiv:1502.04573.

---

## 1. Summary judgement and recommendation

**Recommendation: MAJOR REVISION.**

The section is better than most treatments of this topic. It is careful to attribute claims, and it quotes the authors' own caveats (Troyer–Wiese on "generic" solutions, Ringel–Kovrizhin on nonlocal QMC). It keeps the Ringel–Kovrizhin paper apart from its press coverage, and it does not say that the universe is or is not simulated. The organizing device, which separates execution (T1), deciding model properties (T2) and proving all truths (T3), is sound in essence. It is the familiar distinction between computing the time-*t* evolution map and deciding non-trivial global or asymptotic properties of that map (Moore, Wolfram, Rice-type results, Cubitt et al.). Wolpert's formal definition of the physical Church–Turing thesis (J. Phys. Complex. 6, 045010, Definition 3: "the evolution function g(.,.,.) of V is computable") is exactly T1-computability. That supports the framing, and the authors should say so.

As written, however, the section would not survive a careful complexity or computability referee. Nothing in it is FATAL. But several statements are technically wrong or misclassified, and some important literature is missing. The central problems are these:

1. **One result is misclassified in a way that breaks the section's own taxonomy.** Pour-El–Richards is a *finite-time* non-computability result, which is a T1 failure. The section files it under "the same structure" as the T2 infinite-limit results, and the table and conclusion then assert that no result shows "uncomputability of finite-time dynamics" (Issue 1).
2. **T1 is under-specified.** The section does not distinguish strong from weak simulation, or exact from approximate simulation. It assumes, but does not state, that the laws take a forward-evolution (Cauchy) form. It also does not say that T1 for quantum systems is itself BQP-complete (Issue 2).
3. **The asymptotic nature of complexity claims is never addressed.** Our universe is a single finite instance. "Superpolynomial overhead" needs a scaling parameter, and ECT failure needs scalable fault tolerance to be physically realizable, not just BPP ≠ BQP (Issue 3).
4. **The quantum-advantage discussion is thin and dated.** It omits Shor, Simon, BQP ⊆ PP, the PH-collapse basis of sampling hardness, the polynomial-time classical algorithm for noisy RCS, and experiments after 2022. The resulting Arute → Pan narrative reads as one-sided (Issue 4).
5. **Lloyd's theorem is over-applied to "our physics"** (Issue 5).
6. **The sign-problem subsection misses two points that a complexity theorist regards as central.** The Troyer–Wiese hardness is inherited from a *classical* spin glass, and the sign there is removable by a local basis change, as Troyer–Wiese themselves note. And every sign-problem obstruction concerns Euclidean/equilibrium sampling, not the real-time dynamics a simulator must execute (Issue 6).
7. **The critique of Faizal et al. rests on philosophical premises and a non-specialist, LLM-assisted comment.** It misses decisive internal logical errors in the paper that any logician would spot (Issue 7), and it wrongly calls the physical Church–Turing thesis "an open empirical question" (Issue 8).
8. **There are cross-section errors.** The introduction attributes to Ringel–Kovrizhin an argument that Sec. 6 itself shows they never made (Issue 9). The H-budget row says there is "no empirical test", yet the one place where complexity theory does make empirical contact is scalable quantum computation. Sec. 02 promises a discussion of 't Hooft's prediction that Sec. 6 never gives (Issue 10).

All of these are fixable within the existing structure. Most fixes are a sentence or a short paragraph, and proposed wording is given below.

**Issue counts:** FATAL 0 · MAJOR 10 · MINOR 15 · NIT 8.

---

## 2. Numbered issues

Line numbers refer to the current files (`cat -n`).

### MAJOR

#### Issue 1 (MAJOR): Pour-El–Richards is a T1 (finite-time) negative result, but it is filed and summarized as T2
**Location:** `06-complexity.tex:166` ("Earlier results have the same structure"), `:175–182`, `:187–190`, table row `:329`, conclusion `:342–343`.

**Evidence.** In the account the section itself relies on (Perales-Eceiza et al., C-06-040), Pour-El and Richards give computable initial data at *t* = 0 for the 3D wave equation such that the unique (weak) solution at *t* = 1 is not computable. That is precisely "uncomputability of finite-time dynamics", which the table row at `:329` says none of these results establishes. It is not an infinite-time or thermodynamic-limit property. The escape is different in kind:
- the non-computability depends on the norm or topology (it appears for C¹-but-not-C² data in the sup norm);
- in the energy norm or Sobolev spaces the propagator is computable (Weihrauch–Zhong, which the section cites; also Pour-El & Richards, *Computability in Analysis and Physics*, Springer 1989, doi:10.1007/978-3-662-21717-7);
- the pathological data are arguably not physically preparable.

Wolfram's statement that behaviour "may always be calculated by simulating explicitly each step" (`:172–173`) is presented as "the general point". It is contradicted two sentences later, because it presupposes computable dynamics.

**Fix.** Move Pour-El–Richards and Weihrauch–Zhong into a separate short paragraph. Proposed wording:
> "Pour-El and Richards's example is of a different kind: it is a finite-time (T1) failure. Computable initial data for the three-dimensional wave equation evolve, at time $t=1$, into a solution that is not computable in the supremum norm~\cite{PeralesEceiza2025undecidability}. The failure depends on the choice of norm and on initial data that are only $C^1$. In the energy norm or on Sobolev spaces the propagator is computable, and Weihrauch and Zhong argue that the example does not yield a physically realizable super-Turing device~\cite{Weihrauch2002is}. So T1-computability of continuum dynamics is not automatic. It holds for the function spaces and norms that physics actually uses."

Change the table row to: "Cubitt et al.; Moore; Wolfram | Undecidable thermodynamic-limit or infinite-time properties of computable models | Uncomputability of finite-time dynamics in physically relevant norms (cf. Pour-El–Richards)". Qualify the final sentence (`:342–343`) accordingly. Wolfram's sentence should be attributed as his claim for cellular automata, not given as the general point.

#### Issue 2 (MAJOR): T1 is under-specified in three ways that a complexity theorist will press
**Location:** `06-complexity.tex:9–24`, `:21` ("A simulator of a universe must perform (T1)").

**Evidence and fix.**
- **(a) Strong versus weak simulation.** "Evolving a given initial state forward ... to some accuracy" is ambiguous. It could mean *strong* simulation (computing amplitudes or output probabilities) or *weak* simulation (sampling observations with the correct distribution). This distinction is standard (Terhal & DiVincenzo, quant-ph/0205133; Van den Nest). Strong simulation is #P-hard even for circuit families whose weak simulation is believed easier, and a universe simulator for observers needs only weak simulation of the records it outputs. Feynman's "classical probabilistic computer" question (`:37–40`) is already a question about weak simulation.
- **(b) Exact versus approximate.** Feynman's and Deutsch's "exact" or "perfect" simulation is not what the simulation hypothesis needs. It needs output that is indistinguishable within the observational resolution of the simulated observers. Deutsch himself concedes that his universal quantum computer simulates closed systems only "with arbitrarily high but not perfect accuracy" (Deutsch 1985, §3; I read this in `deutsch85.txt`). His countability argument against *T* therefore applies equally to *Q* for continuous-parameter unitaries.
- **(c) The forward-evolution premise.** "Must perform (T1)" presupposes that the laws are given as a well-posed initial-value problem. That fails for physics with global consistency conditions:
  - closed timelike curves, where Aaronson & Watrous showed CTC computation equals PSPACE (Proc. R. Soc. A 465, 631, 2009; arXiv:0808.2669);
  - final-state or postselection proposals, where PostBQP = PP (Aaronson, Proc. R. Soc. A 461, 3473, 2005; quant-ph/0412187);
  - timeless canonical quantum gravity.

  Faizal et al. themselves invoke Novikov self-consistency (arXiv v1 p. 7). In such physics the simulator's task is a global fixed-point problem that may be PSPACE-hard. That is closer to T2 than to T1.
- **(d) T1 is not "easy".** For local quantum Hamiltonians, real-time evolution is BQP-complete: Feynman's circuit-to-Hamiltonian construction (Found. Phys. 16, 507, 1986, doi:10.1007/BF01886518) plus Lloyd 1996. So the question "does T1 have a cheap classical algorithm?" *is* BPP versus BQP.

**Proposed wording** (after `:20`):
> "We take (T1) to mean \emph{weak} simulation: producing the records that observers inside the model would obtain, with the correct statistics, to within their resolution. \emph{Strong} simulation, which computes output probabilities, is a harder task (it is \#P-hard in general) and a simulator does not need it. For local quantum Hamiltonians, (T1) is BQP-complete, so its classical cost is exactly the BPP-versus-BQP question of \S\ref{sec:complexity:feynman}. The claim that a simulator must perform (T1) assumes that the laws take an initial-value form. Physics with global consistency conditions, such as closed timelike curves, would instead require solving a fixed-point problem, which can be PSPACE-hard~\cite{Aaronson2009closed}."

#### Issue 3 (MAJOR): Complexity statements are asymptotic, and the section never says what scales
**Location:** `06-complexity.tex:75–79`, `:139–141`, `:336–343`.

**Evidence.** "A classical simulator ... incurs a superpolynomial overhead on some instances" (`:76–77`) and "would have to be quantum or pay superpolynomial overhead" (`:340–341`) are statements about *families*. Our universe, at ~10¹²⁰ operations (Lloyd), is one finite instance, and any finite instance has constant cost. The section applies the "undecidability concerns infinite families" point carefully to computability (`:156`) but never applies the analogous point to complexity. Aaronson discusses exactly this objection, calling asymptotic claims "having explanatory force until proven otherwise" (arXiv:1108.1791, §5.2 and fn. 23). Two further premises are hidden.
- **(i) Hard instances must actually occur.** The superpolynomial overhead bites only if hard instances occur *inside* the simulation, for example if the inhabitants build large fault-tolerant quantum computers, or if natural processes realize BQP-hard computations. Generic noisy quantum dynamics can be classically easy: Aharonov, Gao, Landau, Liu & Vazirani give a polynomial-time classical algorithm for noisy random circuit sampling (STOC 2023; arXiv:2211.03999).
- **(ii) BPP ≠ BQP is not enough.** ECT failure in our universe needs BPP ≠ BQP *and* the physical realizability of scalable fault tolerance (the threshold theorem holding for our noise). Informed sceptics dispute the latter (e.g. Kalai, arXiv:1908.02499). The closing paragraph (`:338–341`) lists only BPP ≠ BQP as the premise.

**Fix.** Proposed wording (replacing `:75–79`):
> "What follows validly from these results? Complexity statements concern families of instances, so a scaling parameter is needed. The natural one is the size of the quantum computations performed \emph{inside} the simulated world. Suppose BPP$\neq$BQP, and suppose large fault-tolerant quantum computation is physically possible in our universe. Then a classical simulator that reproduces the outputs of such computations pays a superpolynomial overhead in their size. A quantum simulator need not. If the inhabitants never run large coherent computations, and natural dynamics is noisy enough to be classically tractable~\cite{Aharonov2023polynomial}, then the argument gives no lower bound at all. The argument therefore constrains the simulator's architecture and running time, conditional on these premises. It does not bear on whether a simulation is possible."

Amend `:338–341` to name both premises.

#### Issue 4 (MAJOR): The account of the quantum-advantage evidence is thin, dated and one-sided
**Location:** `06-complexity.tex:63–73`.

**Evidence.**
- **Missing results.** The section omits:
  - Simon's exponential oracle separation (SIAM J. Comput. 26, 1474, 1997);
  - Shor's algorithm (SIAM J. Comput. 26, 1484, 1997; quant-ph/9508027), which is the strongest evidence against the ECT: a natural problem, studied for decades, with a superpolynomial speedup over the best known classical algorithm;
  - the tighter containment BQP ⊆ PP (Adleman, DeMarrais & Huang, SIAM J. Comput. 26, 1524, 1997).
- **Missing basis for sampling hardness.** The complexity-theoretic basis of *sampling* supremacy is the non-collapse of the polynomial hierarchy (Bremner, Jozsa & Shepherd, arXiv:1005.1407; Aaronson & Arkhipov, ToC 9, 143, 2013, arXiv:1011.3245). For approximate sampling, further average-case conjectures are needed (Aaronson & Chen, arXiv:1612.05903; Bouland et al., Nat. Phys. 15, 159, 2019, arXiv:1803.04402). "Experimental evidence is likewise conditional" should *name* these conditions.
- **One-sided narrative.** The narrative stops in 2022 with a classical rebuttal. That gives a 2026 reader the impression that the advantage claim was refuted. Later experiments claim much larger classical costs (e.g. Morvan et al., Nature 634, 328, 2024, arXiv:2304.11119), and below-threshold error correction has been demonstrated (Google Quantum AI, Nature 638, 920, 2025, arXiv:2408.13687). Pan et al. do show that *specific* classical-cost estimates were provisional. They do not bear on the asymptotic question, as the ledger note to C-06-014 correctly says but the text does not.
- **Fidelity comparison.** State that Pan et al.'s fidelity (≈0.0037) *exceeds* Sycamore's XEB fidelity (≈0.002). This is what makes their result a genuine classical match, and it is worth saying.

**Fix.** Proposed wording (after the BV sentence):
> "Simon gave an exponential oracle separation~\cite{Simon1997power}, and Shor gave polynomial-time quantum algorithms for factoring and discrete logarithms, problems for which no classical polynomial-time algorithm is known~\cite{Shor1997polynomial}. The tighter containment BQP$\subseteq$PP~\cite{Adleman1997quantum} means that an unconditional proof of BPP$\neq$BQP would separate P from PP. The classical hardness of the sampling tasks used in advantage experiments rests on the conjecture that the polynomial hierarchy does not collapse, together with further average-case conjectures~\cite{Aaronson2013computational,Bouland2019complexity}."

Then give Arute, Pan (with the fidelity comparison), and one post-2022 experiment. End with: "Such benchmarks bound constant factors at fixed sizes; they do not bear on the asymptotic question."

#### Issue 5 (MAJOR): Lloyd's theorem is over-applied to "our physics", and one attribution is anachronistic
**Location:** `06-complexity.tex:44–56`, `:78` ("A quantum simulator does not, by Lloyd's theorem"), `:340–341`.

**Evidence.**
- **Scope of Lloyd's result.** Lloyd 1996 covers finite-dimensional, bounded-norm, few-body ("local") Hamiltonians. Our physics as currently formulated is a continuum QFT (the Standard Model) plus gravity. Neither is covered. No rigorous construction of interacting 4D QFTs exists, and there is no known lattice regularization of chiral gauge theories. So "by Lloyd's theorem" is an overstatement for our universe.
- **Jordan–Lee–Preskill.** I checked arXiv:1112.4833 (the long version of Jordan2012quantum). The strong-coupling analysis is for D = 2, 3 spacetime dimensions only. In D = 4, φ⁴ is believed trivial, and "strong coupling requires pa to be O(1)" (§2.1.3, §4.2.2). "Polynomial-time quantum algorithms exist for scattering in φ⁴ theory in up to four spacetime dimensions" (`:51–53`) is true as stated, but the paper supports it only in the weak-coupling regime for D = 4. The ledger entry is ABSTRACT-level and misses this.
- **Anachronism.** "Lloyd regarded such results as 'a strong indication'" (`:53–55`) follows sentences about Bravyi–Kitaev (2002) and Jordan–Lee–Preskill (2012). Lloyd's 2002 remark (C-06-058) is about "any theory that is locally finite". It cannot refer to JLP.
- **Lloyd's "directly proportional".** This is Lloyd's phrase. With Trotter splitting at fixed total error the cost is superlinear in *t*. Near-linear cost was established later (Haah, Hastings, Kothari & Low, SIAM J. Comput. 2023; arXiv:1801.03922). This is a NIT-level point, but quote it as Lloyd's claim.

**Fix.** Replace `:78` with:
> "A quantum simulator does not pay this overhead for any finite-dimensional local lattice model (Lloyd's theorem). Efficient quantum simulation has also been shown for some quantum field theories, such as $\phi^4$ theory~\cite{Jordan2012quantum}. That the complete laws of our universe (chiral gauge theories, gravity) are efficiently quantum-simulable is an expectation~\cite{Lloyd2002computational}."

Rephrase `:53–55` as "Lloyd regarded the efficient simulability of locally finite theories as 'a strong indication' ...". Add "(in four dimensions only at weak coupling)" to the JLP sentence. Cite Jordan, Krovi, Lee & Preskill, "BQP-completeness of scattering in scalar quantum field theory" (Quantum 2, 44, 2018; arXiv:1703.00454). It shows that QFT dynamics can itself embody BQP-complete computation, which is the precise sense in which "physics is hard to simulate classically".

#### Issue 6 (MAJOR): The sign-problem subsection misses the two points that decide its relevance
**Location:** `06-complexity.tex:84–130`.

**Evidence.**
- **(a) Troyer–Wiese's hardness is classical in origin.** Their hard model is H = −Σ J_jk σ^x_j σ^x_k. It is diagonal in the σ^x basis, and a Hadamard on every site maps it onto the classical ±J spin glass with non-negative Boltzmann weights. Troyer and Wiese note the representation dependence themselves: the sign problem "is representation-dependent ... in some models it can be solved by a simple local basis change" (cond-mat/0408370, p. 3). In the sign-free basis the problem is equally NP-hard, because low-temperature sampling of a 3D spin glass is hard. So the NP-hardness shows that a generic sign-problem cure would also cure glassy slow mixing. It does *not* show that quantum systems are harder than classical ones. Hangleiter, Roth, Nagaj & Eisert discuss this basis dependence and show that optimizing the basis to ease the sign problem is itself NP-hard (Sci. Adv. 6, eabb8341, 2020; arXiv:1906.02309).
- **(b) All these results concern equilibrium (Euclidean) sampling, not real-time dynamics.** Ringel–Kovrizhin state explicitly that QMC treats "the Euclidean (or thermal) partition function ... with the extra dimension being imaginary time" (Sci. Adv. full text). The same holds for Hastings, Smith et al., Golan et al. and Marvian et al. A universe simulator must execute real-time evolution (T1), and its classical hardness rests on BQP-completeness, not on sign problems. Ringel and Kovrizhin themselves note that some of their bosonic systems "can be used as hardware for universal quantum computations; therefore, simulating them classically in polynomial time is likely to be impossible". That is a BQP argument, not a sign-problem argument, and it should be quoted.

**Fix.** Insert after `:96`:
> "The hard instance is classical in origin. Rotating every spin by a Hadamard gate removes the sign and maps the model onto the classical spin glass, whose low-temperature sampling is equally hard. Troyer and Wiese note that the sign problem is representation-dependent~\cite{Troyer2005computational}, and choosing the representation that eases it is itself NP-hard~\cite{Hangleiter2020easing}. The result therefore shows that a generic cure for the sign problem would also cure glassy slow relaxation. It does not show that quantum systems are harder to simulate than classical ones."

Change `:128–130` to:
> "None of these results concerns classical algorithms outside the QMC family, quantum simulators, or real-time dynamics. All of them concern equilibrium (imaginary-time) sampling. The classical hardness of real-time quantum dynamics rests instead on its BQP-completeness, a point Ringel and Kovrizhin themselves make."

#### Issue 7 (MAJOR): The Faizal et al. critique misses the paper's decisive internal errors and relies on a weak source
**Location:** `06-complexity.tex:198–257`.

**Evidence** (from my own reading of arXiv:2507.22950v1, pp. 3–5 and 8).

- **(a) Condition (S1) contradicts the paper's central claim.** (S1) reads: "whenever T(⌜φ⌝) is an axiom, φ holds in every model of the base theory". By Gödel's *completeness* theorem, a sentence holds in every model of Σ_QG iff Σ_QG ⊢ φ. So (S1) forces Th_T ⊆ Th(F_QG): the "external truth predicate" can certify only sentences that are *already provable*. That contradicts the claim on the same page that it "certifies every Gödel sentence of F_QG". A consistent theory's Gödel sentence is unprovable, and hence false in some model of Σ_QG. On a literal reading, M_ToE as defined is inconsistent with its stated purpose.
- **(b) Their own definition makes the Gödel sentences arithmetic.** They define True(F_QG) = {φ | ℕ ⊨ φ}. The Gödel sentences in question are then arithmetic Π₁ sentences, equivalent to "a certain Turing machine never halts" (for example Con(F_QG)). They are not statements about black-hole microstates. More importantly for this section, the *truth* of a Π₁ sentence is instantiated by a computable process that runs forever. A T1 simulator reproduces that fact trivially by running the machine: in the simulation, too, it never halts. So even if step (iii) is granted, the facts it identifies are instantiated by computable dynamics. This is a sharper and fully rigorous version of Redden's Game-of-Life point.
- **(c) Chaitin's theorem is misstated.** The paper says Chaitin gives "a constant K_F such that any sentence S with prefix-free Kolmogorov complexity K(S) > K_F is undecidable in F_QG" (p. 4). That is false: a long tautology or a long true numerical identity has high complexity and is provable. Chaitin's theorem says that F cannot prove statements *of the form* "K(x) > L" for L above a constant c_F. The section's "Tarski's and Chaitin's theorems add further limits" (`:207–208`) passes over this. A computability referee will notice.
- **(d) The (T3)-to-physics bridge ignores Geroch–Hartle.** Faizal et al.'s step from incompleteness to quantum gravity ignores the one serious prior argument that quantum gravity might be non-computable. Geroch & Hartle (Found. Phys. 16, 533, 1986; doi:10.1007/BF01886519) argue from Markov's theorem, which says that 4-manifolds cannot be algorithmically classified, that a sum over topologies may be non-computable. Citing it would show that the authors know the serious version of the claim, and would contrast it with the Gödelian version.
- **(e) The main counter-source is weak.** The critique leans on Redden (arXiv:2512.11807), a two-page single-author comment by a non-specialist. It discloses LLM assistance, and it contains the conflation the report itself flags ("unrealizable due to the Church-Turing thesis"). The objection is standard and has much stronger sources. Franzén's *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse* (A K Peters, 2005; doi:10.1201/b10700) is the canonical reference on misapplications of Gödel to physics and "theories of everything". Barrow's "Gödel and physics" (arXiv:physics/0612253) is also relevant. Redden can stay, but not as the only critic cited.
- **(f) A petty observation should go.** "Its axioms are recursively enumerable; on the same page they are also said to be finite" (`:202–204`) is not an inconsistency: finite sets are r.e., and "finite (or at least r.e.)" followed by "finite" is simply a choice. It looks petty next to the real errors. Replace it with (a)–(c).

**Fix.** Proposed wording (after `:236`):
> "The paper's formal apparatus does not support its conclusion even on its own terms. Condition (S1) requires every $T$-certified sentence to hold in every model of the base theory. By Gödel's completeness theorem, those are exactly the sentences the base theory already proves, so $T$ cannot certify the unprovable Gödel sentences it is introduced to certify~\cite[p.~5]{Faizal2025consequences}. The paper defines truth as truth in the standard model of arithmetic. Its Gödel sentences are therefore arithmetic $\Pi_1$ sentences, each equivalent to the non-termination of a particular Turing machine. Such a truth is realized by a computable process that simply never halts, and a simulator reproduces it by running that process. The paper also misstates Chaitin's theorem. The theorem bounds a theory's ability to prove lower bounds on Kolmogorov complexity; it does not make every high-complexity sentence undecidable~\cite{Franzen2005godel}."

Delete the "finite / r.e." remark.

#### Issue 8 (MAJOR): Whether physics is Turing-computable is not "an open empirical question" in the ordinary sense, and the "valid core" has the wrong antecedent
**Location:** `06-complexity.tex:224–227`, `:255–257`.

**Evidence.**
- **(a) No finite data can settle it.** Any finite body of finite-precision observations is a finite string, and is trivially Turing-computable (hard-code it). No finite data set can refute the physical Church–Turing thesis or confirm hypercomputation. The question is which *theories* of the data are computable, and whether a device's non-computable behaviour could ever be certified. This is a classic point (Kreisel, Synthese 29, 11, 1974, doi:10.1007/BF00484949; Davis, Appl. Math. Comput. 178, 4, 2006, doi:10.1016/j.amc.2005.09.066). It also bears directly on the paper's methodological thesis in Sec. 9. Calling the question "open empirical" invites the reply that it is exactly as untestable as H_SIM.
- **(b) The antecedent is too strong.** "*If* the observable dynamics ... depends on a non-recursively-enumerable predicate" (`:224–226`) is sufficient but far stronger than needed. Dependence on an r.e. but non-recursive predicate, such as the halting set, already defeats a Turing machine. The correct antecedent is "is not Turing-computable", which is exactly the denial of the physical Church–Turing thesis in Wolpert's Definition 3.

**Fix.**
> "\emph{If} the dynamics of our universe is not Turing-computable, for example if advancing it requires deciding the halting set, then no Turing-equivalent machine reproduces it."

and, at `:255–257`:
> "The disagreement therefore reduces to whether the best theory of physical dynamics is Turing-computable. No finite body of observations can settle that question, because any finite record is computable~\cite{Kreisel1974notion,Davis2006why}. Incompleteness certainly does not settle it."

#### Issue 9 (MAJOR): The introduction attributes to Ringel–Kovrizhin an argument that Sec. 6 shows they never made
**Location:** `00-introduction.tex:4`.

**Evidence.** "Others have argued that computational complexity or undecidability rules simulation out~\cite{Ringel2017quantized,Faizal2025consequences}". Section 6 (`:132–133`), ledger C-06-024 and Table `tab:reception` in `09-methodology.tex` all state that Ringel–Kovrizhin never mention the simulation hypothesis. This is precisely the press misreading the paper is trying to correct, and a referee will quote this sentence back at the authors.

**Fix.**
> "Others have argued that undecidability rules simulation out~\cite{Faizal2025consequences}, and a result on quantum Monte Carlo~\cite{Ringel2017quantized} was widely reported as doing so on grounds of computational complexity~\cite{Eck2017physicists}."

#### Issue 10 (MAJOR): The H-budget row says "no empirical test", but scalable quantum computation *is* the empirical test, and 't Hooft's prediction is never followed up
**Location:** `09-methodology.tex:152`; `10-discussion.tex:13`; `02-digital-physics.tex:246–250` (the cross-reference to Sec. 6 that is never honoured); `00-abstract.tex:1` (which lists "bounded computational resources" among empirical signatures).

**Evidence.** A resource-bounded *classical* simulator, or 't Hooft's classical Planck-scale automaton (C-02-039, C-07-047), predicts that scalable quantum computational advantage fails beyond some size. The prediction is sharpest for *verifiable* tasks such as Shor factoring, where outputs can be checked classically. Random-circuit sampling is weaker because XEB verification needs classical simulation. 't Hooft states that success of such quantum computers would falsify his theory. This is the one place where the complexity literature makes contact with experiment, and the paper's own framework fits it well: a failure of scalable QC would be "new physics, not simulation", degenerate with 't Hooft's CAI, noise-based scepticism (Kalai, arXiv:1908.02499) and gravitationally induced collapse. Section 6 never mentions 't Hooft, although `02-digital-physics.tex:249–250` promises that it does.

An illustrative estimate, which the authors must redo before using it: in the holographic version, the classical machine has ~4×10⁶⁹ sites for 1 m² and ~2×10⁴³ steps per second. That is ~10¹¹² operations per second. By the heuristic GNFS cost L_N[1/3, 1.923], this is exceeded only for integers of order 3–4×10⁴ bits (roughly 7×10⁴ bits in the volume version). Shor's algorithm would need about 10¹³–10¹⁵ gates for such integers. The prediction is therefore falsifiable in principle, but only far beyond RSA-2048.

**Fix.** In Sec. 6, add a short paragraph at the end of §6.1 or in §6.6:
> "One complexity-based sub-hypothesis is testable in principle. If the simulator is a classical machine whose resources scale with the simulated volume, as in 't~Hooft's cellular-automaton proposal~\cite{tHooft2016cellular}, then quantum computers cannot outperform it beyond a fixed factor. Verifiable large-scale quantum computation, such as Shor factoring of integers that are classically infeasible to factor, would refute this design. Its failure would indicate new physics, whether or not the world is simulated."

Change the H-budget row to:
- Signature: "Ceiling on scalable (fault-tolerant) quantum computational advantage".
- Degenerate explanation: "'t Hooft's CA interpretation; noise-based limits on fault tolerance; objective-collapse models".
- Status: "Testable in principle by verifiable large-scale quantum computation; current experiments do not reach the relevant scale".

Adjust `10-discussion.tex:13` ("None of these arguments is an empirical test") accordingly.

### MINOR

#### Issue 11 (MINOR): Troyer–Wiese P vs BPP: "refines this to BPP" is incomplete
**Location:** `06-complexity.tex:92–93`.

**Evidence and fix.** The footnote refines the class of the Monte Carlo *algorithm*. The correct consequence is **NP ⊆ BPP**. It is not "NP = BPP", which is not implied, since BPP ⊆ NP is open. Proposed wording:
> "The paper states that a generic solution would imply P=NP. Its footnote~9 correctly observes that a Monte Carlo solution is a BPP algorithm, so the precise consequence is NP$\subseteq$BPP. This is still considered implausible: it would collapse the polynomial hierarchy, and under standard derandomization conjectures (P=BPP~\cite{Impagliazzo1997bpp}) it would again give P=NP."

The table row at `:327` is already correct.

#### Issue 12 (MINOR): Bernstein–Vazirani: what an oracle separation does and does not show
**Location:** `06-complexity.tex:63–68`.

**Fix.** "First formal evidence" is BV's own description, so attribute it as such. Add that the BV separation (recursive Fourier sampling) is superpolynomial but only quasi-polynomial. Add that oracle separations do not transfer to the unrelativized world. Add that Raz & Tal gave an oracle relative to which BQP ⊄ PH (STOC 2019; J. ACM 69, 2022; doi:10.1145/3530258). Replace, or supplement, BQP ⊆ P^#P with BQP ⊆ PP (ADH 1997) and state the consequence precisely, as in Issue 4. Minor wording point: "requiring superpolynomial time classically" should read "on a bounded-error probabilistic Turing machine, relative to the oracle".

#### Issue 13 (MINOR): The T2 definition misstates where the infinity lies
**Location:** `06-complexity.tex:15–17`; also `:153–156`.

**Evidence.** "Undecidable when they quantify over infinitely many times, sizes or instances" conflates two different things. Every decision problem ranges over infinitely many instances, and a single instance is always trivially decidable. The other thing is a single instance's property involving an infinite limit (halting, thermodynamic-limit gap). Cubitt et al. need both. Moreover, Cubitt et al.'s Corollary 4 (independence of the gap for an individual Hamiltonian from any consistent r.e. theory, `:153–155`) is a T3-type statement derived from T2 undecidability. This is the standard route from algorithmic undecidability to incompleteness, and the section should say so: it links T2 and T3 rather than treating them as independent.

**Fix.**
> "... can be intractable for finite instances. They can be algorithmically undecidable as problems, that is, over infinite families of instances, when the property involves an infinite limit such as infinite time or the thermodynamic limit. Undecidability of a family implies that, for any consistent recursively axiomatized theory, some individual instances are independent of it. This is how (T2) results yield (T3) results."

#### Issue 14 (MINOR): The T3 definition is ill-formed
**Location:** `06-complexity.tex:18–19`.

**Evidence.** "Deriving every true sentence of a formal theory of the model from its axioms." Truth is relative to a structure, not to a theory. The phrase makes T3 either trivial (deriving the theory's theorems) or ill-typed.

**Fix.**
> "(T3) \emph{Proof}: deriving, from a recursively axiomatized theory of the model, every sentence of its language that is true in the intended model. By Gödel's first theorem this is impossible for consistent theories that interpret enough arithmetic."

#### Issue 15 (MINOR): Cubitt et al.: add the promise version and the 1D result, and state what depends on n
**Location:** `06-complexity.tex:148–152`.

**Fix.** Add the following:
- Undecidability holds "even with the promise that each Hamiltonian is either gapped or gapless in the strongest sense" (arXiv:1502.04573, abstract).
- The local dimension d is fixed, while the matrix entries are algebraic numbers that depend on n.
- The result extends to 1D (Bausch, Cubitt, Lucia & Perez-Garcia, PRX 10, 031038, 2020; arXiv:1810.01858).

The last point matters because a reader may otherwise think that dimension ≥ 2 is essential.

#### Issue 16 (MINOR): Wolfram's PSPACE-completeness claim is stated as fact
**Location:** `06-complexity.tex:174–175`.

**Evidence.** "The finite versions are decidable, though PSPACE-complete for universal cellular automata" is Wolfram's 1985 assertion. PSPACE-completeness of the bounded problem does not follow from universality alone. It needs a space-efficient (polynomial-overhead) universality simulation.

**Fix.** "Wolfram states that ... are PSPACE-complete for universal cellular automata, where the universality construction is space-efficient." See also Issue 1 on "may always be calculated".

#### Issue 17 (MINOR): Hamiltonian complexity is missing from the T2 examples
**Location:** `06-complexity.tex:13–14`, `:98–109`.

**Evidence.** The T2 example "whether a ground state has energy below E₀" is, for quantum local Hamiltonians, the QMA-complete Local Hamiltonian problem. The references are Kitaev; Kempe, Kitaev & Regev (SIAM J. Comput. 35, 1070, 2006; quant-ph/0406180); Oliveira & Terhal (quant-ph/0504050); Aharonov, Gottesman, Irani & Kempe for 1D (CMP 287, 41, 2009; arXiv:0705.4077); and Gottesman & Irani for the translation-invariant case (arXiv:0905.2419). For the stoquastic class that underlies the sign-problem literature, see Bravyi, DiVincenzo, Oliveira & Terhal (quant-ph/0606140). Surveys are Osborne (Rep. Prog. Phys. 75, 022001, 2012; arXiv:1106.5875) and Gharibian et al. (arXiv:1401.3916).

The section's argument that "a physical spin glass does not [solve it]" extends directly. Unless QMA ⊆ BQP, nature does not efficiently cool generic local quantum systems to their ground states either. That strengthens the T1/T2 point and should be made with these citations.

#### Issue 18 (MINOR): Wolpert 2025 is a computability result, silent on complexity, and its PCT definition supports the section's framing
**Location:** `06-complexity.tex:250–255`, `:307`.

**Evidence.** Wolpert defines the PCT as computability of the evolution function (Definition 3, p. 9), which is T1-computability. He states that "I have not considered the computational complexity of finding S(Δt)" (§9, p. 25). He also notes that a self-simulation runs "more slowly" (footnote 12).

**Fix.** Add: "Wolpert's result concerns computability only. He leaves its complexity-theoretic counterpart, the time overhead of (self-)simulation, open~\cite{Wolpert2025what}." Cite his Definition 3 in the T1 paragraph as independent support for the framing.

#### Issue 19 (MINOR): The closing claims about the continuum and undecidable properties need qualification
**Location:** `06-complexity.tex:341–343`.

**Evidence and fix.**
- "It would have to approximate continuum quantities to finite precision" is too strong. In computable analysis, a Turing machine can *represent* computable reals exactly and output any requested precision on demand. What is excluded is storing arbitrary (non-computable) real parameters, and, within our physics, unbounded information density (Aaronson 2005 via the holographic bound).
- "It would never need to decide the undecidable properties" is correct for T1 *given* computable dynamics in the relevant norms (see Issue 1).

Proposed wording:
> "It could store only finitely much information about continuum quantities at any stage, although computable quantities can be refined on demand. Provided its dynamics is computable in the relevant norms, it would never need to decide the undecidable properties of the models it runs."

#### Issue 20 (MINOR): Moore: finite-time computability versus finite-time cost
**Location:** `06-complexity.tex:166–171`.

**Evidence.** Moore's systems are chaotic. Finite-time quantities are computable, but at fixed output accuracy the required input precision, and so the cost, grows exponentially with *t*. For a simulator this is a T1 *complexity* issue, not just a T2 computability issue.

**Fix.** Add one clause: "... although, the dynamics being chaotic, the precision and cost required grow exponentially with the simulated time."

#### Issue 21 (MINOR): The "valid core" formulation in the Faizal subsection
Folded into Issue 8(b). Listed here for tracking only; it is not counted separately.

#### Issue 22 (MINOR): Convention violations in the ledger
**Location:** `research/ledgers/06-complexity.md` C-06-013, C-06-014, C-06-040; `06-complexity.tex:177`.

**Evidence.**
- CONVENTIONS §2 requires FULLTEXT for "every numerical value". The Arute figures (200 s, 10,000 years) and the Pan figures (15 h, 512 GPUs, F ≈ 0.0037) are ABSTRACT-verified.
- PourEl1981wave is METADATA-level but is cited with `\cite{PourEl1981wave}` beside a characterization. Attributing the characterization to the review, as `:177–178` does, is acceptable. The better fix is to read Pour-El & Richards 1989, Ch. 3, or the 1981 paper.
- JLP is ABSTRACT-only, and that missed the D = 4 caveat (Issue 5).

**Fix.** Upgrade these entries to FULLTEXT; arXiv:1910.11333 and arXiv:2111.03011 are both open.

#### Issue 23 (MINOR): Sec. 02, Deutsch: his own caveat on closed systems is omitted
**Location:** `02-digital-physics.tex:39–42`.

**Evidence.** "Quantum theory, he argued, is compatible with it through a universal quantum computer". Deutsch claims *perfect* simulation only for "real (dissipative) finite physical system[s]". He concedes that closed systems are simulated "with arbitrarily high but not perfect accuracy" (Deutsch 1985, §§1, 3). His countability argument against *T* therefore applies to *Q* for continuous-parameter closed dynamics.

**Fix.** Add: "... for dissipative systems; closed systems, he conceded, are simulated only to arbitrarily high but not perfect accuracy."

#### Issue 24 (MINOR): The hypercomputation subsection is thin
**Location:** `06-complexity.tex:259–275`.

**Fix.** The subsection relies only on the SEP entry and Aaronson 2005. Add, all verified:
- Hogarth 1992 (Found. Phys. Lett. 5, 173; doi:10.1007/BF00682813);
- Earman & Norton 1993 (Phil. Sci. 60, 22; doi:10.1086/289716);
- Etesi & Németi 2002 (IJTP 41, 341; gr-qc/0104023), on Malament–Hogarth computers;
- Smith 2006, "Church's thesis meets the N-body problem" (Appl. Math. Comput. 178, 154; doi:10.1016/j.amc.2005.09.077), the concrete Newtonian counterexample behind Gandy's remark;
- Piccinini 2011, "The physical Church–Turing thesis: modest or bold?" (BJPS 62, 733; doi:10.1093/bjps/axr016);
- Arrighi & Dowek (arXiv:1102.1612);
- Deutsch, Ekert & Lupacchini 2000 (Bull. Symb. Logic 6, 265; doi:10.2307/421056);
- Geroch & Hartle 1986 (see Issue 7(d)).

#### Issue 25 (MINOR): Faizal et al., premise (i), "finite versus r.e."
Folded into Issue 7(f). Listed for tracking; it is not counted separately.

#### Issue 26 (MINOR): Troyer–Wiese on quantum simulators: add the complexity reason
**Location:** `06-complexity.tex:101–102`.

**Fix.** Their "most likely not a generic solution" is backed in complexity terms by the conjecture NP ⊄ BQP. The oracle evidence for that conjecture is Bennett, Bernstein, Brassard & Vazirani (SIAM J. Comput. 26, 1510, 1997; quant-ph/9701001). Cite it so that the sentence has a complexity-theoretic basis.

#### Issue 27 (MINOR): Aaronson's "Why philosophers should care about computational complexity" is not cited
**Location:** `06-complexity.tex` passim.

**Evidence.** arXiv:1108.1791 is in `/tmp/claude-0/papers/` but is cited nowhere. It is the standard reference for three of the section's moves:
- the asymptotic-versus-finite objection (§5.2, fn. 23);
- the polynomial-time Church–Turing thesis and quantum computing (§8);
- the computational-complexity reply to "waterfall"-style implementation arguments (§6).

Wolpert 2025 cites it too (ref. [3]).

**Fix.** Cite it in the ECT paragraph and in the new asymptotics paragraph (Issue 3).

(Issues 21 and 25 are cross-references and are not counted. The 15 MINOR issues are 11–20, 22–24, 26 and 27.)

### NIT

- **Issue 28 (NIT)** (`06-complexity.tex:63`): Put "first formal evidence" in quotation marks as BV's phrase (see Issue 12).
- **Issue 29 (NIT)** (`06-complexity.tex:99–101`): τ ∝ e^{aN} is Troyer–Wiese's heuristic "as expected for this NP-complete problem", not a theorem. Say "Troyer and Wiese note that ... are expected to be exponentially large".
- **Issue 30 (NIT)** (`06-complexity.tex:326`, table): "Exponential cost for classical storage of general quantum states" is almost tautological. Use "Exponential cost of direct (state-vector) classical simulation; no lower bound for all classical algorithms".
- **Issue 31 (NIT)** (`06-complexity.tex:330`, table): "Incompleteness of r.e. theories (standard)" should read "Incompleteness of consistent r.e. theories interpreting arithmetic (standard; no new result)".
- **Issue 32 (NIT)** (`06-complexity.tex:45–47`): Lloyd's "directly proportional" is his phrase. Modern bounds are near-linear in *t* (HHKL 2018, arXiv:1801.03922). Quote it as Lloyd's claim (see Issue 5).
- **Issue 33 (NIT)** (bibliography): The same ScienceDaily page has two keys, `UBCO2025physicists` (06) and `ScienceDaily2025physicists` (09). Merge them before the bib files are combined.
- **Issue 34 (NIT)** (`00-abstract.tex:1` versus `09-methodology.tex:152`): The abstract lists "bounded computational resources" as an empirical signature, while the H-budget row says "no empirical test". Resolve this via Issue 10.
- **Issue 35 (NIT)** (`06-complexity.tex:139–141`): Aaronson's own formulation is "until someone proves P≠PSPACE" (C-06-030). Given BQP ⊆ PP, the sharper statement is P ≠ PP. Either quote him or state the sharper form. Do not paraphrase in a way that changes the class.

---

## 3. Missing literature (each item verified to exist; identifier checked on arXiv abs pages or Crossref, 2026-09-27)

**Quantum advantage and the ECT**
- P. W. Shor, "Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer", SIAM J. Comput. 26, 1484 (1997). arXiv:quant-ph/9508027; doi:10.1137/S0097539795293172.
- D. R. Simon, "On the power of quantum computation", SIAM J. Comput. 26, 1474 (1997). doi:10.1137/S0097539796298637.
- L. Adleman, J. DeMarrais, M.-D. Huang, "Quantum computability", SIAM J. Comput. 26, 1524 (1997). doi:10.1137/S0097539795293639 (BQP ⊆ PP).
- C. Bennett, E. Bernstein, G. Brassard, U. Vazirani, "Strengths and weaknesses of quantum computing", SIAM J. Comput. 26, 1510 (1997). arXiv:quant-ph/9701001; doi:10.1137/S0097539796300933.
- R. Raz, A. Tal, "Oracle separation of BQP and PH", STOC 2019, doi:10.1145/3313276.3316315; J. ACM 69 (2022), doi:10.1145/3530258.
- R. Impagliazzo, A. Wigderson, "P = BPP if E requires exponential circuits", STOC 1997. doi:10.1145/258533.258590.
- M. Bremner, R. Jozsa, D. Shepherd, "Classical simulation of commuting quantum computations implies collapse of the polynomial hierarchy", Proc. R. Soc. A 467, 459 (2011). arXiv:1005.1407; doi:10.1098/rspa.2010.0301.
- S. Aaronson, A. Arkhipov, "The computational complexity of linear optics", Theory of Computing 9, 143 (2013). arXiv:1011.3245; doi:10.4086/toc.2013.v009a004.
- S. Aaronson, L. Chen, "Complexity-theoretic foundations of quantum supremacy experiments" (CCC 2017). arXiv:1612.05903.
- A. Bouland, B. Fefferman, C. Nirkhe, U. Vazirani, "On the complexity and verification of quantum random circuit sampling", Nat. Phys. 15, 159 (2019). arXiv:1803.04402; doi:10.1038/s41567-018-0318-2.
- A. Harrow, A. Montanaro, "Quantum computational supremacy", Nature 549, 203 (2017). arXiv:1809.07442; doi:10.1038/nature23458.
- D. Aharonov, X. Gao, Z. Landau, Y. Liu, U. Vazirani, "A polynomial-time classical algorithm for noisy random circuit sampling", STOC 2023. arXiv:2211.03999; doi:10.1145/3564246.3585234.
- A. Morvan et al., "Phase transitions in random circuit sampling", Nature 634, 328 (2024). arXiv:2304.11119; doi:10.1038/s41586-024-07998-6.
- Google Quantum AI, "Quantum error correction below the surface code threshold", Nature 638, 920 (2025). arXiv:2408.13687; doi:10.1038/s41586-024-08449-y.
- G. Kalai, "The argument against quantum computers". arXiv:1908.02499 (a sceptic's position, relevant to Issues 3 and 10).
- B. Terhal, D. DiVincenzo, "Adaptive quantum computation, constant depth quantum circuits and Arthur-Merlin games". arXiv:quant-ph/0205133 (strong versus weak simulation).

**Simulating QFT and Hamiltonian dynamics**
- S. Jordan, K. Lee, J. Preskill, "Quantum computation of scattering in scalar quantum field theories" (long version of Jordan2012quantum). arXiv:1112.4833.
- S. Jordan, K. Lee, J. Preskill, "Quantum algorithms for fermionic quantum field theories". arXiv:1404.7115.
- S. Jordan, H. Krovi, K. Lee, J. Preskill, "BQP-completeness of scattering in scalar quantum field theory", Quantum 2, 44 (2018). arXiv:1703.00454; doi:10.22331/q-2018-01-08-44.
- J. Haah, M. Hastings, R. Kothari, G. H. Low, "Quantum algorithm for simulating real time evolution of lattice Hamiltonians", SIAM J. Comput. (2023). arXiv:1801.03922; doi:10.1137/18M1231511.
- R. P. Feynman, "Quantum mechanical computers", Found. Phys. 16, 507 (1986). doi:10.1007/BF01886518.

**Hamiltonian complexity and the sign problem**
- J. Kempe, A. Kitaev, O. Regev, "The complexity of the local Hamiltonian problem", SIAM J. Comput. 35, 1070 (2006). arXiv:quant-ph/0406180; doi:10.1137/S0097539704445226.
- R. Oliveira, B. Terhal, "The complexity of quantum spin systems on a two-dimensional square lattice". arXiv:quant-ph/0504050.
- D. Aharonov, D. Gottesman, S. Irani, J. Kempe, "The power of quantum systems on a line", CMP 287, 41 (2009). arXiv:0705.4077; doi:10.1007/s00220-008-0710-3.
- D. Gottesman, S. Irani, "The quantum and classical complexity of translationally invariant tiling and Hamiltonian problems". arXiv:0905.2419.
- S. Bravyi, D. DiVincenzo, R. Oliveira, B. Terhal, "The complexity of stoquastic local Hamiltonian problems". arXiv:quant-ph/0606140.
- T. Osborne, "Hamiltonian complexity", Rep. Prog. Phys. 75, 022001 (2012). arXiv:1106.5875; doi:10.1088/0034-4885/75/2/022001.
- S. Gharibian, Y. Huang, Z. Landau, S. W. Shin, "Quantum Hamiltonian complexity", Found. Trends TCS 10, 159 (2015). arXiv:1401.3916; doi:10.1561/0400000066.
- D. Hangleiter, I. Roth, D. Nagaj, J. Eisert, "Easing the Monte Carlo sign problem", Sci. Adv. 6, eabb8341 (2020). arXiv:1906.02309; doi:10.1126/sciadv.abb8341.

**Undecidability in physics**
- J. Bausch, T. Cubitt, A. Lucia, D. Perez-Garcia, "Undecidability of the spectral gap in one dimension", PRX 10, 031038 (2020). arXiv:1810.01858; doi:10.1103/PhysRevX.10.031038.
- R. Cardona, E. Miranda, D. Peralta-Salas, F. Presas, "Constructing Turing complete Euler flows in dimension 3", PNAS 118, e2026818118 (2021). arXiv:2012.12828; doi:10.1073/pnas.2026818118.
- M. B. Pour-El, J. I. Richards, *Computability in Analysis and Physics*, Springer (1989), doi:10.1007/978-3-662-21717-7; reissued CUP (2017), doi:10.1017/9781316717325.
- R. Geroch, J. B. Hartle, "Computability and physical theories", Found. Phys. 16, 533 (1986). doi:10.1007/BF01886519.

**Physical Church–Turing thesis and hypercomputation**
- G. Kreisel, "A notion of mechanistic theory", Synthese 29, 11 (1974). doi:10.1007/BF00484949.
- M. Davis, "Why there is no such discipline as hypercomputation", Appl. Math. Comput. 178, 4 (2006). doi:10.1016/j.amc.2005.09.066.
- G. Piccinini, "The physical Church–Turing thesis: modest or bold?", BJPS 62, 733 (2011). doi:10.1093/bjps/axr016.
- P. Arrighi, G. Dowek, "The physical Church–Turing thesis and the principles of quantum theory". arXiv:1102.1612.
- D. Deutsch, A. Ekert, R. Lupacchini, "Machines, logic and quantum physics", Bull. Symb. Logic 6, 265 (2000). arXiv:math/9911150; doi:10.2307/421056.
- M. Hogarth, "Does general relativity allow an observer to view an eternity in a finite time?", Found. Phys. Lett. 5, 173 (1992). doi:10.1007/BF00682813.
- J. Earman, J. Norton, "Forever is a day: supertasks in Pitowsky and Malament–Hogarth spacetimes", Phil. Sci. 60, 22 (1993). doi:10.1086/289716.
- G. Etesi, I. Németi, "Non-Turing computations via Malament–Hogarth space-times", IJTP 41, 341 (2002). arXiv:gr-qc/0104023.
- W. D. Smith, "Church's thesis meets the N-body problem", Appl. Math. Comput. 178, 154 (2006). doi:10.1016/j.amc.2005.09.077.
- S. Aaronson, J. Watrous, "Closed timelike curves make quantum and classical computing equivalent", Proc. R. Soc. A 465, 631 (2009). arXiv:0808.2669; doi:10.1098/rspa.2008.0350.
- S. Aaronson, "Quantum computing, postselection, and probabilistic polynomial-time", Proc. R. Soc. A 461, 3473 (2005). arXiv:quant-ph/0412187; doi:10.1098/rspa.2005.1546.

**Gödel, physics and the simulation hypothesis**
- S. Aaronson, "Why philosophers should care about computational complexity", in *Computability: Turing, Gödel, Church, and Beyond* (MIT Press, 2013), pp. 261–327. arXiv:1108.1791.
- T. Franzén, *Gödel's Theorem: An Incomplete Guide to Its Use and Abuse*, A K Peters (2005). doi:10.1201/b10700.
- J. D. Barrow, "Gödel and physics". arXiv:physics/0612253.

**Already in the paper, but should be used in Sec. 6:** 't Hooft 2016 §5.8 (`tHooft2016cellular`), for Issue 10.

**Search note on "literature explicitly relating complexity to the simulation hypothesis".** Beyond what the paper already covers (Aaronson 2017 blog, Bostrom FAQ, Wolpert 2025, Vazza, Neukart, 't Hooft), a web search found only non-peer-reviewed material: substack essays, PhilArchive preprints by B. James, and a ResearchGate item. The report's statement that no peer-reviewed paper uses complexity hardness to argue *for* the hypothesis is consistent with what I found. I found no blog post by Aaronson on Faizal et al. and I recommend that the paper not suggest one exists.

---

## 4. Spot checks performed

| Claim (location) | Source checked | Result |
|---|---|---|
| Troyer–Wiese reduction, footnote 9, "generic", τ ∝ e^{aN}, quantum simulators (`:84–102`) | cond-mat/0408370 full text | Quotations accurate. The paper *itself* notes representation dependence and "local basis change", which the section omits (Issue 6). The footnote implies NP ⊆ BPP (Issue 11). |
| Ringel–Kovrizhin scope (`:111–130`) | Sci. Adv. full text (Europe PMC) | Accurate: bosonic systems, local sign-free QMC, excludes DQMC and cluster algorithms, "most" FQH phases. Also found that it concerns the Euclidean/imaginary-time partition function, and that the authors appeal to BQP-universality (Issue 6). |
| No mention of the simulation hypothesis in R-K | Same | Confirmed. This contradicts `00-introduction.tex:4` (Issue 9). |
| Faizal et al. premises and quotations (`:198–222`) | arXiv:2507.22950v1 pp. 1–8 | Quotations accurate. Found three errors in the paper that the section does not flag: the (S1)/completeness contradiction, Gödel sentences made arithmetic by ℕ ⊨ φ, and the Chaitin misstatement (Issue 7). |
| Redden comment (`:230–236`) | arXiv:2512.11807 | Accurately summarized; two pages; LLM assistance disclosed; weak as a sole source (Issue 7e). |
| Wolpert 2025 (`:250–255`, `:307`) | wolpert2025.txt (J. Phys. Complex. text) | Accurate. Also found Definition 3 (PCT = computability of the evolution function), the explicit deferral of complexity (§9), and the slowdown footnote (Issue 18). |
| Jordan–Lee–Preskill "up to four dimensions" (`:51–53`) | arXiv:1112.4833 §§2.1.3, 4.2.2 | Strong coupling holds only for D = 2, 3; in D = 4 φ⁴ is believed trivial (Issue 5). Ledger is ABSTRACT-only. |
| Lloyd 2002 "strong indication" (`:53–55`) | Ledger C-06-058 | Statement is about locally finite theories; its placement after JLP 2012 is anachronistic (Issue 5). |
| Deutsch 1985 (02:36–45, 06:267–268) | deutsch85.txt §§1, 3 | Accurate, but omits Deutsch's "arbitrarily high but not perfect accuracy" for closed systems (Issue 23). |
| Cubitt et al. Theorem 3 (`:148–152`) | arXiv:1502.04573 | Accurate (‖h‖ ≤ 1, algebraic α(n), gap ≥ 1). The promise version and the 1D extension are omitted (Issue 15). |
| Bernstein–Vazirani containment and oracle claim (`:63–68`) | Ledger (ABSTRACT); standard results | Accurate as far as it goes; needs ADH/Simon/Shor context (Issues 4, 12). |
| Pan et al. numbers (`:71–73`) | Ledger (ABSTRACT); arXiv:2111.03011 abstract | Numbers match the abstract; ABSTRACT-level verification violates CONVENTIONS (Issue 22). |
| Aaronson "Why philosophers..." | arXiv:1108.1791 §§4.1, 5.2 | Contains the asymptotic-versus-finite discussion relevant to Issue 3; not cited anywhere. |
| 't Hooft prediction (02:246–250) | Ledgers C-02-039, C-07-047 | Cross-reference to Sec. 6 is never honoured (Issue 10). |
| Duplicate press-release keys | 06 and 09 bib files | Confirmed (Issue 33). |
| All items in §3 | arXiv abs meta tags / Crossref API | All resolve to the stated titles. One ID I first tried for Raz–Tal (1805.02145) is *not* their paper; the DOIs given above are correct. |

---

## 5. Priority order for the authors

1. Issue 9: fix the introduction's attribution.
2. Issue 1: reclassify Pour-El–Richards as a T1 result.
3. Issue 7: rebuild the Faizal critique around its internal logical errors.
4. Issue 6: basis dependence and Euclidean-only scope of the sign-problem results.
5. Issues 3 and 4: asymptotics and the modern evidence on quantum advantage.
6. Issue 10: the H-budget test, and honour 't Hooft's cross-reference.
7. Issues 2, 5 and 8: sharpen T1, the scope of Lloyd's theorem, and the "empirical question" wording.
8. The MINOR and NIT issues.

With these changes I would expect the section to be one of the stronger parts of the paper.
