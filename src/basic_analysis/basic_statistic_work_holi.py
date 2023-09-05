import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
from matplotlib import mlab
from scipy import signal, stats
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.linear_model import LinearRegression
from datetime import datetime
from datetime import timedelta
import jpholiday
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

def isBizDay(DATE):
    # DATE = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))
    if DATE.weekday() >= 5 or jpholiday.is_holiday(DATE):
        return "Holiday"
    else:
        return "Workday"

#基本統計量データ算出
data = []
#各地域のデータ読み込み
data_work = []
data_holi = []
for i in range(0, len(list_mobile)):
    mobile = np.load(list_mobile[i])
    tweets = np.load(list_twitter[i])
    mobile = np.sum(mobile, axis=1)
    tweets = np.sum(tweets, axis=1)
    #平日と休日でデータを分けるただし東京のみ年度が違うので分ける


    if i ==0:
        start_date = datetime(2021,1,1)
        mobile_work = []
        mobile_holi = []
        tweets_work = []
        tweets_holi = []
        for j in range(0, 365):
            Today = start_date + timedelta(days=j)
            # Today = str(format(Today, '%Y%m%d'))
            # print(Today)
            work_holi_Flag = isBizDay(Today)
            if (
                j == 0
                or j == 1
                or j == 2
                or j == 362
                or j == 363
                or j == 364
            ):
                mobile_holi.append(mobile[j])
                tweets_holi.append(tweets[j])
            elif (work_holi_Flag == "Holiday"):
                mobile_holi.append(mobile[j])
                tweets_holi.append(tweets[j])
            else:
                mobile_work.append(mobile[j])
                tweets_work.append(tweets[j])
        correlation_work, p_value_work = stats.pearsonr(mobile_work, tweets_work)
        correlation_holi, p_value_holi = stats.pearsonr(mobile_holi, tweets_holi)



        tmp_work = ([correlation_work, p_value_work,
                    int(np.mean(mobile_work)),int(np.median(mobile_work)),int(np.sum(mobile_work)),int(np.var(mobile_work,ddof=1)),int(np.max(mobile_work)),int(np.min(mobile_work)),
                    int(np.mean(tweets_work)),int(np.median(tweets_work)),int(np.sum(tweets_work)),int(np.var(tweets_work,ddof=1)),int(np.max(tweets_work)),int(np.min(tweets_work)),
                    float(np.median(tweets_work)/np.median(mobile_work))])
        data_work.append(tmp_work)

        tmp_holi = ([correlation_holi, p_value_holi,
                    int(np.mean(mobile_holi)),int(np.median(mobile_holi)),int(np.sum(mobile_holi)),int(np.var(mobile_holi,ddof=1)),int(np.max(mobile_holi)),int(np.min(mobile_holi)),
                    int(np.mean(tweets_holi)),int(np.median(tweets_holi)),int(np.sum(tweets_holi)),int(np.var(tweets_holi,ddof=1)),int(np.max(tweets_holi)),int(np.min(tweets_holi)),
                    float(np.median(tweets_holi)/np.median(mobile_holi))])
        data_holi.append(tmp_holi)

    else:
        start_date = datetime(2022,1,1)
        mobile_work = []
        mobile_holi = []
        tweets_work = []
        tweets_holi = []
        for j in range(0, 365):
            Today = start_date + timedelta(days=j)
            # Today = str(format(Today, '%Y%m%d'))
            # print(Today)
            work_holi_Flag = isBizDay(Today)
            if (
                j == 0
                or j == 1
                or j == 2
                or j == 362
                or j == 363
                or j == 364
            ):
                mobile_holi.append(mobile[j])
                tweets_holi.append(tweets[j])
            elif (work_holi_Flag == "Holiday"):
                mobile_holi.append(mobile[j])
                tweets_holi.append(tweets[j])
            else:
                mobile_work.append(mobile[j])
                tweets_work.append(tweets[j])
        correlation_work, p_value_work = stats.pearsonr(mobile_work, tweets_work)
        correlation_holi, p_value_holi = stats.pearsonr(mobile_holi, tweets_holi)



        tmp_work = ([correlation_work, p_value_work,
                    int(np.mean(mobile_work)),int(np.median(mobile_work)),int(np.sum(mobile_work)),int(np.var(mobile_work,ddof=1)),int(np.max(mobile_work)),int(np.min(mobile_work)),
                    int(np.mean(tweets_work)),int(np.median(tweets_work)),int(np.sum(tweets_work)),int(np.var(tweets_work,ddof=1)),int(np.max(tweets_work)),int(np.min(tweets_work)),
                    float(np.median(tweets_work)/np.median(mobile_work))])
        data_work.append(tmp_work)

        tmp_holi = ([correlation_holi, p_value_holi,
                    int(np.mean(mobile_holi)),int(np.median(mobile_holi)),int(np.sum(mobile_holi)),int(np.var(mobile_holi,ddof=1)),int(np.max(mobile_holi)),int(np.min(mobile_holi)),
                    int(np.mean(tweets_holi)),int(np.median(tweets_holi)),int(np.sum(tweets_holi)),int(np.var(tweets_holi,ddof=1)),int(np.max(tweets_holi)),int(np.min(tweets_holi)),
                    float(np.median(tweets_holi)/np.median(mobile_holi))])
        data_holi.append(tmp_holi)






columns_work=['ソーシャルセンサ性能(平日)','p値(平日)',
         '人口平均(平日)','人口中央値(平日)','人口合計(平日)','人口分散(平日)','人口最大値(平日)','人口最小値(平日)',
         '発言者数平均(平日)','発言者数中央値(平日)','発言者数合計(平日)','発言者数分散(平日)','発言者数最大値(平日)','発言者数最小値(平日)','発言者数中央値/人口中央値(平日)']

columns_holi=['ソーシャルセンサ性能(休日)','p値(休日)',
         '人口平均(休日)','人口中央値(休日)','人口合計(休日)','人口分散(休日)','人口最大値(休日)','人口最小値(休日)',
         '発言者数平均(休日)','発言者数中央値(休日)','発言者数合計(休日)','発言者数分散(休日)','発言者数最大値(休日)','発言者数最小値(休日)','発言者数中央値/人口中央値(休日)']

df_work= pd.DataFrame(data_work,index=list_key,columns=columns_work)
df_work.to_csv('/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/consideration/基本統計量_work.csv')

df_holi= pd.DataFrame(data_holi,index=list_key,columns=columns_holi)
df_holi.to_csv('/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/consideration/基本統計量_holi.csv')


# r_r = []
# for i in columns:
#     corr, pvalue = stats.pearsonr(df['相関係数'], df[i])
#     r_r.append([corr, pvalue])
# df_r = pd.DataFrame(r_r,index=columns, columns=['順位相関係数','p値'])
# df_r.to_csv('相関.csv')
