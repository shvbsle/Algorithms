/*
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
So a string of length n has 2^n different possible subsequences.

A Dynamic Programming Problem

Input Format
-------------
ABCDGH
AEDFHR
-------------

LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

another:
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

-----------------------------------------------------------------------

This was a pain in the ass man. maps in C++ automatically initialize to 0 for new value

hence I had to initialize actual 0 values to -1 so that 0 values in the map aren't confused with 
uncomputed values.

This bitch is tabulated
*/
#include <bits/stdc++.h>
#include <exception>

std::map<std::pair<std::string, std::string>, int> memory;

int Dynamic_solve(std::string s1, std::string s2){
	if(s1.length() < 1 || s2.length() < 1){
		memory[std::make_pair(s1,s2)] = -1;
		return 0;
	}
	if((s1.length() == 1 || s2.length() ==1) && s1.at(s1.length()-1) == s2.at(s2.length()-1)){
		memory[std::make_pair(s1,s2)] = 1;
		return memory[{s1,s2}];
	}
	if(s1.at(s1.length()-1) == s2.at(s2.length()-1)){
		if(memory[{s1,s2}] != 0){
			return (memory[{s1,s2}] == -1)?(0):(memory[{s1,s2}]);	
		}
		else{
			memory[std::make_pair(s1,s2)] = 1 + Dynamic_solve(s1.substr(0,s1.length()-1),s2.substr(0,s2.length()-1) );
			return (memory[{s1,s2}] == -1)?(0):(memory[{s1,s2}]);	
		}			
	}
	else{
		if(memory[{s1,s2}] != 0){
			return (memory[{s1,s2}] == -1)?(0):(memory[{s1,s2}]);	
		}
		else{
			memory[std::make_pair(s1,s2)] = std::max(Dynamic_solve(s1.substr(0,s1.length()-1),s2), Dynamic_solve(s1,s2.substr(0,s2.length()-1)));
			return (memory[{s1,s2}] == -1)?(0):(memory[{s1,s2}]);	
		}

	}
}

int main(){
	std::string s1,s2;
	std::cin >> s1;
	std::cin >> s2;

	std::cout << Dynamic_solve(s1,s2);

	return 0;
}