#include</Users/shivjeet.bhosale/stdc++.h>
using namespace std;

int main(){
    pair<string, int> p;

    // way 1
    p = make_pair("shiv", 25);

    // way 2
    // doestn seem to work in my mac
    // p = {"shiv", 25};

    // way 1
    // pair<string, int> pcopy = p; // this code will pass by copy

    // way 2
    pair<string, int> &pcopy = p; // this code will pass by reference
    // dont use any mental logic for this
    // get used to this
    // dont fall for cognitive hypocrisy. `&` will always come on left side and will become reference

    pcopy = make_pair("shiv2", 25);



    cout << p.first << " " << p.second << endl;
    return 0;
}