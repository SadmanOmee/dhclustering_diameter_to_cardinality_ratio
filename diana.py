import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

points = []
inputFile = open("input1.txt","r")
n = int(inputFile.readline())

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
    
    singlePoint = []
    singlePoint.append(x)
    singlePoint.append(y)
    points.append(singlePoint)
#print(points)
inputFile.close()

distMat = []
for i in range(len(points)):
    distFromI = []
    for j in range(len(points)):
        distEuclidean = (((points[i][0] - points[j][0]) * (points[i][0] - points[j][0])) + ((points[i][1] - points[j][1]) * (points[i][1] - points[j][1]))) ** 0.5
        distFromI.append(distEuclidean)
    distMat.append(distFromI)

mat = np.array(distMat)
all_elements = []
for i in range(len(points)):
    all_elements.append(i)
#all_elements = ['a','b','c','d','e']
dissimilarity_matrix = pd.DataFrame(mat,index=all_elements, columns=all_elements)
#print(dissimilarity_matrix)
_points = np.array(points)
plt.scatter(_points[:, 0], _points[:, 1], color="black")
plt.show()

def avg_dissim_within_group_element(ele, element_list):
    max_diameter = -np.inf
    sum_dissm = 0
    for i in element_list:
        sum_dissm += dissimilarity_matrix[ele][i]   
        if( dissimilarity_matrix[ele][i]  > max_diameter):
            max_diameter = dissimilarity_matrix[ele][i]
    if(len(element_list)>1):
        avg = sum_dissm/(len(element_list)-1)
    else: 
        avg = 0
    return avg

def avg_dissim_across_group_element(ele, main_list, splinter_list):
    if len(splinter_list) == 0:
        return 0
    sum_dissm = 0
    for j in splinter_list:
        sum_dissm = sum_dissm + dissimilarity_matrix[ele][j]
    avg = sum_dissm/(len(splinter_list))
    return avg
    
    
def splinter(main_list, splinter_group):
    most_dissm_object_value = -np.inf
    most_dissm_object_index = None
    for ele in main_list:
        x = avg_dissim_within_group_element(ele, main_list)
        y = avg_dissim_across_group_element(ele, main_list, splinter_group)
        diff= x -y
        if diff > most_dissm_object_value:
            most_dissm_object_value = diff
            most_dissm_object_index = ele
    if(most_dissm_object_value>0):
        return  (most_dissm_object_index, 1)
    else:
        return (-1, -1)
    
def split(element_list):
    main_list = element_list
    splinter_group = []    
    (most_dissm_object_index,flag) = splinter(main_list, splinter_group)
    while(flag > 0):
        main_list.remove(most_dissm_object_index)
        splinter_group.append(most_dissm_object_index)
        (most_dissm_object_index,flag) = splinter(element_list, splinter_group)
    
    return (main_list, splinter_group)

def max_diameter(cluster_list):
    max_diameter_cluster_index = None
    max_diameter_cluster_value = -np.inf
    index = 0
    for element_list in cluster_list:
        for i in element_list:
            for j in element_list:
                if dissimilarity_matrix[i][j]  > max_diameter_cluster_value:
                    max_diameter_cluster_value = dissimilarity_matrix[i][j]
                    max_diameter_cluster_index = index
        
        index +=1
    
    if(max_diameter_cluster_value <= 0):
        return -1
    
    return max_diameter_cluster_index
    

def diana():
    num_clusters = 2
    #currClusters = []
    current_clusters = ([all_elements])
    level = 1
    index = 0
    #while(index!=-1):
    while(level < num_clusters):
        #print(level, points)
        (a_clstr, b_clstr) = split(current_clusters[index])
        del current_clusters[index]
        current_clusters.append(a_clstr)
        current_clusters.append(b_clstr)
        index = max_diameter(current_clusters)
        level +=1
        print(level - 1, "done")
    
    #print()
    
    for i in range(len(current_clusters)):
        clusterIndices = current_clusters[i]
        aCluster = []
        for j in range(len(clusterIndices)):
            aCluster.append(points[current_clusters[i][j]])
        aCluster = np.array(aCluster)
        markerNo = str(i + 1)
        markerNo = '$' + markerNo + '$'
        #print(aCluster)
        plt.scatter(aCluster[:, 0], aCluster[:, 1], marker=markerNo)
    plt.show()
    








def main():
    diana()
          
if __name__ == "__main__":
    main()