from __future__ import print_function
from __future__ import division

import sys, os
import glob
import re
from collections import namedtuple

# Struct types for different lines in the bAbI dataset.
# StoryLine represents "ID text" lines as (int, string)
# QALine represents "ID question answer support" lines as
# (int, string, string, list(int)).
# If tokenized, string fields can be replaced with list(string).
StoryLine = namedtuple("StoryLine", ["id", "text"])
QALine = namedtuple("QALine", ["id", "question", "answer", "support_ids"])

class BabiTaskCorpusReader(object):
    """Corpus reader for the bAbI tasks dataset.

    See https://research.fb.com/downloads/babi/ for details.

    This class exposes a similar interface to NLTK's corpus readers, and should
    be interchangable with them in many applications.

    Example usage:

    import babi_utils
    import nltk
    tok = nltk.tokenize.treebank.TreebankWordTokenizer()
    cr = babi_utils.BabiTaskCorpusReader("/home/babi/en",
                                         tokenizer=tok.tokenize)
    words = list(cr.words())
    print(words[:8])
    # ['John', 'travelled', 'to', 'the', 'hallway', '.', 'Mary', 'journeyed']

    """

    ALL_FILES = [
        'qa10_indefinite-knowledge_test.txt',
        'qa10_indefinite-knowledge_train.txt',
        'qa11_basic-coreference_test.txt',
        'qa11_basic-coreference_train.txt',
        'qa12_conjunction_test.txt',
        'qa12_conjunction_train.txt',
        'qa13_compound-coreference_test.txt',
        'qa13_compound-coreference_train.txt',
        'qa14_time-reasoning_test.txt',
        'qa14_time-reasoning_train.txt',
        'qa15_basic-deduction_test.txt',
        'qa15_basic-deduction_train.txt',
        'qa16_basic-induction_test.txt',
        'qa16_basic-induction_train.txt',
        'qa17_positional-reasoning_test.txt',
        'qa17_positional-reasoning_train.txt',
        'qa18_size-reasoning_test.txt',
        'qa18_size-reasoning_train.txt',
        'qa19_path-finding_test.txt',
        'qa19_path-finding_train.txt',
        'qa1_single-supporting-fact_test.txt',
        'qa1_single-supporting-fact_train.txt',
        'qa20_agents-motivations_test.txt',
        'qa20_agents-motivations_train.txt',
        'qa2_two-supporting-facts_test.txt',
        'qa2_two-supporting-facts_train.txt',
        'qa3_three-supporting-facts_test.txt',
        'qa3_three-supporting-facts_train.txt',
        'qa4_two-arg-relations_test.txt',
        'qa4_two-arg-relations_train.txt',
        'qa5_three-arg-relations_test.txt',
        'qa5_three-arg-relations_train.txt',
        'qa6_yes-no-questions_test.txt',
        'qa6_yes-no-questions_train.txt',
        'qa7_counting_test.txt',
        'qa7_counting_train.txt',
        'qa8_lists-sets_test.txt',
        'qa8_lists-sets_train.txt',
        'qa9_simple-negation_test.txt',
        'qa9_simple-negation_train.txt'
    ]

    def __init__(self, directory, mask="qa*.txt",
                 file_list=ALL_FILES,
                 file_reader=open,
                 tokenizer=lambda s: s.split(),
                 verbose=False):
        """Construct a corpus reader for the bAbI tasks dataset.

        Args:
            directory: (string) path to bAbI text files (e.g. /home/babi/en/)
            mask: (string) file glob to match particular files. Use
                "qa16_*" e.g. to match task 16.
            file_list: (list(string) or None) If None, will glob directory to
                find files. Otherwise, will use the given list of basenames.
            file_reader: (function string -> fd) optional replacement for
                Python's built-in open(...) method, to be used for reading
                from alternative file-like objects.
            tokenizer: function string -> list(string), used to split
                sentences.
            verbose: (bool) if true, will print when reading files.
        """
        self._open = file_reader
        self._tokenizer = tokenizer
        self._verbose = verbose

        if file_list:
            basenames = glob.fnmatch.filter(file_list, mask)
            filenames = [os.path.join(directory, f) for f in basenames]
        else:
            # Glob directory
            pattern = os.path.join(directory, mask)
            filenames = glob.glob(pattern)

        # Filenames of form qaXX_task-name_train.txt
        # Want to sort by XX as a number
        key_fn = lambda f: (int(os.path.basename(f).split("_")[0][2:]), f)
        self._filenames = sorted(filenames, key=key_fn)
        # Filenames should be nonempty!
        assert(self._filenames), "No files found matching [{:s}]".format(mask)

    def filenames(self):
        return self._filenames

    def parse_line(self, line):
        """Parse a single line from the bAbI corpus.

        Line is of one of the two forms:
        ID text
        ID question[tab]answer[tab]supporting fact IDs

        See https://research.fb.com/downloads/babi/

        Args:
            line: (string)

        Returns:
            (id, text) as (int, string)
            OR (id, question, answer, [ids]) as (int, string, string, list(int))
        """
        id_text, rest = line.split(" ", 1)
        id = int(id_text)
        if "\t" in rest:
            question, answer, s_ids_text = rest.split("\t")
            s_ids = map(int, s_ids_text.split())
            return QALine(id, question.strip(), answer.strip(), s_ids)
        else:
            return StoryLine(id, rest.strip())

    def tokenize_parsed_line(self, line):
        if isinstance(line, StoryLine):
            return StoryLine(line.id, self._tokenizer(line.text))
        else:
            return QALine(line.id,
                          self._tokenizer(line.question),
                          self._tokenizer(line.answer),
                          line.support_ids)

    def _line_iterator(self):
        for f in self._filenames:
            if self._verbose:
                print("Reading {:s}".format(os.path.basename(f)), end=" ", 
                      file=sys.stderr)
            with self._open(f) as fd:
                for line in fd:
                    yield line.strip()
            if self._verbose:
                print("...done!", file=sys.stderr)

    def examples(self, tokenize=True):
        """Iterator over complete stories (training examples).

        A story spans multiple lines, of the form:

        1 text one
        2 text two
        3 text three
        4 question[tab]answer[tab]supporting fact IDs

        Args:
            tokenize: (bool) If true, will tokenize text fields.

        Returns:
            iterator yielding list(StoryLine|QALine)
              if tokenize=True, then text, question, and answer will be
              list(string); otherwise they will be plain strings.
        """
        buffer = []
        for line in self._line_iterator():
            parsed = self.parse_line(line)
            if tokenize:
                parsed = self.tokenize_parsed_line(parsed)
            # If new story item, flush buffer.
            if buffer and parsed.id <= buffer[-1].id:
                yield buffer
                buffer = []
            buffer.append(parsed)
        # Flush at end.
        yield buffer
        buffer = []

    def _raw_sents_impl(self, stories=False, questions=False, answers=False):
        for line in self._line_iterator():
            parsed = self.parse_line(line)
            if isinstance(parsed, StoryLine) and stories:
                yield parsed.text
            else:
                if questions:
                    yield parsed.question
                if answers:
                    yield parsed.answer

    def raw_sents(self):
        """Iterator over utterances in the corpus.

        Returns untokenized sentences.

        Returns:
            iterator yielding string
        """
        return self._raw_sents_impl(stories=True,
                                    questions=True,
                                    answers=True)

    def sents(self):
        """Iterator over utterances in the corpus.

        Returns tokenized sentences, a la NLTK.

        Returns:
            iterator yielding list(string)
        """
        for sentence in self.raw_sents():
            yield self._tokenizer(sentence)


    def words(self):
        """Iterator over words in the corpus.

        Returns:
            iterator yielding string
        """
        for sentence in self.sents():
            for word in sentence:
                yield word

