# -*- coding: utf-8 -*-

"""
In this program we validate an atm card number.
We used here the grouping concept here.
(\d) - represent a group which contains one digit
\1 - calls the first group of the regex pattern
(\d)\1{3,} - this is the first grp of the regex pattern, and it searches for 
a digit which is in reptition for 4 or more times.
"""
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
Input-
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367 -8912-3456
5123 - 3567 - 8912 - 3456


Output-    
Valid
Valid
Invalid
Valid
Invalid
Invalid
"""




