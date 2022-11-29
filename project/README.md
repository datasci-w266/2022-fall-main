# Final Project Guidelines

Incredibly useful [FAQ](faq.md).

## Introduction

In addition to programming assignments, students will complete a final project that represents a significant implementation and/or application of NLP techniques. Here’s what to expect:
- You can work on the project in a group of up to 3 students. Solo projects are also fine, but we strongly encourage you to collaborate.  While we expect high _quality_ of work from all groups, we expect a higher _quantity_ of work from teams with more members.
- The project can be on anything within the scope of the class, although it need not be something covered explicitly in lecture.
- At the end, you’ll turn in a writeup in the style of a research paper, and give a short presentation to the class. You’ll also submit your code.

## Grading
The project is expected to be significantly more work than each of the assignments, as you’ll need to do planning and research as well as implement much of the code framework to process data, run experiments, generate plots, etc. How to manage all of this? Start early! (and, ask lots of questions!)

We’ll set several milestones to check in along the way:
- [2%] **Project Proposal**
- [0%] **Milestone (optional)**
- [98%] **Write-Up and Final Presentation**


### Our Expectations of You

As a student in a graduate level course, you are responsible for seeking out help when your project is stuck.  There is significant support available if you seek it out.  Do not wait for us to provide feedback on deliverables to take action.  If you're looking for a formal way to seek this help, skip down to the Milestone section.

### Rubric Dimensions

Each of the following dimensions will be considered while grading.  A project significantly lacking in any dimension will receive a considerably lower grade.  Each dimension is illustrated by several bullet points.  Given the diversity of projects, these bullet points may not be appropriate.  Most projects will need more in some areas and less in others, so use your discretion.  They are there mostly to illustrate the various failure modes we've seen in previous offerings of this class in an attempt to steer you away from them.

Overall themes (10%):
- A clear statement of the problem you are trying to solve.
- Novelty of your approach to the problem.
- Who else has worked on this problem?  What did they do?  What are you doing differently?
- Is it clear you read and understood the papers you cited?  Are they the right ones?

Crisp objective (20%):
- "How will I know when my project is successful?", usually in the form of an evaluation metric.
- Tied back to overall problem statement - why is this the right objective?
- Statement of a clear baseline (e.g. for classification, predict most common class for everything).
- Is this the objective others working on this or similar problems use?  If not, why?

Methodology and analysis (50%):
- Are you using appropriate techniques for the problem you're trying to solve?
- What did you learn from the first approaches you made? How did you take what you learned and use that to improve subsequent iterations?
- What weird patterns in the data have you found?  What about how the model interacts with your data?  (Did you find any interesting loss patterns?)
- Do the patterns you observe align well with patterns other researchers have found in the papers you read?  What did they do about them?

Technical communication (20%):
- Primarily:
  - Succinct, interesting presentation explaining the above.
  - Is your paper well organized?
- Table stakes:
  - Did you run spell check before submitting?
  - Did you proof read it?

Volume of work (built into the other components):
- Is this someone else's code (downloaded from github) simply run on already cleaned up data (downloaded from Kaggle)?
- Did you run assignment code on a new dataset and report just the analysis we built in the notebooks?
- Especially for teams of 3, is it clear each person did a solo-project amount of work?

We'll score each dimension by:
- Missing: 0%
- Weak: 40%
- Satisfactory: 70%
- Strong: 80%
- Near-publishable: 100%

We anticipate most students receiving a Satisfactory grade on most components.


## Project Scope and Ideas
The project is very open-ended, but we do require it to be an NLP project. This means that, at its core, your project should be about processing text, speech, or other form of language. It need not be completely novel in the way that academic research is, but should attempt to do something non-trivial or non-obvious with the data and/or algorithm. For example, you could:
- Apply existing (well-known or otherwise) NLP algorithm(s) to a new dataset
- Develop a new NLP algorithm and apply it to a well-known dataset
- Implement an algorithm from a recent paper and apply it to a new domain or dataset
- Use NLP algorithms in a descriptive way to find trends or patterns of practical or linguistic interest

As for scope: an ambitious project for a group of 2-3 would be similar in scope and depth of experiments to a conference paper.

For project ideas, take a look at the final projects from [previous](example-comment-quality.pdf) [semesters](example-grammar.pdf), Stanford [cs224n](https://web.stanford.edu/class/cs224n/index.html) ([2000-2017](http://nlp.stanford.edu/courses/cs224n/)), or for deep-learning projects, [cs224d](http://cs224d.stanford.edu/) ([2015](http://cs224d.stanford.edu/reports_2015.html), [2016](http://cs224d.stanford.edu/reports_2016.html), [2017](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/reports.html),  [2018](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports.html),  [2019](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/reports.html),  [2020](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1204/reports.html),  [2021](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/reports.html)). A few examples, as a place to start:
- Abstractive summarization of news articles
- Restaurant menu extraction from user reviews
- Question-answering with neural attention or memory models
- Image captioning (language generation)
- Analysis of gender roles or power dynamics in movie dialogues
- Exploration of techniques for interpreting “black box” / neural models for language

Additionally, we've put some of the top projects from previous semesters in [a drive folder](https://drive.google.com/drive/folders/1RImrGxaCeGMqoKee0YeYy4etMyVKK1C2?usp=sharing).  The folder and its contents are available for viewing to anyone with a berkeley.edu email address.

Also see below for NLP conferences - [ACL](https://www.aclweb.org/anthology/events/acl-2020/) and [EMNLP](https://www.aclweb.org/anthology/events/emnlp-2020/) are the top two, and you can find plenty of interesting ideas from the recent proceedings!


## Project Proposal

This is the most important deliverable. Take time to get it right! A concrete idea at this early stage will help you build a stronger project and help you in the course overall.

Each group will submit a proposal.  We’ll read each one and give you detailed feedback. The proposal should be concise, 200-300 words. Quality is valued here far more than quantity!

Be sure to address:
- What do you plan to do?
- Why is it important, and why is it challenging?
- What dataset(s) will you use?
- What algorithms might you use? Are good implementations available, or will you need to write your own? (Don’t worry if you can’t answer this well at this stage of the course.)
- References to _at least_ four papers related to your proposal

You must include four references to relevant papers for the technique and/or dataset you’ll be using. Projects should be well-situated with respect to existing work, and so we do require that references be research papers or technical publications of similar scope. While you may also want to cite reference works, textbooks, or code documentation, these don’t count toward the total. Some resources that may be helpful:
- (start here) [The Association of Computational Linguistics (ACL) Anthology](http://aclanthology.org), which indexes papers from most of the top NLP conferences.
- The [ACM Digital Library](http://dl.acm.org/) is also a great resource, indexing across a number of CS conferences. In particular, [SigKDD](http://www.kdd.org/) (Knowledge Discovery and Data Mining) and [WSDM](http://www.wsdm-conference.org/) (Web Search and Data Mining) might be useful.
- [NIPS](https://papers.nips.cc/) and [ICML](http://proceedings.mlr.press/v97/) are the top machine learning conferences; these are good places to look if you want to use neural networks.
- [Google Scholar](https://scholar.google.com/) and the [arXiv](https://arxiv.org/) are great to find specific papers.

This year’s NLP conferences might be good for inspiration as well, or if you just want a sense of what people in the field are working on: [NAACL](https://aclanthology.org/events/naacl-2021/), [ACL](https://aclanthology.org/events/acl-2021/), [EMNLP](https://aclanthology.org/events/emnlp-2021/).

Between Week 2 and Week 4, the instructors will be holding special discussion sections (during OH) to talk about how to search the literature and read NLP papers. Each session will also include a guided discussion of a specific paper. We'll release a schedule and a list of papers each week in the semester.

Please write your proposal in a Google Doc (shared with comment access to anyone with the link) and submit a link to you proposal via [this form](https://forms.gle/gtsYCbxcGyuMLaEf7).  We'll provide feedback as in-line comments, which can be more convenient than an email thread.
_Please no Microsoft Word documents!_

## Milestone (optional)

__If you want more formal feedback on an intermediate stage of your project, feel free to send us an milestone/interim copy of your report a week ahead of our office hour.  We are happy to take a look and prepare some feedback for you either over email or in the office hour.__

You’ll submit a partial report (3-5 pages) and implementation of your project. This should include:
- Evidence that you’ve been able to obtain, load, and play around a bit with your data.  (For example,  some simple exploratory data analysis.)
- Results from a baseline model. This can be very simple, such as random predictor, most-common-class, or a bag-of-words model.

Your report should be the working/rough draft of your final project report (see below), although it’s expected that you won’t have fleshed-out results or conclusion sections. It’s also okay if your report changes substantially between here and the final, especially if you have exciting results in the interim!  

For the milestone, your writeup should have sections similar to the following, in the vein of a proper research paper:
- **Abstract**
- **Introduction** (motivation for your work)
- **Background** (literature review, or related work)
- **Methods** (include a description of any proposed work here, even if you haven’t done it yet)
- **Results and discussion** (for your baseline model, though feel free to include material for anything else you’ve done)
- **Next Steps** section for work you plan to do before submitting the final version (you’ll remove this section and replace it with your conclusions, final results and analysis in your final report)

The easiest way to write your report is LaTeX; the standard ACL template is available [here](http://acl2020.org/downloads/acl2020-templates.zip) (or, on Overleaf [here](https://www.overleaf.com/latex/templates/acl-2020-proceedings-template/zsrkcwjptpcd)). However, you’re welcome to typeset in Microsoft Word, Google Docs, or the editor of your choice as long as you can export to PDF.

You should also share your code with us via GitHub.  Just include a link to your GitHub.

Please send your write-up in PDF format to mids-nlp-instructors@googlegroups.com.

## Presentations 

Expect that your group will give a short (~5 min) presentation summarizing your project during live session in the last week. We’ll announce a schedule and further details of the presentation format closer to the end of the term.

## Final Submission

This will be a final report in the style of a research paper. Aim for 4-6 pages in length, or somewhere between an ACL [short paper](https://acl2020.org/calls/papers/#short-papers) and a [long paper](https://acl2020.org/calls/papers/#long-papers), with sections similar to the following:
- **Abstract**
- **Introduction** (motivation for your work)
- **Background** (literature review, or related work)
- **Methods** (design and implementation)
- **Results and discussion** (include plots & figures, and detailed analysis in comparison to baseline and the literature, if applicable)
- **Conclusion**

**Privacy:** If you don't want us to release your report publicly, please indicate that in the form below.

Please submit your PDF (and your project's code) to your course GitHub if working alone or to a team repo if in a group and then complete [this form](https://forms.gle/dqMnnttYiL22wxEe7).

We will be providing feedback to teams based on the rubric above.  This will take us some time (potentially up to a month after the deadline) and likely term grades will be released ahead of that feedback.

