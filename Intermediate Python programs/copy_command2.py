# -*- coding: utf-8 -*-

# To import time module for duration and time related activity
import time
start_time = time.time()


# To open a file for reading
with open("romeo.txt","r") as fileobj:
    list1 = fileobj.read().splitlines()

words_list = []
for var in range(0, len(list1)):
    words_list.extend(list1[var].split())

dict1 = {}
for var2 in range(0, len(words_list)):
    if words_list[var2] in dict1:
        dict1[words_list[var2]] += 1
    else:
        dict1[words_list[var2]] = 1

print("Words in file:", dict1)

# To check exeution time of the code
print("--- %s seconds ---" % (time.time() - start_time))
