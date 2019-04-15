# -*- coding: utf-8 -*-

"""
Code Challenge 
"""

#Import the local file cars.csv and split the data set equally into test set and training set.
#Print it and save both data sets  into two new .csv file.

import pandas as pd
import numpy as np
dataset = pd.read_csv('cars.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values.reshape(-1,1)

# Importing the dataset

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
print (X_train,X_test,y_train, y_test)

# Write code to save in the csv file

# Combining the features and labels in both train and test data
train_data = np.concatenate([X_train, y_train],axis=1)
test_data = np.concatenate([X_test, y_test], axis=1)

# Fetching all the columns name from the original dataset
head = list(dataset.columns)

# Framing the test and train dataframe
train_df, test_df = pd.DataFrame(), pd.DataFrame()
for var in range(0,12):
    train_df[head[var]] = train_data[:, var]
    test_df[head[var]] = test_data[:, var]

# Creating seperate train and test csv files
train_df.to_csv("Train.csv")
test_df.to_csv("Test.csv")

# Printing the train and test dataframes
print("train_data:", train_df)
print("test_data:", test_df)

# Arranging all the features in one dataframe and all the labels in one dataframe
features_df = dataset.iloc[:,:11]
labels_df = dataset['Leather'])

