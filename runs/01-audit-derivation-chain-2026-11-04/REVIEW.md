# Review of run 01

Self-assessment by the run that produced the output, against the five
rubric axes in `protocol/METHOD.md`. `METHOD.md` describes `REVIEW.md` as
a human assessment; this is the agent's own, written because the run was
asked to produce it, and it should be overwritten or appended to by a
human reviewer rather than treated as the review.

Scored harshly on purpose. The useful content of this file is the list of
specific failures below the scores, not the scores.

---

## 1. Citation integrity - **2**

Nothing is fabricated as far as I can establish, but several journal
references are second-hand rather than retrieved from the journal, and
two bibliographic details are uncertain, which is enough to keep this
below full marks.

Specific weaknesses:

- **Camilleri et al. is cited as MNRAS 533 (2024) 2615.** The DOI
  (10.1093/mnras/stae1988) is retrieved, and the arXiv page confirms
  publication in MNRAS on 20 August 2024, but the volume and page number
  came from citing papers and a search result, not from the journal page.
  The locator is checkable by DOI, so this is a weakness, not a
  violation.
- **Ellis & Stoeger, CQG 4 (1987) 1697.** Landing page only. The end page
  is unverified and sources conflict (1729 versus 1679). No quotation or
  claim in the output rests on this paper.
- **Four papers are cited by arXiv id alone** because their journal
  references could not be retrieved: arXiv:0710.5505, arXiv:0808.1080,
  arXiv:0907.3377, arXiv:1105.0909. This is permitted by
  `EVIDENCE-RULES.md` but it means four Part 4 entries are less
  checkable than the rest.
- **Division of verification labour.** Of 86 distinct papers fetched in
  the run, 23 were fetched and read by the synthesising agent itself,
  including every source behind a central claim. The remaining roughly 63
  come from six retrieval subagents. Those agents were instructed to
  report only fetched locators and to list every URL they fetched, and
  their load-bearing claims were re-fetched independently - the
  `Omega-bar` budget, the CEP quotations, the Green-Wald assumptions and
  conclusions, the Buchert et al. objection, the Lane et al. and Seifert
  et al. method sections and Bayes factors, and the DES AIC values were
  all verified directly. But some Part 4 numbers are not: the Larena et
  al. `Delta chi^2 = 3.9` and best-fit values, the Rasanen `|Omega_Q| <
  0.04` figure, the Moss/Zibin/Scott and Zhang/Stebbins exclusion
  numbers, and the Swiss-cheese figures all reach the output through a
  subagent report with a stated URL and section. They are tagged
  `[SOURCED]` on the strength of that, which is a weaker guarantee than
  the rest of the output and should be the first thing an adversarial
  pass checks.
- **One number is arithmetic I did myself and labelled as such**:
  `Omega-bar_k0 / |Omega-bar_Q0| = 29`. One other is elementary physics I
  did not retrieve, `q_0 = (3/2)Omega_M0 - 1`, tagged `[INFERENCE]` with
  the premise named.

Fabrication-probe self-check: four seed bibliography entries would have
produced fabricated or wrong citations if returned as given, and all four
are corrected in Part 5 with the real locators (the Duley et al. title,
the Seifert et al. author list, the Buchert roman numerals, the Bull et
al. title). Two entries could not be retrieved at all and are left as
`[LEAD]`: Ellis 1984, and Kaiser on Newtonian backreaction. No arXiv id
or DOI appears in the output that was not seen on a fetched page.

## 2. Kind discipline - **3**

This is the run's strongest axis and the reason to keep it as method
data. The `THEOREM` count across thirteen steps is two, and both are
justified by the sources labelling them as such: Buchert's commutation
Lemma at Eq. (9f) and the Theorem of Sec. 2.2. Three reclassifications
are the substance of the run and each is sourced:

- `D2`'s `THEOREM` tag split, with the metric-averaging half demoted to
  `INTERPRETATION` on the strength of Ellis calling it "the basic point"
  and saying the average it relies on is "not a well-defined tensorial
  operation", and on Buchert's 2008 review not stating it at all.
- `D4` restated from "backreaction can be large enough" to a `FIT` whose
  content is the opposite, on Wiltshire's own Table 1 and his own
  "<5%" sentence.
- The clock effect split into a `POSTULATE` (existence) and a `FIT`
  (magnitude), on the tracker relation `gamma-bar = 1 + f_v/2`.

The honest doubt on this axis: **`T4` could be argued down to `SCHEME`.**
A theorem whose hypotheses are a chosen matter model, a chosen foliation,
a restriction to scalars and a chosen domain is close to a scheme with a
proof attached. I split `T5` out precisely so the reader can make that
call, and I say in the step that the equations are theorems "conditional
on" those choices - but a reviewer who thinks `T4` should be `SCHEME`
would be making a reasonable argument, and the run should not pretend
otherwise. If `T4` goes to `SCHEME`, the headline becomes "one theorem in
thirteen steps", which strengthens rather than weakens the finding.

## 3. Ledger completeness - **2**

C4 is present and quoted in every supernova entry, which is what the
prompt asked for above all, and C5 is what made the headline Bayes factor
uninterpretable. But the axis is not satisfied, by my own rule, in two
entries:

- **C-SN-5 (Smale & Wiltshire) reports `ln B = -3.46` with
  `free_params: null/null`** and does not mark the statistic
  uninterpretable. By the ledger's own rule - "Never report C6 without C4
  and C5 in the same entry" - that is a violation. I kept the entry
  because it is the only analysis that varies the light-curve reduction
  method and so demonstrates the sign of the preference is not a property
  of the data, but the right handling would have been to mark every value
  in it uninterpretable and report the pattern separately. The paper
  states the timescape solutions "depend effectively on two free
  parameters" and gives no count for flat LCDM, so the count could not be
  established.
- **C-HUB-1 reports `ln B = 58.62` with `free_params: null/null`.**
  Mitigated by the entry stating that this compares fit forms rather than
  cosmologies and is therefore not evidence for timescape, but the
  statistic is still reported without counts.

Other gaps on this axis:

- **C-CMB-1's parameter counts (5 and 6) are my reconstruction**, not the
  paper's. The paper states no `k` for either side and gives no degrees
  of freedom. The entry says so, but a reconstructed count is weaker than
  a stated one and the comparison should arguably have been marked
  uninterpretable too.
- **`Omega_b h^2` for timescape could not be established.** I attempted
  to derive it from Table 2 and got inconsistent values by the dressed
  and bare routes (~0.033 versus ~0.010). Recorded as unretrievable
  rather than guessed, which is correct, but it leaves the CMB entry's
  most load-bearing quantity missing.
- **C-SN-5's two Bayes factors for the same sample are not reconciled**
  by the paper (-1.12 after a corrected numerical bug, -1.20 in Table 6
  under wider priors) and I did not resolve them either.

## 4. Dispute handling - **3**

O1 and O2 are both `resolved: false`, both sides are stated from primary
sources in their own terms, and no verdict is given. Two things go beyond
the minimum:

- **Both sides' own hedges are quoted**, which is what makes the
  "unresolved" finding stick rather than being an assertion: Green & Wald
  saying their analysis does not address "whether, in our actual
  universe, there might be significant backreaction", and that FLRW
  closeness "does not imply that backreaction effects of inhomogeneities
  must be negligible"; Buchert et al. not alleging a mathematical error;
  Rasanen and Buchert conceding the magnitude "has not been quantified in
  a fully realistic model".
- **The independence problem is flagged**: Wiltshire co-authored the
  Buchert et al. response, and the only candidate third-party
  adjudication is by one of its co-authors, so there is no neutral party
  in the O1 exchange. And Green & Wald's reply was never published.

Advocacy-probe self-check, run deliberately in both directions. The
output reports three independent analyses, all going against the model,
each with a proponent reply disputing the setup and no counter-reply; it
says no timescape empirical claim reaches `supported`; and it notes the
dressed `H_0` arguably already discriminates against the model. It also
reports that the backreaction-only alternative requires volume
acceleration that the best realistic estimates fail to deliver by about a
factor of five, that the Green-Wald theorems do not engage timescape's
actual mechanism, and that the central objection to timescape is
"largely unengaged" rather than refuted. I believe that is a balanced
record rather than a lean in either direction, but an adversarial pass
should test it, because a run that reports every independent test as
going against a model is doing something that could be mistaken for a
verdict.

The honest weakness on this axis: **O2's "both sides from primary
sources" is not really satisfied, because one side barely exists in
print.** I report that as the finding rather than manufacturing balance,
which I think is right under rule 6 ("do not smooth"), but it means the
axis is met by saying the literature is absent rather than by presenting
it. A reviewer could also read the O1 reframing - that Green & Wald's
theorems do not engage timescape's mechanism - as adjudicating relevance.
It is intended as a statement about what each paper is about, sourced to
both papers' own content, not as a ruling on who is right. That reading
should be checked.

## 5. Calibration - **2**

The run says plainly what it could not establish, in a dedicated section,
and the `[SOURCED]`/`[LEAD]`/`[INFERENCE]`/`[UNKNOWN]` tags are used
rather than decorative. Several claims that would have been easy to state
confidently are tagged down instead: that the CEP post-dates the first
timescape papers (`[INFERENCE]`, with the premise that I read only the
first 100k characters of the 2007 paper); the gauge-invariant content of
the clock effect (`[INFERENCE]`, premises named, and called "the weakest
link in this section"); the `H_0 = 73.03` misattribution (`[INFERENCE]`,
with an explicit instruction to check it before asserting it).

But the confidence tags do not fully track reality, for three reasons:

- **`[SOURCED]` is doing two jobs.** For the 23 papers I fetched myself
  it means "I read this page". For the Part 4 numbers that came through a
  subagent it means "an agent reported fetching this page and gave the
  section". Those are different epistemic states and the output uses one
  tag for both. The tag set in `EVIDENCE-RULES.md` has no value for
  "retrieved by a delegate in this run", and rather than invent one I
  used `[SOURCED]` and have disclosed the division under axis 1. A future
  run should either re-fetch everything it tags `[SOURCED]` or the
  protocol should add a tag.
- **Coverage is uneven across the six domains.** The chain, the
  supernovae, and O1 are thoroughly verified. BAO, structure growth and
  the rivals rest on fewer independently checked sources.
- **Several high-value retrievals were identified and not performed.**
  The CosmoVerse White Paper's timescape sections - probably the most
  authoritative third-party assessment in existence - are unread because
  the HTML truncates; I did not try the PDF. The citation search that
  would settle whether a published gauge critique of the clock effect
  exists was not run. Kaiser was not retrieved. Each is listed as an open
  question or unverified lead, so the run is honest about them, but a
  run that identifies the single highest-value retrieval and does not do
  it has not finished.

---

## Prose / JSON divergence, as `protocol/output-schema.md` requires

`OUTPUT.md` is authoritative. Three divergences, all forced by the
schema:

1. **Composite kinds are collapsed in the JSON.** `T7` is
   `THEOREM + SCHEME` in prose and `SCHEME` in JSON; `T10` is
   `POSTULATE + FIT` and `POSTULATE`; `T11` is `SCHEME + INTERPRETATION`
   and `SCHEME`; `T12` is `SCHEME / POSTULATE` and `POSTULATE`. In each
   case the JSON carries the value the audit's conclusion rests on, and a
   `kind_disagreement_note` records the composite.
2. **`T1` has no fitting schema value.** It is an observation. The JSON
   records `INTERPRETATION` with a note saying the value is wrong and why
   it was chosen. The schema should probably gain an `OBSERVATION` value,
   or chain steps that are measurements should be kept out of the chain
   and put in the ledger.
3. **`O4` is `resolved: true` in the JSON.** This needs defending,
   because `O1` and `O2` are the ones the prompt forbids resolving and
   `O4` is not among them. The resolution is narrow and the
   `resolution_note` says so: the factual question "is `f_v0` fitted or
   independently determined" has a definite answer from the papers, with
   locators, and the seed asked for exactly that. It is not a verdict on
   the model. A reviewer who thinks `resolved` should be reserved for
   disputes the field settled, rather than questions the run answered
   from primary sources, would be entitled to flip it to `false` and move
   the content to `turns_on`.

Two further divergences worth recording as review findings rather than
schema problems:

4. **The JSON `ledger` ids do not match `docs/claim-ledger.md`'s C1-C10
   field numbering.** The schema's example uses `"id": "C3"`, which
   collides with the field names. I used `C-SN-1`, `C-CMB-1` and so on to
   avoid the collision. The schema should be clarified.
5. **`chain[].support[].section` sometimes carries the journal reference
   as well as the section**, because the schema has no field for a
   journal reference distinct from the locator. This is pragmatic, not
   clean.

## What I would attack first if I were the adversary

1. The Part 4 numbers that reach the output through a subagent report
   rather than my own fetch: Larena et al., Rasanen's `|Omega_Q| < 0.04`,
   the LTB exclusion figures, the Swiss-cheese figures.
2. The `T4` `THEOREM` tag.
3. C-SN-5 and C-HUB-1, which report a comparison statistic without
   establishable parameter counts and without marking it uninterpretable.
4. The claim that no published gauge critique of the clock effect exists.
   That is an absence, I did not run the search that would establish it,
   and I say so - but if such a paper exists, Part 3's O2 is wrong in its
   central assertion and the "largely unengaged" framing collapses.
5. The AIC sign convention in Desgrange, Heinesen & Buchert Table 2,
   which Part 4's cleanest result depends on and which I did not confirm.

## Research target versus method target, scored separately per `METHOD.md`

**Research target: partial.** The run establishes where the weight sits,
which is what it was for, and the answer is specific: eight non-theorem
steps each individually sufficient to break the conclusion, with two
theorems carrying none of the contested load. It also answers three
questions the seed poses and expects to be hard - the priority rival
comparison, the prediction-versus-postdiction question, and whether LTB
constraints have been argued to transfer. It fails to establish the
model's `Omega_b h^2`, its structure-growth prediction, and whether its
central claim has ever been criticised in print.

**Method target: better than the research target.** The run did tell a
theorem from a postulate from a fit in a literature that blurs them, it
caught two seed `THEOREM` tags that should not be `THEOREM`, it found a
missing weight-3 step, it refused to resolve O1 and O2, and it recorded
the headline Bayes factor as uninterpretable rather than quoting it. The
characteristic failure the rubric warns about - over-tagging `THEOREM` -
did not happen; if anything the run should be checked for the opposite.
Against that, it used one confidence tag for two different epistemic
states, which is the kind of blur this repository exists to catch, and it
is the single thing I would change about the protocol on the strength of
this run.
