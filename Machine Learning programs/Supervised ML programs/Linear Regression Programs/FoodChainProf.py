# -*- coding: utf-8 -*-

""" A program to develop a ML model using Linear Regression algorithm to
predict profit for a food chain company """

""" Regression algorithm basically works on continuous data means like what
will be salary, by how much votes BJP will win, by how much wicket India
will win.

Regression models is a type of Supervised ML - (which predicts some sort of
values for given input. This is done by getting trained on some given
sets of input and output termed as training sets and finding the mapping
function according to those training sets)
In training sets the input which are independent are termed as features
and the output which are dependent corresponding to them are termed as labels

An example using mathematical equation-
y = f(x)
where x - independent variable
y - dependent variable
f - mapping function

Finding the mapping function helps in getting the design pattern for the
particular training sets and then it can be used to predict values according
to those mapping functions.
"""

# Importing pandas, numpy, matplotlib libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# scikitlearn module as it contain all machine learning algorithms
# Importing train_test_split for splitting the faetures and labels for training data and testing data
from sklearn.model_selection import train_test_split

# Importing LinearRegression class for training our ML model
from sklearn.linear_model import LinearRegression

# Contextlib module enhances the functionality of with keyword
import contextlib


# contextlib.suppress handles exception silently
""" This method is equivalent to -
try:
    model_data = pd.read_csv("FoodTruck.csv")
except FileNotFoundError:
    pass """
with contextlib.suppress(FileNotFoundError):
    model_data = pd.read_csv("FoodTruck.csv")

# Seperating the features and labels from model_data
# Features - Population
# Lables - Profit
model_features = model_data.iloc[:, :-1].values
model_labels = model_data.iloc[:, -1].values

# Splitting the collected data in training sets and testing sets
features_train, features_test, labels_train, labels_test = train_test_split(model_features, model_labels, test_size=0.15, random_state=0)

# Training our model using the training sets
# Creating the object of LinearRegression class
regressor = LinearRegression()

# Performing the training using fit method
regressor.fit(features_train, labels_train)

# Testing the model
model_test = regressor.predict(features_test)

# Plotting the regresssion model
plt.scatter(features_test, labels_test)
plt.plot(features_test, model_test)
plt.show()