#!/usr/bin/env python

# Run with:
# python -m unittest -v common.vocabulary_test

import unittest
from . import vocabulary

import numpy as np

class TestVocabulary(unittest.TestCase):

    def setUp(self):
        self._words = "foo bar baz foosball 42 foo 42".split()
        self._vocab = vocabulary.Vocabulary(self._words)

    def test_vocabulary_simple(self):
        vocab = self._vocab  # use default test instance
        self.assertEqual(vocab.size, 5+3)
        for w in self._words:
            self.assertIn(w, vocab.word_to_id)

    def test_vocabulary_truncate(self):
        words = "foo bar baz foosball 42 foo 42".split()
        # Should drop three words to make room for special tokens
        vocab = vocabulary.Vocabulary(words, size=5)
        self.assertEqual(vocab.size, 5)
        self.assertIn("foo", vocab.word_to_id)
        self.assertIn("42", vocab.word_to_id)
        self.assertNotIn("foosball", vocab.word_to_id)

    def test_pad_sentence(self):
        vocab = self._vocab  # use default test instance
        self.assertEqual(vocab.pad_sentence("foo bar".split()),
                         "<s> foo bar </s>".split())
        self.assertEqual(vocab.pad_sentence("foo bar".split(), use_eos=False),
                         "<s> foo bar".split())

    def test_sentence_to_ids(self):
        vocab = self._vocab  # use default test instance

        self.assertEqual(vocab.sentence_to_ids("foo bar".split()),
            [vocab.START_ID, vocab.word_to_id["foo"], vocab.word_to_id["bar"],
                vocab.END_ID])

        self.assertEqual(vocab.sentence_to_ids("foo bar".split(), use_eos=False),
            [vocab.START_ID, vocab.word_to_id["foo"], vocab.word_to_id["bar"]])




if __name__ == '__main__':
    unittest.main()
