from math import sqrt

def f1(points, classes, clusters):
    classes_count  = len(set(classes))
    clusters_count = len(set(clusters))
    f1_ij = []
    for i in set(classes):
        f1_i = []
        for j in set(clusters):
            ni = classes.count(i)
            nj = clusters.count(j)
            nij = zip(classes, clusters).count((i,j))
            if nij == 0:
                f1 = 0
            else:
                precision = nij/float(ni)
                recall    = nij/float(nj)
                f1 = (2*precision*recall)/(precision+recall)
            f1_i.append(f1)
        f1_ij.append(f1_i)

    index = 0
    N = len(points)
    for j in range(clusters_count):
        nj = clusters.count(j)
        index += (nj/float(N))*max([f1_ij[i][j] for i in range(classes_count)])
    
    return index

def fm(points, classes, clusters):
    SS = 0
    SD = 0
    DS = 0
    DD = 0
    print len(points)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if clusters[i] == clusters[j]:
                if classes[i] == classes[j]:
                    SS += 1
                else:
                    SD += 1
            else:
                if classes[i] == classes[j]:
                    DS += 1
                else:
                    DD += 1
    index = SS/sqrt((SS+SD)*(SS+DS))
    return index



def jaccard(points, classes, clusters):
    SS = 0
    SD = 0
    DS = 0
    DD = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if clusters[i] == clusters[j]:
                if classes[i] == classes[j]:
                    SS += 1
                else:
                    SD += 1
            else:
                if classes[i] == classes[j]:
                    DS += 1
                else:
                    DD += 1
    
    index = SS/float(SS+SD+DS)
    return index
	

def rand(points, classes, clusters):
    SS = 0
    SD = 0
    DS = 0
    DD = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if clusters[i] == clusters[j]:
                if classes[i] == classes[j]:
                    SS += 1
                else:
                    SD += 1
            else:
                if classes[i] == classes[j]:
                    DS += 1
                else:
                    DD += 1
    index = (SS+DD)/float(SS+DS+SD+DD)
    return index
	
