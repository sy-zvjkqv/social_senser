import pandas as pd
import numpy as np
from scipy import signal
from scipy import stats
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
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


list_mobile_work = []
list_mobile_holi = []

list_tweets_work = []
list_tweets_holi = []
for i in range(0, 365):
    if i % 7 == 0:
        list_mobile_work.append(mobile[i].tolist())
        list_tweets_work.append(tweets[i].tolist())
    if i % 7 == 1:
        list_mobile_holi.append(mobile[i].tolist())
        list_tweets_holi.append(tweets[i].tolist())
    if i % 7 == 2:
        list_mobile_holi.append(mobile[i].tolist())
        list_tweets_holi.append(tweets[i].tolist())
    if i % 7 == 3:
        list_mobile_work.append(mobile[i].tolist())
        list_tweets_work.append(tweets[i].tolist())
    if i % 7 == 4:
        list_mobile_work.append(mobile[i].tolist())
        list_tweets_work.append(tweets[i].tolist())
    if i % 7 == 5:
        list_mobile_work.append(mobile[i].tolist())
        list_tweets_work.append(tweets[i].tolist())
    if i % 7 == 6:
        list_mobile_work.append(mobile[i].tolist())
        list_tweets_work.append(tweets[i].tolist())

list_mobile_work = np.array(list_mobile_work)
list_tweets_work = np.array(list_tweets_work)

list_mobile_holi = np.array(list_mobile_holi)
list_tweets_holi = np.array(list_tweets_holi)



df_work = pd.DataFrame(
    data=np.stack([list_tweets_work, list_mobile_work]).T,
    columns=["Tweets_num", "Population"],
)
df_holi = pd.DataFrame(
    data=np.stack([list_tweets_holi, list_mobile_holi]).T,
    columns=["Tweets_num", "Population"],
)

fig = plt.figure(figsize=(20, 25))
fig.suptitle(name_key, fontsize=16)
ax1_1 = fig.add_subplot(2, 1, 1)
ax1_2 = fig.add_subplot(2, 1, 2)

# x_axis = []
# for i in range(0, max(df_asa['Tweets_num'])+1):
#     x_axis.append(i)

X = list_mobile_work.reshape(-1, 1)
y = list_tweets_work.reshape(-1, 1)
mi_work = mutual_info_regression(X, y)

X = list_mobile_holi.reshape(-1, 1)
y = list_tweets_holi.reshape(-1, 1)
mi_holi = mutual_info_regression(X, y)


#Fri
for i in range(0, max(df_work['Tweets_num'])):
    if not max(df_work['Tweets_num']==i):
        df_work = pd.concat([df_work, pd.DataFrame([[i,np.nan]],columns=['Tweets_num', 'Population'])])
sns.scatterplot(x="Tweets_num", y="Population", data=df_work, ax=ax1_1)

if max(df_work['Tweets_num']) >40:
    ax1_1.set_xticklabels(ax1_1.get_xticklabels(),rotation = 90)
# x_axis = []
# for i in range(0, max(df_work["Tweets_num"]) + 1):
#     x_axis.append(i)
# a, b = np.polyfit(list_tweets_work, list_mobile_work, 1)
# y2 = a * np.array(x_axis) + b
# df2glaph = pd.DataFrame(
#     np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
# )
# sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_1)

#Sat
for i in range(0, max(df_holi['Tweets_num'])):
    if not max(df_holi['Tweets_num']==i):
        df_holi = pd.concat([df_holi, pd.DataFrame([[i,np.nan]],columns=['Tweets_num', 'Population'])])
sns.scatterplot(x="Tweets_num", y="Population", data=df_holi, ax=ax1_2)





ax1_1.set_title("Workday MI={:.2f}".format(mi_work[0]), fontsize=16)
ax1_2.set_title("Holiday MI={:.2f}".format(mi_holi[0]), fontsize=16)


save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/box/perDay/Work_Holi"
    + name_key
    + ".png"
)
fig.savefig(save_PATH)
