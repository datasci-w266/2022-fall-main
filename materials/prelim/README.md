# Preliminaries

The traditional prerequisites for a course in Machine Learning include probability, statistics, multivariate calculus, and linear algebra as well as a strong programming background. NLP combines this with a hefty dose of linguistics, although most of this will be introduced as we go along.

This Preliminaries unit contains primers on key concepts from the fields above as they apply to this course and to NLP. This is not intended as a substitute for a proper course in these fields, but can be used as a refresher or as a rough guide to the important concepts with which you should be familiar.

Take some time to read through these - the more familiar you are with this background material, the better shape you'll be in to learn quickly about modern NLP!

### Outline

* [Probability](Probability.ipynb)
* [Linear Algebra](Linear%20Algebra.ipynb)
* [Gradient Descent](Gradient%20Descent.ipynb) and [TensorFlow](../../assignment/a2/tensorflow/tensorflow.ipynb)

## [Probability](Probability.ipynb)

Most modern NLP is statistical in nature, and as such relies heavily on concepts from Probability and Statistics. Here we'll review a few basic concepts that will arise frequently in the course:

* Random variables
* Expected value
* Common probability distributions
* Conditional probability and Bayes' Rule
* Statistical independence


## [Information Theory](../../assignment/a1/information_theory.ipynb)
_**Note:** the Information Theory notebook is assigned as part of [Assignment 1](../../assignment/a1)._

Information Theory is the study of information as a concept that can be *quantified*, *stored*, and *communicated*. Originally formulated by [Claude Shannon](https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication) in 1948, Information Theory helps formalize questions like:
* How much information is contained in language? (*Entropy*)
* How well does my model explain this data? (*Cross-Entropy*)
* How much does one word tell me about what other words are nearby? (*Mutual Information*)

Information Theory forms a useful theoretical basis for many concepts in Machine Learning (especially for Neural Networks) and for many statistical approaches to understanding natural language. (Indeed, both Information Theory and many foundational ideas in NLP emerged from the same source: efforts to decrypt Axis communications during World War II.)


## [Linear Algebra](Linear%20Algebra.ipynb)

With the rise of deep learning, modern NLP increasingly deals with vector representations of words, sentences, and other units of language. For example, by training a *word2vec* model (week 3), we get "word vectors" that allow us to solve analogies using simple arithmetic:

```
v(king) - v(man) + v(woman) ≈ v(queen)
```

More generally, most Neural Network training can be expressed as operations on vectors and matrices. Efficient multiplication of matrices on specialized hardware like [GPUs](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) has helped drive dramatic improvements many NLP tasks, including speech recognition and machine translation. Linear Algebra describes the mathematics of vectors, matrices, and tensors, and gives us powerful tools to manipulate them.


## [Gradient Descent](gradient%20descent.ipynb) and [TensorFlow with Keras](../../assignment/a2/tensorflow.ipynb)
_**Note:** the TensorFlow notebook is assigned as part of [Assignment 2](../../assignment/a2)._

We'll use TensorFlow with Keras frequently in this course, as the main framework for building and training neural networks. While commonly accessed as a Python library, TensorFlow is really a programming language of its own that operates in two phases: graph-building and execution. This makes it easier to set up training for complex models, since gradients can be automatically computed, and also allows for seamlessly running models on GPUs.

Most neural networks are trained using variants of the Gradient Descent algorithm. This works well for a broad array of models, but often requires some tuning and attention. In the [Gradient Descent](Gradient%20Descent.ipynb) notebook, we'll use gradient descent to solve a simple linear regression problem and learn about a few important hyperparameters. If you're rusty on ML, we recommend starting with this notebook before undertaking the TensorFlow tutorial.

In the [TensorFlow](../../assignment/a2/tensorflow.ipynb) notebook, we'll introduce the basics of the TensorFlow Python API and implement a simple neural network on toy data, similar to the [TensorFlow Playground](https://github.com/tensorflow/playground).

