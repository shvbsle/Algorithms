# euler 86
import math
import time
dist = lambda d1, d2: math.sqrt((d1**2)+(d2**2))
# spider is at start of a
# fly is at the end of c
def shortest_dist(a, b, c):
    p1 = dist(a, b+c)
    p2 = dist(c, a+b)
    p3 = dist(b, a+c)
    return min(p1, p2, p3)

def dim_generator(M):
    for i in range(1, M+1):
        for j in range(1, M+1):
            for k in range(1, M+1):
                yield (i, j, k)

start = time.time()
seen_dims = {}
total_ints = 0
upper_lim = 1000000
# upper_lim = 500
for a,b,c in dim_generator(upper_lim):
    S = [a,b,c]
    S.sort()
    dim_set = ','.join(list(map(str,S)))
    if dim_set in seen_dims:
        continue
    seen_dims[dim_set] = True
    distance = shortest_dist(a,b,c)
    if distance.is_integer():
        total_ints+=1
print(total_ints)
print("finished in: ", time.time()-start)
    