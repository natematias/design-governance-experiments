# Meta-Analysis Assignment
Cornell University Department of Communication

J. Nathan Matias([@natematias](https://twitter.com/natematias))


## Deadline
This assignment is due by 9pm on Tuesday, April 21 and will be submitted/graded by teams.

# Assignment
For this team assignment, conduct and report an analysis of the effect of **using a number** in headlines, using the code and data provided in the following workshops:

* The workshop on [asking questions with the Upworthy Arvchive](https://github.com/natematias/design-governance-experiments/blob/master/lectures/Lecture%2015%20-%20Asking%20Questions%20of%20the%20Upworthy%20Archive.pdf)
  * [Code here](https://github.com/natematias/design-governance-experiments/tree/master/assignments/upworthy-archive-project)
* The workshop on meta-analysis:
  * [Slides here](https://github.com/natematias/design-governance-experiments/blob/master/lectures/Lecture%2017%20-%20Using%20Fixed%20Effects%20Models%20for%20Meta%20Analysis.pdf)
  * [Code here](https://github.com/natematias/design-governance-experiments/blob/master/lecture-code/lecture-17-meta-analysis.R.ipynb)

You will:
* adjust the code in `selecting_upworthy_archive_packages.ipynb` to use `has_number` instead of `has_notable_person`. 
* output two CSV files:
  * upworthy_archive_exploratory_max_effet_size_dataset.csv
  * upworthy_archive_exploratory_min_effet_size_dataset.csv
* Produce two charts, each showing the results of every test in the max or the min dataset (see `visualizing-max-min-effect-packages.R.ipynb`)
* Conduct two fixed effects models:
  * One testing the maximum effect of using a number in a headline
  * The other testing the minimum effect of using a number in a headline
* Write a report (max 650 words) with the imagined audience of Upworthy editors to give them advice about whether adding at least one number of any kind to a headline influences the click-rate on a story. This report should include the following paragraphs:
  * One paragraph to introduce the question and describe the tests being analyzed (for example, reporting how many tests, how many headlines, etc). Since it's a report to a decision-maker, you also include a sentence about what you found.
  * One paragraph summarizing the range of effects in the min and max datasets (you can include the charts here)
  * One paragraph summarizing the results of the fixed effects models. Report the coefficient for `has_treatment` for the max and the min results.
  * One paragraph that interprets the result and offers advice

## Organizing Your Team
Since this is a team project, CoCalc will be especially helpful as you split up effort. Here's one idea for how to organize:
* One person develops the dataset (getting this done quickly will be important, since everything else depends on this)
* One person uses the max and min datasets to create charts and write the second paragraph
* One person runs the fixed effects models (remember: you don't have to reproduce the whole notebook- just skip down to cell 10)
* One person develops an initial draft that others fill in as you complete bits of data analysis
* Pairs of you review each other's code and analysis, to catch any glitches
* Everyone reviews the results and contributes to the last and first paragraphs
