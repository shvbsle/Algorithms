// #include<bits/stdc++.h> // Have moved to elsewhere
#include</Users/shivjeet.bhosale/stdc++.h>

using namespace std;

int main(){
    string ip;
    getline(cin, ip);
    int iter_len;
    if(ip.size()%2 == 0){
        iter_len = (int)(ip.size()/2);
    }
    else{
        iter_len = (int)((ip.size()/2) + 1);
    }
    int is_pal = 0;
    for(int i = 0; i< iter_len; i++){
        if(ip[i] != ip[ip.size()-1-i]){
            is_pal = 1;
        }
    }
    if(is_pal == 1){
        cout << "NO";
    }else{
        cout << "YES";
    }

    return 0;
}