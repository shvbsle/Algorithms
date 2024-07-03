class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        
        i, j = 0, 0
        currc = s[i]
        budget = k
        maxl = 0
        while i <= j and j < len(s):
            if s[j] == currc:
                j+=1
            elif budget > 0:
                j+=1
                budget -= 1
            else:
                maxl = max(maxl, len(s[i:j]))
                budget = k
                while s[i] == currc:
                    i += 1
                currc = s[i]
                j = i
        maxl = max(maxl, len(s[i:j]))
        return maxl


s = Solution()
ss = "AABABBA"
k = 1
res = s.characterReplacement(ss, k)
print(res)
