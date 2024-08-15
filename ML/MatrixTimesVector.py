'''
Matrix times Vector (easy)
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
Example
Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
'''

from typing import *

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    # a -> n x m  b => m * k
    if len(a[0]) != len(b): return -1
    c = []
    for row in a:
        ele = sum([e[0] * e[1] for e in zip(row, b)])
        c.append(ele)
    
    return c 

a = [[1,2],[2,4]]
b = [1,2]

print(matrix_dot_vector(a, b))
