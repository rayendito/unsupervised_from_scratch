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
    x = 0
    y = 0
    n_members = len(array)
    for i in array:
        x += data[i][0]
        y += data[i][1]
    return [round(x/n_members, 2), round(y/n_members, 2)]
            
def is2DListSame(a, b):
    # asumsi ukuran sama
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j] != b[i][j]):
                return False
    return True

def fitKMeans(data, k):
    centroid = []
    panjang = len(data)

    # random points 
    udah = []
    for i in range(k):
        newrand = randint(0,panjang-1)
        if(newrand not in udah):
            centroid.append(data[newrand].tolist())
            udah.append(newrand)

    # create array of members
    point_label = [0 for i in range(panjang)]
    points = [[] for i in range(len(centroid))]

    same = False
    while(not same):
        for i in range(panjang):
            distances = []
            for j in range(len(centroid)):
                distances.append(calculateEucDistance(data[i], centroid[j]))
            min_idx = distances.index(min(distances))
            points[min_idx].append(i)
            point_label[i] = min_idx

        centroidCompare = []
        for k in points:
            centroidCompare.append(middle(data, k))
        
        # # coloring the center points
        # for i in centroid:
        #     point_label[i] = len(centroid)

        if(is2DListSame(centroid, centroidCompare)):
            print("same")
            same = True
        else:
            print(centroid)
            centroid = centroidCompare


    return point_label