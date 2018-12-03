#-*-coding:utf8;-*-
#qpy:3
#qpy:console

costs = {'a':1,
        'b':1,
        'c':1,
        'aba':2,
        'caa':2,
        'baac':3}
import time
start = time.time()

# minimum string cost
# very similar to rod cutting

tabular = {}
def solve(s):
    if s in tabular: return tabular[s]
    if len(s) == 1 and s in costs:
        tabular[s] = costs[s]
        return tabular[s]
    if len(s) < 1: return 0
    c=[]
    for i in range(len(s)):
        if s[-i:] in costs:
           c.append(solve(s[:-i])+costs[s[-i:]])
    print(s, min(c), c)
    tabular[s] = min(c)
    return tabular[s]

ans= solve('abaacaabaac')
print(ans)
print('solved in:', time.time()-start)
