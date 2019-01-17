# SHIV's implementation of an LRU cache

no_test_case = int(input())

def _parse_q_string(s):
	q_list = s.split()
	parsed_q_list = []
	for ind, q in enumerate(q_list):
		if q == 'SET':
			parsed_q_list.append(('SET', q_list[ind+1], q_list[ind+2]))
			ind+=2
		if q == 'GET':
			parsed_q_list.append(('GET', q_list[ind+1]))
			ind+=1
	return parsed_q_list
			
def process(q_inst, capacity):
	inst_q = []
	inst_dict = {}
	for q in q_inst:
		if q[0] == 'SET':
			if len(inst_dict) <2:
				inst_dict[q[1]] = q[2]
				inst_q.append(q[1])
			elif len(inst_dict) == 2 and q[1] in inst_dict:
				inst_dict[q[1]] = q[2]
				inst_q.pop(inst_q.index(q[1]))
				inst_q.append(q[1])
			else:
				inst_dict.pop(inst_q[0])
				inst_q.pop(0)
				inst_dict[q[1]]= q[2]
				inst_q.append(q[1])
		elif q[0] == 'GET':
			if q[1] in inst_dict: print(inst_dict[q[1]])
			else: print(-1)
		
for i in range(no_test_case):
	capacity = input()
	queries = input()
	q_instructions= _parse_q_string(input())
	print(q_instructions)
	process(q_instructions, capacity)
