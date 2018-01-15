'''
DYnamic Programming: Coing Change problem

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.


Input Format:
4
1 2 3

the first line is the change
and second lines contain denominations (D)

Algorithm Strategy:

N(val) = sum{ N(r) + N(val - r) for r in D }

'''

N = int(input())
D = list(map(int, input().split(" ")))
m = {}

def solve(d, Dd):
	if (d, len(Dd)) in m:
		return m[(d, len(Dd))]
	ans = 0
	if d == 0:
		return 1
	if d < 0:
		return 0
	if len(Dd) <= 0 and d >=1:
		return 0
	#----no .of ways to get to d using sub arrays + number of ways to get to d-r uring D
	ans = solve(d, Dd[:len(Dd)-1])            +       solve(d - Dd[len(Dd)-1], Dd)
	m[(d, len(Dd))] = ans
	return ans

print(solve(4, D))

