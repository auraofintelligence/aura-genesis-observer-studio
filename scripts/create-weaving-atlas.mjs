import fs from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
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
let territories=[];
for(let g=0;g<groups.length;g++){const [domainId,groupTitle,stream,sourceRefs,items]=groups[g]; for(let i=0;i<items.length;i++){const [title,objective]=items[i];territories.push({id:`T${String(g*10+i+1).padStart(3,'0')}`,domainId,groupTitle,title,objective,sourceRefs,quota:1000,stream,generated:0,checked:0,answered:0,gaps:[...gapSets[g],`Develop distinct source-checked questions about ${title.toLowerCase()}; the current plan does not yet establish full coverage.`],priority:['T065','T094','T099'].includes(`T${String(g*10+i+1).padStart(3,'0')}`)?'high':'normal'});}}
const dimensions={
lifeContexts:['Chosen past episode','Present ordinary life','Current demanding episode','Major life transition','Different resource conditions','Different access or support conditions','Relationship or group encounter','Different place or culture','Possible future under named conditions','Return after action and new evidence'],
teacherContexts:['Learner starting point','Teacher planning','Explanation or demonstration','Learner attempt','Misunderstanding or disagreement','Access or context change','Feedback and another attempt','New-context transfer','Peer teaching or handover','Longitudinal review'],
inquiryOperations:['Describe an episode','Identify available and noticed evidence','Explain personal meaning','Expose a competing account','Explore attraction repulsion and urge','Compare resources and resourcefulness','Generate and choose alternatives','Design an authentic test or artifact','Teach or explain across perspectives','Review outcome and revise the account'],
coverageDepths:['Initial account','Specific example','Contrast case','Boundary condition','Unknown or declined information','Counterfactual with one changed variable','Dependency or consequence','Alternative source or viewpoint','Observable action and transfer','Later correction and continuation'],
observerViews:['Environment','Character attention','Narrator description and tentative interpretation','Participant meaning account'],
selfLenses:['Past in its actual conditions','Present','Possible best self with stated resources','Constrained self with stated conditions','Uncertain future without assumed outcomes'],
recordStates:['planned','generated','checked','rejected','needs_revision','answered']
};
const atlas={version:'1.0.0',prepared:'2026-11-10',title:'Whole-of-life and teacher-training question weaving atlas',targetQuestions:100000,batchSize:50,plannedBatches:2000,territories,dimensions,status:{planned:100000,generated:0,checked:0,answered:0},seedBank:{domainPrompts:288,crossCuttingLenses:12,status:'Separate reviewed seed library; not counted as completed atlas slots.'},allocation:[{stream:'whole-of-life',territories:60,plannedQuestions:60000},{stream:'teacher',territories:30,plannedQuestions:30000},{stream:'aura-genesis',territories:10,plannedQuestions:10000}],notes:['This is a coverage and production plan, not a claim that 100,000 questions have been generated.','Territory quotas guide breadth. Reject weak or inapplicable combinations instead of filling a quota with paraphrases.','The 120-hour programme traverses selected pathways; it does not require every atlas question to be spoken or answered.','The existing 300 prompts are a seed and calibration set, separate from generated atlas output.','Generated, checked and answered are independent statuses; checking is not personal endorsement of an answer.','Question generation uses curated design evidence. Exact claims require source verification; a question must not smuggle an unsupported fact into its premise.'],delivery:{wordsPerMinute:{min:260,max:300},timing:'Count actual delivered words and stream minutes; pauses, answers, reflection and actions have separate intervals.',example:{questions:100000,assumedWordsPerQuestion:20,words:2000000,inputHoursAt300:111.111,inputHoursAt260:128.205},exampleStatus:'Planning arithmetic from an explicit hypothetical average, not a measurement of unwritten questions.'}};
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
if(progress) await fs.copyFile(statusPath,path.join(root,'docs/data/weaving-status.json'));
const domainMap=JSON.parse(await fs.readFile(path.join(root,'data/questionnaire.json'),'utf8')).domains;
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
console.log(JSON.stringify({territories:territories.length,slots:territories.reduce((n,t)=>n+t.quota,0),batches:atlas.plannedBatches}));
