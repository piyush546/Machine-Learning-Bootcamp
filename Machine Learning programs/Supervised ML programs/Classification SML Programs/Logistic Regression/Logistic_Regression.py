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



""" Classification is a type Supervised ML where the ouputs are not a 
continuous values rather they are discrete values like 0 and 1.
Bascially we try to classify whether according to feature
does this lie in this class or not.For e.g with the scores and overs we predict 
whether the team will win the match or not"""

""" Classification have many methods like Logistic Regression , KNN etc."""

""" Logistic Regression is a classification algorithm based on logit function
(odd logs). Ti might produce a less accurate answer in compare to KNN algo but
it is time efficient in compare to KNN """

# SparseMatrix - A matrix whose most of the elements are zero
# DenseMatrix - A matrix whose most of the elements are non-zero

# Importing the data processing module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Modules of scikit learn
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Module for exception handling
import contextlib as clb

with clb.suppress((TypeError, ValueError, NameError)):
    # Loading the affairs.csv datasets
    affairs_data = pd.read_csv("affairs.csv")
    
    # Splitting the datasets in features and labels
    features = affairs_data.iloc[:, :-1].values
    labels = affairs_data.iloc[:, -1].values
    
    
    # Preprocessing stage
    # Initializing the sparse equals False creates an array of encoded value instead of sparse matrix
    # if sparse is true then we have to use .toarray method to convert the sparse matrix into array
    onehotencoder1 = OneHotEncoder(categorical_features = [6],sparse=False)
    features = onehotencoder1.fit_transform(features)
    features = features[:, 1:]
    
    onehotencoder2 = OneHotEncoder(categorical_features = [11])
    features = onehotencoder2.fit_transform(features).toarray()
    features = features[:, 1:]
    
    # splitting the training data and test data
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=0)
    
    # standard scaling
    sc = StandardScaler()
    
    features_train = sc.fit_transform(features_train)
    
    features_test = sc.transform(features_test)
    
    # Training the model
    
    classifier = LogisticRegression()
    classifier.fit(features_train, labels_train)
    
    # Testing the model
    labels_pred = classifier.predict(features_test)
    
    """
    # Coefficient weightage
    classifier.coef_
    
    # Intercept
    classifier.intercept_
    """
    # Confusion matrix
    cm = confusion_matrix(labels_test, labels_pred)
    
    print("Training score:", classifier.score(features_train, labels_train))
    print("Testing score:", classifier.score(features_test, labels_test))
    
    # To predict the affair classification for given values
    values = np.array([1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,16]).reshape(1,-1)
    values = sc.transform(values)
    print("Result:", classifier.predict(values))
    