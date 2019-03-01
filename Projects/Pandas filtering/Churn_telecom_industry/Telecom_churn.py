# -*- coding: utf-8 -*-
""" """
# Import pandas, numpy, matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the scikit learn
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

# Importing contextlib to enhance with functionality
import contextlib

with contextlib.suppress(FileNotFoundError):
    # Loading the datasets containing the Telecom churn data
    churn_df = pd.read_csv("Telecom_churn.csv")

# ***************************************** #
with contextlib.suppress((NameError, ValueError, TypeError)):

    # To do churn analysis
    churn_analysis = churn_df['churn'].value_counts()

    # Visualization of the churn analysis
    plt.pie(churn_analysis,labels=['False','True'], autopct="%1.1f%%")
    plt.axis("equal")
    plt.show()

# ******************************************** #
with contextlib.suppress((NameError, ValueError, TypeError)):
    features = churn_df['total day calls'].values.reshape(-1,1)
    labels = churn_df['total day charge'].values.reshape(-1,1)
    features_train,features_test,labels_train,labels_test = train_test_split(features,labels, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(features_train, labels_train)
    test_data = regressor.predict(features_test)
    plt.scatter(features_test, labels_test)
    plt.plot(features_train, labels_train)
    plt.show()