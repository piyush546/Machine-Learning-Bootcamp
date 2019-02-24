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

# Importing numpy for some mathematical calculations
import numpy as np

# Importing matplotlib for pictorial representation of data and records
import matplotlib.pyplot as plt


# Defining a function for performing various calculations on the dataframes column
def frames_filter(dataframe_col,year_repl):

    # Removing the null values from the DataFrames as null values will generate error while we use .apply(int) method
    # Typecasting is required to convert the series to dataframe for applying the further operations
    dataframe_col = pd.DataFrame(dataframe_col[year_repl].dropna())

    # Fetching top 5 males and Females baby names

    # and droping the null value containing rows
    # Series.str.split(delimeter,n,expand) - Split strings around given separator/delimiter.
    # .add_prefix(str) add labels to the dataframe. I used it to name the column by lable col_
    dataframe_col_re= dataframe_col[year_repl].str.split(",", expand=True).add_prefix("col_")

    # pandas.DataFrame.apply(funcn) - to apply function on dataframe
    # I used it here to apply int function on a column containing numeral values
    # but in str format. Using this I converted the type from str to int
    dataframe_col_re.iloc[:, -1] = dataframe_col_re.iloc[:, -1].apply(int)

    # Sorting the female data according to counts using sort_values() method
    # giving false to ascending parameter in sort_values sorts the data in descending order
    # .head() fetch 5 values from the start of the dataframe
    # Female_data the top 5 female baby names
    female_data = dataframe_col_re[dataframe_col_re['col_1']=="F"].sort_values('col_2', ascending=False).head()

    # Top 5 male baby names
    male_data = dataframe_col_re[dataframe_col_re['col_1']=="M"].sort_values('col_2', ascending=False).head()

    # Sum accounting the total_numbers of babies
    sum_year = dataframe_col_re['col_2'].sum()

    # Sum accounting to male and female babies counts
    gender_sum = pd.pivot_table(dataframe_col_re,values=['col_2'], columns=['col_1'], aggfunc=np.sum)

    # Plotting the pictorial pie chart for the sum of counts for whole and accoridng to gender
    plt.pie([gender_sum['F'], gender_sum['M']], explode=[0, 0], labels=['female','male'], autopct="%1.1f%%")

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis("equal")

    # For displaying the plotted pie chart
    return plt.show()
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

    # Function call to analyze the fetched data
    frames_filter(ssa_dataframe, 2010)

except TypeError as e:
    print(e)

except ValueError as e:
    print(e)

except AttributeError as e:
    print(e)
