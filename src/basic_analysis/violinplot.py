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

day_list_long = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
day_list_short = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
day_list_Feb = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
hour_list = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
x_label = []
for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
    if month in ['01', '03', '05', '07', '08','10', '12']:
        day_list = day_list_long
    elif month == '02':
        day_list = day_list_Feb
    else:
        day_list = day_list_short
    for day in day_list:
        for hour in range(0,24):
            hour = str(hour)
            key = int('21'+ month + day + hour)
            key = str(key)
            x_label.append(key)

Kyoto_station_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kyotostation.npy'
Kyoto_station_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kyotostation_users.npy'

Arashi_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Arashiyama_3zi_2022.npy'
Arashi_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Arashiyama_users.npy'

High_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Highclass_3zi_2022.npy'
High_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Highclass_users.npy'

Kinkaku_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kinkaku_3zi_2022.npy'
Kinkaku_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kinkaku_users.npy'

Kiyomizu_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kiyomizu_3zi_2022.npy'
Kiyomizu_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kiyomizu_users.npy'

Lowclass_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Lowclass_3zi_2022.npy'
Lowclass_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Lowclass_users.npy'

Nizyou_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Nizyou_3zi_2022.npy'
Nizyou_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Nizyou_users.npy'

Touzi_mobile_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Touzi_3zi_2022.npy'
Touzi_tweets_PATH = '/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Touzi_users.npy'

list_mobile = [Arashi_mobile_PATH, High_mobile_PATH, Kinkaku_mobile_PATH, Kiyomizu_mobile_PATH, Lowclass_mobile_PATH, Nizyou_mobile_PATH, Touzi_mobile_PATH, Kyoto_station_mobile_PATH]
list_twitter = [Arashi_tweets_PATH, High_tweets_PATH, Kinkaku_tweets_PATH, Kiyomizu_tweets_PATH, Lowclass_tweets_PATH, Nizyou_tweets_PATH, Touzi_tweets_PATH, Kyoto_station_tweets_PATH]
list_key = ['Arashiyama','High_class','Kinkaku_tmple','Kiyomizu_temple','middle_class','Nizyou','Touzi','Kyotostation']

for i in range(0, len(list_mobile)):
    mobile = np.load(list_mobile[i])
    tweets = np.load(list_twitter[i])
    name_key = list_key[i]
    mobile_flatten = mobile.flatten()
    tweets_flatten = tweets.flatten()

    tmp = np.stack([tweets_flatten, mobile_flatten])
    df_mobile_tweets = pd.DataFrame(data = tmp.T, columns=['Tweets_num', 'Population'])


    x_axis = []
    for i in range(0, max(df_mobile_tweets['Tweets_num'])+1):
        x_axis.append(i)


    a, b = np.polyfit(tweets_flatten, mobile_flatten, 1)
    y2 = a * np.array(x_axis) + b
    df2glaph = pd.DataFrame(np.stack((x_axis, y2)).T, columns=['Tweets_num', 'Population'])

    X = mobile_flatten.reshape(-1,1)
    y = tweets_flatten.reshape(-1,1)
    a, b = np.polyfit(X[:,0], y, 1)
    mi = mutual_info_regression(X, y)
    f_test, _ = f_regression(X, y)
    #フィッティング直線

    plt.figure(figsize=(15, 10))
    sns.violinplot(x='Tweets_num', y='Population', data=df_mobile_tweets)
    sns.regplot(x='Tweets_num', y='Population', data=df2glaph)
    #plt.xticks(x_axis, x_axis)
    plt.xlabel('Number of Tweets')
    plt.ylabel('Populations')
    plt.title("{} MI={:.2f}".format(name_key, mi[0]), fontsize=16)

    save_PATH = (
        "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/violin/"
        + name_key
        + ".png"
    )
    plt.savefig(save_PATH)