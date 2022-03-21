// #include<bits/stdc++.h>
#include<iostream>
using namespace std;

/*
ip.txt
3
line 1
line 2
line 3

op.txt
line 1
line 2
line 3

*/

int main(){
    int num_lines;
    cin >> num_lines;
    cin.ignore(); // Yay this works!
    for(int i = 0; i < num_lines; i++){
        string s;
        getline(cin, s);
        cout << s << endl;
    }
    return 0;
}