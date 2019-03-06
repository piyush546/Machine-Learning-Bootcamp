# -*- coding: utf-8 -*-
""" A program to make an image using numpy array """

# Importing the required module
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = np.full((8,8), 5.43355)
img[0][2] = 1
img[0][3] = 1
img[0][4] = 1
img[0][5] = 1
img[7][2] = 1
img[7][3] = 1
img[7][4] = 1
img[7][5] = 1

img[1][1] = 1
img[6][1] = 1

img[2][0] = 1
img[3][0] = 1
img[4][0] = 1
img[5][0] = 1
img[2][7] = 1
img[3][7] = 1
img[4][7] = 1
img[5][7] = 1

img[1][6] = 1
img[6][6] = 1

img[2][2] = 1
img[2][5] = 1

img[4][2] = 1
img[4][5] = 1

img[5][3] = 1
img[5][4] = 1

plt.imshow(img, "gray")

img_file = Image.fromarray(img, "RGB")
img_file.save("Smile.png")
img_file.show()