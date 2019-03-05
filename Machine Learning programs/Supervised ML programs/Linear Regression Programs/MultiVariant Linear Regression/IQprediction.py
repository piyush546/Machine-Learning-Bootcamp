""" A Program to train a Supervised ML model using Regression algorithm
where we have to predict Intelligence of person on multiple variables(features)
provided """

# Multiple Linear Regression / Multivariant Linear Regression

# Importing the data analytics modules
import pandas as pd
import numpy as np

# Importing the contextlib module
import contextlib

# Importing the scikit module
# Module to split the training and testing data with the given
from sklearn.model_selection import train_test_split

# Module to apply LinearRegression algorithm
from sklearn.linear_model import LinearRegression

#

with contextlib.suppress(FileNotFoundError):
    # Loading the person iq_size datasets
    iq_df = pd.read_csv("iq_size.csv")

    # Splitting the features and labels data
    features = iq_df.iloc[:, 1:].values

    labels = iq_df.iloc[:, 0].values.reshape(-1, 1)

    # Splitting the training and testing data
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=15)

    # Initializing a refrence variable for LinearRegression class
    regressor = LinearRegression()

    # Fitting the training model in our model
    regressor.fit(features_train, labels_train)

    # Predicting the output for testing data
    test_result = regressor.predict(features_test)

    # Predicting the score for our model
    test_score = regressor.score(features_test, labels_test)
    train_score = regressor.score(features_train, labels_train)

    # To predict Intelligence for given input data
    input_data = np.array([90, 70, 150])
    predicted_intely = regressor.predict(input_data.reshape(-1, 3))

    # To get the weights of the features that indicate which feature is most important for ouput prediction
    features_weights = regressor.coef_

    # Finding the most important feature using Backtracking