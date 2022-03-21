#include</Users/shivjeet.bhosale/stdc++.h>
using namespace std;

int main(){
	string s;
	cin >> s;
		
	// say we wanna add 1 to last digit then we simple extract the number 
	// from the string and convert it to ascii
	
	int last_digit = (int)(s[s.size()-1] - '0');
	last_digit = last_digit + 6;
	
	s[s.size() - 1] = ((char) last_digit) + '0'; 

	cout << s;
	return 0;
}