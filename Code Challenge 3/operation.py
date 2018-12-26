# -*- coding: utf-8 -*-
# To take inputs for a list
Integer_list = list(map(int, input().split(",")))


# Function for addition of the list element
def Add(list1):
    sum_result = 0
    for i in range(0, len(list1)):
        sum_result = sum_result + list1[i]
    return sum_result


# Function for  multiplying
def Multiply(list2):
    mul_result = 1
    for j in range(0, len(list2)):
        mul_result = mul_result * list2[j]
    return mul_result


# Function to find the largest element
def Largest(list3):
    result = max(list3)
    return result


# Function to find the smallest element
def Smallest(list3):
    result1 = min(list3)
    return result1


# Function to sort elements
def Sorting(list4):
    result2 = sorted(list4)
    return result2


# Function to remove the duplicates
def Remove_duplicates(list5):
    unique_list = []
    for k in range(0, len(list5)):
        if list5[k] not in unique_list:
            unique_list.append(list5[k])
        else:
            continue
    unique_list = sorted(unique_list)
    return unique_list


# Function for printing the values
def Print(list7):
    print("Sum = ", Add(list7))
    print("Multiply = ", Multiply(list7))
    print("Largest = ", Largest(list7))
    print("Smallest = ", Smallest(list7))
    print("Sorted = ", Sorting(list7))
    print("Without Duplicates = ", Remove_duplicates(list7))


# Function call to print values
Print(Integer_list)

# input = 2,5,6,8,7,2,1,8
"""output:
Sum =  39
Multiply =  53760
Largest =  8
Smallest =  1
Sorted =  [1, 2, 2, 5, 6, 7, 8, 8]
Withou Duplicates =  [1, 2, 5, 6, 7, 8]"""

