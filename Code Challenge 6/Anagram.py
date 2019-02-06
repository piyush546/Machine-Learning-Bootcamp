# -*- coding: utf-8 -*-

""" A Program to find the anagram words from a file """
# Importing collections
from collections import OrderedDict

# importing itertools.groupby
# Itertools is used to handle iterators operation fastly
from itertools import groupby

# To get execution time imported time module
import time

# Defined the start time of the program
start_time = time.time()

try:
    # Opening the file anagram.txt to get the words
    with open("anagram.txt") as fileobj:
        words = fileobj.read().splitlines()

except FileNotFoundError as e:
    print(e)

# *************************************************** #
# Processing to find anagram words

# Step 1 - dividing the large file into small sub files
# Finding the len of the words and storing it in the words_len
words_len = list(map(len, words))

# Framimg a dictionary containing the words as keys and len as their values
final_word_dict = dict(zip(words, words_len))

# Sorting the dictionary according to length
final_word_dict = dict(OrderedDict(sorted(final_word_dict.items(),key=lambda x: x[1])))

# Storing the unique lenght from the dictionary
unique_len = set(final_word_dict.values())

# Modified word list
modified_word_list = []

# Used as index for modified_word_list in for loop
count = 0

# dividing the dictionary on the basis of length
for var in unique_len:
    modified_word_list.append([])
    for k, v in final_word_dict.items():
        if v == var:
            modified_word_list[count].append(k)
    count += 1

# Step2 - to find anagram words from modified list
# set to hold anagram words
anagram_words = []


# Function to filter anagram words
anagram_filter = lambda w: sorted(w)

# applying loop and groupby functions going to seperate anagrams and non-anagrams words
for var2 in modified_word_list:
    anagram_words.extend([list(v) for k, v in groupby(sorted(var2, key=anagram_filter), anagram_filter)])

# Extracting the anagrams words by list comphrehension
anagram_words = [x for lis in anagram_words if len(lis) > 1 for x in lis]

# To get the final execution time
print(time.time() - start_time)
