""" A Program to train a Supervised ML model using Regression algorithm
where we have to predict Intelligence of person on multiple variables(features)
provided """

# Multiple Linear Regression / Multivariant Linear Regression

# Importing the data analytics modules
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Importing the contextlib module
import contextlib

# Importing the scikit module
# Module to split the training and testing data with the given
from sklearn.model_selection import train_test_split

# Module to apply LinearRegression algorithm
from sklearn.linear_model import LinearRegression

# Importing statsmodel for applying the BackWard Elimination
import statsmodels.formula.api as sm

with contextlib.suppress((FileNotFoundError, ValueError)):
    # Loading the person iq_size datasets
    iq_df = pd.read_csv("iq_size.csv")

    # Splitting the features and labels data
    features = iq_df.iloc[:, 1:].values.reshape(-1,3)
    
    """ 
    # trained ,tested and visualized on all features seperately
    
    features = iq_df.iloc[:, 1].values.reshape(-1,1)
    
    features = iq_df.iloc[:, 2].values.reshape(-1,1)
    
    features = iq_df.iloc[:, 3].values.reshape(-1,1)
    
    plt.scatter(features_test, labels_test)
    plt.plot(features_train, regressor.predict(features_train))
    plt.show()
    """

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
    
    
    """ # To find the intercept value
    regressor.intercept_ """

    # Finding the most important feature using Backtracking Elimination
    features_obj = features

    # Need to add a column containing contant value which remain constant throughout
    features_obj = np.append(np.ones((38, 1)), features_obj, axis=1)

    """ # To train the model
    # OLS - Optimal least square
    features_OLS = sm.OLS(endog=labels, exog=features_obj).fit()

    # To show the stats
    features_OLS.summary()

    # P-value is related to hypothesis testing in statistics. It help in predicting the significane of our results.

    # Removing the 4th column as it's P% is more than 5%
    features_obj = features_obj[:, [0, 1, 2]]

    features_OLS = sm.OLS(endog=labels, exog=features_obj).fit()

    # To show the stats
    features_OLS.summary()

    # Removing the 1st column
    features_obj = features_obj[:, [1, 2]]

    features_OLS = sm.OLS(endog=labels, exog=features_obj).fit()


    # To show the stats
    features_OLS.summary()
    
    
    features_obj = features_obj[:,[0]]
    
    features_OLS = sm.OLS(endog=labels, exog=features_obj).fit()
    
    features_OLS.summary()"""

    """ After this the third column is also removed thus indicating that
    the brain size is the only important feature for predicting the IQ of a
    person. Thus results from both .coef_ method and Backward elimination methd
    is same.It is rarely possible that both the method gives different values
    """

    # Alternative of above method using looping
    # .pvalues give an array of the P%-values from the summary table

    # looping through column size
    for var in range(0, (features_obj.shape)[-1]):
        features_OLS = sm.OLS(endog=labels, exog=features_obj).fit()
        d = features_OLS.pvalues.max()
        if len([x for x in features_OLS.pvalues if x > 0.05]):

            # .where gives the index of the value passed as parameter in the given array
            a = np.where(features_OLS.pvalues == d)

            # .delete delete the particular element from an array which index is passed as argument
            features_obj = np.delete(features_obj, a, 1)
        else:
            break
        
        
    """ Alternative - 
    # A new way to import api
    import statsmodels.api as sm
    
    features_obj = features[:, [0,1,2]]
    
    # To add the constant 
    features_obj = sm.add_constant(features_obj)
    
    while (True):
        regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
        p_values = regressor_OLS.pvalues
        if p_values.max() > 0.05 :
            # deleting a whole column if required that's why 3rd parameter is 1 means axis=1
            features_obj = np.delete(features_obj, p_values.argmax(),1)
        else:
            break
            
    """

    
    """# Visualization of the most important feature
    features_train_1, features_test_2, labels_train_1, labels_test_2 = train_test_split(features_obj, labels, test_size=0.2, random_state=15)
    obj = regressor.fit(features_train_1,labels_train_1)
    
    #features_grid = np.arange(min(features_obj), max(features_obj),0.01).reshape(-1,1)
    plt.scatter(features_test_2, labels_test_2)
    plt.plot(features_train_1, obj.predict(features_train_1))
    plt.show()"""
    
dataset = pd.read_csv("online_marketing.sql")
pd.read_sql()