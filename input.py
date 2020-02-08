import numpy as np
import matplotlib.pyplot as plt

xCoordinates = []
yCoordinates = []
points = np.random.exponential(size=[200, 2])
points2 = np.random.normal(0.0, 1.0, size=[100, 2])

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
