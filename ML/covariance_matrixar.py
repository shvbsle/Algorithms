'''
https://www.deep-ml.com/problem/Calculate%20Covariance%20Matrix

Calculate Covariance Matrix (medium)
Write a Python function that calculates the covariance matrix from a list of vectors. Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.
Example
Example:
        input: vectors = [[1, 2, 3], [4, 5, 6]]
        output: [[1.0, 1.0], [1.0, 1.0]]
        reasoning: The dataset has two features with three observations each. The covariance between each pair of features (including covariance with itself) is calculated and returned as a 2x2 matrix.


'''

from typing import *
import numpy as np 

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    
    dim = len(vectors) 
    means = [] # \hat_x
    for vec in vectors:
        means.append(sum(vec)/len(vec))

    output = [[0.0 for _ in range(dim)] for _ in range(dim)]

    varf = lambda x, x_hat: sum([ (xi - x_hat)**2 for xi in x])/(len(x)-1) 
    covarf = lambda x, x_hat, y, y_hat: sum([ (x[i] - x_hat)*(y[i] - y_hat) for i in range(len(x))])/(len(x)-1)

    diags = set()
    for i in range(dim):
        for j in range(dim):
            if i == j:
                output[i][j] = varf(vectors[i], means[i])
            else:
                if (j, i) in diags:
                    output[i][j] = output[j][i]
                else:
                    output[i][j] = covarf(vectors[i], means[i], vectors[j], means[j])
                    diags.add((j,i))
    return output
    
vectors = [[1, 2, 3], [4, 5, 6]]

output = calculate_covariance_matrix(vectors)

print(output)

