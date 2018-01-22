'''
SHIV's
Tic Tac Toe game using a non AI method
'''

# this will be my board
board = ['_' for i in range(9)]

# show the board
def show_board():
	for r in range(0, 9, 3):
		print(board[r], board[r+1], board[r+2])
	print("\n---------------\n")

# go will return true if move possible else false
def go(symbol, pos):
	if(board[pos] == '_'):
		board[pos] = symbol
		return True
	else:
		return False

# a generator that returns the corner that is not taken
def corner(symbol):
	cc = [0,2,6,8]
	for c in cc:
		if board[c] == '_':
			yield c
	yield -1

# a generator that returns the edge that is not taken
def edge(symbol):
	cc = [1,3,5,7]
	for c in cc:
		if board[c] == '_':
			yield c
	yield -1

# returns the winning position
def poswin(symbol):
	opp = 'X'
	if symbol ==  'X':
		opp = 'O'
	# eight winning lines
	# 3 horizontal, 3 vertical and 2 diagonal
	win_pos_matrix = [[0,1,2], [3,4,5], [6,7,8],[0,3,6], [1,4,7], [2,5,8],[0,4,8], [2,4,6]]
	for (p,q,r) in win_pos_matrix:
		mov_lis = [p,q,r]
		if [board[p], board[q], board[r]].count(symbol) == 2 and opp not in [board[p], board[q], board[r]]:
			ind = [board[p], board[q], board[r]].index('_')
			# print([board[p], board[q], board[r]], p,q,r, symbol, mov_lis[ind])
			# return index of the blank space
			return mov_lis[ind]

	# no winning move possible :( return 0
	return 0

toggle = True
# main game loop
to, tx = 0, 0
for i in range(9):
	if toggle:
		print("player makes move")
		toggle = False
		while not go('X', int(input("make a move [0-8]:"))):
			print("invalid move. Try again!")
		show_board()
		tx+=1
	else:
		print("computer moves")
		toggle = True
		if board[4] == '_' and tx < 2:
			go('O', 4)
		elif tx < 2:
			go('O', next(corner('O')))

		# don't let opponent win
		if tx == 2:
			if poswin('X') != 0:
				go('O', poswin('X'))
			else:
				go('O', next(corner('O')))

		# now win for yourself
		if to >= 2:
			if poswin('O') != 0:
				go('O', poswin('O'))
				show_board()
				print("hahah Computer wins!")
				break
			elif poswin('X') != 0:
				go('O', poswin('X'))
			else:
				val = go('X', next(corner('X')))
				if val == -1:
					go('X', next(edge('X')))
		to+=1
		show_board()
	print(to, ":to ",tx, ":tx")




