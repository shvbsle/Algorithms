# SHIV's code for largest fibbo sequence

'''
2
7
1 4 3 9 10 13 7
9
0 2 8 5 2 1 4 13 23


'''

tn = int(input())

fiber = {}

def fib(n):
	if n in fiber: return fiber[n]
	if n <=0:
		fiber[0] = 0
		return fiber[0]
	if n == 1:
		fiber[1] = 1 
		return fiber[1]
	fiber[n] = fib(n-1)+fib(n-2)
	return fiber[n]

def process(seq):
	c = 0
	fibs = []	
	while fib(c) <= max(seq):
		fibs.append(fib(c))
		c+=1
	infibs = []
	for i in seq:
		if i in fibs: infibs.append(i)
	print(infibs)

for i in range(tn):
	nos = int(input())
	seq = list(map(int, input().split()))
	process(seq)
