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
Tokyo_station_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Tokyostation/Tokyostation_2021.npy"
Tokyo_station_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Tokyostation_2021/outlier/Tokyostation_3zi_2021.npy"

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
    Tokyo_station_mobile_PATH,
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
    Tokyo_station_tweets_PATH,
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
    "東京駅",
    "嵐山",
    "中京区",
    "金閣寺",
    "清水寺",
    "学生街",
    "二条城",
    "東寺",
    "京都駅",
]

data = []
for i in range(0, len(list_mobile)):
    mobile = np.load(list_mobile[i])
    tweets = np.load(list_twitter[i])
    mobile = np.sum(mobile, axis=1)
    tweets = np.sum(tweets, axis=1)
    correlation, p_value = stats.pearsonr(mobile, tweets)


    tmp = ([correlation, p_value,
            int(np.mean(mobile)),int(np.median(mobile)),int(np.sum(mobile)),int(np.var(mobile,ddof=1)),int(np.std(mobile,ddof=1)),int(np.max(mobile)),int(np.min(mobile)),int(np.percentile(mobile, 25)),int(np.percentile(mobile, 75)),
            int(np.mean(tweets)),int(np.median(tweets)),int(np.sum(tweets)),int(np.var(tweets,ddof=1)),int(np.std(tweets,ddof=1)),int(np.max(tweets)),int(np.min(tweets)),int(np.percentile(tweets, 25)),int(np.percentile(tweets, 75))])
    data.append(tmp)
columns=['相関係数','p値',
         '人口平均','人口中央値','人口合計','人口分散','人口標準偏差','人口最大値','人口最小値','人口四分位点(25%)','人口四分位点(75%)',
         '発言者数平均','発言者数中央値','発言者数合計','発言者数分散','発言者数標準偏差','発言者数最大値','発言者数最小値','発言者数四分位点(25%)','発言者数四分位点(75%)']

df= pd.DataFrame(data,index=list_key,columns=columns)
df.to_csv('tmp.csv')