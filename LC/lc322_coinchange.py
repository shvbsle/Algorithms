import time
from typing import *

class Solution:
    def coinChange(self,coins: List[int], amount: int)-> int:
        """Bitwise BFS. 
            [1,2,5] amt = 11
            seen = 10000000000
        """
        # breakpoint()
        step, seen = 0, 1 << amount
        while seen & 1 != 1: # exit condition when right-shift of seen ends
            cur = seen
            print(bin(cur), "|", bin(seen))
            for coin in coins:
                cur |= seen >> coin
                print(bin(cur), coin)
            if cur == seen:
                return -1
            step, seen = step + 1, cur
            print(step, seen)
        return step
    
s = Solution()
c = [1, 5]
amt = 11
st = time.time()
res = s.coinChange(c, amt)
en = time.time() - st
print(res)
print(f"done in: {en}")