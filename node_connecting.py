# SHIV's

'''
2
2
3 1 L 3 2 R
4
10 20 L 10 30 R 20 40 L 20 60 R
'''

tn = int(input())

class Node:
	def __init__(self, name):
		self.name = name
		self.l = None
		self.r = None
		self.adj=None

def build_tree(query, lookup):
	node_adj_stack = {}
	adjs = []
	for i in range(0,len(query),3):
		p, c, h = query[i:i+3]
		if p not in lookup:
			p_n = Node(p)
			lookup[p] = p_n
		if c not in lookup:
			c_n = Node(c)
			lookup[c] = c_n
		if h =='L': lookup[p].l = lookup[c]
		else: lookup[p].r = lookup[c]
		if p in node_adj_stack:
			node_adj_stack[p][0].adj = lookup[c]
			lookup[c].adj = node_adj_stack[p][0]
			node_adj_stack.pop(p)
			adjs.append([lookup[c].adj, lookup[c]])
		else:node_adj_stack[p] =[lookup[c]]
	return lookup, adjs

for i in range(tn):
	qs = int(input())
	tree_query = input().split()
	lookup = {}
	tree, adjs = build_tree(tree_query, lookup)
	print("trees connected are:")
	print([(i.name, j.name) for i,j in adjs])
