# -*- coding: utf-8 -*-
# The hardcoded string
string  = "RESTART"

# replacing the characters
string = string.replace("R","$")
string = string.replace("$","R",1)

# printing the new string
print(string)
