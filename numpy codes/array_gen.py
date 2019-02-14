# -*- coding: utf-8 -*-
""" A program to create an array for given inputs of specified dimensions"""

# Importing numpy module
import numpy as np

""" Creating an array for the given inputs and storing it in a
variable named array_gen """
array_gen = np.array([6, 9, 2, 3, 5, 8, 1, 5, 4])

""" Reshaping the existing array according to the given dimension and storing
it in a variable named array_mod """
# Reshape and resize both can be used to do this work
# Resize changes the shape of actual array means return type is None
# Reshape changes returns a modified instance or object of actual array
array_mod = array_gen.reshape(3, 3)

# Printing the original and modified array
print("original array:", array_gen)
print("modified array:", array_mod)
