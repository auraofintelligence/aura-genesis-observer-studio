# Producing the one hundred thousand question atlas

The atlas defines **100,000 planned question slots across 100 territories**: 60,000 for whole-of-life reflection, 30,000 for teacher learning and practice, and 10,000 for Aura and Genesis integration. The local weaving runtime turns that design into 2,000 reviewable jobs of up to 50 questions. It does not pretend those slots already contain authored questions.

The work proceeds through separate stages: plan, prepare a source-bound packet, ask a chosen agent or human to author a batch, import the batch, review its meaning, and record any later answers separately. The tool has no network client, model invocation, automatic agent spawning or token-spending operation. Choosing and running a model remains an explicit action outside this runtime.

## Create a local production ledger

From the repository root, use Python 3.10 or later:

```text
python runtime/weave.py plan --atlas data/weaving-atlas.json --out .private/weaving
```

The command reads the atlas and the adjacent `sources.json` and `questionnaire.json`. It verifies quota totals and source IDs, then creates a deterministic `jobs.jsonl`, a plan snapshot in `manifest.json`, and a transactional SQLite ledger. The existing seed questions are registered for duplicate checking; they are not counted as generated atlas slots.

For this atlas, the result is 100,000 planned slots and 2,000 jobs, with zero generated, checked, accepted or answered questions. The command will not overwrite an existing ledger. Keep using that ledger for subsequent work; use another directory only for a deliberately separate production run.

The plan files are snapshots. Their initially planned states do not update when batches arrive. Use `status` for current counts from the ledger.

## Give a lighter agent a complete bounded task

For the first teacher territory:

```text
python runtime/weave.py packet --ledger .private/weaving --job T061-B01 --out .private/weaving/teacher-packet.json
```

For the first whole-of-life territory, substitute `T001-B01`. A job ID names a territory and batch. The first job in T061 owns `W-T061-0001` through `W-T061-0050`; the twentieth owns `W-T061-0951` through `W-T061-1000`.

The packet includes a standalone authoring prompt, territory objective, exact allowed source references, design summaries and source locators, dimension vocabulary, available IDs, existing territory questions and a complete batch-specific JSON Schema. It can be passed to a chosen lighter agent without requiring that agent to reconstruct the whole chat.

The default packet contains curated design summaries, **not the complete original PDF or Word passages**. The author must say what informed the question and what was not verified. A source ID is not permission to invent a quotation, factual premise or claim of close reading. A later source steward can provide an appropriately scoped primary passage and record that provenance in the question's source notes.

Authoring should weave meaningful distinctions rather than mechanically multiply labels. Useful questions expose a specific dilemma, contrast, ambiguity, context change, practical attempt or transfer task. If only 12 good questions are ready, return 12; the other 38 slots remain open. A quota is a coverage target, not a reason to accept filler.

Whole-of-life prompts should accommodate chosen life chapters, changing support, relationships, livelihood, place and meaning without inventing personal facts. Teacher prompts should examine learner purpose, explanation, actual attempts, feedback and transfer. Adding “as a teacher” to an ordinary personal question does not by itself create a teaching question.

## Required batch record

The packet contains the authoritative schema. Its shape is:

```json
{
  "schema": "aura-weaving-batch/1",
  "jobId": "T061-B01",
  "territoryId": "T061",
  "domainId": "teacher-learning",
  "author": {
    "kind": "agent",
    "name": "The actual author or model",
    "runId": "A traceable authoring run identifier"
  },
  "questions": [
    {
      "id": "W-T061-0001",
      "prompt": "A newly authored, open or explicitly hypothetical question belongs here.",
      "tags": ["teacher", "starting-knowledge"],
      "sourceRefs": ["T60"],
      "provenance": {
        "kind": "authored_synthesis",
        "sourceNotes": "State the actual design evidence used and its limits."
      },
      "context": "Learner starting point",
      "operation": "Describe an episode",
      "depth": "Specific example",
      "observerView": "Participant meaning account",
      "selfLens": "Present",
      "gap": "Name the specific distinction missing from the existing territory.",
      "transfer": "Describe what an answer could change in an actual teaching encounter.",
      "premiseMode": "open_or_hypothetical",
      "privateAssumptions": false,
      "diagnosticInference": false
    }
  ],
  "generationNotes": "Explain partial coverage, limitations and unresolved source questions."
}
```

This is a shape illustration, not a completed pilot batch. The generator cannot assign `accepted`, `checked`, `answered` or another review status. The authoring record distinguishes questions from answers, measurements, quotations and claims about a participant's private life.

## Import and inspect

Save an actual agent-produced batch locally, then import it:

```text
python runtime/weave.py import --ledger .private/weaving --input .private/teacher-batch.json
```

The importer checks batch size, assigned IDs, territory and domain, approved dimension labels, source scope, required gap and transfer descriptions, provenance declarations and distinct prompts. It rejects unsupported fields and attempts to claim measured or quoted provenance. A limited text check catches some unqualified private-life assumptions; this is an aid to review, not proof that every premise is appropriate.

Exact duplicates are rejected after Unicode, case, punctuation and whitespace normalisation. This check covers the original seed library and every generated territory. Token-overlap comparisons flag possible near duplicates within the territory and current batch. They do not determine semantic equivalence: differently phrased repetition can escape them, and useful contrast questions can resemble each other. The reviewer decides whether the meaning adds anything.

Import is transactional: an invalid record rejects the batch without partially recording its valid neighbours. A valid import produces **generated** records. Structural validation is not editorial acceptance and does not increase the checked or answered counts.

Only selected question text and production metadata enter this ledger. Actual participant answers are not imported by the batch command. Private source material and answer files should stay outside the published website.

## Record a real review decision

After reading the question, checking source use, judging novelty and assessing its practical purpose, record the reviewer and reason:

```text
python runtime/weave.py review --ledger .private/weaving --ids W-T061-0001 --reviewer "Named reviewer" --decision accepted --note "State the substantive source, novelty and teaching-purpose checks actually performed."
```

The other decisions are `needs_revision` and `rejected`. A reviewer can inspect a partial batch rather than accepting a whole job. Passing the importer is never a reason by itself to accept a question. A declared reviewer name records responsibility; the software does not authenticate that person's identity or prove the review occurred as described.

For a requested revision, create a new packet containing the relevant reviewer notes:

```text
python runtime/weave.py packet --ledger .private/weaving --job T061-B01 --revision --out .private/weaving/teacher-revision-packet.json
python runtime/weave.py import --ledger .private/weaving --input .private/teacher-revision.json --revise
```

Only rejected or revision-requested slots without answer records can be replaced in this way. The earlier question is retained in the event history, and the revised record returns to generated status for fresh review. Accepted questions cannot be silently overwritten. There is no automatic retry loop; the coordinator decides whether another attempt is worthwhile.

## Keep answered separate from accepted

When an actual answer exists, its local reference can be recorded explicitly:

```text
python runtime/weave.py answer --ledger .private/weaving --id W-T061-0001 --reference .private/answers/teacher-example.json --actor "Answer recorder" --kind actual
```

The question must already be accepted. `--kind simulation` records a simulated response instead, and does **not** increase the actual answered count. The runtime records the reference without reading or authenticating its contents. It cannot determine whether the answer is complete, meaningful, endorsed or genuinely experienced. An existing answer reference is not silently replaced.

## Read the honest production totals

```text
python runtime/weave.py status --ledger .private/weaving
python runtime/weave.py report --ledger .private/weaving --out .private/weaving/status-snapshot.json
```

The report gives overall, stream and territory counts. Planned capacity, generated slots, explicitly checked records, accepted records, revision requests, rejections, actual answers and simulated answers remain distinct. `unfilled` means slots with no generated record; rejected slots still need editorial work even though their generation has been recorded. `complete` means every planned slot has an accepted question, not that anyone has answered the corpus or completed teacher training.

Use a current report when preparing a public progress snapshot. A polished coverage map is still a plan until the ledger contains actual text and review decisions. At 100,000 questions, a hypothetical average word count can estimate delivery time, but only generated text can establish actual word counts. Reflection, answers, pauses and practical activity have their own time records.

## Verification and practical limits

```text
python tests/weave_test.py
```

The tests cover deterministic planning; zero fabricated completion; source-bound packets; separate production states; explicit review and answer classification; atomic rejection; invalid IDs, sources and dimensions; exact and near duplicates; private-premise and provenance checks; and revision history. The software uses only Python's standard library and SQLite.

Allocate each job to one authoring worker at a time. Duplicate slot imports are rejected rather than merged automatically. The packet contains earlier questions from its territory so the author can see existing coverage, but there is no automatic semantic search across all 100,000 slots. As the corpus grows, cross-territory conceptual review and learner-use evidence remain necessary.

The aim is a large, coherent and revisable library whose questions earn their place. The production system makes gaps visible and gives lighter agents bounded work; it does not turn a numerical target into evidence of understanding.
