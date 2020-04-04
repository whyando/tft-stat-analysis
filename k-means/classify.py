import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import json
import pytz
import datetime
import random
from sklearn.cluster import KMeans

def get_ymd(ts):
    dt = datetime.datetime.utcfromtimestamp(ts/1000)
    # print(dt.strftime('%Y-%m-%d %H:%M:%S'))
    # print(dt.astimezone(pytz.timezone("Asia/Seoul")))
    # ymd = print()
    return dt.astimezone(pytz.timezone("Asia/Seoul")).strftime('%Y-%m-%d')


def str_OneHot(onehot):
    strList = map(lambda j: inv_unit_dict[j],filter(lambda j: onehot[j] > 0.4, range(unit_dict_sz)))
    # print(list(str))
    return "_".join(strList)

# Set 3 specific constants
unit_dict = json.loads('{"TFT3_Ahri":0,"TFT3_Annie":1,"TFT3_Ashe":2,"TFT3_AurelionSol":3,"TFT3_Blitzcrank":4,"TFT3_Caitlyn":5,"TFT3_ChoGath":6,"TFT3_Darius":7,"TFT3_Ekko":8,"TFT3_Ezreal":9,"TFT3_Fiora":10,"TFT3_Fizz":11,"TFT3_Gangplank":12,"TFT3_Graves":13,"TFT3_Irelia":14,"TFT3_JarvanIV":15,"TFT3_Jayce":16,"TFT3_Jhin":17,"TFT3_Jinx":18,"TFT3_KaiSa":19,"TFT3_Karma":20,"TFT3_Kassadin":21,"TFT3_Kayle":22,"TFT3_KhaZix":23,"TFT3_Leona":24,"TFT3_Lucian":25,"TFT3_Lulu":26,"TFT3_Lux":27,"TFT3_Malphite":28,"TFT3_MasterYi":29,"TFT3_MissFortune":30,"TFT3_Mordekaiser":31,"TFT3_Neeko":32,"TFT3_Poppy":33,"TFT3_Rakan":34,"TFT3_Rumble":35,"TFT3_Shaco":36,"TFT3_Shen":37,"TFT3_Sona":38,"TFT3_Soraka":39,"TFT3_Syndra":40,"TFT3_Thresh":41,"TFT3_TwistedFate":42,"TFT3_VelKoz":43,"TFT3_Vi":44,"TFT3_WuKong":45,"TFT3_Xayah":46,"TFT3_XinZhao":47,"TFT3_Yasuo":48,"TFT3_Ziggs":49,"TFT3_Zoe":50}')
unit_dict_sz = 51;
inv_unit_dict = {v: k[5:10] for k, v in unit_dict.items()}

# Load data
dataset = pd.read_csv('../one-hot.txt', header=None, sep=',')
X = dataset.iloc[:,3:].values

# Load saved model + predict
kmeans = pickle.load(open("trained_kmeans.pkl", "rb"))
N = kmeans.n_clusters
y = kmeans.predict(X)

# Count
total = [0] * N
totalPos = [0] * N
counter = [[0] * 8 for i in range(N)]

day = {}

# Now calculate pop + winrate for each cluster
for i in range(len(X)):
# for i in range(100):
    label = y[i]
    ymd = get_ymd(dataset.iloc[i,1])
    pos = dataset.iloc[i,2]

    if ymd not in day:
        day[ymd] = [0] * N

    day[ymd][label] += 1

    # totalPos[label] += pos
    # counter[label][pos-1] += 1

s = ','.join(str_OneHot(kmeans.cluster_centers_[i]) for i in range(N))
print('Date,'+s)

for d in sorted(day.keys()):
    s = ','.join(str(day[d][i]) for i in range(N))
    print(d + ',' + s)

# # Print comps
# for i in range(N):
#     print('COMP ', i)
#     x = list(range(unit_dict_sz))
#     x.sort(key=lambda z: kmeans.cluster_centers_[i][z], reverse=True)

#     for j in range(unit_dict_sz):
#         if kmeans.cluster_centers_[i][x[j]] < 0.4:
#             break
#         print(f'{inv_unit_dict[x[j]]}\t{round(kmeans.cluster_centers_[i][x[j]],3)}')
#     print('SZ:', j)
#     print('Pop:', total[i])
#     print('Avg pos:', round(totalPos[i]/total[i],2))
#     print('WR:', round(100*counter[i][0]/total[i],2), '%')
#     print('Top4:', round(100*(counter[i][0]+counter[i][1]+counter[i][2]+counter[i][3])/total[i],2), '%\n')


# random.shuffle(example)


# for onehot in example[:10]:
#     strList = map(lambda j: inv_unit_dict[j],filter(lambda j: onehot[j] == 1, list(range(unit_dict_sz))))
#     # print(list(str))
#     print(",".join(strList))