# -*- coding: utf-8 -*-

# Input list
Item_list = list(map(int, input().split(",")))

# Processing the list for the sum
sum3 = 0
d = 0
for i in range(0, len(Item_list)):
    if Item_list[i] == 13:
        continue
    elif Item_list[i-1] == 13:
        continue
    else:
        sum3 = sum3+Item_list[i]
print(sum3)
# Input = 13,5,8,13,9,10,13,12,18
# Output = 36
