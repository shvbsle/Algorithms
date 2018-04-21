'''
SHIV's
Game of Nim using MinMax
'''
# this is the pile of stones
pile = [1, 2, 2]

Computer = "max"
Player = "min"

def next_states(pile):
	state_list = []
	for i in range(len(pile)):
		state = list(pile)
		element = state[i]
		while(element > 0):
			element -= 1
			state[i] = element
			state_list.append(list(state))
	return state_list

# define the state of the score
def state_score(player_type, state):
	opposition = "min"
	if player_type == "min":
		opposition = "max"
	# returns true if
	if all(x == 0 for x in state):
		# empty pile i.e invalid state
		return -2
	if state.count(1) == 1 and 2 not in state:
		# print("heh", state, player_type)
		if player_type == "min":
			return 1
		else:
			return 0
	else:
		# Indicate that the state is not leaf
		stl = next_states(list(state))
		scores = []
		for st in stl:
			sc = state_score(opposition, list(st))
			scores.append(sc)
			# print(player_type, st, sc)
		scores = list(filter((-2).__ne__, scores))
		if player_type == "min":
			return(min(scores))
		else:
			return(max(scores))
		return -1


while(1):
	stl = next_states(pile)
	print(stl)
	best_score = []
	for state in stl:
		score = state_score(Player, state)
		print(state, "score of state:" , score)
		best_score.append([score, state])
		print("----")
	best_move = max(best_score)
	print("Best move by the computer is: ", best_move)
	
	pile = list(best_move[1])
	print("Pile is now: ", pile, "\n Player plays now:")

	p = int(input("Enter Pile no. (0, 1, 2): "))
	while(p > len(pile)):
		p = int(input("Enter Valid Pile no. (0, 1, 2): "))
	r = int(input("enter number of stones to be removed: "))
	while(pile[p] - r < 0):
		r = int(input("You cant pick that many! pick again: "))
	pile[p] = pile[p]-r
	if all(x == 0 for x in pile):
		print("You loose puny human!!!! Hahaha!")
		exit(1)
	print("Pile is now: ", pile, "\n Computer plays now:")



