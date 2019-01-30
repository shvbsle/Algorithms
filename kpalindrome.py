# shiv's code for k-palindrome

'''
3
abcdecba 1
acdcb  1
abcdeca 2
'''

tn = int(input())

def process(s, k):
	#print(s,s[0], s[-k:])
	if s == '': return 1
	if len(s) == 2 and k >=1: return 1
	if s[0] == s[-1]:
		return process(s[1:-1], k)
	elif s[0] in s[-k:]:
		ind_from_end = s[-k:].index(s[0])
		return process(s[:ind_from_end], k-len(s[ind_from_start:]))
	elif s[-1] in s[:k]:
		ind_from_start = s[:k].index(s[-1])
		return process(s[ind_from_start:], k-len(s[:ind_from_start]))
	else:
		return 0
		
for i in range(tn):
	ip = input().split(' ')
	print(process(ip[0], int(ip[1])))
