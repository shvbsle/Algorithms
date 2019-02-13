// SHIV's code for matrix transpose
#include<bits/stdc++.h>

void arr_trans(std::vector<std::vector<int>> vec, int n, int m){
	std::vector<std::vector<int>> trans;
	std::map<int, std::vector<int>> col_map;
	for(int i = 0; i <n; i++){
		col_map.insert(std::pair<int, std::vector<int>>(i, std::vector<int>()));
	}

	std::cout << "Original:\n";
	for(std::vector<std::vector<int> >::iterator t = vec.begin(); t!=vec.end(); t++){
		for(std::vector<int>::iterator t2 = t->begin(); t2!=t->end(); t2++){
			int index = std::distance(t->begin(), t2);
			std::cout << "("<<*t2 <<")";
			col_map[index].push_back(*t2);
		}
		std::cout << "\n";
	}

	std::cout << "Transpose:\n";
	for(std::map<int, std::vector<int>>::iterator itr= col_map.begin(); itr != col_map.end(); ++itr) {
		std::vector<int> temp = itr->second;
		trans.push_back(temp);
		for(std::vector<int>::iterator t2 = temp.begin(); t2!=temp.end(); t2++){
			std::cout << "("<<*t2<<")";
			col_map[itr->first].push_back(*t2);
		}
		std::cout << "\n";
    } 

}

int main(){
	std::vector<std::vector<int> > arr = {{1,2,3,4},{0,2,7,9}, {4,5,1,5}};
	arr_trans(arr, 2, 3);
	return 0;
}


