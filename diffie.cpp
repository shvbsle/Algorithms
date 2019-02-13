/*
SHIV's code for Diffie Hellman key exchange
*/
#include <bits/stdc++.h>

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

int main()
{
	long long int P, pr, Xa, Xb, Ya, Yb, K1, K2;
	std::cout << "Enter a prime number P: ";
	std::cin >> P;

	std::cout << "Enter primitive root for P: ";
	std::cin >> pr;

	std::cout << "Enter Xa for Shiv: ";
	std::cin >> Xa;

	Ya = ModPow(pr, Xa, P);
	std::cout << "Ya is: " << Ya << "\n";

	std::cout << "Enter Xb for Batman: ";
	std::cin >> Xb;

	Yb = ModPow(pr, Xb, P);
	std::cout << "Yb is: " << Yb << "\n";

	std::cout << "\nValidating key exchange:\n";
	K1 = ModPow(Yb, Xa, P);
	std::cout << "Key on Shiv's side: " << K1 << "\n\n";

	K2 = ModPow(Ya, Xb, P);
	std::cout << "Key on Batman's side: " << K2 <<  "\n";


    return 0;
}
