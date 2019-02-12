# SHIV's code for string interleaving

'''
2
YX  X  XXY
XY X XXY
'''

tn = int(input())

def process(a, b, c):
	left = []
	if len(a) > len(b):
		left = a[len(b):]
		C = [x+y for x,y in zip(a[:len(b)], b)]
	elif len(b) > len(a):
		left = b[len(a):]
		C = [x+y for x,y in zip(a, b[:len(a)])]
	if ''.join(C)+left == c: return True
	return False

for i in range(tn):
	a, b, c = input().split()
	print(process(a, b, c))
