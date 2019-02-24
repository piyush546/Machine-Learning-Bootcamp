# -*- coding: utf-8 -*-

# Program to Test User defined Exception cases

# Defining a user exception class
class ValueGreater(Exception):
    def __init__(self, message):
        self.message = message

# Exception handling block
try:
    testing_value = int(input("Enter an integer:"))
    if testing_value >= 10:
        raise ValueGreater("Entered value should be single digit")

except ValueGreater as e:
    print(e.message)

else:
    print("Square of the value entered:",testing_value**2)

finally:
    print("program ended")