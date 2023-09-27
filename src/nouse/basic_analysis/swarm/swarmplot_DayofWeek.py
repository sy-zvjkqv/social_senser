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

Kyoto_station_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kyotostation.npy"
Kyoto_station_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kyotostation_users.npy"

Arashi_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Arashiyama_3zi_2022.npy"
Arashi_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Arashiyama_users.npy"

High_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Highclass_3zi_2022.npy"
High_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Highclass_users.npy"

Kinkaku_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kinkaku_3zi_2022.npy"
Kinkaku_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kinkaku_users.npy"

Kiyomizu_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kiyomizu_3zi_2022.npy"
Kiyomizu_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kiyomizu_users.npy"

Lowclass_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Lowclass_3zi_2022.npy"
Lowclass_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Lowclass_users.npy"

Nizyou_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Nizyou_3zi_2022.npy"
Nizyou_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Nizyou_users.npy"

Touzi_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Touzi_3zi_2022.npy"
Touzi_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Touzi_users.npy"

list_mobile = [
    Arashi_mobile_PATH,
    High_mobile_PATH,
    Kinkaku_mobile_PATH,
    Kiyomizu_mobile_PATH,
    Lowclass_mobile_PATH,
    Nizyou_mobile_PATH,
    Touzi_mobile_PATH,
    Kyoto_station_mobile_PATH,
]
list_tweets = [
    Arashi_tweets_PATH,
    High_tweets_PATH,
    Kinkaku_tweets_PATH,
    Kiyomizu_tweets_PATH,
    Lowclass_tweets_PATH,
    Nizyou_tweets_PATH,
    Touzi_tweets_PATH,
    Kyoto_station_tweets_PATH,
]
list_key = [
    "Arashiyama",
    "High_class",
    "Kinkaku_tmple",
    "Kiyomizu_temple",
    "middle_class",
    "Nizyou",
    "Touzi",
    "Kyotostation",
]

for i in range(0, len(list_mobile)):
    mobile = np.load(list_mobile[i])
    tweets = np.load(list_tweets[i])
    name_key = list_key[i]

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
    sns.stripplot(x="Tweets_num", y="Population", data=df_Fri, ax=ax1_1)
    x_axis = []
    for i in range(0, max(df_Fri["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Fri, list_mobile_Fri, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_1)

    # Sat
    sns.stripplot(x="Tweets_num", y="Population", data=df_Sat, ax=ax1_2)
    x_axis = []
    for i in range(0, max(df_Sat["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Sat, list_mobile_Sat, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_2)

    # Sun
    sns.stripplot(x="Tweets_num", y="Population", data=df_Sun, ax=ax1_3)
    x_axis = []
    for i in range(0, max(df_Sun["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Sun, list_mobile_Sun, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_3)

    # Mon
    sns.stripplot(x="Tweets_num", y="Population", data=df_Mon, ax=ax1_4)
    x_axis = []
    for i in range(0, max(df_Mon["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Mon, list_mobile_Mon, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_4)

    # Tue
    sns.stripplot(x="Tweets_num", y="Population", data=df_Tue, ax=ax1_5)
    x_axis = []
    for i in range(0, max(df_Thu["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Thu, list_mobile_Thu, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_5)

    # Wed
    sns.stripplot(x="Tweets_num", y="Population", data=df_Wed, ax=ax1_6)
    x_axis = []
    for i in range(0, max(df_Wed["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Wed, list_mobile_Wed, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_6)

    # Thu
    sns.stripplot(x="Tweets_num", y="Population", data=df_Thu, ax=ax1_7)
    x_axis = []
    for i in range(0, max(df_Thu["Tweets_num"]) + 1):
        x_axis.append(i)
    a, b = np.polyfit(list_tweets_Thu, list_mobile_Thu, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(
        np.stack((x_axis, y2)).T, columns=["Tweets_num", "Population"]
    )
    sns.regplot(x="Tweets_num", y="Population", data=df2glaph, ax=ax1_7)

    ax1_1.set_title("Fri MI={:.2f}".format(mi_Fri[0]), fontsize=16)
    ax1_2.set_title("Sat MI={:.2f}".format(mi_Sat[0]), fontsize=16)
    ax1_3.set_title("Sun MI={:.2f}".format(mi_Sun[0]), fontsize=16)
    ax1_4.set_title("Mon MI={:.2f}".format(mi_Mon[0]), fontsize=16)
    ax1_5.set_title("Tue MI={:.2f}".format(mi_Tue[0]), fontsize=16)
    ax1_6.set_title("Wed MI={:.2f}".format(mi_Wed[0]), fontsize=16)
    ax1_7.set_title("Thu MI={:.2f}".format(mi_Thu[0]), fontsize=16)

    save_PATH = (
        "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/swarm/DayofWeek/"
        + name_key
        + ".png"
    )
    fig.savefig(save_PATH)
