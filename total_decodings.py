#SHIV's code for total decodings

'''
sample input:

2
3
123
4
2563
'''

tn = int(input())

def process(num):
	count = 1
	for ind, c in enumerate(num[:-1]):
		if int(c+num[i+1]) <= 26:
			count+=1
	print(count)	

for i in range(tn):
	ndig = int(input())
	num = input()
	process(num)
