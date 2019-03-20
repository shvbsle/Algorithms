'''
SHIV's solution for win the game

sample input
3
2 1
1 1
10 0

'''
from math import factorial
import sys
sys.setrecursionlimit(50000)
tn = int(input())

memo = {}

def solve(r, g):
	if g ==0 and r>0 or r ==0 and g>0:
		return 1.0
	if g <0 or  r<0:
		return 0.0
	n = r+g-1
	now = factorial(n)//(factorial(r-1))
	now //= factorial(g)
	return now + solve(r-1, g-2)
 
for i in range(tn):
	memo = {}
	r, g = list(map(int, input().split()))
	x = solve(r, g)
	sl_sp = factorial(r+g)//factorial(r)
	sl_sp //= factorial(g)
	#print(x, sl_sp)
	print(x/sl_sp)
	#print(round(x/sl_sp, 6))
	print("-----------------------------")	
