# SHIV's code
# Longest Common Increasing Subsequence

# Testing arrays
a1 = [3,4,9,1]
a2 = [5,3,8,9,10,2,1]
a3 = [50, 3, 10, 7, 40, 80]
a4 = [3, 10, 2, 1, 20]
a5 = "AGGTAB"
a6 = "GXTXAYB"

# find the LIS for any list
def LIS(a):
	if len(a) < 1: return 1
	least_index = 0
	for ind, i in reversed(list(enumerate(a))):
		#print(i, a[-1])
		if i < a[-1]:
			least_index=ind
			break
	return max(LIS(a[:-1]),1+LIS(a[:least_index]))

# This func will now find LCS
# Also a very nice way to see how to retrieve the elements of the efficient elements
def LCS(a, b):
	try:
		if len(a) <1: return 0, []
		if a[-1] == b[-1]: 
			#cost, arr = LCS(a[:-1], b[:-1])
			#print(arr, a[-1], cost)
			cost, arr = LCS(a[:-1], b[:-1])
			arr.append(a[-1])
			return 1+cost, arr
		else:
			cost1, arr1 = LCS(a[:-1], b)
			cost2, arr2 = LCS(a, b[:-1])
			costs = [cost1, cost2]
			arrs = [arr1, arr2]
			ind = costs.index(max(costs))
			return costs[ind], arrs[ind]
	except:
		return 0, []

# This bro finally finds the LCIS
def LCIS(a, b):
	l, x = LCS(a, b)
	cost = LIS(x)
	return cost
 
# Yayyyy!
print(LCIS(a1, a2))
