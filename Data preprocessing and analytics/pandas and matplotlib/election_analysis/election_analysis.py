# -*- coding: utf-8 -*-
"""
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the above result for the biggest state UP.

3. Visualize the total seats gained by each party in each states.

4. Calculate the total votes casted in each state.

"""

# Data preprocessing modules
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt


dataset = pd.read_csv("election.csv")


dataset = dataset.loc[:,['Candidate', 'Party','State', 'Constituency', 'Total Votes', '%']]


mod_data = dataset.sort_values("%").drop_duplicates(["State","Constituency"], keep="last")
mod_data = mod_data.sort_values("State")
mod_data = mod_data.iloc[:,[2,3,1,5]]
mod_data["State"] = (mod_data["State"]+","+mod_data["Constituency"]+","+mod_data["Party"])
mod_data.index = [x for x in range(0,542)]
mod_data = mod_data.iloc[:,[0,-1]]


seaborn.barplot(mod_data.iloc[83:93,1],mod_data.iloc[83:93,0])

new_mod_data = dataset.sort_values("%").drop_duplicates(["State","Constituency"], keep="last")
new_mod_data.index = [x for x in range(0,542)]
new_mod_data["State"] = new_mod_data["State"]+","+new_mod_data["Party"]
new_mod_data = new_mod_data["State"]
new_mod_data = new_mod_data.value_counts()

plt.figure(figsize=(4,30))
seaborn.barplot(new_mod_data, new_mod_data.index)
plt.xlabel("No.of seats")
plt.ylabel("state and party")
plt.show()
data = mod_data['State'].str.split(",", expand=True).add_prefix("col_")


#% matplotlib.inline
from plotly.offline import init_notebook_mode, plot #, iplot, download_plotlyjs
import plotly.graph_objs as go
plt.figure(figsize=(30,30))
init_notebook_mode(connected=True)
trace=go.Pie(labels=list(data["col_2"].value_counts().index),values=list(data["col_2"].value_counts()))
plot([trace])
#iplot({trace})
"""
north = ['Jammu & Kashmir', 'Himachal Pradesh', 'Punjab', 'Uttarakhand' , 'Uttar Pradesh', 'Haryana']
east  = [ 'Bihar', 'Orissa', 'Jharkhand', 'West Bengal']
west = ['Rajasthan' , 'Gujarat', 'Goa', 'Maharashtra'] 
south = ['Andhra Pradesh', 'Karnataka', 'Kerala','Tamil Nadu']
central = ['Madhya Pradesh','Chhattisgarh']
north east = ['Assam', 'Sikkim', 'Nagaland', 'Meghalaya', 'Manipur', 'Mizoram', 'Tripura', 'Arunachal Pradesh']
"""