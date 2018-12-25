# -*- coding: utf-8 -*-

# To take user name input in single command using split
first_name, last_name = input().split(" ")

# to print the name string after reversing
full_name = first_name+" "+last_name
j = full_name.index(" ")
print(full_name[j+1:len(full_name)+1]+full_name[j]+full_name[0:j])

# Input = piyush kumar
# Output = kumar piyush
