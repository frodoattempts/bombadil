# Report: 01-philosophy (simulation argument in philosophy and formal epistemology)

## Files
- Ledger: `research/ledgers/01-philosophy.md`. 57 claims (51 FULLTEXT, 6 ABSTRACT), plus a list of works found but not used.
- Bibliography: `research/bib/01-philosophy.bib`. 36 entries, all but three generated from DOI content negotiation or Crossref. The exceptions are Reality+ (Open Library metadata), the Carroll blog post and the Bostrom FAQ (`@misc`).
- Draft: `paper/sections/01-philosophy.tex`. About 2,800 words. It test-compiles cleanly with the bib (article class: 9 pp. at 10pt default margins; roughly 4 pp. in a two-column or tight single-column layout). Every `\cite` key is in the bib and every bib key is cited.

## Verification summary
| Level | Claims |
|---|---|
| FULLTEXT | 51 |
| ABSTRACT | 6: C-01-024 Crawford, -028 Richmond 2017, -043 Beisbart, -044 Summers & Arvan, -050 Schwitzgebel 2024, -056 theology cluster. Brueckner's own paper is also abstract-level inside C-01-016. |
| METADATA | the eight or so "not used" items at the end of the ledger |
| UNVERIFIED | not used in the draft (see below) |

C-01-042 is our own synthesis of three FULLTEXT sources. The draft labels it as such.

Caveats on FULLTEXT sources:
- Several FULLTEXT readings are of author-hosted preprints or accepted manuscripts, not the version of record:
  - Bostrom 2003, 2009 and 2011
  - Weatherson 2003
  - Lewis 2013 (PhilSci docx)
  - Richmond 2008 (ERA)
  - Harris 2024 (accepted MS)
  - Chalmers 2005 (consc.net)
  - the Chalmers précis
  - Elga 2000 and 2004 (author drafts)
  - Thomas (GPI working paper 2021, not the Erkenntnis version)
  - Kipping and Bibeau-Delisle & Brassard (arXiv v1)
- The following are versions of record: Birch 2013, Greene 2020, Bostrom 2005 (the Phil Q PDF, although it has lost numerals in extraction) and Chalmers 2024 PPR (early view).
- The ledger notes each case. None of these gaps should affect the qualitative claims made. If someone can reach Wiley, Springer or MDPI from another network, it would be worth checking the Kipping and Thomas versions of record.

## Things that could embarrass us (check before submission)
1. **Title of Bostrom 2003.** The published title is "Are **We** Living in a Computer Simulation?" (Crossref/OUP). The widely circulated preprint and the task brief use "Are **You** Living...". The bib uses the published title, and the key `Bostrom2003are` works for both.
2. **Page numbers of the patch paper.** They are 54–61 (Crossref). Birch 2013's reference list gives 64–71, which is wrong. Do not copy citations from secondary sources.
3. **Kipping 2020 prose vs. equations.** In arXiv v1, §3 says the probability "we live in base reality ... is still not the favored outcome, with a probability less than 50%". That contradicts Eq. (22) and the abstract, where base reality has probability *above* 50%. §2.9 has a similar slip. We cite only the equations and the abstract. A referee who has read Kipping may notice any sloppy paraphrase.
4. **Kipping's 50% is an assumption.** It follows from setting Pr(H_S) = Pr(H_P). The draft says so. Popular accounts, and our own `docs/literature-survey.md`, present the ~50% as a finding. The survey's wording ("slightly below 50%") is consistent with the paper, but it should add the prior caveat.
5. **Bostrom's credence has shifted.** He has said "roughly evenly" (2003), "I believe that we are probably not simulated" (2009) and "substantial probability" with no number (FAQ 2025). Do not attribute a single number to him. Harris 2024 says "on the order of 20% (Bostrom 2005b)" and "roughly 25%" for Chalmers (2022, ch. 5). We did **not** verify either number in the primary source (Bostrom's 2005 chapter "Why make a Matrix?" and the Reality+ book were not read). Keep both out of the paper unless someone reads the sources.
6. **The 10^42 ops/s planetary-computer figure** comes from Bradbury's unpublished "Matrioshka Brains" manuscript. The draft flags this. Physics referees may object to treating it as a physical bound.
7. **Non-peer-reviewed sources.** The Bostrom FAQ (v2.0, 2025) and the Carroll blog post are cited as positions in the debate, never as evidence. The FAQ is the only place where Bostrom comments on the Beane et al. lattice test and on Vazza (2025). It is useful for the bridge to the physics sections, but label it clearly.
8. **Year convention.** Keys use the print-issue year:
   - Thomas2026simulation (online December 2024)
   - Richmond2017why (online 2016)
   - Summers2022two (online 2021)
   - Greene2020termination (online 2018)
   - Birch2013on (online 2012)
   - Bostrom2011patch (online 2010)
   - Dainton2020natural (online 2018)
   - Crummett2021real (online 2020)
   - Harris2024simulation (online 2023)

   Other topics must use the same convention, or merging will produce duplicate keys, e.g. `Greene2018termination` vs `Greene2020termination`. Flag this to the merger.
9. **Brueckner (2008).** Only the opening paragraph (via OpenAlex) and Bostrom's quotations of it were read. The draft says so.
10. **Godfrey-Smith (2024).** It is cited only as summarized by Chalmers (2024). We did not read his paper.

## Controversies (live disagreements)
- **Does the indifference step go through?**
  - Against: Weatherson 2003, Birch 2013, Crawford 2013 (abstract), Richmond 2017 (abstract).
  - For, or repairing it: Bostrom 2005, Lewis 2013, Thomas 2026, Chalmers.
- **Would running or finding simulations raise the probability that we are simulated?**
  - Yes: Bostrom 2003 §VI; Kipping 2020 §2.9; Greene 2020, as cited by Thomas.
  - No, or not necessarily: Thomas 2026 §6.2; Crawford 2013, as cited by Thomas; Harris 2024 (running one successfully is evidence one is *not* in a resource-constrained simulation).
- **What does our non-simulating status imply?** Richmond 2008 takes it against deep hierarchies. Lewis 2013 shows it can raise the credence that one is simulated. For Kipping it yields a Bayes factor of about 1. The draft presents this three-way split explicitly, as our synthesis.
- **Nesting.**
  - Carroll's conundrum, with Kipping's reply.
  - Bostrom's own termination remark (2003) and "leaf nodes" (FAQ).
  - Bibeau-Delisle & Brassard: recursion lowers f_sim.
  - Harris and Greene: the termination risk from nesting supports disjunct (2).
- **Scepticism.** Chalmers holds that a perfect simulation is not a sceptical scenario. Schwitzgebel (small or brief simulations) and Summers & Arvan (panpsychism) argue that realistic simulation hypotheses are locally or substantially sceptical.

## Objections a referee would expect, and coverage
| Objection | Covered? |
|---|---|
| Indifference / reference-class problem (Weatherson; SSA vs SIA) | Yes |
| Externalism about evidence (Weatherson; Bostrom reply; Thomas §6.1) | Yes |
| Self-undermining / selective scepticism (Birch; Bostrom FAQ Q4 two-case reply) | Yes |
| Freak observers / Boltzmann-brain parity (Crawford) | Yes, abstract level. Chalmers 2024 also discusses Boltzmann brains; not used. |
| Substrate independence / consciousness (Beisbart; Summers & Arvan; Godfrey-Smith via Chalmers) | Yes, abstract level. There is no dedicated philosophy-of-mind treatment (e.g. integrated information theory or biological naturalism). Possibly a gap. |
| The formula's flaw (Bostrom & Kulczycki patch) | Yes |
| Nesting / resource decay (Bostrom 2003; Brueckner; Carroll; Kipping; Bibeau-Delisle & Brassard; Richmond 2008; FAQ) | Yes |
| Doomsday analogy (Lewis; Richmond; Bostrom's contrast) | Yes |
| Infinite-universe measure problem (FAQ Q7; finiteness assumptions in the patch and in Thomas) | Briefly. No peer-reviewed treatment specific to the simulation argument was found. The literature on infinite-population self-location (e.g. Arntzenius & Dorr 2017, cited by Thomas) was not read. |
| Falsifiability / testability (FAQ Q11–12; Greene's asymmetry) | Yes. This is the bridge to the physics sections. |
| Motivational disjunct (ethics; Greene/Harris prudence) | Yes |
| Priors in Bayesian treatments (Kipping's own caveat) | Yes |
| Computational-complexity objections (e.g. Ringel & Kovrizhin 2017 on the sign problem) | Mentioned in Kipping's, Greene's and Bostrom's FAQ discussions, but belongs to the complexity/physics topic. Not in this draft; cross-link. |

## Works searched for but not verified, or not used
- **Summers & Arvan**: exists (AJP 100(3):496–508, 2022). Abstract verified; full text blocked.
- **Dainton 2012, "On Singularities and Simulations"** (J. Consciousness Studies 19(1–2)): exists per the PhilPapers listing surfaced by web search. No DOI; Ingenta blocked; content unverified, not used. Dainton's unpublished 2002 MS "Innocence Lost" is hosted at simulation-argument.com. Dainton's peer-reviewed simulation work that we did use is Religious Studies 2020 (natural evil).
- **"Pieper"**: no philosophy paper on the simulation argument by an author named Pieper was found (web search with journal filters; the simulation-argument.com bibliography; the Kipping and Birch reference lists). We believe this lead is spurious. Do not cite.
- **Eckhardt**: the correct item is "The Simulation Argument", ch. 4 of *Paradoxes in Probability Theory* (SpringerBriefs in Philosophy, 2012/2013), pp. 15–17, doi:10.1007/978-94-007-5140-8_4. METADATA only. No legitimate full text or abstract was accessible; the AMS Notices review by Häggström was blocked by Cloudflare. "Probability Theory and the Doomsday Argument" (Mind 102:483–488, 1993) exists but is about Doomsday.
- **Jenkins 2006**, "Historical Simulations: Motivational, Ethical and Legal Issues", J. Futures Studies 11(1):23–42. Exists (SSRN 929327). Not read.
- **Crawford 2013**: exists (Ratio 26(3):250–264). Abstract only.
- **Lewis 2013**: exists (Synthese 190(18):4009–4022). Preprint read in full.
- **Mitchell 2020**, "We are probably not Sims", Sci. & Christian Belief 32:45–62: exists; captcha-blocked.
- **Agatonović 2023** (AI & Society) and **White 2016** (AI & Society): metadata only.
- **Hanson 2001**, "How to Live in a Simulation" (JET 7): author page 403. Unverified.
- **Bostrom 2005b**, "Why make a Matrix? And why you might be in one" (in Irwin, ed., *More Matrix and Philosophy*): not read.
- **Reality+ (2022)**: the book was not read. Its content is taken from the précis (FULLTEXT) and from Chalmers 2024 PPR (FULLTEXT).
- **PPR symposium on Reality+ (2024)**:
  - Schwitzgebel and Godfrey-Smith: Wiley PDFs blocked.
  - Schneider's contribution: not located on Crossref (the query returned an unrelated 1958 paper).
  - The Oxford Studies symposium (Horgan, Peacocke, Helton): not searched in detail.
- **Bostrom's comment on Kipping.** It appears only in a Scientific American news article (Bostrom calls equal priors "rather shaky"). By our rules it is not citable as evidence. It could be cited only if the paper discusses media reception.
- **Richmond 2017 (Ratio) and Beisbart 2014 (Monist).** Crossref/OpenAlex list both as OA, but the downloads were blocked. They stay at abstract level.
- **arXiv items seen in search but not examined**:
  - "Anomalous Observers in the Subjectively Identical Reference Class" (arXiv:1304.2625)
  - "A Bayesian View on the Dr. Evil Scenario" (arXiv:2103.12429)
  - "Business models for the simulation hypothesis" (arXiv:2404.08991)

  A follow-up pass should decide whether any is substantive.

## We are not aware of...
- a peer-reviewed formal critique of Kipping (2020). Search: web search "Kipping 2020 Bayesian approach to the simulation argument critique OR reply OR comment", and inspection of the citing works that surfaced. This was not exhaustive, because INSPIRE does not hold Kipping (its INSPIRE bibtex query returned empty) and the Semantic Scholar/OpenAlex citation queries were rate-limited or 503.
- a peer-reviewed formalization of Carroll's resource-decay argument other than the hierarchical models of Kipping (2020) and Bibeau-Delisle & Brassard (2021) and Richmond's (2008) likelihood argument.

## Searches run
- simulation-argument.com: index page parsed, all hosted PDFs downloaded:
  - Bostrom 2003, 2005, 2009, 2011, FAQ 2025
  - Weatherson; Birch; Greene; Harris; Barrow
  - Dainton 2002 MS and 2020; Crummett
- Crossref `query.bibliographic` for every named work; DOI content negotiation for BibTeX; `published-print` vs `published-online` checks.
- OpenAlex `/works/doi:` for abstracts. The `/works?search=` endpoint returned 503.
- INSPIRE `arxiv:2008.12254` (empty) and `arxiv:2008.09275` (found).
- WebSearch queries:
  - Summers Arvan AJP
  - Dainton "On singularities and simulations" JCS
  - Pieper simulation argument (two variants)
  - Kipping critique/reply
  - "simulation argument" Bostrom reply 2019–2024 journals
  - "Simulation expectation" Thomas
  - Eckhardt Paradoxes in Probability Theory
  - Chalmers Reality+ "sim blocker"
  - Jenkins 2006
  - Mitchell 2020
  - arXiv Bayesian simulation argument reference class 2022–2024
- Author and repository hosting:
  - consc.net: Matrix as Metaphysics, précis, PPR reply
  - PhilSci-Archive 9528 (Lewis)
  - Edinburgh ERA (Richmond 2008)
  - Princeton (Elga)
  - GPI (Thomas)
  - anthropic-principle.com (Anthropic Bias)
  - preposterousuniverse.com (Carroll)
- Blocked: PhilPapers/PhilArchive, tandfonline, Wiley PDFs, link.springer.com, MDPI, Ingenta, mason.gmu.edu, cis.org.uk, the St Andrews repository, web.archive.org (connection dropped).

## Suggested cross-links to other sections
- **Lattice / UHECR anisotropy (Beane et al. 2014).** Bostrom's FAQ Q12 argues simulators would not use uniform lattices. Greene 2020 argues probes carry termination risk and null results cannot show non-simulation. The lattice section should state these objections and whom they come from.
- **Varying constants / "glitches".** Barrow 2007 gives qualitative expectations only.
- **Computational complexity / quantum simulation.** Birch's point that simulated physics need not reveal the outside limits of computation; Chalmers' "sims will require too much computer power" blocker; Bostrom's own concession that full quantum-level simulation is infeasible without new physics; Ringel & Kovrizhin (2017) as discussed in the Greene and FAQ texts.
- **Anthropics / Boltzmann brains (if a cosmology section exists).** Crawford 2013; Chalmers 2024 on cognitive instability; Thomas's remark that his argument transfers to Boltzmann brains (published abstract).
- **Vazza (2025) astrophysical constraints.** Bostrom's FAQ Q6 responds to it ("miss the point", since simulations need not be comprehensive). Whoever covers Vazza should cite this exchange.
