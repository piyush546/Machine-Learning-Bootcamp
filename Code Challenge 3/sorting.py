# -*- coding: utf-8 -*-

# used to label field for sorting - eg-list.sort(key = itemgetter(1))
# from operator import itemgetter
# amount of data to be entered
n = int(input())

# listto hold the details
details_list = []

# To take input
for i in range(0, n):
    list_input = input().split(" ")
    # to hold the name
    name = ''.join(list_input[:-2])
    age = int(list_input[-2])
    height = int(list_input[-1])
    details_list.append((name, age, height))

# list after sorting
details_list = details_list.sort()

print(details_list)
