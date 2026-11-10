# Frontend contract checks

Run the static studio's repeatable logic checks from the repository root:

```text
node tests/frontend-contracts.cjs
```

Use Node.js 20 or newer. No package installation, network connection, browser, model service or credentials are required. The harness reads the committed public files in `docs/data/` and the actual `docs/assets/studio.js`. Regenerate the public data first when changing its source material.

The command exits with a non-zero status on failure. A successful run currently reports **30 frontend logic contracts passed**.

## What is checked

- Default memory-only work, explicit browser-storage opt-in, scoped opt-out, and a visible failed-save state.
- Personal-answer import validation, simulation/source separation, unknown IDs and excessive answer lengths.
- Fictional observer labels that cannot disappear merely by changing the basis selector.
- Curriculum rendering against the supplied entry counts.
- Deep Interview seed/context attribution, blank generated answers, participant recording, parent chains and parent-version snapshots.
- Compatibility with older workbooks, missing/cyclic/duplicate parent rejection, source-label checks and the 1,000-turn import cap.
- Actual JSON and Markdown export payloads, captured in memory without writing personal output files.
- Atlas quota accounting, bounded job-packet templates, preserved sources/gaps and input-time labelling.

All participant text used by the checks is a temporary `QA ONLY` fixture. Storage is an isolated Map, and every fetch is restricted to the public data fixtures. The harness never opens real browser storage, sends a network request or writes participant answers into the repository.

## Test boundary

This is an isolated VM test with a deliberately small DOM double. It does **not** establish correct visual layout, real browser download behaviour, browser-storage persistence, keyboard operation, accessible names or screen-reader behaviour. It also does not certify semantic quality, clinical validity or security of the wider system.

For a substantive interface change, also serve `docs/` locally and check the relevant flow in a real browser. Useful checks include narrow-screen overflow; labelled controls; keyboard focus; storage consent and reload; import confirmation; and a Deep Interview seed → recorded parent → recorded child → export/import round trip.

The harness inserts a test-only access hook immediately before the frontend's closing IIFE. It does not modify production files or publish a testing API. If the frontend wrapper or private function names are intentionally refactored, update the hook and test adapters while preserving the behaviour being tested. A changed number of authored questions or generated atlas records should be reflected by the public data, not by fabricating a passing count.
