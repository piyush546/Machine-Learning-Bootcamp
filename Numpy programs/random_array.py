# -*- coding: utf-8 -*-
""" A program to create an array with 40 random values in the range 5 to 15 """

# Importing numpy module
import numpy as np

# Creating a matrix containing random values using numpy.random.randint()
# and storing it in variable random_array
random_array = np.random.randint(5, 15, 40)

# Printing the array as well as its size for checking the result
print(random_array.size)
print(random_array)
