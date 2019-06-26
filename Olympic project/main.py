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
host_data = pd.read_csv("olym.csv", encoding="Windows 1252")
host_data = host_data.iloc[:,:-2]

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

plt.figure(figsize=(10,7))
plt.style.use('seaborn')
plt.scatter(count.index, count["Summer"])
plt.plot(count.index, count["Summer"],"r-o")
plt.xlim(1880, 2020)
plt.ylim(0,16000)
plt.title("Summer OLympic Athelete counts over year")
plt.xlabel("Year")
plt.ylabel("Athelte Count")
plt.savefig("Summer Athelete count.jpg")

plt.figure(figsize=(10,7))
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

plt.figure(figsize=(10,7))
sns.plt.xlim(1886, 2020)
sns.pointplot(s_male_count.index, s_male_count, color="m")
plt.xticks(rotation=90)
plt.title("Male Athlete Summer olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Male counts")
plt.savefig("Summer olympic Male Trends.jpg")

plt.figure(figsize=(10,7))
sns.pointplot(s_female_count.index, s_female_count,color="g")
plt.xticks(rotation=90)
plt.title("Female Athlete Summer olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Female counts")
plt.savefig("Summer olympic Female Trends.jpg")


w_male_count = olym_data["Year"][(olym_data["Sex"]=="M")&(olym_data["Season"]=="Winter")].value_counts()
w_female_count = olym_data["Year"][(olym_data["Sex"]=="F")&(olym_data["Season"]=="Winter")].value_counts()

plt.figure(figsize=(10,7))
sns.pointplot(w_male_count.index, w_male_count, color="m")
plt.xticks(rotation=90)
plt.title("Male Athlete Winter olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Male counts")
plt.savefig("Winter olympic Male Trends.jpg")

plt.figure(figsize=(10,7))
sns.pointplot(w_female_count.index, w_female_count,color="g")
plt.xticks(rotation=90)
plt.title("Female Athlete Winter olympic trends over year")
plt.xlabel("Year")
plt.ylabel("Female counts")
plt.savefig("Winter olympic Female Trends.jpg")

# Gender Distribution in both seasons
gender_distributions = olym_data.groupby("Sex")["Season"].value_counts().unstack()

plt.style.use("ggplot")

# Summer
# To change the background color
#fig = plt.figure()
#fig.patch.set_facecolor('black')

# To change the text color
#plt.rcParams['text.color'] = 'white'
plt.figure(figsize=(8,7))
plt.pie(gender_distributions["Summer"],labels=list(gender_distributions.index), autopct="%.1f%%")
plt.axis("equal")
# To plot the circle in the middle of pie chart to make a donut chart
my_circle=plt.Circle((0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title("Summer Olympics gender ratio")
plt.savefig("Summer olympics gender distribution.jpg")

# Winter
plt.figure(figsize=(8,7))
plt.pie(gender_distributions["Winter"],labels=list(gender_distributions.index), autopct="%.1f%%")
plt.axis("equal")
my_circle=plt.Circle((0,0), radius=0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title("Winter Olympics gender ratio")
plt.savefig("Winter olympics gender distribution.jpg")

# Countries distribution over years
countries_data = olym_data.groupby(["Year","Season"])["NOC"].apply(lambda x: len(x.unique())).unstack()

plt.figure(figsize=(10,7))
sns.barplot(countries_data.index, countries_data["Summer"])
plt.xticks(rotation=90)
plt.title("Countries participation over years in Summer olympics")
plt.xlabel("Year")
plt.ylabel("Countries count")
plt.savefig("Summer Olympics countries distribution.jpg")

plt.figure(figsize=(10,7))
sns.barplot(countries_data.index, countries_data["Winter"])
plt.xticks(rotation=90)
plt.title("Countries participation over years in Winter olympics")
plt.xlabel("Year")
plt.ylabel("Countries count")
plt.savefig("Winter Olympics countries distribution.jpg")

# Nation-wise Highest participation
nation_data = olym_data.groupby(["Season","NOC"])["Year"].apply(lambda x : len(x.unique())).reset_index()
nation_data.columns = ["Season", "NOC", "Count"]
summer_nation = nation_data[nation_data["Season"]=="Summer"]
summer_nation = summer_nation.sort_values("Count")
winter_nation = nation_data[nation_data["Season"]=="Winter"]
winter_nation = winter_nation.sort_values("Count")

plt.figure(figsize=(10,7))
sns.barplot(summer_nation.NOC.tail(20), summer_nation.Count.tail(20))
plt.xticks(rotation=90)
plt.title("Summer olympics nation wise highest participation")
plt.savefig("Summer olympics nation_wise.jpg")

plt.figure(figsize=(10,7))
sns.barplot(winter_nation.NOC.tail(20), winter_nation.Count.tail(20))
plt.xticks(rotation=90)
plt.title("Winter olympics nation wise highest participation")
plt.savefig("Winter olympics nation_wise.jpg")

# Highest hosting country
def mod_data(var):
    value = list(var)
    if value[2] is not np.nan:
        return "Summer"
    elif value[3] is not np.nan:
        return "Winter"
    else:
        return "Missing"
host_data["Season"] = host_data.apply(mod_data, axis=1)
summer_country = host_data.Country[host_data.Season == "Summer"].value_counts()
winter_country = host_data.Country[host_data.Season == "Winter"].value_counts()

plt.figure(figsize=(10,7))
sns.barplot(summer_country.index, summer_country)
plt.xticks(rotation=90)
plt.title("Summer olympics hosting countries")
plt.xlabel("Country")
plt.ylabel("Number of times hosted")
plt.savefig("Summer olympics hosting countries.jpg")

plt.figure(figsize=(10,7))
sns.barplot(winter_country.index, winter_country)
plt.xticks(rotation=90)
plt.title("Winter olympics hosting countries")
plt.xlabel("Country")
plt.ylabel("Number of times hosted")
plt.savefig("Winter olympics hosting countries.jpg")

# Highest hosting cities
summer_city = host_data.City[host_data.Season == "Summer"].value_counts()
winter_city= host_data.City[host_data.Season == "Winter"].value_counts()

plt.figure(figsize=(10,7))
sns.barplot(summer_city.index, summer_city)
plt.xticks(rotation=90)
plt.title("Summer olympics hosting cities")
plt.xlabel("City")
plt.ylabel("Number of times hosted")
plt.savefig("Summer olympics hosting cities.jpg")

plt.figure(figsize=(10,7))
sns.barplot(winter_city.index, winter_city)
plt.xticks(rotation=90)
plt.title("Winter olympics hosting cities")
plt.xlabel("City")
plt.ylabel("Number of times hosted")
plt.savefig("Winter olympics hosting cities.jpg")

# Average age, height and weight for each sports categories
s_average_age = olym_data[olym_data.Season == "Summer"].groupby("Sport")["Age"].median().sort_values()
w_average_age = olym_data[olym_data.Season == "Winter"].groupby("Sport")["Age"].median().sort_values()

s_average_weight = olym_data[olym_data.Season == "Summer"].groupby("Sport")["Weight"].median().sort_values()
w_average_weight = olym_data[olym_data.Season == "Winter"].groupby("Sport")["Weight"].median().sort_values()

s_average_height = olym_data[olym_data.Season == "Summer"].groupby("Sport")["Height"].median().sort_values()
w_average_height = olym_data[olym_data.Season == "Winter"].groupby("Sport")["Height"].median().sort_values()

plt.figure(figsize=(15,7))
sns.barplot(s_average_age.index, s_average_age)
plt.xticks(rotation=90)
plt.title("Average age representation of each sport category-Summer Olympics")
plt.savefig("Summer olympics average age.jpg")

plt.figure(figsize=(15,7))
sns.barplot(w_average_age.index, w_average_age)
plt.xticks(rotation=90)
plt.title("Average age representation of each sport category-Winter Olympics")
plt.savefig("Winter olympics average age.jpg")

plt.figure(figsize=(15,7))
sns.barplot(s_average_weight.index, s_average_weight)
plt.xticks(rotation=90)
plt.title("Average weight representation of each sport category-Summer Olympics")
plt.savefig("Summer olympics average weight.jpg")

plt.figure(figsize=(15,7))
sns.barplot(w_average_weight.index, w_average_weight)
plt.xticks(rotation=90)
plt.title("Average weight representation of each sport category-Winter Olympics")
plt.savefig("Winter olympics average weight.jpg")

plt.figure(figsize=(15,7))
sns.barplot(s_average_height.index, s_average_height)
plt.xticks(rotation=90)
plt.title("Average Height representation of each sport category-Summer Olympics")
plt.savefig("Summer olympics average height.png")

plt.figure(figsize=(15,7))
sns.barplot(w_average_height.index, w_average_height)
plt.xticks(rotation=90)
plt.title("Average Height representation of each sport category-Winter Olympics")
plt.savefig("Winter olympics average height.jpg")
