# -*- coding: utf-8 -*-

# To import time module for duration and time related activity
import time
start_time = time.time()


# To open a file for reading
File = open("romeo.txt", "r")

# To read all the Lines of the file
List1 = File.readlines()


# function to count occurence of each word
def count1(String1):
    String1 = str.lower(String1)
    List2 = []
    for var1 in range(0, len(String1)):
        if String1[var1].isalpha() is True:
            List2.append((String1[var1], 0))
        else:
            continue
    Dict1 = dict(List2)
    for k, v in Dict1.items():
        for var2 in range(0, len(List2)):
            if k == List2[var2][0]:
                Dict1[k] += 1
            else:
                continue
    print(Dict1)


# To call the function
for var3 in range(0, len(List1)):
    count1(List1[var3])

# To close the file
File.close()

# To check exeution time of the code
print("--- %s seconds ---" % (time.time() - start_time))
