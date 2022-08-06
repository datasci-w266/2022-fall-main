import answers_helper
import unittest

class TestAnswersHelpers(unittest.TestCase):

  def test_parse_shapes(self):
    self.assertFalse(answers_helper.parse_shape(''))
    self.assertFalse(answers_helper.parse_shape('FOO'))
    self.assertFalse(answers_helper.parse_shape('1, 2, 3'))
    self.assertFalse(answers_helper.parse_shape('1,2,3'))
    self.assertFalse(answers_helper.parse_shape('A, B, C'))

    self.assertEqual(['1'], answers_helper.parse_shape('[1]'))
    self.assertEqual(['1', '2', '3'], answers_helper.parse_shape('[1, 2,3]'))
    self.assertEqual(['1', '2', '3'], answers_helper.parse_shape([1, 2,3]))
    self.assertEqual(['1', '2', '3'], answers_helper.parse_shape([1, '2',3]))
    self.assertEqual(['A', '2', 'C'], answers_helper.parse_shape('[A, 2,C]'))
    self.assertEqual(['A', '2', 'C'], answers_helper.parse_shape(['A', 2,'C']))


if __name__ == '__main__':
  unittest.main()
