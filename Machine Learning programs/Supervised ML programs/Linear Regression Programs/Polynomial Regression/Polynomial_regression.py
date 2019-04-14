# -*- coding: utf-8 -*-
""" A program to develop a ML model to predict height of blue gills fish
according to their age using Polynomial Regression """


""" Polynomial Regression is an extended version of Single variant Linear 
regression as far I know where the degree of the feature is extended """

# Impoorting data preprocessing and visualization modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing suppress method from contextlib module
from contextlib import suppress
# Importing the train_test_split method to split the training data and testing data
from sklearn.model_selection import train_test_split

# Importing linearRegression class from scikit learn module
from sklearn.linear_model import LinearRegression

# importing PolynomialRegression tools from scikit learn to handle Polynomial Regression processing
from sklearn.preprocessing import PolynomialFeatures

# Processing stage
with suppress((FileNotFoundError, TypeError, ValueError)):

    # Loading the Bluegillfish datasets
    bluegill_df = pd.read_csv('bluegills.csv')

    # Extracting the features and labels
    features = bluegill_df.iloc[:, :-1].values
    labels = bluegill_df.iloc[:, -1].values


    """ Initializing an object for PolynomialFeatures class with a degree 2
     which means the feature of the model it to be divided into 3 columns
     and its values get raised to power 2 i.e y =  x**2 + x**1 + x**0 """
    poly_obj = PolynomialFeatures(degree=2)

    # Splitting the training data and testing data
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state=0)

    # Inintializing the linearRegression class object
    regressor = LinearRegression()

    # Training our model according to linear_variant regression
    linear_fit = regressor.fit(features_train, labels_train)

    ## To predict the height for the age 5 according to single variant linear regression model
    linear_fit.predict(5)
    
    # Predicting linearmodel score
    linear_train_score = regressor.score(features_train, labels_train)
    linear_test_score = regressor.score(features_test, labels_test)
    
    # Visualization
    plt.scatter(features_test, labels_test)
    plt.plot(features_train, linear_fit.predict(features_train))
    plt.xlabel
    

    # Training our model according to polynomial regression technique
    # Fit_transform will modify the faetures according to the given degree and train the model according to that
    poly_fit = regressor.fit(poly_obj.fit_transform(features_train), labels_train)

    # To predict the height for the age 5 according to polynomial regression model
    poly_fit.predict(poly_obj.transform(5))

    # To visualize the Best fit line
    features_grid = np.arange(min(features), max(features), 0.01).reshape(-1, 1)
    plt.scatter(features_test, labels_test)
    plt.plot(features_grid, poly_fit.predict(poly_obj.transform(features_grid)))
    plt.title('Fish age and Height relationship')
    plt.xlabel('age')
    plt.ylabel('height')

    # Predicting the model training and testing score
    ploy_model_train_score = regressor.score(poly_obj.fit_transform(features_train), labels_train)
    poly_model_test_score = regressor.score(poly_obj.fit_transform(features_test), labels_test)
    
    