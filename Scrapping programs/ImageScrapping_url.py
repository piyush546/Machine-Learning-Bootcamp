# -*- coding: utf-8 -*-
""" A program to scarp a image from the given url and save it on our pc """

# Importing requests module
import requests

# Importing contetxlib module
import contextlib

# Url of the image
url = "https://myfoodstory.com/wp-content/uploads/2017/10/The-Best-Indian-Punjabi-Samosa-1.jpg"

with contextlib.suppress(AttributeError):
    # Fetching the response data in byte form using requests.get(url).content method
    # requests.get(url).text gives response data in unicode format
    image_data = requests.post(url).content

# Saving the image on local pc using file handling method
with open("Scrapped_img.jpg", "wb+") as fileobj:
    fileobj.write(image_data)
