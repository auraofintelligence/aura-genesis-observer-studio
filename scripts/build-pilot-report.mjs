import fs from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
const read=async file=>JSON.parse(await fs.readFile(path.join(root,'data',file),'utf8'));
const report=await read('weaving-status.json');
const review=await read('weaving-pilot-revision-review.json');
const initial=await read('weaving-pilot-review.json');
const decisions=new Map(review.decisions.map(d=>[d.id,d]));
const streams=[['Whole of life — chosen identity','weaving-pilot-life-revised.json'],['Teacher development — learner purpose','weaving-pilot-teacher-revised.json']];
let out=`# A lighter-agent pilot, reviewed and revised

This pilot tests the production method on **50 distinct question slots**: 25 whole-of-life questions and 25 teacher-development questions. The original author was a lighter agent, gpt-6-luna. A separate AI reviewer checked meaning, novelty, source use, premise and practical transfer. The original and revised files are two versions of the same 50 slots, not 100 different questions.

The public production snapshot currently contains **${report.counts.generated} generated**, **${report.counts.checked} checked**, **${report.counts.accepted} accepted**, **${report.counts.needs_revision} requiring revision**, **${report.counts.rejected} rejected**, and **${report.counts.answered} actual answered** records out of **${report.counts.planned.toLocaleString()} planned slots**. These are question-production states. They do not measure anyone's understanding or personal development.

## What the review changed

The first review accepted ${initial.counts.accepted} questions, requested revision of ${initial.counts.needs_revision}, and rejected ${initial.counts.rejected} as semantic duplicates. All original source notes needed the exact supplied locator, while retaining the honest statement that the author had inspected curated design summaries rather than the complete original passages. Three repeated concepts needed replacement. Several view labels, inquiry operations and transfer notes also needed clarification.

The lighter agent returned revised batches. A fresh independent review then judged those versions; each current decision appears below. Earlier files, hashes and review notes remain in the repository. The local ledger preserves the actual import, decision and revision sequence.

Acceptance here means **a useful candidate for this bounded pilot after AI editorial review**. It is not human endorsement, participant testing, proof of exhaustive source verification or evidence that all territory gaps are covered. No personal answers were generated for this pilot.

## How to continue

Use the [production guide](guide-weaving-runtime.html) to create a canonical job packet, then the [weaving handbook](guide-weaving.html) to guide authoring and review. The source packets contain summaries and exact locators; supply actual passages when a question depends on a specific source claim. The atlas's remaining slots and coverage gaps stay visible.

Read the [current count snapshot](data/weaving-status.json), [first review record](data/weaving-pilot-review.json), [revision review record](data/weaving-pilot-revision-review.json), [revised life batch](data/weaving-pilot-life-revised.json) and [revised teaching batch](data/weaving-pilot-teacher-revised.json). These files contain public question text and production metadata, not participant responses.

`;
for(const [title,file] of streams){
 const batch=await read(file);
 out+=`## ${title}\n\n`;
 for(const q of batch.questions){
  const decision=decisions.get(q.id); if(!decision)throw new Error('Missing review: '+q.id);
  out+=`### ${q.id}\n\n**${q.prompt}**\n\n${q.context} · ${q.operation} · ${q.depth} · ${q.observerView} · ${q.selfLens}\n\n**Gap addressed:** ${q.gap}\n\n**Transfer into life or teaching:** ${q.transfer}\n\n**Source basis:** ${q.provenance.sourceNotes}\n\n**Review: ${decision.decision.replaceAll('_',' ')}.** ${decision.note}\n\n`;
 }
}
out+=`## What this sample leaves open\n\nThese two territories do not establish coverage across a whole life or the whole teaching profession. Later jobs need more demanding episodes, contrasting resources and access conditions, observation of actual attention, diverse life chapters, reciprocal relationships, ventures, place, creative practice and teacher transfer. A large atlas earns its value through distinct questions and use in real encounters. The number alone cannot establish that value.\n`;
await fs.writeFile(path.join(root,'content/weaving-pilot.md'),out);
console.log(JSON.stringify({pilotSlots:50,reviewed:review.decisions.length,report:'content/weaving-pilot.md'}));
