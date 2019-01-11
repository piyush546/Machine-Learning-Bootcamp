# -*- coding: utf-8 -*-

import re

n = int(input("Enter the number of lines to be inputed:"))
List = []
# provide input
for i in range(0, n):
    var1 = input()
    List.append(var1)

# Required pattern
regex = re.compile("^[456][0-9]{15}|^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}")

# processing the result
for var in range(0, len(List)):
    result = regex.match(List[var])
    if result is None:
        print("Invalid")
    else:
        print("Valid")
