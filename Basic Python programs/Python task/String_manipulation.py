# -*- coding: utf-8 -*-

"""
Challenge 15 ( loops and strings )

Write a program to count the number of words in a sentence.
The user enters a sentence.
The program responds with the number of words in the sentence.
Hint
Look for spaces and full stops in the string.
Extension
Develop a program that will
display a sentence backwards
after entered.
"""

try:
    # Variable to hold the sentence entered by user
    sentence = input("Enter your sentence here:").split()

    # For checking for the non characters value
    for var in sentence:
        if var.isalpha():
            pass
        else:
            sentence.remove(var)
    # Variable to store the entered sentence after reading it from backward
    sen_repl = " ".join(sentence)
    sen_repl = sen_repl[::-1]

    # To print the sentence after reading it from backward and the number of words in the sentence
    print("sentence from backward:", sen_repl)
    print("No. of words in the sentence:", len(sentence))




except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except AttributeError as e:
    print(e)