# SHIV's algo for word boggle

'''
sample input:

1
4
GEEKS FOR QUIZ GO
3 3
G I Z U E K Q S E



Algo:
for a word W, get the starting positions for the first letter
pass the string excluding the first letter and search in only adj cells from the first.
Do this recursively.

EX:
GEEKS:
call 1:
word = 'GEEKS'; next_char = 'E'; next_pos_adj = [1,1]

call 2:
word = 'EEKS'; next_char = 'E'; next_pos_adj = [2,2]

call 3:
word = 'EKS'; next_char = 'K'; next_pos_adj = [1, 2]
... and so on

if next char pos not found return -1 and exit recursion

Output:
['GEEKS', 'QUIZ']

'''
import math
tn = int(input())

# extract grid from the input structure
def get_grid(letters, size):
	grid = []
	offset = 0
	for i in range(size[1]):
		grid.append(letters[offset:offset+size[0]])
		offset+=size[0]
	return grid

# get the position of the ele from the grid
def get_pos(c, grid):
	pos = []
	for x_pos, x in enumerate(grid):
		for y_pos, y in enumerate(x):
			if y == c:
 				pos.append((x_pos, y_pos))
	
	if not pos: return -1
	return pos

# method to get the adjacent elements out of the list
def get_adj(pos, pos_list):
	adj = []
	for p in pos_list:
		dist = int(math.sqrt((p[0]-pos[0])**2 + (p[1]-pos[1])**2))
		if dist == 1: adj.append(p)
	if not adj: return -1
	else: return adj

# recursive method to trace the grid
def trace(w, pos, grid):
	if len(w) == 1: return 1
	next_char_pos = get_pos(w[1], grid)
	if next_char_pos == -1: return -1
	next_char_pos_adj = get_adj(pos, next_char_pos)
	for p in next_char_pos_adj:
		val = trace(w[1:], p, grid)
		return 1
	
# start tracing for each word
def solve_grid(grid, words):
	in_grid = []
	for w in words:
		w0_pos = get_pos(w[0], grid)
		if w0_pos == -1: continue
		for pos in w0_pos:
			val = trace(w, pos, grid)
			if val == 1: 
				in_grid.append(w)
				break	
	print(in_grid)
	
# driver
for i in range(tn):
	n_words = int(input())
	words = input().split(' ')
	grid_size = list(map(int, input().split(' ')))
	grid = get_grid(input().split(' '), grid_size)
	solve_grid(grid, words)
