from __future__ import print_function
from __future__ import division

import sys, os

class TSVCorpusReader(object):
    """Corpus reader for TSV files.

    Input files are assumed to contain one sentence per line, with tokens
    separated by tabs:

    foo[tab]bar[tab]baz
    span[tab]eggs

    Would correspond to the two-sentence corpus:
        ["foo", "bar", "baz"],
        ["spam", "eggs"]

    """

    def __init__(self, sentence_file, preload=True, file_reader=open):
        """Construct a corpus reader for the given file.

        Args:
            sentence_file: (string) path to a TSV file with one sentence per
                line.
            preload: (bool) If true, will read entire corpus to memory on
                construction. Otherwise, will load on-demand.
            file_reader: (function string -> fd) optional replacement for
                Python's built-in open(...) method, to be used for reading
                from alternative file-like objects.
        """
        self._open = file_reader
        self._sentence_file = sentence_file
        self._sentence_cache = []

        if preload:
            self._sentence_cache = list(self.sents())

    def _line_iterator(self):
        with self._open(self._sentence_file) as fd:
            for line in fd:
                yield line.strip()

    def sents(self):
        """Iterator over sentences in the corpus.

        Yields:
            list(string) of tokens
        """
        if self._sentence_cache:
            for sentence in self._sentence_cache:
                yield sentence
        else:
            # If no cache, actually read the file.
            for line in self._line_iterator():
                yield line.split("\t")

    def words(self):
        """Iterator over words in the corpus.

        Yields:
            (string) tokens
        """
        for sentence in self.sents():
            for word in sentence:
                yield word

