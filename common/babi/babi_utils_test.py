#!/usr/bin/env python

# Run with:
# python -m unittest -v Common.babi.babi_utils_test

import os
import unittest

import babi_utils
from babi_utils import StoryLine, QALine
import utils

def testdata_dir():
    this_dir = os.path.dirname(__file__)
    return os.path.join(this_dir, "testdata")

EXPECTED_EXAMPLES = [
    [StoryLine(1, "Foo bar baz ."),
     StoryLine(2, "This is the second sentence ."),
     QALine(3, "What is a baz ?", "Foo", [1])],
    [StoryLine(1, "Spam and eggs ."),
     StoryLine(2, "Eggs and spam ."),
     QALine(3, "What goes with eggs ?", "Spam", [1, 2])]
]

EXPECTED_RAW_SENTS = [
    "Foo bar baz .",
    "This is the second sentence .",
    "What is a baz ?", "Foo",
    "Spam and eggs .",
    "Eggs and spam .",
    "What goes with eggs ?", "Spam"
]

EXPECTED_SENTS = [
    ["foo", "bar", "baz", "."],
    ["this", "is", "the", "second", "sentence", "."],
    ["what", "is", "a", "baz", "?"], ["foo"],
    ["spam", "and", "eggs", "."],
    ["eggs", "and", "spam", "."],
    ["what", "goes", "with", "eggs", "?"], ["spam"]
]

class TestCorpus(unittest.TestCase):

    def setUp(self):
        self.tokenizer = lambda s: s.lower().split()

        file_list = ["qa42_fake_data.txt", "doesnt_exist.txt"]
        self.corpus = babi_utils.BabiTaskCorpusReader(
            testdata_dir(), file_list=file_list,
            tokenizer=self.tokenizer)

    def test_raw_sents(self):
        raw_sents = list(self.corpus.raw_sents())
        self.assertEqual(raw_sents, EXPECTED_RAW_SENTS)

    def test_sents(self):
        sents = list(self.corpus.sents())
        self.assertEqual(sents, EXPECTED_SENTS)

    def test_words(self):
        words = list(self.corpus.words())
        expected_words = list(utils.flatten(EXPECTED_SENTS))
        self.assertEqual(words, expected_words)

    def test_examples(self):
        examples = list(self.corpus.examples(tokenize=False))
        self.assertEqual(examples, EXPECTED_EXAMPLES)


