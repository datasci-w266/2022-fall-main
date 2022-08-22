# Assignment 0:  Hello W266!

This assignment is a quick walk-through to help you get set up logistically for the course.  It isn't a real assignment and doesn't count towards your grade (but you can't do the other assignments without it!).

**Reminder:** You may only use 2 late days for any one deliverable in this course.  See the [syllabus](../../syllabus/) for details.

If you haven't yet, please:

- Sign up for [Ed Discussion](https://edstem.org/us/join/a9M6fE)

Now we'll get you all set up with the software packages and the course GitHub.

1. [Setup](https://calmail.berkeley.edu/manage/account/create_account) a @berkeley.edu account setup if you don't already have one (@ischool.berkeley.edu is insufficient!)

2. **Set up your computing environment:** We recommend using a Google Cloud Compute instance. We have $25 of credits available per student, and it should only take a few minutes to set up by following [our Cloud guide](cloud/).  
If you prefer to work on your own laptop/desktop/server (including AWS), we strongly recommend looking through the cloud setup script and matching versions as closely as possible.
*(Note that due to the variety of systems out there, we can only provide official support for Google Cloud instances.)*

3. **Clone the course repo** (if you didn't already in the Cloud guide) with:  
`git clone https://github.com/datasci-w266/2022-fall-main.git ~/w266`  
You may also want to do this on your laptop to have a local copy.  

4. **Answer the questions in the `answers`** file in the `assignment/a0`directory.  (If you wish, you can run the presubmit script, answers\_test.py, yourself.  The submit script below will also run these before it pushes.  Unlike in future assignments, these presubmits check your answers for you.)

5. **Open and run `a0.ipynb`**. This notebook will check that your Python packages are up-to-date, test TensorFlow, and give a taste of some of the NLP datasets we'll be working with. You don't need to write any code here - just run the cells and save.

6. **Create your personal submission repo** at [this link](https://classroom.github.com/a/OJE34ZnB). We'll use this for submitting assignments; it's private to you and the instructors.

7. **Run the submit script**: `./assignment/submit.sh -u your-github-username -a 0`, which will push to your personal repo. It will try to verify the submission, but you can should also visit the repo on GitHub and confirm that your changes show up.  (For all assignments in this course, it's your responsibility to make sure your submission has made it to GitHub!)  **Note:** There is no need to send pull requests or any of the other usual git machinery.  All you need to do is run the submit script and check that your code appeared in a branch named a0-submit in your "classroom" repository you setup in the previous step.  If you can't find it, **this is a problem**.  If you can't figure it out, ask (preferably publicly) on Ed Discussion and someone will help you out.  There will be a small number of points for each assignment for submitting your homework in the right place.

**When you run the submit.sh script for the first time**, it will ask you if you want to use https or ssh.  If you choose https then you will need to create a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in your github account and use it in lieu of your password. 

If you choose ssh then you need to follow the directions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to generate an ssh key on your GCP instance and then [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to add the public key to your ssh account.

## Next...

Continue on to [Assignment 1](../a1/) once it's released.  (Unlike Assignment 0, Assignment 1 isn't just a setup exercise.  Don't wait too long to get started!)
