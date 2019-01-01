# -*- coding: utf-8 -*-

import re

n = int(input("Enter the number of lines to be inputed:"))
Email_id = []
# provide input
for i in range(0, n):
    var1 = input()
    Email_id.append(var1)

# required Pattern
regex = re.compile("[-_a-zA-Z0-9]+@[a-zA-Z0-9]+[a-zA-Z]{2,4}")

# List to hold valid email id
valid_email = []

# Finding the valid email
for var in range(0, len(Email_id)):
    result = regex.match(Email_id[var])
    if result is None:
        continue
    else:
        valid_email.append(Email_id[var])

# To print the list of valid email
valid_email.sort()
print(valid_email)
