# SHIV's code for strstr

'''
sample input:

2
GeeksForGeeks Fr
GeeksForGeeks For
'''

tn = int(input())

def strstr(s, x):
	start, end, enumx = -1, -1, 0
	for ind, c in enumerate(s):
		#print(c, x[enumx], start)
		if c == x[0]: 
			start = ind
			enumx+=1
			continue
		if start != -1:
			if enumx >= len(x):
				break
			if x[enumx] == c:
				enumx +=1
			else: enumx, start= 0,-1 
	return start

for i in range(tn):
	x = input().split(' ')
	print(strstr(x[0], x[1]))

