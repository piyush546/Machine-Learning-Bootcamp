# -*- coding: utf-8 -*-

# Collection module is used to alter built-in datatypes like list,dictionary,tuple etc...
# Counter counts the occurence of all the different substring in a variable
import time
from collections import Counter
start_time = time.time()

# To open a file for reading
with open("romeo.txt", "r") as fileobj:
    list1 = fileobj.read().splitlines()

# To store total words in the file
word_list = []
for var in range(0, len(list1)):
    word_list.extend(list1[var].split())

dict1 = dict(Counter(word_list))
print("Words occurence:", dict1)

print("--- %s seconds ---" % (time.time() - start_time))
