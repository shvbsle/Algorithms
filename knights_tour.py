'''
The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once. 

Backtracking problem. These are usually trail and error problems.

Goal is to print the path matrix of the tour that coveres all the squares exaclty once

Starting is always 0,0

Don't try for 8,8.. will take too long. 
Make sure, that you pass copies to the recursive function. Python is weird this way
'''

# size the board
size_x, size_y = 5,5
total_left = size_x*size_y

import copy

#initialize the board
brd = [[0 for i in range(0, size_x)] for j in range(0, size_y)]

def render_path(path):
	rendered_path = [['x' for i in range(0, size_x)] for j in range(0, size_y)]
	begin = 1
	for [x,y] in path:
		rendered_path[x][y] = str(begin)
		begin+=1

	for row in rendered_path:
		print(row)

def possible_moves(x,y, board):
	moves = []
	# Top half moves
	if x+2 < size_x and y+1 < size_y and board[x+2][y+1] != 1:
		moves.append([x+2, y+1])
	if x-2 >= 0 and y+1 < size_y and board[x-2][y+1] != 1:
		moves.append([x-2,y+1])
	if x+2 < size_x and y-1 >= 0 and board[x+2][y-1] != 1:
		moves.append([x+2, y-1])
	if x-2 >=0 and y-1 >=0 and board[x-2][y-1] != 1:
		moves.append([x-2, y-1])
	# bottom half moves
	if y+2 < size_y and x+1 < size_x and board[x+1][y+2] != 1:
		moves.append([x+1, y+2])
	if y-2 >= 0 and x+1 < size_x and board[x+1][y-2] != 1:
		moves.append([x+1, y-2])
	if y+2 < size_y and x-1 >= 0 and board[x-1][y+2] != 1:
		moves.append([x-1,y+2])
	if y-2 >=0 and x-1 >=0 and board[x-1][y-2] != 1:
		moves.append([x-1, y-2])
	return moves

def showbrd(board):
	for row in board:
		print(row)
	print("------------------------------")

def tour(x,y, path,board, total_left):
	board[x][y] = 1
	total_left -= 1
	path.append([x,y])
	moves = possible_moves(x,y, board)
	# print(board)
	# print("---------------------------------------------------")
	if moves:
		for [tx, ty] in moves:
			# print([tx, ty])
			p = tour(tx, ty, copy.deepcopy(path), copy.deepcopy(board), total_left)
			# print(p)
			# showbrd(board)
			if len(p) == size_x*size_y:
				return p
		return []
	elif total_left == 0:
		# render_path(path)
		print("wow tour done!")
		return path
	else:
		# render_path(path)
		print(" :( no moves")
		return []


T = tour(0,0, [], copy.deepcopy(brd),  total_left)

if T:
	print("Tour found!")
	render_path(T)
else:
	print("tour not possible")





