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

# Unique sports over years in Olympics
summer_sports = olym_data[olym_data.Season=="Summer"].groupby(["Year"])["Sport"].apply(lambda x : len(x.unique()))
winter_sports = olym_data[olym_data.Season=="Winter"].groupby(["Year"])["Sport"].apply(lambda x : len(x.unique()))

plt.figure(figsize=(10,7))
sns.pointplot(summer_sports.index, summer_sports, color="purple")
plt.xticks(rotation=80)
plt.ylabel("Sports count")
plt.savefig("Unique sports in Summer olympics over years")

plt.figure(figsize=(10,7))
sns.pointplot(winter_sports.index, winter_sports, color="red")
plt.xticks(rotation=80)
plt.ylabel("Sports count")
plt.savefig("Unique sports in Winter olympics over years")

# Gender event ratio
s_unique_event = pd.DataFrame()
s_unique_event["Event"] = olym_data.Event[olym_data.Season == "Summer"].unique()

w_unique_event = pd.DataFrame()
w_unique_event["Event"] = olym_data.Event[olym_data.Season == "Winter"].unique()

import re
regex_m = re.compile("Men")
regex_w = re.compile("Women")
def gender_mod(value):
    if regex_m.search(value):
        return "Male"
    elif regex_w.search(value):
        return "Female"
    else:
        return "Missing"

s_unique_event["Gender"] = s_unique_event["Event"].apply(gender_mod)
s_gender_ratio = s_unique_event.Gender.value_counts()

w_unique_event["Gender"] = w_unique_event["Event"].apply(gender_mod)
w_gender_ratio = w_unique_event.Gender.value_counts()

plt.style.use("ggplot")
plt.figure(figsize=(10,7))
plt.pie(s_gender_ratio.head(2), labels=list(s_gender_ratio.index[:2]),colors=["Green", "Gold"], autopct="%.1f%%")
my_circle=plt.Circle((0,0), radius=0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.axis("equal")
plt.title("Event ratio according to gender in Summer Olympics")
plt.savefig("Summer olympics event-gender ratio.jpg")

plt.figure(figsize=(10,7))
plt.pie(w_gender_ratio.head(2), labels=list(w_gender_ratio.index[:2]),colors=["Green", "Gold"], autopct="%.1f%%")
my_circle=plt.Circle((0,0), radius=0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.axis("equal")
plt.title("Event ratio according to gender in Winter Olympics")
plt.savefig("Winter olympics event-gender ratio.jpg")

# Events by gender categorisation over years
olym_data["Event category"] = olym_data.Event.apply(gender_mod)
gender_data = olym_data.loc[:,["Year", "Season", "Event", "Event category"]].drop_duplicates(["Year", "Season", "Event", "Event category"])
gender_data.index = [x for x in range(6192)] 
s_gender_data = gender_data[gender_data.Season == "Summer"].sort_values("Year")
s_gender_data = s_gender_data.groupby("Year")["Event category"].value_counts().unstack()
w_gender_data = gender_data[gender_data.Season == "Winter"].sort_values("Year")
w_gender_data = w_gender_data.groupby("Year")["Event category"].value_counts().unstack()

fig=plt.figure(figsize=(10,7))
plt.style.use("ggplot")
plt.scatter(s_gender_data.index, s_gender_data.Male, color="green")
plt.plot(s_gender_data.index, s_gender_data.Male, color="green")
plt.scatter(s_gender_data.index, s_gender_data.Female, color="red")
plt.plot(s_gender_data.index, s_gender_data.Female, color="red")
fig.legend(labels=["Male", "Female"])
plt.xticks(rotation=90)
plt.title("Summer olympics Event-gender categorisation over years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("Summer olympics Event-gender categorisation over years.jpg")

fig=plt.figure(figsize=(10,7))
plt.style.use("ggplot")
plt.scatter(w_gender_data.index, w_gender_data.Male, color="green")
plt.plot(w_gender_data.index, w_gender_data.Male, color="green")
plt.scatter(w_gender_data.index, w_gender_data.Female, color="red")
plt.plot(w_gender_data.index, w_gender_data.Female, color="red")
fig.legend(labels=["Male", "Female"])
plt.xticks(rotation=90)
plt.title("Winter olympics Event-gender categorisation over years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("Winter olympics Event-gender categorisation over years.jpg")

# Discontinued sports till 2016
sports_2016 = olym_data.Sport[(olym_data.Year==2016) & (olym_data.Season == "Summer")].unique()
sports_n2016 = olym_data.Sport[(olym_data.Year!=2016) & (olym_data.Season == "Summer")].unique()
discontinued_sports = np.setdiff1d(sports_n2016, sports_2016)
new_sport = np.setdiff1d(sports_2016, sports_n2016)
print("Discontinued sports till 2016:")
for index, var in enumerate(discontinued_sports):
    print(index,"--->",var)
# print("New sport in 2016 Olympics--->", new_sport[0])

# Revenue distribution
# Revenue Categories
A = ["Acquatics", "Atheletes", "Gymnastics"]
B = ["Cycling", "Tennis"]
C = ["Archery", "Badminton", "Boxing", "Judo", "Rowing", "Shooting", "Table Tennis", "Weightlifting"]
D = ["Canoeing", "Equestrianism", "Sailing", "Fencing", "Taekwondo", "Triathlon", "Wrestling"]
E = ["Modern Pentathlon", "Golf"]
# NRC-No Revenue Category
def rev_cat(value):
    if value in A:
        return "A"
    elif value in B:
        return "B"
    elif value in C:
        return "C"
    elif value in D:
        return "D"
    elif value in E:
        return "E"
    else:
        return "NRC"
olym_data["Revenue_catg"] = olym_data.Sport.apply(rev_cat)
revenue_count = olym_data.Revenue_catg.value_counts()

plt.figure(figsize=(10,7))
plt.style.use("ggplot")
plt.pie(revenue_count[1:], labels=list(revenue_count.index[1:]), autopct="%.1f%%")
plt.axis("equal")
plt.title("Sports revenue categories distribution")
plt.savefig("Sports-revenue-categories-distribution.jpg")

# Medal won in each revenue category
revenue_medal = olym_data.groupby(["Revenue_catg", "Season"])["Medal"].apply(lambda x: len(x)).unstack()

plt.figure(figsize=(10,7))
plt.style.use("ggplot")
plt.pie(revenue_medal.Summer[:-1], labels=list(revenue_medal.index[:-1]), autopct="%.1f%%")
plt.axis("equal")
plt.title("Sports-medal revenue categories distribution")
plt.savefig("Sports-medal-revenue-categories-distribution.jpg")

# Medal tally for each sport category
s_sport_medal = olym_data[olym_data.Season == "Summer"].groupby("Sport")["Medal"].value_counts().unstack()
s_sport_medal = s_sport_medal.iloc[:, [1,2,0]].sort_values("Gold")
s_sport_medal = s_sport_medal.fillna(0)
s_sport_medal["Total"] = s_sport_medal.apply(lambda x: sum(x), axis=1)

plt.figure(figsize=(14,7))
sns.barplot(s_sport_medal.index, s_sport_medal["Total"])
plt.xticks(rotation=90)
plt.title("Medal-tally-summer-sports")
plt.savefig("Medal-tally-summer-sports.jpg")

w_sport_medal = olym_data[olym_data.Season == "Winter"].groupby("Sport")["Medal"].value_counts().unstack()
w_sport_medal = w_sport_medal.iloc[:, [1,2,0]].sort_values("Gold")
w_sport_medal = w_sport_medal.fillna(0)
w_sport_medal["Total"] = w_sport_medal.apply(lambda x: sum(x), axis=1)

plt.figure(figsize=(14,7))
sns.barplot(w_sport_medal.index, w_sport_medal["Total"])
plt.xticks(rotation=90)
plt.title("Medal-tally-winter-sports")
plt.savefig("Medal-tally-winter-sports.jpg")

# Top 100 atheletes information 
s_top_athlete = olym_data[olym_data.Season == "Summer"].groupby("Name")["Medal"].value_counts().unstack()
s_top_athlete = s_top_athlete.iloc[:,[1,2,0]]
s_top_athlete = s_top_athlete.fillna(0)
s_top_athlete["Total"] = s_top_athlete.apply(lambda x: sum(x), axis=1)
s_top_athlete = s_top_athlete.sort_values("Total", ascending=False)

plt.figure(figsize=(22,7))
sns.barplot(s_top_athlete.index[:100], s_top_athlete["Total"][:100])
plt.xticks(rotation=90)
plt.title("Summer olympics top 100 athletes")
plt.savefig("Summer olympics top 100 athletes.jpg")

w_top_athlete = olym_data[olym_data.Season == "Winter"].groupby("Name")["Medal"].value_counts().unstack()
w_top_athlete = w_top_athlete.iloc[:,[1,2,0]]
w_top_athlete = w_top_athlete.fillna(0)
w_top_athlete["Total"] = w_top_athlete.apply(lambda x: sum(x), axis=1)
w_top_athlete = w_top_athlete.sort_values("Total", ascending=False)

plt.figure(figsize=(22,7))
sns.barplot(w_top_athlete.index[:100], w_top_athlete["Total"][:100])
plt.xticks(rotation=90)
plt.title("Winter olympics top 100 athletes")
plt.savefig("Winter olympics top 100 athletes.jpg")

top_athlete = olym_data.groupby("Name")["Medal"].value_counts().unstack()
top_athlete = top_athlete.iloc[:,[1,2,0]]
top_athlete = top_athlete.fillna(0)
top_athlete["Total"] = top_athlete.apply(lambda x: sum(x), axis=1)
top_athlete = top_athlete.sort_values("Total", ascending=False)

plt.figure(figsize=(22,7))
sns.barplot(top_athlete.index[:100], top_athlete["Total"][:100])
plt.xticks(rotation=90)
plt.title("olympics top 100 athletes")
plt.savefig("olympics top 100 athletes.jpg")