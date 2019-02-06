#SHIV's code for longest valid parenthesis

'''
2
((()
)()())
'''

tn = int(input())

def process(exp):
	stack = []
	pop = 0
	for p in exp:
		if p == ')':
			if stack and stack[-1] == '(':
				stack.pop(-1)
				pop+=1
			else: stack.append(p)
		else:stack.append(p)
	print(pop*2)

for i in range(tn):
	exp = input()
	process(exp)
