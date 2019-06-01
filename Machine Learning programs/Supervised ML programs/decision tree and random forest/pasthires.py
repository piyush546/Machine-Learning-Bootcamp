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

"""def mod_fun(value):
    if value is "Y":
        return 1
    else:
        return 0
"""
dataset.iloc[:,[1,4,5,6]] = dataset.iloc[:,[1,4,5,6]].applymap(lambda x: 1 if x is "Y" else 0)
mod_dict = {"BS":0, "MS":1, "PhD":2}
dataset.iloc[:,3] = dataset["Level of Education"].map(mod_dict)

# To build the models
features = dataset.drop("Hired", axis=1)
labels = dataset.iloc[:,-1]

from sklearn.tree import DecisionTreeClassifier

tree_classf = DecisionTreeClassifier()
tree_classf.fit(features, labels)
print(tree_classf.score(features, labels))
print(tree_classf.predict(np.array([10, 1, 4, 0,1,0]).reshape(1,-1)))
print(tree_classf.predict(np.array([10, 0, 4, 1,0,1]).reshape(1,-1)))

from sklearn.ensemble import RandomForestClassifier
for_classf = RandomForestClassifier(n_estimators=10, random_state=0)
for_classf.fit(features, labels)
print(for_classf.score(features, labels))
print(for_classf.predict(np.array([10, 1, 4, 0,1,0]).reshape(1,-1)))
print(for_classf.predict(np.array([10, 0, 4, 1,0,1]).reshape(1,-1)))