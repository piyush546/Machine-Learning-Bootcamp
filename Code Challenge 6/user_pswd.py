# -*- coding: utf-8 -*-
# To import collections for ordered dictionary
from collections import OrderedDict

with open("sample.txt", "r") as fileobj:
    list1 = fileobj.read().splitlines()

data_dict = {}


# defining a function for username and id finding
def user_id(data):
    if len(data) >= 3:
        data_dict[data[0]] = data[2]
    else:
        pass


# Function calling loop
for var in range(0, len(list1)):
    # to handle the comments
    if str(list1[var]).startswith("#"):
        pass
    else:
        dict_list = list1[var].split(":")
        user_id(dict_list)  # function call

# sorting the list alphabetically
data_dict = OrderedDict(sorted(data_dict.items(), key=lambda x: x[0]))

# Printing the values
for k, v in data_dict.items():
    print("Username:%s, password:%s" % (k, v))
