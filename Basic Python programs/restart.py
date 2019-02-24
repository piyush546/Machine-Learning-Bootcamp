# -*- coding: utf-8 -*-

""" A program to use replace method for some particular occurence of a chararcter"""

# The String that is to be modified
string = "RESTART"

# replacing the characters with and without some particular occurence
string = string.replace("R", "$")
string = string.replace("$", "R", 1)

# printing the modified string
print(string)
