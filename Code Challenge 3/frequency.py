# -*- coding: utf-8 -*-

# to import module to sort dictionary or arrange according particular order
from collections import OrderedDict

# to take the input
String_value = input()

# defining the dictionary to count the occurence of a character
dict_value = {}

# Checking the frequency
for var in String_value:
    if var.isalpha() is True:
        if var not in dict_value.keys():
            dict_value[var] = 1
        else:
            dict_value[var] += 1

# Sorting the dictionary
dict_value = dict(OrderedDict(sorted(dict_value.items(), key=(lambda x: x[1]))))

# printing the dictionary
print("Frequency of the characters:", dict_value)
