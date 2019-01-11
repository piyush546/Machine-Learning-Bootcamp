# -*- coding: utf-8 -*-

# Variable to store the name of the file
Filename = input("Enter the name of the file:")

# To open the file for writing
File = open(Filename, "w")

# Input for writing in file
Input = input().split()

for i in range(0, (len(Input)-1)):
    Input[i] = Input[i]+"\n"

# To write data in the file
File.writelines(Input)

# Closing the file
File.close()

# To read the file
File2 = open(Filename, 'r')

last_line = File2.readlines()

print(last_line[-1])

File2.close()
