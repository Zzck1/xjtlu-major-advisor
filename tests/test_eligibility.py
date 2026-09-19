"""Executable reference model for synthetic qualification cases, not the LLM runtime.
All identifiers and thresholds are fictional. Standard library only.
"""
import json, unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
FIXTURE=json.loads((HERE/'fixtures/fictional-policy.json').read_text(encoding='utf-8'))

def decide(fixture, year, identity, major_id, scores, policy_conflict=False):
    scope=fixture['scope']; policy=fixture['policy']
    if policy_conflict or not policy.get('applicability_complete') or year!=scope['entry_year'] or identity!=scope['entry_identity']:
        return 'pending_verification'
    rules=[r for r in policy['rules'] if r['major_id']==major_id]
    if not rules: return 'pending_verification'
    if any(r.get('conditions_complete') is False for r in rules): return 'pending_verification'
    unknown=False
    for rule in rules:
        score=scores.get(rule.get('required_course'))
        if score is None: unknown=True; continue
        if rule.get('operator')!='>=': return 'pending_verification'
        if score < rule['minimum']: return 'confirmed_ineligible'
    return 'pending_verification' if unknown or not policy.get('conditions_complete') else 'confirmed_eligible'

class EligibilityTests(unittest.TestCase):
    def test_fixture_boundary_scope_and_unknown(self):
        for c in FIXTURE['unit_cases']:
            with self.subTest(c['case_id']):
                actual=decide(FIXTURE,c['entry_year'],c['entry_identity'],c['major_id'],{c['student_course']:c['student_score']})
                self.assertEqual(c['expected'],actual)

    def test_only_one_or_two_eligible_without_padding(self):
        for code,expected in ((65,{'TEST-MAJOR-A','TEST-MAJOR-B'}),(55,{'TEST-MAJOR-A'})):
            scores={'TEST-MATH':65,'TEST-CODE':code,'TEST-WRITE':55}
            actual={r['major_id'] for r in FIXTURE['policy']['rules'] if decide(FIXTURE,2099,'TEST-ENTRY',r['major_id'],scores)=='confirmed_eligible'}
            self.assertEqual(expected,actual)

    def test_grade_correction_and_policy_conflict(self):
        self.assertEqual('confirmed_ineligible',decide(FIXTURE,2099,'TEST-ENTRY','TEST-MAJOR-B',{'TEST-CODE':55}))
        self.assertEqual('confirmed_eligible',decide(FIXTURE,2099,'TEST-ENTRY','TEST-MAJOR-B',{'TEST-CODE':75}))
        self.assertEqual('pending_verification',decide(FIXTURE,2099,'TEST-ENTRY','TEST-MAJOR-B',{'TEST-CODE':75},policy_conflict=True))

    def test_fixture_never_uses_real_school_identifiers(self):
        self.assertTrue(all(r['major_id'].startswith('TEST-') for r in FIXTURE['policy']['rules']))
        self.assertNotIn('xjtlu-',json.dumps(FIXTURE))

if __name__=='__main__': unittest.main(verbosity=2)
