"""Check transferred source facts and mappings; does not claim LLM or official policy validation."""
import json
import unittest
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
CORE=BASE/'xjtlu-major-advisor'
DATA=json.loads((CORE/'references/admission-table.json').read_text(encoding='utf-8'))
ROWS={r['source_row']:r for r in DATA['records']}

class AdmissionTableTests(unittest.TestCase):
    def test_complete_row_ranges_and_scope(self):
        expected=set(range(4,17))|set(range(18,22))|{23}|set(range(25,30))|{31,32}|{34,35,36}|set(range(38,63))
        self.assertEqual(set(ROWS),expected)
        self.assertEqual(len(DATA['records']),53)
        self.assertFalse(DATA['source']['official_authenticity_verified'])
        self.assertIsNone(DATA['source']['applicable_entry_years'])
        self.assertTrue(all(r['grade_cutoff'] is None for r in ROWS.values()))

    def test_direction_specific_campus_and_entry_rule(self):
        self.assertEqual((ROWS[6]['source_campus'],ROWS[6]['grade_rule']),('太仓','not_stated'))
        self.assertEqual((ROWS[16]['source_campus'],ROWS[16]['grade_rule']),('本部','calculus_and_linear_algebra_arithmetic_mean'))
        self.assertNotEqual(ROWS[6]['pathway_id'],ROWS[16]['pathway_id'])

    def test_combinations_and_no_module_not_no_requirement(self):
        self.assertEqual(ROWS[18]['semester2_modules'],['MTH031','PHY005'])
        self.assertEqual(ROWS[31]['semester2_modules'],['MTH031','PHY007'])
        self.assertEqual(ROWS[34]['semester2_modules'],['MTH031','MTH033'])
        self.assertEqual(ROWS[23]['semester2_modules'],['PHY008'])
        self.assertTrue(ROWS[62]['no_specified_module_in_table'])
        self.assertEqual(ROWS[62]['grade_rule'],'calculus')
        self.assertEqual(ROWS[26]['grade_rule'],'calculus')
        self.assertTrue(all(r['module_combination']=='all_of' for r in ROWS.values()))

    def test_catalog_mapping_and_missing_entry_remains(self):
        ids={p.stem for p in (CORE/'references/majors').glob('*.md')}
        self.assertEqual(len(ids),52)
        self.assertEqual(ids-{r['major_id'] for r in ROWS.values()},{'xjtlu-film-and-television-production'})
        for r in ROWS.values():
            self.assertIn(r['major_id'],ids)
            if r['pathway_id']:
                self.assertIn(r['pathway_id'],(CORE/'references/majors'/f"{r['major_id']}.md").read_text(encoding='utf-8'))
            self.assertEqual(r['eligibility_status'],'pending_verification')

if __name__=='__main__':
    unittest.main(verbosity=2)
