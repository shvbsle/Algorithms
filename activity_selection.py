# SHIV's code for activity selection
'''
# sample test case

2
6
1 3 2 5 8 5
2 4 6 7 9 9
10
41 13 4 70 10 58 61 34 100 79
68 39 12 97 13 66 82 38 120 99
'''

tn = int(input())

# sort by end times and then pick out those whose start times were greater
# than prev ends
def process(club):
	club.sort(key = lambda x: x[1])
	prev, tasks = 0, 0
	for s, e in club:
		if s >= prev:
			tasks+=1
			prev=e
	return tasks
		
for i in range(tn):
	tasks = int(input())
	starts = list(map(int, input().split(' ')))
	ends = list(map(int, input().split(' ')))
	club = list(map(list, zip(starts, ends)))
	print(process(club))
