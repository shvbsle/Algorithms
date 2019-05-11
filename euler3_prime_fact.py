# euler 3 prime factorization

# OMG so effing EZZZZ
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys
sys.setrecursionlimit(1000000)
N = 13195
N = 600851475143
# N = 2

facs = {}
initial_primes = [2,3,5,7,11,13, 17, 19, 23, 29]

def factorize(num):
    if num in facs:
        return facs[num]
    for i in range(2, 10000):
        if num%i == 0 and i < num:
            print(num, i)
            divisor_facs = factorize(i)
            dividend_facs = factorize(int(num/i))
            facs[num] = list(set(divisor_facs+dividend_facs))
            return facs[num]
    return [num]

factors = factorize(N)
print(factors)
print(max(factors))