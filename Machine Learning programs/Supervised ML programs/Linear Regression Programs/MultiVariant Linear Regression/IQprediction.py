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

# Importing statsmodel for applying the BackWard Elimination
import statsmodels.formula.api as sm

with contextlib.suppress((FileNotFoundError, ValueError)):
    # Loading the person iq_size datasets
    iq_df = pd.read_csv("iq_size.csv")

    # Splitting the features and labels data
    features = iq_df.iloc[:, 1:].values.reshape(-1,3)

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
    features_OLS.summary() """

    """ After this the third column is also removed thus indicating that
    the brain size is the only important feature for predicting the IQ of a
    person. Thus results from both .coef_ method and Backward elimination methd
    is same.It is rarely possible that both the method gives different values
    """

    # Alternative of above method using looping
    # .pvalues give an array of the P%-values from the summary table

    # loping through column size
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
