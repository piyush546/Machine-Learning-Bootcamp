# -*- coding: utf-8 -*-

import re

n = int(input("Enter the number of lines to be inputed:"))
List = []
# provide input
for i in range(0, n):
    var1 = input()
    List.append(var1)

# Required pattern
regex = re.compile("^[456]([0-9]{15}|[0-9]{3}-([0-9]{4}-?){3})")

# processing the result
for var in range(0, len(List)):
    result = regex.match(List[var])
    if result:
        if not(re.search(r"(\d)\1{3,}", List[var])):
            print("valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

"""
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367 -8912-3456
5123 - 3567 - 8912 - 3456
    
Valid
Valid
Invalid
Valid
Invalid
Invalid
"""