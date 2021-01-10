import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs, make_moons, make_circles
from sklearn.cluster import KMeans, AffinityPropagation, SpectralClustering, \
    AgglomerativeClustering, DBSCAN, OPTICS, Birch, MeanShift
from sklearn.mixture import GaussianMixture
from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score, homogeneity_score, \
     completeness_score, v_measure_score, fowlkes_mallows_score, silhouette_score, calinski_harabasz_score, \
     davies_bouldin_score
    
k = 15

inputFile = open("input1.txt","r")
n = int(inputFile.readline());
points = []
qMetrics = False
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
    #z = float(xyz[2])
    #trueLabels.append(z)
    
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
        #print("Affinity Propagation RI:", rand_score(trueLabels, labels))
        print("Affinity Propagation ARI:", adjusted_rand_score(trueLabels, labels))
        print("Affinity Propagation AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("Affinity Propagation HS:", homogeneity_score(trueLabels, labels))
        print("Affinity Propagation CS:", completeness_score(trueLabels, labels))
        print("Affinity Propagation VM:", v_measure_score(trueLabels, labels))
        print("Affinity Propagation FM:", fowlkes_mallows_score(trueLabels, labels))
        print("Affinity Propagation SC:", silhouette_score(points, labels, metric='euclidean'))
        print("Affinity Propagation CH:", calinski_harabasz_score(points, labels))
        print("Affinity Propagation DB:", davies_bouldin_score(points, labels))


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
        print("kmeans AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("kmeans HS:", homogeneity_score(trueLabels, labels))
        print("kmeans CS:", completeness_score(trueLabels, labels))
        print("kmeans VM:", v_measure_score(trueLabels, labels))
        print("kmeans FM:", fowlkes_mallows_score(trueLabels, labels))
        print("kmeans SC:", silhouette_score(points, labels, metric='euclidean'))
        print("kmeans CH:", calinski_harabasz_score(points, labels))
        print("kmeans DB:", davies_bouldin_score(points, labels))


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
        print("Spectral Clustering AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("Spectral Clustering HS:", homogeneity_score(trueLabels, labels))
        print("Spectral Clustering CS:", completeness_score(trueLabels, labels))
        print("Spectral Clustering VM:", v_measure_score(trueLabels, labels))
        print("Spectral Clustering FM:", fowlkes_mallows_score(trueLabels, labels))
        print("Spectral Clustering SC:", silhouette_score(points, labels, metric='euclidean'))
        print("Spectral Clustering CH:", calinski_harabasz_score(points, labels))
        print("Spectral Clustering DB:", davies_bouldin_score(points, labels))

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
        print("Agglomerative Clustering AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("Agglomerative Clustering HS:", homogeneity_score(trueLabels, labels))
        print("Agglomerative Clustering CS:", completeness_score(trueLabels, labels))
        print("Agglomerative Clustering VM:", v_measure_score(trueLabels, labels))
        print("Agglomerative Clustering FM:", fowlkes_mallows_score(trueLabels, labels))
        print("Agglomerative Clustering SC:", silhouette_score(points, labels, metric='euclidean'))
        print("Agglomerative Clustering CH:", calinski_harabasz_score(points, labels))
        print("Agglomerative Clustering DB:", davies_bouldin_score(points, labels))


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
        print("Birch AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("Birch HS:", homogeneity_score(trueLabels, labels))
        print("Birch CS:", completeness_score(trueLabels, labels))
        print("Birch VM:", v_measure_score(trueLabels, labels))
        print("Birch FM:", fowlkes_mallows_score(trueLabels, labels))
        print("Birch SC:", silhouette_score(points, labels, metric='euclidean'))
        print("Birch CH:", calinski_harabasz_score(points, labels))
        print("Birch DB:", davies_bouldin_score(points, labels))


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
        print("MeanShift AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("MeanShift HS:", homogeneity_score(trueLabels, labels))
        print("MeanShift CS:", completeness_score(trueLabels, labels))
        print("MeanShift VM:", v_measure_score(trueLabels, labels))
        print("MeanShift FM:", fowlkes_mallows_score(trueLabels, labels))
        print("MeanShift SC:", silhouette_score(points, labels, metric='euclidean'))
        print("MeanShift CH:", calinski_harabasz_score(points, labels))
        print("MeanShift DB:", davies_bouldin_score(points, labels))


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
    plt.title('Gaussian Mixture')
    plt.show()
    if qMetrics == True:
        print("Gaussian Mixture ARI:", adjusted_rand_score(trueLabels, labels))
        print("Gaussian Mixture AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("Gaussian Mixture HS:", homogeneity_score(trueLabels, labels))
        print("Gaussian Mixture CS:", completeness_score(trueLabels, labels))
        print("Gaussian Mixture VM:", v_measure_score(trueLabels, labels))
        print("Gaussian Mixture FM:", fowlkes_mallows_score(trueLabels, labels))
        print("Gaussian Mixture SC:", silhouette_score(points, labels, metric='euclidean'))
        print("Gaussian Mixture CH:", calinski_harabasz_score(points, labels))
        print("Gaussian Mixture DB:", davies_bouldin_score(points, labels))



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
        print("DBSCAN AMI:", adjusted_mutual_info_score(trueLabels, labels))
        print("DBSCAN HS:", homogeneity_score(trueLabels, labels))
        print("DBSCAN CS:", completeness_score(trueLabels, labels))
        print("DBSCAN VM:", v_measure_score(trueLabels, labels))
        print("DBSCAN FM:", fowlkes_mallows_score(trueLabels, labels))
        #print("DBSCAN SC:", silhouette_score(points, labels, metric='euclidean'))
        #print("DBSCAN CH:", calinski_harabasz_score(points, labels))
        #print("DBSCAN DB:", davies_bouldin_score(points, labels))




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




