# -*- coding: utf-8 -*-

""" A program to build checker pattern """

# variables to store asterisk unicode
Star = "\u002A"


# to print the checker pattern
def main(input_char):
    columns = int(input("columns required:"))
    rows = int(input("rows required:"))
    for i in range(0, rows):
            if (i % 2) == 0:
                print((input_char+"_")*columns)
            else:
                print("_"+(input_char+"_")*columns)


# Function calling
main(Star)
