'''
Dynamic Programming:

not adding c++ files for now. Will add soon

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. 

Input Format:
---------------
1 5 8 9 10 17 17 20


1 2 3 4  5  6  7  8 

total no of enteries are the length of the rod

Algo strategy:
-Create the possible permutations in which the rod can be cut up and add up the max vals

How:
val(l) = max{{ val(l-r)+val(r) } for r in range(0, l)}

# output:

non memoized:
1   1
1   5
1   8
1   1
1   1
5   5
1   10
1   1
1   1
1   5
5   8
1   13
1   1
1   1
1   5
1   8
1   1
1   1
5   5
5   10
1   1
1   5
1   1
1   5
8   8
1   17
1   1
1   1
1   5
1   8
1   1
1   1
5   5
1   10
1   1
1   1
1   5
5   8
5   13
1   1
1   5
1   1
1   5
1   8
1   1
1   1
5   5
8   10
1   18
1   1
1   1
1   5
1   8
1   1
1   1
5   5
1   10
1   1
1   1
1   5
5   8
1   13
1   1
1   1
1   5
1   8
1   1
1   1
5   5
5   10
1   1
1   5
1   1
1   5
8   8
5   17
1   1
1   5
1   1
1   5
1   8
1   1
1   1
5   5
1   10
1   1
1   1
1   5
5   8
8   13
1   1
1   5
1   8
1   1
1   1
5   5
1   1
1   5
1   8
1   1
1   1
5   5
10   10
22


memoized:
lesser no of calls

1   1
1   5
1   8
5   5
1   10
5   8
1   13
5   10
8   8
1   17
5   13
8   10
1   18
5   17
8   13
10   10
22

'''

# haha memoized code for rod cutting

s = list(map(int, input().split(" ")))
m = {}
def solve(l):
	if l in m:
		return m[l]
	val = []
	val.append(s[l-1])
	if(l == 1):
		m[1] = s[0] 
		return m[1]
	for i in range(1, int(l/2)+1):
		a, b = solve(i), solve(l-i)
		print(a," ", b)
		val.append(( a+b ))
	m[l] = max(val)
	return m[l]

print(solve(8))

