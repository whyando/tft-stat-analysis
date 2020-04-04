import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import json
import random
from sklearn.cluster import KMeans

unit_dict = json.loads('{"TFT3_Ahri":0,"TFT3_Annie":1,"TFT3_Ashe":2,"TFT3_AurelionSol":3,"TFT3_Blitzcrank":4,"TFT3_Caitlyn":5,"TFT3_ChoGath":6,"TFT3_Darius":7,"TFT3_Ekko":8,"TFT3_Ezreal":9,"TFT3_Fiora":10,"TFT3_Fizz":11,"TFT3_Gangplank":12,"TFT3_Graves":13,"TFT3_Irelia":14,"TFT3_JarvanIV":15,"TFT3_Jayce":16,"TFT3_Jhin":17,"TFT3_Jinx":18,"TFT3_KaiSa":19,"TFT3_Karma":20,"TFT3_Kassadin":21,"TFT3_Kayle":22,"TFT3_KhaZix":23,"TFT3_Leona":24,"TFT3_Lucian":25,"TFT3_Lulu":26,"TFT3_Lux":27,"TFT3_Malphite":28,"TFT3_MasterYi":29,"TFT3_MissFortune":30,"TFT3_Mordekaiser":31,"TFT3_Neeko":32,"TFT3_Poppy":33,"TFT3_Rakan":34,"TFT3_Rumble":35,"TFT3_Shaco":36,"TFT3_Shen":37,"TFT3_Sona":38,"TFT3_Soraka":39,"TFT3_Syndra":40,"TFT3_Thresh":41,"TFT3_TwistedFate":42,"TFT3_VelKoz":43,"TFT3_Vi":44,"TFT3_WuKong":45,"TFT3_Xayah":46,"TFT3_XinZhao":47,"TFT3_Yasuo":48,"TFT3_Ziggs":49,"TFT3_Zoe":50}')
unit_dict_sz = 51;
# print(unit_dict)
inv_unit_dict = {v: k for k, v in unit_dict.items()}

dataset = pd.read_csv('../one-hot.txt', header=None, sep=',')
X = dataset.iloc[:,3:].values
# print(X)

# TRAIN 16 CLUSTERS

N = 16
kmeans = KMeans(n_clusters=N, random_state=0, n_init=15, tol=1e-6).fit(X)
print(N, kmeans.inertia_, kmeans.n_iter_)

# don't need to save labels
kmeans.labels_ = 0
pickle.dump(kmeans, open("trained_kmeans.pkl", "wb"))

# for N in range(1,30):
#     kmeans = KMeans(n_clusters=N, random_state=0, n_init=25, tol=1e-6).fit(X)
#     print(N, kmeans.inertia_, kmeans.n_iter_)
# exit()