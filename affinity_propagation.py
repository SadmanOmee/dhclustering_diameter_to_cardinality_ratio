import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs, make_moons, make_circles
from sklearn.cluster import KMeans, AffinityPropagation, SpectralClustering, \
    AgglomerativeClustering, DBSCAN, OPTICS, Birch, MeanShift
from sklearn.mixture import GaussianMixture
from sklearn.metrics.cluster import adjusted_rand_score
    
k = 2

inputFile = open("input1.txt","r")
n = int(inputFile.readline())
points = []
qMetrics = True
trueLabels = []

for i in range(0, n):
    line = inputFile.readline()
    #line = line.strip()
    #x,y = line.split("    ")
    #x,y = line.split(" ")
    #x = float(x)
    #y = float(y)
    
    xyz = [i for i in line.split()]
    x = float(xyz[0])
    y = float(xyz[1])
    z = float(xyz[2])
    trueLabels.append(z)
    
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

'''---------Affinity Propagation----------'''
def affinityPropagation():
    clustering = AffinityPropagation()
    clustering = clustering.fit(points)
    labels = clustering.labels_
    C = clustering.cluster_centers_
    
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('Affinity Propagation')
    plt.show()
    if qMetrics == True:
        print("Affinity Propagation ARI:", adjusted_rand_score(trueLabels, labels))


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
    if qMetrics == True:
        print("kmeans ARI:", adjusted_rand_score(trueLabels, labels))


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
    if qMetrics == True:
        print("Spectral Clustering ARI:", adjusted_rand_score(trueLabels, labels))

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
    if qMetrics == True:
        print("Agglomerative Clustering ARI:", adjusted_rand_score(trueLabels, labels))


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
    if qMetrics == True:
        print("Birch ARI:", adjusted_rand_score(trueLabels, labels))


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
    if qMetrics == True:
        print("MeanShift ARI:", adjusted_rand_score(trueLabels, labels))


'''--------Gaussian Mixture---------'''
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
    if qMetrics == True:
        print("Gaussian Mixture ARI:", adjusted_rand_score(trueLabels, labels))



'''--------DBSCAN---------'''
def dbscan():
    clustering = DBSCAN(eps=3, min_samples=3)
    clustering = clustering.fit(points)
    labels = clustering.labels_
    #C = clustering.cluster_centers_
    DataX = [points[i][0] for i in range (len(points))]
    DataY = [points[i][1] for i in range (len(points))]
    plt.scatter(DataX, DataY, c = labels, cmap='Set1')
    #plt.scatter(C[:, 0], C[:, 1], marker='*', c='#050505')
    plt.title('DBSCAN')
    plt.show()
    if qMetrics == True:
        print("DBSCAN ARI:", adjusted_rand_score(trueLabels, labels))




def main():
    kmeans()
    spectralClustering()
    wardAC()
    birch()
    meanShift()
    gaussianMixture()
    affinityPropagation()
    dbscan()
          
if __name__ == "__main__":
    main()




