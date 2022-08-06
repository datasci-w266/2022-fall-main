#!/usr/bin/env python

# Run with:
# python -m unittest -v Common.tsv_corpus_test

import os
import unittest

import tsv_corpus
import utils

def testdata_dir():
    this_dir = os.path.dirname(__file__)
    return os.path.join(this_dir, "testdata")

EXPECTED_SENTENCES = [
    ["foo", "bar", "baz"],
    ["spam", "eggs"],
    ["this", "is", "a", "longer", "sentence"],
    ["the", "fourth", "token", "has spaces"]
]

class TestCorpus(unittest.TestCase):

    def setUp(self):
        self.corpus_tsv = os.path.join(testdata_dir(), "corpus.tsv")
        self.corpus = tsv_corpus.TSVCorpusReader(self.corpus_tsv,
                                                 preload=False)

    def test_sents(self):
        sents = list(self.corpus.sents())
        self.assertEqual(sents, EXPECTED_SENTENCES)

    def test_words(self):
        expected_words = utils.flatten(EXPECTED_SENTENCES)
        words = list(self.corpus.words())
        self.assertEqual(words, expected_words)


class TestCorpusWithPreload(unittest.TestCase):

    def setUp(self):
        self.corpus_tsv = os.path.join(testdata_dir(), "corpus.tsv")
        self.corpus = tsv_corpus.TSVCorpusReader(self.corpus_tsv,
                                                 preload=True)

    def test_sents(self):
        sents = list(self.corpus.sents())
        self.assertEqual(sents, EXPECTED_SENTENCES)

    def test_words(self):
        expected_words = utils.flatten(EXPECTED_SENTENCES)
        words = list(self.corpus.words())
        self.assertEqual(words, expected_words)

