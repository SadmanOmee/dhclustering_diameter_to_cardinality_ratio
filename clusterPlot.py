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
cluster1 = []
cluster2 = []
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
    
kmeans = KMeans(n_clusters=2, init='k-means++', n_init=20, max_iter=300)
# Fitting with inputs
kmeans = kmeans.fit(points)
# Predicting the clusters
labels = kmeans.predict(points)
# Getting the cluster centers
C = kmeans.cluster_centers_

rad1 = 0.0
rad2 = 0.0

for i in range (0, len(points)):
    dist1 = np.linalg.norm(points[i]-C[0])
    dist2 = np.linalg.norm(points[i]-C[1])
    if dist1 < dist2:
        plt.scatter(points[i][0], points[i][1], c = "green")
        cluster1.append(points[i])
        rad1 = max(rad1, dist1)
    else:
        plt.scatter(points[i][0], points[i][1], c = "orange")
        cluster2.append(points[i])
        rad2 = max(rad2, dist2)

#plt.scatter(points[:, 0], points[:, 1], c = y)
plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')

plt.show()
print("sse:", kmeans.inertia_)

diameter1 = 0.0
diameter2 = 0.0

for i in range(0, len(cluster1)):
    for j in range(0, len(cluster1)):
        dist1 = ((cluster1[i][0] - cluster1[j][0]) * (cluster1[i][0] - cluster1[j][0]) + (cluster1[i][1] - cluster1[j][1]) * (cluster1[i][1] - cluster1[j][1])) ** 0.5
        if dist1 > diameter1:
            diameter1 = dist1

for i in range(0, len(cluster2)):
    for j in range(0, len(cluster2)):
        dist2 = ((cluster2[i][0] - cluster2[j][0]) * (cluster2[i][0] - cluster2[j][0]) + (cluster2[i][1] - cluster2[j][1]) * (cluster2[i][1] - cluster2[j][1])) ** 0.5
        if dist2 > diameter2:
            diameter2 = dist2
            
print("diameters:", diameter1, diameter2)
print("sum of diameters:", diameter1 + diameter2)
print("average diameter:", (diameter1 + diameter2) / 2)
print("radii:", rad1, rad2)
print("sum of radii:", rad1 + rad2)
print("average radii:", (rad1 + rad2) / 2)

intraClustDist1 = 0.0
intraClustDist2 = 0.0
for i in range (0, len(cluster1)):
    intraClustDist1 += np.linalg.norm(cluster1[i]-C[0])

for i in range (0, len(cluster2)):
    intraClustDist2 += np.linalg.norm(cluster2[i]-C[1])
    
print("intra-cluster distances:", intraClustDist1, intraClustDist2)

avgIntraClustDist1 = intraClustDist1 / len(cluster1)
avgIntraClustDist2 = intraClustDist2 / len(cluster2)
DbyNdRatio1 = diameter1 / len(cluster1)
DbyNdRatio2 = diameter2 / len(cluster2)
RbyNrRatio1 = rad1 / len(cluster1)
RbyNrRatio2 = rad2 / len(cluster2)
centDist = np.linalg.norm(C[0]-C[1])
maxDbyNdRatio = max(DbyNdRatio1, DbyNdRatio2)
print("average intra-cluster distances:", avgIntraClustDist1, avgIntraClustDist2)
print("sum of average intra-cluster distances:", avgIntraClustDist1 + avgIntraClustDist2)
print("d by nd ratio: ", DbyNdRatio1, DbyNdRatio2)
print("sum of d by nd ratios: ", DbyNdRatio1 + DbyNdRatio2)
print("r by nr ratio: ", RbyNrRatio1, RbyNrRatio2)
print("sum of r by nr ratios: ", RbyNrRatio1 + RbyNrRatio2)
print("centroid distances:", centDist)
diffDbyNd = 0.00389 - maxDbyNdRatio
print("diffDbyNd:", '{:.20f}'.format(diffDbyNd))
diffCentDist = centDist - 0.2428
print("diffCentDist", '{:.20f}'.format(diffCentDist))
#print(diffDbyNd + diffCentDist)
#print('{:.20f}'.format(2 * maxDbyNdRatio * centDist))
#print('{:.20f}'.format(2 * 0.00389 * 0.2428))
#print(maxDbyNdRatio * centDist)
