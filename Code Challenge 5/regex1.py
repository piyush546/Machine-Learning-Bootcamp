# -*- coding: utf-8 -*-

# Importing regular expression module
import re

# Taking the Inputs
List = input().split()

# Storing the required format
regex = re.compile("[.+-]*[0-9]+.")

# finding the required expression
for var in range(0, len(List)):
    result = regex.match(List[var])
    if result is None:
        print("False")
    else:
        print("True")
# input = 4 +4.12 -4.20 4.000
"""output:False
True
True
True"""
