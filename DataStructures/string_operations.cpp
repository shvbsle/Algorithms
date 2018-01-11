/*
here are my implementations of various string operatios
*/
#include <iostream>
#include <string>

int main(){

	char *str = "hahaha", str2[10] = {'O', 'h', ' ', 'g', 'o', 'd', '!', '\0'};
	std::string str3 = "hello world\n";

	// this is the normal method
	std::cout << str3 << "\n";
	// This is bad. Not recommended
	std::cout << str << "\n";

	// cool and good
	std::cout << str2 << "\n";



	return 0;
}