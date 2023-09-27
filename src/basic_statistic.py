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

Tokyo_station_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/numpy_array/Tokyostation.npy"
Tokyo_station_tweets_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/numpy_array/Tokyostaion.npy"

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
    Tokyo_station_mobile_PATH,
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
    Tokyo_station_mobile_PATH,
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
    "Tokyo station",
    "Arashiyama",
    "Karasuma",
    "Kinkaku_tmple",
    "Kiyomizu_temple",
    "Kyoto University",
    "Nizyou",
    "Touzi",
    "Kyoto station",
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
            int(np.mean(tweets)),int(np.median(tweets)),int(np.sum(tweets)),int(np.var(tweets,ddof=1)),int(np.std(tweets,ddof=1)),int(np.max(tweets)),int(np.min(tweets)),int(np.percentile(tweets, 25)),int(np.percentile(tweets, 75)),
            float(np.median(tweets)/np.median(mobile))])
    data.append(tmp)
columns=['ソーシャルセンサ性能','p値',
         '人口平均','人口中央値','人口合計','人口分散','人口標準偏差','人口最大値','人口最小値','人口四分位点(25%)','人口四分位点(75%)',
         '発言者数平均','発言者数中央値','発言者数合計','発言者数分散','発言者数標準偏差','発言者数最大値','発言者数最小値','発言者数四分位点(25%)','発言者数四分位点(75%)','発言者数中央値/人口中央値']

df= pd.DataFrame(data,index=list_key,columns=columns)
df.to_csv('/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/統計/ソーシャルセンサ性能.csv')



r_r = []
for i in columns:
    corr, pvalue = stats.pearsonr(df['ソーシャルセンサ性能'], df[i])
    r_r.append([corr, pvalue])
df_r = pd.DataFrame(r_r,index=columns, columns=['相関係数','p値'])
df_r.to_csv('/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/統計/ソーシャルセンサ性能との相関.csv')
