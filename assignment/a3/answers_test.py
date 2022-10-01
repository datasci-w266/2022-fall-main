import hashlib
import unittest
import yaml

class AnswersTest(unittest.TestCase):

    def setUp(self):
        with open('answers', 'r') as f:
            self.answers = yaml.safe_load(f.read())

    def test_correct_num_questions(self):
            self.assertEqual(23, len(self.answers))



if __name__ == '__main__':
    unittest.main()

