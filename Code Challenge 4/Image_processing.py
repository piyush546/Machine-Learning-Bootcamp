# -*- coding: utf-8 -*-

# PIL - Python Imaging Library(Bascially Pillow is the name but PIL is used)
# Used for performimg various operations on image of various formats like jpg..

# Image module - represent a PIL image,load images from files, to create new images

# importing Image module from PIL
from PIL import Image


# Taking the name of the image
image_name = input("Enter the name of image:")
image_name = image_name+".jpg"

# To open the image to be processed
# An instance is used to store the opened image
image = Image.open(image_name)

# changing the image to Greyscale
img_convert = image.convert('L')

# Rotating the image
img_rotate = img_convert.rotate(90)

# to crop image at center top = (w+h)/2 and bottom = (w+h)/2
img_crop = img_rotate.crop((160, 204, 252, 252))

# To make a thumbnail of the opened image
img_crop.thumbnail((75, 75))

# Printing the image name after modifications
# image.filename is used to get original image file name
print("Output:thumbnail.BMP")

# To save and show the image after modification
img_crop.save("thumbnail.bmp","BMP")
img_crop.show()
