# -*- coding: utf-8 -*-

""" A program to calculate factorial of a number using math module """

# importing math module
from math import factorial

# taking input from user whose factorial is to be found
num = int(input("Enter the number whose factorial is to be found:"))

# printing factorial of number
print("factorial of"+str(num)+":", factorial(num))
