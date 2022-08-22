import hashlib
import unittest
import yaml

class AnswersTest(unittest.TestCase):
    REQUIRED_ANSWERS = [
            'additional_logistics_comments',
            'async_source',
            'beyond_late_days',
            'competing_worries',
            'email',
            'first_name',
            'general_questions',
            'grade_A-',
            'grade_A',
            'grade_B',
            'grade_B+',
            'last_name',
            'late_days',
            'late_days_per',
            'late_penalty',
            'logistics_approach',
            'main_components',
            'past_hard_deadline_grade',
            'private_questions',
            'project_components']

    ANSWER_HASHES = {
        'async_source': 'af14f', 'beyond_late_days': '712b8', 'competing_worries': '306a5', 'general_questions': '3dc52', 'grade_A': '7a80b', 'grade_A-': 'b5fa3', 'grade_B': 'b9885', 'grade_B+': 'af75c', 'late_days': '9386a', 'late_days_per': '5ddcb', 'late_penalty': '15fde', 'main_components': '87d41', 'past_hard_deadline_grade': 'e4012', 'private_questions': 'a048f', 'project_components': '9f392'}

    def setUp(self):
        with open('answers', 'r') as f:
            self.answers = yaml.safe_load(f.read())

    def test_keys(self):
        self.assertEqual(
                sorted(AnswersTest.REQUIRED_ANSWERS),
                sorted(self.answers.keys()))

    def test_simple_hash(self):
        results = {}
        for k, v in AnswersTest.ANSWER_HASHES.items():
          h = hashlib.sha256()
          h.update(k.encode('utf-8'))
          h.update(','.join(str(self.answers[k])).encode('utf-8'))
          self.assertEqual(h.hexdigest()[:5], v, msg='%s incorrect' % k)

    def test_placeholder(self):
        self.assertTrue(self.answers['email'].endswith('@berkeley.edu'))
        self.assertFalse(self.answers['email'].startswith('placeholder'))

    def test_names(self):
        self.assertNotEqual(self.answers['last_name'], 'Lastname')
        self.assertNotEqual(self.answers['first_name'], 'Firstname')


if __name__ == '__main__':
    unittest.main()
