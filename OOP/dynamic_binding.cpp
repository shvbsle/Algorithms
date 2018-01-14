/*
example code for dynamic binding in CPP
*/
#include <bits/stdc++.h>

class base{
public:
	virtual void hello(){
		std::cout << "in base\n";
	}
};

class derived:public base{
public:
	void hello(){
		std::cout << "in derived\n";
	}
};

int main(){

	// scary
	// for c or cpp, access an attribute of a pointer type variable by "->"" and not '.'
	base *b = new derived;
	b->hello();
	return 0;
}