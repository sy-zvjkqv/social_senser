import pandas as pd
import numpy as np
from scipy import signal
from scipy import stats
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
from sklearn import preprocessing
import matplotlib.cm as cm
import seaborn as sns

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


mobile = np.load('/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Tokyostation/Tokyostation_2021.npy')
tweets = np.load('/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Tokyostation_2021/outlier/Tokyostation_3zi_2021.npy')
name_key = 'Tokyostation'

mobile = np.sum(mobile, axis=1)
tweets = np.sum(tweets, axis=1)


list_Week_of_Day = []
for i in range(0, 365):   
    if i % 7 == 1:
        list_Week_of_Day.append('Holiday')
    if i % 7 == 2:
        list_Week_of_Day.append('Holiday')
    if i % 7 == 0:
        list_Week_of_Day.append('Workday')
    if i % 7 == 3:
        list_Week_of_Day.append('Workday')
    if i % 7 == 4:
        list_Week_of_Day.append('Workday')
    if i % 7 == 5:
        list_Week_of_Day.append('Workday')
    if i % 7 == 6:
        list_Week_of_Day.append('Workday')
        

df = pd.DataFrame(
    data=np.stack([mobile, tweets ,list_Week_of_Day]).T,
    columns=[ "Population", "Tweets_num","Week_of_Day"],
)
df["Tweets_num"] =df["Tweets_num"].astype(float)
df["Population"] =df["Population"].astype(float)


fig = sns.scatterplot(x="Tweets_num", y="Population", data=df)

X = mobile.reshape(-1, 1)
y = tweets.reshape(-1, 1)
a, b = np.polyfit(X[:, 0], y, 1)
mi = mutual_info_regression(X, y)
f_test, _ = f_regression(X, y)
fig.set(title = "{} Mi={:.2f}".format(name_key, mi[0]))
print(y.dtype)
print(mi)



save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/scatter_perDay"
    + name_key
    + ".png"
)
plt.savefig(save_PATH)
