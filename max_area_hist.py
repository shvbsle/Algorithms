# SHIV's code for max area of a histogram

'''
1
7
6 2 5 4 5 1 6
'''

tn = int(input())

def process(arr):
	arrs=[]
	for ind, e in enumerate(arr):
		c = ind-1
		cells = 1
		targ = e
		while not c<0:
			if targ > arr[c]:
				arrs.append(targ*cells)
				targ = arr[c]
			cells+=1
			c-=1
		arrs.append(cells*targ)
	return max(arrs)

for i in range(tn):
	n = int(input())
	arrs = list(map(int, input().split()))
	print("max area is:" , process(arrs))
