# SHIV's code for converting ternary exp to binary tree

'''
3
a?b:c
a?b?c:d:e
a?b?c:d?e:f:g?h:i

'''

tn = int(input())

class node:
	def __init__(self, name):
		self.name = name
		self.L= None
		self.R = None
		self.count = 0

def build_tree(tree):
	stack = []
	for c in tree:
		if c == '?': continue
		if c == ':':
			old_head = stack[-1]
			del stack[-1]
			stack[-1].count+=1
			if stack[-1].count == 1:
				stack[-1].L = old_head
			elif stack[-1].count == 2:
				stack[-1].R = old_head
				del stack[-1]
				stack[-1].count+=1
				while stack[-1].count == 2:
					del stack[-1]
					stack[-1].count+=1
		else:
			curr_node = node(c)
			stack.append(curr_node)
	while stack[-1].count == 2 or stack[-1].count == 0:
		del stack[-1]
		if not stack: break
		stack[-1].count+=1
		print([(x.name, x.count) for x in stack])

for i in range(tn):
	tree = input()
	root = build_tree(tree)
	print('----------------')
