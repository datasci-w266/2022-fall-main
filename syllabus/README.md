# DATASCI W266: Natural Language Processing With Deep Learning

[Course Overview](#course-overview)  
[Course Evaluation](#course-evaluation)  
[Final Project](#final-project)  
[Course Resources](#course-resources)  
[Tentative Schedule and Readings](#tentative-schedule-and-readings)  


## Course Overview

**Course Description**
Understanding language is fundamental to human interaction. Our brains have evolved language-specific circuitry that helps us learn it very quickly; however, this also means that we have great difficulty explaining how exactly meaning arises from sounds and symbols. This course provides an introduction to natural language processing, linguistic phenomena, and our attempts to analyze them using modern deep learning approaches. We cover a wide range of concepts with a focus on practical applications such as information extraction, machine translation, sentiment analysis, and summarization. The focus of this course prioritizes practical application over theory. Each week, the course is centered on Python notebooks that include exercises and code examples. The asynchronous lectures provide a foundation to build upon in the live sessions.

**Course Prerequisites**
* [MIDS 207 (Machine Learning)](https://www.ischool.berkeley.edu/courses/datasci/207): We assume you know what gradient descent is.  We review simple linear classifiers and softmax at a high level, but make sure you've at least heard of these! You should also be comfortable with linear algebra, which we use for vector representations and when we discuss deep learning.
* Language: All assignments are in Python using Jupyter notebooks, Google Colab, NumPy, TensorFlow, and Keras.
* Time:  There are three to four substantial assignments in this course as well as a term project.  Make sure you give yourself enough time to be successful! In particular, you may be in for a rough semester if you have other significant commitments at work or home, or take both this course and any of 210 (Capstone), 261, or 271.


**Course Goals and Objectives**
By the completion of this course, students will be able to:
* Understand and describe multiple facets of linguistic phenomena related to natural language processing.
* Describe fundamental concepts, techniques, problems, and modern approaches in the domain of natural language processing (NLP).
* Understand the assumptions, strengths, and limitations of NLP and related deep learning techniques, and make appropriate decisions about application of techniques and solutions to NLP problems. 
* Analyze textual data using a number of machine learning and deep learning-based NLP techniques.
* Demonstrate familiarity with and comprehension of existing NLP techniques for solving practical problems.
* Demonstrate an ability to stay current with a constantly evolving field: by developing a familiarity with the neural network architectures that underpin current state of the art, and an ability to seek out and understand new advances published in the field. 
* Demonstrate expertise in using existing libraries and tools related to NLP work, along with an ability to familiarize oneself to new libraries and tools that are key to NLP practitioners as the domain evolves.


**Communication and Resources**
* Course website: [GitHub datasci-w266/2022-fall-main](../../../)
* [Ed Discussion](https://edstem.org/us/join/a9M6fE): We'll use this for collective Q&A, and this will be the fastest way to reach the course staff. Note that you can post anonymously, or make posts visible only to instructors for private questions.
* Email list for course staff (expect a somewhat slower response here): [mids-nlp-instructors@googlegroups.com](mailto:mids-nlp-instructors@googlegroups.com)


**Live Sessions**
* Section 1: Tuesday 2:00 - 3:30pm PST (Peter Grabowski)
* Section 2: Wednesday 4 - 5:30pm PST (Natalie Ahn) 
* Section 3: Tuesday 4 - 5:30pm PST (Daniel Cer)
* Section 4: Wednesday 4 - 5:30pm PST (Mark Butler)
* Section 5: Monday 6:30 - 8pm PST (Jennifer Zhu) 
* Section 6: Wednesday 6:30 - 8pm PST (Mike Tamir/Paul Spiegelhalter)


**Teaching Staff Office Hours**

* **Daniel Cer**: Monday at noon PST
* **Jennifer Zhu**: Thursday at 6:30pm PST
* **Mike Tamir/Paul Spiegelhalter**: Wednesday immediately after the live session
* **Natalie Ahn**: Wednesday at 6pm PST
* **Peter Grabowski**: Tuesday immediately after his live session
* **Mark Butler**: Friday at 5pm PST
* **Gurdit Chahal**: Wednesday at 2:30pm PST
* **Rajiv Nair**: Monday at 5pm PST

Office hours are for the whole class; students from any section are welcome to attend any of the times above.

**Async Instructors**
* James Kunz
* Joachim Rahmfeld
* Mark Butler


## Course Evaluation

### Breakdown

<table>
<tr>
<th>Assignment</th><th>Topic</th><th>Release</th><th>Deadline</th><th>Weight</th>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a0" target="_blank">Assignment&nbsp;0</a></strong>  -->
  Assignment&nbsp;0
  <td><strong>Course Set Up</strong>
  <ul>
    <li>GitHub
    <li>Ed Discussion
    <li>Google Cloud
  </ul></td>
  <td>Aug&nbsp;22</td>
  <td>Aug&nbsp;28</td>
  <td>0%</td>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a1" target="_blank">Assignment&nbsp;1</a></strong>  -->
  Assignment&nbsp;1
  <td><strong>Basic Neural Nets</strong></td>
  <td>Aug&nbsp;27</td>
  <td>Sep&nbsp;4</td>
  <td>5%</td>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a2" target="_blank">Assignment&nbsp;2</a></strong>  -->
  Assignment&nbsp;2
  <td><strong>Text Classification</strong></td>
  <td>Sep&nbsp;10</td>
  <td>Sep&nbsp;25</td>
  <td>15%</td>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a3" target="_blank">Assignment&nbsp;3</a></strong>  -->
  Assignment&nbsp;3
  <td><strong>Question Answering</strong></td>
  <td>Oct&nbsp;1</td>
  <td>Oct&nbsp;16</td>
  <td>15%</td>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a4" target="_blank">Assignment&nbsp;4</a></strong>  -->
  Assignment&nbsp;4
  <td><strong>Multimodal NLP</strong></td>
  <td>Oct&nbsp;22</td>
  <td>Nov&nbsp;6</td>
  <td>10%</td>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a0" target="_blank">Assignment&nbsp;0</a></strong>  -->
  Final Project
  <td><strong><a href="../project" target="_blank">Final Project Guidelines</a></strong></td>
  <td></td>
  <td>Dec&nbsp;3</td>
  <td>55%</td>
</tr>
</table>

Your assignment grade report can be found at [https://w266grades.appspot.com](https://w266grades.appspot.com).



### General Grading Philosophy

A word of warning:  Given that we (effectively) release solutions to some parts of assignments in the form of unit tests, it shouldn't be surprising that most students earn high scores.  Since the variance is so low, assignment scores aren't the primary driver of the final letter grade for most students.  A good assignment score is necessary but not sufficient for a strong grade in the class.  A well-structured, novel project with good analysis is what makes the difference between a high B/B+ and an A-/A.

As mentioned above, this course is a lot of work.  Give it the time it deserves and you'll be rewarded intellectually and on your transcript.


### Late Submission Policy

We recognize that sometimes things happen in life outside the course, especially in MIDS where we all have full-time jobs and family responsibilities to attend to. To help with these situations, we are giving you **5 "late days"** to use throughout the term as you see fit.  Each late day gives you a 24-hour (or any part thereof) extension to any deliverable in the course **except** the final project presentation or report. (UC Berkeley needs grades submitted very shortly after the end of classes.)

Once you run out of late days, each 24-hour period (or any part thereof) results in a **10 percentage-point deduction** on that deliverable's grade.

You can use a **maximum of 2 late days** on any single deliverable.  We will **not be accepting any submissions more than 48 hours past the original due date**, even if you have late days. (We want to be more flexible here, but your fellow students also want their graded assignments back promptly!)

We don't anticipate granting extensions beyond these policies.  Plan your time accordingly!

### More Serious Issues

If you run into a more serious issue that will affect your ability to complete the course, please email the instructors mailing list and cc MIDS Student Services.  A word of warning: In previous sections, we have had students ask for an Incomplete (INC) grade because their lives were otherwise busy.  Mostly we have declined, opting instead for the student to complete the course to the best of their ability and have a grade assigned based on that work.  (MIDS prefers to avoid giving INCs, as they have been abused in the past.)  The sooner you start this process, the more options we (and the department) have to help.  Don't wait until you're suffering from the consequences to tell us what's going on!


### Collaboration Policy/Academic Integrity

All students —undergraduate, graduate, professional full time, part time, law, etc.— must be familiar with and abide by the provisions of the "Student Code of Conduct" including those provisions relating to Academic Misconduct. All forms of academic misconduct, including cheating, fabrication, plagiarism or facilitating academic dishonesty will not be tolerated. The full text of the UC Berkeley Honor Code is available at:  https://teaching.berkeley.edu/berkeley-honor-code and the Student Code of Conduct is available at: https://sa.berkeley.edu/student-code-of-conduct#102.01_Academic_Misconduct

We encourage studying in groups of two to four people. This applies to working on homework, discussing labs and projects, and studying. However, students must always adhere to the UC Berkeley Code of Conduct (http://sa.berkeley.edu/code-of-conduct ) and the UC Berkeley Honor Code (https://teaching.berkeley.edu/berkeley-honor-code ). In particular, all materials that are turned in for credit or evaluation must be written solely by the submitting student or group. Similarly, you may consult books, publications, or online resources to help you study. In the end, you must always credit and acknowledge all consulted sources in your submission (including other persons, books, resources, etc.)


## Final Project
*See the [Final Project Guidelines](../project/)*


## Attendance and Participation

We believe in the importance of the social aspects of learning —between students, and between students and instructors— and we recognize that knowledge-building does not solely occur on an individual level, but is built by social activity involving people and by members engaged in the activity. Participation and communication are key aspects of this course vital to the learning experiences of you and your classmates.

Therefore, we like to remind all students of the following requirements for live class sessions:

* Students are required to join live class sessions from a study environment with video turned on and with a headset for clear audio, without background movement or background noise, and with an internet connection suitable for video streaming.

* You are expected to engage in class discussions, breakout room discussions and exercises, and to be present and attentive for your and other teams’ in-class presentations. 

* Keep your microphone on mute when not talking to avoid background noise. Do your best to minimize distractions in the background video, and ensure that your camera is on while you are engaged in discussions. 

That said, in exceptional circumstances, if you are unable to meet in a space with no background movement, or if your connection is poor, make arrangements with your instructor (beforehand if possible) to explain your situation. Sometimes connections and circumstances make turning off video the best option. If this is a recurring issue in your study environment, you are responsible for finding a different environment that will allow you to fully participate in classes, without distraction to your classmates.

**Failure to adhere to these requirements will result in an initial warning from your instructor(s), followed by a possible reduction in grades or a failing grade in the course.**


## Diversity and Inclusion

Integrating a diverse set of experiences is important for a more comprehensive understanding of data science. We make an effort to read papers and hear from a diverse group of practitioners. Still, limits exist on this diversity in the field of data science. We acknowledge that it is possible that there may be both overt and covert biases in the material due to the lens through which it was created. We would like to nurture a learning environment that supports a diversity of thoughts, perspectives and experiences, and honors your identities (including race, gender, class, sexuality, religion, ability, veteran status, etc.) in the spirit of the UC Berkeley Principles of Community https://diversity.berkeley.edu/principles-community

To help us accomplish this, please contact us or submit anonymous feedback through I School channels if you have any suggestions to improve the quality of the course. If something was said in class (by anyone) or you experience anything that makes you feel uncomfortable, please talk to your instructors about it. If you feel like your performance in the class is being impacted by experiences outside of class, please don’t hesitate to come and talk with us. We want to be a resource for you. Also, anonymous feedback is always an option and may lead us to make a general announcement to the class, if necessary, to address your concerns. As a participant in teamwork and course discussions, you should also strive to honor the diversity of your classmates.

If you prefer to speak with someone outside of the course, the MIDS Academic Director Drew Paulin, the I School Assistant Dean of Academic Programs Catherine Cronquist Browning, and the UC Berkeley Office for Graduate Diversity are excellent resources. Also see the following: https://www.ischool.berkeley.edu/about/community.

## Disability Services and Accommodations

If you need disability-related accommodations in this class, if you have emergency medical information you wish to share with me, or if you need special arrangements in case the building must be evacuated, please inform me as soon as possible.

The I School recognizes disability in the context of diversity, and the Disabled Students’ Program (DSP) equips students with appropriate accommodations and services to remove barriers to educational access. Students seeking accommodations in this class are responsible for completing the DSP application process to obtain an accommodation letter. You may reach the DSP at (510) 642-0518, or visit the website: https://dsp.berkeley.edu
 
## Publishing Your Work

You are highly encouraged to use your program coursework to build an academic/professional portfolio. 

* Blog about your coursework (and other ideas) and share on the I School Medium channel
  * Instructions are here on the intranet for students: https://www.ischool.berkeley.edu/intranet/connect 
  * Instructions here are public for alumni: https://www.ischool.berkeley.edu/alumni/stay-connected
* Publish projects to your I School project portfolio gallery (for more than just the capstone).
* Publish your work on LinkedIn and tag @UC Berkeley School of Information. Do **NOT** publish your homework assignments!
* Publish in academic journals: Contact your professors for assistance. (Note that multiple review iterations are usually required; this can be a time-intensive endeavor.)
  * For help writing professional academic papers students are encouraged to contact Sabrina Soracco, the Director of the Graduate Writing Center, in the Graduate Division -- see https://grad.berkeley.edu/staff/sabrina-soracco/ and https://grad.berkeley.edu/professional-development/graduate-writing-center/ -- the latter has links to resource guides, appointments with consultants, workshops, etc.
* Publish your news (e.g., conference talks, awards, scholarships) to the I School internal newsletter.



## Course Resources

We are not using any particular textbook for this course. We’ll list some relevant readings each week. Here are some general resources:
* [Speech and Language Processing (3rd edition draft)](https://web.stanford.edu/~jurafsky/slp3/) by Daniel Jurafsky and James H. Martin - _free online!_
* [Speech and Language Processing (2nd edition)](http://www.cs.colorado.edu/~martin/slp.html) by Daniel Jurafsky and James H. Martin - _This edition does not cover neural net approaches_
* [NLTK Book - Natural Language Processing with Python](http://www.nltk.org/book/) - accompanies NLTK (Natural Language Tool Kit) and includes useful, practical descriptions (with python code) of basic concepts.
* [Deep Learning](http://www.deeplearningbook.org/) (Goodfellow, Bengio, and Courville)

We’ll be posting materials to the course [GitHub repo](../../../).

*Note:* This syllabus may be subject to change. We'll be sure to announce anything major on Ed Discussion.

### Code References

The course will be taught in Python, and we'll be making heavy use of NumPy, TensorFlow, Keras, and Jupyter (IPython) notebooks. We'll also be using Git for distributing and submitting materials. If you want to brush up on any of these, we recommend:
* **Git tutorials:** [Introduction / Cheat Sheet](https://git-scm.com/docs/gittutorial), or [interactive tutorial](https://try.github.io/)
* **Python / NumPy:** Stanford's CS231n has [an excellent tutorial](http://cs231n.github.io/python-numpy-tutorial/).
* **TensorFlow:** We'll go over the basics of TensorFlow and Keras in [Assignment 1](../../../tree/master/assignment/a1/).  
  [Effective TensorFlow 2](https://github.com/vahidk/EffectiveTensorflow) is a great reference, ranging from the absolute basics through advanced topics like multi-GPU training, `tf.learn`, and debugging.  
  You can also check out the [tutorials](https://www.tensorflow.org/get_started/) on the TensorFlow website, but these can be somewhat confusing if you're not familiar with the underlying models. Also, look at the [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras/sequential_model) as we will be using Keras in this class.
* **Keras:** The [Keras Site](https://keras.io/getting_started/) has a variety of useful guides as well as code examples.


### Miscellaneous Deep Learning and NLP References
Here are a few useful resources and papers that don’t fit under a particular week -- all optional, but interesting!
* (Optional) [Chris Olah’s blog](http://colah.github.io/) and [Distill](https://distill.pub/)
* (Optional) [GloVe: Global Vectors for Word Representation (Pennington, Socher, and Manning, 2014)](http://nlp.stanford.edu/pubs/glove.pdf)
* (Optional) [Jay Alammar’s blog](https://jalammar.github.io/) 
---

## Tentative Schedule and Readings

We'll update the table below with assignments as they become available, as well as additional materials throughout the semester. Keep an eye on GitHub for updates!

*Dates are tentative:* Assignments in particular may change topics and dates.  (Updated slides for each week will be posted during the live session week.)

### Live Session Slides [[available with @berkeley.edu address](https://drive.google.com/drive/folders/1BYQkr1K6V2Ztr8g-zyOYAPkjv7xMutKO?usp=sharing)]

### Deliverables

Note:  we will update this table as we release assignments.  Each assignment
will be released around the last live session of the week and due approximately 1 week later (for simple assignments) or 2 to 3 weeks later (for complex assignments).

<table>
<tr>
<th></th><th>Topic</th><th>Release</th><th>Deadline</th>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a0" target="_blank">Assignment&nbsp;0</a></strong>  -->
  Assignment&nbsp;0
  <td><strong>Course Set-up</strong>
  <ul>
    <li>GitHub
    <li>Ed Discussion
    <li>Google Cloud
  </ul></td>
  <td>Aug&nbsp;22</td>
  <td>Aug&nbsp;28</td>
</tr

<tr> <!-- a1 -->
  <td><strong><a href="../assignment/a1" target="_blank">Assignment&nbsp;1</a></strong>
  <td><strong>Assignment&nbsp;1</strong>
  <ul>
    <li>Neural Networks
  </ul></td>
  <td>Aug&nbsp;27</td>
  <td>Sep&nbsp;4</td>
</tr>

<tr>  <!-- a2 -->
  <td><strong><a href="../assignment/a2" target="_blank">Assignment&nbsp;2</a></strong>
  <td><strong>Assignment 2</strong>
  <ul>
    <li>Text Classification
  </ul></td>
  <td>Sep&nbsp;9</td>
  <td>Sep&nbsp;25</td>
</tr>

<tr> <!-- project proposal -->
  <td><strong><a href="../project/#project-proposal" target="_blank">Project&nbsp;Proposal</a></strong>
  <td>
  <strong><a href="../project" target="_blank">Final Project Guidelines</a></strong>
  </td>
  <td></td>
  <td>Oct&nbsp;1</td>
</tr>


<tr><!--- Project Reports -->
  <td><strong><a href="../project/#final-submission" target="_blank">Project&nbsp;Reports</a></strong>
  </td>
  <td></td>
  <td></td>
  <td><br>Due Dec&nbsp;3<br><strong>(hard deadline)</strong></td>
</tr>

<tr><!--- Project Presentations -->
  <td><strong><a href="../project/#presentations" target="_blank">Project&nbsp;Presentations</a></strong></td>
  <td></td>
  <td></td>
  <td>In-class Dec&nbsp;5-9</td>
</tr>
</table>


### Course Schedule

<table>
<tr>
<th></th>
<th>Async Material to Watch</th>
<th>Topics</th>
<th>Materials</th>
</tr>
<tr><!--- Introductions -->
  <td><strong>Week&nbsp;1</strong><br>(Aug&nbsp;22)</td>
  <td>Introduction
  </td>
  <td><ul>
    <li>Overview of NLP applications
	<li>NLP tasks, model structures and neural architectures
    <li>Ambiguity and grounding in language
    <li>Introduction to word embeddings
  </ul></td>
  <td><ul>
  <li>Read: <a href="https://www.technologyreview.com/s/602094/ais-language-problem/" target="_blank">AI’s Language Problem (Technology Review)</a>
  <li>Read: <a href="http://nautil.us/issue/54/the-unspoken/the-rise-and-fall-of-the-english-sentence" target="_blank">The Rise and Fall of the English Sentence</a>
  <li>Skim: <a href="http://www.nltk.org/book/ch01.html" target="_blank">NLTK book chapter 1 (python and basics)</a>
  <li>Skim: <a href="http://www.nltk.org/book/ch02.html" target="_blank">NLTK book chapter 2 (data resources)</a>
  <li><em>Optional:</em> <a href="http://www.newyorker.com/magazine/2007/04/16/the-interpreter-2" target="_blank">The Interpreter (New Yorker)</a>
  <li><em>Optional:</em> <a href="https://www.uio.no/studier/emner/hf/ikos/EXFAC03-AAS/h05/larestoff/linguistics/Chapter%204.(H05).pdf" target="_blank">Introduction to Linguistic Typology</a>
  <li><em>Optional:</em> <a href="https://jalammar.github.io/illustrated-word2vec/" target="_blank">The Illustrated Word2Vec</a>
      <li><em>Optional / fun:</em> <a href="http://playground.tensorflow.org/" target="_blank">Tensorflow Playground</a>
  </ul>
  <!-- <p>                                        -->
  <!-- <a href="../materials/week1/TensorFlow%20Tutorial.ipynb" target="_blank">[TensorFlow&nbsp;Intro&nbsp;notebook]</a> -->
  </td>
</tr>

<tr><!--- Week 2 -->
  <td><strong>Week&nbsp;2</strong><br>(Aug&nbsp;29)</td>
  <td>
  <br>Text Classification
  </td>
  <td><ul>
    <li>Text classification approaches with neural networks
	<li>Text classification with CNNs
  </ul></td>
  <td><ul>
    <li>Read: <a href="https://web.archive.org/web/20200119215959/http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/" target="_blank">Understanding Convolutional Neural Networks for NLP (via Wayback Machine link)</a>
    <li>Read: <a href="https://arxiv.org/abs/1408.5882" target="_blank">Convolutional Neural Networks for Sentence Classification</a> (Kim, 2014)
    <li><em>Skim:</em><a href="https://jalammar.github.io/illustrated-word2vec/" target="_blank">The Illustrated Word2vec</em>
    <li><em>Optional / fun:</em> <a href="http://playground.tensorflow.org/" target="_blank">Tensorflow Playground</a>
    <li><em>Optional:</em> <a href="https://arxiv.org/pdf/1103.0398v1.pdf" target="_blank">Natural Language Processing (almost) from Scratch</a> (Collobert et al., 2011)

  </ul>
    </td>
</tr>

<tr><!--- Week 3 -->
  <td><strong>Week&nbsp;3</strong><br>(Sep&nbsp;5)</td>
  <td>Language and Context
    </td>
  <td><ul>
  <li>Recurrent Neural Nets (RNNs) and language modeling
  <li>Attention
  <li>Context awareness and embeddings
  </ul></td>
  <td><ul>
  <li>Read: <a href="https://arxiv.org/abs/1802.05365" target="_blank">Deep contextualized word representations</a> (Peters et. al., 2018)
  <li><em>Skim:</em><a href="https://karpathy.github.io/2015/05/21/rnn-effectiveness/" target="_blank">The Unreasonable Effectiveness of Recurrent Neural Networks</a>
  <li><em>Optional:</em><a href="http://distill.pub/2016/augmented-rnns/#attentional-interfaces" target="_blank">Attention and Augmented Recurrent Neural Networks</a> (section on “Attentional Interfaces” has an awesome visualization of an MT example, showing alignments)
    <li><em>Optional:</em> <a href="http://norvig.com/ngrams/ch14.pdf" target="_blank">Natural Language Corpus Data</a>  (Peter Norvig)
  </ul>
</tr>


<tr><!--- Week 4 -->
  <td><strong>Week&nbsp;4</strong><br>(Sep&nbsp;12)</td>
  <td>Pretrained Transformers
  <p><p>
  </td>
  <td><ul>
  <li>Transformer Architecture
  <li>Pretrained Transformers and Language Models
  <li>Pretrained Transformers and Context-Based Embeddings
  </ul></td>
  <td><ul>
    <li>Read: <a href="https://arxiv.org/pdf/1706.03762.pdf" target="_blank">Attention is All You Need</a> (Vaswani et. al., 2017)
 <li><em>Skim:</em> <a href="https://arxiv.org/pdf/1810.04805v1.pdf" target="_blank">BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”</a>, (Devlin et al, 2018)
 <li><em>Skim:</em> <a href="https://jalammar.github.io/illustrated-bert/" target="_blank">The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)”</a>, (Alammar, 2018)
</ul></td>
</tr>

<tr><!--- Week 5 -->
  <td><strong>Week&nbsp;5</strong><br>(Sep&nbsp;19)</td>
  <td>Text Generation Models</td>
  <td><ul>
    <li>Sequence to Sequence Architectures
    <li>Pretrained Encoder-Decoder Transformer Architectures
  </ul></td>
  <td><ul>
  <li>Read: <a href="https://arxiv.org/pdf/1910.10683.pdf" target="_blank">Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer</a> (Raffel et. al. 2019)
  <li><em>Skim:</em> <a href="https://arxiv.org/pdf/2005.14165.pdf" target="_blank">Language Models are Few Shot Learners</a> (Brown et. al. 2020)
  </ul>
  </td>
</tr>

<tr><!--- Extra Material -->
  <td><strong>Interlude (Extra Material)</strong></td>
  <td>Units of Meaning: Words, Morphology, Sentences</td>
  <td><ul>
  <li>Edit distance for strings
  <li>Tokenization
  <li>Sentence splitting
  </ul></td>
  <td><ul>
  <li>Read: <a href="https://aclanthology.org/N09-2061.pdf" target="_blank">Sentence Boundary Detection and the Problem with the U.S.</a>
  <li><em>Skim:</em> <a href="http://www.nltk.org/book/ch03.html" target="_blank">NLTK book chapter 3</a> (processing raw text)
  <li><em>Skim:</em> <a href="http://norvig.com/ngrams/ch14.pdf" target="_blank">Natural Language Corpus Data</a> (Peter Norvig) <em>(if you didn't read in Week 3)</em>
  <p>
  </ul></td>
</tr>

<tr><!--- Week 6 -->
  <td><strong>Week&nbsp;6</strong><br>(Sep&nbsp;26)</td>
  <td>Machine Translation</td>
  <td><ul>
  <li>Challenges of Language
  <li>Encoder Decoder architecutres for Neural Machine Translation
  <li>Evaluation
  <li>Subword Models
  </ul></td>
  <td><ul>
  <li>Read: <a href="https://arxiv.org/abs/1609.08144" target="_blank">Google’s Neural Machine Translation System</a>
  <li><em>Skim:</em> <a href="http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf" target="_blank">Sequence to Sequence Learning with Neural Networks</a>
  <li><em>Skim:</em> <a href="https://arxiv.org/pdf/1409.0473.pdf" target="_blank">Neural Machine Translation by Jointly Learning to Align and Translate</a>
  <li><em>Skim:</em> <a href="https://arxiv.org/abs/2010.11125" target="_blank">Beyond English-Centric Multilingual Machine Translation</a>
  </ul>
  <p>
  </td>
</tr>

<tr><!--- Week 7  -->
  <td><strong>Week&nbsp;7</strong><br>(Oct&nbsp;3)</td>
  <td>Question Answering
  <br> and Summarization</td>
  <td><ul>
  <li>Question Answering Architectures
  <li>Extractive and Abstractive Summarization
  <li>Evaluation
  </ul></td>
  <td><ul>
  <li>Read: <a href="https://arxiv.org/pdf/1704.04368.pdf" target="_blank">Get To The Point: Summarization with Pointer-Generator Networks</a> (See et al. 2017)
  <li><em>Skim:</em> <a href="https://aclanthology.org/P18-2124.pdf" target="_blank">Know What You Don’t Know: Unanswerable Questions for SQuAD</a> (Rajpurkar et al. 2018)
  <li><em>Skim:</em> <a href="https://aclanthology.org/N19-1246.pdf" target="_blank">DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs</a> (Dua et al. 2019)
  <li><em>Skim:</em> <a href="https://aclanthology.org/2021.naacl-main.393.pdf" target="_blank">Hurdles to Progress in Long-form Question Answering</a> (Krishna et al. 2021)
    <li><em>Skim:</em> <a href="https://www.cs.cmu.edu/~afm/Home_files/Das_Martins_survey_summarization.pdf" target="_blank">A Survey on Automatic Text Summarization</a> (Das and Martins, 2007)
  </ul></td>
  </tr>
  
  <tr><!--- week 8  -->
  <td><strong>Week&nbsp;8</strong><br>(Oct&nbsp;10)</td>
  <td>Linguistic Representation</td>
  <td><ul>
  <li>Elements of Language
  <li>Grammars
  <li>Dependency Parsing
  <li>Phrase based Parsing
  <li>Evaluation
  </ul></td>
  <td><ul>
    <li>Read: <a href="https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html" target="_blank">SyntaxNet (Parsey McParseface)</a>
  <li>Read: <a href="https://aclanthology.org/D14-1082.pdf" target="_blank">A Fast and Accurate Dependency Parser using Neural Networks</a> (Chen & Manning 2014)
  <li>Read: <a href="https://aclanthology.org/P17-1076.pdf" target="_blank">A Minimal Span-Based Neural Constituency Parser</a> (Stern et al. 2017)
    <li><em>Skim:</em> <a href="http://www.nltk.org/book/ch08.html" target="_blank">NLTK book chapter 8 (analyzing sentence structure)</a>
  <li><em>Optional:</em> <a href="http://www.nltk.org/book/ch05.html" target="_blank">NLTK book chapter 5: Categorizing and Tagging Words</a>
  <li><em>Optional:</em> <a href="https://arxiv.org/pdf/1104.2086.pdf" target="_blank">A Universal Part-of-Speech Tagset</a>
  <li><em>Optional:</em> <a href="http://nlp.stanford.edu/pubs/CICLing2011-manning-tagging.pdf" target="_blank">Part-of-Speech Tagging from 97% to 100%: Is It Time for Some Linguistics?</a>
  <li>Optional: <a href="http://ilpubs.stanford.edu:8091/~klein/unlexicalized-parsing.pdf" target="_blank">Accurate Unlexicalized Parsing</a> (Klein & Manning 2003)
  <li><em>Optional / reference:</em> <a href="http://www.surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html" target="_blank">Penn Treebank Constituent Tags</a>
  <li>Play: <a href="https://corenlp.run" target="_blank">Stanford parser</a> (online demo)
  </ul>
  <p>
  </td>
</tr>

<tr><!--- Week 09  -->
  <td><strong>Week&nbsp;9</strong><br>(Oct&nbsp;17)</td>
  <td>Entities and Linking</td>
  <td><ul>
  <li>Named Entity Recognition
  <li>Coreference Resolution
  <li>Entity Linking
  <li>Relation Extraction
  </ul></td>
  <td><ul>
  <li>Read: <a href="http://www.nltk.org/book/ch07.html" target="_blank">NLTK Book Chapter 7 (Extracting Information from Text)</a>
    <li>Read: <a href="https://arxiv.org/pdf/1907.10529.pdf" target="_blank">SpanBERT: Improving Pre-training by Representing and Predicting Spans</a> (Joshi et al. 2019)
  <li><em>Optional:</em> <a href="http://www.aclweb.org/anthology/D09-1120" target="_blank">Simple Coreference Resolution with Rich Syntactic and Semantic Features</a> (Haghighi and Klein 2009, rule-based coreference)
  <li><em>Optional:</em> <a href="http://www.aclweb.org/anthology/P16-1061" target="_blank">Improving Coreference Resolution by Learning Entity-Level Distributed Representations</a> (Clark and Manning 2016, neural coreference)
  </ul>
  <p>
  </td>
</tr>


<tr><!--- Week 10  -->
  <td><strong>Week&nbsp;10</strong><br>(Oct&nbsp;24)</td>
  <td>Embedding-based Retrieval</td>
  <td><ul>
  <li>Single- vs. multi-document retrieval
  <li>Two tower models
  </ul></td>
  <td><ul>
  <li>Read: <a href="http://static.googleusercontent.com/media/research.google.com/en//archive/googlecluster-ieee.pdf" target="_blank">Web Search for a Planet</a> (Google)
  <li>Read: <a href="http://infolab.stanford.edu/~backrub/google.html" target="_blank">The Anatomy of a Large-Scale Hypertextual Web Search Engine</a>
  <li>Skim: <a href="https://arxiv.org/pdf/1907.04307.pdf" target="_blank"> Multilingual Universal Sentence Encoder for Semantic Retrieval</a>
  <li><em>Skim:</em> <a href="http://nlp.stanford.edu/IR-book/pdf/irbookprint.pdf" target="_blank">"An Introduction to Information Retrieval", sections 6.2 and 6.3</a>
  <li><em>Optional:</em> <a href="http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf" target="_blank">PageRank</a> (Page, et al. 1999) 
  </ul>
  <p>
  </td>
</tr>


 <!-- <tr>
  <td><strong>Break</strong><br>(March&nbsp;22)</td>
  <td>No Async</td>
    <td>No class</td>
  <td>No Readings</td>
</tr> -->

 <tr><!---   week 11 -->
  <td><strong>Week&nbsp;11</strong><br>(Oct&nbsp;31)</td>
  <td>Multimodality in NLP</td>
  <td><ul>
  <li>Multimodal Applications
  <li>Image Captioning
  <li>Visual Question Answering
  </ul></td>
  <td><ul>
	<li>Read: <a href="https://arxiv.org/pdf/1411.4555.pdf" target="_blank">Show and Tell: A Neural Image Caption Generator</a> (Vinyals et. al. 2014)
	<li>Read: <a href="https://arxiv.org/pdf/2103.00020.pdf" target="_blank">Learning Transferable Visual Models From Natural Language Supervision</a> (Radford et. al 2021)
  </ul>
  <p>
  </td>
</tr>

<tr>
  <td><strong>Break</strong><br>(Nov&nbsp;7)</td>
  <td>No Async</td>
    <td>No class</td>
  <td>No Readings</td>
</tr>

<tr><!--- Week 12  -->
  <td><strong>Week&nbsp;12</strong><br>(Nov&nbsp;14)</td>
  <td>ML Fairness and Privacy</td>
  <td><ul>
  <li>Fairness
  <li>Privacy
  </ul>
  </td>
  <td><ul>
   <li>Read: <a href="http://blog.conceptnet.io/posts/2017/how-to-make-a-racist-ai-without-really-trying/" target="_blank">How to make a racist AI without really trying</a>
   <li>Read: <a href="https://arxiv.org/pdf/1707.00075.pdf" target="_blank">Data Decisions and Theoretical Implications when Adversarially Learning Fair Representations</a> (Beutel et. al. 2017)
   <li>Read: <a href="https://arxiv.org/pdf/1607.06520.pdf" target="_blank">Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings</a> (Bolukbasi et. al. 2016)
   <li>Read: <a href="https://aclanthology.org/N19-1061/" target="_blank">Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them</a> (Gonen & Goldberg 2019)
  </ul> 
  </td>
</tr>

<tr>
  <td><strong>Thanksgiving Break</strong><br>(Nov&nbsp;21)</td>
  <td>No Async</td>
    <td>No class</td>
  <td>No Readings</td>
</tr>

<tr><!--- Week 13  -->
  <td><strong>Week&nbsp;13</strong><br>(Nov&nbsp;28)</td>
  <td>NLP in the Real World</td>
  <td><ul>
  <li>Productization at Scale
  <li>Infrastructure
  <li>Metrics
  <li>Failure Modes
  <li>NLP Review
  </ul></td>
  <td><ul>
	<li>TBD
  </ul>
  <p>
  </td>
</tr>


 <tr><!--- In class presentations week 14 -->
  <td><strong>Week&nbsp;14</strong><br>(Dec&nbsp;5)</td>
    <td></td>
  <td>In-class project presentations</td>
  <td></td>
</tr>

</table>

Thanks for a great semester!
