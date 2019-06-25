# This project is to describe about the various aspects of Olympic games.

# Stage 1-
# Importing the Data Preprocessing and visualization modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from plotly.offline import init_notebook_mode, plot
import plotly.graph_objs as go
init_notebook_mode(connected=True)


# Loading the olympic data
olym_data = pd.read_csv("olym_data.csv")

# Splitting the data in the summer and winter olympics
#summer_olympic = olym_data[olym_data["Season"]=="Summer"]
#winter_olympic = olym_data[olym_data["Season"]=="Winter"]

# Athelete count over years
count = olym_data.groupby("Year")["Season"].value_counts().unstack()
plt.style.use('seaborn')
plt.scatter(count.index, count["Summer"])
plt.plot(count.index, count["Summer"],"r-o")
plt.xlim(1880, 2020)
plt.ylim(0,16000)
plt.savefig("Summer Athelete count.jpg")

plt.style.use("seaborn")
plt.scatter(count.index, count["Winter"])
plt.plot(count.index, count["Winter"],"r-o")
plt.savefig("Winter Athelete count.jpg")