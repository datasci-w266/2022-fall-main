# Walkthrough Notebooks: BERT as a black box

The purpose of this notebook is to show the use of BERT through some abstract APIs, in this case [HuggingFace Transformer Library](https://huggingface.co/transformers/), without getting in to what exactly is happening inside the model.  The goal is to be able to begin experimenting with that API and some models.

This notebook works better with a GPU.  You can access the notebooks using Colab.  To use Colab, click the open with colab button toward the top of the notebook.  The notebook is designed to use a GPU by default.  If that weren't the case you would need to enable a GPU in your colab notebookby using the Edit menu go to Notebook Settings and selecting GPU as the hardware accelerator.

Note: GPUs are a shared resource.  The assumption is you will only use that shared resource when necessary.  When you are done using the GPU, terminate the session.  Do not use the GPU to run models that don't require a GPU e.g. a simple single dense layer.  Also note that you cannot run these notebooks for more than 12 hours at a time. If you hit the 12 hour mark your session will be terminated regardless of what you are doing at the time.  Therefore, be sure to close your sessions if you are not actively running some cells in the notebook.


