# -*- coding: utf-8 -*-

""" A program to calculate area and perimeter of a circle using math module """

# importing math module
from math import pi

# taking radius of the circle from user
radius = int(input("Enter radius of the circle:"))

# Storing area and perimeter of the circle
area = pi*(radius**2)
perimeter = 2*pi*radius

# To print the area and perimeter of circle
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)
