# -*- coding: utf-8 -*-
""" 
Q1. (Create a program that fulfills the following specification.)
affairs.csv
Import the affairs.csv file.
It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.
Description of Variables
The dataset contains 6366 observations of 10 variables:(modified and cleaned)
rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)
age: women's age
yrs_married: number of years married
children: number of children
religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)
educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)
occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)
occupation_husb: husband's occupation (same coding as above)
affair: outcome 0/1, where 1 means a woman had at least 1 affair.
Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.
NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!
What percentage of total women actually had an affair?
(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)
Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.
Optional:
Build an optimum model, observe all the coefficients.
"""

# Importing the data processing module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the affairs.csv datasets
affairs_data = pd.read_csv("affairs.csv")

# 