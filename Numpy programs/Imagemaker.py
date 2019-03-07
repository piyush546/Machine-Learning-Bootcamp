# -*- coding: utf-8 -*-
""" A program to make an image using numpy array """

# Importing the required module
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = np.ones((8, 8))

img = [[1, 1, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 1, 1, 0],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [1, 1, 0, 0, 0, 0, 1, 1]]

plt.imshow(np.array(img), "gray")


img_file = Image.fromarray(np.array(img), "I")
img_file.save("Smile.png")
img_file.show()
