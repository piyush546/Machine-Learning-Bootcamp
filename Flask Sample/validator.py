# -*- coding: utf-8 -*-
def name_validator(name,age):
    
    if type(age)==float:
        return "Valid name and age"
    else:
        return "Invalid data"
import pandas as pd
dataset = pd.DataFrame()
dataset2 = pd.DataFrame()
dataset[1880] = ["Piyush,M,20"]
def mod(value):
	value = value.split(",")
	return pd.Series([value[0], value[1], value[2]])
dataset2[["Name","Gender","Age"]]=dataset[1880].apply(mod)