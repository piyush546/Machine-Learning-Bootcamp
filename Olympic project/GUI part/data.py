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