'''
tic tac toe game using AI (min max)
'''
import copy

#initialize board
board = ['_' for i in range(9)]

# show the board
def show_board(board):
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

def heur(brd, symbol):
	player = poswin('X', brd)
	opo = poswin('O' ,brd)
	# print(player, opo, "\nscore: ", player-opo)
	# show_board(brd)
	return player - opo

def get_score(symbol, board, depth):
	opp = 'O'
	if symbol == 'O':
		opp = 'X'
	poss_moves = []
	back_prop = 0
	for i in range(9):
		if board[i] == '_':
			dup = copy.copy(board)
			dup[i] = symbol
			h_score = heur(dup, symbol)
			# here is ply 2 :)
			if depth > 1:
				# print("Ply 2---------------")
				val_array = []
				for j in range(9):
					if dup[j] == '_':
						b2 = copy.copy(dup)
						b2[j] = opp
						p2_score = heur(b2, symbol)
						# here is ply 3
						if depth >2:
							# print("Ply 3 O_O ---------------")
							val_array_last = []
							for m in range(9):
								if b2[m] == '_':
									b3 = copy.copy(b2)
									b3[m] = symbol
									val_array_last.append(heur(b3, symbol))
							p2_score+= min(val_array_last)
						val_array.append(p2_score)
				back_prop = max(val_array)

			h_score+= back_prop
			# print("selected score is: ",h_score)
			poss_moves.append([h_score, i, dup])
	
	
	'''
	d2 = []
	if depth == 1:
		for (score, pos, b) in poss_moves:
			V = get_score(symbol, b, depth)
			d2.append(( score +V[0] ,i,b))
		if symbol == 'X':
			return max(d2)
		else:
			return min(d2)	
	'''
	if symbol == 'X':
		return max(poss_moves)
	else:
		return min(poss_moves)	

# returns the winning position
def poswin(symbol, board):
	score = 0
	opp = 'X'
	if symbol ==  'X':
		opp = 'O'
	# eight winning lines
	# 3 horizontal, 3 vertical and 2 diagonal
	win_pos_matrix = [[0,1,2], [3,4,5], [6,7,8],[0,3,6], [1,4,7], [2,5,8],[0,4,8], [2,4,6]]
	for (p,q,r) in win_pos_matrix:
		mov_lis = [p,q,r]
		if opp not in [board[p], board[q], board[r]] and '_' in [board[p], board[q], board[r]] :
			# try:
			# 	ind = [board[p], board[q], board[r]].index('_')
			# except:
			# 	score+=1
			score+=1
		elif opp not in [board[p], board[q], board[r]] and '_' not in [board[p], board[q], board[r]]:
			return 999
		
	# no winning move possible :( return 0
	return score


# returns the winning position
def poswin_old(symbol):
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

# game starts here
# this is the pky depth
depth = int(input("select difficulty: Easy - 1; Medium - 2; Hard - 3: "))
player = input("select symbol (X or O) (X plays first): ")
opp = 'X'
toggle = False
if player == 'X':
	opp = 'O'
	toggle = True

# main game loop
to, tx = 0, 0
for i in range(9):
	if toggle:
		print("player makes move")
		toggle = False
		while not go(player, int(input("make a move [0-8]:"))):
			print("invalid move. Try again!")
		show_board(board)
		tx+=1
	else:
		print("computer moves")
		toggle = True
		if poswin_old(opp) != 0:
				print("heheiehi")
				go(opp, poswin_old(opp))
				show_board(board)
				print("hahah Computer wins!")
				break
		move = get_score(opp, board, depth)
		print(move)
		go(opp, move[1])
		to+=1
		show_board(board)
	print(to, ":comp ",tx, ":player")
