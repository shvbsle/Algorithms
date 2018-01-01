'''
Minimum spanning tree using krusals algorithm

Spanning tree: given a graph G, spanning tree is a subgraph that connects all the edges
Min Span Tree is the one where total edge cost is minmum

Kruskals Algo: start with the shortest edge first and keep adding till all edges are covered

Before I head to this, I will first finish union-find and disjoint set algorithms

Input format:
weight src dest
--------------------------------
1 7 6
2 8 2
2 6 5
4 0 1
4 2 5
6 8 6
7 2 3
7 7 8
8 0 7
8 1 2
9 3 4
10 5 4
11 1 7
14 3 5
---------------------------------

Other points to look out for in the disjoint set algorithm:
- Set the parent of vertex u as parent of vertex v iff parent of u is -1
- same follows for v
- iff both edges are not -1, then traverse depth first in the distionary till -1 is reached and make everyone have a common paret

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


edge_map = {}
edge_list = []
min_span_list = []

for i in range(0, 14):
	w , src, dest = list(map(int, input().split(" ")))
	edge_map[(src,dest)] = w
	edge_list.append([src,dest])

cost = 0

dj= disjoint_set()
# min_span_list.append(edge_list[0])
visited = {e:False for e in edge_map}
for edge in edge_map:
	# print(edge, "| ", edge_map[edge], "| ", min_span_list, "\n-------\n", dj.set_map, "\n--------\n")
	if not visited:
		break	
	if not dj.detect_loop(min_span_list + [edge]):
		cost += edge_map[edge]
		min_span_list.append(edge)
		try:
			visited.pop(edge[0], None)
			visited.pop(edge[1], None)
		except:
			continue

print("cost is: ", cost, "\n", min_span_list)




