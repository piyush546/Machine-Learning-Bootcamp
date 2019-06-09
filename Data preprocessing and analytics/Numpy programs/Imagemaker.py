# -*- coding: utf-8 -*-
""" A program to make an graycsaleimage using numpy array """

# Importing the numpy and matplotlib module
import numpy as np
import matplotlib.pyplot as plt

# Importing Pillow libraray for saving the numpy array as image
from PIL import Image

# Defining the color codes for creating the image
img = [[1, 1, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 1, 1, 0],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [1, 1, 0, 0, 0, 0, 1, 1]]

# Creating the image using .imshow
plt.imshow(np.array(img,dtype=np.uint64), 'gray')

# Saving the numpy array as image
img_file = Image.fromarray(np.array(img,dtype=np.uint64), "I")
img_file.save("Smile.png")
img_file.show()
