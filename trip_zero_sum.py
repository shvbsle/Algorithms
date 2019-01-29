# SHIV's code for triplet zero sum

'''
2
5
0 -1 2 -3 1
3
1 2 3

'''
import bisect
tn = int(input())

def process(arr):
	arr.sort()
	count = 1
	m = arr[-1]
	tot = m
	while count < 3:
		arr.pop(-1)
		if -m in arr:
			next_rem = m
			arr[arr.index(-m)]+=m
		else:
			next_rem = arr[bisect.bisect(arr, -m)-1]
			arr[bisect.bisect(arr, -m)-1]+=m
		tot+=next_rem
		count+=1
		m = max(arr)
	if tot == 0: return 1
	else: return 0

for i in range(tn):
	n = int(input())
	arr = list(map(int, input().split()))
	print(process(arr))
