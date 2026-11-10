# Independent review of the lighter-agent question pilot

Reviewed 10 November 2026 by a curriculum/content review agent separate from the generator. This is **AI editorial review**, not human approval. The scope was the two raw 25-question batches, their territory packets, the source register, sibling questions, the current 288-question seed bank and the weaving rubric. The supplemental 288-question expansion remains unintegrated candidate material and is not counted as an accepted seed library.

## Result

**50 generated questions reviewed: 0 accepted, 47 need revision, 3 rejected as semantic duplicates.** Most prompts are useful. Acceptance is held because all source notes omit the exact supplied locator required by the guidelines; this is a shared, repairable provenance requirement. Three candidates also repeat a substantive inquiry already present in their batch. No batch or ledger was changed by this review.

The machine-readable decisions are in `data/weaving-pilot-review.json`, including hashes of the raw batches reviewed. Root/coordinator may record these dispositions explicitly; generating this report does not itself change a question state.

## Evidence boundary

The notes correctly say the questions are newly authored synthesis from design summaries. They do not pretend to quote original questions or establish private facts. I did not verify every underlying primary-source passage for this pilot. The packet locators and curated source summaries can be cited as the actual design basis; complete primary-passage reading must not be claimed retrospectively.

**S1 — shared source-note repair:** S1: Add the relevant exact locator already supplied by the source register/packet to provenance.sourceNotes, while retaining that the worker used a design summary rather than inspected complete primary-source passages. Current generic summaries are honest but do not meet the weaving guideline source-locus requirement.

For S03/S04/S05, use the relevant named section supplied in the register. For T60, identify the relevant original day or the actual broad locator supplied, while saying the worker used the selected summary. For S01/S02/M2, identify the relevant supplied page or sheet/range. If only a broad locator was supplied, say so; do not invent a finer one. U1 means the specific current user brief and its relevant instruction, not measured evidence. Merely appending an unrelated locator is not a repair.

## Per-question dispositions

Each `needs_revision` entry below includes S1. Additional changes are limited to meaningful source, premise or routing issues; no stylistic rewrite is required merely to make a prompt sound different.

### Whole-of-life identity batch T001-B01

| ID | Decision | Specific content assessment or repair |
|---|---|---|
| W-T001-0001 | needs_revision | Keep the occupational-introduction context: it adds a concrete encounter to the broad identity seed. |
| W-T001-0002 | needs_revision | Keep the paired past introductions and the setting/relationship comparison; this elicits an episode rather than a timeless trait. |
| W-T001-0003 | needs_revision | Keep pronunciation, shortening and translation choices: a concrete deepening of seed MVS-01-03, not a merely cosmetic rewrite. |
| W-T001-0004 | needs_revision | Keep the condition in which an otherwise accurate description becomes misleading; avoid turning its answer into a fixed trait. |
| W-T001-0005 | needs_revision | Keep the former-role demands and retained/relinquished parts. Check the operation tag: the prompt does not explicitly examine urge, so either use a more accurate allowed operation or add that distinction deliberately. |
| W-T001-0006 | needs_revision | Keep the present-only non-disclosure route; it provides a practical alternative rather than requiring biography. |
| W-T001-0007 | needs_revision | Keep this explicit time-limited new-group introduction and invitation to ask later; use it as the canonical version instead of 0017. |
| W-T001-0008 | needs_revision | Keep resource-dependent versus continuing identity meaning. Its resource comparison is substantive. |
| W-T001-0009 | needs_revision | Keep the hypothetical support change. Consider a meaning/revision operation instead of an attention-evidence label if no cue comparison is intended. |
| W-T001-0010 | needs_revision | Keep the evidence/context attached to an older record; this is distinct from revising the wording of an introduction. |
| W-T001-0011 | needs_revision | Keep continuity in a setting where a practice is less available. The hypothetical alternative is clear. |
| W-T001-0012 | needs_revision | Keep the boundary for outside accounts. Repair gap wording: it invokes the observer distinction although the listed S04/S05 summaries do not establish that architecture; describe the qualified-meaning connection or obtain an allowed source packet that supports the observer claim. |
| W-T001-0013 | needs_revision | Keep the concrete symbolic cue and its limits. Change observerView from Environment to Participant meaning account and operation to Explain personal meaning; the question asks what feels representative, not what an environment observer can establish. |
| W-T001-0014 | needs_revision | Keep the distinction among changed meaning, outdated wording and narrower conditions; its answer can guide record revision. |
| W-T001-0015 | needs_revision | Keep only if its gap is stated more specifically: specify the stored preference and forbidden inference, so it adds to seed MVS-23-01 instead of becoming another broad remember/avoid question. |
| W-T001-0016 | needs_revision | Keep the forced-category interface dilemma. Change observerView to Participant meaning account unless the task is rewritten to examine the form itself. |
| W-T001-0017 | rejected | REJECT semantic duplicate of W-T001-0007: introducing identity first and delaying disclosure in a new place does not add a materially different inquiry to the more concrete time-limited group example. Preserve this wording only as an alternate phrasing, not another unique question. |
| W-T001-0018 | needs_revision | Keep the recalled or absent respectful-wording encounter and the concrete action that helped; the can-you-recall wording allows no example. |
| W-T001-0019 | needs_revision | Keep the audience/control inquiry, but change operation from Compare resources and resourcefulness to Generate and choose alternatives. Invite a category-level or fictional response rather than requiring the private content itself. |
| W-T001-0020 | needs_revision | Keep the explicitly hypothetical future account. The current depth claims one changed variable while the prompt lists several condition types; ask the respondent to choose one change or use Boundary condition instead. |
| W-T001-0021 | needs_revision | Keep chosen actions alongside surrounding conditions in the timeline; it adds agency evidence rather than merely naming events. |
| W-T001-0022 | needs_revision | Keep the practical correction phrase and if-any option. Gentle is a proposed tone, not a required personality characteristic. |
| W-T001-0023 | needs_revision | Keep the after-encounter revision of an introduction; it is a distinct feedback stage from 0007. |
| W-T001-0024 | needs_revision | Keep the external expectation signal for retiring a label; it differs from 0014 by asking about consequences in an encounter. |
| W-T001-0025 | needs_revision | Keep the participant-designed next question; use it to revise onboarding rather than treating it as proof the helper now understands the person. |

### Teacher purpose and starting knowledge batch T061-B01

| ID | Decision | Specific content assessment or repair |
|---|---|---|
| W-T061-0001 | needs_revision | Keep the familiar-example boundary test of a claimed explanation; it directly examines prior understanding. |
| W-T061-0002 | needs_revision | Keep the competing learner purpose/curriculum sequence and evidence for adapting it; canonical version instead of 0011. |
| W-T061-0003 | needs_revision | Keep the distinction between unfamiliar content and familiar knowledge under another name. |
| W-T061-0004 | needs_revision | Keep the learner method account before another demonstration. If the scenario is hypothetical, use Present or an explicit chosen-past framing rather than automatically assigning Past in its actual conditions. |
| W-T061-0005 | needs_revision | Keep the meaningful-project connection with non-disclosure preserved; it adds a real teaching entry route. |
| W-T061-0006 | needs_revision | Keep the separation of observed response from the teacher explanation. Add describe or imagine so novice teachers without a prior incident have an explicit route; the gap note offers that route but the prompt currently does not. |
| W-T061-0007 | needs_revision | Keep disagreement without forced agreement and an inspectable competing account. |
| W-T061-0008 | needs_revision | Keep readiness as a tentative interpretation with a rival explanation; no validated indicator is claimed. |
| W-T061-0009 | needs_revision | Keep alternative evidence under resource/access constraints; use as the canonical question instead of 0022. |
| W-T061-0010 | needs_revision | Keep prerequisite skill demonstrated without formal terminology. Allow a skill you teach or plan to teach so the question serves the adult trainee as well as an experienced teacher. |
| W-T061-0011 | rejected | REJECT semantic duplicate of W-T061-0002: deciding whether an unexpected learner goal connects to the plan or needs another route repeats the same decision already made more concrete by competing demands and evidence in 0002. |
| W-T061-0012 | needs_revision | Keep the slip-versus-model distinction and a changed-task follow-up; this is a learning interpretation, not clinical diagnosis. |
| W-T061-0013 | needs_revision | Keep two correct methods and peer comparison; the question examines different affordances, not simple correctness. |
| W-T061-0014 | needs_revision | Keep a prediction before demonstration so hindsight cannot replace the earlier idea. |
| W-T061-0015 | needs_revision | Keep the halved-time constraint and deliberate preservation of starting-knowledge evidence. |
| W-T061-0016 | needs_revision | Keep alternative explanations for changed participation across tasks; the observed/personal account boundary is preserved. |
| W-T061-0017 | needs_revision | Keep the learner-owned meaning of an unfamiliar term before teacher translation. This differs from 0003 because the teacher, not the learner, lacks the term meaning. |
| W-T061-0018 | needs_revision | Keep provisional sufficiency and visible uncertainty; no universal mastery threshold is invented. |
| W-T061-0019 | needs_revision | Keep the non-personal route after a learner declines their reason; prior-knowledge evidence can still be gathered. |
| W-T061-0020 | needs_revision | Keep task-conditional handover rather than a fixed label. Add the intended audience/permission boundary to the transfer note before suggesting actual learner information be shared. |
| W-T061-0021 | needs_revision | Keep one controlled reduction of support to test independent capability, with restoration when needed. |
| W-T061-0022 | rejected | REJECT semantic duplicate of W-T061-0009: a usual response route becoming unavailable leads to the same alternative-evidence/equivalent-thinking inquiry as limited access/materials. A future new question could instead test whether two assessment formats are truly equivalent. |
| W-T061-0023 | needs_revision | Keep unfamiliar-context evidence at unit review. It extends the personal transfer seed to a teacher decision about a taught unit and observed learner work. |
| W-T061-0024 | needs_revision | Keep changing a goal after experience without calling it failure; this is a longitudinal revision rather than the initial mismatch in 0002. |
| W-T061-0025 | needs_revision | Keep the retrospective account of what helped and what needed adaptation in a real or explicitly hypothetical project. |

## What the pilot establishes

The worker can produce coherent, practical questions with open premises and no fabricated answers. Whole-of-life prompts invite context, chosen identity and revision. Teacher prompts examine actual starting knowledge, learner choice, evidence, instruction and transfer rather than merely adding “as a teacher” to personal questions. The stream, territorial and enum boundaries are broadly respected. There are no asserted December events, diagnoses, endorsements or private family histories.

Exact lexical checks alone would miss the rejected pairs: their wording differs while the decision and expected evidence remain substantially the same. Semantic review therefore adds a real quality gate. The name-pronunciation prompt usefully deepens the broad name/language seed; the unit-transfer prompt adds a teacher review context. Those are retained rather than mechanically rejected for sharing a topic with a seed.

## Coverage gaps before another batch

- The identity batch is concentrated on introductions and labels. The next batch should explore consequences of identity claims in actual work, conflicting obligations, changed resources and a return after a concrete action. Do not spend another 25 slots paraphrasing preferred self-description.
- The teacher batch covers immediate explanation and starting knowledge well. Later retention, fair assessment of changed conditions, learner-created artefacts, prerequisite sequencing and conflicting evidence from more than one attempt remain useful next gaps.
- Only two territories were piloted. Nothing here establishes coverage of all 100 territories, the proposed 100,000-question atlas or the spatial cognitive architecture as a whole.
- Operation, observer and depth labels need semantic checking, not merely enum validation. The mismatches noted above would otherwise inflate apparent coverage of resourcefulness, environment observation or single-variable counterfactuals.
- SourceNotes need question-relevant locators and limits. Repeating one broad source summary across every question is transparent about origin but weak for tracing a particular design choice.

## Bounded next step

Preserve these raw batches. Record the three duplicate rejections and the 47 revision requests. In one deliberate revision cycle, add relevant packet locators, make the specific premise/routing repairs and retain authored_synthesis status. Review only changed content and its near neighbours, then issue explicit per-ID decisions. Do not silently upgrade generated records to accepted or call this AI review a human-reviewed corpus. The two-cycle limit remains in force.


## Revision review — 10 November 2026

**50 revised questions reviewed: 50 accepted, 0 need revision, 0 rejected for this bounded AI editorial pilot.** This supersedes the first-pass disposition only for the revised file contents identified below. The original batches and first review remain the evidence of what failed and how it was repaired. Accepted means suitable as authored candidate questions under this review scope; it does not mean source-authored wording, human approval, participant validation or complete primary-passage verification.

The full per-ID decisions are in `data/weaving-pilot-revision-review.json`. This report does not itself change the ledger.

| Revised input | SHA-256 |
|---|---|
| weaving-pilot-life-revised.json | `ed90d4c819c629f673e71e932072e732fd1ce986afaf1a3284482c26fc6f5380` |
| weaving-pilot-teacher-revised.json | `d872b9dbc1512a751c821f597b5119feeae2e135d44f981946a278a8f42898fe` |

### Repairs verified

All 50 source notes now reproduce the actual supplied register locators and say the worker used packet summaries and locators, without independently rechecking underlying passages. The notes identify the questions as authored synthesis and assert no participant facts. Broad source locators remain broad: I did not invent narrower passages or treat the summary as proof that the primary document explicitly states each pedagogical idea. Relevant source IDs remain inside the territory packet permissions.

The first-pass metadata and premise repairs are present: the identity meaning/view labels now match their prompts; the outside-account gap no longer misattributes the observer architecture; audience choices have an explicit category-level or fictional route; unknown future conditions use a boundary-condition tag; novice teachers can imagine a lesson or choose a skill they plan to teach; handover now carries audience, permission, purpose and uncertainty limits.

The three rejected duplicates now ask substantively different questions:

| ID | Replacement evidence sought | Distinction checked |
|---|---|---|
| W-T001-0017 | What two potentially conflicting roles each mean without either defining the whole person. | Distinct from joining a group through a contribution (0007) and the seed about chosen, assigned or outgrown roles. |
| W-T061-0011 | How to design a task that reveals knowledge gained outside school without rewarding familiarity with classroom examples. | Distinct from identifying unfamiliar terminology (0003) or checking a prerequisite performed under another name (0010). |
| W-T061-0022 | Whether two response formats actually reveal equivalent reasoning, including evidence that would overturn that judgement. | Distinct from supplying another access route under resource constraints (0009). |

W-T001-0007 was also revised: it now examines contribution-based entry to a shared task and the limits of what others may infer. Its existing introduction transfer note remains usable as an encounter review.

All 50 prompts were read again. Strict key sets, allowed dimension labels, permitted sources and supplied locators were checked across every record. The 50 prompt strings are distinct. Semantic review considered evidence/decision value against sibling questions and the current seed bank; token overlap was used only to surface comparisons, not as proof of novelty. Broad seed questions may legitimately have concrete deepening questions when answering the latter adds a condition, evidence or practical decision.

### Remaining coverage limits

- Only two of 100 territories have this reviewed pilot coverage; 50 accepted candidates do not establish the 100,000-question target or comprehensive source coverage.
- T60 and several register entries supply broad ranges or section collections. More precise question-specific primary excerpts are a priority for later production packets; this pilot does not claim that source passages explicitly teach every authored question.
- The whole-of-life identity batch is predominantly participant-meaning reflection. Other territories must supply environment, attention, action, time, competing accounts and actual transfer coverage; do not manufacture observer variety in identity prompts merely to fill quotas.
- Full-immersion 260–300 delivered wpm, recall, delayed retention, practical ventures and network contribution require further dedicated territories. Their absence from an identity/starting-knowledge pilot is a coverage gap, not a defect in these questions.
- Routing labels are navigation hints. Open or hypothetical examples should be recorded as such even where a Past lens is offered; a one-variable counterfactual requires choosing the named condition at use.
- Future expansion must continue global semantic review. This bounded check found substantive distinctions within the reviewed pilot and relevant existing seeds; it is not proof of unique meaning against an ungenerated 100,000-item corpus.

The next useful improvement is better source packets and trials with actual learners, not another cosmetic revision of these 50 prompts. Use future participant corrections and observed learning outcomes to decide which accepted candidates remain useful, need more precise routing, or should merge.
