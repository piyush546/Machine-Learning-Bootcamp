# -*- coding: utf-8 -*-
# Program to understand working of numpy with its various operation

# To use numpy features importing numpy modules
import numpy as np

# A 3*3 matrix stored in variable matrix_1
matrix_1 = np.array([[1,    2,   3],   [4,   5,   6],   [7,   8,   9]])

# To get a string representation of an array.and storing it in mat_str
mat_str = np.array2string(matrix_1)

# To get the shape,  datas type,  dimensional of the matrix
print(matrix_1.shape)
print(matrix_1.dtype)
print(matrix_1.ndim)

# To create a matrix of floating numbers
matrix_2 = np.float_(matrix_1)

# to print datas type of matrix_2
print(matrix_2.dtype)

# similarly np.int_(matrix_2) can be usec to create integer matrix
# we can also specify bit size instead of '_' like 32 or 64

# To create matrix within specified range and store it in matrix_3
matrix_3 = np.arange(1,  10,  dtype=np.float)

# To create an array with random values in a given range and size
# start(1) is inclusive and stop(100) is exclusive
matrix_4 = np.random.randint(1, 100, 20)

# To create an array with equally spaced values in a given range and size
# start(1) and stop(100)of the range both are inclusive
matrix_5 = np.linspace(1, 100, 20)
