# Aura local observer runtime

This standard-library Python prototype turns an evidence file into three separate observer packets, preserves the participant's own account, and prepares a bounded team of research, critique, building and evaluation tasks. It runs on Python 3.10 or later without installing packages. Run commands from the repository root.

## Try the complete offline demonstration

```text
python runtime/aura.py demo --output .private/runs/demo.json
```

The bundled example is a **deterministic simulation** of a workshop room change. Nothing in it is Luke's actual answer, an observed learner result, a booking, a viable business finding or a measured outcome. The command creates a JSON run containing seven labelled source records, three observer packets, the separate participant account, unknowns, disagreement and correction links, three proposed actions, and four completed **simulated reference-design** tasks.

Every output has `export_permission: "none"`. Here that means no public or third-party release permission; saving the requested local run is permitted. No command publishes files. The default example does not permit model processing either. Existing output files are never overwritten; choose `demo-02.json` for another run. Keep private run files outside the published website and version control.

## Prepare your own evidence

Copy `runtime/examples/community-workshop.simulated.json` to a private working location and replace it with an honestly labelled scene. Use a separate file for real observations. Preserve the original event record and append corrections with explicit links.

```text
python runtime/aura.py prepare --input .private/my-scene.json --output .private/runs/my-scene-prepared.json
```

`prepare` validates the file and constructs packets; it does not call a model or execute the proposed tasks. It does not search files named by source locators, scrape webpages or inspect accounts. Locators are references for human review. The input contract is in `schemas/input.schema.json`; the output contract is in `schemas/output.schema.json`. The runtime also checks relationships that JSON Schema alone does not establish.

The source file is a declaration of provenance. Validation checks its consistency; it cannot authenticate whether someone actually measured an event or labelled a source honestly. `source_content_authenticated` remains false.

## Keep four accounts distinct

| Account | Included evidence | What it cannot silently acquire |
| --- | --- | --- |
| Environment observer | Records assigned to the defined world/scene stream | Real-world omniscience or personal meaning |
| Character-attention observer | The focal person's recorded noticed cues, their accessible reports and unknowns | Facts visible only to the whole-world observer |
| Narrator observer | Observable behaviour and explicitly distinguished tentative interpretations | An authoritative account of motives or personality |
| Participant's own meaning | Separately attributed self-report and corrections | Replacement by a narrator consensus |

Each packet has only its own stream. Source labels and locators stay in the coordinator's full provenance catalogue because they can themselves reveal another stream. Packet sources contain only source ID and source kind. Cross-stream relationship IDs are omitted from packets; a count records that inaccessible references exist. The coordinator retains the complete evidence, conflict and correction history.

The runtime trusts the input author to assign a record to the correct stream. It cannot identify a secretly copied fact hidden inside a text field. It enforces packet boundaries, not semantic omniscience detection or operating-system isolation.

Records distinguish `claim_kind` from `evidence_class`. An interpretation, proposed action or derived record cannot be promoted to measured evidence. Measurements require a measurement source and no derivation. Simulation lineage propagates through source, derivation and supersession references; changing only a record flag cannot turn a demonstration into a real result. A simulation file cannot be mixed into a real set. `unknown` remains an explicit claim kind, not a blank to complete automatically.

## The agent team

The coordinator schedules a fixed dependency graph:

```text
researcher → critic → builder → evaluator
       └───────────→ builder
              └─────────────→ evaluator
```

Only IDs explicitly listed in `swarm_evidence_ids` are available to the planned team. The default is an empty list. The demo deliberately selects only the invented room-change world record. This is separate from the three-observer access scopes.

The researcher frames the workshop question and evidence needs. The critic challenges assumptions. The builder supplies a mock service-flow template and cue-repair experiment. The evaluator supplies comparison and transfer criteria. The demo's outputs are fixed reference templates; they are not model-generated research or a functioning autonomous business. `prepare` leaves these tasks planned. No external tools are available: `allowed_tools` is empty and `external_tool_execution_available` is false. Actions remain in a proposed queue for review.

`max_swarm_tasks` limits simulated completions. A task outside the budget is `budget_stopped`, with no fabricated output. Dependencies must complete before a simulated successor can complete. Model calls, prompt characters, response tokens and elapsed scheduling time have separate limits.

## Optional local model processing

The optional adapter supports an **already installed local model** behind an already running Ollama service. This adapter uses Ollama's documented `POST /api/chat` request, JSON output, non-streaming response and output-token metadata. It does not install software, download models or enable a cloud provider. [Official Ollama chat API](https://docs.ollama.com/api/chat).

In a private input copy, set `local_model_permission: true` only on sources you intend to send to the local service. Then explicitly choose the model and command:

```text
python runtime/aura.py run-local --allow-local-model --model YOUR_INSTALLED_LOCAL_MODEL --input .private/my-scene-local.json --output .private/runs/my-scene-local-result.json
```

`YOUR_INSTALLED_LOCAL_MODEL` is a placeholder to replace, not a model recommendation. The default service origin is `http://127.0.0.1:11434`; `--endpoint` may select a different port on `127.0.0.1`, `localhost` or `::1`. The client normalises `localhost` to the loopback IP, disables environment proxies, rejects redirects and rejects cloud-tagged/URL model names. It never sends the participant's fourth account to the observer model calls.

The client controls its destination, not the server's internal configuration. A local service could itself forward data; this prototype does not verify server egress, and `upstream_service_egress_verified` remains false. Use a service configured for local inference. Source permission and the explicit command are required even when a service happens to be running.

Each observer receives its own prompt. A result must use the required JSON shape and cite accessible evidence IDs. Unsupported fields, inaccessible citations and tool calls are rejected. Accepted text remains an **unreviewed derived interpretation**, never a measurement, an approved personal answer or a completed action. Citation validity does not prove the interpretation is correct. The user must review its meaning.

The token allowance is supplied per call and checked against returned usage. Failed or rejected calls conservatively consume their full allocation. The elapsed-time budget prevents starting further calls after the deadline; each request has a bounded socket timeout. This is not a hard process kill or a guarantee that the model server stops generating after a timeout.

**Integration status:** offline adapter tests pass with an injected transport. No live Ollama service/model was invoked for this release, so real-server compatibility and output quality remain unverified. The mock swarm remains a reference design even when observer prompts use a live model.

## Verify the runtime

```text
python tests/runtime_test.py
```

The offline checks cover observer separation; source-label and cross-reference leaks; the fourth account; preserved unknowns, conflicts and corrections; simulation contamination; invalid measurement promotion; invalid references and duplicate JSON keys; no default network use; swarm dependencies/budget stops; source-level local permission; remote endpoint and redirect rejection; model citation rejection; token accounting; and output-history preservation.

The runtime implements no model training, clinical assessment, biometric collection, sensor control, messaging, payments, public release or hardware/Geode operating procedure. It is an executable foundation for evidence-scoped reflection and a reviewable agent-work plan. See `content/agent-runtime.md` for how it fits the wider Genesis programme.
