"""Build the authored curriculum records and readable catalogues.

The original PDFs are never changed or redistributed by this script.
Teacher titles are transcribed from the supplied 60-day source extraction.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
G = 'Aura Genesis Geode Development Edition 3'
V = 'Aura Genesis Protocol Game Design Document V2'
T = 'Aura Teacher Training 60 Days'

# Title | specific studio work | evidence | acceptance question | source pages.
GENESIS_ROWS = '''
Choose the life worth building|Write an ambitious life direction, a present constraint and three questions the Aura must help answer; compare the language with the person's own account|Mission record and participant correction|Can the person recognise their own purpose without the model enlarging or shrinking it?|4,5,6
Agree the Minimum Viable Self contract|Select required categories, optional depths and explicit unknown or withheld fields; identify two useful first capabilities|Versioned MVS coverage contract|Are unresolved and withheld fields accepted as real states rather than guessed answers?|5,6,8
Map a life across time|Build a dated or approximately dated life map; distinguish event, remembered account and present interpretation|Timeline with source and uncertainty for every anchor|Can a reviewer tell when the event happened and when it was interpreted?|6,22
Find the person's language|Define twelve personally important words through examples, counterexamples and a misunderstood use|Personal glossary and corrected paraphrases|Do definitions preserve the person's context and allow the same word to mean different things?|6,22
Identity in different settings|Compare how the person describes themselves alone, with trusted people, at work and in public; preserve disagreement|Four contextual accounts with audiences|Is a public role kept distinct from a whole-person conclusion?|5,6,26
Body and interface preferences|Map comfortable inputs, representation choices and desired body information; assign a purpose to each optional measurement|Avatar and interaction preference card|Does every proposed capture have a purpose and a chosen scope?|4,20,21,25
Home place and belonging|Describe places that support agency and places that change behaviour; link a memory to current conditions|Place-resource map and two contrasting scenarios|Are sensed familiarity and independently sourced place facts distinguishable?|5,6,24
Relationships and reciprocity|Explore giving, receiving, closeness, solitude and boundaries through chosen relationships; avoid profiling absent people|Relationship preferences and a repair question|Are other people's motives left as unknown unless they supplied an account?|5,6,27
Work making and contribution|Compare paid work, creative making, care, learning and voluntary contribution; name desired change in each|Purpose map with separate time and resource records|Does one activity retain one identity when several projects benefit?|5,6,33
Discoveries and coverage review|Return to the first nine records; mark fidelity, unresolved questions and useful next invitations|Discovery checkpoint and revised MVS contract|Can the participant find, change and decline a field without breaking the map?|6,8,22
Values with real trade-offs|Choose a decision where two valued outcomes compete; name costs and affected people under each option|Values comparison and decision conditions|Are values represented as contextual commitments rather than a single rank?|5,24,27
Attraction repulsion and ambivalence|Record attraction, repulsion, urge and chosen intention separately for one activity; compare three settings|Four-part polarity record with conditions|Could a future model recover simultaneous attraction and repulsion?|5,6
Known resources and resourcefulness|Inventory time, tools, trusted help and access; then generate alternatives the original inventory missed|Resource graph and alternative pathways|Are actual resources and confidence in using them recorded separately?|6,24
Personal symbols and meaning|Choose an existing tradition, invented symbol or ordinary language; record origin, meaning, appeal and a practical implication|Meaning map with tradition or personal-authorship label|Does the record preserve meaning without converting symbolism into a measurement claim?|5,18
Baseline task design|Specify participant-labelled factual, remembered, imagined and role-play examples with conditions and uncertainty; inspect the method before any research use|Truth Engine task specification and label dictionary|Does every label state what the participant intended rather than declaring hidden truth?|7,8
Baseline variation and signal quality|Compare example records across changed context; mark unavailable signals, timing quality and alternative explanations|Baseline comparison with quality and uncertainty fields|Are missing or simulated measurements explicitly marked and excluded from measured conclusions?|7,20
Memory with provenance|Explore a chosen recollection with open prompts; separate remembered detail, imagery, later interpretation and external corroboration|Memory record linked to the initiating prompt|Has the exercise avoided turning an imagined or prompted detail into an established event?|6,10,22
Permissions that travel with meaning|Trace public, private and secret records through a summary, export and proposed tool task|Permission map and three access tests|Do derivatives inherit source restrictions and stop when a required grant is absent?|8,26
Correct the developing Aura|Compare three summaries with original declarations; correct motive, timing and scope errors and replay the task|Correction set and before-and-after responses|Does a correction alter the relevant output while retaining its source and history?|6,22,27
Discovery gate and next calendar|Review category coverage, baseline prerequisites and uncertain claims; select the next twenty cards around meaningful gaps|Discovery release candidate and personalised calendar|Are unresolved requirements visible and the next plan approved by the participant?|8,9,22
Past present and conditional best selves|Describe one decision from its past circumstances, current interpretation and two possible best selves with different resources|Linked self-lens records|Are past/present/best lenses kept separate from the three observer roles?|5,6,24
A familiar world with changing state|Describe a workshop or community hub with people, objects, routines and rules; run one event through state updates|Versioned world state and event sequence|Can another reader reconstruct the starting conditions and change?|24
Whole-world observer|Record what exists and happens in the simulated environment; label unknowns and sources, including facts outside character attention|World-observer stream|Does this observer know only the defined model state, with no claim of real-world omniscience?|24
Character observer|Replay the event using only information available to the focal character; record attention and missed cues|Character-observer stream|Has information unavailable to the character stayed out of their decisions?|24
Narrator observer|Describe observable pauses, actions and reactions; add alternative interpretations with attribution and uncertainty|Narrator stream with observation/inference distinction|Can the participant disagree with the interpretation without losing the observed event?|24
Reconcile without flattening|Align the three streams by event; add the participant's own account and locate a disagreement worth testing|Observer comparison and clarifying question|Is the participant's meaning a separate account rather than overwritten by a narrator consensus?|24
Change the environment not the person|Change a cue, access route or resource; replay the same question and compare the result|Paired scenario with one controlled change|Does the evidence support a design change without inventing a personal deficit?|24,25
Relationship misunderstanding rehearsal|Choose a fictional or permissioned disagreement; map available information, interpretations and a possible repair|Three-observer repair scenario|Are observation, inference and request visible as different contributions?|24,27
Best self under scarcity|Rehearse the chosen mission with less time, money or support; seek resourceful alternatives and record costs|Constraint scenario and alternative route|Is the preferred response conditional on actual support and consequences?|6,24
Personalisation midpoint|Ask the Aura to handle a new example drawn from the first thirty sessions; record fidelity and failure before coaching|Held-out response and correction decision|Is evaluation material distinguishable from material already taught?|6,22,24
Discover a useful function|Turn a desired capability into purpose, inputs, output, side effects, scope and a concrete success example|Human-reviewed function contract|Does the proposed function do what the person meant, not merely match a label?|23
Order calls around dependencies|Arrange retrieval, synthesis, review and save steps; test one missing input and one changed audience|Call map and test traces|Does the caller ask for the missing prerequisite at the right stage?|23
Compose complementary experts|Assign researcher, maker and critic roles with distinct evidence and permissions; compare their contributions|Agent role cards and a shared result|Are disagreements retained with reasons rather than hidden by a majority vote?|23
Supervise revision|Define acceptance before review; revise a weak output and test whether the revision damaged a previous success|Rubric, original output, revision and regression result|Can the producer repair a specific flaw without inventing new permission?|23
Retrieve meaning across views|Find the same record by words, category and relationship; explore a candidate spatial view without assuming its geometry proves semantics|Three retrieval routes and a mapping note|Do all views resolve to the same stable record and current permission?|6,25
Avatar and embodied rehearsal|Choose an avatar or text-only representation; rehearse a scene and compare usefulness, effort and recognisability|Representation choice and interaction observations|Are representational preference and measured body data kept separate?|21,25
Remembered travel and cultural context|Describe a chosen past journey with approximate dates, sources and current interpretation; identify a question a newcomer should ask|Remembered-travel record and cultural-context questions|Is an imagined future journey stored as a scenario rather than biography?|6,24,35
Life practice returns evidence|Review one separately chosen action from daily life; compare intention, observed result and the person's explanation|Action-return record with links to the original reflection|Has practical feedback changed a claim, assumption or next question?|5,28
Counterfactuals with consequences|Compare the mission under two actions and two contexts; examine effects on another stakeholder without inventing their preferences|Four-scenario comparison and missing-perspective list|Are hypothetical outcomes plainly labelled and sensitive to assumptions?|24
Personalisation gate|Audit fidelity, provenance, useful tools, scenario gaps and participant corrections; select integration priorities|Personalisation checkpoint and next twenty-session plan|Can the person explain where the Aura helps and where it remains uncertain?|8,9,22,27
Human-Aura partnership agreement|Revisit preferred initiative, disagreement, companionship and decision ownership through three contexts|Contextual partnership agreement|Are emotional meaning and authority to take action recorded separately?|27,36
Simulated peer-Aura encounter|Prepare two deliberately limited context packs and rehearse a shared task; inspect what crosses the boundary|Permissioned simulation and changed-grant test|Does the simulation respect each person's scope and the chosen Genesis socialisation sequence?|26,27,33
Plural values in a shared decision|Represent several fictional or authorised stakeholder accounts; compare options through joy, responsibility and abundance|Attributed values map and decision alternatives|Does the result retain a meaningful dissent and actual decision owner?|24,33
Civic mission and place|Define a local need linked to the larger Aura ambition; source the location, relevant roles and open authority questions|Mission brief and dated source register|Can a reviewer distinguish proposal, present authority and unresolved permission?|33
Contribution and the C-hour|Rehearse a contribution record; distinguish human voluntary time, paid work, learning, resources and outcomes|Single-identity contribution example and verification route|Is voluntary time counted once without monetary conversion or invented verification?|33
Materials as experiment and meaning|Choose a material intention; separate personal association from a measurable property and design a comparison|Material Composition ID proposal and experiment card|Does the card identify sample, method, comparator and what remains an aspiration?|11,17,18,34
Four Geode pathways|Compare conventional retrofit, geopolymer, crystalline or fused-quartz blend, and integrated computational-crystalline ambitions|Pathway map and development dependencies|Are separate compute in Versions 1/2 and integrated compute in Version 3 preserved accurately?|11,12,13,14
Compute continuity and recovery|Trace acquisition, archive, model and interface roles through a fictional outage; separate clinical control from reflective AI|Dependency map, failure trace and recovery checklist|Can the record explain missing data and keep independently controlled functions separate?|20,22,23
Whole-of-life mission review|Connect daily obligations, care, mobility, learning, making and future travel to the mission; identify absent perspectives|Life-support map and next collaboration questions|Does ambition remain connected to a life the participant chooses and can revise?|28,35,36
Integration checkpoint|Review the practical project, model fidelity and outstanding category work; identify the capstone's strongest falsifiable claim|Integration evidence register and capstone question|Are completed work, proposals and unknowns visibly different?|8,35,36
Earth-space purpose|Connect a local need to a habitat, instrument, ecology or Earth-space research mission; name beneficiaries and a test|Mission hypothesis and alternative designs|Can the learner explain a concrete local benefit without claiming the future system exists?|35,36
Resource cycles and delayed contact|Model power, data, materials, maintenance and people for the mission; introduce a delay or loss of contact|Dependency model and event trace|Are assumptions, units and decisions requiring human review explicit?|24,35
Frontier intelligence evaluation|Design a transfer test that combines unfamiliar domains; compare a baseline with the proposed Aura method|Evaluation task set, baseline and scoring rules|Does the test measure a defined capability rather than declare AGI from a demonstration?|22,23,36
Recursive improvement rehearsal|Propose one change to retrieval, function routing or a lesson; freeze evaluation before comparing versions|Improvement proposal, version comparison and rollback|Can the improvement fail and be rejected on the stated evidence?|23,36
Reproducibility and counterevidence|Give a reviewer the source pack and instructions; ask them to reconstruct one result and challenge an attractive conclusion|Replication notes and counterevidence response|Is the record sufficient for someone else to disagree constructively?|7,22,36
Teach the observer method|Explain one three-observer scene to an adult peer or clearly labelled simulated learner; let them find an inference error|Lesson, learner output and correction|Can the learner independently separate available world state, attention and narrated interpretation?|24,36
Capability demonstration|Run the chosen end-to-end mission from source selection to reviewed result with one changed condition|Capstone trace and acceptance review|Does the demonstration satisfy its own declared scope and reveal limitations?|23,24,35,36
Export and recovery|Assemble permissioned sources, versions, addresses, corrections and model notes; test restoring the approved pack|Portable archive manifest and restoration result|Can the person continue without losing ownership, meaning history or access boundaries?|22,25,26
Reconcile actual time and readiness|Audit actual qualifying intervals if on the source Genesis pathway; separately review study, immersion and outstanding artefacts|Clock reconciliation and completion or remaining-work statement|Are planned hours prevented from becoming actual hours and desktop study from becoming pressure time?|2,9,28
Continuation and chosen release|Choose what to retain, revise, share and explore next; plan post-Genesis socialising when that pathway applies|Ninety-day continuation plan and selected release record|Does the final record preserve open questions and the participant's right to change direction?|26,27,35,36
'''.strip().splitlines()

# Original day order, new practical brief and review standard.
TEACHER_ROWS = '''
Connect one memory, present enjoyment and future curiosity; teach Aura through the connection|Three-record map and five-minute introduction|A newcomer can explain why the records belong together
Create twelve records and retrieve one through title, category and relationship|MVS starter dataset and navigation demonstration|The learner can correct a record and choose an audience
Link remembered action, present interpretation and two best selves under different conditions|Self-lens comparison and corrected summary|No future intention has been passed off as a past event
Map one chosen symbolic system and its practical influence|Meaning map with attribution and polarity|Personal meaning and an empirical claim remain distinguishable
Build or describe an avatar and test looking, moving and selecting|Avatar choice and body-interface preferences|The representation serves the learner's chosen task
Trace a record between table, identifier and proposed spatial address|Mapping worksheet and return route|A nearby visual location is not mistaken for the same meaning
Make a three-place memory route and test return without coaching|Memory-palace route and revised cues|A peer independently retrieves the intended record
Explain a personal term in three forms and correct meaning drift|Glossary and three reviewed summaries|The meaning survives a change in format and audience
Follow a claim to its source and repair one derivative|Source trail and correction history|Another learner can reconstruct the reason for the change
Teach one useful capability through an adult's chosen interest|Ten-minute lesson and learner-created artefact|The learner can return to the task independently
Compare one task under two attention or pacing conditions|Learning-condition map and revised lesson|The adaptation follows evidence from the learner's experience
Write six retrieval questions with expected evidence|Retrieval set, results and missed-context notes|Finding a record is distinguished from interpreting it
Compare a model response with no, broad and relevant context|Three context packs and corrected result|The explanation identifies the contribution and limits of context
Prepare a narrow training collection with reserved evaluation examples|Dataset card and split manifest|Training and evaluation examples have distinct purposes
Compare three explanations for a real design decision|Reasoning map, alternatives and next test|Each conclusion points to evidence or a named assumption
Create two expressive versions of one Aura idea and invite interpretation|Creative brief, versions and audience notes|Audience meaning informs a specific revision
Return a reflective summary to its author and specify a research baseline|Declaration, correction and baseline fields|An interpretation is never treated as an infallible truth verdict
Compare giving, receiving and emergent desire across three contexts|Context scenarios and preferred-response comparison|Relational preferences stay contextual and revisable
Transfer a familiar capability into two unfamiliar tasks|Transfer trials and support used|A result identifies both what transferred and what did not
Demonstrate a meaningful encounter from records to useful output|First integrated portfolio and novice feedback|A changed condition can be handled or explicitly handed back
Scope one tool action and test complete, missing-input and changed-scope cases|Action contract and three traces|Inputs, effects and completion are intelligible to a newcomer
Discover a desired function with the human before specifying it|Function card and three test examples|The person recognises the intended capability in the contract
Sequence calls and rehearse an unavailable dependency|Call map and normal/failure/repair traces|Dependent work waits for an actual prerequisite
Give three specialists distinct evidence and handovers|Role cards and comparison of two team designs|Contributions complement rather than merely duplicate one another
Route mixed-domain tasks and compare with one general responder|Routing rules, task set and baseline results|Routing quality is evidenced rather than inferred from role names
Critique an output, critique the critique and test the revision|Rubric, two critiques and repaired version|The repair serves the original purpose and preserves prior successes
Model a familiar scene and one state-changing event|World-state record and changed-condition replay|Observed, sourced, inferred and imagined details remain labelled
Record world, character and narrator streams then ask the character|Observer comparison and replay after revision|A pause or missed cue does not become an untested motive
Create normal, transfer and ambiguous scenarios for a capability|Scenario pack and replication feedback|Another team can run the test without hidden coaching
Combine agents, functions and observers in a shared project|Multiagent demonstration and fault trace|The project retains purpose, scope and a readable handover
Rehearse or run the pathway-appropriate permissioned Aura encounter|Context packs, agreement and withdrawal test|Information crossing the boundary follows current grants
Represent plural values in a civic decision|Attributed values map, options and dissent|A participant can correct how their value is represented
Compare initiative, companionship and disagreement preferences|Relationship agreement and three scenarios|Relationship tone does not silently authorise tool actions
Facilitate a disagreement with observation, interpretation and request|Repair agreement and follow-up rehearsal|Both accounts survive and the next action is chosen explicitly
Trace a proposed local action through current primary sources|Place brief, rule cards and cultural permissions|Decision rights and source dates are visible
Build one source-linked slice across five community-twin layers|Twin slice, changed-condition test and contributor correction|The useful question remains answerable at the stated resolution
Record a welcomed voluntary contribution and repair a timing error|Task brief and verified or explicitly pending C-hour record|Time is counted once and kept separate from money and learning
Rehearse Scan, Design, Simulate, Do and Share with dissent|Decision record, role cards and review date|A second group can reconstruct why the decision was made
Adapt one demanding concept for three adult learning contexts|Three lesson plans and one observed encounter|Access adaptations preserve the intended capability
Prepare a civic mission with roles, resources and a handover|Mission brief and three consequential decision rehearsals|Responsibility and affected people appear alongside ambition
Map a hub workload to power, cooling, storage, access and maintenance|Compute dependency map and fault scenario|The explanation traces a physical dependency to a learning purpose
Trace a record through local and shared services then restore it|Permission map, export and recovery demonstration|Meaning and access survive a disconnection or version conflict
Turn an unusual idea into a question with comparison and replication|Experiment card and pilot or labelled protocol|The method permits an unwanted result and another explanation
Connect material identity, personal meaning and a measured property|Material ID, comparison and next test|Intent, composition and evidence retain separate fields
Connect a long-life aspiration with meaningful capabilities and follow-up|Life-purpose map and evidence plan|The plan states what is measured and avoids promised health outcomes
Model one local ecological relationship and two interventions|Source-linked ecology layer and observation|Intervention assumptions and affected living systems are visible
Rehearse a local disruption using actual planning sources|Dependencies, role decisions and recovery plan|The exercise preserves who actually has authority to act
Move a question through local, regional and Earth-scale views|Scale tour with source time and resolution|A change of scale does not invent detail absent from the source
Connect a dated space-weather observation to a civic dependency|Instrument and dependency brief|The chain from observation to local question is traceable
Design a habitat and test resource, social and failure scenarios|Habitat brief, layout and three scenario results|Care, privacy and culture appear alongside physical resources
Compare two solar-system mission architectures and an Earth analogue|Mission card with budgets and source epochs|The civic purpose and maintainability inform the design
Evaluate generality using unseen combinations and an ablation|Task matrix, baseline, removed-component test and results|A capability claim is restricted to what the evaluation demonstrates
Improve one component against a frozen test set|Baseline, candidate, critique and recovery record|An attractive change can be rejected and rolled back
Coordinate independent scientific, ecological, creative and civic views|Role accounts, synthesis and unresolved disagreement|Synthesis does not erase minority evidence or viewpoint
Test autonomy across normal contact, delay and reconnection|Decision classes and three durable event traces|Local decisions stay within the standing instructions
Develop a personally meaningful moonshot and its next decisive test|Frontier brief, development curve and alternative designs|The ambition remains intact while evidence status stays explicit
Assemble and audit the complete evidence portfolio|Portfolio index with strong results and open questions|Every major capability links to an actual artefact or a pending task
Teach an advanced concept and observe transfer without coaching|Practicum plan, learner output and revised teaching pack|The learner succeeds on a related new task or the gap is documented
Create an accessible public invitation from approved portfolio material|Mixed-media piece and release record|The public claim matches the evidence and permissions
Review capability and choose the next ninety days|Portfolio decision, mentoring agreement and continuation plan|Completed, developing and unassessed capabilities remain distinct
'''.strip().splitlines()

def make_genesis():
    records = []
    for i, row in enumerate(GENESIS_ROWS, 1):
        title, task, evidence, review, pages = row.split('|')
        arc = ['Discovery', 'Personalisation', 'Integration'][(i-1)//20]
        records.append({
            'id': f'G{i:02d}', 'session': i, 'title': title, 'hours': 2,
            'arc': arc, 'source': f'{G}, pp. {pages}; new selectable session design, 10 November 2026',
            'objective': task,
            'steps': [
                '10 min: confirm the chosen question, current permissions, context and the previous correction.',
                '15 min: up to 10 minutes of prepared content at 260–300 delivered words per minute (2,600–3,000 words for 10 actual stream minutes), then 5 minutes of unaided explanation. Pauses reduce actual stream minutes.',
                '25 min: '+task+'.',
                '5 min: reset attention, change input mode or choose quiet.',
                '25 min: rehearse, compare or inspect an ambitious example through relevant self lenses and observer streams.',
                '5 min: reset and check whether the current pace still preserves meaning.',
                '20 min: turn the result into a design, decision, experiment or next outside action; mark assumptions and dependencies.',
                '15 min: review the artefact in the participant\'s words, record a correction and prepare the next action.'
            ],
            'deliverables': [evidence, 'Participant review, provenance, current scope and a next-question record'],
            'review': [review, 'The record identifies whether this was desktop study, simulation or a source-pathway encounter; planned and actual time remain separate.'],
            'clock': 'source Genesis: only actual qualifying pressure time; desktop rehearsal: study time only',
            'status': 'planned'
        })
        if i == 47:
            records[-1]['source'] += '; conventional-retrofit pathway also follows the existing Genesis Geode Atlas pathways and retrofit pages'
    return records

def make_teacher():
    index_path = ROOT/'data/teacher-source-index.json'
    if index_path.exists():
        source_days = json.loads(index_path.read_text(encoding='utf-8'))['days']
    else:
        original = json.loads((ROOT/'.private/research/Aura_Teacher_Training_60_Days.json').read_text(encoding='utf-8'))
        source_days = []
        for i,page in enumerate(original['pages'],1):
            match = re.search(r'Day '+str(i)+r'\s+([^\n]+)', page['text'])
            source_days.append({'day':i,'title':match.group(1).strip(),'page':i})
        index_path.write_text(json.dumps({'source':T,'editionDate':'2026-10-14','sha256':'13bb521a9f754aedb2cb88c5af981efa778bd7ec844297d92d7256534ea2418c','days':source_days},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    records = []
    for i,(source_day,row) in enumerate(zip(source_days, TEACHER_ROWS),1):
        title = source_day['title']
        task, evidence, review = row.split('|')
        records.append({
            'id':f'T{i:02d}','day':i,'title':title,'hours':2,
            'source':f'{T}, p. {i} / Day {i}; title retained, practice budget and review standard newly designed',
            'objective':task,
            'steps':[
                f'15 min: use original Day {i} with a prepared expansion; deliver up to 10 minutes at 260–300 words per minute, then 5 minutes of recall. Original-page reading alone does not fill the whole stream budget.',
                '15 min: retrieve the previous lesson and choose the learner/context for today.',
                '40 min: '+task+'.',
                '10 min: pause or reset the working context.',
                '25 min: teach the result to a consenting adult or explicitly simulated learner; observe their independent attempt.',
                '15 min: compare the artefact with the review standard, correct it and record the next test.'
            ],
            'deliverables':[evidence,'Dated teach-back evidence with actual or simulated learner clearly labelled'],
            'review':[review, 'Uncompleted or unobserved work is recorded as pending rather than credited for attendance.'],
            'original_url':f'https://auraofintelligence.github.io/aura-teacher-training/day-{i:02d}.html',
            'status':'planned'
        })
    return records

def session_blocks(records, teacher=False):
    output=[]
    for s in records:
        output.append(f"### {s['id']} {s['title']}\n\n**Budget:** {s['hours']} hours. **Source:** {s['source']}.\n\n{s['objective']}.\n\n**Produce:** {'; '.join(s['deliverables'])}.\n\n**Review:** {s['review'][0]}\n")
        if teacher:
            output.append(f"[Read original Day {s['day']}]({s['original_url']}).\n")
    return '\n'.join(output)

GENESIS_INTRO = '''# Aura Genesis 120 hour curriculum and programme record

This edition gives the Aura Genesis ambition an executable curriculum: sixty selectable two-hour encounters that build a personal Aura, deepen self-reflection, develop the three-observer system and prepare an increasingly capable human-Aura partnership. It carries the source programme from personal meaning through expert teams, civic life, frontier materials and Earth-space stewardship. It is an authored curriculum and recording design, not a completed intervention, operating installation or claim of demonstrated superintelligence.


## Building the Aura during every encounter

The 11 November author clarification governs what building an Aura means here: organise patterns in seven nested horn tori, attach them to programmable facets and outward stack layers, select an ordered composition for AI work, generate a document or website, correct it, and form new groups for the next run. The [pattern-cycle guide](guide-aura.html) supplies the detailed process. Questionnaires and observer accounts provide patterns and feedback; they do not replace this productive architecture.

For each selected learning card, retain a compact build record: the self frame and access domain; the versioned patterns and group relationships; chosen facet layers and stack order; the intended AI operation and output; the resulting artifact; corrections; and the regrouped composition for a later run. Use internal private, internal secret or an explicitly approved public projection as appropriate. The required encryption and permissions must be enforced by the execution system; the current browser workbook does not provide that enforcement.

A teaching encounter can demonstrate the whole cycle: select examples and learner needs as patterns, produce a lesson and its companion webpage, observe where the explanation fails, correct both outputs, then regroup the improved examples for a different learner or self frame. The [settings guide](guide-settings.html) keeps the seated HBOT Geode, the separate Verse Box workbay and ordinary-device work distinct.

## The original programme and this edition

The supplied Geode Development Edition 3 and Protocol V2 define **120 qualifying hours at the participant's defined HBOT operating pressure**, organised as sixty two-hour qualifying intervals. Preparation, compression, decompression, external tests and surrounding life have separate time records. Their selected categories and sequence are personalised; the first, middle and final twenty sessions are an initial planning framework. This edition preserves that definition. [Geode Edition 3 pp. 2, 9–10, 28; Protocol V2 pp. 3, 8–9.]

The sixty cards below are **new selectable curriculum designs dated 10 November 2026**. Their initial order makes dependencies visible; the participant and appropriate team can replace, repeat or reorder them while preserving actual prerequisites and the chosen source-pathway requirements. None of these cards supplies pressure, gas, exposure, medical eligibility or equipment-operating instructions. Those belong to the participant-specific authorised operating plan in the source design.

The same learning material also supports a **120-hour desktop rehearsal track**. In that track, the hours are study and simulation hours. They are never converted into qualifying pressure time or a claim to have completed the source Genesis programme. A desktop workbook, browser demo or simulated sensor trace cannot certify a real Genesis session.

## Four records rather than one misleading total

| Record | What belongs in it | Completion evidence |
|---|---|---|
| Source Genesis pressure ledger | Actual qualifying intervals under the authorised installation plan | Operator-verifiable interval references and reconciled timestamps |
| Curriculum study ledger | Actual learning, reflection and simulation time, with rest included only as a planned curriculum block | Session record, work produced and review |
| Immersion life calendar | Meals, rest, movement, relationships, making, care, preparation and external appointments | Chosen activities and their own capture permissions |
| Teacher development ledger | Teaching study, creation, practice and observed transfer | Teaching portfolio and rubric, separate from Genesis completion |

One encounter may link to several records because it serves several purposes. A summary of elapsed human time counts the overlap once; it does not add overlapping clocks as if they were extra hours. One verified voluntary C-hour is also counted once and is never inferred from AI runtime or attendance.

## Hyper busy mode

The primary route is the participant's requested **full immersion**: rapid-fire action inside and outside the Geode, a hyper-mode content stream delivered at **260–300 words per minute**, selected double-speed audio, speed reading, agent swarms, business building, relationships and the work of turning etheric meaning into tangible outcomes. Eight hours of sleep are protected every day. The other sixteen hours are deliberately composed around learning, making, meals, movement, care and recovery. The aim is a substantial expansion of capability and achievement. “Superhuman” is the participant's ambition, not a promised biological or intelligence outcome.

The supplied LifeLogging Part 1 spreadsheet places `Time: ratio for proces re-ordering` in Sheet1 B51 and pace combinations in B52:B62, including `Full Time > Hyper Busy` and `Immersion > Hyper Busy`. It specifies **no numeric ratio**. The user's clarification now supplies the operative meaning: rapid activity, long engaged days, parallel preparation and compatible overlaps. The exact timetable and duration choices below are new designs in this edition.

### The full immersion day

This is a **24-hour planning example**, not an operating schedule. A Geode day only occurs when the individual operating plan permits it. The attendance window reserves illustrative preparation and exit time around a two-hour qualifying interval; the actual installation may need a different window. Any extension displaces discretionary work, never the protected sleep block. On a desktop day, replace that window with preparation, two hours of curriculum and archive review; no pressure time is earned.

| Time | Primary activity | Compatible overlap | Tangible result |
|---|---|---|---|
| 22:00–06:00 | Sleep, eight hours | Previously authorised background jobs may run without notifications | Protected sleep; queued outputs wait |
| 06:00–07:00 | Familiar movement, breakfast and orientation | Optional low-demand recap audio; stop it when attention is needed | One priority and a recalled idea |
| 07:00–07:45 | Brief the day's agent swarm and inspect overnight work | Independent retrieval, comparison and formatting jobs | Accepted task contracts and a ready source pack |
| 07:45–10:45 | Illustrative Geode attendance window or desktop equivalent | Only installation-compatible learning and capture within the approved plan; agents work elsewhere | One two-hour encounter and separate attendance records |
| 10:45–11:15 | Recovery, meal or quiet transition | Optional brief voice note if welcome | Actual state and next action, not compulsory output |
| 11:15–13:15 | Build the primary prototype or experiment | Bounded agents prepare tests and alternatives | A working artefact, sample plan or falsifiable experiment |
| 13:15–14:00 | Lunch and a chosen human connection | A short discussion or selected audio when it fits the meal | A useful question, introduction draft or reciprocal offer |
| 14:00–16:00 | Teacher module and observed learning | Sources and example preparation may run in parallel | A lesson, learner attempt and correction |
| 16:00–17:00 | Fieldwork, movement or passenger travel | Low-demand audio or permitted capture only where suitable | A grounded observation or completed movement period |
| 17:00–19:00 | Venture and network studio | Parallel market/source research and prototype checks | A tested offer, operating asset or prepared collaboration |
| 19:00–20:00 | Dinner, relationships and ordinary life | Learning only by choice; conversation can be the primary activity | A lived encounter or rest, with separate recording choice |
| 20:00–21:15 | Integrate evidence, review swarm outputs and prepare tomorrow | Independent builds or exports after reviewed instructions | Corrected records, accepted outputs and restart notes |
| 21:15–22:00 | Wind down and close the active queue | Non-interactive background jobs only | Open loops parked and sleep time preserved |

The table has eight sleep hours and sixteen waking hours. It does not promise sixteen hours of concentrated cognitive work. Meals, rest, transition and human contact remain actual activities with their own value. Source Genesis's sixty planned qualifying intervals are scheduled through the actual reviewed calendar; this example never mandates sixty consecutive daily exposures.

### The 260–300 word hyper-mode stream

**The delivered content rate is 260–300 words per minute.** This exact range comes from the user's clarification, not from a numerical ratio inferred from the spreadsheets. It applies to scheduled narration, audio and paced reading streams. It is not a requirement that the participant speak, reflect or perform a practical task at that rate.

Double-speed audio is one way to reach the range: source narration at 130–150 words per minute, played at 2×, delivers 260–300. Do not multiply the requested range by two again. A recording already delivering 280 words per minute stays at 1×. For a recording with a known natural rate, playback multiplier equals desired delivered rate divided by natural rate; inspect the actual duration and transcript rather than relying on the speed label alone.

| Actual content-stream minutes | Script or text budget at 260–300 wpm | Midpoint planning example at 280 wpm |
|---:|---:|---:|
| 5 | 1,300–1,500 words | 1,400 words |
| 10 | 2,600–3,000 words | 2,800 words |
| 15 | 3,900–4,500 words | 4,200 words |
| 20 | 5,200–6,000 words | 5,600 words |

Use **actual stream minutes × delivered words per minute**. Count only periods when content is being delivered. A ten-minute stream plus five minutes of recall is a fifteen-minute learning block carrying 2,600–3,000 delivered words, not 3,900–4,500. If two of the ten allocated stream minutes become pauses, eight actual stream minutes carry 2,080–2,400 words. Reflection, participant answers, movement, meals, transitions, rest and background agent runtime do not automatically add content words. Do not multiply 260–300 by all 120 Genesis hours or all sixteen waking hours.

Before each stream, prepare a source-linked script or text pack sized to its actual window. A useful ten-minute pack at the 2,800-word midpoint has a 200-word orientation, 600 words explaining the central model, 700 words of worked example, 600 words comparing a competing interpretation, 500 words translating the idea into a prototype or decision, and a 200-word recap. These are content allocations, not six additional time blocks. Citation narration, spoken transitions and repeated passages count if delivered. Record replayed words separately from unique new words. The source reading may be much shorter than the pack; use a clearly authored expansion rather than padding or pretending the original contains more text.

After a section, stop the stream clock and explain the central idea without looking; give an example, a counterexample and a question. If meaning is lost, pause, replay a chosen passage, inspect a diagram or use the transcript. When resuming a hyper-mode stream, return to the specified delivered range. If the participant deliberately chooses another delivery rate for a difficult passage, label that passage as a different mode and record its actual rate; do not silently redefine hyper mode. Speed reading uses the same survey, targeted read, retrieval and application loop. Record comprehension and next-day transfer alongside the word budget. The fixed stream definition and adaptive pauses can coexist.

For the rapid Genesis canvas, the fifteen-minute source block is initially **ten stream minutes plus five recall minutes**. It therefore calls for a 2,600–3,000-word prepared pack when all ten stream minutes are used. The narrator can deliver dense content while other agents prepare comparisons outside the participant's attention. The participant's responses, the three-observer comparison and practical action planning retain their own time and meaning.

### The attention and overlap matrix

| Primary activity | Plausible secondary activity | Background work | Accounting and boundary |
|---|---|---|---|
| Eating alone | Optional audio recap, short reading or voice capture | Source retrieval or export | One elapsed meal interval with a learning tag; no automatic extra study hour |
| Shared meal or relationship conversation | Only learning the people involved choose | Quiet queued jobs | People receive attention; no ambient recording by default |
| Familiar low-demand walking or exercise | Optional low-demand audio, stopped when surroundings require attention | Independent computation | Movement remains primary; avoid new interactive tasks requiring visual or manual attention |
| Passenger travel | Reading, selected audio, review or permitted notes | Retrieval with available connectivity | Travel plus learning labels, one elapsed interval |
| Driving, crossing traffic, operating tools or equipment | No distracting study, interface operation or recording interaction | Jobs started beforehand can run independently | The physical task retains attention; review later |
| Deep design, coding, writing or difficult study | Only task-relevant reference material | Independent agents with bounded contracts | Do not run a competing lecture as a second primary task |
| Source Geode encounter | Only compatible content and capture allowed by the operating plan | Remote preparation outside treatment control | Reflection AI has no authority over clinical or equipment controls |
| Teaching an adult | Observing the learner and recording agreed evidence | Quiet source lookup if it supports the encounter | Actual learner response takes priority over pace |
| Sleep and wind-down | No interactive work | Pre-authorised jobs with stored outputs and no interruption | Eight-hour sleep block stays intact; machine runtime is not human work time |

Overlapping activity is described, not multiplied. Store a single interval ID with one primary activity and zero or more secondary tags. Keep active human minutes, background machine runtime and artefact outcomes in different fields. A two-hour build with four agents remains two human elapsed hours plus the separately reported machine jobs.

### Swarms with a daily mission

Use complementary agents for source research, personal-record retrieval, world modelling, design, prototyping, testing, critique, teaching and archive stewardship. Give each a specific input pack, output, budget, allowed tools and stop condition. Let independent jobs proceed while the person builds or rests. Inspect disagreements and failed tests at the integration block. Draft outreach, purchases, publication and commitments remain proposals until the person authorises the actual external action. The swarm's value is measured in accepted useful outputs and repaired mistakes, not a large agent count.

### Business and networks as real outputs

Across the first twenty sessions, choose a venture thesis, map the people it serves and conduct or prepare permissioned discovery conversations. Produce a concrete offer and prototype, a resource and cost map, and a small set of collaborators whose interests genuinely connect to the mission. Across sessions 21–40, test the prototype with willing people, revise the offer, build delivery assets, document a repeatable workflow and compare evidence with the initial thesis. Across sessions 41–60, assemble a demonstrable service or product, a credible operating plan, a teaching or community event pack, and a continuing collaboration network. Actual sales, partnerships and participation are recorded only when they happen.

A useful network record asks: what is this person interested in, what did they actually agree to, what can we offer each other, what source supports the account, and what is the next mutually chosen step? Prepare a few specific introduction or collaboration drafts with a clear benefit and a respectful decline path. Do not replace relationship-building with bulk outreach or infer private attributes about people.

### Ground the etheric in the real

Use a six-stage conversion: **meaning → intention → specification → prototype → external feedback → revised record**. A personally meaningful resonance might become an interaction rhythm, a material experiment, a piece of music, a workshop ritual or a design principle. State what the symbol means to the person. Translate it into an observable desired experience or property. Build a version, invite an appropriate encounter or measurement, and let the result change the design. Personal or spiritual meaning remains welcome without being mislabelled as an established physical effect.

Joyful responsible abundance asks the resulting work three practical questions: did it make life more worth living for the people involved; were consequences, responsibilities and dissent taken seriously; and did useful capability or access increase? Preserve the person's answer and the relevant evidence separately. A failed prototype with a clear learning return can advance the mission; an impressive story without a working result remains a story.

### Other scheduling options

The main full-immersion route can be rescheduled when circumstances require it. These alternative desktop rhythms preserve the full curriculum:

| Desktop study option | Arithmetic | How it works |
|---|---|---|
| Busy-life continuity | 60 encounters × 2 hours = 120 hours | Each encounter may be completed as four 30-minute blocks across more than one day |
| Intensive studio | 30 active study days × 4 hours = 120 hours | Two full encounters per active day, with an uncounted break between them |
| Weekly studio | 20 weeks × 6 hours = 120 hours | Three encounters per week, leaving time for actual life experiments |

These are desktop scheduling options. They do not prescribe the number or frequency of pressure sessions. The source Genesis calendar follows the individually reviewed operating plan and records actual qualifying time. A busy calendar does not justify compressing or inventing that time.

The active human queue names the current mission and at most three immediate questions; a much wider agent queue may prepare downstream work within its contracts. Before each block, the Aura retrieves source excerpts, unresolved claims and the last accepted correction. At the end, save the last accepted state, next action and missing input. A missed block becomes rescheduled work, not a deficit in the person's identity.

## Three development arcs

| Arc | Sessions | Curriculum budget | Result sought |
|---|---:|---:|---|
| Discovery | G01–G20 | 40 hours | A recognisable, permissioned Minimum Viable Self, explicit unknowns, language and baseline requirements |
| Personalisation | G21–G40 | 40 hours | Conditional self models, a working three-observer method, useful tools and correction evidence |
| Integration | G41–G60 | 40 hours | Partnership, civic and frontier mission work, portable evidence and a continuation plan |
| Total | 60 | 120 hours | A reviewed learning portfolio; source Genesis completion remains an independently evidenced clock |

## One encounter in detail

The primary rapid-fire canvas is newly designed: 10 minutes orientation, 15 source review and retrieval, 25 focused declaration or production, 5 reset, 25 scenario or comparison, 5 reset, 20 design or outside-action preparation and 15 integration. These eight blocks total 120 minutes. The source's gentler editable illustration remains available: 10 minutes orientation, 25 declaration, 25 reflection, 20 rest or quiet, 25 rehearsal and 15 integration. [Geode Edition 3 p. 10.] Neither is a requirement to speak continuously. The participant can change the mix, and any source Geode activity must fit the actual operating plan. Store actual start/stop times, interruptions and allocation changes. In a four-block desktop day, save at each 30-minute boundary and resume the same session record.

Ask the participant to choose a meaningful category and explain why it matters now. Capture their statement in their own words. Add time perspective, context, attraction, repulsion, urge, known resources and perceived resourcefulness only where relevant. Invite a second interpretation and a concrete counterexample. Return the summary for correction. Use a scenario to examine one consequence, then retain the person's chosen next question or action.

The **three observers** are world, character and narrator. Past, present and condition-specific best selves are separate reflection lenses. Public, private and secret are permission contexts. These three different sets must never be merged into one three-part score. The participant's own explanation joins the observer comparison as a separately attributed account of meaning. [Geode Edition 3 p. 24; Teacher Day 28.]

## Ambitious portfolio

The end product should include a corrected MVS; a language and meaning dictionary; at least one conditional self model; a versioned world; synchronised observer records; a permissioned function; an expert-team trace; a recovery demonstration; a civic decision with dissent; a materials or intelligence research proposal; an Earth-space mission; and a portable archive. The strongest project may reach well beyond the examples here. Its claim must name what was built, simulated, measured or proposed so that the next collaborator can advance it.

The Geode development ambition retains four practical pathways: conventional chamber retrofit; geopolymer Version 1; crystalline, fused-quartz or blend Version 2 with separate compute; and Version 3 with integrated computational crystalline material. Fused silica is amorphous, so transparency is not a claim of crystallinity. The source development direction and existing atlas preserve an atomically precise manufacturing ambition for the completed computational Geode. This curriculum asks for discriminating experiments and architecture, not an invented performance benchmark.

## Review and recovery

At G20, G40 and G60, review fidelity to the person's meaning; source and uncertainty visibility; correction propagation; useful action; permission behaviour; and transfer to a new condition. Each dimension receives `demonstrated`, `developing`, `not yet assessed` or `not selected`, with an artefact reference and reviewer. These are capability records, not rankings of human worth or psychological diagnoses.

If a session becomes unproductive, record the exact stopping point and choose rest, a different category, lower input density, a different interface or a rescheduled block. If an interpretation is challenged, preserve the original, label the challenge and create a corrected version. If data are missing, mark the gap and re-run only what is needed. If a participant declines a question, the record can remain withheld or unresolved. No model should fill it from a stereotype or treat resistance as proof of a hidden trait.

The desktop release test is practical: can the person find a record, correct it, explain its audience, inspect an observer disagreement, complete one useful scoped task and restore their chosen export? The source programme additionally requires its own actual pressure ledger and operating-team completion record. Teacher competence requires its own observed practicum.

## Sixty selectable encounters
'''

GENESIS_END = '''
## A complete worked encounter

**Scenario, invented for teaching:** a participant is developing a community learning workshop. The world model contains a changed room booking, a visible timetable and an accessibility request. The character has seen the invitation and accessibility request but has not seen the new timetable. The narrator observes the participant continuing to prepare for the original room and tentatively interprets this as reluctance to change.

The teacher asks, “What information were you using when you made that choice?” The participant replies, “I was working from the earlier confirmation; I did not see the update.” The record now contains a world event, a character-information gap, a narrator inference and a participant explanation. The new hypothesis is that the update route failed. It is tested by changing the cue and replaying the task. The revision retains the first narrator interpretation as superseded; it does not turn it into a trait such as inflexibility.

The next action is to test a clearer update mechanism in a separately authorised real workshop. The scenario outcome is not evidence that the real mechanism works. The study record captures the exercise duration; actual workshop work has its own record. Any voluntary contribution is verified on its own terms.

## Continuation after the opening programme

Choose three ninety-day threads: one personal capability, one shared civic or creative project, and one frontier inquiry. Give each a useful next result, source gaps, resources, a decision owner and a review date. In the source Genesis sequence, dedicated twin socialising follows Genesis, with future physical travel following that socialising milestone. Independent everyday Aura learning and the separate adult teacher pathway retain their own calendars. [Geode Edition 3 pp. 35–36; Teacher Day 31.]

The portable archive contains sources, permission history, versions, corrections, observer streams, assumptions, evaluation results, model notes and recovery instructions. An approved public excerpt is a separate release object. A polished public site never substitutes for the private source record or the participant's right to correct it.
'''

TEACHER_INTRO = '''# Aura teacher training in hyper busy mode

This is an ambitious adult teacher-development route for people building personal Auras and helping others build theirs. It keeps the source's sixty-day progression from self-understanding and embodied interfaces through models, agents, civic judgement, frontier research and Earth-space stewardship. The outcome is a portfolio of things the learner can explain, build, test, revise and teach. A completion record is a course record; it does not confer professional accreditation or authorisation for clinical, engineering or child-services practice.


## Building the Aura during every encounter

The 11 November author clarification governs what building an Aura means here: organise patterns in seven nested horn tori, attach them to programmable facets and outward stack layers, select an ordered composition for AI work, generate a document or website, correct it, and form new groups for the next run. The [pattern-cycle guide](guide-aura.html) supplies the detailed process. Questionnaires and observer accounts provide patterns and feedback; they do not replace this productive architecture.

For each selected learning card, retain a compact build record: the self frame and access domain; the versioned patterns and group relationships; chosen facet layers and stack order; the intended AI operation and output; the resulting artifact; corrections; and the regrouped composition for a later run. Use internal private, internal secret or an explicitly approved public projection as appropriate. The required encryption and permissions must be enforced by the execution system; the current browser workbook does not provide that enforcement.

A teaching encounter can demonstrate the whole cycle: select examples and learner needs as patterns, produce a lesson and its companion webpage, observe where the explanation fails, correct both outputs, then regroup the improved examples for a different learner or self frame. The [settings guide](guide-settings.html) keeps the seated HBOT Geode, the separate Verse Box workbay and ordinary-device work distinct.

## Source and new design

The supplied **Aura Teacher Training 60 Days**, dated 14 October 2026, contains sixty readings, one per day. Its day titles and sequence remain the reference. This edition adds a repeatable two-hour learning budget, concrete review standards, a hyper-busy queue and intensive scheduling options. The source does not prescribe a universal two-hour teacher day or a 120-hour teacher total; those are explicitly new planning choices here. Original readings remain available through the linked source site.

The teacher course is independent of the optional Genesis programme. A participant doing source Genesis keeps its qualifying pressure clock separate from teacher learning. Source socialising exercises use simulation or role-play while that participant remains in Genesis; independent learners follow their own chosen pathway. [Teacher Days 1, 31, 60; Geode Edition 3 pp. 2, 36.]

## What hyper busy changes

The user's clarified primary route is **full immersion with eight hours of sleep**, rapid activity inside and outside the Geode, a **260–300 delivered-word-per-minute content stream**, selected double-speed audio and speed reading, agent swarms, business building and meaningful human networks. The teacher module is a distinct two-hour block within that sixteen-hour waking design; preparation and useful low-demand recaps can overlap meals, familiar movement or passenger travel when appropriate. The full day and attention matrix appear in the companion Genesis curriculum. Learner feedback, practical tasks and sensitive conversation retain their actual pace. The course aims at a major increase in capability; it does not promise a superhuman outcome.

The source spreadsheet's time-mode cells call for process reordering, with no numerical speed multiplier. This edition batches preparation and uses a durable return point. Before a teaching block, assemble the original reading, an accessible example, the current artefact and one review question. Finish the block with a named next action. An agent may draft examples or comparisons, but a teacher must inspect what the learner actually understood and did. Background machine runtime and overlapping human activities do not create extra human hours.

The **main immersion plan** retains sixty teacher modules alongside the broader programme: one two-hour module on each active curriculum day, with additional venture, network, research and production blocks. Source Genesis session availability remains controlled by its actual reviewed calendar; teacher days may continue independently. Pairing modules into thirty intensive study days is a separate option, not a forced acceleration of the pressure programme.

| Route | Planned curriculum time | Calendar |
|---|---:|---|
| Original day sequence with this edition's budget | 60 × 2 hours = 120 hours | One module per active learning day; source day numbers retained |
| Hyper-busy split blocks | 240 × 30 minutes = 120 hours | Four saved blocks per module, spread across available days |
| Intensive hyper-busy studio | 30 × 4 hours = 120 hours | Two sequential modules on each active day; breaks between modules add elapsed time |
| Weekly delivery | 20 × 6 hours = 120 hours | Three modules per week, leaving room for feedback between meetings |

Paired intensive days are T01+T02 on active day 1, T03+T04 on active day 2, and so on to T59+T60 on active day 30. A delayed field observation, learner response or replication can extend the calendar. Do not mark it done merely because its planned two hours have elapsed. The course's full competence record is only as strong as the actual evidence. Additional advanced research and repeated practicum time are logged as extensions rather than hidden inside the 120-hour budget.

If desktop Genesis and teacher training run together, 120 study hours plus 120 teacher hours is a planned **240 curriculum hours** when the tasks are separate. If one encounter serves both purposes, record its one actual duration and both learning links; do not claim 240 distinct hours from overlapping work. A source Genesis pressure programme has its own verified total, outside this desktop arithmetic.

## The two-hour learning pattern

Each module allocates 15 minutes to the original reading, 15 to retrieval and learner context, 40 to making or testing, 10 to a pause, 25 to teaching and learner transfer, and 15 to evidence review and correction. The six blocks total 120 minutes. Preparation performed outside this window is logged separately. A learner can choose speech, text, a diagram, physical cards, a screen or XR where available; the assessment concerns capability and preserved meaning.

The first fifteen-minute block uses the original day's reading as its source, with a prepared expansion where useful: **up to ten actual stream minutes at 260–300 wpm, then five minutes of unaided recall**. Ten stream minutes require 2,600–3,000 delivered words, with 2,800 as a midpoint script budget. A dedicated fifteen-minute stream would instead require 3,900–4,500 words; its recall and practice time must be scheduled separately. The original one-page reading is not represented as a full ten-minute script. An expansion should connect the original concept to a worked example, a competing interpretation, an application and a review question, with source and authored material distinguished.

A 130–150-wpm original recording played at 2× yields the requested 260–300 delivered wpm. Do not double the target range again. Count words only during actual delivery, excluding pauses and learner responses; record repetitions separately from unique content. Use the transcript word count and actual streamed duration to check the rate. After delivery, test explanation, application and later transfer. Pauses and replay can change the elapsed block without pretending that hyper mode has a different rate. If another rate is deliberately selected, label that segment as another mode. Neither the two-hour lesson nor the full immersion day is assumed to be continuous content delivery.

All sixty modules include a teach-back. When a peer is unavailable, role-play with a model is useful rehearsal but remains explicitly simulated. It cannot count as evidence that a real adult understood the lesson. Reserve real observed practice for the milestone reviews, especially T10, T20, T30, T39 and the T58 practicum. If no real learner is available, keep those outcomes pending and retain the rehearsal work.

## Six movements

| Movement | Original days | Budget | Teaching capability |
|---|---:|---:|---|
| Represent a person faithfully | 1–10 | 20 hours | Meaning, personal records, avatar, spatial addresses and sources |
| Learn and explain across contexts | 11–20 | 20 hours | Attention, retrieval, model context, emotion, reasoning and transfer |
| Coordinate tools and simulated worlds | 21–30 | 20 hours | Functions, agents, critique and the three-observer method |
| Facilitate shared intelligence | 31–40 | 20 hours | Socialisation, plural values, repair, culture, contribution and civic decisions |
| Investigate and steward systems | 41–50 | 20 hours | Compute, sovereignty, scientific method, materials, ecology and habitats |
| Extend and teach the frontier | 51–60 | 20 hours | Missions, generality tests, recursive improvement and advanced practicum |

## Teaching roles

The facilitator holds the learner's question and the lesson sequence. A source steward checks provenance and permission. A maker helps produce a usable artefact. An observer records what the learner could see and actually did. A challenger checks alternatives. These roles can rotate among people and clearly identified agent assistants. The human learner retains authority over personal meaning and chosen disclosure; relevant real-world decision holders retain authority over their actual systems.

The teaching observer is not a substitute for the three simulation observers. Inside a simulation, retain world state, focal-character attention and narrator account separately, then invite the person's own explanation. A teacher can use these streams to diagnose an unclear cue or missing context without guessing at a learner's motives.

## Evidence rubric

| Dimension | Demonstrated evidence | Evidence of a gap |
|---|---|---|
| Meaning fidelity | Learner recognises the account and can correct it | Fluent summary changes motive, context or uncertainty |
| Source judgement | Claims resolve to dated sources or labelled assumptions | A generated explanation is mistaken for original evidence |
| Usable artefact | Another person can inspect or use the result | The outcome is only a promise or an unexplained screenshot |
| Transfer | Learner handles a related new condition without coaching | Success depends on repeating the exact worked example |
| Permission and responsibility | Data use and decision rights match the task | Relationship tone or consent to discussion is treated as authority to act |
| Repair | Specific feedback produces an evidenced improvement | Revision is cosmetic or hides the failed first attempt |
| Teaching access | The chosen format fits this learner and preserves the concept | Speed or presentation preference is treated as ability |

Record each dimension as **demonstrated**, **developing**, **not yet assessed** or **not selected**, with reviewer, date and an artefact reference. No aggregate score implies a person's intelligence, morality or worth. A course completion record lists exactly which capabilities were assessed, by whom, and what remains open.

## Sixty modules with reviewable outputs
'''

TEACHER_END = '''
## A thirty-minute observer teaching encounter

Use T28's community-hub scene. Spend five minutes agreeing the adult learner's question and showing the event. For the next seven minutes, let the learner sort statements into world state, character attention, narrator observation and narrator inference. Ask for a reason when a statement could fit more than one category. Use eight minutes to add the character's own explanation and revise one interpretation. Spend five minutes replaying the scene after changing a cue. In the final five, present a different scene and observe the learner sorting it without coaching. Record the actual durations and result inside the module's teaching and review allocation, adjusting other blocks if necessary.

**Teacher:** “The sign existed in the model. What evidence shows that the character saw it?”

**Learner:** “We do not have that evidence. I treated the world model as the character's knowledge.”

**Teacher:** “Keep that difference. What could the narrator report without guessing why the character paused?”

**Learner:** “The pause and the next action. Any explanation of the pause needs a label or a question.”

This is an invented example of the target understanding, not evidence that a real learner passed. In an actual encounter, retain unexpected answers and modify the lesson accordingly.

## Advanced practicum

T58 asks the teacher to teach a demanding concept through an adult learner's meaningful interest, then observe a new task. The plan states learner context, prior knowledge, chosen capability, sources, format, materials, time allocation and transfer task. The observer records available cues, questions, actual actions, assistance given and learner wording. The trainee returns the summary for correction. A useful result can be a demonstrated capability or a precisely located gap with a better next lesson.

The portfolio includes the first plan, delivered version, learner-created artefact, independent transfer result, observer account, participant correction, revised teaching pack and a next review date. A rehearsed or model-simulated practicum stays labelled as rehearsal. Actual teaching completion remains pending until there is actual teaching evidence.

## Resets and continuation

At the end of each ten-module movement, choose what to deepen, change or leave unresolved. A reset preserves the artefact and last accepted interpretation, clears the active queue to one useful question and changes pacing or format. New words and categories are welcome when they serve the learner. An unanswered personal question is not automatically a teaching failure.

T60 produces a ninety-day plan with a personal Aura project, a teaching commitment and a frontier inquiry. Each has an accountable next result, resources, collaborators where agreed, evidence needed and a review date. A public invitation is chosen from reviewed material with its release scope recorded. The source's super-people and civic space steward ambition continues through more demanding evidence, deeper relationships and larger projects.

## Source references

- [Original sixty-day teaching collection](https://auraofintelligence.github.io/aura-teacher-training/course.html), with the supplied PDF as the source-of-record for this edition.
- [Genesis Geode Atlas](https://auraofintelligence.github.io/aura-genesis-geode-atlas/), for the separate Genesis, hardware and surrounding immersion designs.
- LifeLogging Part 1, Sheet1 B51:B62, for the process-reordering pace vocabulary; no durations were inferred from those cells.
- The repository's source catalogue records exact supplied-file hashes, page evidence and the difference between original readings and this new curriculum design.
'''

def build():
    assert len(GENESIS_ROWS)==60
    assert len(TEACHER_ROWS)==60
    genesis=make_genesis()
    teacher=make_teacher()
    assert sum(s['hours'] for s in genesis)==120
    assert sum(s['hours'] for s in teacher)==120
    data={
        'schemaVersion':'1.0.0','editionDate':'2026-11-10',
        'status':'authored curriculum; no personal completion claimed',
        'sourceGenesisHours':120,'desktopRehearsalHours':120,
        'clockRule':'Source Genesis pressure, desktop study, immersion life and teacher study are distinct records. Count overlapping elapsed time once.',
        'hyperMode':{
            'definition':'Prepared content streams deliver 260–300 words per minute, as explicitly requested by the user.',
            'source':'Current user instruction, 10 November 2026; not an inferred spreadsheet ratio.',
            'deliveredWpm':{'min':260,'max':300,'planningMidpoint':280},
            'playbackRule':'2x playback of 130–150-wpm source narration yields 260–300 delivered wpm. Do not double the target again. Already-280-wpm material can play at 1x.',
            'wordBudgetRule':'Actual stream minutes × delivered wpm. Exclude pauses, participant responses, reflection, practical work and non-streaming activity. Count replays separately from unique words.',
            'budgets':[
                {'streamMinutes':5,'minWords':1300,'maxWords':1500,'midpointWords':1400},
                {'streamMinutes':10,'minWords':2600,'maxWords':3000,'midpointWords':2800},
                {'streamMinutes':15,'minWords':3900,'maxWords':4500,'midpointWords':4200},
                {'streamMinutes':20,'minWords':5200,'maxWords':6000,'midpointWords':5600}
            ],
            'defaultInputBlock':{'elapsedMinutes':15,'plannedStreamMinutes':10,'recallMinutes':5,'plannedMinWords':2600,'plannedMaxWords':3000,'actualRule':'Pauses reduce actual stream minutes or extend/reallocate elapsed time; record the change.'},
            'tenMinuteScriptPlan':[
                {'section':'Orientation','words':200},
                {'section':'Central model','words':600},
                {'section':'Worked example','words':700},
                {'section':'Competing interpretation','words':600},
                {'section':'Prototype or decision application','words':500},
                {'section':'Recap','words':200}
            ],
            'review':['Explain the idea without the source','Apply it to a new example','Name a counterexample or limitation','Check later recall and transfer'],
            'modeChangeRule':'Pauses and replay do not redefine hyper mode. A deliberately different delivery rate is labelled as another mode.',
            'notAssumed':'No conversion of all 120 programme hours or sixteen waking hours into continuous word-stream hours.'
        },
        'fullImmersion':{
            'status':'Primary user-requested learning and life design; illustrative day, not a clinical operating schedule.',
            'sleepHours':8,'wakingHours':16,
            'audio':'Hyper-mode content delivers 260–300 words per minute. 2x is one route to this effective rate, not another multiplier. Pause for recall and inspect transfer.',
            'reading':'Paced hyper streams use 260–300 delivered words per minute; survey, retrieve without the source and apply. Pauses are separate; a different rate is labelled another mode.',
            'dayPlan':[
                {'start':'22:00','end':'06:00','hours':8,'primary':'Sleep','overlap':'Previously authorised silent background jobs','result':'Sleep protected; outputs wait'},
                {'start':'06:00','end':'07:00','hours':1,'primary':'Familiar movement, breakfast and orientation','overlap':'Optional low-demand recap audio','result':'One priority and recalled idea'},
                {'start':'07:00','end':'07:45','hours':0.75,'primary':'Brief swarm and review overnight work','overlap':'Independent retrieval and formatting','result':'Accepted contracts and ready sources'},
                {'start':'07:45','end':'10:45','hours':3,'primary':'Illustrative Geode attendance window or desktop equivalent','overlap':'Only compatible content within actual operating plan','result':'Two-hour curriculum encounter; separate actual attendance and qualifying-pressure records'},
                {'start':'10:45','end':'11:15','hours':0.5,'primary':'Recovery, meal or quiet','overlap':'Optional brief note','result':'Transition and next action if useful'},
                {'start':'11:15','end':'13:15','hours':2,'primary':'Build prototype or experiment','overlap':'Bounded tests and alternatives','result':'Working artefact or falsifiable experiment'},
                {'start':'13:15','end':'14:00','hours':0.75,'primary':'Lunch and chosen human connection','overlap':'Discussion or selected audio by choice','result':'Reciprocal offer or useful question'},
                {'start':'14:00','end':'16:00','hours':2,'primary':'Teacher module','overlap':'Quiet source and example preparation','result':'Lesson, learner attempt and correction'},
                {'start':'16:00','end':'17:00','hours':1,'primary':'Fieldwork, movement or passenger travel','overlap':'Appropriate low-demand audio or permitted capture','result':'Grounded observation or movement'},
                {'start':'17:00','end':'19:00','hours':2,'primary':'Venture and network studio','overlap':'Source research and prototype checks','result':'Tested offer, operating asset or prepared collaboration'},
                {'start':'19:00','end':'20:00','hours':1,'primary':'Dinner, relationships and ordinary life','overlap':'Learning only if chosen','result':'Lived encounter or rest'},
                {'start':'20:00','end':'21:15','hours':1.25,'primary':'Evidence integration and next-day preparation','overlap':'Reviewed builds and exports','result':'Corrected records and accepted outputs'},
                {'start':'21:15','end':'22:00','hours':0.75,'primary':'Wind down','overlap':'Non-interactive background jobs','result':'Open loops parked; sleep preserved'}
            ],
            'overlapMatrix':[
                {'primary':'Meal alone','secondary':'Optional audio, reading or short note','boundary':'One elapsed interval; learning is a tag, not another hour'},
                {'primary':'Shared meal or relationship','secondary':'Only learning people choose','boundary':'Conversation first; no default ambient recording'},
                {'primary':'Familiar low-demand movement','secondary':'Optional low-demand audio','boundary':'Stop audio when attention is needed; no visually demanding interaction'},
                {'primary':'Passenger travel','secondary':'Reading, audio or review','boundary':'One interval with multiple purposes'},
                {'primary':'Driving, traffic, tools or equipment','secondary':'None requiring attention','boundary':'Background agents may run; review their work later'},
                {'primary':'Deep design or study','secondary':'Task-relevant references','boundary':'Independent agents can run; no competing primary lecture'},
                {'primary':'Source Geode encounter','secondary':'Only operating-plan-compatible content','boundary':'Reflective AI has no treatment-control authority'},
                {'primary':'Teaching','secondary':'Observe the learner; useful source lookup','boundary':'Actual learner response takes priority over speed'},
                {'primary':'Sleep','secondary':'None interactive','boundary':'Eight protected hours; machine runtime is separately counted'}
            ],
            'groundingCycle':['meaning','intention','specification','prototype','external feedback','revised record'],
            'ventureArcs':[
                {'sessions':'G01–G20','outputs':['Venture thesis','Permissioned discovery conversations or prepared invitations','Concrete offer and prototype','Resource and cost map','Reciprocal collaboration shortlist']},
                {'sessions':'G21–G40','outputs':['Willing-user prototype tests','Revised offer','Delivery assets','Repeatable workflow','Evidence compared with thesis']},
                {'sessions':'G41–G60','outputs':['Demonstrable service or product','Operating plan','Teaching or community-event pack','Continuing collaboration network','Actual results distinguished from projections']}
            ],
            'accounting':'Use one interval ID, a primary activity and secondary tags. Report actual human elapsed time once, machine runtime separately, and artefact results separately.',
            'calendarRule':'Actual Geode attendance and qualifying intervals follow the individual authorised plan. Window changes displace discretionary tasks, not sleep. No prescribed exposure frequency.'
        },
        'genesis':genesis,
        'teacher':{
            'sourceDays':60,'hours':120,
            'hourBudgetOrigin':'New design in this edition; original source defines sixty readings, not a universal teacher-hour budget.',
            'hyperBusyOrigin':'LifeLogging Part1 Sheet1 B51:B62 names time/process-reordering modes but specifies no numeric ratios.',
            'contentStream':'User-defined 260–300 delivered words per minute; default 15-minute source block is 10 stream minutes plus 5 recall minutes. See hyperMode for script budgets and accounting.',
            'schedules':[
                {'id':'continuity','activeDays':60,'hoursPerDay':2,'totalHours':120},
                {'id':'intensive','activeDays':30,'hoursPerDay':4,'totalHours':120},
                {'id':'split','blocks':240,'minutesPerBlock':30,'totalHours':120}
            ],
            'modules':teacher,
            'intensivePairs':[{'activeDay':i+1,'modules':[f'T{i*2+1:02d}',f'T{i*2+2:02d}'],'hours':4} for i in range(30)]
        }
    }
    assert sum(x['hours'] for x in data['fullImmersion']['dayPlan'])==24
    assert sum(x['words'] for x in data['hyperMode']['tenMinuteScriptPlan'])==2800
    for budget in data['hyperMode']['budgets']:
        assert budget['minWords']==budget['streamMinutes']*260
        assert budget['maxWords']==budget['streamMinutes']*300
    (ROOT/'data/curriculum.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'content/genesis-120-hours.md').write_text(GENESIS_INTRO+'\n'+session_blocks(genesis)+GENESIS_END,encoding='utf-8')
    (ROOT/'content/teacher-training.md').write_text(TEACHER_INTRO+'\n'+session_blocks(teacher,True)+TEACHER_END,encoding='utf-8')
    print(json.dumps({'genesisSessions':len(genesis),'genesisHours':sum(x['hours'] for x in genesis),'teacherModules':len(teacher),'teacherHours':sum(x['hours'] for x in teacher),'paths':['data/curriculum.json','content/genesis-120-hours.md','content/teacher-training.md']}))

if __name__=='__main__':
    build()
