# Validation report

Prepared 10 November 2026. This report records observed checks and their limits for the Aura Genesis Observer Studio edition assembled on this date. It is a validation record, not a certificate of clinical efficacy, teaching accreditation, security or completion of the 100,000-question target.

## Executable checks

| Suite | Observed result | What the result supports |
| --- | --- | --- |
| [Observer runtime tests](../tests/runtime_test.py) | 19 passed | The tested evidence-stream boundaries, provenance, simulation lineage, correction and budget behaviours of the local prototype. |
| [Question-weaving runtime tests](../tests/weave_test.py) | 12 passed | The tested planning, import, validation, review and status-accounting contracts. |
| [Frontend contract checks](../tests/frontend-contracts.cjs) | 30 passed | The tested storage choices, import validation, observer labels, contextual interview records, parent chains, actual export payloads and atlas accounting. |

The two Python suites passed together as 31 tests. Together with the frontend suite, the recorded total is 61 passing checks. These are test results for the behaviours exercised, not proof that every possible input or integration has been tested.

The frontend harness executes the actual studio JavaScript with isolated public-data fixtures and a small DOM double. It checks default memory-only operation; explicit storage opt-in; scoped opt-out; a visible storage failure; rejection of demo data as personal answers; malformed or excessive records; retained simulation labels; legacy workbook compatibility; missing, cyclic or duplicate interview parents; participant/source labels; parent-version snapshots; JSON and Markdown exports; and bounded territory packets. It makes no network requests and does not use real browser storage. Its method and limitations are documented in [tests/FRONTEND.md](../tests/FRONTEND.md).

## Static site and real-browser observations

The final static-site check covered **14 HTML pages and 564 internal references, with zero errors**. This includes the pilot guide, inline hero-image URLs and CSS asset references. The 30 frontend contracts were also rerun successfully against the final public files; the 31 passing Python runtime checks remain the recorded runtime result.

Real-browser checks reported by the publishing agent covered:

- Desktop overview and question atlas rendering.
- The teacher stream filter, showing 30 territories and 30,000 planned slots.
- A Deep Interview seed, recorded parent and continued child turn.
- Loading the fictional observer example with its simulation label intact, followed by a verified blank-event reset.
- Clearing only test entries after checking the workflows and resetting the browser viewport.
- The questionnaire and teacher guide at a 375-pixel viewport, with no horizontal page overflow observed.
- The corrected reading-guide hero after a CSS-relative image path problem was found and repaired. A subsequent browser screenshot confirmed the workshop artwork rendered; the mobile guide measured 375 pixels of scroll width at a 375-pixel viewport.

The native Learning stream label appeared in the browser, and role-based selection worked. Explicit label associations were also added to the static controls. This is not a screen-reader audit.

The available evidence does **not** establish browser download persistence, reload persistence across browser profiles, comprehensive keyboard or assistive-technology coverage, a full accessibility audit, or operation of the optional Ollama adapter against a live model. Those behaviours must not be described as tested on the strength of the isolated harness or the visual checks above.

## Source coverage and interpretation

All **15 supplied original files** were structurally read or extracted into the source workflow. Relevant sections were closely read, and selected PDF pages and spreadsheet regions were visually inspected. The public source register distinguishes original design documents, later project context, current user instructions and external references. This does not mean every assertion in every original has been independently verified.

The three spreadsheets contain **30,105 non-empty cells** in the structural inventory. The research identifies **33 candidate spatial regions** and preserves their sheet/range context, grouping evidence, ambiguity and proposed uses. The preview reconstructs a selected source region while retaining meaningful placement, merged areas, borders and blank space; display sizing was adjusted for legibility.

The semantic interpretation remains incomplete. Adjacency, reading direction, bounding boxes, colour, repetition and blank space are evidence to investigate, not automatic proof of the author's meaning. The new system must retain author correction and competing interpretations. See [matrix-analysis.md](matrix-analysis.md) and [matrix-map.json](matrix-map.json).

## Question counts and review state

The atlas plans **100,000 questions** across 100 territories. The canonical work plan divides that target into 2,000 jobs of 50 questions. These are planned slots and jobs, not generated or accepted questions.

The original seed pilot contains **288 domain questions and 12 reflection lenses**. The lenses provide reusable ways to examine an answer; deterministic combinations in Deep Interview are navigation routes, not additional authored or reviewed questions.

The lighter-agent pilot has **50 original question records**, comprising 25 whole-of-life questions and 25 teacher-development questions. The two revised pilot files contain revised versions of those same 50 records. Keeping both editions does **not** establish 100 distinct questions.

The first-edition editorial review recorded 50 reviewed items: **0 accepted, 47 needing revision and 3 rejected**. That review was an AI editorial review against the supplied packets, source register and seed questions; it was not human approval or complete primary-passage verification. The revised versions then received an [independent revision review](../data/weaving-pilot-revision-review.json) accepting all 50. The publishing agent recorded all 50 acceptance decisions explicitly through the runtime CLI. The earlier 47-revision/3-rejection results remain version-specific review history. These are recorded editorial decisions under the supplied rubric, not human approval or independent verification of every underlying source claim.

The additional [question-expansion-a.json](../data/question-expansion-a.json) holds **288 candidate prompts**. They remain unreviewed and uncounted in the atlas's completed-question totals. Their existence must not be added to generated, checked, accepted or answered counts without the appropriate import and review workflow.

The final ledger-derived public snapshot records **50 generated, 50 checked, 50 accepted, 0 needing revision, 0 rejected and 0 actual participant answers**, with **99,950 question slots unfilled**. Generated, checked, accepted and answered remain distinct stages. A schema or automatic check does not certify semantic quality. A simulated demonstration answer is not an actual participant answer. The accepted revised questions are available in the [readable pilot guide](../docs/guide-pilot.html).

## Public and private boundary

The public site provides authored guidance, source descriptions, explicitly labelled simulations, public planning data, local tools and credited artwork. Personal browser answers are not sent to the site or incorporated into the public catalogue. The browser's sharing labels record intentions; they do not encrypt files or enforce access control.

Private source extraction, original preservation working copies, actual learner responses, local run outputs, ledgers containing personal material, credentials and private logs belong outside the published directory and version control. The repository ignore rules exclude the private working area, environment files and transient test output. These reports contain no personal answer fixtures or machine-specific source paths.

## Repeating the checks

Run from the repository root:

```text
python -m unittest discover -s tests -p '*test.py'
node tests/frontend-contracts.cjs
node scripts/build-site.mjs
python scripts/check-site.py
```

Regenerate the relevant public guides and data after source changes. Check the actual final pages in a browser when changing layout or interaction. The revised pilot review, explicit ledger decisions, public status refresh and final enlarged-site check are complete. Publication itself remains pending in this report and must be confirmed separately from local build and test success.
