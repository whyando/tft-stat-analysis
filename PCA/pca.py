import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

from sklearn.decomposition import PCA 

dataset = pd.read_csv('../one-hit', header=None, sep=',')
X = dataset.iloc[:,2:].values

print(X)

pca = PCA() 
  
print(pca.fit(X))
print(pca.explained_variance_ratio_)

print(pca.components_)

X_pca = pca.transform(X)
print(X_pca)

Xax=X_pca[:,0]
Yax=X_pca[:,1]

fig,ax=plt.subplots(figsize=(7,5))
fig.patch.set_facecolor('white')

ax.scatter(Xax,Yax,c='red',s=1,
           label='hmm')

# for loop ends
plt.xlabel("First Principal Component",fontsize=14)
plt.ylabel("Second Principal Component",fontsize=14)
plt.legend()
plt.show()

print('plot:')