"""Publish aggregate weaving progress, never the private ledger or answers."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
COUNTERS = ("planned", "generated", "checked", "accepted", "needs_revision", "rejected", "answered", "simulated_answers", "unfilled", "review_flags")
REVIEW_NOTE = "Checked counts record summary-only AI editorial reviews of the generated pilot questions. They do not establish primary-source close reading, independent human approval, teaching competence or participant answers."


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def validate_counts(counts, label):
    require(isinstance(counts, dict), f"{label} must be an object")
    for key in COUNTERS:
        require(type(counts.get(key)) is int and counts[key] >= 0, f"{label}.{key} must be a nonnegative integer")
    require(counts["accepted"] <= counts["checked"] <= counts["generated"] <= counts["planned"], f"{label} has inconsistent production counts")
    require(counts["accepted"] + counts["needs_revision"] + counts["rejected"] == counts["checked"], f"{label} review decisions do not total checked")
    require(counts["answered"] + counts["simulated_answers"] <= counts["accepted"], f"{label} has answers without accepted questions")
    require(counts["unfilled"] == counts["planned"] - counts["generated"], f"{label} unfilled count is inconsistent")
    require(counts["review_flags"] <= counts["generated"], f"{label} has more flagged than generated questions")


def prepare_snapshot(atlas, report, review_note=REVIEW_NOTE):
    """Validate everything before returning any prospective public mutation."""
    require(report.get("schema") == "aura-weaving-status/1", "Unsupported runtime status schema")
    validate_counts(report.get("counts"), "total")
    source_rows = report.get("territories", [])
    atlas_rows = atlas.get("territories", [])
    require(isinstance(source_rows, list) and isinstance(atlas_rows, list), "Territories must be lists")
    require(len({r["id"] for r in source_rows}) == len(source_rows), "Duplicate territory in report")
    require(len({r["id"] for r in atlas_rows}) == len(atlas_rows), "Duplicate territory in atlas")
    expected = {r["id"]: r for r in atlas_rows}
    actual = {r["id"]: r for r in source_rows}
    require(set(expected) == set(actual), "Report territory IDs do not match the current atlas; no public files changed")
    require(sum(r["quota"] for r in atlas_rows) == atlas["targetQuestions"], "Current atlas quotas do not total its target")
    require(report["counts"]["planned"] == atlas["targetQuestions"], "Report planned total differs from current atlas target")
    require(report.get("jobCount") == atlas.get("plannedBatches"), "Report job count differs from current atlas batch plan")
    rows = []
    for territory in atlas_rows:
        row = actual[territory["id"]]
        validate_counts(row, territory["id"])
        require(row["planned"] == territory["quota"], f"Quota mismatch for {territory['id']}")
        require(row.get("stream") == territory.get("stream"), f"Stream mismatch for {territory['id']}")
        # Copy an explicit allowlist: no question text, reviewer identity, answer
        # reference or future private report field can enter this snapshot.
        rows.append({"id": territory["id"], "title": territory["title"], "stream": territory["stream"], **{key: row[key] for key in COUNTERS}})
    for key in COUNTERS:
        require(sum(r[key] for r in rows) == report["counts"][key], f"Territory totals disagree for {key}")
    streams = {}
    for stream in sorted({r["stream"] for r in rows}):
        streams[stream] = {key: sum(r[key] for r in rows if r["stream"] == stream) for key in COUNTERS}
    require(report.get("streams") == streams, "Runtime stream totals do not reconcile")
    require(type(report.get("complete")) is bool and report["complete"] == (report["counts"]["accepted"] == report["counts"]["planned"]), "Completion flag is inconsistent")
    require(isinstance(review_note, str) and review_note.strip(), "A factual review-scope note is required")
    timestamp = datetime.now(timezone.utc).isoformat()
    snapshot = {"schema": "aura-weaving-status/1", "snapshotAt": timestamp, "atlasSha256": report["atlasSha256"], "counts": {key: report["counts"][key] for key in COUNTERS}, "streams": streams, "territories": rows, "jobCount": report["jobCount"], "complete": report["complete"], "reviewNote": review_note, "note": "Aggregate production snapshot only. Planned, generated, checked, accepted and actual answered counts are distinct; simulated answers are counted separately. No ledger, question payloads, private answers or answer references are included. The hash identifies the ledger's original plan snapshot; current territory IDs, quotas, streams and totals were checked before synchronisation."}
    updated = json.loads(json.dumps(atlas))
    updated["status"] = dict(snapshot["counts"])
    updated["statusSnapshot"] = {"snapshotAt": timestamp, "source": "weaving-status.json", "reviewNote": review_note}
    for territory in updated["territories"]:
        row = actual[territory["id"]]
        territory.update({key: row[key] for key in COUNTERS if key != "planned"})
    return updated, snapshot


def atomic_json(path, value):
    path = Path(path)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    handle, temporary = tempfile.mkstemp(prefix=path.name+".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf8", newline="\n") as stream:
            stream.write(payload)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--review-note", default=REVIEW_NOTE, help="Change only when the actual recorded review scope changes")
    args = parser.parse_args(argv)
    try:
        result = subprocess.run([sys.executable, "-X", "utf8", str(ROOT/"runtime/weave.py"), "status", "--ledger", args.ledger], cwd=ROOT, capture_output=True, text=True, encoding="utf8", timeout=120, check=False)
        require(result.returncode == 0, "Runtime status failed: "+result.stderr.strip())
        report = json.loads(result.stdout)
        atlas_path = ROOT/"data/weaving-atlas.json"
        atlas, snapshot = prepare_snapshot(load(atlas_path), report, args.review_note)
        atomic_json(atlas_path, atlas)
        atomic_json(ROOT/"data/weaving-status.json", snapshot)
        published = ROOT/"docs/data"
        if published.exists():
            if (published/"weaving-atlas.json").exists():
                atomic_json(published/"weaving-atlas.json", atlas)
            # A pre-existing publication data directory receives the new summary;
            # no private file or answer reference is copied.
            atomic_json(published/"weaving-status.json", snapshot)
        print(json.dumps({"synced": True, "counts": snapshot["counts"], "snapshotAt": snapshot["snapshotAt"], "reviewNote": snapshot["reviewNote"]}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(f"Weaving status sync failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
