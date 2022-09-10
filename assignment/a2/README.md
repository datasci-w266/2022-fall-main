# Assignment 2: Text Classification With Various Neural Networks

This assignment consists of one notebook:
* [Text_classification.ipynb](Text_classification.ipynb), Neural Network Text Classification in Keras and HuggingFace
* [answers](answers) file where you'll put all your answers

You may want to review the notebook for [lesson 3](../../materials/lesson_notebooks/lesson_3_adding_RNNs_and_attention_to_classification_notebook.ipynb).

## Submission Instructions

In order to run this notebook you will need to use Colab.  Click on the Open in Colab button.  The notebook will use a GPU by default.  This free colab is a shared resource so please terminate your session when you are done working.  When you are at a stopping point please download the Colab (see File -> Download -> Download .ipynb) as an ipynb file onto your local machine.  You can then use 

```
gcloud compute scp LOCAL_FILE_PATH VM_NAME:~/w266/assignment/a2

```

to copy your downloaded notebook to the a2 directory in your instance git repo.  Please make sure that your notebook remains named Text_classification.ipynb.  From there you can run the submit.sh script as usual.  Remember to also copy the answers from your notebook into the answers sheet as required.  And also make sure thta you do not clear the output cells in your notebook so we can see the results of your work.


If you have difficulty uploading the file, please consult [this page](https://cloud.google.com/compute/docs/instances/transfer-files#transfergcloud) which has more explanation and alternatives for transfer.


As with Assignment 1, please submit by running the submit script, only with `-a 2` (since this is assignment 2).
```
./assignment/submit.sh -u your-github-username -a 2
```

It is your responsibility to check that your work has made it to your GitHub repository in the `a2-submit` branch.  As always, a small number of points will be given in each assignment for submitting in the right place.  We will give each person who correctly submits their assignment two bonus points on this homework assignment.
