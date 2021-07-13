from random import randint
from src.dbscan import calculateEucDistance
import pandas as pd
from sklearn.preprocessing import StandardScaler

# dataset transforming and scaling
df = pd.read_csv("xclara.csv")

dataset = df.astype(float).values.tolist()

# scale it
dataset_std = StandardScaler().fit_transform(dataset)

def middle(data, array):
    mins = 0
    minidx = 0
    for i in range(len(array)):
        distWithAll = 0
        for j in range(len(array)):
            distWithAll += calculateEucDistance(data[array[i]], data[array[j]])
        if(i == 0):
            mins = distWithAll
        else:
            if(distWithAll < mins):
                mins = distWithAll
                minidx = i
    return array[minidx]
            
def isListSame(a, b):
    for i in range(len(a)):
        if(a[i] != b[i]):
            return False
    return True

def fitKMeans(data, k):
    centroid = []
    panjang = len(data)

    # random points 
    for i in range(k):
        newrand = randint(0,panjang-1)
        if(newrand not in centroid):
            centroid.append(newrand)

    # create array of members
    point_label = [0 for i in range(panjang)]
    points = [[] for i in range(len(centroid))]

    same = False
    while(not same):
        for i in range(len(data)):
            distances = []
            for j in range(len(centroid)):
                distances.append(calculateEucDistance(data[i], data[centroid[j]]))
            min_idx = distances.index(min(distances))
            points[min_idx].append(i)
            point_label[i] = min_idx

        centroidCompare = []
        for k in points:
            centroidCompare.append(middle(data, k))
        
        # coloring the center points
        for i in centroid:
            point_label[i] = len(centroid)

        if(isListSame(centroid, centroidCompare)):
            print("same")
            same = True
        else:
            print(centroid)
            centroid = centroidCompare

    return point_label


# a = [5,3,6,7,8,3,6,7,2]
# b = [3,4,5,7]
# b = a
# print(b)
# print(a.index(min(a)))
# a = fitKMeans(dataset_std,3, [399, 1050, 700])
# c, d = fitKMeans(dataset_std,3, b)
