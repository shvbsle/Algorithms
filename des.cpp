/*
SHIV bhau ka code for S-DES
*/
#include <bits/stdc++.h>
// here are my globals n keys and what not:

std::map<int, int> p10 = {{1,3}, {2,5}, {3,2}, {4,7}, {5,4}, {6,10}, {7,1}, {8,9}, {9,8}, {10,6}};
std::map<int, int> p8 = {{1,6}, {2,3}, {3,7}, {4,4}, {5,8}, {6,5}, {7, 10}, {8, 9}};
std::map<int, int> ip = {{1,2}, {2,6}, {3,3}, {4,1}, {5,4}, {6,8}, {7,5}, {8,7}};
std::map<int, int> ip_i = {{1,4}, {2,1}, {3,3}, {4,5}, {5,7}, {6,2}, {7,8}, {8, 6}};
std::map<int, int> EP = {{1,4}, {2,1}, {3,2}, {4,3}, {5,2}, {6,3}, {7,4}, {8,1}};
std::map<int, int> p4 = {{1,2}, {2,3}, {3,4}, {4,1}};
// this is because I'm too lazy to do convert string to binary
std::map<std::string, int> bin_vals = {{"00", 0}, {"01", 1}, {"10", 2}, {"11", 3}};
// them s-boxes
std::string s0[4][4] = {{"01","00","11","10"},
				{"11","10","01","00"},
				{"00","10","01","11"},
				{"11","01","11","10"}};

std::string s1[4][4] = {{"00","01","10","11"},
				{"10","00","01","11"},
				{"11","00","01","00"},
				{"10","01","00","11"}};

// global keys that I have to generate
std::pair<std::string, std::string> keys;
std::pair<std::string, std::string> temp_keys;
// key generation function
std::pair<std::string, std::string> generate_keys(std::string key_str){
	std::pair<std::string, std::string> answer;
	std::string temp = "0000000000";
	// bitset the key boi
	// std::bitset<10> key(key_str), temp("0000000000");
	for(int i = 0 ; i < key_str.length(); i++){
		temp[i] = key_str.at(p10[i+1]-1);
	}
	std::cout << "After P10: "<< temp << "\n";
	std::string r = temp.substr(0,5);
	std::string l = temp.substr(5,9);
	// LS-1
	r = r.substr(1,5) + r.substr(0,1);
	l = l.substr(1,5) + l.substr(0,1);

	std::cout <<"After LS1: " << r << "|" << l << "\n";
	std::string t2 = r+l, k1 = r+l;
	for(int i = 0; i< 8; i++){
		k1[i] = t2.at(p8[i+1]-1);
	}
	// std::cout << k1;
	std::cout << "After P8: " << k1 << "\n"; 

	// LS-2
	r = r.substr(1,5) + r.substr(0,1);
	l = l.substr(1,5) + l.substr(0,1);
	r = r.substr(1,5) + r.substr(0,1);
	l = l.substr(1,5) + l.substr(0,1);
	std::cout <<"After LS2: "<< r << "|" << l << "\n";
	std::string k2 = r+l;
	t2 = r+l;
	for(int i = 0; i< 8; i++){
		k2[i] = t2.at(p8[i+1]-1);
	}
	std::cout << "After P8: " << k2 << "\n";

	std::cout <<"Keys are:" << k1.substr(0,8) << ", " << k2.substr(0,8) << "\n";
	answer.first = k1.substr(0,8);
	answer.second = k2.substr(0,8);
	return answer;
}

std::string encrypt(std::string plaintext){
	std::string answer="00000000", temp = plaintext, l, r;

	for(int i = 0 ; i < plaintext.length(); i++){
		temp[i] = plaintext.at(ip[i+1]-1);
	}
	std::cout <<"After IP:"<< temp <<"\n";
	l = temp.substr(0,4);
	r = temp.substr(4,8);

	for(int i = 0 ; i < r.length()*2; i++){
		temp[i] = r.at(EP[i+1]-1);
	}
	std::cout << "After EP: " << temp << "\n";
	//xor with K1
	for(int i =0; i < 8; i++){
		if(temp.at(i) == keys.first.at(i)){
			temp[i] = '0';
		}
		else{
			temp[i] = '1';
		}
	}
	std::cout <<"After XOR with K1: " << temp << "\n";

	// S0 value
	std::string row,col, t1, t2;
	row.push_back(temp[0]);
	row.push_back(temp[3]);
	col.push_back(temp[1]);
	col.push_back(temp[2]);// = temp[1]+temp[2];
	std::cout <<"S0 value:" << row << " | " << col << "\n";
	t1 = s0[bin_vals[row]][bin_vals[col]];

	// S1 value
	row = "", col = "";	
	row.push_back(temp[4]);
	row.push_back(temp[7]);
	col.push_back(temp[5]);
	col.push_back(temp[6]);// = temp[1]+temp[2];
	std::cout <<"S1 value: "<< row << " | " << col << "\n";
	t2 = s1[bin_vals[row]][bin_vals[col]];
	// std::cout << t1 << "|" << t2 << "\n"; 
	t1 = t1+t2;
	t2 = "0000";
	for(int i = 0 ; i < 4; i++){
		t2[i] = t1.at(p4[i+1]-1);
	}
	std::cout <<"After P4: " <<  t2 << "\n";
	// std::cout << l << "\n";
	//xor with r
	for(int i =0; i < 4; i++){
		if(t2.at(i) == l.at(i)){
			t2[i] = '0';
		}
		else{
			t2[i] = '1';
		}
	}
	std::cout << "XOR with r:" << t2 << "\n";
	// l = r;
	// r = t1;

	// round 2:
	// l = temp.substr(0,4);
	// r = temp.substr(4,8);
	std::cout << "After Swap: "<< r+t2 << "\n";
	temp = r+t2;
	std::string random_temp = temp;

	std::string r_temp = temp.substr(4,8);

	for(int i = 0 ; i < 8; i++){
		temp[i] = r_temp.at(EP[i+1]-1);
	}
	std::cout << "After EP: " << temp << "\n";
	//xor with K1
	for(int i =0; i < 8; i++){
		if(temp.at(i) == keys.second.at(i)){
			temp[i] = '0';
		}
		else{
			temp[i] = '1';
		}
	}
	std::cout <<"Round 2: XOR with K2: "<< temp << "\n";

	// S0 value
	row = col = t1 = t2 = "";
	row.push_back(temp[0]);
	row.push_back(temp[3]);
	col.push_back(temp[1]);
	col.push_back(temp[2]);// = temp[1]+temp[2];
	std::cout <<"S0 value: " << row << " | " << col << "\n";
	t1 = s0[bin_vals[row]][bin_vals[col]];

	// S1 value
	row = "", col = "";	
	row.push_back(temp[4]);
	row.push_back(temp[7]);
	col.push_back(temp[5]);
	col.push_back(temp[6]);// = temp[1]+temp[2];
	std::cout <<"S1 value: " <<row << " | " << col << "\n";
	t2 = s1[bin_vals[row]][bin_vals[col]];
	// std::cout << t1 << "|" << t2 << "\n"; 
	t1 = t1+t2;
	std::cout << "this is t1:" << t1;
	t2 = "0000";
	for(int i = 0 ; i < 4; i++){
		t2[i] = t1.at(p4[i+1]-1);
	}
	std::cout <<"\nAfter P4: " << t2 << "\n";

	//xor with l
	l = random_temp.substr(0,4);
	for(int i =0; i < 4; i++){
		if(t2.at(i) == l.at(i)){
			t2[i] = '0';
		}
		else{
			t2[i] = '1';
		}
	}

	std::cout <<"After xor with l: " << t2 << "\n";
	r = random_temp.substr(4,8);
	std::string temp2 = t2+r;
	// std::cout << temp2 << "\n";

	for(int i = 0 ; i < 8; i++){
		answer[i] = temp2.at(ip_i[i+1]-1);
	}
	std::cout << "After IP^-1: "<<answer<< "\n";

	return answer;
}

std::string poly_bound(std::string dividend){
	std::string divisor = "10011", temp = "00000";
	int diff = dividend.length() - divisor.length();
	for(int i = diff; i >= 0; i--){
		temp = "00000";
		std::string r = dividend.substr(0, 5), l = dividend.substr(5, dividend.length());
		for(int j = 0; j < 5; j++){
			if(divisor.at(j) == r.at(j)){
				temp[j] = '0';
			}
			else{
				temp[j] = '1';
			}
		}
		dividend = temp.substr(1,temp.length()) + l;
	}
	return temp.substr(temp.length()-4, temp.length());
}

int main(){
	std::string key_str = "0010010111", plaintext;
	// this function will generate them keys biatch!
	std::cout << "Original key: " << key_str << "\nKey generation wil now begin:\n";
	keys = generate_keys(key_str);

	std::cout << "Enter plaintext (8 bits): ";
	// plaintext = "10100101";
	std::cin >> plaintext;
	std::cout << "plaintext is: " << plaintext << "\n";
	std::cout << "\n----------Encryption---------\n";
	std::cout << "beginning encryption: \n";
	std::string cipher = encrypt(plaintext);
	std::cout << "encrypted text is: " << cipher << "\n";
	std::string tkey;
	tkey = keys.first;
	keys.first = keys.second;
	keys.second = tkey;
	std::cout << "\n----------Decryption---------\n";
	tkey = encrypt(cipher);
	std::cout << "decrypted text is: " << tkey;
	// std::cin >> temp;
	// // create a bitset of plaintext
	// std::bitset<8> PT(temp);
	// std::cout << poly_bound("111000");



	return 0;
}
