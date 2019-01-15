# -*- coding: utf-8 -*-
# Here we are using map,lambda,filter,reduce instead of traditional methods

# importing time module to check execution time
import time
from functools import reduce

start_time = time.time()

# To take input
Integer_list2 = list(map(int, input().split()))

# For adding the number
Add = reduce(lambda x, y: x+y, Integer_list2)

# For multiplying number
Multiply = reduce(lambda x, y: x*y, Integer_list2)

# To find maximum and minimum
Largest = max(map(lambda x: x, Integer_list2))
Smallest = min(map(lambda x: x, Integer_list2))

# For sorting the collection
Sorted = sorted(map(lambda x: x, Integer_list2))


# For removing duplicates

Filtered = list(set(Sorted))


# Function to print the values
def Print():
    print("SUM =", Add)
    print("PRODUCT =", Multiply)
    print("LARGEST_VALUE =", Largest)
    print("SMALLEST_VALUE =", Smallest)
    print("SORTED_LIST =", Sorted)
    print("FILTERED_LIST =", Filtered)


# To print the values
Print()
print("Exceution time--------%s seconds-------" % (time.time() - start_time))
