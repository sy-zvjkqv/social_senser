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

mobile = np.sum(mobile, axis=1)
tweets = np.sum(tweets, axis=1)


list_Week_of_Day = []
for i in range(0, 365):
    if i % 7 == 1:
        list_Week_of_Day.append("Holiday")
    if i % 7 == 2:
        list_Week_of_Day.append("Holiday")
    if i % 7 == 0:
        list_Week_of_Day.append("Workday")
    if i % 7 == 3:
        list_Week_of_Day.append("Workday")
    if i % 7 == 4:
        list_Week_of_Day.append("Workday")
    if i % 7 == 5:
        list_Week_of_Day.append("Workday")
    if i % 7 == 6:
        list_Week_of_Day.append("Workday")


df = pd.DataFrame(
    data=np.stack([mobile, tweets, list_Week_of_Day]).T,
    columns=["Population", "Tweets_num", "Week_of_Day"],
)
df["Tweets_num"] = df["Tweets_num"].astype(float)
df["Population"] = df["Population"].astype(float)


fig = sns.scatterplot(x="Tweets_num", y="Population", hue="Week_of_Day", data=df)
df_work = df[df["Week_of_Day"] == "Workday"]
df_holi = df[df["Week_of_Day"] == "Holiday"]

X = df_work["Population"].to_numpy()
y = df_work["Tweets_num"].to_numpy()
X = X.astype(int)
y = y.astype(int)
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)
mi_work = mutual_info_regression(X, y)

X = df_holi["Population"].to_numpy()
y = df_holi["Tweets_num"].to_numpy()
X = X.astype(int)
y = y.astype(int)
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)
mi_holi = mutual_info_regression(X, y)
fig.set(
    title="{} Mi_workday={:.2f} Mi_holiday={:.2f}".format(
        name_key, mi_work[0], mi_holi[0]
    )
)


save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/scatter_perDay/work_holi/"
    + name_key
    + ".png"
)
plt.savefig(save_PATH)
