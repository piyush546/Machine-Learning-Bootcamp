# -*- coding: utf-8 -*-
""" A program to perform addition of two numbers with the illustration of
resource management technique """

# Importing time from time module
from time import time

# Defining a class to illustrate the resource management
class Timer():
    def __enter__(self):
        self.start = time()
        print("Starting at {}".format(self.start))

    def __exit__(self, *excp):
        self.end = time() - self.start
        print("Execution time {0:.2f}s".format(self.end))

# Calling the class and performing the addition of two numbers
with Timer():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    print("sum of the entered numbers:", a+b)

#############################################################################
""" Implementing the above program using contextlib module """

# Importing contextmanager from contextlib module
from contextlib import contextmanager

# Defining our own contextmanager instead of class
@contextmanager
def Timed():
    start = time()
    print("Starting time {}".format(start))
    yield
    end = time() - start
    print("Execution time {0:.2f}s".format(end))

# calling our contextmanager function
with Timed():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    print("sum of the entered numbers:", a+b)
