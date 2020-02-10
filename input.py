import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

xCoordinates = []
yCoordinates = []
#points = np.random.weibull(8.0, size=[200, 2])
#points2 = np.random.normal(0.0, 1.0, size=[100, 2]) #gaussian distribution
#points = np.random.exponential(1.0, size=[100, 2])
#points = np.random.beta(1.0, 1.0, size=[200, 2])
#points = np.random.binomial(size=[100, 2], n=5, p= 0.5)
#points = np.random.binomial(size=[100, 2], n=1, p= 0.5) #bernoulli distribution
#points = np.random.gamma(2.0, 2.0, size=[100, 2])
#points = np.random.pareto(3.0, size=[50, 2])
#points = np.random.poisson(5, size=[50, 2])
#points = np.random.lognormal(3, 1, size=[100, 2])
#points = np.random.geometric(p=0.35, size=[100, 2])
#points = np.random.rayleigh(3, size=[100, 2])
points, y = make_blobs(n_samples=200, centers=3, cluster_std=0.80, random_state=0)

inp = str(len(points)) + "\n"

file = open("input1.txt","w")
file.write(inp)

for i in range (0, len(points)):
    #np.around(points[i], decimals=100)
    xCoordinates.append(points[i][0])
    yCoordinates.append(points[i][1])
    inp = str(points[i][0]) + " " + str(points[i][1]) + "\n"
    file.write(inp)
    #None
print(points)
print(points[0][1])






file.close() 

plt.scatter(points[:, 0], points[:, 1], color="red")
#plt.scatter(points2[:, 0], points2[:, 1], color="blue")
plt.scatter(xCoordinates, yCoordinates, color="blue")
plt.show()
