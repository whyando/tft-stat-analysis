import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import random
from sklearn.cluster import KMeans

unit_dict = json.loads('{"TFT3_Ahri":0,"TFT3_Annie":1,"TFT3_Ashe":2,"TFT3_AurelionSol":3,"TFT3_Blitzcrank":4,"TFT3_Caitlyn":5,"TFT3_ChoGath":6,"TFT3_Darius":7,"TFT3_Ekko":8,"TFT3_Ezreal":9,"TFT3_Fiora":10,"TFT3_Fizz":11,"TFT3_Gangplank":12,"TFT3_Graves":13,"TFT3_Irelia":14,"TFT3_JarvanIV":15,"TFT3_Jayce":16,"TFT3_Jhin":17,"TFT3_Jinx":18,"TFT3_KaiSa":19,"TFT3_Karma":20,"TFT3_Kassadin":21,"TFT3_Kayle":22,"TFT3_KhaZix":23,"TFT3_Leona":24,"TFT3_Lucian":25,"TFT3_Lulu":26,"TFT3_Lux":27,"TFT3_Malphite":28,"TFT3_MasterYi":29,"TFT3_MissFortune":30,"TFT3_Mordekaiser":31,"TFT3_Neeko":32,"TFT3_Poppy":33,"TFT3_Rakan":34,"TFT3_Rumble":35,"TFT3_Shaco":36,"TFT3_Shen":37,"TFT3_Sona":38,"TFT3_Soraka":39,"TFT3_Syndra":40,"TFT3_Thresh":41,"TFT3_TwistedFate":42,"TFT3_VelKoz":43,"TFT3_Vi":44,"TFT3_WuKong":45,"TFT3_Xayah":46,"TFT3_XinZhao":47,"TFT3_Yasuo":48,"TFT3_Ziggs":49,"TFT3_Zoe":50}')
unit_dict_sz = 51;
# print(unit_dict)
inv_unit_dict = {v: k for k, v in unit_dict.items()}

dataset = pd.read_csv('../one-hot', header=None, sep=',')
X = dataset.iloc[:,3:].values

# print(X)


N = 16
kmeans = KMeans(n_clusters=N, random_state=0, n_init=1, tol=1e-6).fit(X)
print(N, kmeans.inertia_, kmeans.n_iter_)

# for N in range(1,30):
#     kmeans = KMeans(n_clusters=N, random_state=0, n_init=25, tol=1e-6).fit(X)
#     print(N, kmeans.inertia_, kmeans.n_iter_)
# exit()

# print(kmeans.labels_)
# print(kmeans.cluster_centers_)

total = [0] * N
totalPos = [0] * N
counter = [[0] * 8 for i in range(N)]

example = []

# Now calculate pop + winrate for each cluster
for i in range(len(X)):
    label = kmeans.labels_[i]
    pos = dataset.iloc[i,2]
    total[label] += 1
    totalPos[label] += pos
    counter[label][pos-1] += 1

    if(label == 2):
        example.append(X[i])


# Print comps
for i in range(N):
    print('COMP ', i)
    x = list(range(unit_dict_sz))
    x.sort(key=lambda z: kmeans.cluster_centers_[i][z], reverse=True)

    for j in range(unit_dict_sz):
        if kmeans.cluster_centers_[i][x[j]] < 0.4:
            break
        print(f'{inv_unit_dict[x[j]]}\t{round(kmeans.cluster_centers_[i][x[j]],3)}')
    print('SZ:', j)
    print('Pop:', total[i])
    print('Avg pos:', round(totalPos[i]/total[i],2))
    print('WR:', round(100*counter[i][0]/total[i],2), '%')
    print('Top4:', round(100*(counter[i][0]+counter[i][1]+counter[i][2]+counter[i][3])/total[i],2), '%\n')


random.shuffle(example)


for onehot in example[:10]:
    strList = map(lambda j: inv_unit_dict[j],filter(lambda j: onehot[j] == 1, list(range(unit_dict_sz))))
    # print(list(str))
    print(",".join(strList))