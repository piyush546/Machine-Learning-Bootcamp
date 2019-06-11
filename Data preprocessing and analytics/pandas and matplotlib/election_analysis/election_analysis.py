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

seaborn.barplot(mod_data.iloc[:,1],mod_data.iloc[:,0])

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
init_notebook_mode(connected=True)
trace=go.Pie(labels=list(data["col_2"].value_counts().index),values=list(data["col_2"].value_counts()))
#bar = go.Bar(y=mod_data.iloc[:,1], x=mod_data.iloc[:,0])
#layout = go.Layout(title="parties distribution in each constituency",autosize=False, width=1000, height=600)
#fig = go.Figure(data=[trace], layout=layout)
#plot(fig)
plot([trace])
#iplot([trace])

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



data = new_mod_data.reset_index()
seats = data["State"]
data[["State","Party"]] = data["index"].str.split(",", expand=True)
data["index"] = seats
data.columns = ["seats", "state","party"]
data = data.sort_values("seats").drop_duplicates(["state"], keep="last")
data.index =  [x for x in range(0, 36)]
states = data["state"].tolist()

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
data['region'] = data['state'].map(mod)

data = data.sort_values("region")

pie = {'data':[{
        'labels':data["party"][data["region"]=="North"],
        'values':data["seats"][data["region"]=="North"],
        "text":["Election"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "Party Trend",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"},
    {
        'labels':data["party"][data["region"]=="East"],
        'values':data["seats"][data["region"]=="East"],
        "text":["Election"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "Party Trend",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"},
     {
        'labels':data["party"][data["region"]=="west"],
        'values':data["seats"][data["region"]=="west"],
        "text":["Election"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "Party Trend",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"},
      {
        'labels':data["party"][data["region"]=="South"],
        'values':data["seats"][data["region"]=="South"],
        "text":["Election"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "Party Trend",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"},
       {
        'labels':data["party"][data["region"]=="Central"],
        'values':data["seats"][data["region"]=="Central"],
        "text":["Election"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "Party Trend",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"},
        {
        'labels':data["party"][data["region"]=="north_east"],
        'values':data["seats"][data["region"]=="north_east"],
      "text":["Election"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "Party Trend",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"}],
        "layout": {
        "title":"Lok sabaha election 2019",
        "grid": {"rows": 1, "columns": 2},
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "GHG",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Parties",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }}
plot(pie)