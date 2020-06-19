import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

xCoordinates = []
yCoordinates = []
#points = np.random.weibull(2.0, size=[300, 2])
#points = np.random.normal(0.0, 2.0, size=[40, 2]) #gaussian distribution
#points = np.random.exponential(1.0, size=[20, 2])
#points = np.random.beta(1.0, 1.0, size=[20, 2])
#points = np.random.binomial(size=[100, 2], n=5, p= 0.5)
#points = np.random.binomial(size=[100, 2], n=1, p= 0.5) #bernoulli distribution
#points = np.random.gamma(2.0, 2.0, size=[400, 2])
#points = np.random.pareto(5.0, size=[100, 2])
#points = np.random.poisson(5, size=[50, 2])
#points = np.random.lognormal(3, 1, size=[100, 2])
#points = np.random.geometric(p=0.35, size=[100, 2])
#points = np.random.rayleigh(3, size=[400, 2])
#points, y = make_blobs(n_samples=200, centers=12, cluster_std=0.60, random_state=8)
#points, y = make_blobs(n_samples=50, centers=2, cluster_std=1.25, random_state=3)
#points, y = make_blobs(n_samples=30, centers=4, cluster_std=1.20, random_state=1)
points, y = make_blobs(n_samples=30, centers=3, cluster_std=1.28, random_state=17)

inp = str(len(points)) + "\n"
#inp = str(len(points) + len(points2)) + "\n"

file = open("input1.txt","w")
file.write(inp)

for i in range (0, len(points)):
    xCoordinates.append(points[i][0])
    yCoordinates.append(points[i][1])
    inp = str(points[i][0]) + " " + str(points[i][1]) + "\n"
    file.write(inp)
    
    #None
'''
for i in range (0, len(points2)):
    xCoordinates.append(points2[i][0] + 15)
    yCoordinates.append(points2[i][1] + 15)
    inp = str(points2[i][0] + 15) + " " + str(points2[i][1] + 15) + "\n"
    file.write(inp)
    
    #None
'''
print(points)
#print(points[0][1])

file.close() 

pointsX = []
pointsY = []
inputFile = open("input1.txt","r")

totalPoints = int(inputFile.readline())
for i in range(0, totalPoints):
    line = inputFile.readline()
    x,y = line.split(" ")
    x = float(x)
    y = float(y)
    pointsX.append(x)
    pointsY.append(y)

inputFile.close()
'''diameter = 0.0
for i in range(0, len(points)):
    for j in range(0, len(points)):
        dist = ((points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])) ** 0.5
        if dist > diameter:
            diameter = dist

print(diameter / len(points))'''

diameter = 0.0
for i in range(0, len(pointsX)):
    for j in range(0, len(pointsX)):
        dist = ((pointsX[i] - pointsX[j]) * (pointsX[i] - pointsX[j]) + (pointsY[i] - pointsY[j]) * (pointsY[i] - pointsY[j])) ** 0.5
        if dist > diameter:
            diameter = dist

print(diameter / len(points))

plt.scatter(points[:, 0], points[:, 1], color="red")
#plt.scatter(points2[:, 0], points2[:, 1], color="blue")
plt.scatter(xCoordinates, yCoordinates, color="black")

plt.show()










'''kmeans = KMeans(n_clusters=2)
# Fitting with inputs
kmeans = kmeans.fit(points)
# Predicting the clusters
labels = kmeans.predict(points)
# Getting the cluster centers
C = kmeans.cluster_centers_

#dist = np.linalg.norm(points[0]-C[0])
#print(dist)

for i in range (0, len(points)):
    dist1 = np.linalg.norm(points[i]-C[0])
    dist2 = np.linalg.norm(points[i]-C[1])
    if dist1 < dist2:
        plt.scatter(points[i][0], points[i][1], c = "green")
    else:
        plt.scatter(points[i][0], points[i][1], c = "orange")

#plt.scatter(points[:, 0], points[:, 1], c = y)
plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')

plt.show()'''
