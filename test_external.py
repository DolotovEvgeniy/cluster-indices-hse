import util.cluster as cluster
import matplotlib.pyplot as plt
from index.external import *
import csv
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import util.dataset as dataset
def argmax(scores):
	return max(enumerate(scores), key=lambda x: x[1])[0]+1
X, classes = dataset.load(sys.argv[1])
print 'Samples count: ', len(X), ', class count', len(set(classes))

max_cluster_count = int(sys.argv[2])
clusterizer_type = sys.argv[3]
rand_scores    = []
jaccard_scores = []
fm_scores      = []
f1_scores      = []
file = open('res.txt', 'w')
for i in range(1, max_cluster_count+1):
	#print '----------', i, '----------'
	clusterizer = None
	if clusterizer_type == 'kmeans':
		clusterizer = KMeans(n_clusters=i).fit(np.array(X))
	elif clusterizer_type == 'ward':
		clusterizer = AgglomerativeClustering(n_clusters=i).fit(np.array(X))

	clusters = clusterizer.labels_.tolist()
	
	########## Rand ###########
	rand_score = rand(X, classes, clusters)
	rand_scores.append(rand_score)
	#print 'Rand index: ', rand_score
	#file.write(str(rand_score)+',')
	######### Jaccard #########
	jaccard_score = jaccard(X, classes, clusters)
	jaccard_scores.append(jaccard_score)
	#print 'Jaccard index: ', jaccard_score
	#file.write(str(jaccard_score)+',')
	############ FM ###########
	fm_score = fm(X, classes, clusters)
	fm_scores.append(fm_score)
	#print 'FM index:', fm_score
	#file.write(str(fm_score)+',')
	############ F1 ###########
	f1_score = f1(X, classes, clusters)
	f1_scores.append(f1_score)
	#print 'F1: ', f1_score
	#file.write(str(f1_score)+'\n')
	#print '-----------------------'

	############ Best result ############
print 'Rand best:', argmax(rand_scores)
print 'Jaccard best:', argmax(jaccard_scores)
print 'FM best:', argmax(fm_scores)
print 'F1 best:', argmax(f1_scores)
