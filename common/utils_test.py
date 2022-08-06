#!/usr/bin/env python

# Run with:
# python -m unittest -v common.utils_test

import unittest
from . import utils

import nltk
import numpy as np

from . import vocabulary  # from this module, for testing preprocessing code

class TestMiscHelpers(unittest.TestCase):

    def test_flatten(self):
        l1 = [1,2,3]
        l2 = [4,5,6]
        self.assertEqual(utils.flatten([l1,l2]), [1,2,3,4,5,6])


    def test_pretty_timedelta(self):
        since = 12345
        until = since + 3934 # 1 hr, 5 min, 34 sec
        res = utils.pretty_timedelta(since=since, until=until)
        self.assertEqual(res, "1:05:34")


class TestWordProcessing(unittest.TestCase):

    def test_canonicalize_digits(self):
        self.assertEqual(utils.canonicalize_digits("123"), "DGDGDG")
        self.assertEqual(utils.canonicalize_digits("1.5"), "DG.DG")
        self.assertEqual(utils.canonicalize_digits("1:05:34"), "DG:DGDG:DGDG")
        # Should pass-through anything with alphanumeric chars
        self.assertEqual(utils.canonicalize_digits("97se"), "97se")

    def test_canonicalize_word(self):
        wordset = {"foo", "bar", "baz", "DGDG"}
        self.assertEqual(utils.canonicalize_word("foo", wordset=wordset), "foo")
        self.assertEqual(utils.canonicalize_word("FOO", wordset=wordset), "foo")
        self.assertEqual(utils.canonicalize_word("14", wordset=wordset), "DGDG")
        self.assertEqual(utils.canonicalize_word("14", wordset=wordset, digits=False), "<unk>")
        self.assertEqual(utils.canonicalize_word("ASdf", wordset=None), "asdf")

    def test_canonicalize_words(self):
        wordset = {"foo", "bar", "baz", "DGDG"}
        res = utils.canonicalize_words(["foo", "BAR", "foosball", "14"],
                wordset=wordset)
        self.assertEqual(res, ["foo", "bar", "<unk>", "DGDG"])


class TestDataLoading(unittest.TestCase):

    def test_get_corpus(self):
        self.assertEqual(utils.get_corpus("treebank"), nltk.corpus.treebank)

    def test_build_vocab(self):
        corpus = utils.get_corpus("treebank")
        vocab = utils.build_vocab(corpus, V=1000)
        self.assertTrue(isinstance(vocab, vocabulary.Vocabulary))
        self.assertEqual(vocab.size, 1000)
        self.assertEqual(vocab.word_to_id[vocab.START_TOKEN], 0)
        self.assertEqual(vocab.word_to_id[vocab.END_TOKEN], 1)
        self.assertEqual(vocab.word_to_id[vocab.UNK_TOKEN], 2)
        self.assertEqual(vocab.word_to_id["work"], 397)
        self.assertEqual(vocab.word_to_id["ability"], 999)

    def test_get_train_test_sents(self):
        corpus = utils.get_corpus("treebank")
        train, test = utils.get_train_test_sents(corpus, shuffle=42)
        self.assertEqual(len(train), 3131)
        self.assertEqual(len(test), 783)
        self.assertEqual(test[0][:2], ["Ed", "Macheski"])

    def test_preprocess_sentences(self):
        words = "foo bar baz".split()
        vocab = vocabulary.Vocabulary(words)
        s1 = "foo bar BAR".split()
        s2 = "FOO bar BAZ".split()
        res = utils.preprocess_sentences([s1, s2], vocab)
        expected_ids = vocab.words_to_ids("<s> foo bar bar <s> foo bar baz <s>".split())
        self.assertTrue(np.array_equal(res, np.array(expected_ids)))

    def test_preprocess_sentences_with_eos(self):
        words = "foo bar baz".split()
        vocab = vocabulary.Vocabulary(words)
        s1 = "foo bar BAR".split()
        s2 = "FOO bar BAZ".split()
        res = utils.preprocess_sentences([s1, s2], vocab, use_eos=True)
        expected_ids = vocab.words_to_ids("<s> foo bar bar </s> <s> foo bar baz </s>".split())
        self.assertTrue(np.array_equal(res, np.array(expected_ids)))

    def test_preprocess_sentences_emit_tokens(self):
        words = "foo bar baz".split()
        vocab = vocabulary.Vocabulary(words)
        s1 = "foo bar BAR".split()
        s2 = "FOO bar BAZ".split()
        res = utils.preprocess_sentences([s1, s2], vocab, use_eos=True,
                                         emit_ids=False)
        expected_tokens = "<s> foo bar bar </s> <s> foo bar baz </s>".split()
        self.assertTrue(np.array_equal(res, np.array(expected_tokens)))


class TestBatchAndWindowFunctions(unittest.TestCase):

    def test_rnnlm_batch_generator(self):
        ids = np.arange(15)
        batches = list(utils.rnnlm_batch_generator(ids, batch_size=2,
            max_time=3))
        self.assertEqual(len(batches), 3)
        self.assertTrue(np.array_equal(batches[0][0], [[0,1,2],[7,8,9]]))     # x0
        self.assertTrue(np.array_equal(batches[0][1], [[1,2,3],[8,9,10]]))    # y0
        self.assertTrue(np.array_equal(batches[1][0], [[3,4,5],[10,11,12]]))  # x1
        self.assertTrue(np.array_equal(batches[1][1], [[4,5,6],[11,12,13]]))  # y1
        self.assertTrue(np.array_equal(batches[2][0], [[6],[13]]))            # x2
        self.assertTrue(np.array_equal(batches[2][1], [[7],[14]]))            # y2

    def test_build_windows(self):
        ids = np.arange(7)
        windows = utils.build_windows(ids, 4, shuffle=False)
        self.assertEqual(len(windows), 3)
        self.assertTrue(np.array_equal(windows[0], [0,1,2,3,4]))
        self.assertTrue(np.array_equal(windows[1], [1,2,3,4,5]))
        self.assertTrue(np.array_equal(windows[2], [2,3,4,5,6]))


    def test_batch_generator(self):
        ids = np.arange(10)
        batches = list(utils.batch_generator(ids, batch_size=4))
        self.assertEqual(len(batches), 3)
        self.assertTrue(np.array_equal(batches[0], [0,1,2,3]))
        self.assertTrue(np.array_equal(batches[1], [4,5,6,7]))
        self.assertTrue(np.array_equal(batches[2], [8,9]))

    def test_multi_batch_generator(self):
        ids = np.arange(10)
        targets = ids + 10
        batches = list(utils.multi_batch_generator(4, ids, targets))
        self.assertEqual(len(batches), 3)
        self.assertTrue(np.array_equal(batches[0], ([0,1,2,3], [10,11,12,13])))
        self.assertTrue(np.array_equal(batches[1], ([4,5,6,7], [14,15,16,17])))
        self.assertTrue(np.array_equal(batches[2], ([8,9], [18,19])))


if __name__ == '__main__':
    unittest.main()

