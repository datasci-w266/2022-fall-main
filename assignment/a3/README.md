# Assignment 3: Multiclass Text Classification, Question Answering & Summarization

This assignment consists of the following:
* [Multiclass Classification](Multiclass_text_classification.ipynb), more fine-tuning of a BERT model with a multiclass classification dataset. You'll modify the output layer and change some hyperparameters to improve the predictions.
* [Summarization_test](Summarization_test.ipynb), in which you'll experiment with some hyperparamters to affect the output of three separate systems.
* [QuestionAnswering_test](QuestionAnswering_test.ipynb), in which you'll explore the question answering capabilites of a language model based system.

## Submission Instructions

In order to run this notebook you will need to use Colab.  Click on the Open in Colab button.  The notebook will use a GPU by default.  This free colab is a shared resource so please terminate your session when you are done working.  When you are at a stopping point please download the Colab (see File -> Download -> Download .ipynb) as an ipynb file onto your local machine.  You can then use

```
gcloud compute scp LOCAL_FILE_PATH VM_NAME:~/w266/assignment/a3

```

to copy your downloaded notebook to the a3 directory in your instance git repo.  Please make sure that your notebooks keep their names.  From there you can run the submit.sh script as usual.  Remember to also copy the answers from your notebook into the answers sheet as required.  And also make sure thta you do not clear the output cells in your notebook so we can see the results of your work.

As with Assignment 2, please submit by running the submit script, only with `-a 3` (since this is assignment 3).
```
./assignment/submit.sh -u your-github-username -a 3
```

It is your responsibility to check that your work has made it to your GitHub repository in the `a3-submit` branch.  As always, a small number of points will be added for submitting correctly.  We will give each person who correctly submits their assignment two bonus points on this homework assignment.
