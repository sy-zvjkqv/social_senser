import datetime

import jpholiday
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
work_holi_Flag = []
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
        Flag = int("2021" + month + day)
        Flag = str(Flag)
        work_holi_Flag.append(Flag)


mobile = np.load(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Tokyostation.npy"
)
tweets = np.load(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Tokyostaion.npy"
)
name_key = "Tokyostation"

mobile = np.sum(mobile, axis=1)
tweets = np.sum(tweets, axis=1)


# DATE = yyyymmdd#
def isBizDay(DATE):
    Date = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))
    if Date.weekday() >= 5 or jpholiday.is_holiday(Date):
        return "Holiday"
    else:
        return "Workday"


list_Week_of_Day = []
for i in work_holi_Flag:
    if (
        i == "20210101"
        or i == "20210102"
        or i == "20210103"
        or i == "20211229"
        or i == "20211230"
        or i == "20211231"
    ):
        list_Week_of_Day.append("Holiday")
    else:
        list_Week_of_Day.append(isBizDay(i))

df = pd.DataFrame(
    data=np.stack([mobile, tweets, list_Week_of_Day]).T,
    columns=["Population", "Tweets_num", "Week_of_Day"],
)
df["Tweets_num"] = df["Tweets_num"].astype(float)
df["Population"] = df["Population"].astype(float)


fig = plt.figure(figsize=(20, 25))


fig = sns.lmplot(
    x="Tweets_num",
    y="Population",
    hue="Week_of_Day",
    data=df,
    ci=None,
    palette=dict(Workday="g", Holiday="m"),
)

df_work = df[df["Week_of_Day"] == "Workday"]
df_holi = df[df["Week_of_Day"] == "Holiday"]

X = df_work["Population"].to_numpy()
y = df_work["Tweets_num"].to_numpy()
correlation_work, p_value_work = stats.pearsonr(X, y)

X = df_holi["Population"].to_numpy()
y = df_holi["Tweets_num"].to_numpy()
correlation_holi, p_value_holi = stats.pearsonr(X, y)

fig.set(
    title="r_work={:.2f} r_holi={:.2f}\n p_work={:.2e} p_holi={:.2e}".format(
        correlation_work, correlation_holi, p_value_work, p_value_holi
    )
)
print(" {}, {}, {}, {}, {},".format(
        name_key, correlation_work, p_value_work, correlation_holi, p_value_holi
    ))

save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/perday/work_holi/"
    + name_key
    + ".png"
)
fig.savefig(save_PATH)
