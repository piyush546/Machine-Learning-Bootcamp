# -*- coding: utf-8 -*-

""" A program to visualize some given data by histogram and calculate their
std.deviation and variance """

# Importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# To get the normaml distribution of the data with mean 150 , std.deviation 20 and size 1000
normal_matrix = np.random.normal(150, 20, 1000)

# To plot the histogram of the collected data with bucket size 100
plt.hist(normal_matrix, bins=100)
plt.show()

# To calculate the std deviation and variance of the fetched data
std_dev = np.std(normal_matrix)

variance = np.var(normal_matrix)
