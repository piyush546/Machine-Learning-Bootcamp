# -*- coding: utf-8 -*-

# to take multiple values for list
int_list = input().split(' ')

# a variable for verifying existence of pallindromic integer
c = 0

# Checking for pallindromic integer
for i in range(0, len(int_list)):
    if(int_list[i][::-1] == int_list[i]):
        c = c+1
        int_list[i] = int(int_list[i])
    else:
        int_list[i] = int(int_list[i])
        continue
if(c > 0):
    print("True")
else:
    print("False")

# Input = 12 9 8 10 15
# Output = True
