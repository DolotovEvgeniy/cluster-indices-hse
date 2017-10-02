import index.internal as index
import numpy as np
print 'dunn',index.dunn([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])


print 'calinski_harabasz', index.calinski_harabasz([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])


print 'gamma', index.gamma([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'c_index', index.c_index([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])


print 'davies_bouldin', index.davies_bouldin([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'silhouette', index.silhouette([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'cs_index', index.cs_index([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'score_function', index.score_function([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'cop', index.cop([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])

print 'sv', index.sv([[1, 2],[4,4] ,[3, 4] ,[10 , 10]], [1,1,1, 0])
