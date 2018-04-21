/*
Shiv's implementation for S-AES code
*/
#include <bits/stdc++.h>
#include <bitset>
std::map<std::string, std::string> Sbox = {{"0000", "1001"}, {"0001", "0100"}, {"0010", "1010"},
											{"0011", "1011"}, {"0100", "1101"}, {"0101", "0001"},
											{"0110", "1000"}, {"0111", "0101"}, {"1000", "0110"},
											{"1001", "0010"}, {"1010", "0000"}, {"1011", "0011"},
											{"1100", "1100"}, {"1101", "1110"}, {"1110", "1111"},
											{"1111", "0111"}};
// A vector containing keys
std::vector<std::string> keys;
std::string XOR(std::string s1, std::string s2){
	for(int i =0; i < s1.length(); i++){
		if(s1.at(i) == s2.at(i)){
			s1[i] = '0';
		}
		else{
			s1[i] = '1';
		}
	}

	return s1;
}

std::string SubNib(std::string s){
	return Sbox[s.substr(0,4)]+Sbox[s.substr(4,4)];
}

std::string RotNib(std::string s){
	return s.substr(4,8)+s.substr(0,4);
}

std::vector<std::string> generate_key(std::string key0){
	std::vector<std::string> answer;
	std::string temp, w0, w1,w2,w3,w4,w5;
	answer.push_back(key0);
	std::cout << "key0: " << key0 << "\n"; 

	w0 = key0.substr(0,8);
	w1 = key0.substr(8,8);

	w2 = XOR(w0, XOR("10000000", SubNib(RotNib(w1))));
	
	w3 = XOR(w2,w1);
	std::cout << "w2: " << w2 << " |w3: " << w3 << "\nkey1:"<< w2+w3 << "\n";

	// push key1
	answer.push_back(w2+w3);

	w4 = XOR(w2, XOR("00110000", SubNib(RotNib(w3))));
	
	w5 = XOR(w3,w4);
	std::cout << "w4: " << w4 << " |w5: " << w5 << "\nkey2:"<< w4+w5 << "\n";

	// push key2
	answer.push_back(w4+w5);

	return answer;
}

int to_dec(std::string s){
	int ans = 0, p = 0;
	for(int i = s.length(); i >0; i--){
		if(s.at(i-1) == '1')
		{		
			ans+= std::pow(2,p);	
		}
		p++;
	}
	// std::cout << "\n";
	return ans;
}

std::string reduce(std::string dividend){
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
	// std::cout << temp.substr(temp.length()-4, temp.length()) << "\n";
	return temp.substr(temp.length()-4, temp.length());
}

std::string matrix(std::string e1, std::string e2, int a, int b){
	std::string answer = "", t1, t2;
	int t = to_dec(e1), f = to_dec(e2);
	a = t*a;
	b = f*b;

	if(a > 15){
		t1 = reduce(std::bitset< 6 >(a).to_string());

	}
	else{
		t1 = std::bitset< 4 >(a).to_string();
	}

	if(b > 15){
		t2 = reduce(std::bitset< 6 >(b).to_string());
	}
	else{
		t2 = std::bitset< 4 >(b).to_string();
	}

	answer = XOR(t1, t2);
	// std::cout << answer << "\n"; 

	return answer;
}

std::string encrypt(std::string s){
	std::string add_round_key = XOR(keys[0], s);
	std::cout << "After add round key 1: " << add_round_key << "\n";
	add_round_key = SubNib(add_round_key.substr(0,8)) + SubNib(add_round_key.substr(8,8));
	std::cout << "After S-box substitution: " << add_round_key << "\n";
	add_round_key = add_round_key.substr(0,4)+add_round_key.substr(12,4)+add_round_key.substr(8,4)+add_round_key.substr(4,4);
	std::cout << "After swapping 2nd and 4th nibble: " << add_round_key << "\n";

	// beginning Matrix multiplication
	std::string s00= add_round_key.substr(0,4), s01= add_round_key.substr(4,4), s10= add_round_key.substr(8,4), s11= add_round_key.substr(12,4);
	// std::cout <<to_dec(s00) << "|eu" << to_dec(s01) << ":" << s01 << "haha";
	std::string s00_ = matrix(s00, s10, 1, 4), s10_ = matrix(s00, s10, 4, 1), s01_ = matrix(s10, s11, 1, 4), s11_ = matrix(s10, s11, 4, 1);
	std::cout << "After matrix multiplication:\n";
	std::cout << "s00' : " << s00_ << "\ns01' : " << s01_ << "\ns10' : " << s10_ << "\ns11' : " << s11_ << "\n";
	std::string out1 = s00_+s10_+s01_+s11_;
	std::cout << "output round 1: " << out1 << "\n";

	// round 2
	add_round_key = XOR(keys[1], out1);
	std::cout << "After add round key 2: " << add_round_key << "\n";
	add_round_key = SubNib(add_round_key.substr(0,8)) + SubNib(add_round_key.substr(8,8));
	std::cout << "After S-box substitution: " << add_round_key << "\n";
	add_round_key = add_round_key.substr(0,4)+add_round_key.substr(12,4)+add_round_key.substr(8,4)+add_round_key.substr(4,4);
	std::cout << "After swapping 2nd and 4th nibble: " << add_round_key << "\n";

	add_round_key = XOR(keys[2], add_round_key);
	std::cout << "After add round key 3: " << add_round_key << "\n";
	
	return add_round_key;
}

std::string decrypt(std::string s){
	std::string add_round_key = XOR(keys[2], s);
	std::cout << "After add round key 3: " << add_round_key << "\n";
	add_round_key = SubNib(add_round_key.substr(0,8)) + SubNib(add_round_key.substr(8,8));
	std::cout << "After S-box substitution: " << add_round_key << "\n";
	add_round_key = add_round_key.substr(0,4)+add_round_key.substr(12,4)+add_round_key.substr(8,4)+add_round_key.substr(4,4);
	std::cout << "After swapping 2nd and 4th nibble: " << add_round_key << "\n";

	// beginning Matrix multiplication
	std::string s00= add_round_key.substr(0,4), s01= add_round_key.substr(4,4), s10= add_round_key.substr(8,4), s11= add_round_key.substr(12,4);
	// std::cout <<to_dec(s00) << "|eu" << to_dec(s01) << ":" << s01 << "haha";
	std::string s00_ = matrix(s00, s10, 9, 2), s10_ = matrix(s00, s10, 2, 9), s01_ = matrix(s10, s11, 9, 2), s11_ = matrix(s10, s11, 2, 9);
	std::cout << "After matrix multiplication:\n";
	std::cout << "s00' : " << s00_ << "\ns01' : " << s01_ << "\ns10' : " << s10_ << "\ns11' : " << s11_ << "\n";
	std::string out1 = s00_+s10_+s01_+s11_;
	std::cout << "output round 1: " << out1 << "\n";

	// round 2
	add_round_key = XOR(keys[1], out1);
	std::cout << "After add round key 2: " << add_round_key << "\n";
	add_round_key = SubNib(add_round_key.substr(0,8)) + SubNib(add_round_key.substr(8,8));
	std::cout << "After S-box substitution: " << add_round_key << "\n";
	add_round_key = add_round_key.substr(0,4)+add_round_key.substr(12,4)+add_round_key.substr(8,4)+add_round_key.substr(4,4);
	std::cout << "After swapping 2nd and 4th nibble: " << add_round_key << "\n";

	add_round_key = XOR(keys[0], add_round_key);
	std::cout << "After add round key 1: " << add_round_key << "\n";
	
	return add_round_key;
}

int main(){
	std::string key, plaintext, cipher;
	key = "0100101011110101";
	plaintext = "1101011100101000";

	std::cout << "Key generation shall now begin: \n";
	// A vector containing keys
	keys = generate_key(key);

	std::cout << "Encryption will now begin: \n";

	cipher = encrypt(plaintext);
	std::cout << "Encrypted text is: " << cipher << "\n";

	std::cout << "\n--------------------------------\nDecryption will now begin: \n";

	cipher = decrypt(cipher);
	std::cout << "decrypted text is: " << cipher << "\n";
	return 0;
}