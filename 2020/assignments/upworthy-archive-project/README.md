# Sampling and Analyzing the Upworthy Archive Exploratory Dataset

This folder includes example code for working with the Upworthy Archive dataset. It covers a sample case where researchers want to study the effect of including the name of a notable person in a headline. 

The ideas behind these files are fully explained in the slide deck on [Asking Questions of the Upworthy Archive](https://github.com/natematias/design-governance-experiments/blob/master/lectures/Lecture%2015%20-%20Asking%20Questions%20of%20the%20Upworthy%20Archive.pdf).

Files include:

* [selecting_upworthy_archive_packages.py.ipynb](selecting_upworthy_archive_packages.py.ipynb): a worked example of data-mining the archive for valid tests. The script also creates upper and lower bounds of a possible effect across many tests
* [visualizing-max-min-effect-packages.R.ipynb](visualizing-max-min-effect-packages.R.ipynb): example code for estimating and visualizing all of the tests independently from each other
* [upworthy-methods.py](upworthy-methods.py): utility methods for datamining the upworthy archive.
