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
from sklearn import preprocessing
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


mobile_flatten = mobile.flatten()
tweets_flatten = tweets.flatten()

def standardization(x, axis=None, ddof=0):
    x_mean = x.mean(axis=axis, keepdims=True)
    x_std = x.std(axis=axis, keepdims=True, ddof=ddof)
    return (x - x_mean) / x_std


mobile_flatten = standardization(mobile_flatten)
tweets_flatten = standardization(tweets_flatten)
print(tweets_flatten)
tmp = np.stack([tweets_flatten, mobile_flatten])
df_mobile_tweets = pd.DataFrame(data=tmp.T, columns=["Tweets_num", "Population"])
# for i in range(0, max(df_mobile_tweets["Tweets_num"])):
#     if not max(df_mobile_tweets["Tweets_num"] == i):
#         df_mobile_tweets = pd.concat(
#             [
#                 df_mobile_tweets,
#                 pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
#             ]
#         )


# x_axis = []
# for i in range(0, int(max(df_mobile_tweets["Tweets_num"])) + 1):
#     x_axis.append(i)

# a, b = np.polyfit(tweets_flatten, mobile_flatten, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )

# X = mobile_flatten.reshape(-1, 1)
# y = tweets_flatten.reshape(-1, 1)
# a, b = np.polyfit(X[:, 0], y, 1)
# mi = mutual_info_regression(X, y)
# f_test, _ = f_regression(X, y)
# フィッティング直線


X = mobile_flatten
y = tweets_flatten
correlation, p_value = stats.pearsonr(X, y)

plt.figure(figsize=(15, 10))

#sns.jointplot(x=x, y=y, kind="hist", color="#D91887")


sns.histplot(x="Population", y="Tweets_num", data=df_mobile_tweets,bins=10)
sns.regplot(x="Population", y="Tweets_num",data=df_mobile_tweets, scatter=False, ci=None)

# sns.regplot(x="Tweets_num", y="Population", data=df2glaph)
# plt.xticks(x_axis, x_axis)
plt.xlabel("Number of Twitter Users per 1hour")
plt.ylabel("Populations per 1hour")
plt.title("{}  r={:.2f} p={:.2e}".format(name_key, correlation, p_value), fontsize=16)
plt.xticks(rotation=90)

save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/heat/perhour/"
    + name_key
    + ".png"
)
plt.savefig(save_PATH)
