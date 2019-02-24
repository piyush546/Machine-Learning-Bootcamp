# -*- coding: utf-8 -*-

""" A program to check whether the target dimensions can be achieved using given number of bricks """


# User defined Exception class for handling wrong input for target like 0
class WrongInputException(Exception):
    def __init__(self):
        self.message = "Please provide a valid dimension as target"


# Exception handling block
try:

    # To take input for number of bricks and target following the sequence[1-inch,5-inch,target]
    bricks_data = input().split()
    # To convert the input into integers as they are in str format
    bricks_data = [int(x) for x in bricks_data]

    # Raising the Exception if target inputted is 0
    if bricks_data[-1] == 0:
        raise WrongInputException

except WrongInputException as e:
    print(e.message)

else:
    # A function to check whether target size can be achieved or not
    def check_func(data):
        target = data[-1]
        count_5 = data[1]
        count_1 = data[0]
        while((count_5 != 0 and count_1 != 0) or target != 0):
            if target >= 5:
                target = target-5
                count_5 -= 1
            else:
                target = target-1
                count_1 -= 1
        if target == 0:
            return True
        else:
            return False

    # function call
    print(check_func(bricks_data))


# input = 2 2 11
# output: True
