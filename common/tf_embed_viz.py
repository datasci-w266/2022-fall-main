from __future__ import print_function
from __future__ import division

import sys, os

import tensorflow as tf
from tensorboard.plugins import projector

def mkdirp(dirname):
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

def WriteEmbeddings(Wv, vocab):
    assert(len(Wv.shape) == 2)
    import vocabulary
    if isinstance(vocab, list):
        words = vocab
    elif isinstance(vocab, vocabulary.Vocabulary):
        words = vocab.ids_to_words(range(Wv.shape[0]))
    else:
        raise ValueError("Invalid vocabulary format; must be list(str) or "
                         "vocabulary.Vocabulary.")

    assert(len(words) == Wv.shape[0])
    ev = TFEmbeddingVizWrapper()
    ev.write_vocab_file(words=words)
    ev.write_embeddings(Wv)

class TFEmbeddingVizWrapper(object):
    """Wrapper class to handle vizualizing an embedding matrix with TensorBoard.

    Based on https://www.tensorflow.org/how_tos/embedding_viz/, but attempting
    to hide some of the boilerplate involved in setting up a graph, session,
    checkpoints, etc.
    """

    def __init__(self, LOGDIR="tf_embedding_viz"):
        mkdirp(LOGDIR)

        self.LOGDIR = LOGDIR
        self.VOCAB_FILE_BASE = "metadata.tsv"
        self.VOCAB_FILE = os.path.join(LOGDIR, self.VOCAB_FILE_BASE)
        self.CHECKPOINT_FILE = os.path.join(LOGDIR, "model.ckpt")

    def write_vocab_file(self, words):
        """Write a vocab list to a file.

        Args:
          words: (list of string)
        """
        with open(self.VOCAB_FILE, 'w') as fd:
            for word in words:
                fd.write(word + "\n")
        print("Vocabulary ({:,} words) written to '{:s}'".format(len(words),
                                                                 self.VOCAB_FILE))

    def write_embeddings(self, Wv, name="WordVectors"):
        """Write embedding matrix to the right place.

        Args:
          Wv: (numpy.ndarray) |V| x d matrix of word embeddings
        """
        #with tf.Graph().as_default(), tf.Session() as session:
        with tf.Graph().as_default(), tf.compat.v1.Session() as session:
            ##
            # Feed embeddings to tf, and save.
            embedding_var = tf.Variable(Wv, name=name, dtype=tf.float32)
            session.run(tf.compat.v1.global_variables_initializer())

            saver = tf.compat.v1.train.Saver()
            saver.save(session, self.CHECKPOINT_FILE, 0)

            ##
            # Save metadata
            summary_writer = tf.compat.v1.summary.FileWriter(self.LOGDIR)
            config = projector.ProjectorConfig()
            embedding = config.embeddings.add()
            embedding.tensor_name = embedding_var.name
            embedding.metadata_path = self.VOCAB_FILE_BASE
            projector.visualize_embeddings(summary_writer, config)

        msg = "Saved {s0:d} x {s1:d} embedding matrix '{name}'"
        msg += " to LOGDIR='{logdir}'"
        print(msg.format(s0=Wv.shape[0], s1=Wv.shape[1], name=name,
                         logdir=self.LOGDIR))

        print("To view, run:")
        print("\n  tensorboard --logdir=\"{logdir}\"\n".format(logdir=self.LOGDIR))
        print("and navigate to the \"Embeddings\" tab in the web interface.")


