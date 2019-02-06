# shivs code for finding the numbers

'''
2
2
1 2 3 2 1 4
1
2 1 3 2
'''

tn = int(input())

def process(nums, n):
	d = {}
	for n in nums:
		if n in d: d.pop(n)
		else:d[n] = 0
	print(d.keys())

for i in range(tn):
	n = int(input())
	nums = list(map(int, input().split()))
	process(nums, n)
