# -*- coding: utf-8 -*-

""" Minor Project - 
Our main objective in this project is to develop a Machine Learning model that
will be predicting the cost of the food served by the restaurants across 
different cities in India and to investigate the factors that really affect 
the cost.

Size of training set: 12,690 records

Size of test set: 4,231 records

Columns:

TITLE: The feature of the restaurant which can help identify what and for 
whom it is suitable for.

RESTAURANT_ID: A unique ID for each restaurant.

CUISINES: The variety of cuisines that the restaurant offers.

TIME: The open hours of the restaurant.

CITY: The city in which the restaurant is located.

LOCALITY: The locality of the restaurant.

RATING: The average rating of the restaurant by customers.

VOTES: The overall votes received by the restaurant.

COST: The average cost of a two-person meal.
 
"""

# Data Preprocessing and Visualization Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the training and testing dataset
train_data = pd.read_excel("Data_Train.xlsx")
test_data = pd.read_excel("Data_Test.xlsx")

# Extracting the features and labels from training data
features = train_data.iloc[:,:-1]
labels = train_data.iloc[:,-1].values.reshape(-1,1)

# Fetching the datatypes of each column
column_df = test_data.dtypes.reset_index()
# Renaming the columns
column_df.columns = ['features', 'datatypes']
from sklearn.feature_extraction import FeatureHasher
h = FeatureHasher(n_features=8, input_type="string")
features = h.transform(features).toarray()
test_data = h.transform(test_data).toarray()
labels = h.transform(labels).toarray()
from sklearn.linear_model import LinearRegression
lin  = LinearRegression()
lin.fit(features, labels)
features.iloc[:,2].nunique()

