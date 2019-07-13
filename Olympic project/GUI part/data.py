# -*- coding: utf-8 -*-
def data_mod():
    import pandas as pd
    # import numpy as np
    data = pd.read_csv("olym_data.csv")
    data = data.fillna(data.median())
    return data

def years(Season):
    data = data_mod()
    unique_years = data.Year[data["Season"]==Season].unique()
    return unique_years

def result(S, y):
    data = data_mod()
    result = data[(data["Season"]==S) &(data["Year"]==y)]
    result = result.groupby("NOC")["Medal"].value_counts().unstack()
    result = result.iloc[:[1,2,0]]
    result = result.fillna(0)
    result["Total"] = result.apply(lambda x: sum(x), axis=1)
    result = result.sort_values("Gold")
    return result