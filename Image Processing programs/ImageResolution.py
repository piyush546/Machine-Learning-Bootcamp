"""# -*- coding: utf-8 -*-"""

# PIL library is used to perform actions on the images of any kind
from PIL import Image

# opening the required image
img = Image.open("sample.jpg")

# To get the resolution of the image
width, height = img.size

print("Resolution of image is: %d*%d" % (width, height))
