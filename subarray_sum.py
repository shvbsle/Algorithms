# SHIV's
# Subarray with given sum
'''
testing cases:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10

'''
tn = int(input())

def process(arr, s):
	sum_arr = []
	for ind, e in enumerate(arr):
		sum_arr.append(e)
		if sum(sum_arr) == s:
			break
		if sum(sum_arr) > s:
			sum_arr.pop(0)
			if sum(sum_arr) == s:
				break
	inds, inde = arr.index(sum_arr[0]), arr.index(sum_arr[-1])
	if sum(arr[inds:inde+1]) == s: 
		print(inds+1, inde+1)
	else: print(-1)

for i in range(tn):
	n_s = input().split(' ')
	n, s = int(n_s[0]), int(n_s[1])
	arr = list(map(int, input().split(' ')))
	process(arr, s)
