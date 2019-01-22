# SHIV's algo for finding sum or pairs

'''
Test input

2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
'''

tn = int(input())

def process(A, B, s):
	arr = []
	for a in A:
		for b in B:
			if a+b == s: arr.append((a, b))
	print(arr)

for i in range(tn):
	cases = list(map(int, input().split()))
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	process(A, B, cases[2])
