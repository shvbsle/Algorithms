# Shiv's code for counting BST nodes

'''
1
6
10 5 50 1 40 100
5 45
'''

tn = int(input())

class Node:
	def __init__(self, name):
		self.name=name
		self.l=None
		self.r=None

def build_tree(root, node):
	if node>=root.name:
		if root.r == None:
			root.r = Node(node)
		else:
			build_tree(root.r, node)
	elif node < root.name:
		if root.l == None:
			root.l = Node(node)
		else:
			build_tree(root.l, node)

node_count = 0

def getCountOfNode(root, l, h):
	global node_count
	if l <= root.name <= h:
		node_count+=1
	if root.l != None:
		getCountOfNode(root.l, l, h)
	if root.r !=None:
		getCountOfNode(root.r, l, h)
	

for i in range(tn):
	node_count = 0
	n = int(input())
	nodes = list(map(int, input().split()))
	l, h = list(map(int, input().split()))
	root = Node(nodes[0])
	for node in nodes[1:]:
		build_tree(root, node)
	getCountOfNode(root,l,h)
	print(node_count)

