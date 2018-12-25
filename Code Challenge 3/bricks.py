# -*- coding: utf-8 -*-
# To take input for number of bricks and target sixe[1-inch,5-inch,target]
list2 = list(map(int, input().split(' ')))


# A function to check whether target size can be achieved or not
def check_func(list_repl):
    target = list_repl[2]
    while ((list_repl[1] != 0 or list_repl[0] != 0) and target > 0):
        if (target >= 5):
            if (list_repl[1] != 0):
                target = target-5
                list_repl[1] = list_repl[1]-1
                print(target)
        else:
            if(list_repl[0] != 0):
                target = target-1
                list_repl[0] = list_repl[0]-1
                print(target)

    if (target == 0):
        print("True")
    else:
        print("False")


# function call
check_func(list2)


# input = 2 2 11
"""output:
6
1
0
True"""
