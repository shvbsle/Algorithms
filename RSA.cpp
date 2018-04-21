/*
SHIV's code for RSA n what not in cpp
*/
#include <bits/stdc++.h>

// mod pow function 
int ModPow(int x, int y, int p)
{
	int res = 1;
	x = x % p;
	while (y > 0)
	{
	if ((y & 1) == 1){
		res = (res*x) % p;
		std::cout << res << " = " <<(res*x) <<  " mod(" << p << ")\n";
	}
	y = y>>1;
	x = (x*x) % p;
	}

	return res;
}

// Mod inverse
int ModInverse(int iNum1, int iNum2)
{
	iNum1 = iNum1%iNum2;
	for (int i=1; i < iNum2; i++)
		if ((iNum1*i) % iNum2 == 1)
			return i;
	return 0;
}

#include <bits/stdc++.h>

int main(){
	int M, P, Q, E, N, phi, C, D;
	std::cout << "Enter some message (int): ";
	std::cin >> M;
	std::cout << "\nP value: ";
	std::cin >> P;
	std::cout << "\nQ value: ";
	std::cin >> Q;
	std::cout << "\nE value: ";
	std::cin >> E;

	// N and phi
	N = P*Q;
	phi = (P-1)*(Q-1);

	std::cout << "\nN: " << N << " and phi: " << phi << "\n";

	std::cout << "beginning encryption: \n";
	C = ModPow(M,E,N);
	std::cout << "Encrypted text is: " << C << "\n";

	std::cout << "beginning decryption: \n";

	D = ModInverse(E, phi);

	std::cout << "D is: " << D << "\n";

	M = ModPow(C, D, N);

	std::cout << "Decrypted value is: " << M << "\n";




	return 0;
}