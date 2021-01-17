import numpy as np
import matplotlib.pyplot as plt

xData = []
yData = []

#----------small ari------------------------
'''labels = ['Aggregation', 'Flame', 'Compound', 'R15']
kMeans = [0.7952, 0.4901, 0.5364, 0.7512]
oae = [0.8133, 0.762, 0.5972, 0.7553]
oam = [0.8561, 0.7475, 0.5413, 0.7266]
oac = [0.8039, 0.682, 0.5189, 0.6945]
wac = [0.769, 0.4734, 0.5506, 0.739]
diana = [0.7245, 0.4825, 0.4923, 0.714]
affprop = [0.3456, 0.4423, 0.3557, 0.7134]

x = np.arange(len(labels))  # the label locations
width = 0.12  # the width of the bars

fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(x - 3 * width, kMeans, width, label='k-Means Clustering', edgecolor='black')
rects2 = ax.bar(x - 2 * width, oae, width, label='Our Algorithm(euclidean)', edgecolor='black')
rects3 = ax.bar(x - width, oam, width, label='Our Algorithm(manhattan)', edgecolor='black')
rects4 = ax.bar(x, oac, width, label='Our Algorithm(chebyshev)', edgecolor='black')
rects5 = ax.bar(x + width, wac, width, label='WAC', edgecolor='black')
rects6 = ax.bar(x + 2 * width, diana, width, label='DIANA', edgecolor='black')
rects7 = ax.bar(x + 3 * width, affprop, width, label='Affinity Propagation', edgecolor='black')

ax.set_xlabel('Datasets', fontsize='large')
ax.set_ylabel('Adjusted Rand Index', fontsize='large')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)

plt.xlim(-0.6, 3.6)
plt.show()'''



#----------small sc------------------------
'''labels = ['Aggregation', 'Flame', 'Compound', 'R15']
kMeans = [0.4801, 0.378, 0.4312, 0.472]
oae = [0.5203, 0.4615, 0.4916, 0.4752]
oam = [0.5325, 0.4379, 0.4692, 0.4482]
oac = [0.4481, 0.3942, 0.4251, 0.4055]
wac = [0.4716, 0.3288, 0.4175, 0.4622]
diana = [0.4737, 0.359, 0.487, 0.4368]
affprop = [0.4052, 0.3418, 0.4151, 0.4688]

x = np.arange(len(labels))  # the label locations
width = 0.12  # the width of the bars

fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(x - 3 * width, kMeans, width, label='k-Means Clustering', edgecolor='black')
rects2 = ax.bar(x - 2 * width, oae, width, label='Our Algorithm(euclidean)', edgecolor='black')
rects3 = ax.bar(x - width, oam, width, label='Our Algorithm(manhattan)', edgecolor='black')
rects4 = ax.bar(x, oac, width, label='Our Algorithm(chebyshev)', edgecolor='black')
rects5 = ax.bar(x + width, wac, width, label='WAC', edgecolor='black')
rects6 = ax.bar(x + 2 * width, diana, width, label='DIANA', edgecolor='black')
rects7 = ax.bar(x + 3 * width, affprop, width, label='Affinity Propagation', edgecolor='black')

ax.set_xlabel('Datasets', fontsize='large')
ax.set_ylabel('Silhouette Coefficient', fontsize='large')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)

plt.xlim(-0.6, 3.6)
plt.show()'''



#----------big ari------------------------
'''labels = ['A1', 'A2', 'A3', 'S1', 'S2', 'Unbalance']
kMeans = [0.826, 0.8277, 0.8213, 0.8523, 0.8672, 0.6478]
oae = [0.8724, 0.849, 0.8573, 0.8341, 0.8414, 0.892]
oam = [0.8314, 0.8158, 0.7835, 0.8214, 0.8253, 0.8798]
oac = [0.8179, 0.7874, 0.7623, 0.7466, 0.8045, 0.8486]
wac = [0.7926, 0.7885, 0.8091, 0.8332, 0.8527, 0.7884]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots(figsize=(12,5))
rects1 = ax.bar(x - 2 * width, kMeans, width, label='k-Means Clustering', edgecolor='black')
rects2 = ax.bar(x - width, oae, width, label='Our Algorithm(euclidean)', edgecolor='black')
rects3 = ax.bar(x, oam, width, label='Our Algorithm(manhattan)', edgecolor='black')
rects4 = ax.bar(x + width, oac, width, label='Our Algorithm(chebyshev)', edgecolor='black')
rects5 = ax.bar(x + 2 * width, wac, width, label='WAC', edgecolor='black')

ax.set_xlabel('Datasets', fontsize='large')
ax.set_ylabel('Adjusted Rand Index', fontsize='large')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)

plt.xlim(-0.5, 5.5)
plt.show()'''




#----------big sc------------------------
'''labels = ['A1', 'A2', 'A3', 'S1', 'S2', 't4.8k', 'Unbalance']
kMeans = [0.595, 0.5975, 0.5894, 0.7112, 0.6261, 0.4125, 0.5042]
oae = [0.6441, 0.6247, 0.6498, 0.6534, 0.5892, 0.4713, 0.8386]
oam = [0.5823, 0.5672, 0.5455, 0.6192, 0.5748, 0.4188, 0.8157]
oac = [0.542, 0.5034, 0.5127, 0.5282, 0.5536, 0.3995, 0.7961]
wac = [0.5762, 0.5797, 0.5875, 0.7084, 0.6076, 0.3667, 0.7225]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots(figsize=(12,5))
rects1 = ax.bar(x - 2 * width, kMeans, width, label='k-Means Clustering', edgecolor='black')
rects2 = ax.bar(x - width, oae, width, label='Our Algorithm(euclidean)', edgecolor='black')
rects3 = ax.bar(x, oam, width, label='Our Algorithm(manhattan)', edgecolor='black')
rects4 = ax.bar(x + width, oac, width, label='Our Algorithm(chebyshev)', edgecolor='black')
rects5 = ax.bar(x + 2 * width, wac, width, label='WAC', edgecolor='black')

ax.set_xlabel('Datasets', fontsize='large')
ax.set_ylabel('Silhouette Coefficient', fontsize='large')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)

plt.xlim(-0.5, 6.5)
plt.show()'''














plotW = 10
plotH = 5
xK = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#yK = [97.000, 94.000, 91.000, 89.067, 87.100, 86, 83.500, 81.033, 80.067, 79.950]
yK = [0.93, 0.92, 0.90, 0.88, 0.865, 0.85, 0.83, 0.817, 0.812, 0.805]
plt.figure(figsize=(plotW, plotH))
plt.plot(xK, yK, marker='o', markerfacecolor='none', label='k-Means Clustering')
xD = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#yD = [97.033, 95.000, 92.050, 91.033, 89.038, 87, 85.067, 83.500, 83.000, 82.500]
yD = [0.95, 0.94, 0.92, 0.90, 0.89, 0.875, 0.86, 0.845, 0.84, 0.835]
#plt.figure(figsize=(plotW, plotH))
plt.plot(xD, yD, linestyle=':', marker='o', markerfacecolor='none', label='Our Algorithm (euclidean)')
xW = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yW = [0.91, 0.90, 0.89, 0.87, 0.845, 0.835, 0.825, 0.820, 0.817, 0.815]
#plt.figure(figsize=(plotW, plotH))
plt.plot(xW, yW, linestyle='--', marker='o', markerfacecolor='none', label='Ward Agglomerative Clustering')
plt.legend()
plt.xlabel('number of clusters', fontsize='large')
plt.ylabel('Adjusted Rand Index', fontsize='large')

plt.show()