# -*- coding: utf-8 -*-
# To arrange the dictionary in a specific order
from collections import OrderedDict

# To take input string
Input_string = list(input())

# Variable to store count of digit and letters
digit = 0
letters = 0

Dictionary4 = {'Letters': {}, 'Digits': {}}

for i in range(0,len(Input_string)):
    if Input_string[i].isalpha() is True:
        letters = letters+1
    elif Input_string[i].isdigit() is True:
        digit = digit+1
    else:
        continue

# Assigning the count values
Dictionary4['Letters'] = letters
Dictionary4['Digits'] = digit
Dictionary4 = dict(OrderedDict(sorted(Dictionary4.items(), key=lambda x: x[1], reverse = True)))

# To print the result
for k, v in Dictionary4.items():
    print(k+" "+str(v))
