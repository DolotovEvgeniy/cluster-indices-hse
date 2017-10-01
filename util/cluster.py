import numpy as np
import random

def generateCluster(ndims, count, cltype = 'rectangle', size = [10, 10]):
	points = []
	for i in range(count):
		point = []
		for dim in range(ndims):
			point.append(random.uniform(0, 50))
		points.append(point)
	return points
