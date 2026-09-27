# Report: 06-complexity (complexity and computability arguments)

## Files
- Ledger: `research/ledgers/06-complexity.md` has 65 claims: 54 FULLTEXT, 11 ABSTRACT, 0 METADATA-only claims, 0 UNVERIFIED.
- Bib: `research/bib/06-complexity.bib` has 37 entries, all cited in the draft. BibTeX test run: 0 warnings.
- Draft: `paper/sections/06-complexity.tex` is about 2,850 words plus one table (`tab:complexity`). A test compile with a minimal two-column `article` preamble gave no LaTeX or BibTeX errors. That is about 4 pages in 10pt two-column `article`; revtex would be denser.
- Labels: `sec:complexity` and the subsections `sec:complexity:{feynman,sign,undecidability,faizal,hypercomputation,resources}`.
- Cross-references used: `sec:philosophy:bostrom` (section 01) and `sec:methodology:unrestricted` (section 09). Both labels exist in the current drafts.

## Framing used in the section
The organizing device is to separate three tasks:
- (T1) executing the dynamics for a finite time;
- (T2) deciding global or asymptotic properties of models;
- (T3) proving all truths of a formal theory.

A simulator must do only T1. Every negative result reviewed concerns T2 or T3, or a restricted algorithm class for T1. For each argument we name the extra premise needed to reach "not simulable".

The resource bounds are stated with the host-physics caveat, attributed to published statements:
- Vazza 2025 abstract;
- Neukart et al. 2022;
- Edge & Brown 2026;
- Bostrom FAQ 2025;
- Wolpert 2025;
- Aaronson 2017 on slowdown.

## Overstatements by press and authors (documented in the ledger)
1. **Ringel & Kovrizhin (2017).** The paper never mentions the simulation hypothesis; we searched the full text. It explicitly excludes nonlocal QMC (determinant QMC, cluster algorithms) from scope. The press nevertheless reported it as follows:
   - PBS NOVA Next (A. Eck, 3 Oct 2017): "Physicists Confirm That We're Not Living In a Computer Simulation" and "impossible to model the physics of our universe on even the biggest computer".
   - UPI (4 Oct 2017): "We're not living in a simulation, scientists confirm". UPI put quotations in the researchers' mouths as "wrote in a paper" ("memory built from more atoms than there are in the universe"; "double the number of processors") that do **not** appear in the Science Advances text or in arXiv:1704.03880. They probably come from the Oxford press release on phys.org, which we could not access.
   - The AFHU (American Friends of the Hebrew University) site reposted the PBS piece on 4 Oct 2017. It is not cited in the draft.
   - Aaronson's blog post (3 Oct 2017) and Bostrom's FAQ (Q12) are the published rebuttals we cite.
2. **Faizal, Krauss, Shabir & Marino (2025).**
   - The paper itself claims the simulation hypothesis is "logically impossible rather than merely implausible" and the universe "definitely not a simulation".
   - The UBC Okanagan press release (ScienceDaily, 10 Nov 2025) says "mathematically impossible" and "the final, definitive answer".
   - By the paper's own wording, the conclusion excludes only Turing-equivalent simulators.
   - The physical identification of Gödel sentences with "black-hole microstates" is asserted without argument.
   - The undecidability results it cites as "empirical backing" are proved by embedding Turing machines in *computable* models.
   - We also noticed an internal inconsistency: the axioms are described as "finite (or at least recursively-enumerable)" and then as "finite".
3. **Troyer & Wiese (2005)** are careful: they give a worst-case result, and a footnote corrects P to BPP. Secondary literature often paraphrases the result as "the sign problem is NP-hard, so fermions cannot be simulated". The draft states precisely what is excluded: a generic polynomial-time solution, unless NP ⊆ BPP. It also notes that the hard instances are low-temperature spin-glass equilibrium tasks that nature itself does not solve efficiently (Troyer-Wiese on autocorrelation times; Aaronson 2005 on relaxation).
4. **Redden (2025)** writes that hypercomputers are unrealizable "due to the Church-Turing thesis". That conflates the mathematical thesis with the physical one, so we did not reproduce it.

## Gaps and items not verified at full-text level
- **Pour-El & Richards (1981)**: the original was not accessible. Elsevier open-archive/S3 returned 403, CORE returned 404, and core.ac.uk is blocked in WebFetch. The characterization ("non-computable weak solutions ... computable initial conditions") is taken from the Perales-Eceiza et al. review, which we read in full, and is attributed to it in the draft. The Weihrauch & Zhong 2002 counterpoint is ABSTRACT-level.
- **Bernstein & Vazirani (1997)**: ABSTRACT only. The full text is a PostScript file with bitmap fonts and no ghostscript was available. The abstract suffices for the claims made.
- **Copeland 2002 "Hypercomputation"** (Minds & Machines) was not accessible because Springer returned a bot wall. We used Copeland's SEP entry "The Church-Turing Thesis" (2023 revision), read in full. Gandy 1980 and Deutsch 1985 are reported only via the SEP.
- **JHAP "Discussion on the Faizal-Krauss-Shabir-Marino Argument about the Theory of Everything"** (jhap.du.ac.ir article_2003): the site is unreachable from our proxy, and its author and content are unverified. We cite only the authors' *Reply* (abstract via INSPIRE 3145749). **Metadata discrepancy:** the DOI registrar record for 10.22128/jhap.2026.3205.1181 carries the Discussion paper's title with Faizal et al. as authors. INSPIRE gives "Reply to 'Discussion ...'", JHAP 6(2) 119–124. We follow INSPIRE and note this in the bib.
- **Faizal et al., published JHAP version**: we read only arXiv v1 (29 Jul 2025) and could not compare it with JHAP 5(2) 10–21.
- **Ringel quote to New Scientist** ("not a scientific question"): this appears in secondary reports (Futurism). New Scientist and Futurism were not reachable. It is UNVERIFIED and not used.
- **Cosmos Magazine article** ("We're not living in a computer simulation!", Oct 2017) and the Oxford/phys.org press release were both blocked and are not cited.
- **Benjamin James** (PhilArchive, "More simulation hypothesis hullabaloo, a refutation redux"; "The Logical and Physical Impossibility of the Simulation Hypothesis") was blocked (403). Not cited; it does not appear to be peer reviewed.
- **Lucas-Penrose critique**: the IEP article by J. Megill was read, but it has no date, so we did not cite it. The draft mentions Lucas-Penrose only as Faizal et al.'s motivation. If a referee wants the standard objections cited, add Feferman 1996 (Psyche) or the IEP entry.
- **Wolpert 2025**: arXiv v5 (Mar 2026) was read, and its title differs from the J. Phys. Complexity title. We did not compare it with the published text.
- **Bostrom FAQ dating**: the page reads "(2025) Nick Bostrom version 2.0". Edge & Brown (2026) cite a sentence mentioning Vazza (2025) as "Bostrom 2008 FAQ". That is an error in the commentary, not ours.
- **Neukart et al. 2022** is an arXiv/SSRN preprint with no peer-reviewed version found. **Redden 2025** is a single-author arXiv comment that discloses LLM assistance with wording. Both are flagged as preprints in the bib.

## Literature searches performed (for "we are not aware of" statements)
- INSPIRE: `refersto:recid:2955837` (papers citing Faizal et al.) returned 5 records, including the JHAP Reply and a PRD paper by the same group. INSPIRE title searches for "simulation hypothesis", "simulated universe" and "living in a simulation" returned 12 records; none has a new complexity argument beyond those covered (Vazza, Neukart).
- arXiv full-text search for "simulation hypothesis" returned 19 hits; we filtered them for complexity, computability, undecidability and Turing terms. Relevant: 2212.04921 (Neukart). Others were off-topic (algorithmic idealism, the "how many simulations" note, etc.).
- Web searches:
  - "computational complexity argument simulation hypothesis";
  - "Faizal Krauss response rebuttal";
  - "Ringel Kovrizhin not living in a computer simulation";
  - "Vazza commentary".
- We found **no peer-reviewed paper that uses complexity-theoretic hardness (e.g. BQP vs BPP, sign-problem hardness) to argue *for* the simulation hypothesis**. The only formal CS-theory treatment is Wolpert 2025 (J. Phys. Complexity), which argues for *logical possibility* (self-simulation via Kleene) under the physical CT thesis. The draft does not make a "we are not aware" claim about pro-simulation complexity arguments. Section 09 may want one, and this search supports it.

## Suggested cross-links
- **Section 01 (philosophy)**: Bostrom's ancestor-simulation estimates, the FAQ "comprehensive simulation" point, and Edge & Brown's scope objection to Vazza. Section 01 already uses `Bostrom2025simulation`, with a different `url` (faq.pdf); the key is the same.
- **Section 02 (digital physics)**: Lloyd 2002 bounds and Vazza 2025. The shared keys `Lloyd2002computational` and `Vazza2025astrophysical` are consistent across topics.
- **Section 05 (holographic)**: Aaronson 2005's use of the holographic bound against analog and hypercomputation.
- **Section 07 (rendering)**: Bostrom's "fill in detail as needed", which the resource argument depends on.
- **Section 09 (methodology)**: the unrestricted-hypothesis/testability trade-off (`sec:methodology:unrestricted`) and press-distortion examples (Ringel-Kovrizhin, Faizal et al.). Section 09 uses the key `Aaronson2005np`, and we renamed ours to match; it also uses `Wolpert2025what`, which is identical.

## Things that could embarrass us (and how the draft avoids them)
- The draft never says "the universe is/is not a simulation". It says that no reviewed result rules the hypothesis in or out.
- "NP-hard" is always qualified as worst-case, with the BPP refinement.
- Ringel-Kovrizhin is described as ruling out *local sign-free QMC* for specific bosonic phases, with the authors' own caveats quoted.
- The ECT's failure is presented as conjectural (BV: BQP ⊆ P^#P), and the quantum-advantage evidence as provisional (Pan et al. 2022).
- Lloyd's claim that quantum gravity is efficiently simulable is flagged as an expectation.
- Wolpert 2008 is characterized as a limit on *embedded* inference devices, marked as our reading.
