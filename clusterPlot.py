import numpy as np
import matplotlib.pyplot as plt

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

#plt.show()
