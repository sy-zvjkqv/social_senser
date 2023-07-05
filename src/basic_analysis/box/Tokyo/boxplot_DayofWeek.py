import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
from matplotlib import mlab
from scipy import signal, stats
from sklearn import preprocessing
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.linear_model import LinearRegression

day_list_long = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
]
day_list_short = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
]
day_list_Feb = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
]
hour_list = [
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
]
x_label = []
for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    if month in ["01", "03", "05", "07", "08", "10", "12"]:
        day_list = day_list_long
    elif month == "02":
        day_list = day_list_Feb
    else:
        day_list = day_list_short
    for day in day_list:
        for hour in range(0, 24):
            hour = str(hour)
            key = int("21" + month + day + hour)
            key = str(key)
            x_label.append(key)


mobile = np.load(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Tokyostation/Tokyostation_2021.npy"
)
tweets = np.load(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Tokyostation_2021/outlier/Tokyostation_3zi_2021.npy"
)
name_key = "Tokyostation"

list_mobile_Sun = []
list_mobile_Mon = []
list_mobile_Tue = []
list_mobile_Wed = []
list_mobile_Thu = []
list_mobile_Fri = []
list_mobile_Sat = []

list_tweets_Sun = []
list_tweets_Mon = []
list_tweets_Tue = []
list_tweets_Wed = []
list_tweets_Thu = []
list_tweets_Fri = []
list_tweets_Sat = []
for i in range(0, 365):
    if i % 7 == 0:
        list_mobile_Fri.append(mobile[i].tolist())
        list_tweets_Fri.append(tweets[i].tolist())
    if i % 7 == 1:
        list_mobile_Sat.append(mobile[i].tolist())
        list_tweets_Sat.append(tweets[i].tolist())
    if i % 7 == 2:
        list_mobile_Sun.append(mobile[i].tolist())
        list_tweets_Sun.append(tweets[i].tolist())
    if i % 7 == 3:
        list_mobile_Mon.append(mobile[i].tolist())
        list_tweets_Mon.append(tweets[i].tolist())
    if i % 7 == 4:
        list_mobile_Tue.append(mobile[i].tolist())
        list_tweets_Tue.append(tweets[i].tolist())
    if i % 7 == 5:
        list_mobile_Wed.append(mobile[i].tolist())
        list_tweets_Wed.append(tweets[i].tolist())
    if i % 7 == 6:
        list_mobile_Thu.append(mobile[i].tolist())
        list_tweets_Thu.append(tweets[i].tolist())

list_mobile_Fri = np.array(list_mobile_Fri)
list_tweets_Fri = np.array(list_tweets_Fri)

list_mobile_Sat = np.array(list_mobile_Sat)
list_tweets_Sat = np.array(list_tweets_Sat)

list_mobile_Sun = np.array(list_mobile_Sun)
list_tweets_Sun = np.array(list_tweets_Sun)

list_mobile_Mon = np.array(list_mobile_Mon)
list_tweets_Mon = np.array(list_tweets_Mon)

list_mobile_Tue = np.array(list_mobile_Tue)
list_tweets_Tue = np.array(list_tweets_Tue)

list_mobile_Wed = np.array(list_mobile_Wed)
list_tweets_Wed = np.array(list_tweets_Wed)

list_mobile_Thu = np.array(list_mobile_Thu)
list_tweets_Thu = np.array(list_tweets_Thu)

list_mobile_Fri = list_mobile_Fri.flatten()
list_tweets_Fri = list_tweets_Fri.flatten()

list_mobile_Sat = list_mobile_Sat.flatten()
list_tweets_Sat = list_tweets_Sat.flatten()

list_mobile_Sun = list_mobile_Sun.flatten()
list_tweets_Sun = list_tweets_Sun.flatten()

list_mobile_Mon = list_mobile_Mon.flatten()
list_tweets_Mon = list_tweets_Mon.flatten()

list_mobile_Tue = list_mobile_Tue.flatten()
list_tweets_Tue = list_tweets_Tue.flatten()

list_mobile_Wed = list_mobile_Wed.flatten()
list_tweets_Wed = list_tweets_Wed.flatten()

list_mobile_Thu = list_mobile_Thu.flatten()
list_tweets_Thu = list_tweets_Thu.flatten()


df_Fri = pd.DataFrame(
    data=np.stack([list_tweets_Fri, list_mobile_Fri]).T,
    columns=["Tweets_num", "Population"],
)
df_Sat = pd.DataFrame(
    data=np.stack([list_tweets_Sat, list_mobile_Sat]).T,
    columns=["Tweets_num", "Population"],
)
df_Sun = pd.DataFrame(
    data=np.stack([list_tweets_Sun, list_mobile_Sun]).T,
    columns=["Tweets_num", "Population"],
)
df_Mon = pd.DataFrame(
    data=np.stack([list_tweets_Mon, list_mobile_Mon]).T,
    columns=["Tweets_num", "Population"],
)
df_Tue = pd.DataFrame(
    data=np.stack([list_tweets_Tue, list_mobile_Tue]).T,
    columns=["Tweets_num", "Population"],
)
df_Wed = pd.DataFrame(
    data=np.stack([list_tweets_Wed, list_mobile_Wed]).T,
    columns=["Tweets_num", "Population"],
)
df_Thu = pd.DataFrame(
    data=np.stack([list_tweets_Thu, list_mobile_Thu]).T,
    columns=["Tweets_num", "Population"],
)

fig = plt.figure(figsize=(20, 25))
plt.subplots_adjust(hspace=0.6)
fig.suptitle(name_key, fontsize=16)
ax1_1 = fig.add_subplot(4, 2, 1)
ax1_2 = fig.add_subplot(4, 2, 2)
ax1_3 = fig.add_subplot(4, 2, 3)
ax1_4 = fig.add_subplot(4, 2, 4)
ax1_5 = fig.add_subplot(4, 2, 5)
ax1_6 = fig.add_subplot(4, 2, 6)
ax1_7 = fig.add_subplot(4, 2, 7)

# x_axis = []
# for i in range(0, max(df_asa['Tweets_num'])+1):
#     x_axis.append(i)

X = list_mobile_Fri.reshape(-1, 1)
y = list_tweets_Fri.reshape(-1, 1)
mi_Fri = mutual_info_regression(X, y)

X = list_mobile_Sat.reshape(-1, 1)
y = list_tweets_Sat.reshape(-1, 1)
mi_Sat = mutual_info_regression(X, y)

X = list_mobile_Sun.reshape(-1, 1)
y = list_tweets_Sun.reshape(-1, 1)
mi_Sun = mutual_info_regression(X, y)

X = list_mobile_Mon.reshape(-1, 1)
y = list_tweets_Mon.reshape(-1, 1)
mi_Mon = mutual_info_regression(X, y)

X = list_mobile_Tue.reshape(-1, 1)
y = list_tweets_Tue.reshape(-1, 1)
mi_Tue = mutual_info_regression(X, y)

X = list_mobile_Wed.reshape(-1, 1)
y = list_tweets_Wed.reshape(-1, 1)
mi_Wed = mutual_info_regression(X, y)

X = list_mobile_Thu.reshape(-1, 1)
y = list_tweets_Thu.reshape(-1, 1)
mi_Thu = mutual_info_regression(X, y)

# Fri
for i in range(0, max(df_Fri["Tweets_num"])):
    if not max(df_Fri["Tweets_num"] == i):
        df_Fri = pd.concat(
            [df_Fri, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Fri, ax=ax1_1, whis=100)

if max(df_Fri["Tweets_num"]) > 40:
    ax1_1.set_xticklabels(ax1_1.get_xticklabels(), rotation=90)
# x_axis = []
# for i in range(0, max(df_Fri["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Fri, list_mobile_Fri, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_1)

# Sat
for i in range(0, max(df_Sat["Tweets_num"])):
    if not max(df_Sat["Tweets_num"] == i):
        df_Sat = pd.concat(
            [df_Sat, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Sat, ax=ax1_2, whis=100)

if max(df_Sat["Tweets_num"]) > 40:
    ax1_2.set_xticklabels(ax1_2.get_xticklabels(), rotation=90)

# x_axis = []
# for i in range(0, max(df_Sat["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Sat, list_mobile_Sat, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_2)

# Sun
for i in range(0, max(df_Sun["Tweets_num"])):
    if not max(df_Sun["Tweets_num"] == i):
        df_Sun = pd.concat(
            [df_Sun, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Sun, ax=ax1_3, whis=100)

if max(df_Sun["Tweets_num"]) > 40:
    ax1_3.set_xticklabels(ax1_3.get_xticklabels(), rotation=90)
# x_axis = []
# for i in range(0, max(df_Sun["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Sun, list_mobile_Sun, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_3)

# Mon
for i in range(0, max(df_Mon["Tweets_num"])):
    if not max(df_Mon["Tweets_num"] == i):
        df_Mon = pd.concat(
            [df_Mon, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Mon, ax=ax1_4, whis=100)

if max(df_Mon["Tweets_num"]) > 40:
    ax1_4.set_xticklabels(ax1_4.get_xticklabels(), rotation=90)
# x_axis = []
# for i in range(0, max(df_Mon["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Mon, list_mobile_Mon, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_4)

# Tue
for i in range(0, max(df_Tue["Tweets_num"])):
    if not max(df_Tue["Tweets_num"] == i):
        df_Tue = pd.concat(
            [df_Tue, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Tue, ax=ax1_5, whis=100)

if max(df_Tue["Tweets_num"]) > 40:
    ax1_5.set_xticklabels(ax1_5.get_xticklabels(), rotation=90)
# x_axis = []
# for i in range(0, max(df_Thu["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Thu, list_mobile_Thu, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_5)

# Wed
for i in range(0, max(df_Wed["Tweets_num"])):
    if not max(df_Wed["Tweets_num"] == i):
        df_Wed = pd.concat(
            [df_Wed, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Wed, ax=ax1_6, whis=100)

if max(df_Wed["Tweets_num"]) > 40:
    ax1_6.set_xticklabels(ax1_6.get_xticklabels(), rotation=90)
# x_axis = []
# for i in range(0, max(df_Wed["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Wed, list_mobile_Wed, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_6)

# Thu
for i in range(0, max(df_Thu["Tweets_num"])):
    if not max(df_Thu["Tweets_num"] == i):
        df_Thu = pd.concat(
            [df_Thu, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.boxplot(x="Tweets_num", y="Population", data=df_Thu, ax=ax1_7, whis=100)

if max(df_Thu["Tweets_num"]) > 40:
    ax1_7.set_xticklabels(ax1_7.get_xticklabels(), rotation=90)
# x_axis = []
# for i in range(0, max(df_Thu["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_Thu, list_mobile_Thu, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_7)


ax1_1.set_title("Fri MI={:.2f}".format(mi_Fri[0]), fontsize=16)
ax1_2.set_title("Sat MI={:.2f}".format(mi_Sat[0]), fontsize=16)
ax1_3.set_title("Sun MI={:.2f}".format(mi_Sun[0]), fontsize=16)
ax1_4.set_title("Mon MI={:.2f}".format(mi_Mon[0]), fontsize=16)
ax1_5.set_title("Tue MI={:.2f}".format(mi_Tue[0]), fontsize=16)
ax1_6.set_title("Wed MI={:.2f}".format(mi_Wed[0]), fontsize=16)
ax1_7.set_title("Thu MI={:.2f}".format(mi_Thu[0]), fontsize=16)


save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/box/DayofWeek/"
    + name_key
    + ".png"
)
fig.savefig(save_PATH)
