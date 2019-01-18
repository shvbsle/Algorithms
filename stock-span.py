# SHIV's solution for stock span
'''
# sample test cases

2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80
'''


tn = int(input())

def get_span(arr):
	for_check = arr[-1]
	count = 0
	for i, e in enumerate(reversed(arr)):
		if for_check-e >=0:
			count+=1
		else: break
	return count 

def span(stocks, cases):
	spans = []
	for s in range(1,cases+1):
		spans.append(get_span(stocks[:s]))
	return list(map(str, spans))
		
for i in range(tn):
	cases = int(input())
	stocks = list(map(int, input().split(' ')))
	print(' '.join(span(stocks, cases)))
