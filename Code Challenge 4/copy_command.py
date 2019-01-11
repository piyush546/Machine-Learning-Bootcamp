# -*- coding: utf-8 -*-

import time
start_time = time.time()

# To open a file for reading
File = open("romeo.txt", "r")

# To read all the Lines of the file
List1 = File.readlines()


# function to count occurence of each word
def count1(String1):
    String1 = String1.replace(" ", "")
    String1 = str.lower(String1)
    List2 = list(String1)
    if List2[-1] == '\n':
        List2.remove('\n')
    Unique_list = []
    for var in range(0, len(List2)):
        if List2[var] not in Unique_list:
            Unique_list.append(List2[var])
        else:
            continue
    Unique_list2 = []
    d = 0
    for var2 in range(0, len(Unique_list)):
        d = List2.count(Unique_list[var2])
        Unique_list2.append(d)
    Dictionary = dict(zip(Unique_list, Unique_list2))
    print(Dictionary)


# To call the function
for var3 in range(0, len(List1)):
    count1(List1[var3])

# To close the file
File.close()
print("--- %s seconds ---" % (time.time() - start_time))
