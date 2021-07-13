from math import sqrt
import queue

def calculateEucDistance(a, b):
    retval = 0
    # a and b are of the same length
    for i in range(len(a)):
        retval += (a[i] - b[i])**2
    return sqrt(retval)

def neighbors(data, idxCenter, epsilon, minpt):
    points = []
    for i in range(len(data)):
        jarak = calculateEucDistance(data[idxCenter],data[i])
        if(jarak <= epsilon):
            points.append(i)
    return points

def fit(data, epsilon, minpt):
    point_label = [0]*len(data)
    points = [] # matriks 2d buat ngetauin siapa aja anggota cluster tsb

    # siapa core siapa border
    core = [] # yang punya cukup tetangga
    border = [] # yang engga

    # label dari core sama border
    core_label = -1
    border_label = -2

    # ngisi points
    for i in range(len(data)):
        points.append(neighbors(data, i, epsilon, minpt))

    # which masuk core which masuk border
    for i in range(len(points)):
        if(len(points[i]) >= minpt):
            point_label[i] = core_label
            border.append(i)
        else:
            core.append(i)

    # buat ngelabelin yang ada di border
    for i in border:
        for j in points[i]:
            if j in core:
                point_label[i] = border_label
                break
    
    # mulai clustering and labelling pake queue secara bfs
    cluster = 1
    for i in range(len(point_label)):
        # ubah yang masih core_label
        if(point_label[i] == core_label):
            point_label[i] = cluster
            que = queue.Queue()
            for j in points[i]:
                # kalo core,masukin ke dalam que buat dilanjutin
                if(point_label[j] == core_label):
                    que.put(j)
                    point_label[j] = cluster
                elif(point_label[j] == border_label):
                    point_label[j] = cluster
            while (not que.empty()):
                neighborz = points[que.get()]
                for k in neighborz:
                    if(point_label[k] == core_label):
                        que.put(k)
                        point_label[k] = cluster
                    elif(point_label[k] == border_label):
                        point_label[k] = cluster
            # udah gaada, cluster berikutnya
            cluster += 1

    return point_label, cluster
