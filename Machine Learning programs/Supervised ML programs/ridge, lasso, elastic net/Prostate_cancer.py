# -*- coding: utf-8 -*-
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

# Data preprocessing modules
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


# Fetching the dataset
dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delim_whitespace=True)

# Developing the models
features = dataset.drop("lpsa", axis=1)
labels = dataset["lpsa"]


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
regressor = LinearRegression()
regressor.fit(features, labels)
print(regressor.score(features, labels))
print(mean_absolute_error(labels, regressor.predict(features)))
print(mean_squared_error(labels, regressor.predict(features)))
print(np.sqrt(mean_squared_error(labels, regressor.predict(features))))
print((np.mean(labels)*0.1)*100)


""" Regularization
ridge regression,lasso and elastic net. These alternative linear fitting techniques can 
improve a model's performance and interpretability.
"""

from sklearn.linear_model import Ridge, Lasso, ElasticNet
ridge = Ridge()
lasso = Lasso()
en = ElasticNet()

ridge.fit(features, labels)
lasso.fit(features, labels)
en.fit(features, labels)

print(ridge.score(features, labels))
print(lasso.score(features, labels))
print(en.score(features, labels))

print(mean_absolute_error(labels, ridge.predict(features)))
print(mean_squared_error(labels, ridge.predict(features))*100)
print(np.sqrt(mean_squared_error(labels, ridge.predict(features))*100))


print(mean_absolute_error(labels, lasso.predict(features)))
print(mean_squared_error(labels, lasso.predict(features))*100)
print(np.sqrt(mean_squared_error(labels, lasso.predict(features))*100))

print(mean_absolute_error(labels, en.predict(features)))
print(mean_squared_error(labels, en.predict(features))*100)
print(np.sqrt(mean_squared_error(labels, en.predict(features))*100))

###############################################################
# Converting the regression dataset into classification data
# Converting lpsa to 0 and 1 based on the mean comparison

avg_lpsa = np.mean(labels)


labels = labels.apply(lambda x: 1 if x>avg_lpsa else 0)

from sklearn.tree import DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(features, labels)
print(dt_classifier.score(features, labels))

from sklearn.linear_model import LogisticRegression
lr_classifier = LogisticRegression()
lr_classifier.fit(features, labels)
print(lr_classifier.score(features, labels))