#SHIV's code for maximum index

'''
1
9
34 8 10 3 2 80 30 33 1
'''

tn = int(input())

def process(arr):
	max_arr = []
	for ind, i in enumerate(arr):
		interm = []
		for ind2, j in enumerate(arr):
			if ind2 < ind: continue
			if i<=j:
				interm.append(((ind, ind2),ind2-ind))
		if interm:
			max_dist = max(interm, key=lambda x: x[1])
			max_arr.append(max_dist)
		else: max_arr.append(((i, i), 0))
	print(max(max_arr, key=lambda x:x[1]))

for i in range(tn):
	ns = int(input())
	arr = list(map(int, input().split()))
	process(arr)
