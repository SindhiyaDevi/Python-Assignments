import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mcdonalds.csv")
print(df.head(10))
print(df.shape)
print(df.describe())
print(df.dtypes)
print(df.isnull().sum())

#count of gender, visit frequency and like

df['Gender'].value_counts()
df['VisitFrequency'].value_counts()
df['Like'].value_counts()


#Consumer segmentation based on Age and Gender

#Gender

labels = ['Female', 'Male']
size = df['Gender'].value_counts()
colors = ['green', 'pink']
explode = [0, 0.1]
plt.rcParams['figure.figsize'] = (7, 7)
plt.pie(size, colors = colors, explode = explode, labels = labels, shadow = True, autopct = '%.2f%%')
plt.title('Gender', fontsize = 20)
plt.axis('off')
plt.legend()
plt.show()

#Acco to the above pie char mcdonalds getting more female customers than men

#Age

plt.rcParams['figure.figsize'] = (25, 8)
f = sns.countplot(x=df['Age'],palette = 'hsv')
f.bar_label(f.containers[0])
plt.title('Age distribution of customers')
plt.show()

#converting catgorical values into binary

from sklearn.preprocessing import LabelEncoder
def labelling(x):
    df[x] = LabelEncoder().fit_transform(df[x])
    return df

catagory = ['yummy', 'convenient', 'spicy', 'fattening','greasy', 'fast', 'cheap', 'tasty', 'expensive',
       'healthy', 'disgusting']

for i in catagory:
    labelling(i)
df
print(df)

#converting 11 columns into array

x = df.loc[:, catagory].values
print(x)

df_eleven = df.loc[:, catagory]

#Elbow method to find the optimal number of clusters

from sklearn.cluster import KMeans
wcss = []
for k in range(1,11):
   kmeans= KMeans(n_clusters=k, init='k-means++', random_state=42)
   kmeans.fit(x)
   wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss, linewidth=2, color="blue", marker = '*')
plt.title('The Elbow method')
plt.xlabel('Number of cluster')
plt.ylabel('wcss')
plt.show()


#From Elbow method we decided to take number 5 as an optimal cluster

#training the K-means model on the dataset

kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(x)
print(y_kmeans)
#here the array mentioned that which consumer belongs to which catagory.example, the row customer fall under 5 th cluster
#second row customer fall under 2nd cluster
#here o mentions first cluster catagory
#1 mention 2nd cluster, 2 mentions 3rd cluster, 3 mentions 3rd cluster and 4 mentions 5th cluster

# Principal component Analysis

from sklearn.decomposition import PCA
from sklearn import preprocessing

pca_data = preprocessing.scale(x)
pca = PCA(n_components=11)
pc = pca.fit_transform(x)
names = ['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6', 'pc7', 'pc8', 'pc9', 'pc10', 'pc11']
pf = pd.DataFrame(data = pc, columns = names)
print(pf)


#variance from pc1 to pc11

pca.explained_variance_ratio_
np.cumsum(pca.explained_variance_ratio_)

loadings = pca.components_
num_pc = pca.n_features_
pc_list = ["PC"+str(i) for i in list(range(1, num_pc+1))]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['variable'] = df_eleven.columns.values
loadings_df = loadings_df.set_index('variable')
print(loadings_df)

#pc scores
from bioinfokit.visuz import cluster
pca_scores = PCA(). fit_transform(x)
cluster.biplot(cscore=pca_scores, loadings=loadings, labels=df.columns.values, var1=round(pca.explained_variance_ratio_[0]*100, 2),
    var2=round(pca.explained_variance_ratio_[1]*100, 2),show=True,dim=(10,5))



plt.scatter(data = pc, x="pc1", y="pc2", s=30, c='red', label='cluster1')
plt.scatter(data = pc, x="pc1", y="pc2", s=30, c= 'blue', label='cluster2')
plt.scatter(data = pc, x="pc1", y="pc2", s=30, c= 'pink', label='cluster3')
plt.scatter(data = pc, x="pc1", y="pc2", s=30, c='cyan', label='cluster4')
plt.scatter(data = pc, x="pc1", y="pc2", s=30, c='magenta', label='cluster5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label='centroids')
plt.title('Clusters of customers')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()



