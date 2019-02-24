# -*- coding: utf-8 -*-

""" A program to demonstrate list content reversing and optimizing the reversing method of string """

# To take user name input in single command using split
name = input().split()

# to print the name string after reversing
name = name[::-1]

name = " ".join(name)

print(name)

# Input = piyush kumar
# Output = kumar piyush
