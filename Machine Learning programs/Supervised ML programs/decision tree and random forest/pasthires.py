# -*- coding: utf-8 -*-
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not
based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some 
scale of 0-2.

Build and perform Decision tree based on the predictors and see how accurate 
your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of 
specific candidate profiles:

Predict employment of a currently employed 10-year veteran, 
previous employers 4, went to top-tire school, having Bachelor's Degree 
without Internship.


Predict employment of an unemployed 10-year veteran, ,previous employers 4, 
didn't went to any top-tire school, having Master's Degree with Internship.
"""

# Data preprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset
dataset = pd.read_csv("PastHires.csv")
