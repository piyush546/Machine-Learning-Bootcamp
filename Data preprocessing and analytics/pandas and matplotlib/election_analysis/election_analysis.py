# -*- coding: utf-8 -*-
"""
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country

"""

# Data preprocessing and visualization modules
import pandas as pd
# import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Plotly module for better visualization
from plotly.offline import init_notebook_mode, plot #, iplot, download_plotlyjs
import plotly.graph_objs as go
init_notebook_mode(connected=True)

# Loading the data
dataset = pd.read_csv("election.csv")

# Selecting the important features for further processing
dataset = dataset.loc[:,['Candidate', 'Party','State', 'Constituency', 'Total Votes', '%']]

# State -> Constituency -> Top parties with their vote percentage
state_con_data = dataset.sort_values("%").drop_duplicates(["State","Constituency"], keep="last")
state_con_data = state_con_data.sort_values("State")
state_con_data = state_con_data.iloc[:,[2,3,1,5]]
state_con_data["State"] = (state_con_data["State"]+","+state_con_data["Constituency"]+","+state_con_data["Party"])
state_con_data.index = [x for x in range(0,542)]
state_con_data = state_con_data.iloc[:,[0,-1]]

# Visualization of Rajasthan state constituency
sns.barplot(state_con_data.iloc[332:356,0],state_con_data.iloc[332:356,1])
plt.xticks(rotation=90)
plt.title("Rajasthan consitutency wise party win %")
plt.xlabel("State,Constituency,party")
plt.ylabel("vote %")
plt.grid(True)
plt.show()

"""
bar = go.Bar(y=state_con_data.iloc[:,1], x=state_con_data.iloc[:,0])
layout = go.Layout(title="parties distribution in each constituency",autosize=False, width=1000, height=600)
fig = go.Figure(data=[bar], layout=layout)
plot(fig)
"""

# State -> party seat count
state_party_data = dataset.sort_values("%").drop_duplicates(["State","Constituency"], keep="last")
state_party_data.index = [x for x in range(0,542)]
state_party_data["State"] = state_party_data["State"]+","+state_party_data["Party"]
state_party_data = state_party_data["State"]
state_party_data = state_party_data.value_counts()

# Visualizing the parties in each state with their seats won
plt.figure(figsize=(4,30))
sns.barplot(state_party_data, state_party_data.index)
plt.title("Top Parties in Each state")
plt.xlabel("No.of seats won")
plt.ylabel("state and party")
plt.grid(True)
plt.show()


# Visualizations of total seats won by each party in whole country
total_seats = state_con_data['State'].str.split(",", expand=True).add_prefix("col_")
trace=go.Pie(labels=list(total_seats["col_2"].value_counts().index),values=list(total_seats["col_2"].value_counts()))
plot([trace])
#iplot([trace])

# Fetching the States on basis of directions to show region wise trend of parties win
north = ['Jammu & Kashmir', 'Himachal Pradesh', 'Punjab', 'Uttarakhand' , 'Uttar Pradesh',
         'Haryana', 'Chandigarh','NCT OF Delhi']
east  = [ 'Bihar', 'Odisha', 'Jharkhand', 'West Bengal']
west = ['Rajasthan' , 'Gujarat', 'Goa', 'Maharashtra', 'Dadra & Nagar Haveli',
        'Daman & Diu'] 
south = ['Andhra Pradesh', 'Karnataka','Puducherry','Telangana','Kerala',
         'Tamil Nadu', 'Andaman & Nicobar Islands', 'Lakshadweep']
central = ['Madhya Pradesh','Chhattisgarh']
north_east = ['Assam', 'Sikkim', 'Nagaland', 'Meghalaya', 'Manipur', 'Mizoram', 
              'Tripura', 'Arunachal Pradesh']



region_wise_trend = state_party_data.reset_index()
seats = region_wise_trend["State"]
region_wise_trend[["State","Party"]] = region_wise_trend["index"].str.split(",", expand=True)
region_wise_trend["index"] = seats
region_wise_trend.columns = ["seats", "state","party"]
region_wise_trend = region_wise_trend.sort_values("seats").drop_duplicates(["state"], keep="last")
region_wise_trend.index =  [x for x in range(0, 36)]
states = region_wise_trend["state"].tolist()

def mod(var):
    if var in north:
        return "North"
    elif var in east:
        return "East"
    elif var in south:
        return "South"
    elif var in central:
        return "Central"
    elif var in west:
        return "west"
    elif var in north_east:
        return "north_east"
    else:
        return "missing"
region_wise_trend['region'] = region_wise_trend['state'].map(mod)
"""
region_wise_trend = region_wise_trend.sort_values("region")
sns.barplot(region_wise_trend["party"][region_wise_trend["region"]=="North"], region_wise_trend["seats"])
sns.barplot(region_wise_trend["party"][region_wise_trend["region"]=="East"], region_wise_trend["seats"])
plt.xticks(rotation=90)
"""
# data = region_wise_trend["party"][region_wise_trend["region"]  == "North"].values.tolist()
