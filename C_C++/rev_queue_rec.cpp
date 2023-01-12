#include <bits/stdc++.h>
#include <queue>
using namespace std;

void Print(queue<int> &q){
    while(!q.empty()){
        cout << q.front() << " ";
        q.pop();
    }
}

void reverse(queue<int> &q){
    if(q.empty())
        return;

    int x = q.front();
    q.pop();

    reverse(q);
    q.push(x);
}

int main(){
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);
    q.push(40);

    reverse(q);
    Print(q);
}