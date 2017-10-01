from math import *
from itertools import combinations


def splitClusters(points, clusters_idx):
	setOfCluster = set(clusters_idx)
	clusters = []
	for cl in setOfCluster:
		cluster = []
		for i, point in enumerate(points):
			if clusters_idx[i] == cl:
				cluster.append(point)
		clusters.append(cluster)
	return clusters


def euclidian_dist(a, b):
	if type(a) is int:
		return fabs(a-b)
	if len(a) != len(b):
		raise Exception('dimension of object are not equal: %d and %d' % (len(a), len(b)))
	dist = 0
	for i in range(len(a)):
		dist += (a[i] - b[i]) ** 2
	return sqrt(dist) 

		
def nearest_neighbour_dist(norm, points1, points2):
	min_dist = float('inf')	
	for p1 in points1:
		for p2 in points2:
			dist = norm(p1, p2)
			min_dist = min(min_dist, dist)
	return min_dist


def max_cluster_diam(norm, points):
	max_dist = 0
	for pair in combinations(points, 2):
		dist = norm(pair[0], pair[1])
		max_dist = max(max_dist, dist)
	return max_dist
	

def mean(points):
	N = len(points)
	mean_result = [0 for i in range(len(points[0]))]
	for p in points:
		for d in range(len(p)):
			mean_result[d] += p[d]/N
	return mean_result

def dl_elem(norm, point1, point2, points, clusters_idx):
	count = 0
	for i in range(len(points)):
		for j in range(len(points)):
			if clusters_idx[i] != clusters_idx[j]:
				if norm(point1, point2) > norm(points[i], points[j]):
					count += 1
	return count

def dl(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	total_sum = 0
	for cluster in clusters:
		for pair in combinations(cluster, 2):
			total_sum += dl_elem(norm, pair[0], pair[1], points, clusters_idx)
	return total_sum


def pairCount(points):
	N = len(points)
	return N*(N-1)/2


def nw(points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	count = 0
	for cluster in clusters:
		count += pairCount(cluster)
	return count
	
########################################################

def dunn(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	if len(clusters) == 1:
		return 0
	separation = min([min([nearest_neighbour_dist(norm, ck, cl) for cl in clusters if cl != ck]) for ck in clusters])	

	cohesion = max([max_cluster_diam(norm, cluster) for cluster in clusters])
	return separation/cohesion


def calinski_harabasz(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	if len(clusters) == 1:
		return 0
	N = len(points)
	K = len(clusters)

	separation = 0
	for cluster in clusters:
		separation += len(cluster)*norm(mean(cluster), mean(points))

	cohesion = 0
	for cluster in clusters:
		cluster_center = mean(cluster)
		for p in cluster:
			cohesion += norm(p, cluster_center)
		
	return ((N-K)/float(K-1))*(separation/cohesion)


def gamma(norm, points, clusters_idx):
	if len(set(clusters_idx)) == 1:
		return float('inf')
	return dl(norm, points, clusters_idx)/float(nw(points, clusters_idx)*(pairCount(points)-nw(points, clusters_idx)))


def c_index(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	s = 0
	for cluster in clusters:
		for pair in combinations(cluster, 2):
			s += norm(pair[0], pair[1])
	distances = []
	for pair in combinations(points, 2):
			distances.append(norm(pair[0], pair[1]))
	distances = sorted(distances)
	nw_value = nw(points, clusters_idx)
	s_min = 0
	for i in range(nw_value):
		s_min += distances[i]
	s_max = 0
	for i in range(len(distances)-nw_value, len(distances)):
		s_max += distances[i]

	return (s-s_min)/float(s_max-s_min)


def davies_bouldin(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	centers = []
	for cluster in clusters:
		centers.append(mean(cluster))
	
 	sum_result = 0
	for i in range(len(clusters)):
		s_i = 0
		for p in clusters[i]:
			s_i += norm(p, centers[i])
		s_i = s_i / len(clusters[i])
		max_value = 0
		for j in range(len(clusters)):
			if i == j:
				continue
			s_j = 0
			for p in clusters[j]:
				s_j += norm(p, centers[j])
			s_j = s_j / len(clusters[j])
			value = (s_i+s_j)/norm(centers[i], centers[j])
			max_value = max(max_value, value)
		sum_result += max_value
	return sum_result/len(clusters)
	
##### Silhouette #######

def a(norm, point, cluster):
	sum_result = 0
	for p in cluster:
		sum_result += norm(point, p)
	return sum_result/len(cluster)

def b(norm, point, cluster_num, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	min_value = float('inf')
	for i in range(len(clusters)):
		if i == cluster_num:
			continue
		value = 0
		for p in clusters[i]:
			value += norm(p, point)
		value = value/len(clusters[i])
		min_value = min(min_value, value)
	return min_value


def silhouette(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	sum_result = 0
	for i, cluster in enumerate(clusters):
		for p in cluster:
			b_value = b(norm, p, i, points, clusters_idx)
			a_value = a(norm, p, cluster)
			sum_result += (b_value-a_value)/max(b_value, a_value)
	return sum_result/len(points)

########## CS #############

def cs_index(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	cohesion = 0
	for cluster in clusters:
		value = 0
		for p1 in cluster:
			max_value = 0
			for p2 in cluster:
				max_value = max(max_value, norm(p1, p2))
			value += max_value
		value = value/len(cluster)
		cohesion += value
	
	centers = []
	for cluster in clusters:
		centers.append(mean(cluster))
	separation = 0
	for i in range(len(clusters)):
		min_value = float('inf')
		for j in range(len(clusters)):
			if i == j:
				continue
			else:	
				min_value = min(min_value, norm(centers[i], centers[j]))
		separation += min_value
			 
	return cohesion/separation

######### score function #########


def bcd(norm, points, clusters_idx):
	N = len(points)
	K = len(set(clusters_idx))
	clusters = splitClusters(points, clusters_idx)
	X = mean(points)
	result_sum = 0
	for cluster in clusters:	
		result_sum += len(cluster)*norm(mean(cluster), mean(points))
	return result_sum/(N*K)

def wcd(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	result_sum = 0
	for cluster in clusters:
		value = 0
		for p in cluster:
			value += norm(p, mean(cluster))
		value = value/len(cluster)
		result_sum += value
	return result_sum

def score_function(norm, points, clusters_idx):
	return 1-1/exp(bcd(norm, points, clusters_idx)+wcd(norm, points, clusters_idx))


####### cop ##########
def cop(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	N = len(points)
	result_sum = 0
	for i, cluster in enumerate(clusters):
		dist = 0
		for p in cluster:
			dist += norm(p, mean(cluster))
		min_max = float('inf')
		for j in range(len(points)):
			if clusters_idx[j] != i:
				max_dist = 0
				for p in cluster:
					max_dist = max(max_dist, norm(p, points[j]))
				min_max = min(min_max, max_dist)
		result_sum += dist/min_max
	return result_sum
					 
######### sv ###########

def sv(norm, points, clusters_idx):
	clusters = splitClusters(points, clusters_idx)
	centers = []
	for cluster in clusters:
		centers.append(mean(cluster))

	separation = 0
	for i, cluster in enumerate(clusters):
		min_value = float('inf')
		for j in range(len(clusters)):
			if i ==j:
				continue
			min_value = min(min_value, norm(centers[i], centers[j]))
		separation += min_value
	
	cohesion = 0
	for cluster in clusters:
		dist = []
		for p in cluster:
			dist.append(norm(p, mean(cluster)))
		max_sum = 0
		dist = sorted(dist)
		for i in range(len(dist)-max(1, 0.1*len(cluster)), len(dist)):
			max_sum += dist[i]
		cohesion += 10.0/len(cluster)*max_sum
		
	return separation/cohesion


