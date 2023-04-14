#include <bits/stdc++.h>
#include <set>
using namespace std;

int main(){
    set<int> s;
    s.insert(10);
    s.insert(5);
    s.insert(20);
    for(int i :  s){
        cout << i << " ";
    }cout << endl;

    set<int, greater<int>> s1; // for Decreasing order
    s1.insert(10);
    s1.insert(5);
    s1.insert(20);
    for(auto it = s1.begin(); it!= s1.end();it++){
        cout << (*it) << " ";
    }cout << endl;
}