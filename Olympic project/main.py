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
noc_data = pd.read_csv("noc_regions.csv")

"""def country(value):
    return noc_data["region"][noc_data["NOC"]==value].tolist()
olym_data["Country"] = olym_data["NOC"].apply(country)
"""

# Splitting the data in the summer and winter olympics
#summer_olympic = olym_data[olym_data["Season"]=="Summer"]
#winter_olympic = olym_data[olym_data["Season"]=="Winter"]

# Most medal winning sportperson details of both season
athlete_data = pd.pivot_table(olym_data, values="Medal", index="Name", columns="Season", aggfunc=lambda x:x.count())
summer_athlete = athlete_data[athlete_data["Summer"]==athlete_data["Summer"].max()].index[0]
s_NOC_name = olym_data["NOC"][olym_data["Name"]==summer_athlete].unique()[0]
s_gender = olym_data["Sex"][olym_data["Name"]==summer_athlete].unique()[0]
s_country_name = noc_data["region"][noc_data["NOC"]==s_NOC_name].tolist()[0]
s_sports_name = olym_data["Sport"][olym_data["Name"]==summer_athlete].unique()[0]
print("Summer Olympic top athlete")
print("Name ----->", summer_athlete)
print("Gender ----->", s_gender)
print("Country ------>", s_country_name)
print("Sports -------->", s_sports_name)
print("Total medals ------>", athlete_data["Summer"].max())

winter_athlete = athlete_data[athlete_data["Winter"]==athlete_data["Winter"].max()].index[0]
w_NOC_name = olym_data["NOC"][olym_data["Name"]==winter_athlete].unique()[0]
w_gender = olym_data["Sex"][olym_data["Name"]==winter_athlete].unique()[0]
w_country_name = noc_data["region"][noc_data["NOC"]==w_NOC_name].tolist()[0]
w_sports_name = olym_data["Sport"][olym_data["Name"]==winter_athlete].unique()[0]
print("Winter Olympic top athlete")
print("Name ----->", winter_athlete)
print("Gender ----->", w_gender)
print("Country ------>", w_country_name)
print("Sports -------->", w_sports_name)
print("Total medals ------>", athlete_data["Winter"].max())

# Athlete count over years
count = olym_data.groupby("Year")["Season"].value_counts().unstack()
plt.style.use('seaborn')
plt.scatter(count.index, count["Summer"])
plt.plot(count.index, count["Summer"],"r-o")
plt.xlim(1880, 2020)
plt.ylim(0,16000)
plt.title("Summer OLympic Athelete counts over year")
plt.xlabel("Year")
plt.ylabel("Athelte Count")
plt.savefig("Summer Athelete count.jpg")

plt.style.use("seaborn")
plt.scatter(count.index, count["Winter"])
plt.plot(count.index, count["Winter"],"r-o")
plt.title("Winter OLympic Athelete counts over year")
plt.xlabel("Year")
plt.ylabel("Athelte Count")
plt.savefig("Winter Athelete count.jpg")

# Athlete count distinguished by gender over years
s_male_count = olym_data["Year"][(olym_data["Sex"]=="M")&(olym_data["Season"]=="Summer")].value_counts()
s_female_count = olym_data["Year"][(olym_data["Sex"]=="F")&(olym_data["Season"]=="Summer")].value_counts()

sns.pointplot(s_male_count.index, s_male_count, color="m")
plt.xticks(rotation=90)
plt.title("Male Athlete Summer olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Male counts")
plt.savefig("Summer olympic Male Trends.jpg")

sns.pointplot(s_female_count.index, s_female_count,color="g")
plt.xticks(rotation=90)
plt.title("Female Athlete Summer olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Female counts")
plt.savefig("Summer olympic Female Trends.jpg")


w_male_count = olym_data["Year"][(olym_data["Sex"]=="M")&(olym_data["Season"]=="Winter")].value_counts()
w_female_count = olym_data["Year"][(olym_data["Sex"]=="F")&(olym_data["Season"]=="Winter")].value_counts()

sns.pointplot(w_male_count.index, w_male_count, color="m")
plt.xticks(rotation=90)
plt.title("Male Athlete Winter olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Male counts")
plt.savefig("Winter olympic Male Trends.jpg")

sns.pointplot(w_female_count.index, w_female_count,color="g")
plt.xticks(rotation=90)
plt.title("Female Athlete Winter olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Female counts")
plt.savefig("Winter olympic Female Trends.jpg")

# Gender Distribution in both seasons
gender_distributions = olym_data.groupby("Sex")["Season"].value_counts().unstack()

plt.style.use("ggplot")
plt.pie(gender_distributions["Summer"],labels=list(gender_distributions.index), autopct="%.1f%%")
plt.title("Summer Olympics gender ratio")
plt.axis("equal")
plt.savefig("Summer olympics gender distribution.jpg")

plt.pie(gender_distributions["Winter"],labels=list(gender_distributions.index), autopct="%.1f%%")
plt.title("Winter Olympics gender ratio")
plt.axis("equal")
plt.savefig("Winter olympics gender distribution.jpg")
