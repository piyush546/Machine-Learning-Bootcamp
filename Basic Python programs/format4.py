# -*- coding: utf-8 -*-

""" A program to reverse the position of user name and surname using slicing"""

# To take two string in one single input command
first_name, last_name = input().split(" ")

# To store both the name using a single variable
full_name = first_name+last_name

# process to reverse the string
var = len(first_name)
var1 = len(last_name)

# to print the reversed string
print(full_name[var:(var+var1)]+" "+full_name[0:var])

# Input = piyush kumar
# Output = kumar piyush

# Alternative and optimization of above program
# Using list and join property
"""name = input().split()
name = name[::-1]
name = " ".join(name)
"""
