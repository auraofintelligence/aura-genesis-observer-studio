# Aura Genesis Observer Studio

An Aura built through seven nested horn tori, programmable facets and stacks: organise patterns, select AI computation, produce documents and websites, correct, regroup and compute again across multiple selves and access domains. Minimum Viable Self reflection and the three observers supply patterns and feedback within this wider whole-of-life and teacher-development process. This edition turns Luke's source documents and spatial matrices into an explorable studio and a bounded production process for lighter agents.

[Open the companion site](https://auraofintelligence.github.io/aura-genesis-observer-studio/) · [All reading guides](https://auraofintelligence.github.io/aura-genesis-observer-studio/sitemap.html) · [Aura of Intelligence](https://auraofintelligence.github.io/)

## Begin with a pattern and a purpose

Read [Building an Aura](content/aura-pattern-cycle.md) first. The pattern architecture is the organising and productive system. Internal private and secret selves require separately enforced encryption and permissions; the external public self exposes approved material with reduced capabilities. The current static companion documents those requirements and supports reflection; it is not yet the encrypted AI execution engine.

The [Geode and Verse Box guide](content/geode-and-verse-box.md) preserves the specific seated HBOT workspace and the separate portable public booth. Source-reference imagery replaces the first edition’s mistaken rock-geode illustration.

1. Open **Minimum Viable Self** and choose a question that matters in your present life. Add your own answer, context, evidence and uncertainty. Use **Deep Interview** to follow it through different conditions, examples, tensions and practical attempts.
2. Open **Three observers**. Record the wider available scene, the character's actual attention and a narrator's description separately. Add your own meaning or correction. These are attributed accounts, not three independent witnesses merely because three prompts exist.
3. Choose an action that can make the reflection useful: a prototype, a lesson, an offer, an encounter, a community contribution or a revised decision. Return with what actually happened.
4. Use the **Genesis** and **Teacher development** workspaces for the longer progression. Follow the full reading guides for session detail and review standards.
5. Export your workbook before closing. It starts in memory only. Browser saving is optional and is not encryption. No participant answers are sent by this static application to an AI service or inserted into the public repository.

The public December 2026 examples are **fictional, conditional demonstrations** for Luke at age 44. They are not predictions, memories, endorsements or completed achievements. They remain separate from your answers.

## Scale and delivery

The target is **100,000 useful questions**, allocated as 60,000 whole-of-life, 30,000 teacher-development and 10,000 Aura/Genesis questions across 100 territories. The production plan contains 2,000 jobs of up to 50 questions. It is a map of work to do, not a claim that the whole corpus has been written.

The **288 domain questions** cover the 12 × 24 facets on one side of one torus for one self. The **12 reflection lenses** are reusable across questions. Browse the seed by practical chakra theme, then choose its spatial placement separately. **48 December example answers** demonstrate attributed, revisable responses. A separate **50-question lighter-agent pilot** exercises generation, editorial review and revision; its original and revised versions occupy the same 50 slots. See the [current production snapshot](data/weaving-status.json) and [pilot review](research/weaving-pilot-review.md) for actual states. The extra `question-expansion-a.json` file is an unintegrated candidate set and is not included in any accepted atlas count.

Hyper-mode is **260–300 delivered words per minute**. Double-speed playback is one possible way to reach that rate; it does not double the target again. The seed questions contain 3,397 words, about 11–13 minutes of prompt input. Answering, reflecting, practising and building take additional time. The 100,000-question atlas supports selective pathways over a whole life and teaching practice; it is not a demand to answer every question during Genesis.

The full-immersion design retains **eight hours of sleep** and a sixteen-hour waking calendar. It includes meals, movement, learning, building businesses, reciprocal networks, creative work and background agent jobs. Compatible activities can overlap, but an elapsed hour is counted once. Human activity, machine runtime and outcomes have separate records.

## The programme and its sources

- **Three observers:** environment; character–environment attention; narrator. Participant meaning and correction are a separate attributed account. Past/present/possible selves are a different axis.
- **Minimum Viable Self:** a useful, revisable representation with evidence, context, uncertainty, purposes and permission boundaries. It is not a personality score or a trained model.
- **Genesis:** 60 two-hour learning cards, grounded in the source's three arcs. The source's 120 qualifying at-pressure hours, any separately undertaken desktop curriculum, teacher study, life calendar and machine runtime remain distinct. This site supplies no chamber controls or treatment instructions.
- **Teacher training:** 60 source-aligned modules with explanations, practice, learner feedback, transfer tasks, portfolio outputs and review criteria. The two-hour module budget is a new design choice, not a quotation of the original teacher document.
- **Spatial matrices:** 33 mapped regions preserve cell ranges, boxes, clusters, alternate reading directions and interpretation limits. They are not flattened into an assumed row-by-row taxonomy.
- **Joyful Responsible Abundance:** expansive ideas return to tangible offers, useful work, reciprocal relationships, learning and revisable evidence. Frontier Geode concepts remain an explicit development direction rather than claims of proven hardware.

Start with the [system guide](content/system-guide.md), [Genesis protocol](content/genesis-120-hours.md), [teacher handbook](content/teacher-training.md) and [matrix analysis](research/matrix-analysis.md). The [source register](data/sources.json) distinguishes source claims, design synthesis, public context and user instructions. Original private files and chat transcripts are not republished.

## Give lighter agents bounded work

Python 3.10 or newer is enough for the local production ledger. No model account, package installation or network access is needed for these commands. Use a new directory for a new run; the planner does not overwrite an existing ledger.

```text
python runtime/weave.py plan --atlas data/weaving-atlas.json --out .private/my-weave
python runtime/weave.py packet --ledger .private/my-weave --job T061-B01 --out .private/teacher-packet.json
```

Give that packet to a chosen authoring agent together with the [weaving guidelines](content/question-weaving-guidelines.md). It provides reserved IDs, territory purpose, source summaries and locators, coverage gaps, dimension vocabulary and a strict output schema. Ask for fewer questions when the remaining ones would be filler. The command itself does not call or spend money on a model.

```text
python runtime/weave.py import --ledger .private/my-weave --input .private/teacher-batch.json
python runtime/weave.py status --ledger .private/my-weave
```

Import validates structure and flags possible repetition. It does **not** accept questions automatically. A separate reviewer assesses meaning, novelty, source use, premise and practical transfer, then records an explicit decision. A revision retains earlier history. Actual answers and simulated answers are different states.

See the [complete production instructions](content/weaving-runtime.md) for review, revision and answer commands. To update the public progress snapshot from a reviewed local ledger:

```text
python scripts/sync-weaving-status.py --ledger .private/my-weave
```

This publishes only production counts and metadata. It does not publish the ledger or participant answers. Regenerating the atlas preserves a compatible public snapshot and refuses an incompatible one.

## Run the local observer prototype

```text
python runtime/aura.py demo --output .private/runs/my-first-demo.json
```

This produces an explicitly simulated observer comparison and four-role task graph, without a model call or external action. The [runtime guide](runtime/README.md) explains how to prepare your own evidence and the optional, explicitly enabled loopback Ollama adapter. The adapter has been checked with isolated tests; a real local-model connection has not been verified in this edition. Nothing here claims a personal nanoLLM has been trained or a live autonomous swarm deployed.

## Preview, build and check

The committed `docs/` folder is the complete static GitHub Pages site. A local HTTP server is needed because the application loads its JSON files.

```text
python -m http.server 4317 --bind 127.0.0.1 --directory docs
```

Open `http://127.0.0.1:4317/` in your browser. To rebuild the reading guides after editing their sources, use a current Node.js version supporting `import.meta.dirname` and install the pinned Markdown renderer:

```text
npm install
npm run build
python scripts/check-site.py
python -m unittest discover -s tests -p '*test.py'
node tests/frontend-contracts.cjs
```

The source generators are `scripts/create-questionnaire.mjs`, `scripts/create-demo.mjs`, `scripts/create-weaving-atlas.mjs` and `scripts/build_curriculum.py`. They are intentional regeneration operations; edit the relevant source generator when changing generated material. `npm run build` refreshes the website from current content and data rather than regenerating the authored sources.

GitHub Pages serves the **`main` branch, `/docs` folder**. `.nojekyll` preserves the static files. No third-party analytics, remote font loading or external model key is required. The hosted page is still subject to ordinary hosting access logs. A project-subpath `robots.txt` is advisory; host-root rules govern crawlers.

## Catalogue and continuing work

See the [artifact catalogue](research/artifact-catalogue.md) and [validation report](research/validation-report.md) for what was inspected, built and checked. The next production cycle is to allocate an unfilled job, supply the relevant source passages where needed, generate a small batch, review meaning and duplication, revise, and learn from voluntary participant use. Cross-territory semantic review and real teaching-transfer evidence become increasingly important as the corpus grows.

Private records belong under `.private/` or another deliberately private location. Never commit actual answers, credentials, raw private sources or contact lists. Sharing labels describe intent; they are not an access-control system. Public simulation files remain labelled wherever they are exported.

## Rights and attribution

Original project work uses the [Strange But True Public Source Licence](LICENCE.md), following the established Aura project terms. It is a public-source licence with restrictions, not an OSI open-source licence. Commercial, institutional and government use must follow its permission requirements. Participant outputs remain theirs under the licence's terms.

Original generated hero illustrations and a generated favicon are mixed with credited real photographs. The [image credits](docs/image-credits.html), [generation prompts](docs/assets/image-provenance.json), [photo provenance](docs/assets/photo-provenance.json) and bundled font notices preserve the separate third-party terms.

Luke Nathan Hayes / Strange But True / Aura of Intelligence. Developed with an AI team, including a lighter-agent authoring pilot. Edition 2, 11 November 2026.
