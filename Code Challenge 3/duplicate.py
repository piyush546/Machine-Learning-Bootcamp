# -*- coding: utf-8 -*-

# list containing the integers
list4 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

# A method to eliminate duplicate values
# list containing the unique element
unique_list = []

for i in range(0, len(list4)):
    if list4[i] not in unique_list:
        unique_list.append(list4[i])
    else:
        continue

# List after removing the duplicate elements
list4 = unique_list
print(list4)
# output = [12, 24, 35, 88, 120, 155]
