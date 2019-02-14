# -*- coding: utf-8 -*-
""" A program"""

import glob
import pandas as pd
df = pd.DataFrame()
list_of_files = glob.glob('./*.txt')
for var in range(0, len(list_of_files)):
    with open(list_of_files[var],"r") as fileobj:
        words = fileobj.read().splitlines()
    for var2 in range(1880, 2011):
        df[var2] = pd.Series(words)