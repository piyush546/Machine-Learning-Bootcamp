# -*- coding: utf-8 -*-

"""
T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.

"""

# Preprocessing and Visualization modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sklearn modules
from sklearn.cluster import KMeans

# Exceptioon Handling module
# import contextlib

# Loading the tshirt csv
tshirt_data = pd.read_csv("tshirts.csv")

# Extracting the features i.e height and weight
features = tshirt_data.iloc[:, 1:].values

