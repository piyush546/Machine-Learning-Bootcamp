# -*- coding: utf-8 -*-

# To perform operations related to os like related with folder....
import os

import re
from PIL import Image

# To get the images name from a particular folder
List = os.listdir("..\Code challenge 4")

d = 0


# A function to resize the PNG images
def Resize(image):
    img_obj = Image.open(image)
    img_resize = img_obj.resize((100, 100))
    img_resize.save(f'output{d+1}.png', "PNG")


for img in range(0, len(List)):
    img_name = re.search(r'(\.png)$', List[img])
    if img_name is None:
        continue
    else:
        Resize(List[img])
