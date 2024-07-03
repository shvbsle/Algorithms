#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

from collections import Counter
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, need, have, pos = 0, Counter(t), Counter(), [inf, '']
        for r, e in enumerate(s):
            have[e] += 1
            while have >= need:
                pos = min(pos, [r - l + 1, s[l : r + 1]])
                have[s[l]] -= 1 
                l+=1

        return pos[1]
     
 # @lc code=end

 