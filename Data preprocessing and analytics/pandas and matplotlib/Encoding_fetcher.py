# -*- coding: utf-8 -*-
""" A program to detect the encoding of an file """

# Importing chardet module
# It is universal encoding detector module of python
# Install it using pip install chardet
import chardet


# Creating a class for fetching the encoding of the file
class detect_encoding():
    # Inintializing the filename
    def __init__(self, filename):
        self.filename = filename
        with open(f'{self.filename}', 'rb') as fileobj:
            self.result = chardet.detect(fileobj.read())

    # Fetching the encoding of the file and returning it
    def code(self):
        return self.result['encoding']


# Creating the obj of the class
obj = detect_encoding("training_titanic.csv")

# Printing the encoding of the file
print(obj.code())
