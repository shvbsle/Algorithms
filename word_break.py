# SHIV's code for word break

'''
2
12
i like sam sung samsung mobile ice cream icecream man go mango
ilike
12
i like sam sung samsung mobile ice cream icecream man go mango
idontlike

Non-Memoized:
1
0
finished in:  0.00020813941955566406

Memoized:
1
0
finished in:  7.009506225585938e-05

Crazyy!
'''
import time
tn = int(input())

memoize = {}
def solve(q, words):
	if q in memoize: return memoize[q]
	if len(q) == 1:
		if q[0] in words: return 1
		else: return 0
	segments = []
	for i in range(len(q)-1,0,-1):
		left, right = q[:i], q[i:]
		if solve(left, words) == 1:
			segments.append(right)
	for seg in segments:
		if seg in words:
			memoize[q] = 1
			return memoize[q]
	memoize[q] = 0
	return memoize[q]

start = time.time()
for i in range(tn):
	w_n = int(input())
	words = input().split()
	query = input()
	ans = solve(query, words)
	print(ans)

print("finished in: ", time.time()-start)
