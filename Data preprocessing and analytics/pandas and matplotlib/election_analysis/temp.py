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
from plotly.offline import init_notebook_mode, plot
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
