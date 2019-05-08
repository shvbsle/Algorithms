# multiples of 3 and 5

'''
EULER:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Performance:
233168
finished in: 0.0001709461212158203

Performance with extra condition (avoiding re computations):
233168
finished in: 9.894371032714844e-05

'''

import time

n = 1000

def get_multiples(n):
    multiples = set()
    for i in range(1,n):
        val = 3*i
        if val<n: multiples.add(val)
        else:break
    for i in range(1,n):
        # a condition to speed it up
        if i%3 == 0:
            # because all the previous multiples of 3 are covered
            continue
        val = 5*i
        if val<n: multiples.add(val)
        else:break
    return sum(multiples)


start =time.time()
print(get_multiples(n))
print('finished in:', time.time()-start)