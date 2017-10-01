import index.internal as index
import numpy as np
print 'dunn',index.dunn(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])


print 'calinski_harabasz', index.calinski_harabasz(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])


print 'gamma', index.gamma(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'c_index', index.c_index(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])


print 'davies_bouldin', index.davies_bouldin(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'silhouette', index.silhouette(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'cs_index', index.cs_index(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'score_function', index.score_function(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'cop', index.cop(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'sv', index.sv(index.euclidian_dist, [[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])
