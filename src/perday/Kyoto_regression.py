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
            key = int("22" + month + day + hour)
            key = str(key)
            x_label.append(key)

Kyoto_station_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Kyotostation.npy"
Kyoto_station_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Kyotostation.npy"

Arashi_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Arashiyama.npy"
Arashi_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Arashiyama.npy"

Karasuma_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Karasuma.npy"
Karasuma_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Karasuma.npy"

Kinkaku_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Kinkaku.npy"
Kinkaku_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Kinkaku.npy"

Kiyomizu_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Kiyomizu.npy"
Kiyomizu_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Kiyomizu.npy"

University_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/University.npy"
University_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/University.npy"

Nizyou_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Nizyou.npy"
Nizyou_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Nizyou.npy"

Touzi_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Touzi.npy"
Touzi_tweets_PATH = "//home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Touzi.npy"

list_mobile = [
    Arashi_mobile_PATH,
    Karasuma_mobile_PATH,
    Kinkaku_mobile_PATH,
    Kiyomizu_mobile_PATH,
    University_mobile_PATH,
    Nizyou_mobile_PATH,
    Touzi_mobile_PATH,
    Kyoto_station_mobile_PATH,
]
list_twitter = [
    Arashi_tweets_PATH,
    Karasuma_tweets_PATH,
    Kinkaku_tweets_PATH,
    Kiyomizu_tweets_PATH,
    University_tweets_PATH,
    Nizyou_tweets_PATH,
    Touzi_tweets_PATH,
    Kyoto_station_tweets_PATH,
]
list_key = [
    "Arashiyama",
    "Karasuma",
    "Kinkaku_tmple",
    "Kiyomizu_temple",
    "Kyoto University",
    "Nizyou",
    "Touzi",
    "Kyotostation",
]

for i in range(0, len(list_mobile)):
    mobile = np.load(list_mobile[i])
    tweets = np.load(list_twitter[i])
    name_key = list_key[i]

    mobile = np.sum(mobile, axis=1)
    tweets = np.sum(tweets, axis=1)

    list_Week_of_Day = []
    for i in range(0, 365):
        if i % 7 == 0:
            list_Week_of_Day.append("Holiday")
        if i % 7 == 1:
            list_Week_of_Day.append("Holiday")
        if i % 7 == 2:
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
        columns=["The number of people", "The number of Twets", "Week_of_Day"],
    )
    df["The number of Twets"] = df["The number of Twets"].astype(float)
    df["The number of people"] = df["The number of people"].astype(float)

    fig = plt.figure(figsize=(20, 25))
    # fig.suptitle(name_key, fontsize=16)



    X = mobile
    y = tweets
    fig = sns.lmplot(x="The number of Twets", y="The number of people", data=df, ci=None, legend=True)
    correlation, p_value = stats.pearsonr(X, y)


    # テキストを図の上に追加
    ax = plt.gca()
    ax.text(0.65, 0.9, 'social sensor performance \n: {:.2f}'.format(correlation), transform=ax.transAxes,
            fontsize=9, verticalalignment='top')
    plt.show()


    save_PATH = (
        "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/perday/"
        + name_key
        + ".png"
    )
    fig.savefig(save_PATH)
