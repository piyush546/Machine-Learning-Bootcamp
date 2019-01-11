# -*- coding: utf-8 -*-
# To take input for number of bricks and target sixe[1-inch,5-inch,target]
list2 = input().split(",")


# A function to check whether target size can be achieved or not
def check_func(list_repl):
    target = int(list_repl[2])
    while ((int(list_repl[1]) != 0 or int(list_repl[0]) != 0) and target > 0):
        if (target >= 5):
            if (int(list_repl[1]) != 0):
                target = target-5
                list_repl[1] = int(list_repl[1])-1
        else:
            if(int(list_repl[0]) != 0):
                target = target-1
                list_repl[0] = int(list_repl[0])-1

    if (target == 0):
        return "True"
    else:
        return "False"


# function call
print(check_func(list2))


# input = 2 2 11
"""output:
True"""

