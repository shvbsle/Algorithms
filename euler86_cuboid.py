# euler 86
import math
import time
import operator as op
from functools import reduce
from itertools import combinations

# a smarter distance func
dist2 = lambda s: math.sqrt(s)

# spider is at start of a
# fly is at the end of c
# square lookup:
square_lookup = {}
familiar_pair = {}
familiar_combinations = {}
seen_results = {}
def shortest_dist2(a, b, c):
    if a not in square_lookup:
        square_lookup[a] = a**2
    if b not in square_lookup:
        square_lookup[b] = b**2
    if c not in square_lookup:
        square_lookup[c] = c**2
    base = square_lookup[c]+square_lookup[b]+square_lookup[a]
    s1 = base+(2*b*c)
    s2 = base+(2*a*c)
    s3 = base+(2*a*b)
    if s1 not in familiar_pair:
        familiar_pair[s1] = dist2(s1)
    if s2 not in familiar_pair:
        familiar_pair[s2] = dist2(s2)
    if s3 not in familiar_pair:
        familiar_pair[s3] = dist2(s3)
    p1 = familiar_pair[s1]
    p2 = familiar_pair[s2]
    p3 = familiar_pair[s3]
    return min(p1, p2, p3)

def ncr(n, r): 
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def dim_generator2(M):
    for i in range(1, M+1):
        for j in range(1, M+1):
            yield (i, i, j)
    combs = list(combinations([i for i in range(1,M+1)], 3))
    for a,b,c in combs:
        yield (a, b, c)

start = time.time()
seen_dims = {}
total_ints = 0
upper_lim = 1000000
upper_lim = 1000
upper_lim = 500
for a,b,c in dim_generator2(upper_lim):
    S = [a,b,c]
    S.sort()
    dim_set = ','.join(list(map(str,S)))
    if dim_set in seen_dims:
        continue
    seen_dims[dim_set] = True
    distance = shortest_dist2(a,b,c)
    if distance.is_integer():
        total_ints+=1
print(total_ints)

print("finished in: ", time.time()-start)

# val = upper_lim + (upper_lim*(upper_lim-1))+ ncr(upper_lim, 3)
# print(val, upper_lim**3)
# the current loop generates
# 1000000000000000000
# when the total uniques are 
# 166667166667000000

