'''
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
'''

# start and finish time tuples
start_finish = [[1,2],[0,6],[3,4],[5,7],[8,9],[5,9]]

#lambda sorting by the second element, index 1
start_finish.sort(key = lambda x : x[1])
print(start_finish)
count = 1
st = start_finish[0][1]
for en in range(0, len(start_finish)-1):
	diff = start_finish[en+1][0] - st
	print(diff)
	if  diff >=0 :
		st = start_finish[en+1][1]
		count +=1
	else:
		while not start_finish[en+1][0] - st >= 0 and en < len(start_finish)-2:
			en+=1
print(count)

'''
Tricky corner cases!

The greedy algorithm is good but the thing to remember here is the we have to eliminate overlapping work schedules. Consecutive difference calculation doesn't work!

'''