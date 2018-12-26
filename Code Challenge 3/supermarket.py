# -*- coding: utf-8 -*-
# numbers of item purchased
n = int(input())

# list to hold the item_name and quantity
details_list = []

# a list to sum up the qunatity of each unique item
unique_list1 = []

# To take input
for i in range(0, n):
    list_item = input().split(" ")
    # to hold the name of the item
    item_name = " ".join(list_item[:-1])
    # to hold item quantity
    quantity = int(list_item[-1])
    # To append the item_name and quantity in the detail_list
    details_list.append([item_name, quantity])
    # to append the item with 0 count in unique_list1
    unique_list1.append([details_list[i][0], 0])

# to count the total quantity of each unique item
for j in range(0, len(unique_list1)):
    for k in range(0, len(details_list)):
        if unique_list1[j][:-1] == details_list[k][:-1]:
            unique_list1[j][-1] += details_list[k][-1]
        else:
            continue

# To remove the duplicated data
unique_list2 = []
for m in range(0, len(unique_list1)):
    if unique_list1[m][:-1] not in unique_list2:
        print(unique_list1[m][0]+" "+str(unique_list1[m][-1]))
        unique_list2.append(unique_list1[m][:-1])
    else:
        continue
"""input:9

banana fries 30

apple juice 10

candy 5

potato chips 20

apple juice 10

banana fries 30

candy 5

candy 5

candy 5"""

"""output:banana fries 60
apple juice 20
candy 20
potato chips 20"""

