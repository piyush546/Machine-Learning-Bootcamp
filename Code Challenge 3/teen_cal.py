# -*- coding: utf-8 -*-

# Inputed dictionary
n = int(input("Number of data to be inserted:"))
dictionary = dict(input().split() for _ in range(n))


# function to sum up the items of dictionary
def sum_item(dictionary1):
    # variable for sum
    sum1 = 0
    # variable to hold items
    item_list = list(dictionary1.values())
    for i in range(0, len(item_list)):
        if int(item_list[i]) in range(13, 20):
            if int(item_list[i]) == 15 or int(item_list[i]) == 16:
                sum1 = sum1 + int(item_list[i])
            else:
                sum1 = sum1 + 0
        else:
            sum1 = sum1 + int(item_list[i])
    return sum1


# printing the sum of items
print("Sum =", sum_item(dictionary))
