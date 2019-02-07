# SHIV's code for jumping numbers

'''
2
10
50
'''

tn = int(input())

def process(n):
	arr = [str(i) for i in range(n+1)]
	jumping = []
	for a in arr:
		f = list(map(int, list(a)))
		nos = [i-j for i,j in zip(f, f[1:])]
		if nos.count(-1)+nos.count(1) == len(nos):
			jumping.append(a)
	print(jumping)

for i in range(tn):
	n = int(input())
	process(n)
