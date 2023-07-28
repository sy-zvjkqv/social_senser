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

mobile_0to3 = mobile[:, 0:3]
mobile_4to6 = mobile[:, 4:6]
mobile_7to9 = mobile[:, 7:9]
mobile_10to12 = mobile[:, 10:12]
mobile_13to15 = mobile[:, 13:15]
mobile_16to18 = mobile[:, 16:18]
mobile_19to21 = mobile[:, 19:21]
mobile_22to24 = mobile[:, 22:24]

tweets_0to3 = tweets[:, 0:3]
tweets_4to6 = tweets[:, 4:6]
tweets_7to9 = tweets[:, 7:9]
tweets_10to12 = tweets[:, 10:12]
tweets_13to15 = tweets[:, 13:15]
tweets_16to18 = tweets[:, 16:18]
tweets_19to21 = tweets[:, 19:21]
tweets_22to24 = tweets[:, 22:24]

mobile_0to3_flatten = mobile_0to3.flatten()
mobile_4to6_flatten = mobile_4to6.flatten()
mobile_7to9_flatten = mobile_7to9.flatten()
mobile_10to12_flatten = mobile_10to12.flatten()
mobile_13to15_flatten = mobile_13to15.flatten()
mobile_16to18_flatten = mobile_16to18.flatten()
mobile_19to21_flatten = mobile_19to21.flatten()
mobile_22to24_flatten = mobile_22to24.flatten()

tweets_0to3_flatten = tweets_0to3.flatten()
tweets_4to6_flatten = tweets_4to6.flatten()
tweets_7to9_flatten = tweets_7to9.flatten()
tweets_10to12_flatten = tweets_10to12.flatten()
tweets_13to15_flatten = tweets_13to15.flatten()
tweets_16to18_flatten = tweets_16to18.flatten()
tweets_19to21_flatten = tweets_19to21.flatten()
tweets_22to24_flatten = tweets_22to24.flatten()


df_0to3 = pd.DataFrame(
    data=np.stack([tweets_0to3_flatten, mobile_0to3_flatten]).T,
    columns=["Tweets_num", "Population"],
)
df_4to6 = pd.DataFrame(
    data=np.stack([tweets_4to6_flatten, mobile_4to6_flatten]).T,
    columns=["Tweets_num", "Population"],
)
df_7to9 = pd.DataFrame(
    data=np.stack([tweets_7to9_flatten, mobile_7to9_flatten]).T,
    columns=["Tweets_num", "Population"],
)

df_10to12 = pd.DataFrame(
    data=np.stack([tweets_10to12_flatten, mobile_10to12_flatten]).T,
    columns=["Tweets_num", "Population"],
)

df_13to15 = pd.DataFrame(
    data=np.stack([tweets_13to15_flatten, mobile_13to15_flatten]).T,
    columns=["Tweets_num", "Population"],
)

df_16to18 = pd.DataFrame(
    data=np.stack([tweets_16to18_flatten, mobile_16to18_flatten]).T,
    columns=["Tweets_num", "Population"],
)

df_19to21 = pd.DataFrame(
    data=np.stack([tweets_19to21_flatten, mobile_19to21_flatten]).T,
    columns=["Tweets_num", "Population"],
)

df_22to24 = pd.DataFrame(
    data=np.stack([tweets_22to24_flatten, mobile_22to24_flatten]).T,
    columns=["Tweets_num", "Population"],
)

fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.4, hspace=0.6)
fig.suptitle(name_key, fontsize=16)
ax1_1 = fig.add_subplot(4, 2, 1)
ax1_2 = fig.add_subplot(4, 2, 2)
ax2_1 = fig.add_subplot(4, 2, 3)
ax2_2 = fig.add_subplot(4, 2, 4)
ax3_1 = fig.add_subplot(4, 2, 5)
ax3_2 = fig.add_subplot(4, 2, 6)
ax4_1 = fig.add_subplot(4, 2, 7)
ax4_2 = fig.add_subplot(4, 2, 8)


# x_axis = []
# for i in range(0, max(df_0to3['Tweets_num'])+1):
#     x_axis.append(i)

X = mobile_0to3_flatten
y = tweets_0to3_flatten
r_0to3, p_0to3 = stats.pearsonr(X, y)

X = mobile_4to6_flatten
y = tweets_4to6_flatten
r_4to6, p_4to6 = stats.pearsonr(X, y)

X = mobile_7to9_flatten
y = tweets_7to9_flatten
r_7to9, p_7to9 = stats.pearsonr(X, y)

X = mobile_10to12_flatten
y = tweets_10to12_flatten
r_10to12, p_10to12 = stats.pearsonr(X, y)

X = mobile_13to15_flatten
y = tweets_13to15_flatten
r_13to15, p_13to15 = stats.pearsonr(X, y)

X = mobile_16to18_flatten
y = tweets_16to18_flatten
r_16to18, p_16to18 = stats.pearsonr(X, y)

X = mobile_19to21_flatten
y = tweets_19to21_flatten
r_19to21, p_19to21 = stats.pearsonr(X, y)

X = mobile_22to24_flatten
y = tweets_22to24_flatten
r_22to24, p_22to24 = stats.pearsonr(X, y)

plt.figure(figsize=(15, 10))
for i in range(0, max(df_0to3["Tweets_num"])):
    if not max(df_0to3["Tweets_num"] == i):
        df_0to3 = pd.concat(
            [df_0to3, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_0to3, ax=ax1_1, alpha=0.2)
sns.regplot(x="Population", y="Tweets_num", data=df_0to3, scatter=False, ci=None, ax=ax1_1)


for i in range(0, max(df_4to6["Tweets_num"])):
    if not max(df_4to6["Tweets_num"] == i):
        df_4to6 = pd.concat(
            [df_4to6, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )

sns.scatterplot(x="Population", y="Tweets_num", data=df_4to6, ax=ax1_2, alpha=0.2)
sns.regplot(x="Population", y="Tweets_num", data=df_4to6, scatter=False, ci=None, ax=ax1_2)

for i in range(0, max(df_7to9["Tweets_num"])):
    if not max(df_7to9["Tweets_num"] == i):
        df_7to9 = pd.concat(
            [df_7to9, pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"])]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_7to9, ax=ax2_1, alpha=0.2)
sns.regplot(x="Population", y="Tweets_num", data=df_7to9, scatter=False, ci=None, ax=ax2_1)

for i in range(0, max(df_10to12["Tweets_num"])):
    if not max(df_10to12["Tweets_num"] == i):
        df_10to12 = pd.concat(
            [
                df_10to12,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_10to12, ax=ax2_2, alpha=0.200)
sns.regplot(x="Population", y="Tweets_num", data=df_10to12, scatter=False, ci=None, ax=ax2_2)

for i in range(0, max(df_13to15["Tweets_num"])):
    if not max(df_13to15["Tweets_num"] == i):
        df_13to15 = pd.concat(
            [
                df_13to15,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_13to15, ax=ax3_1, alpha=0.200)
sns.regplot(x="Population", y="Tweets_num", data=df_13to15, scatter=False, ci=None, ax=ax3_1)

for i in range(0, max(df_16to18["Tweets_num"])):
    if not max(df_16to18["Tweets_num"] == i):
        df_16to18 = pd.concat(
            [
                df_16to18,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_16to18, ax=ax3_2, alpha=0.200)
sns.regplot(x="Population", y="Tweets_num", data=df_16to18, scatter=False, ci=None, ax=ax3_2)

for i in range(0, max(df_19to21["Tweets_num"])):
    if not max(df_19to21["Tweets_num"] == i):
        df_19to21 = pd.concat(
            [
                df_19to21,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_19to21, ax=ax4_1,alpha=0.200)
sns.regplot(x="Population", y="Tweets_num", data=df_19to21, scatter=False, ci=None, ax=ax4_1)

for i in range(0, max(df_22to24["Tweets_num"])):
    if not max(df_22to24["Tweets_num"] == i):
        df_22to24 = pd.concat(
            [
                df_22to24,
                pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
            ]
        )
sns.scatterplot(x="Population", y="Tweets_num", data=df_22to24, ax=ax4_2, alpha=0.2)
sns.regplot(x="Population", y="Tweets_num", data=df_22to24, scatter=False, ci=None, ax=ax4_2)



ax1_1.set_title("0~3 r={:.2f} p={:.2e}".format(r_0to3, p_0to3), fontsize=16)
ax1_2.set_title("4~6 r={:.2f} p={:.2e}".format(r_4to6, p_4to6), fontsize=16)
ax2_1.set_title("7~9 r={:.2f} p={:.2e}".format(r_7to9, p_7to9), fontsize=16)
ax2_2.set_title("10~12 r={:.2f} p={:.2e}".format(r_10to12, p_10to12), fontsize=16)
ax3_1.set_title("13~15 r={:.2f} p={:.2e}".format(r_13to15, p_13to15), fontsize=16)
ax3_2.set_title("16~18 r={:.2f} p={:.2e}".format(r_16to18, p_16to18), fontsize=16)
ax4_1.set_title("19~21 r={:.2f} p={:.2e}".format(r_19to21, p_19to21), fontsize=16)
ax4_2.set_title("22~24 r={:.2f} p={:.2e}".format(r_22to24, p_22to24), fontsize=16)

ax1_1.set_xticklabels(ax1_1.get_xticklabels(), rotation=90)
ax1_2.set_xticklabels(ax1_2.get_xticklabels(), rotation=90)
ax2_1.set_xticklabels(ax2_1.get_xticklabels(), rotation=90)
ax2_2.set_xticklabels(ax2_2.get_xticklabels(), rotation=90)
ax3_1.set_xticklabels(ax3_1.get_xticklabels(), rotation=90)
ax3_2.set_xticklabels(ax3_2.get_xticklabels(), rotation=90)
ax4_1.set_xticklabels(ax4_1.get_xticklabels(), rotation=90)
ax4_2.set_xticklabels(ax4_2.get_xticklabels(), rotation=90)

save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/heat/time"
    + name_key
    + ".png"
)
fig.savefig(save_PATH)
fig.savefig(save_PATH)
