import index.external as external
import index.internal as internal
import math.sqrt
ALGORITHM_COUNT = 6
benefit_measures = {external.f1: True,
                    external.fm: True,
                    external.jaccard: True,
                    external.rand: True,
                    internal.dunn: True,
                    internal.calinski_harabasz: True,
                    internal.gamma: False, 
                    internal.c_index: False,
                    internal.davies_bouldin: False,
                    internal.silhouette: True,
                    internal.cs_index: False,
                    internal.score_function: True,
                    internal.cop: False,
                    internal.sv: True]


external_measures = [external.f1,
                     external.fm,
                     external.jaccard,
                     external.rand]


internal_measures = [internal.dunn,
                     internal.calinski_harabasz,
                     internal.gamma, 
                     internal.c_index,
                     internal.davies_bouldin,
                     internal.silhouette,
                     internal.cs_index,
                     internal.score_function,
                     internal.cop,
                     internal.sv]

MEASURES_COUNT = len(external_measures)+len(internal_measures)

def decision_matrix(points, classes_idx, clusters_idx_list):
	r = []
	for i, measure in enumerate(external_measures+internal_measures):
		r_algorithm = []
		for i in range(ALGORITHM_COUNT):
			if i < len(external_measures):
				r_measures.append(measure(points, classes_idx, clusters_idx_list[i]))
			else:
				r_measures.append(measure(points, clusters_idx_list[i]))
		r.append(r_algorithm)
	# normalize
	for i in range(MEASURES_COUNT):
		norm_constant = 0
		for j in range(ALGORITHM_COUNT):
			norm_constant += (r[i][j] ** 2)
		norm_constant = sqrt(norm_constant)
		for j in range(ALGORITHM_COUNT):
			r[i][j] /= norm_constant

	return r

def weighted_decision_matrix(decision_mat, weights = None):
	if weights == None:
		weights = [1/float(MEASURES_COUNT) for i in range(MEASURES_COUNT)]
	for i in range(MEASURES_COUNT):
		for j in range(ALGORITHM_COUNT):
			decision_mat[i][j] *= weights[i]

	return decision_mat
			
def ideal_alternative_solution(decision_mat):
	v = []	
	for i, measure in enumerate(external_measures+internal_measures):
		if benefit_measures[measure] == True:
			v.append(max(decision_mat[i]))
		else:
			v.append(min(decision_mat[i]))
	return v

def negative_ideal_alternative_solution(decision_mat):
	v = []	
	for i, measure in enumerate(external_measures+internal_measures):
		if benefit_measures[measure] == True:
			v.append(min(decision_mat[i]))
		else:
			v.append(max(decision_mat[i]))
	return v

def separate_measures(decision_mat, v):
	d = []
	for j in range(ALGORITHM_COUNT):
		d_j = 0
		for i in range(MEASURES_COUNT):
			d_j += (decision_mat[i][j]-v[i]) ** 2
		d_j = sqrt(d_j)
		d.append(d_j)
	return d

def ratio_measures(sep_ideal_sol, sep_nideal_sol):
	r = []
	for j in range(ALGORITHM_COUNT):
		r.append(sep_nideal_sol/(sep_nideal_sol+sep_ideal_sol))
	return r
def evaluate(points, classes_idx):
	return None
	
