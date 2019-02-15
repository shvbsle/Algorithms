# SHIV's code for duplicate sub tree


'''
2
(a(b(d()())(e()()))(c()(b(d()())(e()()))))
(a(b()())(c()()))
'''
import re

tn = int(input())

def next_ind(c, tree):
	if c == '-': return -1
	if c not in tree: return -1
	return tree.index(c)

def is_dup(tree):
	index_bool = [False for i in tree]
	# skip the root
	index_bool[0] = True
	index_bool[1] = True
	
	for ind, vis in enumerate(index_bool):
		if vis:continue
		index_bool[ind] = True
		if tree[ind] == '(':
			continue
		elif tree[ind] != ')':
			ind2 = next_ind(tree[ind], tree[ind+1:])
			if ind2!=-1:
				ind2 = ind2+ind
				# visit the opening paranthesis
				index_bool[ind2] = True
				ind2+=1
				index_bool[ind2] = True
			else:continue
			
			#initialize a stack
			stack=[]
			stack.append(tree[ind])
			i,j = ind, ind2
			while stack:
				i+=1
				j+=1
				try:
					if index_bool[i] or index_bool[j]:continue
				except:
					break
				index_bool[i], index_bool[j] = True, True
				if tree[i] == tree[j]:
					if tree[i] == '(':continue
					elif tree[i] == ')':
						del stack[-1]
					else:
						stack.append(tree[i])
			if not stack:return True
	return False	
			
		

for i in range(tn):
	tree = input()
	tree = re.sub('\(\)', '(-)', tree)
	ans = is_dup(tree)
	print(ans)
	print("----------------------------")
