import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Kyoto_station_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kyotostation.npy"
Kyoto_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kyotostation_users.npy"

Arashi_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Arashiyama_3zi_2022.npy"
Arashi_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Arashiyama_users.npy"

High_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Highclass_3zi_2022.npy"
High_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Highclass_users.npy"

Kinkaku_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kinkaku_3zi_2022.npy"
Kinkaku_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kinkaku_users.npy"

Kiyomizu_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kiyomizu_3zi_2022.npy"
Kiyomizu_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Kiyomizu_users.npy"

Lowclass_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Lowclass_3zi_2022.npy"
Lowclass_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Lowclass_users.npy"

Nizyou_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Nizyou_3zi_2022.npy"
Nizyou_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Nizyou_users.npy"

Touzi_mobile_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Touzi_3zi_2022.npy"
Touzi_users_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/users/Touzi_users.npy"

list_mobile = [
    Arashi_mobile_PATH,
    High_mobile_PATH,
    Kinkaku_mobile_PATH,
    Kiyomizu_mobile_PATH,
    Lowclass_mobile_PATH,
    Nizyou_mobile_PATH,
    Touzi_mobile_PATH,
]
list_users = [
    Arashi_users_PATH,
    High_users_PATH,
    Kinkaku_users_PATH,
    Kiyomizu_users_PATH,
    Lowclass_users_PATH,
    Nizyou_users_PATH,
    Touzi_users_PATH,
    Kyoto_users_PATH,
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
    twitter = np.load(list_users[i])
    key = list_key[i]

    prob = twitter / mobile

    mobile_perhour = np.sum(mobile, axis=0)
    twitter_perhour = np.sum(twitter, axis=0)
    prob_perhour = np.sum(prob, axis=0)

    mobile_perday = np.sum(mobile, axis=1)
    twitter_perday = np.sum(twitter, axis=1)
    prob_perday = np.sum(prob, axis=1)

    list_mobile_Sun = []
    list_mobile_Mon = []
    list_mobile_Tue = []
    list_mobile_Wed = []
    list_mobile_Thu = []
    list_mobile_Fri = []
    list_mobile_Sat = []

    list_twitter_Sun = []
    list_twitter_Mon = []
    list_twitter_Tue = []
    list_twitter_Wed = []
    list_twitter_Thu = []
    list_twitter_Fri = []
    list_twitter_Sat = []

    list_prob_Sun = []
    list_prob_Mon = []
    list_prob_Tue = []
    list_prob_Wed = []
    list_prob_Thu = []
    list_prob_Fri = []
    list_prob_Sat = []

    for i in range(0, 365):
        if i % 7 == 6:
            list_mobile_Fri.append(mobile[i].tolist())
            list_twitter_Fri.append(twitter[i].tolist())
            list_prob_Fri.append(prob[i].tolist())
        if i % 7 == 0:
            list_mobile_Sat.append(mobile[i].tolist())
            list_twitter_Sat.append(twitter[i].tolist())
            list_prob_Sat.append(prob[i].tolist())
        if i % 7 == 1:
            list_mobile_Sun.append(mobile[i].tolist())
            list_twitter_Sun.append(twitter[i].tolist())
            list_prob_Sun.append(prob[i].tolist())
        if i % 7 == 2:
            list_mobile_Mon.append(mobile[i].tolist())
            list_twitter_Mon.append(twitter[i].tolist())
            list_prob_Mon.append(prob[i].tolist())
        if i % 7 == 3:
            list_mobile_Tue.append(mobile[i].tolist())
            list_twitter_Tue.append(twitter[i].tolist())
            list_prob_Tue.append(prob[i].tolist())
        if i % 7 == 4:
            list_mobile_Wed.append(mobile[i].tolist())
            list_twitter_Wed.append(twitter[i].tolist())
            list_prob_Wed.append(prob[i].tolist())
        if i % 7 == 5:
            list_mobile_Thu.append(mobile[i].tolist())
            list_twitter_Thu.append(twitter[i].tolist())
            list_prob_Thu.append(prob[i].tolist())

    mobile_perdays = [
        np.average(list_mobile_Sun),
        np.average(list_mobile_Mon),
        np.average(list_mobile_Tue),
        np.average(list_mobile_Wed),
        np.average(list_mobile_Tue),
        np.average(list_mobile_Fri),
        np.average(list_mobile_Sat),
    ]

    twitter_perdays = [
        np.average(list_twitter_Sun),
        np.average(list_twitter_Mon),
        np.average(list_twitter_Tue),
        np.average(list_twitter_Wed),
        np.average(list_twitter_Tue),
        np.average(list_twitter_Fri),
        np.average(list_twitter_Sat),
    ]

    prob_perdays = [
        np.average(list_prob_Sun),
        np.average(list_prob_Mon),
        np.average(list_prob_Tue),
        np.average(list_prob_Wed),
        np.average(list_prob_Tue),
        np.average(list_prob_Fri),
        np.average(list_prob_Sat),
    ]

    x_label_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    fig = plt.figure(figsize=(20, 16))
    fig.suptitle(key)
    ax1_1 = fig.add_subplot(3, 3, 1)
    ax1_2 = fig.add_subplot(3, 3, 2)
    ax1_3 = fig.add_subplot(3, 3, 3)
    ax2_1 = fig.add_subplot(3, 3, 4)
    ax2_2 = fig.add_subplot(3, 3, 5)
    ax2_3 = fig.add_subplot(3, 3, 6)
    ax3_1 = fig.add_subplot(3, 3, 7)
    ax3_2 = fig.add_subplot(3, 3, 8)
    ax3_3 = fig.add_subplot(3, 3, 9)

    ax1_1.set_title("population day")
    ax1_2.set_title("twitter users day")
    ax1_3.set_title("prob day")
    ax2_1.set_title("population hour")
    ax2_2.set_title("twitter users hour")
    ax2_3.set_title("prob hour")
    ax3_1.set_title("population day of week")
    ax3_2.set_title("twitter users day of week")
    ax3_3.set_title("prob day of week")

    ax1_1.set_xticks(
        [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    )
    ax1_2.set_xticks(
        [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    )
    ax1_3.set_xticks(
        [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    )

    ax1_1.set_xlabel("month")
    ax1_2.set_xlabel("month")
    ax1_3.set_xlabel("month")

    ax2_1.set_xlabel("hour")
    ax2_2.set_xlabel("hour")
    ax2_3.set_xlabel("hour")

    ax3_1.set_xlabel("day of week")
    ax3_2.set_xlabel("day of week")
    ax3_3.set_xlabel("day of week")

    ax1_1.plot(mobile_perday)
    ax1_2.plot(twitter_perday)
    ax1_3.plot(prob_perday)

    ax2_1.plot(mobile_perhour)
    ax2_2.plot(twitter_perhour)
    ax2_3.plot(prob_perhour)

    ax3_1.plot(x_label_days, mobile_perdays)
    ax3_2.plot(x_label_days, twitter_perdays)
    ax3_3.plot(x_label_days, prob_perdays)

    save_PATH = (
        "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/make_graph_users/"
        + key
        + ".png"
    )
    fig.savefig(save_PATH)
