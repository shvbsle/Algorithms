#SHIV's code for look and say

'''
2
2
3

'''

tn = int(input())

pattern = {1:"1"}

def get_next(s):
	prev = s[0]
	t = 0
	L=[]
	for c in s:
		if c == prev:
			t+=1
		else:
			L.append(str(t))
			L.append(str(prev))
			t=1
		prev=c
	L.append(str(t))
	L.append(str(prev))
	return ''.join(L)
 
def lookup(n):
	if n in pattern:return pattern[n]
	else:
		max_n = max(pattern.keys())
		max_pat = pattern[max_n]
		while max_n != n:
			pattern[max_n+1] = get_next(max_pat)
			max_pat = pattern[max_n+1]
			max_n+=1
		print(pattern[max_n])

for i in range(tn):
	n = int(input())
	lookup(n)
