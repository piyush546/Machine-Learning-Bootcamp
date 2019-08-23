# -*- coding: utf-8 -*-

import pandas as pd
#import numpy as np
train_data = pd.read_csv("Beer Train Data Set.csv")
import re
import string
def category_removal(value):
    value = value.replace("Meat",",")
    value = value.replace("General",",")
    value = value.replace("Cheese",",")
    return value

train_data["Food Paring"] = train_data["Food Paring"].map(category_removal)

def nickname_removal(value):
    regex = re.compile("\s*\w+\(")
    if regex.search(value) != None:
        value = regex.findall(value)
        return ",".join(value)
    else:
        return value

train_data["Glassware Used"] = train_data["Glassware Used"].map(nickname_removal)

def punctuators_removal(value):
    translator = str.maketrans(" "," " ,string.punctuation)
    return value.translate(translator)

train_data[["Food Paring","Glassware Used"]] = train_data[["Food Paring","Glassware Used"]].applymap(punctuators_removal)

