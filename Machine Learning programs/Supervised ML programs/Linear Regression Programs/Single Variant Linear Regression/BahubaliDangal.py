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

with suppress((FileNotFoundError, NameError, TypeError, ValueError, NotFittedError)):
    
    
    # Loading the datasets containing the 9 days collections record of Bahubali and Dangal
    collection_df = pd.read_csv("Bahubali2_vs_Dangal.csv")


    # Defining a function for training models for various labels
    def model_train(x, y, test_in):
        # Training our model
        # Creating an object for LinearRegression class
        obj = LinearRegression()
        return obj.fit(x, y), obj.predict(test_in)

    # Splitting the features and lables
    features = collection_df.iloc[:, 0].values.reshape(-1, 1)
    label_1 = collection_df.iloc[:, 1].values.reshape(-1, 1)
    label_2 = collection_df.iloc[:, -1].values.reshape(-1, 1)


    """ A wrong approcah - For Multiple label
     Bahubali 10th day collection
     Bahu_coll = model_train(regressor, features, [label_1,label_2], 10)
     ValueError: Found array with dim 3. Estimator expected <= 2.
     """

    """ A correct approach - For multiple label
     import pandas as pd

    dataset = pd.read_csv("Bahubali2_vs_Dangal.csv")

    feature = dataset.iloc[:,0:1].values
    labels = dataset.iloc[:,1:].values

    from sklearn.linear_model import LinearRegression

    box = LinearRegression()

    box.fit(feature, labels)

    box.predict(10)

    import matplotlib.pyplot as plt
    plt.plot(feature, box.predict(feature))
    """

    # Bahubali 10th day collection
    reg_obj_1, Bahu_coll = model_train(features, label_1, 10)
    # Dangal 10th day collection
    reg_obj_2, Dangal_coll = model_train(features, label_2, 10)

    # Visualizing the collection of the movies using pie chart
    plt.pie([float(Bahu_coll), float(Dangal_coll)], explode=[0, 0], labels=['Bahubali','Dangal'], autopct="%1.1f%%")
    plt.axis("equal")
    plt.title("Bahubali vs Dangal collection on 10th day")
    plt.show()
    
    # Visualizing the best fit lines
    plt.plot(features, reg_obj_1.predict(features),label="Bahu_coll")
    plt.plot(features, reg_obj_2.predict(features),label="Dangal_coll")
    plt.title("Bahubali vs Dangal collection on 10th day")
    plt.legend()
    plt.show()
    
    
    