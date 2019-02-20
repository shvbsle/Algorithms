# SHIV's code to reverse the words in a string in O(n) time

query = "the quick brown fox jumped over the lazy fox"

def solve(query):
	stack_sent = []
	token=""
	for i in range(len(query)-1, -1, -1):
		if query[i] == " ":
			stack_sent.append(token)
			token = ""
			continue
		token+=query[i]
	while stack_sent:
		print(stack_sent[-1], end=' ')
		del stack_sent[-1]

solve(query)
