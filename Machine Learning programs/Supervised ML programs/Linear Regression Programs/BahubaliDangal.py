# -*- coding: utf-8 -*-

""" A program to develop a ML model to predict which movie will earn more on
a particular day after training the model on the given records """

# Importing pandas, numpy, matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing contextlib module to enhance functionality of with keyword
from contextlib import suppress

# Importing the scikit learn module for splitting training and testing data
# from sklearn.model_selection import train_test_split

# Importing scikit learn module to import LinearRegression class
from sklearn.linear_model import LinearRegression

# Importing exceptions module of Scikit learn
from sklearn.exceptions import NotFittedError

with suppress(FileNotFoundError):
    # Loading the datasets containing the 9 days collections record of Bahubali and Dangal
    collection_df = pd.read_csv("Bahubali2_vs_Dangal.csv")


# Defining a function for training models for various labels
def model_train(obj, x, y, test_in):
    obj.fit(x, y)
    return obj.predict(test_in)


with suppress((NameError, TypeError, ValueError, NotFittedError)):

    # Splitting the features and lables
    features = collection_df.iloc[:, 0].values.reshape(-1, 1)
    label_1 = collection_df.iloc[:, 1].values.reshape(-1, 1)
    label_2 = collection_df.iloc[:, -1].values.reshape(-1, 1)

    # Training our model
    # Creating an object for LinearRegression class
    regressor = LinearRegression()

    # Bahubali 10th day collection
    Bahu_coll = model_train(regressor, features, label_1, 10)

    # Dangal 10th day collection
    Dangal_coll = model_train(regressor, features, label_2, 10)

    # Visualizing the collection of the movies using pie chart
    plt.pie([float(Bahu_coll), float(Dangal_coll)], explode=[0, 0], labels=['Bahubali','Dangal'], autopct="%1.1f%%")
    plt.axis("equal")
    plt.show()