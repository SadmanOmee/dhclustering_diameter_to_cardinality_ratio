import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

clust1x = []
clust1y = []
clust2x = []
clust2y = []


cluster1file = open("cluster1Points.txt","r")
cluster2file = open("cluster2Points.txt","r")

n1 = int(cluster1file.readline())
n2 = int(cluster2file.readline())









for i in range(0, n1):
    line = cluster1file.readline()
    x,y = line.split(" ")
    x = float(x)
    y = float(y)
    clust1x.append(x)
    clust1y.append(y)

for i in range(0, n2):
    line = cluster2file.readline()
    x,y = line.split(" ")
    x = float(x)
    y = float(y)
    clust2x.append(x)
    clust2y.append(y)

cluster1file.close()
cluster2file.close() 

#plt.scatter(points[:, 0], points[:, 1], color="red")
#plt.scatter(points2[:, 0], points2[:, 1], color="blue")
plt.scatter(clust1x, clust1y, color="blue")
plt.scatter(clust2x, clust2y, color="red")
#plt.scatter(0.927386, -0.305095, color="green")
#plt.scatter(3.66395, 1.46738, color="orange")
#plt.scatter(-1.80918, -2.07757, color="black")
#plt.scatter(26, 23, color="orange")
#plt.scatter(30, 15, color="black")

plt.show()

points = []
for i in range (0, len(clust1x)):
    singlePoint = []
    singlePoint.append(clust1x[i])
    singlePoint.append(clust1y[i])
    points.append(singlePoint)
for i in range (0, len(clust2x)):
    singlePoint = []
    singlePoint.append(clust2x[i])
    singlePoint.append(clust2y[i])
    points.append(singlePoint)
    
kmeans = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300)
# Fitting with inputs
kmeans = kmeans.fit(points)
# Predicting the clusters
labels = kmeans.predict(points)
# Getting the cluster centers
C = kmeans.cluster_centers_

for i in range (0, len(points)):
    dist1 = np.linalg.norm(points[i]-C[0])
    dist2 = np.linalg.norm(points[i]-C[1])
    if dist1 < dist2:
        plt.scatter(points[i][0], points[i][1], c = "green")
    else:
        plt.scatter(points[i][0], points[i][1], c = "orange")

#plt.scatter(points[:, 0], points[:, 1], c = y)
plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')

plt.show()
print(kmeans.inertia_)
