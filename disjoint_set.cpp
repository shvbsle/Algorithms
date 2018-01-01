/*
A disjoint set is a data structure for finding if elements belong to the same or different groups

Find and Union can be performed on it
*/
#include <bits/stdc++.h>

class disjoint_set{
public:
	std::map<int, int> set_map;
	std::vector<std::pair<int, int>> elist;

	// default constructor
	disjoint_set(std::vector<std::pair<int,int>> edge_list){
		for(int i = 0; i < edge_list.end()-edge_list.begin(); i++){
			set_map[edge_list[i].first] = -1;
			set_map[edge_list[i].second] = -1;
		}

		elist = edge_list;
	}
public:
	bool detect_loop(){
		int temp,temp2;
		for(int i = 0; i < elist.end()-elist.begin(); i++){
			int par_u = find_parent(elist[i].first), par_v = find_parent(elist[i].second);
			if (par_u == par_v){
				return true;
			}
			else{
				// Make sure that the following three condidtions are taken care of
				if(set_map[elist[i].first] != -1)
					set_map[elist[i].first] = find_parent(elist[i].second);
				else if(set_map[elist[i].second] != -1)
					set_map[elist[i].second] = find_parent(elist[i].first);
				else
					temp = elist[i].second;
					while(set_map[temp]!= -1){
						temp2 = set_map[temp];
						set_map[temp] = find_parent(elist[i].first);
						temp = temp2;
					}
					set_map[temp] = find_parent(elist[i].first);
			}
		}

		return false;
	}

	int find_parent(int vertex){
		int par = vertex;
		while(set_map[par] != -1){
			par = set_map[par] ;
		}
		return par;
	}
};

int main(){

	std::vector<std::pair<int,int>> graph = {{7, 6}, {8, 2}, {6, 5}, {0, 1}, {2, 5}, {2, 3}, {0, 7}, {1, 2}};
	// std:: cout << "compiles";
	disjoint_set l(graph);

	if (l.detect_loop()){
		std::cout << "loop detected\n";
	}
	else{
		std::cout << "no loop\n";
	}
	return 0;
}