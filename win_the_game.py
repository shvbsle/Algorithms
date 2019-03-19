'''
SHIV's solution for win the game

sample input
3
2 1
1 1
10 0

'''
import math

tn = int(input())

memo = {}
def solve(player, rn, gn):
	n = rn+gn
	if (player, rn, gn) in memo:
		return memo[player, rn, gn]
	if n <= 1:
		return 0
	c1, c2 = 0, 0
	if player == 1:
		c1 = rn*(n-1)
		c2 = solve(2, rn, gn-1)
	elif player == 2:
		c1 = gn*(n-1)
		c2 = solve(1, rn-1, gn)
	memo[player, rn,gn] = c1+c2
	return c1+c2

for i in range(tn):
	r, g = list(map(int, input().split()))
	if r == 0 or g == 0:
		print(1.0)
		continue
	x = solve(1, r, g)
	print(round(x/math.factorial(r+g), 6))
	
