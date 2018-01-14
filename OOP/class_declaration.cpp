/*CPP class declaration code*/
#include <bits/stdc++.h>

class parent{
public:
	int variable;

	parent(){
		std::cout << "parent initialized haha\n";
	}

	int addition(int a, int b){
		return (a+b);
	}

	void access_variable(int b){
		variable = b;
		std::cout << variable << "\n";
	}
};

int main(){

	parent p;
	std::cout << p.addition(1, 6) << "\n";
	p.access_variable(4);

}