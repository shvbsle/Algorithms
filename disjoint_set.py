'''
A disjoint set is a data structure for finding if elements belong to the same or different groups

Find and Union can be performed on it
'''

class disjoint_set:
	set_map = {}
	edge_list = []
	def detect_loop(self, edge_list):
		# initialize the edge list
		self.edge_list = edge_list
		for edge in edge_list:
			self.set_map[edge[0]], self.set_map[edge[1]] = -1, -1

		for edge in self.edge_list:
			par_u, par_v = self.find_parent(edge[0]), self.find_parent(edge[1])
			
			print(edge[0], edge[1])
			print("\n==\n", self.set_map, "\n==\n")
			if par_u == par_v:
				return True
			else:
				# This distiction is very important. Improper implementation of
				# this part will really cost you!

				# Added another important while loop. Now the algorithm is correct. God damn
				if self.set_map[edge[0]] == -1:
					self.set_map[edge[0]] = self.find_parent(edge[1])#edge[1]
				elif self.set_map[edge[1]] == -1:
					self.set_map[edge[1]] = self.find_parent(edge[0])#edge[1]
				else:
					temp = edge[1]
					while self.set_map[temp] != -1:
						temp2 = self.set_map[temp]
						self.set_map[temp] = self.find_parent(edge[0])
						temp = temp2
					self.set_map[temp] = self.find_parent(edge[0])

				#self.union(self.find_parent(par_u), self.find_parent(par_v))
		return False

	def union(self, u, v):
		set_map[u] = v

	def find_parent(self, vertex):
		par = vertex
		# self.set_map[par]
		while(self.set_map[par] != -1):
			par = self.set_map[par]
		return par

graph =  [(7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (2, 3), (0, 7), (1, 2)]

l = disjoint_set()
print(l.detect_loop(graph))