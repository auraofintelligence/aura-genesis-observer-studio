# Artifact catalogue

Prepared 10 November 2026. This catalogue identifies the authored outputs, their source relationships and their intended public or private boundary. Paths are repository-relative. It does not claim completion of the 100,000-question target or an operational medical device, trained personal model or autonomous business.

## Start here

| Reader's purpose | Primary artifact | Role |
| --- | --- | --- |
| Use the companion studio | [docs/index.html](../docs/index.html) | Public interactive workspaces for the atlas, Minimum Viable Self, Deep Interview, three observers, Genesis, teacher development, sources and data choices. |
| Understand the complete architecture | [content/system-guide.md](../content/system-guide.md) | Three observer streams, separately attributed participant meaning, personal records, permissions and the route from a starting self to continuing development. |
| Understand the large question programme | [content/question-weaving-guidelines.md](../content/question-weaving-guidelines.md) | The 100,000-question design, writing and review requirements, coverage gaps and distinctions between dimensions, questions, answers and outcomes. |
| Read the accepted pilot | [content/weaving-pilot.md](../content/weaving-pilot.md) and [docs/guide-pilot.html](../docs/guide-pilot.html) | The readable set of 50 accepted revised pilot questions, retaining original and revision provenance. |
| Follow Genesis | [content/genesis-120-hours.md](../content/genesis-120-hours.md) | Sixty learning encounters tied to the original Genesis design, with pressure-reference, desktop learning and life-calendar clocks kept distinct. |
| Develop teaching practice | [content/teacher-training.md](../content/teacher-training.md) | The independent adult teacher-development pathway, its original source days, practices, artefacts, learner feedback and transfer. |
| Examine a future demonstration | [content/demo-december-2026.md](../content/demo-december-2026.md) | Explicitly simulated 15 December 2026 examples, with Luke aged 44. These are not his testimony or known future outcomes. |
| Run the local observer prototype | [runtime/README.md](../runtime/README.md) and [content/agent-runtime.md](../content/agent-runtime.md) | An executable evidence-separated observer workflow, a deterministic demonstration and the declared boundary of optional local-model processing. |
| Produce and track question batches | [runtime/weave.py](../runtime/weave.py) and [content/weaving-runtime.md](../content/weaving-runtime.md) | Canonical planning, bounded job packets, imports, validation, explicit review and status accounting. |

## Question and curriculum data

| Artifact | Contents and accounting treatment |
| --- | --- |
| [data/questionnaire.json](../data/questionnaire.json) | The 288 authored domain seed questions and 12 reusable reflection lenses. This is the initial 300-item seed pilot. |
| [content/questionnaires.md](../content/questionnaires.md) | Readable source edition of the questionnaire material. |
| [data/interview-engine.json](../data/interview-engine.json) | Authored branch patterns, domain scenarios, tensions, transfer tasks, self lenses and conditions. Rule-based combinations are not counted as newly authored questions. |
| [data/weaving-atlas.json](../data/weaving-atlas.json) | 100 territories with quotas, streams, objectives, sources, gaps, dimensions and a status snapshot. The planned target is 100,000 questions, arranged in 2,000 batches of 50. Runtime ledger results should govern refreshed completion counts. |
| [data/weaving-quality-rubric.json](../data/weaving-quality-rubric.json) | The explicit quality and review criteria used to assess generated questions. |
| [data/curriculum.json](../data/curriculum.json) | Sixty Genesis entries, sixty teacher entries, the full-immersion day, compatible overlap rules, venture pathways and hyper-mode delivery assumptions. |
| [data/teacher-source-index.json](../data/teacher-source-index.json) | The original teacher-day source index used to retain the source progression. |
| [data/demo-answers.json](../data/demo-answers.json) | Read-only simulated answers with basis, uncertainty, alternatives and verification prompts. They are separate from personal answer fields. |
| [data/simulated-mvs.json](../data/simulated-mvs.json) | An explicitly simulated Minimum Viable Self representation for demonstration. It is not approved personal training data. |

Deep Interview stores a selected seed, branch, perspective, condition, exact prompt, participant answer, context, evidence, review note, parent ID and parent-version snapshot. Its saved turns can be exported or imported with a personal workbook. Unrecorded drafts are not included in workbook exports. The application caps a workbook's interview chain and import size; this is a storage boundary, not a limit on the larger question programme.

Hyper mode uses an effective content stream of **260–300 words per minute**. Suitable 2× playback can be a means of reaching that range. Input-time estimates exclude participant answers, reflection, teaching, practice and action. The full-immersion plan retains eight hours for sleep and counts overlapping human activity once.

## Pilot editions and uncounted candidates

| Artifact group | Exact role |
| --- | --- |
| [weaving-pilot-life.json](../data/weaving-pilot-life.json) and [weaving-pilot-teacher.json](../data/weaving-pilot-teacher.json) | The original lighter-agent pilot: 25 whole-of-life and 25 teacher-development question records, 50 in total. |
| [weaving-pilot-life-revised.json](../data/weaving-pilot-life-revised.json) and [weaving-pilot-teacher-revised.json](../data/weaving-pilot-teacher-revised.json) | Revised versions of the same 50 question records. Retaining both editions does not create 100 distinct questions. |
| [weaving-pilot-review.json](../data/weaving-pilot-review.json) and [research/weaving-pilot-review.md](weaving-pilot-review.md) | The first-edition editorial review: 0 accepted, 47 needing revision and 3 rejected. This history is preserved alongside later decisions. |
| [weaving-pilot-revision-review.json](../data/weaving-pilot-revision-review.json) | Independent re-review accepting all 50 revised questions, followed by 50 explicit runtime CLI acceptance decisions. |
| [question-expansion-a.json](../data/question-expansion-a.json) | An additional 288 unreviewed candidate prompts. These are uncounted in completed atlas totals and are not silently merged into the public seed bank. |

The final ledger-derived snapshot is **50 generated, 50 checked, 50 accepted, 0 needing revision, 0 rejected, 0 actual participant answers and 99,950 unfilled slots**. The [pilot guide](../docs/guide-pilot.html) presents the accepted revised edition.

A revised file, a passing schema check, an editorial recommendation, acceptance and an actual participant answer are different artifacts and different states. Use stable IDs and version history to follow a question through them. Acceptance here records the completed editorial review workflow; it does not claim human approval or automatic semantic certification.

## Sources and spatial research

The source workflow covers all **15 originals supplied for the task**: the two expert/agent papers, the three whole-of-life/tourism/children proposal documents, the C-Hour plan, the whole-system preview, the alignment paper, the UNGA81 paper, the Geode Development Edition 3, Genesis Game Design Edition 2, sixty-day teacher PDF and three spreadsheets.

The originals remain source evidence. New explanations, prompts, simulations and proposed interpretations are labelled as authored additions rather than silently substituted for those originals.

| Artifact | Role |
| --- | --- |
| [data/sources.json](../data/sources.json) | Public source catalogue with stable IDs, locators, roles and status. It also identifies public autobiographical/project material, the current user brief and selected external primary references. |
| [research/source-manifest-additional.json](source-manifest-additional.json) | Supplemental source-preservation metadata for the supplied materials. |
| [research/genesis-source-analysis.md](genesis-source-analysis.md) | Edition-specific analysis supporting Genesis and teacher development. |
| [research/public-context.md](public-context.md) and [public-source-register.json](public-source-register.json) | Public project context, visual conventions, licence provenance and evidence boundaries for simulated responses. |
| [research/matrix-analysis.md](matrix-analysis.md) | Structural and spatial reading of the three unconventional workbooks, with ambiguities and interpretation limits. |
| [research/matrix-map.json](matrix-map.json) | 33 candidate regions with source IDs, sheet/range addresses, observed grouping, proposed roles and unresolved meaning. |
| [research/matrix-spatial-preview.png](matrix-spatial-preview.png) and [matrix-spatial-preview.svg](matrix-spatial-preview.svg) | A reconstruction of a selected source region retaining spatial relationships. Display row heights and type sizes were adjusted for legibility. |
| [research/content-review.md](content-review.md) | Review observations about source fidelity and the authored synthesis. |

The structural spreadsheet inventory contains **30,105 non-empty cells**. That inventory is not a complete interpretation of their cognitive architecture. The source region map remains provisional and open to the author's correction; the workbooks are not assumed to read uniformly from top left to bottom right.

Original-preservation working copies, extracted text and detailed local processing records belong in the private working area, not in the deployed site. The public catalogue supplies references and authored explanations without copying personal source-working details into this report.

## Public site, artwork and rights

The deployed artifact is the **docs directory**. It contains the interactive studio, generated reading guides, public JSON datasets, downloadable authored Markdown, sitemap and rights pages. Repository research and runtime files are catalogued alongside it but are not automatically website routes.

The frontend files are [docs/index.html](../docs/index.html), [docs/assets/studio.js](../docs/assets/studio.js) and [docs/assets/studio.css](../docs/assets/studio.css). The guide builder uses [scripts/build-site.mjs](../scripts/build-site.mjs), with [docs/assets/reader.css](../docs/assets/reader.css) for reading-page presentation. [docs/sitemap.html](../docs/sitemap.html) provides the complete public page index.

Original generated artwork includes the Genesis hero, workshop hero and favicon. The [image provenance register](../docs/assets/image-provenance.json) identifies their production records. Real coastal photographs retain their separate Creative Commons terms in the [photo provenance register](../docs/assets/photo-provenance.json). The [image credits page](../docs/image-credits.html) distinguishes photographs, generated concepts and the spatial source reconstruction. Self-hosted fonts retain their SIL notices.

Original project material uses the [Strange But True Public Source Licence](../LICENCE.md), also presented at [docs/licence.html](../docs/licence.html). Third-party photo and font rights remain separate. Personal outputs belong to their creator under the licence terms; publishing the tool does not publish their answers.

## Executable and repeatable work

| Artifact | Role |
| --- | --- |
| [runtime/aura.py](../runtime/aura.py) | Standard-library local observer runtime, explicit simulation and optional local-model adapter. No clinical controls or autonomous publication tools are supplied. |
| [runtime/schemas](../runtime/schemas) | Input and output contracts for observer records. Runtime checks also enforce relationships that schema alone cannot establish. |
| [runtime/examples/community-workshop.simulated.json](../runtime/examples/community-workshop.simulated.json) | Labelled fictional scene used by the local demonstration. |
| [runtime/weave.py](../runtime/weave.py) | Canonical question-work planner and review/status workflow. |
| [scripts/create-questionnaire.mjs](../scripts/create-questionnaire.mjs), [create-demo.mjs](../scripts/create-demo.mjs), [create-weaving-atlas.mjs](../scripts/create-weaving-atlas.mjs) and [build_curriculum.py](../scripts/build_curriculum.py) | Reproducible preparation of the relevant authored datasets. Review regenerated differences before replacing a curated edition. |
| [scripts/check-site.py](../scripts/check-site.py) | Static publication checks for pages, references and core data invariants. |
| [tests/runtime_test.py](../tests/runtime_test.py), [weave_test.py](../tests/weave_test.py) and [frontend-contracts.cjs](../tests/frontend-contracts.cjs) | Repeatable runtime and interface contracts. [tests/FRONTEND.md](../tests/FRONTEND.md) explains the isolated frontend harness. |
| [research/validation-report.md](validation-report.md) | Observed results, browser checks, source coverage and remaining verification limits. |

## Private working material

The private working area and ignore rules are for actual learner records, unredacted extraction, originals used during analysis, runtime outputs, canonical ledgers containing personal material, credentials and private logs. The public demonstration and writing-packet examples remain explicitly labelled public artifacts.

Browser workbooks are memory-only by default. A user can choose browser saving and can export ordinary unencrypted JSON or Markdown. These outputs are not appended to the repository or sent to a remote service by the public interface. Generated questions do not authorise the system to generate or publish a person's answers.
