import numpy as np
from numpy import dot
from numpy.linalg import norm
#import math
import matplotlib.pyplot as plt
#from scipy.spatial import distance
import time
from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score, homogeneity_score, \
     completeness_score, v_measure_score, fowlkes_mallows_score, silhouette_score, calinski_harabasz_score, \
     davies_bouldin_score

points = []
labels = []
inputFile = open("input1.txt","r")
n = int(inputFile.readline())
labels = [0] * n
dupPoints = []
qMetrics = 1 - True
trueLabels = []

for i in range(0, n):
    line = inputFile.readline()
    #print(line)
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
#print(points)
dupPoints = points[:]
inputFile.close()



'''labelInput = open("trueLabels.txt","r")
totalLabels = int(labelInput.readline())
for i in range(0, totalLabels):
    line = labelInput.readline()
    getLabel = int(line)
    trueLabels.append(getLabel)
labelInput.close()'''





def euclidean(p1, p2):
    dist = (((p1[0] - p2[0]) * (p1[0] - p2[0])) + ((p1[1] - p2[1]) * (p1[1] - p2[1]))) ** 0.5
    return dist

def manhattan(p1, p2):
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return dist

def chebyshev(p1, p2):
    dist = max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
    return dist

def cosineSimilarity(p1, p2):
    #dist = (p1[0] * p2[0] + p1[1] * p2[1]) / (((p1[0] * p1[0] + p1[1] * p1[1]) ** 0.5) * ((p2[0] * p2[0] + p2[1] * p2[1]) ** 0.5))
    dist = dot(p1, p2) / (norm(p1) * norm(p2))
    return dist

def mahalanobis(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    V = np.cov(np.array([p1, p2]).T)
    IV = np.linalg.pinv(V)
    dist = distance.mahalanobis(p1, p2, IV)
    return dist

def distance(p1, p2):
    dist = euclidean(p1, p2)
    #dist = manhattan(p1, p2)
    #dist = chebyshev(p1, p2)
    #dist = cosineSimilarity(p1, p2)
    #dist = mahalanobis(p1, p2)
    return dist

def centroid(points):
    centroidX = 0.0
    centroidY = 0.0
    totalPoints = len(points)
    for i in range(totalPoints):
        centroidX += points[i][0]
        centroidY += points[i][1]
    centroidX /= totalPoints
    centroidY /= totalPoints
    centre = [centroidX, centroidY]
    return centre


def diameter(points):
    diam = -1
    totalPoints = len(points)
    for i in range(totalPoints):
        for j in range(totalPoints):
            dist = distance(points[i], points[j])
            if dist > diam:
                diam = dist
                ind1 = i
                ind2 = j
    return diam, ind1, ind2

def nearestNeighbor(point, points):
    nearestDist = 99999999.0
    totalPoints = len(points)
    for i in range(totalPoints):
        dist = distance(point, points[i])
        if dist < nearestDist:
            nearestDist = dist
            ind = i
    return nearestDist, ind

def cleanCluster(cluster):
    newCluster = []
    for i in range(len(cluster)):
        if cluster[i] != 'pop':
            newCluster.append(cluster[i])
    return newCluster

def calculateRatio(cluster):
    diam, ind1, ind2 = diameter(cluster)
    return diam / len(cluster)
    #return diam

def calculateRatio2(cluster):
    diam, ind1, ind2 = diameter(cluster)
    return diam
            

def initialDivide(points):
    C_1 = []
    C_2 = []
    diam, ind1, ind2 = diameter(points)
    #print(diam)
    C_1.append(points[ind1])
    C_2.append(points[ind2])
    if ind1 < ind2:
        points.pop(ind1)
        points.pop(ind2 - 1)
    else:
        points.pop(ind2)
        points.pop(ind1 - 1)
    '''print(C_1)
    print(C_2)
    print()'''
    while points:
        point1 = C_1[-1]
        #print(point1, end=' ')
        nearestDist1, ind1 = nearestNeighbor(point1, points)
        C_1.append(points[ind1])
        points.pop(ind1)
        if points:
            point2 = C_2[-1]
            #print(point2)
            nearestDist2, ind2 = nearestNeighbor(point2, points)
            C_2.append(points[ind2])
            points.pop(ind2)
    #print(C_1)
    #print()
    #print(C_2)
    #print()
    return C_1, C_2
    
def temporaryClusterCreation(C_1, C_2):
    C_temp = []
    centroid1 = centroid(C_1)
    centroid2 = centroid(C_2)
    centroidTotal = [(centroid1[0] + centroid2[0]) / 2, (centroid1[1] + centroid2[1]) / 2]
    #print(centroid1, centroid2, centroidTotal)
    totalC_1 = len(C_1)
    totalC_2 = len(C_2)
    indToBePopped1 = []
    indToBePopped2 = []
    for i in range(totalC_1):
        distCent1 = distance(C_1[i], centroid1)
        distCentTotal = distance(C_1[i], centroidTotal)
        if distCent1 > distCentTotal:
            C_temp.append(C_1[i])
            indToBePopped1.append(i)
    for i in range(totalC_2):
        distCent2 = distance(C_2[i], centroid2)
        distCentTotal = distance(C_2[i], centroidTotal)
        if distCent2 > distCentTotal:
            C_temp.append(C_2[i])
            indToBePopped2.append(i)
    for i in range(len(indToBePopped1)):
        C_1[indToBePopped1[i]] = 'pop'
    for i in range(len(indToBePopped2)):
        C_2[indToBePopped2[i]] = 'pop'
    
    C_1 = cleanCluster(C_1)
    C_2 = cleanCluster(C_2)
    #print(C_temp)
    #print(len(C_1), len(C_2), len(C_temp))
    #print(C_2)
    #print()
    #print(len(C_temp))
    return C_1, C_2, C_temp

def mergeByGreedyHeuristics(C_1, C_2, C_temp):
    C_1_star = C_1[:]
    C_2_star = C_2[:]
    C_1_star.extend(C_temp)
    C_2_star.extend(C_temp)
    
    #print(C_2_star)
    
    #ratio1 = calculateRatio(C_1) + calculateRatio(C_2_star)
    #ratio2 = calculateRatio(C_2) + calculateRatio(C_1_star)
    
    ratio1 = calculateRatio(C_2_star)
    ratio2 = calculateRatio(C_1_star)
    
    if ratio1 <= ratio2:
        C_2 = C_2_star[:]
    else:
        C_1 = C_1_star[:]
    #print(len(C_1), len(C_2))
    #print(C_2)
    return C_1, C_2

def filtering(C_1, C_2):
    totalC_1 = len(C_1)
    centroid1 = centroid(C_1)
    centroid2 = centroid(C_2)
    for i in range(totalC_1):
        distCent1 = distance(C_1[i], centroid1)
        distCent2 = distance(C_1[i], centroid2)
        if distCent1 > distCent2:
            C_2.append(C_1[i])
            C_1[i] = 'pop'
            #print('a')
    C_1 = cleanCluster(C_1)
    

    totalC_2 = len(C_2)
    centroid1 = centroid(C_1)
    centroid2 = centroid(C_2)
    for i in range(totalC_2):
        distCent1 = distance(C_2[i], centroid1)
        distCent2 = distance(C_2[i], centroid2)
        if distCent1 < distCent2:
            C_1.append(C_2[i])
            C_2[i] = 'pop'
            #print('b')
    C_2 = cleanCluster(C_2)
    return C_1, C_2


def dhclustering(points):
    points_ = np.array(points)
    plt.scatter(points_[:, 0], points_[:, 1], color="black")
    plt.show()
    '''colorList = ['blue', 'red', 'green', 'darkorange', 'black', 'lime', 'turquoise', 'deeppink', \
                 'slategray', 'pink', 'peru', 'cyan', 'tan', 'yellow', 'khaki', 'crimson', \
                 'indigo', 'darkorchid', 'darkseagreen']'''
    k = 3
    ratios = []
    currClusters = []
    start_time = time.time()
    
    for i in range(k - 1):
        C_1, C_2 = initialDivide(points)
        print("id done", i + 1)
        C_1, C_2, C_temp = temporaryClusterCreation(C_1, C_2)
        print("tcc done", i + 1)
        C_1, C_2 = mergeByGreedyHeuristics(C_1, C_2, C_temp)
        print("mbgh done", i + 1)
        C_1, C_2 = filtering(C_1, C_2)
        print("flt done", i + 1)
        
        currClusters.append(C_1)
        currClusters.append(C_2)
        
        ratio1 = calculateRatio(C_1)
        ratios.append(ratio1)
        ratio2 = calculateRatio(C_2)
        ratios.append(ratio2)
        
        maxRatio = -1
        maxIndex = -1
        totalRatio = 0.0
        index = -1
        for j in ratios:
            #print(j)
            totalRatio += j
            index += 1
            if j > maxRatio:
                maxIndex = index
                maxRatio = j
        print("Average Total Ratio: ", totalRatio / len(ratios))
        
        if i != k - 2:
            ratios.pop(maxIndex)
            points = currClusters[maxIndex]
            currClusters.pop(maxIndex)
        print()
    
    end_time = time.time()
    print("total execution time: %s seconds" % (end_time - start_time))
    
    
    '''tempColor = ["blue", "red", "purple"]
    tempMarker = ['^', 'x', 's']'''
    #plt.xlim(1, 23)
    #plt.ylim(-2.5, 2.5)
    
    for i in range(len(currClusters)):
        cluster = np.array(currClusters[i])
        markerNo = str(i + 1)
        markerNo = '$' + markerNo + '$'
        #plt.scatter(cluster[:, 0], cluster[:, 1], color=colorList[i], marker=markerNo)
        plt.scatter(cluster[:, 0], cluster[:, 1], marker=markerNo)
        #plt.scatter(cluster[:, 0], cluster[:, 1], color=tempColor[i], marker=tempMarker[i])
    plt.show()
    
    for i in range(len(currClusters)):
        cluster = currClusters[i]
        #print(cluster[:][0])
        #print(len(cluster))
        #print(dupPoints[4][1])
        #break
        for j in range(len(cluster)):
            for l in range(len(dupPoints)):
                #print(cluster[:][0])
                if cluster[:][j] == dupPoints[l]:
                    labels[l] = i + 1
    #print(labels)
    #print(dupPoints)
    if qMetrics == True:
        pnt = np.array(dupPoints)
        #print("Affinity Propagation RI:", rand_score(trueLabels, labels))
        print("Our algorithm ARI:", adjusted_rand_score(trueLabels, labels))
        #print("Our algorithm AMI:", adjusted_mutual_info_score(trueLabels, labels))
        #print("Our algorithm HS:", homogeneity_score(trueLabels, labels))
        #print("Our algorithm CS:", completeness_score(trueLabels, labels))
        #print("Our algorithm VM:", v_measure_score(trueLabels, labels))
        #print("Our algorithm FM:", fowlkes_mallows_score(trueLabels, labels))
        print("Our algorithm SC:", silhouette_score(pnt, labels, metric='euclidean'))
        #print("Our algorithm CH:", calinski_harabasz_score(dupPoints, labels))
        #print("Our algorithm DB:", davies_bouldin_score(points, labels))
    
    
    
    
    
    





def main():
    dhclustering(points)
          
if __name__ == "__main__":
    main()