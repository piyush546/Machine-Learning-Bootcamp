# -*- coding: utf-8 -*-
""" A program to read the collections of text files, fetch data from them,
frame csv for them according to particular year that is included in their
names (Given year range - 1880 to 2010)  """

""" There are two modules to read the files present in a folder - they are
os and glob. glob basically uses unix stylling but os have omnipresence means
it has presence worldwide """

# Importing os module for getting the list of files
import os

# Importing pandas for framing datasets
import pandas as pd
import numpy as np
# Exception handling for the Dataframe exceptions
try:
    # Initializing the parent dataframe
    ssa_dataframe = pd.DataFrame()

    # For specifying the column names with year to store data related to that
    # year
    count = 1880

    # A list containing dataframes for different years data
    dataframe_list = []

    # To fetch list of text files from where the datas are to be fetched
    # And applying the file handling techniques on them
    for file_name in os.listdir("./textfiles"):

        # As data is required till 2010
        if count > 2010:
            break

        else:
            with open("./textfiles/"+file_name, "r") as fileobj:

                # Initializing the names of the dataframes
                data_set = "data_frame"+str(count)

                # Framing the dataframes according to specific year
                # columns parameter specify the name of the coulumn in the dataframe
                # column_name can be some kind of collections type not str or integer type
                data_set = pd.DataFrame(fileobj.read().splitlines(), columns=[count])

                # Appending the dataframes in dataframe_list
                dataframe_list.append(data_set)

        count = count+1
    ssa_dataframe = pd.concat(dataframe_list, axis=1)

except TypeError as e:
    print(e)

except ValueError as e:
    print(e)

# ************************************************* #
# Fetching top 5 males and Females baby names

# Fetching 2010 records in a variable data_2010 with filtering it
# and droping the null value containing rows
# Series.str.split(delimeter,n,expand) - Split strings around given separator/delimiter.
# .add_prefix(str) add labels to the dataframe. I used it to name the column by lable col_
data_set = data_set[2010].str.split(",", expand=True).add_prefix('col_')

# pandas.DataFrame.apply(funcn) - to apply function on dataframe
# I used it here to apply int function on a column containing numeral values
# but in str format. Using this I converted the type from str to int
data_set.iloc[:, -1] = data_set.iloc[:, -1].apply(int)

# Sorting the female data accprding to counts using sort_values() method
# giving false to ascending parameter in sort_values sorts the data in descending order
# .head() fetch 5 values from the start of the dataframe
# Female_data the top 5 female baby names
Female_data = data_set[data_set['col_1'] == 'F'].sort_values('col_2',ascending=False).head()

# Top % male baby names
Male_data = data_set[data_set['col_1'] == 'M'].sort_values('col_2',ascending=False).head()
