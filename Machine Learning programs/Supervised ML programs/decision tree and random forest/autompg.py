# -*- coding: utf-8 -*-
"""
1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
"""

# Data processing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset
dataset = pd.read_csv("autompg.txt", delim_whitespace = True, header = None)

# Changing the column names
dataset.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

# fetching the car name with maximum mpg
car_name = dataset["car name"][dataset["mpg"].argmax()]
dataset["horsepower"] = dataset["horsepower"].replace("?", 100.0)
dataset["horsepower"] = dataset["horsepower"].astype("float64")
features = dataset.drop("mpg", axis=1)
features = pd.get_dummies(features)
features = features.iloc[:,:-1]
labels = dataset["mpg"]
from sklearn.model_selection import train_test_split

feature_train, feature_test, label_train, label_test = train_test_split(features, labels, test_size = 0.2, random_state=0)
# Creating the decision tree for regression
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor()
regressor.fit(feature_train, label_train)

labels_pred = regressor.predict(feature_test)

print(regressor.score(feature_test, label_test))




