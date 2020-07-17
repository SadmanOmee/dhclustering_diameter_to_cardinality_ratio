import numpy as np
import matplotlib.pyplot as plt

xData = []
yData = []

labels = ['Aggregation', 'S1', 'Unbalance', 'Flame', 'A1', 'A2', 'A3']
kMeans = [78.553, 87.02, 68.108, 81.250, 83.2, 79.086, 81.906]
oae = [80.838, 85.32, 94.169, 87.083, 85.067, 83.048, 84.013]
oam = [85.787, 82.04, 88.277, 73.333, 81.133, 78.038, 78.933]

x = np.arange(len(labels))  # the label locations
width = 0.21  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, kMeans, width, label='k-Means Clustering', edgecolor='black')
rects2 = ax.bar(x, oae, width, label='Our Algorithm(euclidean)', edgecolor='black')
rects2 = ax.bar(x + width, oam, width, label='Our Algorithm(manhattan)', edgecolor='black')

ax.set_xlabel('Datasets', fontsize='large')
ax.set_ylabel('Accuracy(in percentage)', fontsize='large')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)

plt.xlim(-0.7, 6.7)
plt.show()

xK = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yK = [97.000, 94.000, 91.000, 89.067, 87.100, 86, 83.500, 81.033, 80.067, 79.950]
plt.plot(xK, yK, color='blue', 
         marker='o', markerfacecolor='blue', label='k-Means Clustering')
xD = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yD = [97.033, 95.000, 92.050, 91.033, 89.038, 87, 85.067, 83.500, 83.000, 82.500]
plt.plot(xD, yD, color='red', linestyle='--', 
         marker='o', markerfacecolor='red', label='Our Algorithm(euclidean)')
plt.legend()
plt.xlabel('number of clusters', fontsize='large')
plt.ylabel('Accuracy(in percentage)', fontsize='large')

plt.show()