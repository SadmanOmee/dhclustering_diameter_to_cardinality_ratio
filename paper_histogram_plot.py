import numpy as np
import matplotlib.pyplot as plt

xData = []
yData = []

labels = ['Aggregation', 'S1', 'Unbalance', 'Flame', 'A1', 'A2', 'A3']
kMeans = [0.7952, 0.8523, 0.6478, 0.4901, 0.826, 0.8277, 0.8213]
oae = [0.8133, 0.8341, 0.945, 0.762, 0.8724, 0.849, 0.8573]
oam = [0.8561, 0.8214, 0.8898, 0.7475, 0.8314, 0.8158, 0.7835]

x = np.arange(len(labels))  # the label locations
width = 0.21  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, kMeans, width, label='k-Means Clustering', edgecolor='black')
rects2 = ax.bar(x, oae, width, label='Our Algorithm(euclidean)', edgecolor='black')
rects2 = ax.bar(x + width, oam, width, label='Our Algorithm(manhattan)', edgecolor='black')

ax.set_xlabel('Datasets', fontsize='large')
ax.set_ylabel('ARI', fontsize='large')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)

plt.xlim(-0.7, 6.7)
plt.show()

xK = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#yK = [97.000, 94.000, 91.000, 89.067, 87.100, 86, 83.500, 81.033, 80.067, 79.950]
yK = [0.93, 0.92, 0.90, 0.88, 0.865, 0.85, 0.83, 0.82, 0.815, 0.81]
plt.plot(xK, yK, color='blue', 
         marker='o', markerfacecolor='none', label='k-Means Clustering')
xD = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#yD = [97.033, 95.000, 92.050, 91.033, 89.038, 87, 85.067, 83.500, 83.000, 82.500]
yD = [0.95, 0.94, 0.92, 0.90, 0.89, 0.875, 0.86, 0.845, 0.84, 0.835]
plt.plot(xD, yD, color='red', linestyle=':', marker='o', markerfacecolor='none', label='Our Algorithm(euclidean)')
plt.legend()
plt.xlabel('number of clusters', fontsize='large')
plt.ylabel('ARI', fontsize='large')

plt.show()