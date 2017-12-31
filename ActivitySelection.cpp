/*
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
*/
#include <bits/stdc++.h>

// driver fucntion to sort a vector by it's secont element
bool sort_by_sec(const std::pair<int, int> &a, const std::pair<int,int> &b){
	return a.second < b.second;
}

int main(){
	std::vector<std::pair<int, int>> st_fn;
	int start_fin [6][2] = {{1,2},{0,6},{3,4},{5,7},{8,9},{5,9}};

	for(int i = 0; i < 6; i++){
		st_fn.push_back(std::make_pair(start_fin[i][0], start_fin[i][1]));
	}

	// sor by the second element
	sort(st_fn.begin(), st_fn.end(), sort_by_sec);

	int st = st_fn[0].second;
	int diff, count = 1;
	for(int i = 0; i < 5; i++){
		diff = st_fn[i+1].first - st;
		// std::cout <<st_fn[i+1].first << "|" << st << ":" << diff << "\n";
		if(diff >= 0){
			count +=1;
			st = st_fn[i+1].second;
		}
		else{
			//this is equivalent to an if statement
			while(st_fn[i+1].first - st < 0 && i < 4){
				// i+=1;
				break;
			}
		}
	}
	std::cout << count;
	return 0;
}
