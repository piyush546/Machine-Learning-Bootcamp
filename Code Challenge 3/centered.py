# -*- coding: utf-8 -*-

# To make an array of integers
items = list(map(int, input().split()))

# to sort the array
items.sort()

# to remove the smallest and the largest element from the array
items.remove(items[0])
items.remove(items[-1])

# to hold the sum of the array elements
# sum is used to sum up the numeral list and guve the sum of all the numeral value
sum2 = sum(items)
"""for i in range(0, len(items)):
    sum2 = sum2 + items[i]"""

# Centered average value
centered_average = sum2//len(items)
print(centered_average)
# input = 1 2 3 4 10
# output = 3
