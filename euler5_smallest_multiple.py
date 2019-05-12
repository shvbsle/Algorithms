# euler 5

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math
primes_less_than_20 = [2,3,5,7,11,13,17,19]
# 16 contains all possible multiples of 2 under 20
nums_less_than_20 = [16, 9,5,7,11,13,17,19]
num=1
for i in nums_less_than_20:
    num*=i 
print(num)
import copy
num2 = copy.copy(num)
for i in range(1,21):
    if num2%i !=0:
        print('fail', i)
        num2*=i
print('pass')