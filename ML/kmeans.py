'''
https://www.deep-ml.com/problem/K-Means%20Clustering

K-Means Clustering (medium)
Write a Python function that implements the k-Means algorithm for clustering, starting with specified initial centroids and a set number of iterations. The function should take a list of points (each represented as a tuple of coordinates), an integer k representing the number of clusters to form, a list of initial centroids (each a tuple of coordinates), and an integer representing the maximum number of iterations to perform. The function will iteratively assign each point to the nearest centroid and update the centroids based on the assignments until the centroids do not change significantly, or the maximum number of iterations is reached. The function should return a list of the final centroids of the clusters. Round to the nearest fourth decimal.
Example
Example:
        input: points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], k = 2, initial_centroids = [(1, 1), (10, 1)], max_iterations = 10
        output: [(1, 2), (10, 2)]
        reasoning: Given the initial centroids and a maximum of 10 iterations,
        the points are clustered around these points, and the centroids are
        updated to the mean of the assigned points, resulting in the final
        centroids which approximate the means of the two clusters.
        The exact number of iterations needed may vary,
        but the process will stop after 10 iterations at most.

Learnings:
    - Do not assume that the K-means will only be 2-d coordinate system! IT CAN BE N-dimensional space!
'''

from math import *
from collections import defaultdict

def distf(point1, point2, cnum):
    L = len(point1)
    return (sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(L)])), cnum)

def newcentf(points):
    L = len(points[0])
    size = len(points)
    return tuple([round(sum([p[i] for p in points])/size, 4) for i in range(L)])

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    '''
    strategy: 
        - for num iterations:
            - iterate through the points
                - for each centroid find distance from point (track min dist)
                - assign point to min centroid and its respective clusters
            - for each cluster, update the centroid for its points
            return final centroids
    '''
    
    cluster_centroids = defaultdict(tuple)
    for cnum in range(k):
        cluster_centroids[cnum] = initial_centroids[cnum]

    for _ in range(max_iterations):
        clust_assignment = defaultdict(list)
        for p in points:
            distvals = [distf(p, cluster_centroids[cnum], cnum) for cnum in range(k)]
            _, clust = min(distvals)
            clust_assignment[clust].append(p)
        
        # update centroids
        for cnum, cvals in clust_assignment.items():
            cluster_centroids[cnum] = newcentf(cvals)

    return list(cluster_centroids.values())

points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10

print(k_means_clustering(points, k, initial_centroids, max_iterations))
print(k_means_clustering([(0, 0, 0), (2, 2, 2), (1, 1, 1), (9, 10, 9), (10, 11, 10), (12, 11, 12)], 2, [(1, 1, 1), (10, 10, 10)], 10))