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
            key = int("22" + month + day + hour)
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

    X = mobile_0to3_flatten.reshape(-1, 1)
    y = tweets_0to3_flatten.reshape(-1, 1)
    mi_0to3 = mutual_info_regression(X, y)

    X = mobile_4to6_flatten.reshape(-1, 1)
    y = tweets_4to6_flatten.reshape(-1, 1)
    mi_4to6 = mutual_info_regression(X, y)

    X = mobile_7to9_flatten.reshape(-1, 1)
    y = tweets_7to9_flatten.reshape(-1, 1)
    mi_7to9 = mutual_info_regression(X, y)

    X = mobile_10to12_flatten.reshape(-1, 1)
    y = tweets_10to12_flatten.reshape(-1, 1)
    mi_10to12 = mutual_info_regression(X, y)

    X = mobile_13to15_flatten.reshape(-1, 1)
    y = tweets_13to15_flatten.reshape(-1, 1)
    mi_13to15 = mutual_info_regression(X, y)

    X = mobile_16to18_flatten.reshape(-1, 1)
    y = tweets_16to18_flatten.reshape(-1, 1)
    mi_16to18 = mutual_info_regression(X, y)

    X = mobile_19to21_flatten.reshape(-1, 1)
    y = tweets_19to21_flatten.reshape(-1, 1)
    mi_19to21 = mutual_info_regression(X, y)

    X = mobile_22to24_flatten.reshape(-1, 1)
    y = tweets_22to24_flatten.reshape(-1, 1)
    mi_22to24 = mutual_info_regression(X, y)

    plt.figure(figsize=(15, 10))
    for i in range(0, max(df_0to3["Tweets_num"])):
        if not max(df_0to3["Tweets_num"] == i):
            df_0to3 = pd.concat(
                [
                    df_0to3,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_0to3, ax=ax1_1, whis=100)

    for i in range(0, max(df_4to6["Tweets_num"])):
        if not max(df_4to6["Tweets_num"] == i):
            df_4to6 = pd.concat(
                [
                    df_4to6,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )

    sns.boxplot(x="Tweets_num", y="Population", data=df_4to6, ax=ax1_2, whis=100)

    for i in range(0, max(df_7to9["Tweets_num"])):
        if not max(df_7to9["Tweets_num"] == i):
            df_7to9 = pd.concat(
                [
                    df_7to9,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_7to9, ax=ax2_1, whis=100)

    for i in range(0, max(df_10to12["Tweets_num"])):
        if not max(df_10to12["Tweets_num"] == i):
            df_10to12 = pd.concat(
                [
                    df_10to12,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_10to12, ax=ax2_2, whis=100)

    for i in range(0, max(df_13to15["Tweets_num"])):
        if not max(df_13to15["Tweets_num"] == i):
            df_13to15 = pd.concat(
                [
                    df_13to15,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_13to15, ax=ax3_1, whis=100)

    for i in range(0, max(df_16to18["Tweets_num"])):
        if not max(df_16to18["Tweets_num"] == i):
            df_16to18 = pd.concat(
                [
                    df_16to18,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_16to18, ax=ax3_2, whis=100)

    for i in range(0, max(df_19to21["Tweets_num"])):
        if not max(df_19to21["Tweets_num"] == i):
            df_19to21 = pd.concat(
                [
                    df_19to21,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_19to21, ax=ax4_1, whis=100)

    for i in range(0, max(df_22to24["Tweets_num"])):
        if not max(df_22to24["Tweets_num"] == i):
            df_22to24 = pd.concat(
                [
                    df_22to24,
                    pd.DataFrame([[i, np.nan]], columns=["Tweets_num", "Population"]),
                ]
            )
    sns.boxplot(x="Tweets_num", y="Population", data=df_22to24, ax=ax4_2, whis=100)

    ax1_1.set_title("0to3 MI={:.2f}".format(mi_0to3[0]), fontsize=16)
    ax1_2.set_title("4to6 MI={:.2f}".format(mi_4to6[0]), fontsize=16)
    ax2_1.set_title("7to9 MI={:.2f}".format(mi_7to9[0]), fontsize=16)
    ax2_2.set_title("10to12 MI={:.2f}".format(mi_10to12[0]), fontsize=16)
    ax3_1.set_title("13to15 MI={:.2f}".format(mi_13to15[0]), fontsize=16)
    ax3_2.set_title("16to18 MI={:.2f}".format(mi_16to18[0]), fontsize=16)
    ax4_1.set_title("19to21 MI={:.2f}".format(mi_19to21[0]), fontsize=16)
    ax4_2.set_title("222to24 MI={:.2f}".format(mi_22to24[0]), fontsize=16)

    ax1_1.set_xticklabels(ax1_1.get_xticklabels(), rotation=90)
    ax1_2.set_xticklabels(ax1_2.get_xticklabels(), rotation=90)
    ax2_1.set_xticklabels(ax2_1.get_xticklabels(), rotation=90)
    ax2_2.set_xticklabels(ax2_2.get_xticklabels(), rotation=90)
    ax3_1.set_xticklabels(ax3_1.get_xticklabels(), rotation=90)
    ax3_2.set_xticklabels(ax3_2.get_xticklabels(), rotation=90)
    ax4_1.set_xticklabels(ax4_1.get_xticklabels(), rotation=90)
    ax4_2.set_xticklabels(ax4_2.get_xticklabels(), rotation=90)

    save_PATH = (
        "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/box/24hour/"
        + name_key
        + ".png"
    )
    fig.savefig(save_PATH)
