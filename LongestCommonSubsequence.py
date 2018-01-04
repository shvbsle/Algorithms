'''
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
So a string of length n has 2^n different possible subsequences.

A Dynamic Programming Problem

Input Format
-------------
ABCDGH
AEDFHR
-------------

LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

another:
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Algorithm Description:
Start from the end for these sequence preservation
Haha easy pesy.I just need to think more properly

'''
s1 = input()
s2 = input()

# This approach is good but non memoized method
def solve(s1, s2):
	if len(s1) <1 or len(s2) <1:
		return 0
	if len(s1) == 1 and s2[-1] == s1[-1]:
		return 1
	if len(s2) == 1 and s1[-1] == s2[-1]:
		return 1
	if s1[-1] == s2[-1]:
		return 1 + solve(s1[:len(s1)-1], s2[:len(s2)-1])
	else:
		return max(solve(s1[:len(s1)-1], s2), solve(s1, s2[:len(s2)-1]))

# print(solve(s1,s2))

# My favourite method if memoization is to directly record the function parameters
# in a map. Watch and learn
memory = {}
def Dynamic_solve(s1,s2):
	if len(s1) <1 or len(s2) <1:
		memory[(s1,s2)] = 0
		return 0
	if len(s1) == 1 and s2[-1] == s1[-1]:
		memory[(s1,s2)] = 1
		return memory[(s1,s2)]
	if len(s2) == 1 and s1[-1] == s2[-1]:
		memory[(s1,s2)] = 1
		return memory[(s1,s2)]
	if s1[-1] == s2[-1]:
		try:
			return 1+ memory[(s1[:len(s1)-1], s2[:len(s2)-1])] 
		except:
			memory[(s1,s2)] = 1 + solve(s1[:len(s1)-1], s2[:len(s2)-1])
			return memory[(s1,s2)]
	else:
		try:
			return max(memory[(s1[:len(s1)-1],s2)] , memory[(s1, s2[:len(s2)-1])])
		except:
			memory[(s1,s2)] = max(solve(s1[:len(s1)-1], s2), solve(s1, s2[:len(s2)-1]))
			return memory[(s1,s2)]

print(Dynamic_solve(s1,s2))

