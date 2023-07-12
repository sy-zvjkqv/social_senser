import datetime

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


def weekofday(date):
    w_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    year = "20" + date[0:2]
    year = int(year)
    month = int(date[2:4])
    day = int(date[4:6])
    dt = datetime.datetime(year, month, day)
    return w_list[dt.weekday()]


list_Week_of_Day = []
for date in x_label:
    list_Week_of_Day.append(weekofday(date))


mobile = np.load(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Tokyostation/Tokyostation_2021.npy"
)
tweets = np.load(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Tokyostation_2021/outlier/Tokyostation_3zi_2021.npy"
)
name_key = "Tokyostation"
mobile_flatten = mobile.flatten()
tweets_flatten = tweets.flatten()

tmp = np.stack([tweets_flatten, mobile_flatten, list_Week_of_Day])
df_mobile_tweets = pd.DataFrame(
    data=tmp.T, columns=["Tweets_num", "Population", "DayofWeek"]
)
df_mobile_tweets["Tweets_num"] = df_mobile_tweets["Tweets_num"].astype(int)
df_mobile_tweets["Population"] = df_mobile_tweets["Population"].astype(int)
for i in range(0, max(df_mobile_tweets["Tweets_num"])):
    if not max(df_mobile_tweets["Tweets_num"] == i):
        df_mobile_tweets = pd.concat(
            [
                df_mobile_tweets,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
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


df_Mon = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Mon"]
df_Tue = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Tue"]
df_Wed = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Wed"]
df_Thu = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Thu"]
df_Fri = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Fri"]
df_Sat = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Sat"]
df_Sun = df_mobile_tweets[df_mobile_tweets["DayofWeek"] == "Sun"]

X = df_Mon["Population"]
y = df_Mon["Tweets_num"]
c_Mon, p_Mon = stats.pearsonr(X, y)

X = df_Tue["Population"]
y = df_Tue["Tweets_num"]
c_Tue, p_Tue = stats.pearsonr(X, y)

X = df_Wed["Population"]
y = df_Wed["Tweets_num"]
c_Wed, p_Wed = stats.pearsonr(X, y)

X = df_Thu["Population"]
y = df_Thu["Tweets_num"]
c_Thu, p_Thu = stats.pearsonr(X, y)

X = df_Fri["Population"]
y = df_Fri["Tweets_num"]
c_Fri, p_Fri = stats.pearsonr(X, y)

X = df_Sat["Population"]
y = df_Sat["Tweets_num"]
c_Sat, p_Sat = stats.pearsonr(X, y)

X = df_Sun["Population"]
y = df_Sun["Tweets_num"]
c_Sun, p_Sun = stats.pearsonr(X, y)


for i in range(0, max(df_Mon["Tweets_num"])):
    if not max(df_Mon["Tweets_num"] == i):
        df_Mon = pd.concat(
            [
                df_Mon,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
for i in range(0, max(df_Tue["Tweets_num"])):
    if not max(df_Tue["Tweets_num"] == i):
        df_Tue = pd.concat(
            [
                df_Tue,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
for i in range(0, max(df_Wed["Tweets_num"])):
    if not max(df_Wed["Tweets_num"] == i):
        df_Wed = pd.concat(
            [
                df_Wed,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
for i in range(0, max(df_Thu["Tweets_num"])):
    if not max(df_Thu["Tweets_num"] == i):
        df_Thu = pd.concat(
            [
                df_Thu,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
for i in range(0, max(df_Fri["Tweets_num"])):
    if not max(df_Fri["Tweets_num"] == i):
        df_Fri = pd.concat(
            [
                df_Fri,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
for i in range(0, max(df_Sat["Tweets_num"])):
    if not max(df_Sat["Tweets_num"] == i):
        df_Sat = pd.concat(
            [
                df_Sat,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
for i in range(0, max(df_Sun["Tweets_num"])):
    if not max(df_Sun["Tweets_num"] == i):
        df_Sun = pd.concat(
            [
                df_Sun,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )


sns.boxplot(x="Tweets_num", y="Population", data=df_Mon, whis=100, ax=ax1_1)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Mon, scatter=False, ci=None, ax=ax1_1
)
sns.boxplot(x="Tweets_num", y="Population", data=df_Tue, whis=100, ax=ax1_2)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Tue, scatter=False, ci=None, ax=ax1_2
)
sns.boxplot(x="Tweets_num", y="Population", data=df_Wed, whis=100, ax=ax1_3)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Wed, scatter=False, ci=None, ax=ax1_3
)
sns.boxplot(x="Tweets_num", y="Population", data=df_Thu, whis=100, ax=ax1_4)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Thu, scatter=False, ci=None, ax=ax1_4
)
sns.boxplot(x="Tweets_num", y="Population", data=df_Fri, whis=100, ax=ax1_5)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Fri, scatter=False, ci=None, ax=ax1_5
)
sns.boxplot(x="Tweets_num", y="Population", data=df_Sat, whis=100, ax=ax1_6)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Sat, scatter=False, ci=None, ax=ax1_6
)
sns.boxplot(x="Tweets_num", y="Population", data=df_Sun, whis=100, ax=ax1_7)
sns.regplot(
    x="Tweets_num", y="Population", data=df_Sun, scatter=False, ci=None, ax=ax1_7
)
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph)
# plt.xticks(x_axis, x_axis)
plt.xlabel("Number of Twitter Users per 1hour")
plt.ylabel("Populations per 1hour")
plt.title("{}".format(name_key), fontsize=16)


ax1_1.set_title("Mon r={:.2f} p={:.2e}".format(c_Mon, p_Mon), fontsize=16)
ax1_2.set_title("Tue r={:.2f} p={:.2e}".format(c_Tue, p_Tue), fontsize=16)
ax1_3.set_title("Wed r={:.2f} p={:.2e}".format(c_Wed, p_Wed), fontsize=16)
ax1_4.set_title("Thu r={:.2f} p={:.2e}".format(c_Thu, p_Thu), fontsize=16)
ax1_5.set_title("Fri r={:.2f} p={:.2e}".format(c_Fri, p_Fri), fontsize=16)
ax1_6.set_title("Sat r={:.2f} p={:.2e}".format(c_Sat, p_Sat), fontsize=16)
ax1_7.set_title("Sun r={:.2f} p={:.2e}".format(c_Sun, p_Sun), fontsize=16)

ax1_1.set_xticklabels(ax1_1.get_xticklabels(), rotation=90)
ax1_2.set_xticklabels(ax1_2.get_xticklabels(), rotation=90)
ax1_3.set_xticklabels(ax1_3.get_xticklabels(), rotation=90)
ax1_4.set_xticklabels(ax1_4.get_xticklabels(), rotation=90)
ax1_5.set_xticklabels(ax1_5.get_xticklabels(), rotation=90)
ax1_6.set_xticklabels(ax1_6.get_xticklabels(), rotation=90)
ax1_7.set_xticklabels(ax1_7.get_xticklabels(), rotation=90)


save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/regression/perhour/dayofweek/"
    + name_key
    + ".png"
)
plt.savefig(save_PATH)
