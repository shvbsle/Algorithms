/*
Minimum spanning tree using krusals algorithm

Spanning tree: given a graph G, spanning tree is a subgraph that connects all the edges
Min Span Tree is the one where total edge cost is minmum

Kruskals Algo: start with the shortest edge first and keep adding till all edges are covered

Before I head to this, I will first finish union-find and disjoint set algorithms

Input format:
weight src dest
---------------
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
---------------
*/
#include <bits/stdc++.h>

class disjoint_set{
public:
	std::map<int, int> set_map;
	std::vector<std::pair<std::pair<int,int>, int>> graph;

	bool detect_loop(std::vector<std::pair<std::pair<int, int>, int>> g){
		graph = g;
		int temp2, temp;

		// remember how map iteration works! It is important to use this!
		for(std::vector<std::pair<std::pair<int, int>, int>> :: iterator it = graph.begin(); it != graph.end(); ++it){
			set_map[it->first.first] = -1;
			set_map[it->first.second] = -1;
		}

		for(std::vector<std::pair<std::pair<int, int>, int>> :: iterator it = graph.begin(); it != graph.end(); ++it){
			int par_u = find_parent(it->first.first), par_v = find_parent(it->first.second);
			// std::cout << "\nworking on: " << it->first.first << "," << it->first.second << "\n";
			if( par_u == par_v){
				return true;
			}
			else if(set_map[it->first.first] == -1){
				set_map[it->first.first] = find_parent(it->first.second);
			}
			else if(set_map[it->first.second] == -1){
				set_map[it->first.second] = find_parent(it->first.first);
			}
			else{
				temp = it->first.second;
				while(set_map[temp] != -1){
					temp2 = set_map[temp];
					set_map[temp] = find_parent(it->first.first);
					temp = temp2;
				}
				set_map[temp] = find_parent(it->first.first);
			}

		}
		return false;


	}

	int find_parent(int vertex){
		int par = vertex;
		while(set_map[par] != -1){
			par = set_map[par];
		}
		return par;
	}
};

int main(){
	std::vector<std::pair<std::pair<int, int>, int>> graph, min_span_tree = {};
	std::map<int, int> vertices;
	int cost = 0, V;

	for(int i = 0; i < 14; i++){
		int w, u, v;
		std::cin >> w;
		std::cin >> u;
		std::cin >> v;
		graph.push_back(std::make_pair(std::make_pair(u, v), w)); //[std::make_pair(u , v)] = w;
		vertices[u] = 1;
		vertices[v] = 1;
	}

	// because in min spanning tree, number of edges  = no. or vertices - 1
	V = vertices.size()-1;
	disjoint_set dj;

	for(std::vector<std::pair<std::pair<int, int>, int>> :: iterator it = graph.begin(); it!= graph.end(); ++it){
		min_span_tree.push_back(*it);
		// std::cout << it->first.first << ", " << it->first.second << " |\n";
		// for(std::map<int, int> ::iterator it2 = dj.set_map.begin(); it2 !=dj.set_map.end(); ++it2){
		// 	std::cout << it2->first << ":" << it2->second << " |";
		// }
		// std::cout << "\n";std::map<int, int> ::iterator it2 = dj.set_map.begin(); it2 !=dj.set_map.end(); ++it2){
		// 	std::cout << it2->first << ":" << it2->second << " |";
		// }
		if(V == 0){
			break;
		}
		if(!dj.detect_loop(min_span_tree)){
			cost+=it->second;
			V-=1;
		}
		else{
			// std:: cout << "loop found :( ";
			// pop out the value that cause the loop :)
			min_span_tree.pop_back();
		}
	}

	std::cout << "min cost is: " << cost << "\n";

	return 0;
}
