import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

key = "Kyoto_station"
df = pd.read_csv(
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/twitter/Kyoto/proceed/processed_Kyotostation_3zi_2022.csv"
)
mobile_npy_PATH = "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/data/mobile/Kyoto/Kyotostation.npy"

day_list_long = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
]
day_list_short = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
]
day_list_Feb = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
]
hour_list = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
]

list_num_day = []
for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    df_onemonth = df[df["creatid_at_month"] == month]
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day_list = day_list_long
    elif month == 2:
        day_list = day_list_Feb
    else:
        day_list = day_list_short
    for day in day_list:
        list_num_hour = []
        for hour in hour_list:
            df_oneday = df_onemonth[df_onemonth["creatid_at_day"] == day]
            num = len(df_oneday[df_oneday["creatid_at_hour"] == hour])
            list_num_hour.append(num)
        list_num_day.append(list_num_hour)

list_num_day = np.array(list_num_day)

# swarm
df_swarm = df[
    (df["text"].str.contains("I'm at"))
    | (df["text"].str.contains("@") & df["text"].str.contains("in"))
]
df = df_swarm
list_num_day_swarm = []
for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    df_onemonth = df[df["creatid_at_month"] == month]
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day_list = day_list_long
    elif month == 2:
        day_list = day_list_Feb
    else:
        day_list = day_list_short
    for day in day_list:
        list_num_hour = []
        for hour in hour_list:
            df_oneday = df_onemonth[df_onemonth["creatid_at_day"] == day]
            num = len(df_oneday[df_oneday["creatid_at_hour"] == hour])
            list_num_hour.append(num)
        list_num_day_swarm.append(list_num_hour)
list_num_day_swarm = np.array(list_num_day_swarm)

# make graph
mobile = np.load(mobile_npy_PATH)
twitter = list_num_day
prob = twitter / mobile
swarm = list_num_day_swarm
prob_swarm = swarm / mobile

mobile_perhour = np.average(mobile, axis=0)
twitter_perhour = np.average(twitter, axis=0)
prob_perhour = np.average(prob, axis=0)
swarm_perhour = np.average(swarm, axis=0)
prob_swarm_perhour = np.average(prob_swarm, axis=0)


mobile_perday = np.average(mobile, axis=1)
twitter_perday = np.average(twitter, axis=1)
prob_perday = np.average(prob, axis=1)
swarm_perday = np.average(swarm, axis=1)
prob_swarm_perday = np.average(prob_swarm, axis=1)

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

list_swarm_Sun = []
list_swarm_Mon = []
list_swarm_Tue = []
list_swarm_Wed = []
list_swarm_Thu = []
list_swarm_Fri = []
list_swarm_Sat = []

list_prob_swarm_Sun = []
list_prob_swarm_Mon = []
list_prob_swarm_Tue = []
list_prob_swarm_Wed = []
list_prob_swarm_Thu = []
list_prob_swarm_Fri = []
list_prob_swarm_Sat = []

# 2021 mod
for i in range(0, 365):
    if i % 7 == 6:
        list_mobile_Fri.append(mobile[i].tolist())
        list_twitter_Fri.append(twitter[i].tolist())
        list_prob_Fri.append(prob[i].tolist())
        list_swarm_Fri.append(swarm[i].tolist())
        list_prob_swarm_Fri.append(prob_swarm[i].tolist())
    if i % 7 == 0:
        list_mobile_Sat.append(mobile[i].tolist())
        list_twitter_Sat.append(twitter[i].tolist())
        list_prob_Sat.append(prob[i].tolist())
        list_swarm_Sat.append(swarm[i].tolist())
        list_prob_swarm_Sat.append(prob_swarm[i].tolist())
    if i % 7 == 1:
        list_mobile_Sun.append(mobile[i].tolist())
        list_twitter_Sun.append(twitter[i].tolist())
        list_prob_Sun.append(prob[i].tolist())
        list_swarm_Sun.append(swarm[i].tolist())
        list_prob_swarm_Sun.append(prob_swarm[i].tolist())
    if i % 7 == 2:
        list_mobile_Mon.append(mobile[i].tolist())
        list_twitter_Mon.append(twitter[i].tolist())
        list_prob_Mon.append(prob[i].tolist())
        list_swarm_Mon.append(swarm[i].tolist())
        list_prob_swarm_Mon.append(prob_swarm[i].tolist())
    if i % 7 == 3:
        list_mobile_Tue.append(mobile[i].tolist())
        list_twitter_Tue.append(twitter[i].tolist())
        list_prob_Tue.append(prob[i].tolist())
        list_swarm_Tue.append(swarm[i].tolist())
        list_prob_swarm_Tue.append(prob_swarm[i].tolist())
    if i % 7 == 4:
        list_mobile_Wed.append(mobile[i].tolist())
        list_twitter_Wed.append(twitter[i].tolist())
        list_prob_Wed.append(prob[i].tolist())
        list_swarm_Wed.append(swarm[i].tolist())
        list_prob_swarm_Wed.append(prob_swarm[i].tolist())
    if i % 7 == 5:
        list_mobile_Thu.append(mobile[i].tolist())
        list_twitter_Thu.append(twitter[i].tolist())
        list_prob_Thu.append(prob[i].tolist())
        list_swarm_Thu.append(swarm[i].tolist())
        list_prob_swarm_Thu.append(prob_swarm[i].tolist())

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

swarm_perdays = [
    np.average(list_swarm_Sun),
    np.average(list_swarm_Mon),
    np.average(list_swarm_Tue),
    np.average(list_swarm_Wed),
    np.average(list_swarm_Tue),
    np.average(list_swarm_Fri),
    np.average(list_swarm_Sat),
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

prob_swarm_perdays = [
    np.average(list_prob_swarm_Sun),
    np.average(list_prob_swarm_Mon),
    np.average(list_prob_swarm_Tue),
    np.average(list_prob_swarm_Wed),
    np.average(list_prob_swarm_Tue),
    np.average(list_prob_swarm_Fri),
    np.average(list_prob_swarm_Sat),
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
ax1_2.set_title("tweets day")
ax1_3.set_title("prob day")
ax2_1.set_title("population hour")
ax2_2.set_title("tweets hour")
ax2_3.set_title("prob hour")
ax3_1.set_title("population day of week")
ax3_2.set_title("tweets day of week")
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
ax1_2.plot(twitter_perday, label="Twitter")
ax1_2.plot(swarm_perday, label="Swarm")
ax1_2.legend(loc="upper right")
ax1_3.plot(prob_perday)

ax2_1.plot(mobile_perhour)
ax2_2.plot(twitter_perhour, label="Twitter")
ax2_2.plot(swarm_perhour, label="Swarm")
ax2_2.legend(loc="upper right")
ax2_3.plot(prob_perhour, label="Twitter")
ax2_3.plot(prob_swarm_perhour, label="Swarm")
ax2_3.legend(loc="upper right")

ax3_1.plot(x_label_days, mobile_perdays)
ax3_2.plot(x_label_days, twitter_perdays, label="Twitter")
ax3_2.plot(x_label_days, swarm_perdays, label="Swarm")
ax3_2.legend(loc="upper right")
ax3_3.plot(x_label_days, prob_perdays, label="Twitter")
ax3_3.plot(x_label_days, prob_swarm_perdays, label="Swarm")
ax3_3.legend(loc="upper right")

save_PATH = (
    "/home/is/shuntaro-o/dev/compare_population_and_tweet_number/outputs/make_graph_divide/"
    + key
    + ".png"
)
fig.savefig(save_PATH)
