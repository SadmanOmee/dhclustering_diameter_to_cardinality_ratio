import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs, make_moons, make_circles
from sklearn.cluster import KMeans, AffinityPropagation, SpectralClustering, \
    AgglomerativeClustering, DBSCAN, OPTICS, Birch, MeanShift
from sklearn.mixture import GaussianMixture
    
k = 8

inputFile = open("input1.txt","r")
n = int(inputFile.readline())
points = []

for i in range(0, n):
    line = inputFile.readline()
    #line = line.strip()
    #x,y = line.split("    ")
    x,y = line.split(" ")
    x = float(x)
    y = float(y)
    singlePoint = []
    singlePoint.append(x)
    singlePoint.append(y)
    points.append(singlePoint)
points = np.array(points)
inputFile.close()
#print(points)

#points, y = make_blobs(n_samples=100, centers=2, cluster_std=2.0, random_state=1)
#points, y = make_moons(n_samples=100, noise=0.05, random_state = 1)
#points, y = make_circles(n_samples=100, noise=0.01)
plt.scatter(points[:, 0], points[:, 1], color="black")
#print(points)
plt.show()

markers = ['^', 'x', 'o']

'''---------Affinity Propagation----------'''
'''clustering = AffinityPropagation()
clustering = clustering.fit(points)
labels = clustering.labels_
C = clustering.cluster_centers_

DataX = [points[i][0] for i in range (len(points))]
DataY = [points[i][1] for i in range (len(points))]
plt.scatter(DataX, DataY, c = labels, cmap='Set1')
plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
plt.title('Affinity Propagation')
plt.show()'''


'''---------kmeans----------'''
def kmeans():
    clustering = KMeans(n_clusters=k, init='k-means++', n_init=30, max_iter=1000)
    clustering = clustering.fit(points)
    labels = clustering.predict(points)
    C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('kmeans')
    plt.show()


'''--------Spectral Clustering---------'''
def spectralClustering():
    clustering = SpectralClustering(n_clusters=k, assign_labels="discretize", random_state=0)
    clustering = clustering.fit(points)
    labels = clustering.labels_
    #C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    #plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('Spectral Clustering')
    plt.show()

'''--------Agglomerative Clustering---------'''
def wardAC():
    clustering = AgglomerativeClustering(n_clusters=k, linkage='ward')
    clustering = clustering.fit(points)
    labels = clustering.labels_
    #C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    #plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('Agglomerative Clustering')
    plt.show()


'''--------OPTICS---------'''
'''clustering = OPTICS(min_samples=2)
clustering = clustering.fit(points)
labels = clustering.labels_
#C = clustering.cluster_centers_
DataX = [points[i][0] for i in range (len(points))]
DataY = [points[i][1] for i in range (len(points))]
plt.scatter(DataX, DataY, c = labels, cmap='Set1')
#plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
plt.title('OPTICS')
plt.show()'''


'''--------Birch---------'''
def birch():
    clustering = Birch(n_clusters=k)
    clustering = clustering.fit(points)
    labels = clustering.predict(points)
    #C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    #plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('Birch')
    plt.show()


'''--------MeanShift---------'''
def meanShift():
    clustering = MeanShift()
    #clustering = MeanShift(bandwidth=2)
    clustering = clustering.fit(points)
    labels = clustering.labels_
    C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('MeanShift')
    plt.show()


'''--------GaussianMixture---------'''
def gaussianMixture():
    #clustering = GaussianMixture(n_components=2, random_state=0)
    clustering = GaussianMixture(n_components=k, random_state=0)
    clustering = clustering.fit(points)
    labels = clustering.predict(points)
    #C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    #plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('GaussianMixture')
    plt.show()



'''--------DBSCAN---------'''
def dbscan():
    clustering = DBSCAN(eps=3, min_samples=2)
    clustering = clustering.fit(points)
    labels = clustering.labels_
    #C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    #plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('DBSCAN')
    plt.show()




def main():
    kmeans()
    spectralClustering()
    wardAC()
    birch()
    meanShift()
    gaussianMixture()
    dbscan()
          
if __name__ == "__main__":
    main()




