# Referee report: philosophy of science, philosophy of physics, formal epistemology

**Manuscript:** "Testing the Simulation Hypothesis: A Critical Review of Arguments, Proposed Signatures, and Empirical Constraints" (draft of 27 Sep 2026)

**Sections reviewed in depth:** `00-abstract.tex`, `00-introduction.tex`, `01-philosophy.tex` (§2 in the PDF), `02-digital-physics.tex` (§3), `09-methodology.tex` (§4), `10-discussion.tex` (§11). I skimmed §§5–10 for context and to check that the abstract and introduction match them.

**Reviewer's field:** philosophy of science, philosophy of physics, formal epistemology (anthropics, self-locating belief, confirmation theory).

---

## Summary judgement

The survey of the philosophical literature (§2) is careful. Its quotations are accurate: every one I checked against the source matched. It is more even-handed than most treatments of the topic, and the digital-physics genealogy (§3) is useful and well sourced. The weak point is the methodological framework (§4), which is also the paper's headline thesis. It treats the unrestricted hypothesis inconsistently: "not empirical", "likelihood ratio unity", Carroll category 1 and "confirmable by disclosure" cannot all hold. It mistakes the existence of a degenerate rival for the absence of confirmation. It misreports Bostrom's stated view on testability. It overlooks a peer-reviewed philosophy-of-science paper (Greene 2020, *Erkenntnis*, already cited in §2) that argues against the paper's own thesis. The introduction also commits, in its first paragraph, the misattribution the paper criticises in the press. All of this can be fixed, and the fixes would make the thesis stronger, not weaker.

**Recommendation: major revision.**

Counts: FATAL 0, MAJOR 11, MINOR 12, NIT 5.

---

## Issues

### 1. MAJOR — The unrestricted hypothesis is characterised inconsistently, and "confirmable but not disconfirmable" is false in the paper's own Bayesian framework

**Location:**
- `00-abstract.tex:1` ("cannot be refuted by any observation. Only conjunctions … can be tested")
- `00-introduction.tex:14` ("The unrestricted hypothesis is not an empirical claim")
- `09-methodology.tex:100-107` ("Their likelihood ratio is unity for every possible observation")
- `09-methodology.tex:109-116` ("can therefore in principle be confirmed by a cooperative simulator, but it cannot be refuted")
- `09-methodology.tex:317-320`

**What is wrong.** The paper makes four claims about $H_{\rm SIM}$:
- (a) it is "not an empirical claim";
- (b) its likelihood ratio against $\neg H_{\rm SIM}$ is unity for every possible observation;
- (c) it belongs in Carroll's category 1;
- (d) it can be strongly confirmed by disclosure (source code, a message in the CMB).

Claim (d) contradicts (a) and (b). In the relevance-confirmation framework the paper adopts from Crupi (09:47-55), if some $e$ has $P(e\mid H)\gg P(e\mid\neg H)$, then $H$ has empirical content. Conservation of expected evidence then forces $\neg e$ to lower $P(H)$:

$P(H)=P(H\mid e)P(e)+P(H\mid\neg e)P(\neg e)$.

So "confirmable but not disconfirmable" is false. What survives is "not *conclusively* refutable". Almost no theoretical hypothesis is conclusively refutable (Duhem), so that alone does not distinguish $H_{\rm SIM}$.

The "likelihood ratio unity" claim (09:103) holds only for the sub-case "a perfect, non-disclosing simulation of $T$". The unrestricted $H_{\rm SIM}$ is a mixture over designs:

$P(e\mid H_{\rm SIM})=\sum_i P(e\mid H_{\rm SIM}\wedge A_i)\,P(A_i\mid H_{\rm SIM})$.

Table 1 of the paper exhibits $A_i$ whose likelihoods differ from those of $\neg H_{\rm SIM}$. Hence a null result for H-grid does disconfirm $H_{\rm SIM}$, by an amount set by the prior weight $P(A_{\rm grid}\mid H_{\rm SIM})$. This is the correct formal content of the paper's slogan "constraining simulator designs", and it is more defensible than "not empirical".

**Evidence.**
- The paper's own 09:109-116 (Chalmers: "very strong evidence"; Hsu–Zee).
- Bostrom FAQ Q11 (sa_faq.txt l.370-371): "the simulation hypothesis is clearly empirically testable in the sense that there are possible observations we might make that would either increase or decrease the probability that it is true."

**Suggested fix.**

Abstract. Replace "We argue that the unrestricted hypothesis cannot be refuted by any observation. Only conjunctions … can be tested." with:
> "We argue that no observation can conclusively refute the unrestricted hypothesis, and that how any observation bears on it is fixed by a prior over simulator designs that nothing constrains. Observations bear on it only through conjunctions with explicit assumptions about the simulator's architecture, resources and adaptivity; a null result disconfirms the unrestricted hypothesis only in proportion to the prior weight on the designs it excludes."

`00-introduction.tex:14`. Replace "The unrestricted hypothesis is not an empirical claim." with:
> "The unrestricted hypothesis cannot be conclusively refuted, and the evidence bearing on it is mediated by assumptions about simulators for which there is no independent evidence."

`09-methodology.tex:103-105`. Replace "Their likelihood ratio is unity for every possible observation. $H_{\rm SIM}$ is thus …" with:
> "For this sub-case the likelihood ratio is unity for every observation. The unrestricted $H_{\rm SIM}$ is a mixture over this case and over imperfect, disclosing or resource-limited designs, $P(e\mid H_{\rm SIM})=\sum_i P(e\mid H_{\rm SIM}\wedge A_i)P(A_i\mid H_{\rm SIM})$, so its evidential behaviour is set by weights $P(A_i\mid H_{\rm SIM})$ that no available evidence constrains."

`09-methodology.tex:115-116`. Replace "cannot be refuted" with "cannot be conclusively refuted; the absence of disclosure disconfirms it only negligibly, because nothing fixes the probability that a simulator would disclose itself".

### 2. MAJOR — Placing $H_{\rm SIM}$ in Carroll's category 1 misapplies Carroll and silently abandons the paper's neutrality

**Location:** `09-methodology.tex:57-68` and `09-methodology.tex:104-107`.

**What is wrong.** Carroll's category 1 is not merely "not refutable". By his own gloss (1801.05016, pp. 4-5), such theories "aren't actually saying anything about the world" and "don't really even have a chance of being true". His examples are Freud, Adler and Marx. His paradigm of a definite but untestable claim is the multiverse, which he places in category 2: it "says something definite … but in such a way that this prediction cannot be directly tested".

The simulation hypothesis makes a definite claim: a computer exists outside our universe. Bostrom (FAQ Q11) lists conceivable observations that would show it (a disclosure window; being "uplift[ed]" into the host reality). By Carroll's own criteria it therefore belongs in category 2.

The paper quotes the "chance of being true" gloss (09:65-66) and then puts $H_{\rm SIM}$ in category 1. It thereby asserts that the hypothesis has no chance of being true, which contradicts "We do not argue for or against the simulation hypothesis" (intro:14). A philosopher referee will notice this immediately.

The disclaimer "Carroll discusses the multiverse, not simulation" (09:106-107) is also inaccurate as worded: the paper cites a Carroll blog post on simulation in §2 (`Carroll2016maybe`).

**Suggested fix.** Replace 09:105-107 with:
> "In Carroll's scheme the unrestricted hypothesis is closest to category 2: like the multiverse, it makes a definite claim (that there is a computer outside our universe) whose decisive tests (access to the host, or a disclosure) are conceivable but not in our control. It is not in category 1, which Carroll reserves for theories that 'aren't actually saying anything about the world'. This placement is our application; Carroll's paper on falsifiability does not discuss simulation."

### 3. MAJOR — "A degenerate rival exists" does not imply "a detection would not confirm simulation"; the underdetermination step proves too much

**Location:**
- `00-abstract.tex:1` ("For every such sub-hypothesis we found, a detection would establish new physics, not simulation")
- `00-introduction.tex:14`
- `09-methodology.tex:159-173`
- `09-methodology.tex:323-327`
- `10-discussion.tex:21` ("A detection would be evidence for discreteness, not for simulation")

**What is wrong.**

*First problem: the pairwise comparison is not the relevant one.* The argument shows only that $P(s\mid H_{\rm SIM}\wedge A)\approx P(s\mid P)$ for one physical rival $P$. Whether $s$ confirms $H_{\rm SIM}$ depends on

$P(s\mid H_{\rm SIM})$ versus $P(s\mid\neg H_{\rm SIM})=\sum_j P(s\mid P_j)P(P_j\mid\neg H_{\rm SIM})$,

that is, on the catch-all. Most non-simulation physics (Lorentz-invariant continuum QFT, causal sets) does *not* predict a cubic anisotropy. Suppose simulators would use hypercubic grids with higher probability than nature without simulators has a hypercubic preferred frame. Then a detection *confirms* $H_{\rm SIM}$, even though $P$ predicts the same signature. The paper's own 09:162-163 concedes that $s$ "would confirm their disjunction". The honest conclusion is that $s$ does not *discriminate* $H_{\rm SIM}\wedge A$ from $P$, and that whether it confirms $H_{\rm SIM}$ turns on priors nobody can estimate. The paper's asymmetric wording ("establish new physics, not simulation") privileges $P$ without argument.

*Second problem: the fallback argument proves too much.* 09:171-173 says: "Even then, contrastive underdetermination allows a non-simulation model to be built that reproduces the feature". If sound, this would show that no evidence ever favours any hypothesis over an ad hoc constructed rival, general relativity included. The SEP entry the paper cites for underdetermination reports the standard objection in the same section (§3.2). Laudan and Leplin (1991) argue that "theories with exactly the same empirical consequences may admit of differing degrees of evidential support". Neither the objection nor the reply appears in the paper.

**Evidence.** SEP "Underdetermination of Scientific Theory" (sep-scientific-underdetermination.txt l.1000-1075), including the quotation from Laudan & Leplin 1991, p. 465.

**Suggested fix.**

Abstract. Replace with:
> "For every such sub-hypothesis we found, the proposed signature is also predicted by non-simulation physics, so a detection would not discriminate simulation from these rivals, and a null result bounds only a class of simulator designs."

`09-methodology.tex:164-168`. Replace with:
> "A detection would establish the content that $H_{\rm SIM}\wedge A$ and $P$ share (for example, discreteness with a preferred frame). It would not discriminate between them. Whether it raised the probability of simulation would depend on how probable the signature is under simulation compared with non-simulation physics as a whole, and we know of no principled way to estimate either quantity."

`09-methodology.tex:171-173`. Delete the sentence, or replace it with:
> "A sub-Planckian scale would favour $H_{\rm SIM}\wedge A$ over quantum-gravity models that tie discreteness to the Planck length. It would still leave open non-simulation models with an independent fundamental length, and whether it favours simulation over those is again a matter of priors."

Cite Laudan & Leplin (1991) where empirical equivalence is invoked (09:41-43, 09:102).

### 4. MAJOR — Bostrom's stated view on testability and empirical content is misreported

**Location:** `09-methodology.tex:116-123`; `01-philosophy.tex:309-311`.

**What is wrong.** 09:116-117 states: "Bostrom himself does not claim empirical content for the unrestricted hypothesis." 01:309-311 says Bostrom holds the hypothesis "testable only in the weak sense that evidence bearing on disjuncts (1) or (2) shifts credence in (3)". Both are contradicted by the FAQ passage the paper cites (Q11).

The 2003 quotation used in 09:120-121 ("chief empirical importance … lies in its role in the trilemma") is followed immediately by: "If we learn more about posthuman motivations and resource constraints … the hypothesis that we are simulated will come to have a much richer set of empirical implications." Quoting the first sentence without the second misleads.

09:121-123 ("The probability assigned to $H_{\rm SIM}$ therefore comes from the prior … and not from data") also contradicts Bostrom 2005 §4, which the paper itself reports correctly at 01:113-115.

**Evidence.**
- FAQ Q11 (sa_faq.txt l.354-379):
  - "There are clearly possible observations that would show that we are in a simulation. For example, the simulators could make a 'window' pop up … Or they could uplift you into their level of reality."
  - "So the simulation hypothesis is clearly empirically testable in the sense that there are possible observations we might make that would either increase or decrease the probability that it is true."
  - "Most theoretical science is of course untestable in that sense, so it is not a useful criterion for whether a theory is worth taking seriously."
- Bostrom 2005, §4 (sa_weathersonreply.txt l.279-285): "The simulation argument relies crucially on non-obvious empirical premises about future technological abilities."

**Suggested fix.**

`09-methodology.tex:116-123`. Replace with:
> "Second, Bostrom holds that the hypothesis is 'clearly empirically testable in the sense that there are possible observations we might make that would either increase or decrease the probability that it is true', citing both direct disclosure and indirect evidence bearing on disjuncts (1) and (2), and he denies that the absence of a decisive experiment is 'a useful criterion for whether a theory is worth taking seriously' [FAQ Q11]. In 2003 he located its 'chief empirical importance' in the trilemma, while expecting 'a much richer set of empirical implications' once more is known about posthuman motivations and resources [Bostrom2003are, §VI]. Our disagreement with Bostrom is therefore not about whether evidence can bear on the hypothesis, but about whether the likelihoods involved can be estimated. The credence assigned to $H_{\rm SIM}$ comes from the simulation argument, whose inputs are empirical premises about computing capacity together with an indifference principle (Sec. 2), not from observations of the kind reviewed in Secs. 5–10."

`01-philosophy.tex:309-311`. Replace with:
> "Bostrom holds that the hypothesis is testable in a probabilistic sense: some possible observations (a disclosure by the simulators) would show that we are simulated, and evidence bearing on disjuncts (1) or (2) shifts credence in (3) [Q11]."

### 5. MAJOR — Calling $H_{\rm SIM}$ "underdetermination of the sceptical, Cartesian kind" contradicts the positions reported in §2, without argument

**Location:** `09-methodology.tex:104-105`, against `01-philosophy.tex:113-115` and `01-philosophy.tex:260-265`.

**What is wrong.** Section 2 reports two positions:
- Chalmers argues that the matrix hypothesis "is not a skeptical hypothesis, but a metaphysical hypothesis".
- Bostrom argues (2005, §4) that the simulation argument "is fundamentally different from traditional brain-in-a-vat arguments".

Section 4 then classifies $H_{\rm SIM}$ as Cartesian-sceptical underdetermination, with no engagement. This is the central philosophical dispute about the hypothesis's status, and the paper takes a side in it without saying so.

**Evidence.** Chalmers 2005 (chalmers_matrix.txt l.158-163): "nothing about this Metaphysical Hypothesis is skeptical … the Metaphysical Hypothesis is analogous to a physical hypothesis, such as one involving quantum mechanics."

**Suggested fix.** Replace 09:104-105 with:
> "Formally, the perfect-simulation case has the structure of Cartesian underdetermination: nothing in experience distinguishes it from $T$. Chalmers [Chalmers2005matrix] and Bostrom [Bostrom2005simulation, §4] argue, however, that it is not a sceptical hypothesis: it leaves ordinary empirical beliefs true and is motivated by empirical premises. On that reading it is a hypothesis about what realizes physical structure, comparable to other metaphysical hypotheses that are empirically equivalent to their rivals. Our methodological conclusions do not depend on which reading is adopted."

### 6. MAJOR — A peer-reviewed philosophy-of-science paper on exactly this question is overlooked, and it argues against the paper's thesis

**Location:**
- `09-methodology.tex:258-263` ("the explicit discussions of testability that we found are physics or computer-science papers, not philosophy of science")
- §4.4 (adaptive simulators)
- §4.6 (reception)
- §4.7 (thesis)

**What is wrong.** Greene, "The Termination Risks of Simulation Science", *Erkenntnis* 85 (2020) 489–509, is a philosophy-of-science journal article. It is already cited in §2, but it is absent from §4. The note `research/notes/09-methodology-report.md` item 6 shows the 09 author could not read it, while the 01 author did.

Greene:
1. discusses the testability of the simulation hypothesis explicitly, including Beane et al.;
2. states the null/positive asymmetry that §4.2 presents;
3. documents the Ringel–Kovrizhin misreporting, including the Eck headline, in fn. 17, well before this paper's reception table;
4. argues, against this paper's thesis, that observed "abnormalities" *can demonstrate* that we are simulated, via a constructive dilemma.

The negative claim at 09:258-263 is therefore false as worded. Point 4 also needs a reply. The reply is available: none of the signatures reviewed is an "abnormality" in Greene's sense, meaning an observation impossible in any basement reality. That is precisely why they are degenerate. Greene's premise 1 also presupposes that we could recognise an observation as being of non-basement reality. Saying this would sharpen the thesis.

**Evidence.** Greene 2020, pp. 504-505 (sa_preston-greene-termination-risks.txt l.818-852):
- "no matter how sophisticated our experiments become, they could never allow us to conclude that we do not live in a simulation"
- "experimental observation of abnormalities can demonstrate that we do live in a simulation … 3. Either way, we live in a simulation."
- fn. 17: "Many news articles reported this as proof our world is unsimulated, with headlines like 'Physicists Confirm That We're Not Living In a Computer Simulation' (Eck 2017)."

**Suggested fix.** Replace 09:258-263 with:
> "Explicit discussions of testability in the peer-reviewed literature include physics and computer-science papers [Beane, Campbell, Vazza, Wolpert] and, in philosophy of science, Greene [Greene2020termination], who argues that experiments can never show that we are not simulated, that observed 'abnormalities' could show that we are, and who already noted the misreporting of Ringel and Kovrizhin. We are not aware of a peer-reviewed article devoted specifically to the falsifiability of the simulation hypothesis."

In §4.3, add a paragraph on Greene's constructive dilemma, stating that no proposed signature is an abnormality in his sense. In §4.6, credit Greene fn. 17 and Bostrom FAQ Q12 as prior observations of the misreporting.

### 7. MAJOR — The introduction and Table 1 present the Holometer programme as a simulation test, which the paper's own §7 denies; this is the error the paper criticises in the press

**Location:**
- `00-introduction.tex:5`
- Table `tab:subhyp`, row H-noise (`09-methodology.tex:150`)
- `10-discussion.tex:9`

**What is wrong.**

*Status of the Ringel–Kovrizhin part.* The draft I first read said "Others have argued that computational complexity or undecidability rules simulation out~\cite{Ringel2017quantized,Faizal2025consequences}". That directly contradicted §4.6, which says the paper "never mentions the simulation hypothesis"; I confirmed zero occurrences of "universe" in its full text. Commit e50c7e6 has since corrected this. Two problems remain in the new sentence:
- It is a comma splice: "Others have argued that … rules simulation out [Faizal], a complexity result … was widely reported as doing so (…), and it has been argued that …".
- "it has been argued" is the construction CONVENTIONS §5 discourages; name Vopson in the text.

*Hogan and the Holometer (not fixed).* Intro:5 still presents the Hogan and Chou papers as physicists' proposals "to test the idea" (interferometric searches for "pixelation"). Section 7 (`05-holographic.tex:12-15, 228-229`) states that "None of the theoretical or experimental papers reviewed here invokes the simulation hypothesis" and that the "pixelated" description "blurs the distinction". I confirmed zero occurrences of "simulat" in arXiv:0712.3419 and arXiv:1512.01216.

*Beane et al.* "They have looked for lattice artefacts" is inaccurate. Beane et al. derived bounds and proposed a search; they performed no search. Section 6 says no search has been published.

*Table 1.* The H-noise row presents a simulation sub-hypothesis for which, by §7's own finding, no simulation-based derivation exists. Only a non-refereed preprint (Neukart et al.) makes the link.

A referee who reads the first paragraph alongside §7 will conclude that the authors repeat the framing they criticise.

**Suggested fix.** Replace the relevant sentences of intro:5 with:
> "Physicists have since proposed ways to test the idea. Beane, Davoudi and Savage derived the artefacts that a simulation on a cubic lattice would imprint on the highest-energy cosmic rays~\cite{Beane2014constraints}, and Campbell et al. proposed quantum-optics experiments to detect a simulator that renders only what is observed~\cite{Campbell2017on}. Interferometric searches for Planckian noise~\cite{Hogan2008measurement,Chou2016first} were designed to test quantum-gravity models, not simulation, but have been described in the press as tests of 'pixelated' space (Sec.~\ref{sec:holographic}). Faizal et al. argue that undecidability rules simulation out~\cite{Faizal2025consequences}; a result of Ringel and Kovrizhin on classical simulability~\cite{Ringel2017quantized} was reported as doing so, although the paper does not address the question (Sec.~\ref{sec:methodology:reception})."

In Table 1, rename the H-noise row to make clear that it is the authors' construction, and change the status cell to begin: "No published derivation from simulator assumptions (Sec. 7); …".

### 8. MAJOR — The anthropics subsection lists positions but does not identify the choice that drives the disagreement (SSA vs SIA / halfer vs thirder); Kipping's 50% is misdiagnosed

**Location:** `01-philosophy.tex:194-199`, `01-philosophy.tex:201-232`, `01-philosophy.tex:249-255`.

**What is wrong.**

*Kipping's 50%.* 01:249 says: "The 50% ceiling comes from the equal-prior assumption, not from data." That is incomplete. Kipping's eq. (17) sets $\Pr(\mathrm{CES}\mid H_S)/\Pr(\mathrm{CES}\mid H_P)=1$: the fact that one exists is treated as uninformative about how many realities there are. That is a halfer/SSA-type choice. Under SIA (which the paper defines at 01:208) or Lewis's location-uniform prior (01:223-224), the likelihood grows with the number of realities or observers, and $H_S$ is strongly favoured. The ceiling therefore depends on the self-locating rule as well as on equal model priors.

*The "different conclusions from one observation" paragraph (01:194-199).* Its main source of disagreement is this same choice. Lewis's preprint equates LU with the thirder answer and HU with the halfer answer, and notes that under HU the effect holds only for small $n$. The paper presents the split as a curiosity when it is the central formal lesson of the literature.

*Missing standard material.*
- the defence of SIA (Dieks 1992; Olum 2002) and Bostrom & Ćirković's reply (2003);
- the typicality critique in physics (Hartle & Srednicki 2007), which Carroll's blog post, cited in the paper, invokes explicitly;
- the measure problem for infinite populations (Arntzenius & Dorr 2017). This is cited by Thomas and mentioned in the ledger, but not in the text.

**Evidence.**
- Kipping arXiv:2008.12254v1, eqs. (17)-(22).
- Lewis preprint (lewis_sim.txt l.315): "The LU distribution corresponds to the answer 1/3—the 'thirder' solution … and the HU distribution to the answer 1/2—the 'halfer' solution."
- Carroll 2016 blog (carroll_blog.txt l.53): "As James Hartle and Mark Srednicki have pointed out, that's a fake kind of humility".

**Suggested fix.**

`01-philosophy.tex:249`. Replace the first sentence with:
> "The 50% ceiling is not a finding. It follows from two choices: equal prior probabilities for $H_S$ and $H_P$, and a likelihood $\Pr(\mathrm{CES}\mid H_S)=\Pr(\mathrm{CES}\mid H_P)$ that treats one's existence as uninformative about the number of realities [eq. (17)]. The second is a halfer, SSA-type choice; under SIA or Lewis's location-uniform prior the same model strongly favours $H_S$."

Add a paragraph to §2.4:
> "How the argument fares depends on the self-locating rule. SSA with Bostrom's reference class yields the indifference step; SIA, defended by Dieks and Olum and rejected by Bostrom, additionally favours hypotheses with many observers like us, which raises credence in (3) [cites]. The opposite verdicts of Kipping and Lewis on the same evidence (Sec. 2.3) reflect this choice. Hartle and Srednicki argue that the typicality assumption behind all such reasoning is itself a substantive hypothesis to be tested, not a default [HartleSrednicki2007]."

### 9. MAJOR — Key critiques are characterised from abstracts only, against the project's own rules, and the verification claim in the introduction overstates

**Location:**
- `01-philosophy.tex:130-132` (Crawford)
- `01-philosophy.tex:146-151` (Beisbart; Summers & Arvan)
- `01-philosophy.tex:225-226` (Richmond 2017)
- `01-philosophy.tex:279-282` (Schwitzgebel; Summers & Arvan)
- `01-philosophy.tex:284-290` (theology cluster)
- `09-methodology.tex:70-76` (Dawid 2013; Ellis & Silk)
- `00-introduction.tex:24` ("Claims we could not verify are excluded from the text")

**What is wrong.** `research/CONVENTIONS.md` §2 says FULLTEXT is "Required for … every characterization of what a paper argues or concludes", and ABSTRACT is acceptable only "for high-level 'X proposed Y' statements". Sentences such as "Summers and Arvan argue that if panpsychism or panqualityism is true, living in a simulation might be possible only as a brain in a vat, which would make simulation unlikely" characterise arguments.

These are five of the roughly fifteen substantive critiques the section covers. Three of them (Summers & Arvan, Schwitzgebel, Crawford) are ones a specialist would expect the review to engage properly. Printing "(abstract-level)" four times in the running text reads as an unfinished draft.

**Suggested fix.**
- Obtain the full texts before submission; all are in mainstream journals: *Ratio*, *AJP*, *PPR*, *Monist*, *Religious Studies*.
- If that is impossible, reduce each to a neutral pointer ("For objections from panpsychism, see [Summers2022two]") and move verification levels to a footnote or supplementary table.
- Revise intro:24 to: "Claims about what a work argues are based on its full text, except for the N works marked in the ledger, for which only the abstract was accessible; for these we report only the thesis stated in the abstract."

### 10. MAJOR — Two "degenerate rival" entries in Table 1 are wrong or unsupported

**Location:** `09-methodology.tex:151` (H-lazy), `09-methodology.tex:154` (H-patch), `09-methodology.tex:164-166`, `09-methodology.tex:215-218`.

**What is wrong.**

*H-lazy.* GRW/CSL collapse rates depend on mass and spatial separation. They do not depend on whether which-path information is "available to an observer", and they predict nothing like the render-on-demand signature. Section 8 (`07-rendering-qm.tex:79-85`) itself stresses that in QM which-path information suppresses interference "whether or not anyone reads it". The observer-dependent rival is consciousness-collapse (von Neumann–Wigner; Chalmers & McQueen, already cited in §8), not GRW/CSL. For the same reason, 09:165-166 ("A detected deviation from linear quantum dynamics would support a collapse-type modification") misidentifies the rival.

*H-patch.* The Uzan passage the paper relies on gives a discriminating consequence: "Any constant varying in space and/or time would reflect the existence of an almost massless field that couples to matter. This will induce a violation of the universality of free fall." A drift with no accompanying violation of the equivalence principle, or a sudden non-dynamical jump (Barrow's "glitches"), would not fit the field-theoretic rival. So H-patch is *not* shown to be degenerate. It is untestable because Barrow gives no magnitudes, rates or timing. This also undercuts the abstract's "for every such sub-hypothesis".

**Suggested fix.**

H-lazy cell. Replace with:
> "Consciousness-collapse models (von Neumann–Wigner; Chalmers–McQueen~\cite{...}), a link noted by the proposers~\cite{Campbell2017on}."

09:165-166. Replace with:
> "A detected observer-dependent deviation from quantum dynamics would support a consciousness-dependent collapse model."

09:215-218. Replace with:
> "Barrow's patching scenario yields qualitative signatures: glitches and drifting constants. Field-theoretic varying-constant models also predict drifts, but tie them to violations of the universality of free fall~\cite{Uzan2011varying}; a drift without such violations, or a discontinuous jump, would not fit them. Because Barrow gives no magnitudes, rates or timing, however, no observation can at present count against the scenario."

Adjust the H-patch status cell to match.

### 11. MAJOR — The headline thesis, as worded, restates the Duhem–Quine point, which holds for every theoretical hypothesis

**Location:** `00-abstract.tex:1`, `00-introduction.tex:14`, `09-methodology.tex:128`, `09-methodology.tex:321-322`.

**What is wrong.** "Only its conjunctions with explicit assumptions … can be tested" is true of general relativity, of the atomic hypothesis and of every theoretical claim. The paper's own §4.1 (holist underdetermination, 09:38-41) says so. A philosopher of science will read the thesis as either trivial or a misunderstanding of holism.

The distinctive and defensible claim is different. For the simulation hypothesis the auxiliaries concern the architecture, resources and *goals* of an unobserved agent, and there is no independent evidence for them. They cannot be fixed independently of the very test that uses them, so the likelihood of any observation under the unrestricted hypothesis is unconstrained. This is Sober's well-known diagnosis of design hypotheses: design hypotheses make predictions only with auxiliary assumptions about the designer's goals and abilities, which must be independently supported. Sober's analysis also gives the paper a non-Popperian account of testability, which it needs; see issue 20.

**Suggested fix.** Replace intro:14 from "Our thesis is methodological." to "(Table~\ref{tab:subhyp})." with:
> "Our thesis is methodological. Like any theoretical hypothesis, the simulation hypothesis yields predictions only together with auxiliary assumptions. What is distinctive is that the auxiliaries it needs concern the architecture, resources and goals of an unobserved agent, for which there is no independent evidence. As with design hypotheses in biology~\cite{Sober2007what}, this leaves the likelihood of any observation under the unrestricted hypothesis unconstrained. We therefore assess conjunctions with explicit auxiliaries. Each such conjunction we found predicts signatures that non-simulation physics also predicts (Table~\ref{tab:subhyp})."

Make the parallel change in the abstract and in §4.7.

### 12. MINOR — The "ad hoc rescue" charge is aimed at no one, and misdescribes Bostrom's adaptivity

**Location:** `09-methodology.tex:190-204`, `09-methodology.tex:210-212`.

**What is wrong.** Bostrom introduced adaptivity in 2003, before any test was proposed. He motivated it independently, by resource economy. In the Popper and Lakatos sense, ad hocness concerns modifications made after a failure and lacking independent support. The paper cites no one who invokes adaptivity to explain away a null result.

The paragraph also sets Hossenfelder's challenge (how could the programmer fix a contradiction in time without prediction) beside Bostrom's answer (rewind and rerun, 09:195) without noting that the answer meets the challenge. It does so at a computational cost.

**Suggested fix.** Replace 09:210-212 with:
> "If adaptivity were invoked specifically to explain away a null result, it would have the structure Popper classed as an ad hoc rescue~\cite{Thornton2026karl}. In Bostrom's argument it is instead motivated in advance by resource economy. The difficulty is therefore not ad hocness but that adaptivity removes the likelihood difference on which any test depends."

After the Hossenfelder sentence, add:
> "Bostrom's rewind option answers this at the price of additional computation, which bears on the finite-resource premise below."

### 13. MINOR — Dawid's "non-empirical confirmation" is misapplied

**Location:** `09-methodology.tex:82-87`.

**What is wrong.** Dawid's non-empirical confirmation consists of observations about the research context: no alternatives found, meta-inductive success, unexpected explanatory interconnections. Bostrom's argument is not of that kind. It is a direct probabilistic argument from empirical premises plus an indifference principle. Saying the literature is "largely non-empirical in Dawid's sense" is a category mistake.

"The no-alternatives argument is plainly unavailable to proponents" rebuts an argument no proponent has made. The NAA also concerns alternatives that solve a scientific problem, not rival explanations of signatures.

**Suggested fix.** Replace 09:82-87 with:
> "The simulation-hypothesis literature is largely non-empirical in the everyday sense, but not in Dawid's technical sense. The arguments for it are probabilistic arguments from empirical premises about computing (Sec. 2), and several arguments against it are a priori or concern in-principle cost (Sec. 8). None of Dawid's three arguments has been offered for it."

### 14. MINOR — §2 opens with a claim that §3 contradicts

**Location:** `01-philosophy.tex:4-5`.

**What is wrong.** "Most scientific interest in whether the universe is a computation goes back to … Bostrom." Section 3 shows that interest in whether the universe *is* a computation goes back to Zuse, Fredkin, Feynman and Wheeler. Section 3's key distinction is precisely between "is a computation" and "run on a computer".

**Suggested fix.** Replace with:
> "Most recent interest in whether our universe is a simulation, as distinct from the older digital-physics thesis that it is a computation (Sec.~\ref{sec:digital-physics}), goes back to a probabilistic argument by Bostrom~\cite{Bostrom2003are}."

### 15. MINOR — The title promises what the thesis denies

**Location:** `main.tex` title.

**What is wrong.** The paper's thesis is that the simulation hypothesis, unrestricted, cannot be tested, and that only restricted sub-hypotheses can. "Testing the Simulation Hypothesis" invites the one-line dismissal "the paper's own conclusion is that you can't".

**Suggested fix.** Retitle to "Can the Simulation Hypothesis Be Tested? A Critical Review of Arguments, Proposed Signatures, and Empirical Constraints", or to "Testing Simulation Hypotheses: …".

### 16. MINOR — The abstract under-reports the paper's strongest finding and over-reports its novelty

**Location:** `00-abstract.tex:1`.

**What is wrong.**
- **Contribution 3 invites a rejoinder.** "The success criteria … contradict standard quantum mechanics" invites the reply "that is what a test of new physics is". The accurate and more damaging findings of §8 (`07-rendering-qm.tex:79-106`) are different: the deviations are not acknowledged by the proposers, and "as written, the protocol has no outcome that counts against the hypothesis".
- **Missing signature class.** The list of signature classes omits the adaptive/patching class (glitches, drifting constants), even though it is a row of Table 1.
- **Credit.** "We argue that the unrestricted hypothesis cannot be refuted" is presented as the paper's own claim. It is a commonplace, found in Chalmers, Greene, Aaronson and Bostrom's FAQ, and should be credited.

**Suggested fix.**

Contribution 3. Replace with:
> "Third, we show that the proposed render-on-demand experiments count as success outcomes that standard quantum mechanics excludes, without saying so, and that as written they have no outcome that counts against the hypothesis."

Signature list. Add ", and adaptive patching (glitches, drifting constants)" to the list.

Credit. Replace "We argue that" with "Building on Chalmers, Greene and others, we argue that".

### 17. MINOR — Open problem 5 is partly solved in work the paper cites

**Location:** `10-discussion.tex:25`.

**What is wrong.**
- Bibeau-Delisle and Brassard already model nested simulations whose resources shrink geometrically with depth. Their eq. (10) is $N_{i+1}(1+C_{\rm Env})=N_i f_{\rm Civ}f_{\rm Ded}R_{\rm Cal}f_{\rm Eff}$, and they obtain the $f_{\rm Eff}$ ceiling (eqs. 15-16).
- Kipping (§2.3) responds to Carroll's resource-decay point.

**Suggested fix.** Replace with:
> "Existing models treat either resources that decrease with depth, in a Drake-style count~\cite{BibeauDelisle2021probability}, or self-location in a fixed hierarchy~\cite{Kipping2020bayesian}, but not both, and none varies the self-locating rule (SSA versus SIA). A model combining these would show which conclusions depend on assuming that the simulator shares our physics and which on the choice of self-locating rule."

### 18. MINOR — The discussion overstates in two places

**Location:** `10-discussion.tex:11`, `10-discussion.tex:43`.

**What is wrong.**
- 10:11, "inconsistent with established physics". Every test of new physics predicts something inconsistent with established physics. The problems §8 identifies are that the inconsistency is unacknowledged, that it is already constrained, and that the protocol has no disconfirming outcome.
- 10:43, "often more strongly than their proponents noted". The paper documents one such case (Beane et al.).

**Suggested fix.**
- 10:11. Replace with: "…are either untested or, as stated, count as success outcomes that standard quantum mechanics excludes, without acknowledging this, and have no outcome that counts against them."
- 10:43. Replace "often" with "in the case of the lattice proposal".

### 19. MINOR — §3 omits the standard philosophy-of-physics literature on discreteness and on the physical Church–Turing thesis

**Location:** `02-digital-physics.tex:47-53`, `02-digital-physics.tex:26-45`, `02-digital-physics.tex:286-304`.

**What is wrong.**
- **Thesis (D).** Thesis (D) is the hinge of the lattice sections. A philosopher of physics would expect:
  - Weyl's tile argument against discrete space and the replies to it (Van Bendegem 1987; Forrest 1995, who argues that discreteness is an empirical question);
  - Hagar's monograph on fundamental length (2014).
- **Thesis (CU) and Deutsch's principle.** These should cite Piccinini 2011 on "modest" versus "bold" physical Church–Turing theses. The paper's (CU)/Deutsch distinction is exactly this one.
- **Thesis (S).** The paper defines (S) as "a computation implemented on hardware that exists outside it". It needs at least a pointer to the implementation problem (Chalmers 1996, "Does a rock implement every finite-state automaton?"). The limited/unlimited pancomputationalism paragraph (02:289-294) raises the issue but does not connect it to (S).

**Suggested fix.** Add one sentence on each point, with the citations listed under "Missing literature" below.

### 20. MINOR — The primary methodological authorities are cited only through the SEP

**Location:** `09-methodology.tex:24-45`.

**What is wrong.** Popper, Lakatos, van Fraassen and Duhem–Quine are cited only via SEP entries. In the section that carries the paper's thesis this will be read as thin. More substantively, Popper's own treatment of purely existential statements as unfalsifiable but verifiable is the confirmable-but-irrefutable asymmetry the paper presents in §4.2. The methodology report (`research/notes/09-methodology-report.md`, item 3) recognises this but leaves it out.

**Suggested fix.**
- Cite *The Logic of Scientific Discovery* for demarcation, and check the section on strictly existential statements before quoting it.
- Cite Lakatos (1978) for the protective belt.
- Cite van Fraassen (1980) for empirical equivalence.
- Cite Quine (1951) for holism.

### 21. MINOR — A promissory note in the limitations section

**Location:** `10-discussion.tex:35` ("We will repeat these searches manually before publication").

**What is wrong.** Referees assess the submitted version. The negative existence claims ("we are not aware of …") are the weakest statements in the paper, as the methodology report itself says.

**Suggested fix.** Run the PhilPapers "Simulation Hypothesis" category search by hand before submission, report it, and delete the sentence.

### 22. MINOR — The H-info row does not name a rival that predicts the same signature

**Location:** `09-methodology.tex:153`.

**What is wrong.** "Information physics within standard physics [Lloyd]" does not predict "new information-thermodynamic laws or effects", so it is not a degenerate rival in the table's sense. The relevant point is different: the proposed laws are not derived from any simulation assumption, and their proposer says the law "is valid regardless of whether the universe is a simulation or not" (09:300-302).

**Suggested fix.** Change the cell to:
> "None needed: the proposed laws are not derived from simulator assumptions, and the proposer states they hold whether or not the universe is simulated~\cite{Ferreira2023mind}."

### 23. MINOR — Contribution 2 and open problem 1 need a motivation consistent with the thesis

**Location:** `00-introduction.tex:19`, `10-discussion.tex:21`.

**What is wrong.** By the paper's own analysis (`03-lattice-liv.tex:128-130`), a cubic-anisotropy search is informative only for simulators that are "nonperturbatively improved" with $b^{-1}$ within an order of magnitude of $10^{11}$ GeV, and a detection would not bear on simulation. The paper nonetheless ranks this search first "in order of feasibility". A referee will ask why it is worth doing.

**Suggested fix.** Motivate the search primarily as an untested test of Lorentz invariance with public data. Say explicitly that its bearing on simulation is limited to one fine-tuned design class.

### 24. NIT — Two small misattributions

**Location:** `09-methodology.tex:212-215`; `09-methodology.tex:182`.

**What is wrong.**
- **Rovelli.** Rovelli says each failure "decreases the credibility in the theory, because a positive result would have increased it". The paper's "only when" adds a necessity condition. The condition is correct Bayesian reasoning but it is not Rovelli's statement.
- **Collins et al.** "Collins et al. show" should be "argue". Section 5 (`03-lattice-liv.tex:135-139`) rightly treats the point as a debate with Beane et al.'s symmetry-protection claim.

**Suggested fix.**
- 09:212-215. Reword as: "Rovelli notes that, on a Bayesian view, each failed prediction lowers a flexible theory's credibility 'because a positive result would have increased it'."
- 09:182. Replace "show" with "argue".

### 25. NIT — Stale integration comments will ship in the arXiv source

**Location:** `09-methodology.tex:1-7`.

**What is wrong.** The header comment lists "ASSUMED labels, which the integrator must reconcile". These no longer match the labels in use, and arXiv source is public.

**Suggested fix.** Delete the comment block.

### 26. NIT — Process notes appear in the running text

**Location:**
- `01-philosophy.tex:173-175` (Brueckner)
- `01-philosophy.tex:251-252` (Kipping v1 typos)
- `09-methodology.tex:97-98` ("publisher-authorized excerpt")
- `09-methodology.tex:254-256` (the AMNH debate, "as an event only")

**What is wrong.** These read as lab notes. Pointing out typos in Kipping's preprint in the main text reads as petty. The AMNH debate adds nothing to the argument.

**Suggested fix.**
- Move the Brueckner, Kipping and Nautilus notes to footnotes or to the ledger.
- Delete the AMNH sentence and citation.

### 27. NIT — Tegmark's "specify, not compute" claim is conditional on the MUH

**Location:** `02-digital-physics.tex:268-269`, `02-digital-physics.tex:316-318`.

**What is wrong.** Tegmark (arXiv:0704.0646, §VI B) says computations need only describe the universe, not evolve it, "if the MUH is correct". The paper states it unconditionally in the "Consequences" paragraph.

**Suggested fix.** At 02:268-269, replace "On his account" with "If the MUH is correct, he argues". At 02:318, add "(on the assumption of the MUH)".

### 28. NIT — An unattributed "often presented"

**Location:** `02-digital-physics.tex:4-5`.

**What is wrong.** "The simulation hypothesis is often presented as the latest form of an older idea" is attributed to no one. CONVENTIONS §5 forbids unattributed "it has been argued" constructions.

**Suggested fix.** Cite an instance (for example, Tegmark 2008 §VI A, which groups them), or write "It is natural to view the simulation hypothesis as …".

---

## Missing literature

I verified each item's existence and bibliographic data through Crossref (DOI lookup or bibliographic query) or the arXiv abstract page on 27 Sep 2026. Where I also read the abstract or text, the note in brackets says so. None of these is cited anywhere in `paper/sections/`.

**Confirmation theory and underdetermination (issues 3, 11, 20)**
- Laudan, L. & Leplin, J. (1991). "Empirical Equivalence and Underdetermination." *Journal of Philosophy* 88(9): 449–472. doi:10.2307/2026601. [Also verified via SEP §3.2's report of its argument.]
- Sober, E. (2007). "What Is Wrong with Intelligent Design?" *Quarterly Review of Biology* 82(1): 3–8. doi:10.1086/511656. [Abstract read (OpenAlex): discusses the unfalsifiability criticism and "a conception of testability … that avoids the defects in Karl Popper's falsifiability criterion".]
- Sober, E. (2008). *Evidence and Evolution: The Logic Behind the Science.* Cambridge University Press. doi:10.1017/CBO9780511806285.
- Popper, K. *The Logic of Scientific Discovery.* Routledge (Crossref record: 2005 printing). doi:10.4324/9780203994627.
- Lakatos, I. (1978). *The Methodology of Scientific Research Programmes.* Cambridge University Press. doi:10.1017/CBO9780511621123.
- van Fraassen, B. C. (1980). *The Scientific Image.* Oxford University Press. doi:10.1093/0198244274.001.0001.
- Quine, W. V. O. (1951). "Two Dogmas of Empiricism." *Philosophical Review* 60(1): 20–43. doi:10.2307/2181906.

**Self-locating belief, typicality and anthropics (issue 8)**
- Dieks, D. (1992). "Doomsday—Or: The Dangers of Statistics." *Philosophical Quarterly* 42(166): 78–84. doi:10.2307/2220450.
- Olum, K. D. (2002). "The Doomsday Argument and the Number of Possible Observers." *Philosophical Quarterly* 52(207): 164–184. doi:10.1111/1467-9213.00260. arXiv:gr-qc/0009081.
- Bostrom, N. & Ćirković, M. M. (2003). "The Doomsday Argument and the Self-Indication Assumption: Reply to Olum." *Philosophical Quarterly* 53(210): 83–91. doi:10.1111/1467-9213.00298.
- Hartle, J. B. & Srednicki, M. (2007). "Are We Typical?" *Physical Review D* 75: 123523. doi:10.1103/PhysRevD.75.123523. arXiv:0704.2630. [Carroll's blog post, cited in the paper, invokes this.]
- Srednicki, M. & Hartle, J. (2010). "Science in a Very Large Universe." *Physical Review D* 81: 123524. doi:10.1103/PhysRevD.81.123524. arXiv:0906.0042.
- Dorr, C. & Arntzenius, F. (2017). "Self-Locating Priors and Cosmological Measures." In K. Chamcham et al. (eds), *The Philosophy of Cosmology*, Cambridge University Press, pp. 396–428. doi:10.1017/9781316535783.021. [Cited by Thomas and noted in the paper's ledger, but not in the text.]
- Isaacs, Y., Hawthorne, J. & Sanford Russell, J. (2022). "Multiple Universes and Self-Locating Evidence." *Philosophical Review* 131(3): 241–294. doi:10.1215/00318108-9743809. [Abstract read: gives a systematic framework and theorems for self-locating updating rules; directly relevant to Kipping vs Lewis.]
- Titelbaum, M. G. (2013). "Ten Reasons to Care About the Sleeping Beauty Problem." *Philosophy Compass* 8(11): 1003–1017. doi:10.1111/phc3.12080.
- Neal, R. M. (2006). "Puzzles of Anthropic Reasoning Resolved Using Full Non-indexical Conditioning." arXiv:math/0608592.

**Self-undermining and freak observers (the Birch, Crawford and Thomas material)**
- Carroll, S. M. (2020). "Why Boltzmann Brains Are Bad." arXiv:1702.00850. In *Current Controversies in Philosophy of Science* (Routledge). [Text read: defines "cognitively unstable" theories, which "cannot simultaneously be true and justifiably believed". This is the physics version of Birch's selective-scepticism charge.]
- Dogramaci, S. (2020). "Does My Total Evidence Support That I'm a Boltzmann Brain?" *Philosophical Studies* 177(12): 3717–3723. doi:10.1007/s11098-019-01404-y.

**Sceptical-credence framing (Chalmers's 1% illustration)**
- Schwitzgebel, E. (2017). "1% Skepticism." *Noûs* 51(2): 271–290. doi:10.1111/nous.12129. [In the project bib, but not cited in the text.]

**Philosophy of physics and computation (issue 19)**
- Hagar, A. (2014). *Discrete or Continuous? The Quest for Fundamental Length in Modern Physics.* Cambridge University Press. doi:10.1017/CBO9781107477346.
- Forrest, P. (1995). "Is Space-Time Discrete or Continuous? An Empirical Question." *Synthese* 103(3): 327–354. doi:10.1007/BF01089732.
- Van Bendegem, J. P. (1987). "Zeno's Paradoxes and the Tile Argument." *Philosophy of Science* 54(2): 295–302. doi:10.1086/289379.
- Piccinini, G. (2011). "The Physical Church–Turing Thesis: Modest or Bold?" *British Journal for the Philosophy of Science* 62(4): 733–769. doi:10.1093/bjps/axr016.
- Chalmers, D. J. (1996). "Does a Rock Implement Every Finite-State Automaton?" *Synthese* 108(3): 309–333. doi:10.1007/BF00413692.

**Already cited elsewhere in the paper, but missing from §4 where they matter**
- Greene (2020) *Erkenntnis* (issue 6).
- Chalmers & McQueen, arXiv:2105.02314 (issue 10).
- Arvan (2014), *Philosophical Forum* 45(4): 433–446, doi:10.1111/phil.12043. This is a peer-reviewed philosophy paper arguing that a peer-to-peer simulation hypothesis explains quantum phenomena. §4.5 should note it.

**Lead I could not verify.** Dainton, "On Singularities and Simulations", *J. Consciousness Studies* 19(1–2) (2012). The paper's own ledger lists it as UNVERIFIED, and my OpenAlex and Ingenta searches did not find it. It is the main philosophical paper that argues the simulation argument can be broadened beyond substrate-independence, which bears directly on the Beisbart and Summers–Arvan objections. The authors should obtain it.

---

## Spot checks performed

| # | Claim in paper (location) | Source checked | Outcome |
|---|---|---|---|
| 1 | Ringel & Kovrizhin "argued that computational complexity … rules simulation out" (intro:5, draft as first read) versus "never mentions the simulation hypothesis" (09:293-294) | Europe PMC full text, `rk.txt` | 0 occurrences of "universe". §4.6 is correct. The introduction was wrong; it was corrected in commit e50c7e6 while this review was being written (issue 7). |
| 2 | Hogan 2008 and Chou 2016 as proposals "to test the idea" (intro:5) | arXiv:0712.3419 and arXiv:1512.01216 full text | 0 occurrences of "simulat". **The introduction contradicts §7** (issue 7). |
| 3 | "Bostrom himself does not claim empirical content" (09:116-117); "testable only in the weak sense" (01:309-311) | Bostrom FAQ Q11 (`sa_faq.txt` l.354-379) | **Contradicted.** The FAQ says "clearly empirically testable" and lists direct observations (issue 4). |
| 4 | FAQ Q12 quotes: "crude simulation technique", "could fake the results", philosophical methods "immune" (01:302-305, 319-321) | `sa_faq.txt` l.383-441 | Accurate. |
| 5 | "chief empirical importance … in its role in the trilemma" (09:120-121) | Bostrom 2003 preprint §VI (`sa_simulation.txt` l.558-567) | Quote accurate, but the next sentence ("much richer set of empirical implications") is omitted, which misleads (issue 4). |
| 6 | Bostrom 2005: simulation argument relies on empirical premises and differs from BIV scepticism (01:113-115) | `sa_weathersonreply.txt` l.277-301 | Accurate in §2. It contradicts 09:121-123 and 09:104-105 (issues 4 and 5). |
| 7 | Chalmers 2005: matrix hypothesis "not a skeptical hypothesis" (01:260-265) | `chalmers_matrix.txt` l.142-163 | Accurate. Inconsistent with the §4 classification (issue 5). |
| 8 | Greene: no experiment can show we are not simulated; only a positive anomaly is diagnostic (01:316-318) | Greene 2020 pp. 504-505 (`sa_preston-greene-termination-risks.txt` l.794-852) | Accurate. The same pages discuss testability and the RK misreporting, falsifying 09:258-263 (issue 6). |
| 9 | Carroll's five categories; category 1 has no "chance of being true" (09:57-68) | arXiv:1801.05016 pp. 4-6 | Quotes accurate. The category-1 placement of the simulation hypothesis is inconsistent with Carroll's criteria; the multiverse is his category-2 example (issue 2). |
| 10 | Kipping: Pr(base) = ½ + 1/[2(N_sim+1)]; Bayes factor (λ−1)/λ; λ/N_sim after parity; "too generous" (01:237-251) | arXiv:2008.12254v1 eqs. (17)-(22), (32), §3 | All accurate. Eq. (17) builds in a no-SIA likelihood the paper does not mention (issue 8). The v1 prose slips the paper notes are real (§2.9 and §3 text). |
| 11 | Empirically equivalent theories "cannot be better or worse supported by any possible evidence" (09:41-43) | SEP "Underdetermination" §3.2 (`sep-scientific-underdetermination.txt` l.940-1075) | Quote accurate as a report of van Fraassen's view. The same section presents Laudan & Leplin's rebuttal, which the paper omits (issue 3). |
| 12 | Bibeau-Delisle & Brassard: recursive f_sim bounded by f_Eff "most likely under 50%" (01:190-192) | arXiv:2008.09275 eqs. (10)-(16) | Accurate. Their model already has depth-decreasing resources, so discussion open problem 5 is partly solved (issue 17). |
| 13 | Lewis: result depends on the LU prior, identified with the thirder answer (01:222-224) | Lewis preprint (`lewis_sim.txt` l.315) | Accurate. LU is the thirder answer and HU the halfer answer. |
| 14 | Thomas: the simulation argument establishes only a conditional (01:134-141); Birch: a simulated observer can infer only that at least one ancestor-simulation is possible (01:126-128) | `thomas_simexp.txt` l.56; Birch 2013 (`sa_birch…txt` l.446) | Accurate. |
| 15 | Deutsch's principle and the third-law analogy; Wheeler's "supermachine" and "continuum-based physics, no"; Tegmark's "common misconception" (02:35-45, 170-178, 264-271) | `deutsch85.txt`; `wheeler_jaw.txt` l.160-177; arXiv:0704.0646 §VI B | Accurate. Tegmark's "describe, not evolve" is conditional on the MUH (issue 27). |
| 16 | Wolpert on FHE indistinguishability and "partial answers"; Vazza's "Physics play book" (09:98-101, 243-251) | `wolpert2025.txt` l.1399ff; arXiv:2504.08461 l.598 | Accurate. |
| 17 | Abstract and intro contribution 1: b⁻¹ ≳ 10¹⁶ GeV (Crab, 95% CL); γ→e⁺e⁻ allowed far below 1/b | `03-lattice-liv.tex:113-119` | Supported by the body. |
| 18 | Abstract and intro contribution 3: success criteria contradict QM "by up to 1/2" | `07-rendering-qm.tex:74-106` | Supported. The body's stronger finding (no outcome counts against the hypothesis) is missing from the abstract (issue 16). |
| 19 | "We are not aware of a review that treats all of it together" (intro:7) | Yampolskiy 2023 (`yampolskiy2023.txt`, abstract and introduction) | Yampolskiy explicitly does "not evaluate evidence" and is not a review. The claim survives. |
| 20 | Carroll's typicality critique (01:178-182) | Carroll 2016 blog (`carroll_blog.txt` l.53) | Accurate. Carroll invokes Hartle & Srednicki, whom the paper does not cite (issue 8). |

**Checked and not found missing.** Arvan 2014, Chalmers & McQueen, Pour-El & Richards, and Gandy are already cited in §§7–8, so they are not listed as missing.
