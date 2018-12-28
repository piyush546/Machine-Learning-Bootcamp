# -*- coding: utf-8 -*-

# Filename to be accessed
Filename = input()

# To open the file
File = open(Filename, 'r')

List = File.readlines()


# To count characters
def count_char(list2):
    list2 = "".join(list2)
    count = 0
    for var in range(0, len(list2)):
        if list2[var] == "\n":
            continue
        else:
            count += 1
    return count


# to count words
list4 = []


def count_words(list3):
    for var1 in range(0, len(list3)):
        list4.extend(list3[var1].split())
    return len(list4)


# To count unique words
def unique_words(list5):
    list6 = set(list4)
    return len(list6)


# Wc function
def wc(list1):
    print("Number of characters:", count_char(list1))
    print("Number of words:", count_words(list1))
    print("Number of lines:", len(list1))
    print("Number of unique words:", unique_words(list1))


# Function call for wc
wc(List)

# File closed
File.close()
# Input = romeo.txt
"""output :Number of characters: 163
Number of words: 33
Number of lines: 4
Number of unique words: 26"""