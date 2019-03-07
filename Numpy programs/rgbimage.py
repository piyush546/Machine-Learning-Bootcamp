# -*- coding: utf-8 -*-
""" Wap to create an  colored image using numpy array"""
# Importing the numpy and matplotlib module
import numpy as np
import matplotlib.pyplot as plt

# Importing Pillow libraray for saving the numpy array as image
from PIL import Image

# Defining the color codes for creating the image
numpy_img = [[(255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255)],
           [(255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255)],
           [(255, 0, 0), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 0, 0)],
           [(255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0)],
           [(255, 0, 0), (255, 255, 255), (0, 255, 0), (255, 255, 255), (255, 255, 255), (0, 255, 0), (255, 255, 255), (255, 0, 0)],
           [(255, 0, 0), (255, 255, 255), (255, 255, 255), (0, 255, 0), (0, 255, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0)],
           [(255, 255, 255),(255,0,0),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,0,0),(255,255,255)],
           [(255,255,255),(255,255,255),(255,0,0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255)]]

# Creating the image using .imshow
plt.imshow(np.array(numpy_img, dtype=np.uint8))

# Saving the numpy array as image
img_data = Image.fromarray(np.array(numpy_img,dtype=np.uint8), 'RGB')
img_data.save("colorsmile.png")
img_data.show()
