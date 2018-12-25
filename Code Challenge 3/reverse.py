# -*- coding: utf-8 -*-
# To take input string
String3 = input()


# Function to reverse the string
def reverse_func(Input):
    Input2 = list(Input[::-1])
    Input2 = "".join(Input2)
    print(Input2)


reverse_func(String3)