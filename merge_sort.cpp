/*
A standard divide and conquer algorithm for mergesort

input format
============
12 11 13 5 6 7
==============
*/
#include <bits/stdc++.h>
std::vector<int> v, answer;

std::vector<int> merge(std::vector<int> low, std::vector<int> high){
	std::vector<int> l, ret;
	while(!low.empty() && !high.empty()){
		if(low[0] < high[0]){
			l.push_back(low[0]);
			low.erase(low.begin());
		}
		else{
			l.push_back(high[0]);
			high.erase(high.begin());
		}
	}
	ret.reserve(l.size() + low.size() + high.size());
	ret.insert(ret.end(), l.begin(), l.end());
	ret.insert(ret.end(), low.begin(), low.end());
	ret.insert(ret.end(), high.begin(), high.end());
	return ret;
}

std::vector<int> mergesort(int l, int h){
	std::vector<int> low;
	std::vector<int> high;
	int mid = (l+h)/2;
	if (l < h){
		low = mergesort(l, mid);
		high = mergesort(mid+1, h);
		return merge(low, high);
	}
	return {v[l]};
}

int main(){
	int temp;
	for(int i = 0; i<6; i++){
		std::cin >> temp;
		v.push_back(temp);
	}

	answer = mergesort(0, 5);
	for(int i = 0; i < 6; i++){
		std::cout << answer[i] << " "; 
	}
	return 0;
}