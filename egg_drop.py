# SHIV's code for egg dropping

'''
1
2 10
'''

tn = int(input())

egg_dict = {}
def egger(floor, egg):
	if floor == 0 or floor == 1:
		return floor
	if egg == 1:
		return floor
	eggdr = []
	for i in range(1, floor+1):
		if (i-1, egg-1) in egg_dict:
			a = egg_dict[i-1, egg-1]
		else:
			a = egger(i-1, egg-1)
			egg_dict[i-1, egg-1] = a
		if (floor-i, egg) in egg_dict:
			b = egg_dict[floor-i, egg]
		else:
			b = egger(floor-i, egg)
			egg_dict[floor-i, egg] = b
		eggdr.append(max(a, b))
	return min(eggdr)+1

for i in  range(tn):
	egg_dict = {}
	egg, floor = list(map(int, input().split()))
	print(egger(floor, egg))
