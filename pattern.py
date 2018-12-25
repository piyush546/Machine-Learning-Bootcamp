# -*- coding: utf-8 -*-
# To take the column range from user
columns = int(input())

# Printing the pattern
for i in range(1, columns+1):
    print("*"*i)
for j in range(columns-1, 0,-1):
    print("*"*j)
