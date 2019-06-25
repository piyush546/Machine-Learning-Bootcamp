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


