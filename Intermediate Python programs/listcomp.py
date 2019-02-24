# -*- coding: utf-8 -*-

# Taking input
word = input()

# Defining the vowels characters with space
v = "aeiou "

# List comprehension
words_list1 = [i if i.lower() in v else i+'o'+i for i in word]

# printing the translated word
print("Translated word:", "".join(words_list1))
