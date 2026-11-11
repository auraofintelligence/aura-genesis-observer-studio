import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const args=process.argv.slice(2);
if(args.some(arg=>arg!=='--atlas-only')) throw new Error('Supported option: --atlas-only');
const atlasOnly=args.includes('--atlas-only');
const authoringRevision='2026-11-11-chakra-targeting';
const questionnaire=JSON.parse(await fs.readFile(path.join(root,'data/questionnaire.json'),'utf8'));
const chakraThemes=questionnaire.chakraLenses.map(lens=>`chakra:${lens.id} (${lens.name}, ${lens.colour}): ${lens.focus}`).join('; ');
const groups=[
['identity','Identity memory and unfolding lives','whole-of-life',['S03','S04','S05','M2'],[
['Chosen identity','Self-description, name, language, roles and the right to remain more than a profile.'],
['Autobiographical episodes','Events, uncertain recall, corroboration and changing interpretations across time.'],
['Childhood and adolescence in context','Chosen recollections, family and learning environments without compulsory intimate disclosure.'],
['Adult transitions','Leaving, joining, relocating, retraining and revising direction with actual resources.'],
['Ageing and continuity','What to preserve, adapt and keep creating as circumstances and capabilities change.'],
['Conditional possible selves','Past, present and several futures under different material and social conditions.'],
['Narrative disagreement','Conflicting memories, others’ accounts, corrections and respectful unresolved differences.'],
['Personal symbols and rituals','Meaningful practices, imaginative associations and their ordinary effects.'],
['Unknown and unrecorded selves','What remains undefined, unavailable, declined, not yet discovered or deliberately forgotten.'],
['Legacy and succession','Skills, memories, responsibilities and artifacts someone may choose to pass on.']]],
['embodied-life','Embodiment care and everyday living','whole-of-life',['S04','S05','M2'],[
['Everyday physical capacity','Task-specific readiness, comfort and access without diagnostic inference.'],
['Rest sleep and sustainable intensity','Protected sleep, recovery, wind-down and evidence of useful engagement.'],
['Food meals and nourishment','Preferences, routines, culture, preparation and shared meals without prescribing diets.'],
['Movement and participation','Enjoyable movement, access needs, surroundings and compatible attention.'],
['Sensory environments','Light, sound, touch, crowding and interfaces that change an encounter.'],
['Communication access','Speech, text, visual, assisted and alternative communication chosen by the person.'],
['Support relationships','How assistance is offered, directed, understood and reviewed.'],
['Changing support needs','Transitions in support while retaining current preferences, choice and identity.'],
['Home and daily routines','Spaces, objects, task sequences and practical conditions for a worthwhile day.'],
['Care introductions and continuity','Reviewed personal context for a new supporter, with clear purpose and permission.']]],
['relationships','Relationships households and belonging','whole-of-life',['S04','S06','S09','U1'],[
['Friendship and chosen kin','Reciprocal connection, shared history and room for difference.'],
['Affection and chosen boundaries','Optional self-defined closeness with no inferred intimate biography.'],
['Family and intergenerational life','Roles, care, expectations, learning and changing household arrangements.'],
['Trust and repair','How trust develops, breaks, is corrected or is deliberately not restored.'],
['Conflict and negotiation','Different meanings, interests and workable decisions without coerced agreement.'],
['Group participation','Entry, voice, belonging, contribution and exit in groups.'],
['Interesting people and discovery','Curiosity-led encounters and mutually useful introductions.'],
['Reciprocal collaboration','Offers, actual agreements, responsibilities and value to each participant.'],
['Culture and different worldviews','Translation, hospitality, cultural authority and limits of one’s interpretation.'],
['Network depth and stewardship','Maintaining living relationships without treating people as acquisition metrics.']]],
['livelihood','Livelihood enterprise resources and contribution','whole-of-life',['S06','S08','S09','P1','U1'],[
['Work histories and capabilities','Skills learnt across jobs, informal work and experiences beyond credentials.'],
['Useful offers and customers','Observed problems, people served, clear offers and evidence of actual use.'],
['Prototype to service','Delivery, maintenance, support and the gap between a demo and a dependable offer.'],
['Business experiments','Hypotheses, discovery, willingness to engage, alternatives and stopping rules.'],
['Money and practical resources','Self-chosen current constraints and source-checked assumptions; no personalised financial advice.'],
['Ownership and independence','Tools, data, dependencies, switching options and control over useful work.'],
['Voluntary contribution and C-hours','Freely given time, verification, actual benefit and correction without ranking worth.'],
['Shared capability and mutuals','Pooling resources, reciprocity, participation and accountable governance choices.'],
['Work life and intermittent retirement','Freedom, learning, care, travel and meaningful work across changing phases.'],
['Resilience and succession in enterprise','Continuity, alternatives, handover and recovery after disruption.']]],
['place-civic','Places civic participation and living systems','whole-of-life',['S03','S05','S06','S09'],[
['Home place and Country','Belonging, local knowledge and who holds authority over stories and recordings.'],
['Travel and encounter','Learning through travel, hosts, access and the effects of being a visitor.'],
['Memory palaces and meaningful objects','Place-linked cues with distinguishable original, remembered and reconstructed material.'],
['Civic questions and participation','A concern, actual decision-maker, evidence and a usable participation route.'],
['Rules sources and consequences','Origin, current authority, lived effects and uncertainty in rules.'],
['Institutions and accountability','Promises, evidence, corrections, power and accountable decisions.'],
['Community preparation and recovery','Chosen local roles, continuity, resources and learning from disruption.'],
['Ecology and more-than-human consequences','Effects on living systems with appropriate evidence and local perspectives.'],
['Infrastructure and shared access','Useful computing, spaces, energy and services people can understand and maintain.'],
['Future generations and Earth-space stewardship','Long horizons, reversible steps and the responsibilities of expanding capability.']]],
['meaning-creation','Creativity joy meaning and inquiry','whole-of-life',['S08','S09','M1','P1','U1'],[
['Joy and a worthwhile day','Enjoyment, play, curiosity, rest and what the person values now.'],
['Emotion and personal interpretation','First-person meaning beside observable response, with room for correction.'],
['Values and difficult trade-offs','Principles under pressure, hidden costs and plural good lives.'],
['Attraction repulsion and urge','Distinct contextual motives, volatility and chosen response without personality scoring.'],
['Creative practice and authorship','Making, revising, finishing and crediting original and assisted work.'],
['Music story and emotional expression','Meaning, memory, audience and the value of a creative encounter.'],
['Belief evidence and uncertainty','Claims, sources, disconfirmation and the freedom to keep exploring.'],
['Symbolic etheric and infinite','Optional metaphysical and symbolic meaning distinguished from measurable claims.'],
['Meaning into material form','Intuition to specification, prototype, encounter, measurement and revision.'],
['Joyful Responsible Abundance in practice','Interacting meanings of joy, consequence and useful shared capability.']]],
['teacher-learning','Teacher understanding learning and curriculum','teacher',['T60','S01','S02','S05','U1'],[
['Learner purpose and starting knowledge','What a learner wants, can already do and chooses to explore.'],
['Attention perception and cognitive load','Available and noticed cues, task demands and changes in conditions.'],
['Memory retrieval and retention','Recall, meaningful connection, revision and later access to understanding.'],
['Concepts misconceptions and explanation','Competing models, examples, counterexamples and changed explanations.'],
['Accelerated content and comprehension','260–300 delivered words/minute with separately timed pause, recall and application.'],
['Skill practice and feedback','Demonstration, attempt, informative feedback and another opportunity.'],
['Transfer and generalisation','Using understanding in a new setting rather than copying a worked example.'],
['Curriculum prerequisites and routes','Dependencies, flexible sequence, entry points and purpose-specific depth.'],
['Inquiry sources and research literacy','Finding, reading, comparing and qualifying sources with an audit trail.'],
['Scientific mathematical and systems reasoning','Models, quantities, evidence, uncertainty and limits of analogies.']]],
['teacher-facilitation','Teacher facilitation inclusion and relationships','teacher',['T60','S04','S05','U1'],[
['Adult facilitation and learner agency','A voluntary adult learning relationship with shared purpose and choice.'],
['Teaching across the life course','Age/context-sensitive questions and clear scope for supported learning.'],
['Access and inclusive explanation','Representation, pacing, communication and accessible demonstration choices.'],
['Dialogue listening and follow-up','Questions that respond to actual meaning rather than a predetermined script.'],
['Disagreement without enforced conformity','Assessing comprehension while preserving a learner’s independent judgement.'],
['Group learning and collaboration','Roles, turn-taking, overlooked contributions and shared problem solving.'],
['Play simulation and serious games','Scenario design, explicit fiction, debrief and real transfer.'],
['Teaching through making and fieldwork','A worthwhile artifact or encounter as the place where learning happens.'],
['Care boundaries and appropriate support','Role clarity, consent and referral boundaries without demanding sensitive disclosure.'],
['Mentorship peer teaching and networks','Reciprocal learning, feedback and the ability to pass on useful capability.']]],
['teacher-practice','Teacher assessment reflection and professional growth','teacher',['T60','S02','S08'],[
['Observable learning outcomes','What a learner can do, explain or transfer and how it will be seen.'],
['Evidence and assessment design','Tasks that genuinely test intended capability rather than compliance or polish.'],
['Feedback correction and another attempt','Specific evidence, learner interpretation and improvement opportunities.'],
['Three observers in teaching','Whole scene, learner attention, observable reactions and learner meaning kept distinct.'],
['Lesson design and rehearsal','Objectives, examples, tasks, timing and review before teaching.'],
['Facilitation under changing conditions','Equipment failure, time pressure, misunderstanding and adaptive response.'],
['Teaching portfolio and capability claims','Actual work and observed learner evidence with unresolved limits visible.'],
['Teacher self-reflection and conditional selves','Own motives, assumptions, constraints and changes across experience.'],
['Teaching as a viable contribution or enterprise','Honest offers, delivery capacity, reciprocity and conditions of use.'],
['Continued inquiry and stewardship','Ongoing improvement, peer review, source maintenance and responsible handover.']]],
['aura-development','Aura Genesis agents and frontier integration','aura-genesis',['G3','GDD2','S01','S02','S08','M1','M2','U1'],[
['Minimum Viable Self and qualification','Purpose-specific own meaning, evidence, permissions, correction and first useful task.'],
['Three observer evidence architecture','Separation, alignment, uncertainty and disagreement across observer streams.'],
['Personal models retrieval and training','Different operations, selected evidence, evaluation and versioned correction.'],
['Agent swarm contracts and orchestration','Dependencies, tools, budgets, stopping rules and inspected outputs.'],
['Spatial matrix and cognitive architecture','Addresses, multiple meanings, nonlinear reading and explicit inference limits.'],
['Data sovereignty and permission propagation','Capture, storage, retrieval, training and sharing as separate choices.'],
['Genesis clocks and immersive learning','Source pressure record, desktop rehearsal, teacher time and real-life transfer.'],
['Truth Engine hypotheses and evaluation','Conditions, baseline, rival explanations and measured limitations.'],
['Geode materials and computational ambitions','Distinct design stages, material tests and unproven frontier goals.'],
['Human Aura partnership and continuation','A growing relationship that makes chosen life and shared capability more possible.']]]
];
const gapSets=[
 ['Keep recollection, contemporaneous evidence and later interpretation distinguishable.','Cover changed conditions across the life course, including what the person leaves unrecorded.'],
 ['Separate a person’s account of access and comfort from any clinical inference.','Explore how support can change while the person’s current choices remain authoritative.'],
 ['Distinguish a hoped-for relationship, an actual agreement and another person’s own account.','Include conflict, repair, refusal and reciprocal value rather than only successful connection.'],
 ['Test the gap between an attractive offer, a usable prototype and a dependable ongoing service.','Keep paid work, voluntary contribution, resource use and actual outcomes in separate accounts.'],
 ['Identify who holds the relevant knowledge or decision authority and what source supports it.','Include consequences across places, living systems, communities and time delays.'],
 ['Preserve symbolic or spiritual meaning without converting it into an unsupported empirical premise.','Use counterexamples and real creative encounters to explore changed meaning.'],
 ['Distinguish recognition, immediate recall, later retention and transfer to a new task.','Ask what a willing learner can actually do, not whether they agree with the teacher.'],
 ['Vary the learner’s chosen purpose, access conditions and social setting without stereotyping.','Include misunderstanding, disagreement, opting out and repair in facilitation scenarios.'],
 ['Require observed learner attempts and corrections rather than teacher confidence alone.','Separate peer role-play, source knowledge and demonstrated real-world teaching evidence.'],
 ['Keep observer view, self lens, permission, record status and spatial address as separate axes.','Distinguish implemented prototype behaviour, testable design, metaphor and frontier ambition.']
];
// These requirements enter each territory packet through the frozen plan manifest.
// They specify useful operations, not a Cartesian product or an extra questionnaire quota.
const authoringRequirements=[
 `Use U3 for seed scope and MS2 for practical chakra themes. Choose the primary theme for the question’s actual purpose and include its tag: ${chakraThemes}. Retarget the question to a concrete situation, decision, observation or practice within that theme.`,
 'Explain the fit in provenance.sourceNotes. If a question is intended for a specific torus, side and self, name the chosen placement in that note. A theme tag is a description of the inquiry. A placement is a separate choice. The seed has 288 questions for one torus, one side and one self, plus 12 reusable reflection lenses.',
 'Use U2 as the controlling November 11 author clarification and MS1 as current prototype evidence. Aura organises patterns in seven nested horn tori with programmable facets; questionnaires are one capture route into a compute/create/correct/regroup process.',
 'Across a territory’s batches, examine collecting or deriving a pattern, choosing its group or facet/layer binding, selecting an ordered stack and its input records/instructions, generating a useful output, finding a defect, correcting the relevant source or instruction, and regrouping for another attempt. Choose the operations that add a real distinction; do not make every question recite the complete loop.',
 'Include concrete making, selection, comparison, inspection and transfer tasks alongside personal reflection. A pattern may hold data, an instruction, a relationship or an asset reference. Explain what a chosen arrangement enables; do not equate geometric proximity with semantic evidence or invent fixed meanings for seven shells.',
 'Separate observer evidence, participant meaning, past/present/conditional selves, spatial addresses and public/private/secret access contexts. Compare how a chosen self or audience changes permitted inputs and output purpose without fabricating personal records.',
 'Internal private and secret material have differentiated encryption and permissions; an external public projection has reduced information and capabilities. Reading permission does not grant computation, training, writing, execution, republication, external action or access to internal sources; each further operation needs its own applicable grant. Ask about inherited restrictions and field-level release where relevant. A moved facet, visual shell or generated summary cannot silently release a source or expand authority.',
 'Use source locators accurately and identify new authored synthesis. Matrix Studio currently supports addressed records, stacks and local sequence/export operations; do not claim its browser already runs an encrypted AI service. Keep Geode/HBOT and Verse Box setups distinct, and distinguish design inquiry from operating equipment.',
 'Record the specific gap and transfer value in the existing strict question fields. Use tags for relevant operations rather than adding new schema keys. No invented answers, generic colour/self permutations, compulsory disclosure or unearned completion claims.'
];
const territoryGaps={
 T061:['Choose a learner’s intended artifact and identify the smallest useful set of prior records, examples and instructions for a first pattern stack; test the choice through an attempt rather than inferring readiness from confidence.'],
 T063:['Compare a stack that recalls its source with one that reveals a polished answer: design a delayed retrieval task showing whether the learner can reconstruct the relationship and find the original evidence.'],
 T064:['Place two rival explanations and a discriminating example in a teaching stack; ask which result would require correcting the explanation rather than merely changing its visual order.'],
 T066:['Choose where a demonstration, learner attempt and feedback step belong in an ordered program; identify the instruction to revise when the learner repeats a specific observable error.'],
 T067:['Regroup a successful lesson’s source patterns for a materially different problem while withholding the worked answer; judge whether the learner selects and adapts useful relationships.'],
 T068:['Build two routes through the same pattern collection for learners with different demonstrated prerequisites; distinguish a necessary dependency from a teacher’s habitual sequence.'],
 T073:['Generate two accessible representations from the same permitted concept records and inspect whether either transformation loses an important distinction; let the learner choose how to demonstrate it.'],
 T074:['Use an actual or fictional learner correction to choose which prompt, pattern relationship or explanation must change; preserve the learner’s meaning instead of classifying disagreement as failure.'],
 T076:['Compose a shared task from members’ separately permissioned contributions; decide what the group output may reveal and how an absent contribution changes the remaining dependencies.'],
 T078:['Select records and instructions for a document or website that teaches a making or fieldwork task; inspect the resulting artifact against an actual attempt and regroup the failed step.'],
 T081:['Define an observable learner action that tests whether selecting and ordering patterns improved capability; distinguish the quality of an AI-generated teaching artifact from the learner’s independent performance.'],
 T082:['Construct an assessment stack containing source evidence, the task and competing explanations without exposing its answer key; examine what a correct response would and would not establish.'],
 T083:['Trace a fault in a generated lesson to evidence selection, instruction, ordering or representation; use the learner’s next attempt to test the specific correction.'],
 T084:['Give the environment, character-attention and narrator accounts separate evidence inputs for a teaching encounter; compare their outputs with learner meaning before revising the teaching stack.'],
 T085:['Compose and rehearse an ordered lesson program with examples, demonstrations and learner actions; inspect where an AI-generated script asks for a capability the preceding steps never established.'],
 T086:['When a selected source becomes unavailable or an activity loses time, regroup the lesson around its essential dependency and specify what capability can no longer honestly be claimed.'],
 T087:['Build a public teaching portfolio from chosen evidence while withholding restricted learner material; inspect whether summaries preserve actual limitations and whether any permissioned claim needs a narrower form.'],
 T088:['Compare a remembered teaching choice with a present or conditional future self’s proposed pattern selection; identify which changed condition justifies the difference without rewriting the past event.'],
 T089:['Use a bounded pattern program to draft a teaching-service offer and delivery artifact, then test whether actual preparation, learner access and support work match what the offer promises.'],
 T090:['Hand a lesson stack to another willing teacher with its source versions and unresolved gaps; identify what they must understand to adapt it rather than reproduce its surface wording.'],
 T091:[
  'Distinguish unplaced MVS intake from a chosen pattern set: what source, meaning, instruction or relationship makes a record usable for one first document or site without claiming the person is fully modelled?',
  'Compare two selections drawn from the same MVS for different intended outputs; identify the useful information missing from each and avoid collecting unrelated private material just to fill facets.',
  'After the first output is corrected, decide whether to revise a self-description, its contextual qualification, the selected pattern relationship or the output instruction; preserve the earlier account and why it changed.'
 ],
 T092:[
  'Specify which source records each observer may read in a pattern-compute task and construct a case where the character did not notice something available to the environment account.',
  'Trace a conflicting generated claim back to observer evidence, an instruction or an unsupported combination; keep participant meaning as a separate correction without turning it into omniscient world evidence.',
  'Regroup a disputed account into a new document or simulation while keeping the unresolved alternatives visible; identify the missing observation that would distinguish them.'
 ],
 T093:[
  'For the same selected patterns, compare retrieval, a one-off prompt computation and a proposed training use: which inputs, permissions, costs and evaluation records differ?',
  'Change one source version after an output has been generated and decide which derived summaries or artifacts need recomputation; do not treat moving a facet as updating the underlying claim.',
  'Inspect a useful AI output that cites the wrong record or misstates a condition; choose a retrieval, instruction or model-evaluation correction rather than claiming training occurred automatically.'
 ],
 T094:[
  'Turn a selected stack into a bounded handoff between researcher, builder and critic: name each input, instruction, required output and dependency without granting all agents the whole private archive.',
  'When one computation fails or exhausts its budget, distinguish reusable intermediate artifacts from results that depend on the failed step; regroup the remaining work and preserve the stop reason.',
  'Compare running independent pattern computations concurrently with a sequence whose next instruction needs the previous artifact; test duplicate-action prevention and stale-input checks through a reference-only rehearsal.'
 ],
 T095:[
  'Select a concrete record, instruction and asset and explain whether they belong on separate facets, ordered layers of one stack or a shared group; judge the arrangement by a chosen computation and output rather than colour preference.',
  'Keep a record’s identity through flat, nested-torus and stack views; identify when reordering changes program meaning and when changing presentation should leave the same operation unchanged.',
  'Use the workbook’s alternate reading direction as an explicit interpretation choice, then compare generated results; retain the chosen relationship rules instead of treating adjacency as proof.'
 ],
 T096:[
  'Compose an output from public, private and secret inputs in a fictional example; determine which fields may reach the chosen model or audience and which require omission, transformation or a new explicit grant.',
  'Move or regroup a pattern from an internal view to a public-facing stack and identify what must remain restricted until release is authorised; distinguish read permission from write, execution and training permissions.',
  'After an input permission changes, trace dependent outputs, caches and shared artifacts; distinguish stopping future authorised use from the impossible promise of recalling plaintext already received.'
 ],
 T097:[
  'Track a pattern-selection task, a 260–300 delivered-word-per-minute stream, learner responses and background computation on separate records while preserving one elapsed human interval.',
  'Compare what MVS pattern preparation can occur in the distinct phone or Verse Box setting with what the source assigns to Geode/HBOT Genesis; retain actual setup and pressure-time boundaries without inventing operating instructions.',
  'At a planned return point, use a generated artifact or remembered explanation to decide whether to continue, correct or regroup the learning sequence; do not infer retained capability from playback completion.'
 ],
 T098:[
  'Make a source claim, its rival explanation and a discriminating observation available as distinct patterns; inspect whether the generated conclusion preserves the difference between evidence, inference and participant meaning.',
  'Compare outputs with and without one disputed record while holding the requested task fixed; identify whether the changed result exposes source dependence, prompt sensitivity or a genuinely tested hypothesis.',
  'Design a correction test that can fail after consensus among several agents; distinguish a reproducible artifact check from agreement produced by shared inputs or repeated wording.'
 ],
 T099:[
  'Separate the programmable seven-torus information architecture from the specific Geode/HBOT physical setup and its development stages; inspect an explanatory artifact for conflated geometry, materials and demonstrated computation.',
  'Build a source-linked comparison of proposed material capabilities, measured results and untested ambitions; identify the missing result needed before a generated description can call a capability implemented.',
  'Choose what a software-only pattern-stack rehearsal can test about a future Geode workflow and what remains dependent on separate equipment, material or integration evidence; keep Verse Box preparation distinct.'
 ],
 T100:[
  'Compare the patterns selected by a present self and a conditional future self for a chosen life project; generate contrasting artifacts without asserting that either imagined future has happened.',
  'After a useful output changes the person’s understanding, decide what to retain, correct, regroup or leave deliberately unresolved so the Aura remains revisable rather than fixing one narrative.',
  'Prepare a permissioned handover of a pattern program and its source history to a chosen collaborator or successor; distinguish continuity of useful work from claims of identity transfer or continuing consciousness.'
 ]
};
let territories=[];
for(let g=0;g<groups.length;g++){const [domainId,groupTitle,stream,sourceRefs,items]=groups[g]; for(let i=0;i<items.length;i++){const [title,objective]=items[i];territories.push({id:`T${String(g*10+i+1).padStart(3,'0')}`,domainId,groupTitle,title,objective,sourceRefs,quota:1000,stream,generated:0,checked:0,answered:0,gaps:[...gapSets[g],`Develop distinct source-checked questions about ${title.toLowerCase()}; the current plan does not yet establish full coverage.`],priority:['T065','T094','T099'].includes(`T${String(g*10+i+1).padStart(3,'0')}`)?'high':'normal'});}}
for(const territory of territories){
 territory.sourceRefs=[...new Set([...territory.sourceRefs,'U2','MS1','U3','MS2'])];
 territory.authoringRevision=authoringRevision;
 territory.authoringRequirements=[...authoringRequirements];
 territory.gaps.push(...(territoryGaps[territory.id]||[]));
}
const sourceIds=new Set(JSON.parse(await fs.readFile(path.join(root,'data/sources.json'),'utf8')).sources.map(source=>source.id));
for(const territory of territories) for(const ref of territory.sourceRefs){
 if(!sourceIds.has(ref)) throw new Error(`Cannot regenerate atlas: ${territory.id} references missing source ${ref}.`);
}
const dimensions={
lifeContexts:['Chosen past episode','Present ordinary life','Current demanding episode','Major life transition','Different resource conditions','Different access or support conditions','Relationship or group encounter','Different place or culture','Possible future under named conditions','Return after action and new evidence'],
teacherContexts:['Learner starting point','Teacher planning','Explanation or demonstration','Learner attempt','Misunderstanding or disagreement','Access or context change','Feedback and another attempt','New-context transfer','Peer teaching or handover','Longitudinal review'],
inquiryOperations:['Describe an episode','Identify available and noticed evidence','Explain personal meaning','Expose a competing account','Explore attraction repulsion and urge','Compare resources and resourcefulness','Generate and choose alternatives','Design an authentic test or artifact','Teach or explain across perspectives','Review outcome and revise the account','Compose a pattern group or ordered stack','Choose computation inputs instructions and scope','Inspect an artifact and correct its generating pattern','Regroup patterns across selves and access contexts'],
coverageDepths:['Initial account','Specific example','Contrast case','Boundary condition','Unknown or declined information','Counterfactual with one changed variable','Dependency or consequence','Alternative source or viewpoint','Observable action and transfer','Later correction and continuation'],
observerViews:['Environment','Character attention','Narrator description and tentative interpretation','Participant meaning account'],
selfLenses:['Past in its actual conditions','Present','Possible best self with stated resources','Constrained self with stated conditions','Uncertain future without assumed outcomes'],
recordStates:['planned','generated','checked','rejected','needs_revision','answered']
};
const atlas={version:'1.0.0',prepared:'2026-11-10',title:'Whole-of-life and teacher-training question weaving atlas',targetQuestions:100000,batchSize:50,plannedBatches:2000,territories,dimensions,status:{planned:100000,generated:0,checked:0,answered:0},seedBank:{domainPrompts:288,crossCuttingLenses:12,spatialScope:questionnaire.spatialScope,status:'Separate reviewed seed library; not counted as completed atlas slots.'},allocation:[{stream:'whole-of-life',territories:60,plannedQuestions:60000},{stream:'teacher',territories:30,plannedQuestions:30000},{stream:'aura-genesis',territories:10,plannedQuestions:10000}],notes:['This is a coverage and production plan, not a claim that 100,000 questions have been generated.','Territory quotas guide breadth. Reject weak or inapplicable combinations instead of filling a quota with paraphrases.','The 120-hour programme traverses selected pathways; it does not require every atlas question to be spoken or answered.','The existing 300 prompts are a seed and calibration set, separate from generated atlas output.','Generated, checked and answered are independent statuses; checking is not personal endorsement of an answer.','Question generation uses curated design evidence. Exact claims require source verification; a question must not smuggle an unsupported fact into its premise.'],delivery:{wordsPerMinute:{min:260,max:300},timing:'Count actual delivered words and stream minutes; pauses, answers, reflection and actions have separate intervals.',example:{questions:100000,assumedWordsPerQuestion:20,words:2000000,inputHoursAt300:111.111,inputHoursAt260:128.205},exampleStatus:'Planning arithmetic from an explicit hypothetical average, not a measurement of unwritten questions.'}};
atlas.version='1.1.0';
atlas.revised='2026-11-11';
atlas.authoringRevision={id:authoringRevision,sourceRefs:['U2','MS1','U3','MS2'],summary:'Practical chakra targeting within the operative pattern cycle across selves and access contexts. Territory IDs, titles and quotas are unchanged.',packetPolicy:'Existing runtime plan manifests are immutable scope snapshots. Use a new revision-specific plan directory for fresh packets; do not present packets from the earlier ledger as updated. Keep accepted IDs and progress from the existing ledger. Cross-ledger progress consolidation requires explicit reconciliation; creating another plan does not create another target or replace the production ledger.'};
atlas.notes.push('November 11 is an authoring-scope revision. The original private ledger and atlas hash remain unchanged. Historical accepted questions retain their review record and are not automatically reclassified as reviewed against the revised scope.');
// Regenerating the coverage design must never erase recorded production work.
const statusPath=path.join(root,'data/weaving-status.json');
const counterKeys=['planned','generated','checked','accepted','needs_revision','rejected','answered','simulated_answers','unfilled','review_flags'];
let progress=null;
try { progress=JSON.parse(await fs.readFile(statusPath,'utf8')); }
catch(error) { if(error.code!=='ENOENT') throw error; }
if(progress){
  const fail=message=>{throw new Error(`Cannot regenerate atlas: ${message}. Synchronise or reconcile the production snapshot first.`);};
  const validate=(value,label)=>{
    for(const key of counterKeys) if(!Number.isSafeInteger(value?.[key])||value[key]<0) fail(`${label}.${key} is invalid`);
    if(!(value.accepted<=value.checked&&value.checked<=value.generated&&value.generated<=value.planned)) fail(`${label} production counts are inconsistent`);
    if(value.accepted+value.needs_revision+value.rejected!==value.checked) fail(`${label} review counts do not reconcile`);
    if(value.answered+value.simulated_answers>value.accepted||value.unfilled!==value.planned-value.generated||value.review_flags>value.generated) fail(`${label} answer, gap or flag counts are inconsistent`);
  };
  if(progress.schema!=='aura-weaving-status/1'||!Array.isArray(progress.territories)) fail('unsupported snapshot schema');
  validate(progress.counts,'total');
  const rows=new Map(progress.territories.map(row=>[row.id,row]));
  if(rows.size!==progress.territories.length||rows.size!==territories.length||territories.some(t=>!rows.has(t.id))) fail('territory IDs do not match');
  if(progress.counts.planned!==atlas.targetQuestions||progress.jobCount!==atlas.plannedBatches) fail('planned total or batch count does not match');
  for(const territory of territories){
    const row=rows.get(territory.id);validate(row,territory.id);
    if(row.planned!==territory.quota||row.stream!==territory.stream) fail(`quota or stream differs for ${territory.id}`);
  }
  for(const key of counterKeys) if(progress.territories.reduce((sum,row)=>sum+row[key],0)!==progress.counts[key]) fail(`territory totals differ for ${key}`);
  for(const stream of new Set(territories.map(t=>t.stream))) for(const key of counterKeys){
    const total=progress.territories.filter(row=>row.stream===stream).reduce((sum,row)=>sum+row[key],0);
    if(progress.streams?.[stream]?.[key]!==total) fail(`stream totals differ for ${stream}.${key}`);
  }
  if(progress.complete!==(progress.counts.accepted===progress.counts.planned)) fail('completion flag is inconsistent');
  atlas.status=Object.fromEntries(counterKeys.map(key=>[key,progress.counts[key]]));
  atlas.statusSnapshot={snapshotAt:progress.snapshotAt,source:'weaving-status.json',reviewNote:progress.reviewNote};
  for(const territory of territories) for(const key of counterKeys) if(key!=='planned') territory[key]=rows.get(territory.id)[key];
}else{
  let previous=null;
  try { previous=JSON.parse(await fs.readFile(path.join(root,'data/weaving-atlas.json'),'utf8')); }
  catch(error) { if(error.code!=='ENOENT') throw error; }
  if(previous&&['generated','checked','accepted','answered','needs_revision','rejected','simulated_answers'].some(key=>(previous.status?.[key]??0)>0||previous.territories?.some(t=>(t[key]??0)>0))){
    throw new Error('Cannot regenerate atlas: recorded counters exist but data/weaving-status.json is missing. Run scripts/sync-weaving-status.py before regeneration.');
  }
}
await fs.writeFile(path.join(root,'data/weaving-atlas.json'),JSON.stringify(atlas,null,2)+'\n');
await fs.mkdir(path.join(root,'docs/data'),{recursive:true});
await fs.copyFile(path.join(root,'data/weaving-atlas.json'),path.join(root,'docs/data/weaving-atlas.json'));
if(progress&&!atlasOnly) await fs.copyFile(statusPath,path.join(root,'docs/data/weaving-status.json'));
if(!atlasOnly){
const domainMap=questionnaire.domains;
const patterns=[
['episode','A concrete episode','Start with this question: {seed}\nFor {selfLens}, in {condition}, choose one concrete episode. What happened, in what order, and what makes this episode relevant? Keep uncertainty about dates or details visible.'],
['evidence','Evidence and unknowns','Return to: {seed}\nTake the account so far: {previousAnswer}\nWhich parts are observation, recollection, testimony, inference or imagination? What could you check, what is unavailable and what should remain unknown?'],
['attention','The three views','Use this question as the anchor: {seed}\nIn {condition}, separate the wider available scene, what you actually noticed, and what a narrator could observe you doing. Where do the accounts diverge?'],
['meaning','Your meaning and correction','For {seed}, consider your account so far: {previousAnswer}\nWhat mattered to you that an observer could not know unaided? Correct one plausible misinterpretation and leave any disagreement unresolved if needed.'],
['counterexample','A counterexample','Explore the claim or preference in: {seed}\nGive an episode where the opposite was true. For {selfLens}, what changed in the conditions rather than in your identity?'],
['motives','Attraction repulsion and urge','Around {seed}, identify separately what attracts you, what repels you and what creates an urge to act. In {condition}, which of these should influence the choice, and which needs more interpretation?'],
['resources','Resources and resourcefulness','For {seed}, describe available time, tools, people and access. Separately describe your perceived ability to use them. Change one resource condition: what becomes possible and what remains difficult?'],
['choice','Competing good choices','Consider {seed} through {selfLens}. Name two worthwhile but competing actions. What would each make possible, cost or leave undone for you and others? What would make waiting a useful third option?'],
['future','Conditional future','Starting from {seed}, describe two possible good futures under different stated conditions. What would have to change, what cannot yet be known and which claim must remain an aspiration?'],
['action','Make something real','Translate {seed} into an observable experiment, artifact or encounter. Use this domain task as an option: {transferTask}\nState a result that would count against the idea and the permission needed before involving anyone.'],
['teach','Teach and test transfer','Turn the insight in {seed} into a short explanation for a willing learner. What could they do in a different example to show understanding? How could they disagree with you while still demonstrating it?'],
['review','Return after life','Revisit {seed} after an actual action or encounter. What did you expect, what happened, what did it mean and what should change? If no action occurred, record that honestly and identify the missing condition.']
];
const engine={version:'1.0.0',statement:'Rule-based contextual interview navigation. These are generated follow-up routes, not responses from an AI or a count of new authored atlas questions.',followupPatterns:patterns.map(([id,title,promptTemplate])=>({id,title,promptTemplate})),domains:domainMap.map(d=>({id:d.id,scenario:d.summary,tensions:['Your interpretation and another plausible account','A preferred future and present conditions','Useful speed and retained understanding'],transferTask:`Create a useful ${d.title.toLowerCase()} artifact or encounter, then return with evidence and your own meaning.`})),selfLenses:dimensions.selfLenses.map((title,i)=>({id:'self-'+i,title})),conditions:dimensions.lifeContexts.map((title,i)=>({id:'context-'+i,title}))};
await fs.writeFile(path.join(root,'data/interview-engine.json'),JSON.stringify(engine,null,2)+'\n');
await fs.copyFile(path.join(root,'data/interview-engine.json'),path.join(root,'docs/data/interview-engine.json'));
}
console.log(JSON.stringify({territories:territories.length,slots:territories.reduce((n,t)=>n+t.quota,0),batches:atlas.plannedBatches,authoringRevision,atlasOnly,status:atlas.status}));
