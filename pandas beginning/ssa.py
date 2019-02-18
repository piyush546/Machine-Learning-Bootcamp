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


# A function to clean data and synchronize it in a structured way
def data_cleansing(unst_lst):
    st_lst = []
    for var in unst_lst:
        st_lst.append(var.split())
    return st_lst


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
                data_set = pd.DataFrame(fileobj.readlines(), columns=[count])

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

# Initializing a list to hold the data of 2010 named column as the data is in
# string format and we have to find the maximum count of males and female

