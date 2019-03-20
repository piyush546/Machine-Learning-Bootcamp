# -*- coding: utf-8 -*-
""" A program to perform addition of two numbers with the illustration of
context manager workflow """

# Importing time from time module
from time import time

# Defining a class to illustrate the resource management
class Timer():

    # Starting phase of the code execution
    def __enter__(self):
        self.start = time()
        print("Starting at {}".format(self.start))

    # End Phase of the code execution
    # *excp accepts the Exception from with statement code body
    def __exit__(self, *excp):
        self.end = time() - self.start
        print("Execution time {0:.2f}s".format(self.end))

# Calling the class and performing the addition of two numbers
# Middle phase of the code execution
with Timer():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    print("sum of the entered numbers:", a+b)

#############################################################################
""" Implementing the above program using contextlib module and creating
our own contextmanager for the above task"""

# Importing contextmanager from contextlib module
from contextlib import contextmanager

# Defining our own contextmanager instead of class
# Decorators
@contextmanager
def Timed():
    start = time()
    print("Starting time {}".format(start))
    yield # generator
    end = time() - start
    print("Execution time {0:.2f}s".format(end))

# calling our contextmanager function
with Timed():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    print("sum of the entered numbers:", a+b)
