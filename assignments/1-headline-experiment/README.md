# Headline Experiment(Week 2 Assignment)

**COMM4940**

Cornell University Department of Communication

J. Nathan Matias ([@natematias](https://twitter.com/natematias))

> *Disclaimer: while this assignment includes reference to factual people, events, and experiments, the assignment is a hypothetical scenario.

## Background

One day in 2013, you receive an email from Upworthy, an organization dedicated to amplifying meaningful and inspiring stories. 

Upworthy wants to reach the greatest number of people with the inspiring story of a teenager who won a major engineering competition. They know that headline choice might influence how many people click and read the article. 

As an experimenter who's taken COMM4940, you convince Upworthy to carry out a field experiment to compare the outcomes of different headlines. Their writers produce four headlines which you then set up in an A/B test. After 14,951 people are randomly assigned to see one of the headlines, you collect the data.

Now that the experiment is complete and you have collected all the data, it's time for you to analyze the results and write a report to Upworthy so they can choose their headline. But there's a wrinkle: in the time since you were commissioned to do the study, a social media analytics company offered to provide real-time analytics to the Upworthy based on "predictive models" and "data science." This company argues that A/B testing is slow and wasteful, and that their linear regression models will give the foundation "real-time predictions" that they can use to make daily decisions about how to post articles.

## Assignment
For this assignment, create a report for Upworthy that describes what you learned and proposes which headline to use. You should also explain the benefits of causal inference, and argue why field experiments could help the foundation test its headlines and beyond.

Your essay should include:

* a paragraph **describing the experiment design**, including the intervention being tested, the outcome measures being used, and how many participants were included.
* a paragraph **summarizing the findings**. It should summarize the outcome variable, the means for each condition, and include a statement of the effect size.
* a paragraph that **suggests a course of action**, contextualizing the findings in a way that the organization would normally think about, such as the payoff per thousand people who see the headline. Think about whether the result could inform future headline writing. Make sure to reflect on the limitations of the sample, which is drawn from the Upworthy's homepage.
* include a **table of results** and an **illustration of the average treatment effect**. You could (a) show the effect with error bars or (b) show fitted(predicted) values for each condition, with error bars for the treatment (color). If you show fitted values, document details of any covariates(predictors) used to generate the fitted values (such as weekend). 
* a paragraph that builds on this finding in the attempt to **convince Upworthy to do more testing** with headlines and in the organization.

The assignment can be submitted via Canvas.

## Purpose of the assignment
The main purpose of this assignment is to gain a rough sense of where different students are in the skills that this class will support you to develop

* using R to analyze data, including conduct regression models
* reasoning through the contribution and the limitations of a result
* illustrating results graphically
* writing clear, accurate language about statistical findings in a way that a general audience can understand

## Resources
This folder includes everything you need to do this assignment:
* data from the experiment (	assignment-one-impressions.csv)
* the headlines being tested (assignment-one-heds.csv)
* code for conducting the analysis and generating illustrations (headline-analysis-example.R.ipynb)
