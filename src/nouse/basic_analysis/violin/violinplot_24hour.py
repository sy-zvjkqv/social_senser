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
list_twitter = [
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
    tweets = np.load(list_twitter[i])
    name_key = list_key[i]

    mobile_asa = mobile[:, 0:7]
    mobile_hiru = mobile[:, 8:15]
    mobile_ban = mobile[:, 16:23]

    tweets_asa = tweets[:, 0:7]
    tweets_hiru = tweets[:, 8:15]
    tweets_ban = tweets[:, 16:23]

    mobile_asa_flatten = mobile_asa.flatten()
    tweets_asa_flatten = tweets_asa.flatten()
    mobile_hiru_flatten = mobile_hiru.flatten()
    tweets_hiru_flatten = tweets_hiru.flatten()
    mobile_ban_flatten = mobile_ban.flatten()
    tweets_ban_flatten = tweets_ban.flatten()

    df_asa = pd.DataFrame(
        data=np.stack([tweets_asa_flatten, mobile_asa_flatten]).T,
        columns=["Tweets_num", "Population"],
    )
    df_hiru = pd.DataFrame(
        data=np.stack([tweets_hiru_flatten, mobile_hiru_flatten]).T,
        columns=["Tweets_num", "Population"],
    )
    df_ban = pd.DataFrame(
        data=np.stack([tweets_ban_flatten, mobile_ban_flatten]).T,
        columns=["Tweets_num", "Population"],
    )

    fig = plt.figure(figsize=(20, 16))
    fig.suptitle(name_key, fontsize=16)
    ax1_1 = fig.add_subplot(3, 1, 1)
    ax1_2 = fig.add_subplot(3, 1, 2)
    ax1_3 = fig.add_subplot(3, 1, 3)

    # x_axis = []
    # for i in range(0, max(df_asa['Tweets_num'])+1):
    #     x_axis.append(i)

    X = mobile_asa_flatten.reshape(-1, 1)
    y = tweets_asa_flatten.reshape(-1, 1)
    mi_asa = mutual_info_regression(X, y)

    X = mobile_hiru_flatten.reshape(-1, 1)
    y = tweets_hiru_flatten.reshape(-1, 1)
    mi_hiru = mutual_info_regression(X, y)

    X = mobile_ban_flatten.reshape(-1, 1)
    y = tweets_ban_flatten.reshape(-1, 1)
    mi_ban = mutual_info_regression(X, y)

    plt.figure(figsize=(15, 10))
    sns.violinplot(x="Tweets_num", y="Population", data=df_asa, ax=ax1_1)
    sns.violinplot(x="Tweets_num", y="Population", data=df_hiru, ax=ax1_2)
    sns.violinplot(x="Tweets_num", y="Population", data=df_ban, ax=ax1_3)
    ax1_1.set_title("morning MI={:.2f}".format(mi_asa[0]), fontsize=16)
    ax1_2.set_title("noon MI={:.2f}".format(mi_hiru[0]), fontsize=16)
    ax1_3.set_title("evening MI={:.2f}".format(mi_ban[0]), fontsize=16)

    save_PATH = (
        "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/violin/24hour/"
        + name_key
        + ".png"
    )
    fig.savefig(save_PATH)
