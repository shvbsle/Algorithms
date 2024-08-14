from typing import *
from math import *
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Strategy:
            k_upper = max(piles)
            k_lower = 1
        '''
        low, high = ceil(sum(piles)/h), max(piles)
        while low < high:
            mid = (low + high) // 2
            h_mid = sum([ceil(p/mid) for p in piles])
            if h_mid > h:
                low = mid + 1
            else:
                high = mid
        return low


piles = [30,11,23,4,20]
h = 6

piles = [312884470]
h = 312884469

s = Solution()
print(s.minEatingSpeed(piles, h))

'''
Reflections:
Things that I did incorrectly:
- Forgot how to write the basic binary search loop! [IMP]
The basic struct should be as such:

l, h = 0, max([])
while l < h:
    m = (l+h)//2
    if satisfy(m):
        h = m 
    else:
        l = m + 1
return l 

- DID NOT IMMEDIATELY THINK OF APPLYING BINARY SEARCH TO THE  PROBLEM SPACE! 
    dont just think of using binary search on an array and start sorting it. Perhaps you can try to do binary search to improve your brute-force approach!
'''
