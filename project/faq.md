# Frequently Asked Questions

## Use whatever tooling you want

A few students were asking in office hours if they could use software tools they didn't write to make their jobs easier.  The short answer is "Absolutely!".  The long answer is that you have to understand what tool you're using, why you're using it and there should be a coherent reason for its application to your problem.  And you absolutely must cite it in your report.  We need to know what work you leveraged and what you contributed!
 
## Target instructors as your audience

The page limit is small. Use the space wisely.  Your target audience is your instructors (as it turns out, it actually is!).  Don’t waste space explaining things covered in class.  Assume we have a reasonable depth of understanding of common language and neural models.  Spend your time on your contributions and how they deviate from published work.

## Keep your report focused
Focus your report on 1-2 models (plus baseline).  Understand them deeply and demonstrate that you do.  Instead of telling us which software package you used, tell us about the details of the algorithm and what inspired you to apply it to your task.  Don’t make things up/copy long lists of algorithms without motivating why each is useful (ideally with references and empirical results on your dataset - if you didn't do the work yet, best just to leave it out).  Graders should not want to shout "Bingo!" after reading a paragraph of your report :).  Instead, you want them to feel as though you understand your data set, where the baseline is getting things wrong, and that you are proposing coherent solutions to those problems.

## Literature review is required
Your work should fit with other published work.  What inspired your project's direction?  Cite that work!  If you claim approach X has been found not to work, you need to substantiate that claim.  This means you need references.  Knowing that X doesn't work and avoiding it with a citation isn't cheating.  It's how you skip over the solved problems and work on something interesting.  References must be:

* Related to your project.
From published, peer-reviewed, sources.
* Not project reports from previous offering of this course or Stanford’s CS224N/CS224D.
* Not GitHub links or blog posts.
* Seriously, not blog posts.
* (Of course, for academic honesty, when you use them, you should still cite project reports, GitHub, and blog posts.  But they do not stand in for proper research when motivating your approach/claims.)

## Analysis is critical
Explain your errors in terms of your model.  Use the work you put in understanding your model to good use!  Projects with one model and really good error analysis are (much) better than projects with a “throw every algorithm at the wall” with little thought about what they’re doing.

## Data selection
Data selection as with all ML projects is a critical component. You generally are permited to use any data sets to which you have access for your project which are appropriately sampled, of sufficient volume, and otherwise leveraged with good methodology to acomplish your project goals. Howevever, please keep in mind that instructors will potentially need to be able to review any data that you use for your project without signing an NDA, which rules out the use of private propriatary data for your project. 

## Concrete example
A couple of (not real) sentences inspired from the above hints.  Imagine your project is on some classification task:

* Example (bad): “We stored our data in /foo/bar.csv.  Next we processed the data with scikit_learn.TFIDFVectorizer and perplexity is 38.02.”
* Example (good): “Because Hinton [1] and Bengio [2] have found a bag of vectors model achieves good performance on our task, we started with that as a baseline.  We noticed, however, that many of our losses seemed to be sentences with many stop words.  We hypothesize that these words overwhelmed the average embedding.  For example, ....  To combat this, we decided to weight the terms by TF-IDF rather than simply TF.  Our hypothesis is that this weighting will improve performance on these losses because it down-weights stopwords and emphasizes semantically-important terms.  This achieves a classification accuracy of 89%, a 2%age point increase over the Hinton model.  As expected, all but one of the previous examples are now correctly classified.  The remaining incorrect example is likely because [The Who] is the name of a band but its embedding is the mean of two stopwords.  (... discuss not lowercasing all the text before training, perform NER first, do the concept trick from the Word2Vec paper, etc... )” 
 
The "bad" example:

* We don't care where you store your data, or even in what format.  We care that you have looked at your data and that it makes sense for your problem.
* Does not inspire confidence that you know what you're doing, just that you're hitting your problem with a tool (TFIDFVectorizer) you picked up seemingly at random.  You need to motivate your choice.
* Perplexity isn't the right/common metric for this task.  Demonstrates the student didn't even do a cursory look through papers on their topic or they would have picked up on what people are using in the field.  If there is some fundamental reason you believe your metric is more appropriate, you should motivate that (and maybe drop by OH to discuss).
* Final model performance matters a lot less than us believing that you understand what you're doing and can apply that understanding to real world problems.  Being a data scientist without actually looking at your data is a strange proposition.  (Hint: you need to look at your data!  Bonus points for looking at the examples your model gets wrong and proposing ideas of why that might be.)
 
The "good" example:

* Support for a claim and an approach, citing peer reviewed literature
* Demonstration that you're close to your data (examining losses)
* Inspiration derived from peer reviewed literature combined with observations from the data
* Concrete plan, plausible from all of the above.  (Demonstrates a depth of understanding about BoV models, TF & IDF, and why they might improve the embedding averaging.)
* Empirical results.
 
Happy projecting!
