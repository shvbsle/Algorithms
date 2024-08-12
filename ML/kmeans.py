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

def distf(point1, point2, clusternum):
    L = len(point1)
    dist = sqrt(sum([(point1[i] - point2[i])**2 for i in range(L)]))
    return (dist, clusternum)

def centroidf(points):
    L = len(points[0])
    num_points = len(points)
    new_centroids = tuple([ round(sum([points[row][col] for row in range(num_points)])/num_points, 4) for col in range(L) ])
    return new_centroids 


def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    '''
    Strategy:
        - for max_iterations:
            - go through all the points
                - figure out which centroid is closest to the current point (assign that centroids cluster number as the poitns cluster)
            - for all points, update the centroids
    '''

    centroid_dict = defaultdict(tuple)
    for i in range(len(initial_centroids)):
        centroid_dict[i] = initial_centroids[i]
    
    for _ in range(max_iterations):
        cluster_allocation = defaultdict(list)
        for p in points:
            _, cnum = min([distf(p, centroid_dict[i], i) for i in range(k)])
            cluster_allocation[cnum].append(p)

        for cluster_num, cluster_points in cluster_allocation.items():
            centroid_dict[cluster_num] = centroidf(cluster_points)
            
    return list(centroid_dict.values())

points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10

print(k_means_clustering(points, k, initial_centroids, max_iterations))
print(k_means_clustering([(0, 0, 0), (2, 2, 2), (1, 1, 1), (9, 10, 9), (10, 11, 10), (12, 11, 12)], 2, [(1, 1, 1), (10, 10, 10)], 10))