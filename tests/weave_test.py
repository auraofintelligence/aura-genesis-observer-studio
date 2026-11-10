"""Offline planner, provenance, duplicate and review-state tests."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("aura_weave",ROOT/"runtime/weave.py")
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)


class WeavingTests(unittest.TestCase):
    def setUp(self):
        parent=(ROOT/".private/weave-test-tmp").resolve()
        self.assertTrue(parent.is_relative_to(ROOT.resolve()))
        parent.mkdir(parents=True,exist_ok=True)
        self.tmp=tempfile.TemporaryDirectory(dir=parent)
        self.base=Path(self.tmp.name)
        atlas=w.read_json(ROOT/"data/weaving-atlas.json")
        atlas["territories"]=[copy.deepcopy(atlas["territories"][0]),copy.deepcopy(atlas["territories"][60])]
        for t in atlas["territories"]:t["quota"]=50
        atlas["targetQuestions"]=100
        (self.base/"atlas.json").write_text(json.dumps(atlas),encoding="utf8")
        (self.base/"sources.json").write_text((ROOT/"data/sources.json").read_text(encoding="utf8"),encoding="utf8")
        (self.base/"questionnaire.json").write_text(json.dumps({"domains":[{"questions":[{"prompt":"Which observation would change your chosen teaching plan before another learner attempts the task?"}]}]}),encoding="utf8")
        self.ledger=self.base/"ledger"
        w.plan(self.base/"atlas.json",self.ledger)

    def tearDown(self):
        self.tmp.cleanup()

    def batch(self, job="T061-B01", count=2):
        p=w.packet(self.ledger,job)
        t=p["brief"]["territory"];d=p["brief"]["dimensions"]
        questions=[]
        prompts=["How would a learner demonstrate a skill in an unfamiliar setting, and which detail would distinguish independent understanding from copying your example?", "When two plausible explanations of a learner's pause compete, what respectful next question would leave their own account open rather than deciding their motive?"]
        for i in range(count):
            questions.append({"id":p["brief"]["availableSlotIds"][i],"prompt":prompts[i],"tags":["teaching","evidence"],"sourceRefs":[t["sourceRefs"][0]],"provenance":{"kind":"authored_synthesis","sourceNotes":"Authored from the source catalogue's teaching purpose; no primary passage quotation is claimed."},"context":d["teacherContexts" if t["stream"]=="teacher" else "lifeContexts"][0],"operation":d["inquiryOperations"][0],"depth":d["coverageDepths"][1],"observerView":d["observerViews"][3],"selfLens":d["selfLenses"][1],"gap":"Distinguishes repeated explanation from practical transfer and learner meaning.","transfer":"Choose a useful next teaching encounter based on observed independent action.","premiseMode":"open_or_hypothetical","privateAssumptions":False,"diagnosticInference":False})
        return {"schema":w.SCHEMA,"jobId":job,"territoryId":t["id"],"domainId":t["domainId"],"author":{"kind":"agent","name":"Test author","runId":"offline-fixture"},"questions":questions,"generationNotes":"Partial test batch; invented prompts are not actual answers or measured outcomes."}

    def import_data(self,batch,name="batch.json",revise=False):
        path=self.base/name;path.write_text(json.dumps(batch),encoding="utf8")
        return w.import_batch(self.ledger,path,revise)

    def test_plan_does_not_create_question_text_or_completion(self):
        r=w.report(self.ledger)
        self.assertEqual(r["counts"]["planned"],100)
        self.assertEqual(r["jobCount"],2)
        self.assertEqual(r["counts"]["generated"],0)
        self.assertEqual(r["counts"]["checked"],0)
        self.assertEqual(r["counts"]["answered"],0)
        self.assertFalse(r["complete"])

    def test_plan_index_is_deterministic_and_cannot_overwrite_ledger(self):
        other=self.base/"other"
        w.plan(self.base/"atlas.json",other)
        self.assertEqual((self.ledger/"jobs.jsonl").read_bytes(),(other/"jobs.jsonl").read_bytes())
        with self.assertRaises(w.WeavingError):w.plan(self.base/"atlas.json",self.ledger)

    def test_packet_has_topic_sources_schema_and_correct_teaching_context(self):
        p=w.packet(self.ledger,"T061-B01")
        self.assertEqual(p["brief"]["territory"]["stream"],"teacher")
        self.assertIn("T60",[s["id"] for s in p["brief"]["sources"]])
        self.assertIn("requiredOutputSchema",p)
        self.assertIn("not complete primary-source passages",p["brief"]["sourceStatus"])
        self.assertEqual(len(p["brief"]["availableSlotIds"]),50)

    def test_import_is_generated_not_checked_or_accepted(self):
        self.import_data(self.batch())
        c=w.report(self.ledger)["counts"]
        self.assertEqual((c["generated"],c["checked"],c["accepted"],c["answered"]),(2,0,0,0))
        self.assertEqual(c["unfilled"],98)

    def test_generator_cannot_assign_accepted_state(self):
        b=self.batch();b["questions"][0]["status"]="accepted"
        with self.assertRaises(w.WeavingError):self.import_data(b)
        self.assertEqual(w.report(self.ledger)["counts"]["generated"],0)

    def test_explicit_review_and_actual_answers_are_independent(self):
        self.import_data(self.batch())
        with self.assertRaises(w.WeavingError):w.answer(self.ledger,"W-T061-0001","private-answer","Reviewer","actual")
        w.review(self.ledger,["W-T061-0001","W-T061-0002"],"Named reviewer","accepted","Read both prompts and verified distinct teaching purposes.")
        w.answer(self.ledger,"W-T061-0001","private/actual-answer.json","Recorder","actual")
        w.answer(self.ledger,"W-T061-0002","private/simulated-answer.json","Recorder","simulation")
        c=w.report(self.ledger)["counts"]
        self.assertEqual((c["generated"],c["checked"],c["accepted"],c["answered"],c["simulated_answers"]),(2,2,2,1,1))

    def test_wrong_slot_source_domain_and_dimension_are_rejected_atomically(self):
        mutations=[("id","W-T001-0001"),("sourceRefs",["NOT-A-SOURCE"]),("context","Unregistered context")]
        for field,value in mutations:
            with self.subTest(field=field):
                b=self.batch();b["questions"][1][field]=value
                with self.assertRaises(w.WeavingError):self.import_data(b)
                self.assertEqual(w.report(self.ledger)["counts"]["generated"],0)
        b=self.batch();b["domainId"]="wrong-domain"
        with self.assertRaises(w.WeavingError):self.import_data(b)

    def test_duplicate_and_seed_reuse_rejected(self):
        b=self.batch();b["questions"][1]["prompt"]=b["questions"][0]["prompt"].upper()+"!!!"
        with self.assertRaisesRegex(w.WeavingError,"duplicate"):self.import_data(b)
        b=self.batch(count=1);b["questions"][0]["prompt"]="Which observation would change your chosen teaching plan before another learner attempts the task?"
        with self.assertRaisesRegex(w.WeavingError,"seed library"):self.import_data(b)

    def test_duplicate_across_territories_rejected(self):
        self.import_data(self.batch(count=1))
        other=self.batch("T001-B01",count=1)
        with self.assertRaisesRegex(w.WeavingError,"another generated slot"):self.import_data(other,"other.json")

    def test_near_duplicate_is_flagged_without_automatic_acceptance(self):
        b=self.batch()
        b["questions"][1]["prompt"]=b["questions"][0]["prompt"].replace("unfamiliar setting","different classroom")
        r=self.import_data(b)
        self.assertIn("W-T061-0002",r["reviewFlags"])
        self.assertEqual(w.report(self.ledger)["counts"]["accepted"],0)

    def test_provenance_and_unqualified_private_premises_rejected(self):
        b=self.batch();b["questions"][0]["provenance"]["kind"]="measured"
        with self.assertRaises(w.WeavingError):self.import_data(b)
        b=self.batch();b["questions"][0]["prompt"]="How did your wife respond to your teaching programme, and what did she learn from the experience?"
        with self.assertRaisesRegex(w.WeavingError,"private-life premise"):self.import_data(b)

    def test_revision_requires_review_request_and_preserves_history(self):
        b=self.batch(count=1);self.import_data(b)
        b["questions"][0]["prompt"]="Which feature of a learner-chosen demonstration would distinguish remembering a sequence from adapting it thoughtfully when the available materials change?"
        with self.assertRaises(w.WeavingError):self.import_data(b,"revision.json",True)
        w.review(self.ledger,["W-T061-0001"],"Reviewer","needs_revision","Make the transfer condition concrete before accepting this prompt.")
        repair_packet=w.packet(self.ledger,"T061-B01",revision=True)
        self.assertEqual(repair_packet["brief"]["availableSlotIds"],["W-T061-0001"])
        self.assertIn("concrete",repair_packet["brief"]["revisionRequests"][0]["reviewNote"])
        self.import_data(b,"revision.json",True)
        c=w.report(self.ledger)["counts"]
        self.assertEqual((c["generated"],c["checked"],c["accepted"]),(1,0,0))
        with w.connect(self.ledger) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM events WHERE kind='question_revision_previous'").fetchone()[0],1)


if __name__=="__main__":unittest.main()
