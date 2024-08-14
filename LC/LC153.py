from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            m = (l + h) // 2
            if nums[h] <= nums[m]:
                l = m + 1 
            else:
                h = m
        return nums[l]

s = Solution()

nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
print(s.findMin(nums))

'''
Reflections:
- I had a massive brainfart when writing the comparison operator
-- I wrote if nums[h] <= nums[m]: h = m
--- This effectively REMOVES/IGNORES the solution!
--- My brain just did poorly at arithemetic comparison
'''
