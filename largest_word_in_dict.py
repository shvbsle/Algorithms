# SHIV's code for largest word in the dictionary

'''
2
4
ale apple monkey plea
abpcplea
4
pintu geeksfor geeksgeeks forgeek
geeksforgeeks

Non-memoized soln
-----------------------
finished in:  0.056343793869018555


Memoized soln
-----------------------
finished in:  0.0030579566955566406
'''
import time
tn = int(input())

overlap_dict = {}
def solve(query, wdict, dels):
	if query in overlap_dict: return overlap_dict[query]
	if dels < 0:
		overlap_dict[query] = False
		return False
	if query in wdict:
		overlap_dict[query] = query
		return query
	contestants = []
	for i in range(len(query)):
		s1 = query[:i]+query[i+1:]
		val = solve(s1, wdict, dels-1)
		if val:
			contestants.append(val)
	if contestants:
		overlap_dict[query] = max(contestants, key = lambda x: len(x))
		return overlap_dict[query]
	overlap_dict[query] = False
	return False

start = time.time()
for i in range(tn):
	overlap_dict = {}
	nw = int(input())
	wdict = input().split()
	query = input()
	ans = solve(query, wdict, nw)
	print(ans)
	print("-----------------------")

print("finished in: ", time.time()-start)
