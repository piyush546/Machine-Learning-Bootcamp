# -*- coding: utf-8 -*-

# to import module to sort dictionary or arrange according particular order
from collections import OrderedDict

# to take the input
String_list = list(input())

# values to contain the occurence of each character
values = []

for i in String_list:
    count = String_list.count(i)
    values.append(count)

# Required dictionary
dictionary3 = dict(zip(String_list, values))

dictionary3 = dict(OrderedDict(sorted(dictionary3.items(), key=lambda x: x[1])))
print(dictionary3)
